# src/plot_substations.py
import os
import warnings
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

warnings.filterwarnings("ignore", category=UserWarning)

# =========================
# CONFIG
# =========================
# Arquivos de entrada (troque para seus caminhos/URLs locais)
PATH_ONS = "data/ons_substations.geojson"          # pontos com lon/lat, capacidade,

# Bloco para converter o Shapefile da EPE para GeoJSON (só precisa rodar uma vez)
try:
    if not os.path.exists("data/epe_substations.geojson"):
        if os.path.exists("data/epe_substations/Subestações_-_Base_Existente.shp"):
            print("Convertendo Shapefile EPE para GeoJSON...")
            gdf_epe_shp = gpd.read_file("data/epe_substations/Subestações_-_Base_Existente.shp")
            gdf_epe_shp.to_file("data/epe_substations.geojson", driver="GeoJSON")
            print("Conversão concluída.")
        else:
            print("Aviso: Shapefile da EPE não encontrado, pulando conversão.")
except Exception as e:
    print(f"Aviso: Falha ao converter Shapefile EPE: {e}")


PATH_EPE = "data/epe_substations.geojson"          # idem
PATH_REGIOES = "data/regions/BR_Regioes_2024.shp"       # polígonos: N, NE, CO, SE, S (coluna 'REGIAO' ou similar)
PATH_LINHAS_TX = "data/linhas_transmissao.geojson" # opcional; se não existir, o script ignora

# Nomes de colunas esperadas nas camadas ONS/EPE
COL_LON = "lon"
COL_LAT = "lat"
COL_CAP = "capacidade_mva"     # capacidade instalada MVA
COL_CAP_OP = "cap_operacional_mva"  # opcional; se não existir, será assumida igual à instalada
COL_KV = "tensao_kv"           # nível de tensão em kV
COL_NOME = "nome"              # nome da subestação (opcional)

# CRS
CRS_GEO = "EPSG:4674"   # SIRGAS 2000 (geográfico) para referência
CRS_AREA = "EPSG:5880"  # SIRGAS 2000 / Brazil Polyconic, adequado para área km²

# Saída
OUT_PNG = "data/mapa_subestacoes.png"

# =========================
# Funções utilitárias
# =========================
def read_points_layer(path_or_url: str) -> gpd.GeoDataFrame:
    """
    Lê uma camada de pontos. Aceita:
    - GeoPackage/GeoJSON/Parquet com geometria já pronta, OU
    - CSV/Parquet com colunas lon/lat -> cria geometria.
    Normaliza colunas esperadas.
    """
    if not os.path.exists(path_or_url) and not str(path_or_url).startswith(("http://", "https://")):
        raise FileNotFoundError(f"Arquivo não encontrado: {path_or_url}")

    ext = os.path.splitext(path_or_url)[-1].lower()

    if ext in [".csv"]:
        df = pd.read_csv(path_or_url)
        if COL_LON not in df.columns or COL_LAT not in df.columns:
            raise ValueError(f"CSV precisa ter colunas {COL_LON} e {COL_LAT}.")
        gdf = gpd.GeoDataFrame(
            df,
            geometry=gpd.points_from_xy(df[COL_LON], df[COL_LAT]),
            crs="EPSG:4326",  # assume WGS84, ajustaremos para SIRGAS em seguida
        )
    else:
        gdf = gpd.read_file(path_or_url)

    # Se geometria não existir mas lon/lat existirem
    if "geometry" not in gdf.columns and COL_LON in gdf.columns and COL_LAT in gdf.columns:
        gdf = gpd.GeoDataFrame(
            gdf,
            geometry=gpd.points_from_xy(gdf[COL_LON], gdf[COL_LAT]),
            crs="EPSG:4326",
        )

    # Ajusta CRS para SIRGAS 2000
    if gdf.crs is None:
        # tenta inferir que veio em WGS84
        gdf.set_crs("EPSG:4326", inplace=True)
    gdf = gdf.to_crs(CRS_GEO)

    # Garante campos-chave
    for c in [COL_CAP, COL_KV]:
        if c not in gdf.columns:
            gdf[c] = None
    if COL_CAP_OP not in gdf.columns:
        gdf[COL_CAP_OP] = gdf[COL_CAP]

    # Limpa tipos numéricos
    for c in [COL_CAP, COL_CAP_OP, COL_KV]:
        gdf[c] = pd.to_numeric(gdf[c], errors="coerce")

    # Nome opcional
    if COL_NOME not in gdf.columns:
        gdf[COL_NOME] = None

    return gdf


