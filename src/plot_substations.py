import warnings
from pathlib import Path
from typing import Optional, List, Any, Dict
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
warnings.filterwarnings("ignore", category=UserWarning)

DATA_DIR = Path("data")
REGIONS_DIR = DATA_DIR / "regions"
EPE_SUBSTATIONS_DIR = DATA_DIR / "epe_substations"
EPE_TRANSMISSAO_DIR = DATA_DIR / "epe_transmissao"
OUT_DIR = DATA_DIR

# Entrada
PATH_ONS = DATA_DIR / "ons_substations.geojson"           # Pontos com lon/lat, capacidade, etc.
PATH_EPE_SHP = EPE_SUBSTATIONS_DIR / "Subestações_-_Base_Existente.shp"
PATH_LINHAS_TX_SHP = EPE_TRANSMISSAO_DIR / "Linhas_de_Transmissão_-_Base_Existente.shp"
PATH_EPE = DATA_DIR / "epe_substations.geojson"           # Idem
PATH_LINHAS_TX = DATA_DIR / "epe_transmissao.geojson"     # linhas de transmissão
PATH_REGIOES = REGIONS_DIR / "BR_Regioes_2024.shp"        # Polígonos das regiões

# Colunas Esperadas
COL_LON = "lon"
COL_LAT = "lat"
COL_CAP = "capacidade_mva"          # Capacidade instalada MVA
COL_CAP_OP = "cap_operacional_mva"  # Opcional; se não existir, será assumida igual à instalada
COL_KV = "Tensao"                # Nível de tensão em kV
COL_NOME = "nome"                   # Nome da subestação (opcional)

# --- Sistemas de Referência de Coordenadas (CRS) ---
CRS_GEO = "EPSG:4674"    # SIRGAS 2000 (geográfico) para referência
CRS_AREA = "EPSG:5880"   # SIRGAS 2000 / Brazil Polyconic (métrico), adequado para cálculo de área

# --- Saída ---
OUT_PNG = OUT_DIR / "mapa_subestacoes.png"
OUT_CSV_METRICS = OUT_DIR / "metricas_regionais.csv"

# converter shapefile em geojson
def convert_shp_to_geojson_if_needed(shp_path: Path, geojson_path: Path) -> None:

    try:
        if not geojson_path.exists():
            if shp_path.exists():
                print(f"Convertendo Shapefile {shp_path.name} para GeoJSON...")
                gdf_shp = gpd.read_file(shp_path)
                gdf_shp.to_file(geojson_path, driver="GeoJSON")
                print(f"Conversão concluída: {geojson_path}")
            else:
                print(f"Aviso: Shapefile de origem não encontrado: {shp_path}. Pulando conversão.")
    except Exception as e:
        # Captura ampla para qualquer falha na leitura/escrita do geopandas/fiona
        print(f"Aviso: Falha ao converter {shp_path}: {e}")



def read_points_layer(path_or_url: str | Path) -> gpd.GeoDataFrame:
    path_str = str(path_or_url)

    if not path_str.startswith(("http://", "https://")):
        path_obj = Path(path_or_url)
        if not path_obj.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {path_obj}")
        ext = path_obj.suffix.lower()
    else:
        # Assume que é uma URL, a extensão será inferida pelo geopandas ou está no nome
        ext = Path(path_str).suffix.lower()

    if ext == ".csv":
        df = pd.read_csv(path_or_url)
        if COL_LON not in df.columns or COL_LAT not in df.columns:
            raise ValueError(f"CSV precisa ter colunas {COL_LON} e {COL_LAT}.")
        gdf = gpd.GeoDataFrame(
            df,
            geometry=gpd.points_from_xy(df[COL_LON], df[COL_LAT]),
            crs="EPSG:4326",  # Assume WGS84 para CSVs, ajustaremos para SIRGAS
        )
    else:
        gdf = gpd.read_file(path_or_url)

    # Se geometria não existir mas lon/lat existirem (ex: Parquet sem geo)
    if "geometry" not in gdf.columns and COL_LON in gdf.columns and COL_LAT in gdf.columns:
        gdf = gpd.GeoDataFrame(
            gdf,
            geometry=gpd.points_from_xy(gdf[COL_LON], gdf[COL_LAT]),
            crs="EPSG:4326",
        )

    # Ajusta CRS para SIRGAS 2000
    if gdf.crs is None:
        gdf.set_crs("EPSG:4326", inplace=True) # Tenta inferir WGS84

    gdf = gdf.to_crs(CRS_GEO)

    # Garante campos-chave
    if COL_CAP not in gdf.columns:
        gdf[COL_CAP] = None
    if COL_KV not in gdf.columns:
        gdf[COL_KV] = None
    if COL_CAP_OP not in gdf.columns:
        gdf[COL_CAP_OP] = gdf[COL_CAP] # Assume operacional = instalada se faltar
    if COL_NOME not in gdf.columns:
        gdf[COL_NOME] = None

    # Limpa tipos numéricos
    for c in [COL_CAP, COL_CAP_OP, COL_KV]:
        gdf[c] = pd.to_numeric(gdf[c], errors="coerce")

    return gdf


def minmax_norm(values: pd.Series) -> pd.Series:
    """Normalização min-max (0 a 1), robusta a NaNs e divisão por zero."""
    s = pd.to_numeric(values, errors="coerce")
    vmin = s.min(skipna=True)
    vmax = s.max(skipna=True)

    # Retorna zeros se não houver variação ou dados válidos
    if pd.isna(vmin) or pd.isna(vmax) or vmin == vmax:
        return pd.Series(0.0, index=s.index)

    return (s - vmin) / (vmax - vmin)


def classify_voltage(kv: pd.Series) -> pd.Series:
    """Classifica a tensão (kV) em categorias discretas para visualização."""
    kv_num = pd.to_numeric(kv, errors="coerce")
    bins = [-1, 69, 138, 230, 440, 10000]
    labels = ["< 69 kV", "69–138 kV", "138–230 kV", "230–440 kV", ">= 440 kV"]
    return pd.cut(kv_num, bins=bins, labels=labels)


def availability_percentage(cap_op: pd.Series, cap_inst: pd.Series) -> pd.Series:
    """Calcula disponibilidade percentual (Cap. Operacional / Cap. Instalada)."""
    op = pd.to_numeric(cap_op, errors="coerce")
    inst = pd.to_numeric(cap_inst, errors="coerce")

    pct = (op / inst) * 100

    # Substitui infinitos (divisão por zero, ex: inst=0, op=100) por NaN
    pct = pct.replace([float('inf'), float('-inf')], float('nan'))
    return pct


def availability_bucket(pct: pd.Series) -> pd.Series:
    """Categoriza a disponibilidade percentual em 'Alta', 'Média', 'Baixa'."""
    def _lab(v):
        if pd.isna(v):
            return "Indefinida"
        if v > 80:
            return "Alta"
        if v >= 50:
            return "Média"
        return "Baixa"

    return pct.apply(_lab).astype("category")


def safe_read_regions(path: str | Path) -> gpd.GeoDataFrame:
    """Lê a camada de polígonos das regiões e normaliza o CRS e a coluna de nome."""
    try:
        gdf = gpd.read_file(path)
    except Exception as e:
        raise FileNotFoundError(f"Não foi possível ler o arquivo de regiões em {path}. Erro: {e}")

    if gdf.crs is None:
        gdf.set_crs(CRS_GEO, inplace=True)
    else:
        gdf = gdf.to_crs(CRS_GEO)

    col_reg = None

    # 1. Tenta achar correspondências exatas (mais seguro)
    possible_exact_cols = ["REGIAO", "NM_REGIAO", "REGIAO_NOME", "nome", "name", "SIGLA"]
    cols_lower = {c.lower(): c for c in gdf.columns} # {nome_min: Nome_Orig}

    for col_name in possible_exact_cols:
        if col_name.lower() in cols_lower:
            col_reg = cols_lower[col_name.lower()]
            break

    # 2. Se não achar, tenta correspondências parciais (mais flexível)
    if col_reg is None:
        possible_partial_keys = ["reg", "macro", "nome", "name"]
        for c in gdf.columns:
            c_lower = c.lower()
            if any(key in c_lower for key in possible_partial_keys):
                col_reg = c
                break

    if col_reg is None:
        # Se ainda falhar, mostra ao usuário as colunas que encontrou
        raise ValueError(
            f"Camada de regiões em {path} sem coluna de nome identificável (ex: 'REGIAO').\n"
            f"--> Colunas encontradas no arquivo: {list(gdf.columns)}"
        )

    gdf["REGIAO_NOME"] = gdf[col_reg].astype(str).str.upper().str.strip()
    return gdf[["REGIAO_NOME", "geometry"]].copy()