def minmax_norm(values: pd.Series) -> pd.Series:
    """Normalização min-max, robusta e sempre retornando Series com o mesmo index."""
    # Garante Series com mesmo índice de 'values'
    s = pd.Series(pd.to_numeric(values, errors="coerce"), index=getattr(values, "index", None))
    vmin = s.min(skipna=True)
    vmax = s.max(skipna=True)
    if pd.isna(vmin) or pd.isna(vmax) or vmin == vmax:
        # Retorna zeros preservando o index
        return pd.Series(0.0, index=s.index)
    return (s - vmin) / (vmax - vmin)


def classify_voltage(kv: pd.Series) -> pd.Series:
    """Classes discretas de tensão para visualização."""
    kv_num = pd.Series(pd.to_numeric(kv, errors="coerce"), index=kv.index)
    bins = [-1, 69, 138, 230, 440, 10000]
    labels = ["< 69 kV", "69–138 kV", "138–230 kV", "230–440 kV", ">= 440 kV"]
    return pd.cut(kv_num, bins=bins, labels=labels)


def availability_percentage(cap_op: pd.Series, cap_inst: pd.Series) -> pd.Series:
    """Disponibilidade percentual = cap_operacional / cap_instalada * 100 (sempre Series)."""
    op = pd.Series(pd.to_numeric(cap_op, errors="coerce"), index=cap_op.index)
    inst = pd.Series(pd.to_numeric(cap_inst, errors="coerce"), index=cap_inst.index)

    # Executa a divisão
    pct = (op / inst) * 100

    # Substitui manualmente valores infinitos (positivos ou negativos) por NaN
    # Isso acontece se inst=0 e op!=0
    pct = pct.replace([float('inf'), float('-inf')], float('nan'))

    return pct  # manter como Series; NaN quando faltar dado


def availability_bucket(pct: pd.Series) -> pd.Series:
    """
    Categoriza disponibilidade:
    Alta: > 80%
    Média: 50–80%
    Baixa: < 50%
    """
    def _lab(v):
        if pd.isna(v):
            return "Indefinida"
        if v > 80:
            return "Alta"
        if v >= 50:
            return "Média"
        return "Baixa"
    return pct.apply(_lab)


def safe_read_regions(path_or_url: str) -> gpd.GeoDataFrame:
    gdf = gpd.read_file(path_or_url)
    if gdf.crs is None:
        gdf.set_crs(CRS_GEO, inplace=True)
    else:
        gdf = gdf.to_crs(CRS_GEO)
    # Normaliza nome de região
    # Tenta achar uma coluna com nome de região
    col_reg = None
    for c in gdf.columns:
        if any(k in c.lower() for k in ["reg", "macro", "nome", "name"]):
            col_reg = c
            break
    if col_reg is None:
        raise ValueError("Camada de regiões sem coluna de nome identificável.")
    gdf["REGIAO_NOME"] = gdf[col_reg].astype(str).str.upper().str.strip()
    return gdf[["REGIAO_NOME", "geometry"]].copy()