def overlay_region(points: gpd.GeoDataFrame, regions: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """Atribui a cada ponto sua região por sobreposição espacial (sjoin)."""
    pts = points.sjoin(regions, how="left", predicate="within")
    # Limpa coluna de índice espacial
    pts = pts.drop(columns=[c for c in pts.columns if c.startswith("index_right")], errors="ignore")
    pts["REGIAO_NOME"] = pts["REGIAO_NOME"].fillna("Fora do Território")
    return pts


def compute_region_metrics(points: gpd.GeoDataFrame, regions: gpd.GeoDataFrame) -> pd.DataFrame:
    """
    Agrupa por região e calcula métricas:
    - densidade de subestações por km²
    - capacidade média instalada (MVA)
    - disponibilidade média (%)
    """
    # 1. Calcula área em km² (usando CRS projetado)
    reg_proj = regions.to_crs(CRS_AREA).copy()
    reg_proj["area_km2"] = reg_proj.geometry.area / 1_000_000.0
    reg_areas = reg_proj[["REGIAO_NOME", "area_km2"]]

    # 2. Agrega métricas dos pontos por região
    grp = points.groupby("REGIAO_NOME", dropna=False).agg(
        qtd_subestacoes=("geometry", "count"),
        cap_inst_media_mva=(COL_CAP, "mean"),
        disponibilidade_media_pct=("disponibilidade_pct", "mean"),
    ).reset_index()

    # 3. Junta com áreas e calcula densidade
    met = grp.merge(reg_areas, on="REGIAO_NOME", how="left")
    met["densidade_sub_km2"] = met["qtd_subestacoes"] / met["area_km2"]

    return met


def try_read_lines(path: str | Path) -> Optional[gpd.GeoDataFrame]:
    """Tenta ler a camada opcional de linhas de transmissão."""
    path_str = str(path)

    try:
        if path_str.startswith(("http://", "https://")) or Path(path).exists():
            gdf = gpd.read_file(path)
            if gdf.crs is None:
                gdf.set_crs(CRS_GEO, inplace=True)
            else:
                gdf = gdf.to_crs(CRS_GEO)
            return gdf
    except Exception as e:
        print(f"Aviso: Não foi possível carregar camada de linhas de {path}. {e}")
        return None
    return None

def main():

    print(" 0) SETUP: Converte Shapefiles para GeoJSON se necessário ")
    convert_shp_to_geojson_if_needed(PATH_EPE_SHP, PATH_EPE)
    convert_shp_to_geojson_if_needed(PATH_LINHAS_TX_SHP, PATH_LINHAS_TX)

    print(" 1) EXTRAÇÃO E LIMPEZA ")
    try:
        gdf_ons = read_points_layer(PATH_ONS)
        gdf_epe = read_points_layer(PATH_EPE)
    except FileNotFoundError as e:
        print(f"Arquivo de dados de entrada não encontrado.")
        print(f"Detalhe: {e}")
        print("\nVerifique se os caminhos PATH_ONS e PATH_EPE estão corretos.")
        return
    except Exception as e:
        print(f"Erro inesperado ao ler os dados: {e}")
        return

    print(" 2) TRANSFORMAÇÃO E UNIÃO ")
    gdf_ons["fonte"] = "ONS"
    gdf_epe["fonte"] = "EPE"

    gdf_raw = pd.concat([gdf_ons, gdf_epe], ignore_index=True)
    gdf_raw = gpd.GeoDataFrame(gdf_raw, geometry="geometry", crs=CRS_GEO)

    # Remove duplicatas (opcional, baseado em geometria e nome)
    gdf_raw = gdf_raw.drop_duplicates(subset=[COL_NOME, "geometry"])

    print(f"Total de {len(gdf_raw)} registros de subestação carregados.")

    # Normalização e classificação
    gdf_raw["cap_norm_0_1"] = minmax_norm(gdf_raw[COL_CAP])
    gdf_raw["kv_norm_0_1"] = minmax_norm(gdf_raw[COL_KV])
    gdf_raw["disponibilidade_pct"] = availability_percentage(gdf_raw[COL_CAP_OP], gdf_raw[COL_CAP])
    gdf_raw["disp_cat"] = availability_bucket(gdf_raw["disponibilidade_pct"])
    gdf_raw["classe_kv"] = classify_voltage(gdf_raw[COL_KV])

    print(" 3) REGIÕES + OVERLAY ")
    try:
        gdf_regioes = safe_read_regions(PATH_REGIOES)
    except FileNotFoundError as e:
        print(f"Erro fatal: Arquivo de regiões não encontrado.")
        print(f"Detalhe: {e}")
        print(f"\nVerifique se o caminho PATH_REGIOES está correto: {PATH_REGIOES}")
        return
    except ValueError as e:
        print(f"Erro fatal ao ler regiões: {e}")
        return

    gdf_pts = overlay_region(gdf_raw, gdf_regioes)

    print(" 4) AGRUPAMENTO E MÉTRICAS REGIONAIS")
    met_reg = compute_region_metrics(gdf_pts, gdf_regioes)


    print("Gerando o mapa...")
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_aspect('equal')

    # Camada base: regiões
    gdf_regioes.plot(ax=ax, color="#f5f5f5", edgecolor="#aaaaaa", linewidth=0.6)

    # Camada opcional: linhas de transmissão
    gdf_lines = try_read_lines(PATH_LINHAS_TX)
    if gdf_lines is not None:
        gdf_lines.plot(ax=ax, color="#9e595968", linewidth=0.5, alpha=0.7, zorder=1)

    # Define a ordem da legenda de tensão
    class_order = ["< 69 kV", "69–138 kV", "138–230 kV", "230–440 kV", ">= 440 kV"]
    gdf_pts["classe_kv"] = gdf_pts["classe_kv"].astype("category")
    gdf_pts["classe_kv"] = gdf_pts["classe_kv"].cat.set_categories(class_order, ordered=True)

    # Prepara argumentos da plotagem
    base_size = 10
    scale_factor = 90
    plot_kwargs: Dict[str, Any] = {
        "ax": ax,
        "markersize": base_size + scale_factor * gdf_pts["cap_norm_0_1"].fillna(0.1),
        "linewidth": 0.2,
        "edgecolor": "#333333",
        "zorder": 2,
    }

    # Adiciona categorização por cor SOMENTE se houver dados válidos
    if gdf_pts["classe_kv"].notna().any():
        plot_kwargs.update({
            "column": "classe_kv",
            "legend": True,
            "categorical": True,
            "legend_kwds": {
                "title": "Nível de Tensão",
                "loc": "lower left",
                "bbox_to_anchor": (0.01, 0.2), # Posição da legenda
                "frameon": False,
            }
        })
    else:
        print(f"Aviso: Nenhum dado válido em '{COL_KV}'. Mapa não será categorizado por tensão.")
        plot_kwargs["color"] = "blue" # Cor padrão se não houver categoria

    # Plota as subestações
    gdf_pts.plot(**plot_kwargs)

    # Título e subtítulo
    ax.set_title("Subestações Elétricas no Brasil: Quantidade e Nível de Tensão", fontsize=14, fontweight="bold", pad=12)

    # Legenda customizada para disponibilidade (contagem)
    share = gdf_pts["disp_cat"].value_counts(dropna=False).sort_index()
    legend_text = "Disponibilidade (Contagem):\n" + "\n".join([f"• {k}: {int(v)}" for k, v in share.items()])
    ax.text(0.01, 0.01, legend_text, transform=ax.transAxes, fontsize=9, va="bottom", ha="left",
            bbox=dict(facecolor="white", edgecolor="#cccccc", boxstyle="round,pad=0.4"))

    ax.axis("off")
    plt.tight_layout()

    # Salvar
    OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(OUT_PNG, dpi=300)
    plt.close(fig)

    print(f"Mapa salvo em: {OUT_PNG}")


    OUT_CSV_METRICS.parent.mkdir(parents=True, exist_ok=True)
    met_reg.sort_values("REGIAO_NOME").to_csv(OUT_CSV_METRICS, index=False, float_format="%.4f")
    print(f"Métricas regionais salvas em: {OUT_CSV_METRICS}")
    print("\n--- Processo concluído ---")


if __name__ == "__main__":
    main()