def overlay_region(points: gpd.GeoDataFrame, regions: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """Atribui a cada subestação sua região por overlay espacial."""
    pts = points.sjoin(regions, how="left", predicate="within")
    pts = pts.drop(columns=[c for c in pts.columns if c.startswith("index_right")], errors="ignore")
    # Devolve explicitamente como GeoDataFrame para sossegar o type checker
    return gpd.GeoDataFrame(pts, geometry="geometry", crs=points.crs)


def compute_region_metrics(points: gpd.GeoDataFrame, regions: gpd.GeoDataFrame) -> pd.DataFrame:
    """
    Agrupa por região:
    - densidade de subestações por km²
    - capacidade média instalada (MVA)
    - disponibilidade média (%)
    """
    # Área km² por região em projeção apropriada
    reg_proj = regions.to_crs(CRS_AREA).copy()
    reg_proj["area_km2"] = reg_proj.geometry.area / 1_000_000.0
    reg = reg_proj[["REGIAO_NOME", "area_km2"]].copy()

    # Agregações por região
    grp = points.groupby("REGIAO_NOME", dropna=False).agg(
        qtd_subestacoes=("geometry", "count"),
        cap_inst_media_mva=(COL_CAP, "mean"),
        disponibilidade_media_pct=("disponibilidade_pct", "mean"),
    )
    grp = grp.reset_index()

    # Junta área e calcula densidade
    met = grp.merge(reg, on="REGIAO_NOME", how="left")
    met["densidade_sub_km2"] = met["qtd_subestacoes"] / met["area_km2"]
    return met


def try_read_lines(path: str) -> gpd.GeoDataFrame | None:
    try:
        if os.path.exists(path) or str(path).startswith(("http://", "https://")):
            gdf = gpd.read_file(path)
            if gdf.crs is None:
                gdf.set_crs(CRS_GEO, inplace=True)
            else:
                gdf = gdf.to_crs(CRS_GEO)
            return gdf
    except Exception:
        return None
    return None


# =========================
# Pipeline
# =========================
def main():
    # 1) EXTRAÇÃO E LIMPEZA
    try:
        gdf_ons = read_points_layer(PATH_ONS)
        gdf_epe = read_points_layer(PATH_EPE)
    except FileNotFoundError as e:
        print(f"Erro fatal: Arquivo de dados de entrada não encontrado.")
        print(f"Detalhe: {e}")
        print("\nVerifique se os caminhos PATH_ONS e PATH_EPE estão corretos no script.")
        return # Para a execução
    except Exception as e:
        print(f"Erro inesperado ao ler os dados: {e}")
        return

    # Identificador da fonte
    gdf_ons["fonte"] = "ONS"
    gdf_epe["fonte"] = "EPE"

    # União das bases ONS + EPE
    gdf_raw = pd.concat([gdf_ons, gdf_epe], ignore_index=True)
    gdf_raw = gpd.GeoDataFrame(gdf_raw, geometry="geometry", crs=CRS_GEO)

    # Normalização das variáveis (MVA e kV)
    gdf_raw["cap_norm_0_1"] = minmax_norm(gdf_raw[COL_CAP])
    gdf_raw["kv_norm_0_1"] = minmax_norm(gdf_raw[COL_KV])

    # Disponibilidade percentual e bucket
    gdf_raw["disponibilidade_pct"] = availability_percentage(gdf_raw[COL_CAP_OP], gdf_raw[COL_CAP])
    gdf_raw["disp_cat"] = availability_bucket(gdf_raw["disponibilidade_pct"])

    # Classificação por classe de tensão (para visual)
    gdf_raw["classe_kv"] = classify_voltage(gdf_raw[COL_KV])

    # 2) GEOREFERENCIAMENTO NO SIRGAS 2000
    # Já garantimos CRS_GEO acima; se viesse em outro CRS, foi convertido

    # 3) REGIÕES + OVERLAY
    try:
        gdf_regioes = safe_read_regions(PATH_REGIOES)
    except FileNotFoundError as e:
        print(f"Erro fatal: Arquivo de regiões não encontrado.")
        print(f"Detalhe: {e}")
        print(f"\nVerifique se o caminho PATH_REGIOES está correto: {PATH_REGIOES}")
        return

    gdf_pts = overlay_region(gdf_raw, gdf_regioes)

    # 4) AGRUPAMENTO E MÉTRICAS REGIONAIS
    met_reg = compute_region_metrics(gdf_pts, gdf_regioes)

    # 5) DENSIDADE E CAPACIDADE MÉDIA
    # Já calculadas em met_reg; mantemos também uma versão no nível do ponto se for útil
    # Nada adicional aqui

    # 6) CATEGORIZAÇÃO FINAL DE DISPONIBILIDADE
    # Já está em gdf_pts["disp_cat"]

    # ================
    # GERAÇÃO DO MAPA
    # ================
    # Base: regiões
    fig, ax = plt.subplots(figsize=(12, 10))
    gdf_regioes.plot(ax=ax, color="#f5f5f5", edgecolor="#aaaaaa", linewidth=0.6)

    # Linhas de transmissão (opcional)
    gdf_lines = try_read_lines(PATH_LINHAS_TX)
    if gdf_lines is not None:
        try:
            gdf_lines.plot(ax=ax, linewidth=0.5, alpha=0.6)
        except Exception:
            pass

    # Paleta discreta para classes de tensão
    # Matplotlib criará as cores automaticamente a partir das categorias
    # Para melhor legibilidade, ordenamos as classes
    class_order = ["< 69 kV", "69–138 kV", "138–230 kV", "230–440 kV", ">= 440 kV"]
    gdf_pts["classe_kv"] = gdf_pts["classe_kv"].astype("category")
    gdf_pts["classe_kv"] = gdf_pts["classe_kv"].cat.set_categories(class_order, ordered=True)

    # Plota subestações com tamanho proporcional à capacidade normalizada
    # e cor por classe de tensão

    # Prepara os argumentos base da plotagem
    plot_kwargs = {
        "ax": ax,
        "markersize": 10 + 90 * gdf_pts["cap_norm_0_1"].fillna(0.1),  # 10 a 100 px
        "linewidth": 0.2,
        "edgecolor": "#333333",
    }

    # SÓ adiciona a categorização se houver dados válidos em 'classe_kv'
    if gdf_pts["classe_kv"].notna().any():
        plot_kwargs["column"] = "classe_kv"
        plot_kwargs["legend"] = True
        plot_kwargs["categorical"] = True
    else:
        # Se não houver dados, avisa o usuário e plota sem cores
        print(
            f"Aviso: Nenhum dado válido encontrado na coluna '{COL_KV}'. "
            "O mapa não será categorizado por tensão."
        )

    # Executa a plotagem com os argumentos condicionais
    gdf_pts.plot(**plot_kwargs)

    # Rótulos simples (opcional)
    # for _, r in gdf_pts.sample(min(60, len(gdf_pts))).iterrows():
    #     if pd.notna(r[COL_NOME]):
    #         ax.annotate(str(r[COL_NOME])[:20], xy=(r.geometry.x, r.geometry.y), xytext=(3, 3), textcoords="offset points", fontsize=6)

    # Título e subtítulo
    ax.set_title("Subestações Elétricas no Brasil — Capacidade e Nível de Tensão", fontsize=14, fontweight="bold", pad=12)
    ax.text(
        0.01, 0.97,
        "Círculos maiores indicam maior capacidade instalada (MVA). Cores indicam classes de tensão (kV).",
        transform=ax.transAxes, fontsize=10, va="top"
    )

    # Legenda adicional para disponibilidade (Alta/Média/Baixa): criamos um inset textual
    share = gdf_pts["disp_cat"].value_counts(dropna=False)
    legend_text = "Disponibilidade (por ponto):\n" + "\n".join([f"• {k}: {int(v)}" for k, v in share.items()])
    ax.text(0.01, 0.01, legend_text, transform=ax.transAxes, fontsize=9, va="bottom", ha="left",
            bbox=dict(facecolor="white", edgecolor="#cccccc", boxstyle="round,pad=0.4"))

    ax.axis("off")
    plt.tight_layout()

    # Salvar
    os.makedirs(os.path.dirname(OUT_PNG), exist_ok=True)
    plt.savefig(OUT_PNG, dpi=300)
    plt.close(fig)

    # =========================
    # Exporta métricas regionais (se quiser inspecionar)
    # =========================
    met_reg.sort_values("REGIAO_NOME").to_csv("data/metricas_regionais.csv", index=False)

    print(f"Mapa salvo em: {OUT_PNG}")
    print("Métricas regionais em: data/metricas_regionais.csv")


if __name__ == "__main__":
    main()
