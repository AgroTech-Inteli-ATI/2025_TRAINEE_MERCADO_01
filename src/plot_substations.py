import warnings
from pathlib import Path
from typing import Optional, List, Any, Dict, Union

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

warnings.filterwarnings("ignore", category=UserWarning)


# Paths
DATA_DIR = Path("data")
REGIONS_DIR = DATA_DIR / "regions"
EPE_SUBSTATIONS_DIR = DATA_DIR / "epe_substations"
EPE_TRANSMISSAO_DIR = DATA_DIR / "epe_transmissao"
OUT_DIR = DATA_DIR

# Inputs
PATH_ONS = DATA_DIR / "ons_substations.geojson"
# Shapefile fallbacks (accents removed to avoid encoding issues). Used only if GeoJSON is missing.
PATH_EPE_SHP = EPE_SUBSTATIONS_DIR / "Subestacoes_-_Base_Existente.shp"
PATH_LINHAS_TX_SHP = EPE_TRANSMISSAO_DIR / "Linhas_de_Transmissao_-_Base_Existente.shp"
PATH_EPE = DATA_DIR / "epe_substations.geojson"
PATH_LINHAS_TX = DATA_DIR / "epe_transmissao.geojson"
PATH_REGIOES = REGIONS_DIR / "BR_Regioes_2024.shp"

# Expected columns for points
COL_LON = "lon"
COL_LAT = "lat"
COL_CAP = "capacidade_mva"
COL_CAP_OP = "cap_operacional_mva"
COL_KV = "Tensao"
COL_NOME = "nome"

# CRS
CRS_GEO = "EPSG:4674"   # SIRGAS 2000 geographic
CRS_AREA = "EPSG:5880"  # SIRGAS 2000 / Brazil Polyconic (meters)

# Outputs
OUT_PNG = OUT_DIR / "mapa_subestacoes.png"
OUT_CSV_METRICS = OUT_DIR / "metricas_regionais.csv"


def convert_shp_to_geojson_if_needed(shp_path: Path, geojson_path: Path) -> None:
    try:
        if not geojson_path.exists():
            if shp_path.exists():
                print(f"Convertendo Shapefile {shp_path.name} para GeoJSON...")
                gdf_shp = gpd.read_file(shp_path)
                gdf_shp.to_file(geojson_path, driver="GeoJSON")
                print(f"Conversao concluida: {geojson_path}")
            else:
                print(f"Aviso: Shapefile de origem nao encontrado: {shp_path}. Pulando conversao.")
    except Exception as e:
        print(f"Aviso: Falha ao converter {shp_path}: {e}")


def read_points_layer(path_or_url: Union[str, Path]) -> gpd.GeoDataFrame:
    path_str = str(path_or_url)

    if not path_str.startswith(("http://", "https://")):
        path_obj = Path(path_or_url)
        if not path_obj.exists():
            raise FileNotFoundError(f"Arquivo nao encontrado: {path_obj}")
        ext = path_obj.suffix.lower()
    else:
        ext = Path(path_str).suffix.lower()

    if ext == ".csv":
        df = pd.read_csv(path_or_url)
        if COL_LON not in df.columns or COL_LAT not in df.columns:
            raise ValueError(f"CSV precisa ter colunas {COL_LON} e {COL_LAT}.")
        gdf = gpd.GeoDataFrame(
            df,
            geometry=gpd.points_from_xy(df[COL_LON], df[COL_LAT]),
            crs="EPSG:4326",
        )
    else:
        gdf = gpd.read_file(path_or_url)

    if "geometry" not in gdf.columns and COL_LON in gdf.columns and COL_LAT in gdf.columns:
        gdf = gpd.GeoDataFrame(
            gdf,
            geometry=gpd.points_from_xy(gdf[COL_LON], gdf[COL_LAT]),
            crs="EPSG:4326",
        )

    if gdf.crs is None:
        gdf.set_crs("EPSG:4326", inplace=True)

    gdf = gdf.to_crs(CRS_GEO)

    # Ensure expected fields
    if COL_CAP not in gdf.columns:
        gdf[COL_CAP] = None
    if COL_KV not in gdf.columns:
        gdf[COL_KV] = None
    if COL_CAP_OP not in gdf.columns:
        gdf[COL_CAP_OP] = gdf[COL_CAP]
    if COL_NOME not in gdf.columns:
        gdf[COL_NOME] = None

    for c in [COL_CAP, COL_CAP_OP, COL_KV]:
        gdf[c] = pd.to_numeric(gdf[c], errors="coerce")

    return gdf


def minmax_norm(values: pd.Series) -> pd.Series:
    s = pd.to_numeric(values, errors="coerce")
    vmin = s.min(skipna=True)
    vmax = s.max(skipna=True)
    if pd.isna(vmin) or pd.isna(vmax) or vmin == vmax:
        return pd.Series(0.0, index=s.index)
    return (s - vmin) / (vmax - vmin)


def classify_voltage(kv: pd.Series) -> pd.Series:
    """Classifica a tensao (kV) em categorias discretas para visualizacao."""
    kv_num = pd.to_numeric(kv, errors="coerce")
    bins = [-1, 69, 138, 230, 440, 10000]
    labels = ["< 69 kV", "69-138 kV", "138-230 kV", "230-440 kV", ">= 440 kV"]
    return pd.cut(kv_num, bins=bins, labels=labels)


def availability_percentage(cap_op: pd.Series, cap_inst: pd.Series) -> pd.Series:
    op = pd.to_numeric(cap_op, errors="coerce")
    inst = pd.to_numeric(cap_inst, errors="coerce")
    pct = (op / inst) * 100
    pct = pct.replace([float("inf"), float("-inf")], float("nan"))
    return pct


def availability_bucket(pct: pd.Series) -> pd.Series:
    def _lab(v):
        if pd.isna(v):
            return "Indefinida"
        if v > 80:
            return "Alta"
        if v >= 50:
            return "Media"
        return "Baixa"

    return pct.apply(_lab).astype("category")


def safe_read_regions(path: Union[str, Path]) -> gpd.GeoDataFrame:
    """Le a camada de poligonos das regioes e normaliza o CRS e a coluna de nome."""
    try:
        gdf = gpd.read_file(path)
    except Exception as e:
        raise FileNotFoundError(f"Nao foi possivel ler o arquivo de regioes em {path}. Erro: {e}")

    if gdf.crs is None:
        gdf.set_crs(CRS_GEO, inplace=True)
    else:
        gdf = gdf.to_crs(CRS_GEO)

    col_reg = None

    # 1) Correspondencias exatas
    possible_exact_cols = ["REGIAO", "NM_REGIAO", "REGIAO_NOME", "nome", "name", "SIGLA"]
    cols_lower = {c.lower(): c for c in gdf.columns}
    for col_name in possible_exact_cols:
        if col_name.lower() in cols_lower:
            col_reg = cols_lower[col_name.lower()]
            break

    # 2) Correspondencias parciais
    if col_reg is None:
        possible_partial_keys = ["reg", "macro", "nome", "name"]
        for c in gdf.columns:
            c_lower = c.lower()
            if any(key in c_lower for key in possible_partial_keys):
                col_reg = c
                break

    if col_reg is None:
        raise ValueError(
            f"Camada de regioes em {path} sem coluna de nome identificavel (ex: 'REGIAO').\n"
            f"--> Colunas encontradas no arquivo: {list(gdf.columns)}"
        )

    gdf["REGIAO_NOME"] = gdf[col_reg].astype(str).str.upper().str.strip()
    return gdf[["REGIAO_NOME", "geometry"]].copy()


def overlay_region(points: gpd.GeoDataFrame, regions: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """Atribui a cada ponto sua regiao por sobreposicao espacial (sjoin)."""
    pts = points.sjoin(regions, how="left", predicate="within")
    pts = pts.drop(columns=[c for c in pts.columns if c.startswith("index_right")], errors="ignore")
    pts["REGIAO_NOME"] = pts["REGIAO_NOME"].fillna("FORA DO TERRITORIO")
    return pts


def compute_region_metrics(points: gpd.GeoDataFrame, regions: gpd.GeoDataFrame) -> pd.DataFrame:
    # Area km2
    reg_proj = regions.to_crs(CRS_AREA).copy()
    reg_proj["area_km2"] = reg_proj.geometry.area / 1_000_000.0
    reg_areas = reg_proj[["REGIAO_NOME", "area_km2"]]

    # Aggregates
    grp = points.groupby("REGIAO_NOME", dropna=False).agg(
        qtd_subestacoes=("geometry", "count"),
        cap_inst_media_mva=(COL_CAP, "mean"),
        disponibilidade_media_pct=("disponibilidade_pct", "mean"),
    ).reset_index()

    met = grp.merge(reg_areas, on="REGIAO_NOME", how="left")
    met["densidade_sub_km2"] = met["qtd_subestacoes"] / met["area_km2"]
    return met


def try_read_lines(path: Union[str, Path]) -> Optional[gpd.GeoDataFrame]:
    """Tenta ler a camada opcional de linhas de transmissao."""
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
        print(f"Aviso: Nao foi possivel carregar camada de linhas de {path}. {e}")
        return None
    return None


def _pick_numeric_column(gdf: gpd.GeoDataFrame, candidates: List[str]) -> Optional[str]:
    """Escolhe a primeira coluna candidata que existir e tiver valores numericos validos."""
    for col in candidates:
        if col in gdf.columns:
            s = pd.to_numeric(gdf[col], errors="coerce")
            if s.notna().any():
                return col
    return None


def main():
    # 0) Conversao opcional de SHP -> GeoJSON
    print("0) Setup: conversao de Shapefile para GeoJSON (se necessario)")
    convert_shp_to_geojson_if_needed(PATH_EPE_SHP, PATH_EPE)
    convert_shp_to_geojson_if_needed(PATH_LINHAS_TX_SHP, PATH_LINHAS_TX)

    # 1) Leitura
    print("1) Leitura dos pontos (ONS/EPE)")
    try:
        gdf_ons = read_points_layer(PATH_ONS)
        gdf_epe = read_points_layer(PATH_EPE)
    except FileNotFoundError as e:
        print("Arquivo de dados de entrada nao encontrado.")
        print(f"Detalhe: {e}")
        return
    except Exception as e:
        print(f"Erro inesperado ao ler os dados: {e}")
        return

    # 2) Uniao e limpeza
    print("2) Transformacao e uniao")
    gdf_ons["fonte"] = "ONS"
    gdf_epe["fonte"] = "EPE"
    gdf_raw = pd.concat([gdf_ons, gdf_epe], ignore_index=True)
    gdf_raw = gpd.GeoDataFrame(gdf_raw, geometry="geometry", crs=CRS_GEO)
    gdf_raw = gdf_raw.drop_duplicates(subset=[COL_NOME, "geometry"])  # opcional
    print(f"Total de {len(gdf_raw)} registros de subestacao carregados.")

    # 3) Variaveis derivadas
    gdf_raw["cap_norm_0_1"] = minmax_norm(gdf_raw[COL_CAP])
    gdf_raw["kv_norm_0_1"] = minmax_norm(gdf_raw[COL_KV])
    gdf_raw["disponibilidade_pct"] = availability_percentage(gdf_raw[COL_CAP_OP], gdf_raw[COL_CAP])
    gdf_raw["disp_cat"] = availability_bucket(gdf_raw["disponibilidade_pct"])
    gdf_raw["classe_kv"] = classify_voltage(gdf_raw[COL_KV])

    # 4) Regioes
    print("3) Regioes + overlay")
    try:
        gdf_regioes = safe_read_regions(PATH_REGIOES)
    except (FileNotFoundError, ValueError) as e:
        print(f"Erro ao ler regioes: {e}")
        return
    gdf_pts = overlay_region(gdf_raw, gdf_regioes)

    # 5) Metricas regionais
    print("4) Agrupamento e metricas regionais")
    met_reg = compute_region_metrics(gdf_pts, gdf_regioes)

    # 6) Mapa
    print("Gerando o mapa...")
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_aspect("equal")

    # Regioes com cores distintas + legenda
    unique_regs = list(gdf_regioes["REGIAO_NOME"].astype(str).unique())
    cmap = plt.get_cmap("tab10" if len(unique_regs) <= 10 else ("tab20" if len(unique_regs) <= 20 else "hsv"))
    reg_colors = {reg: cmap(i % cmap.N) for i, reg in enumerate(unique_regs)}
    gdf_regioes = gdf_regioes.copy()
    gdf_regioes["_color"] = gdf_regioes["REGIAO_NOME"].map(reg_colors)
    gdf_regioes.plot(ax=ax, color=gdf_regioes["_color"], edgecolor="#aaaaaa", linewidth=0.6)

    handles = [Patch(facecolor=reg_colors[r], edgecolor="#777777", label=r) for r in unique_regs]
    reg_legend = ax.legend(handles=handles, title="Regioes", loc="upper right", bbox_to_anchor=(0.99, 0.99), frameon=False)
    ax.add_artist(reg_legend)

    # Linhas de transmissao com espessura por tensao (ou fallback por comprimento)
    gdf_lines = try_read_lines(PATH_LINHAS_TX)
    if gdf_lines is not None:
        candidates = [
            "Tensao", "TENSAO", "tensao", "kv", "KV", "VOLT_KV",
            "NIVEL_TENSAO", "NIVEL_TENS", "N_TENSAO", "classe_kv",
        ]
        col = _pick_numeric_column(gdf_lines, candidates)
        metric = None
        if col is not None:
            metric = pd.to_numeric(gdf_lines[col], errors="coerce")
        else:
            try:
                metric = gdf_lines.to_crs(CRS_AREA).geometry.length / 1000.0  # km
            except Exception:
                metric = None

        if metric is not None:
            lw = minmax_norm(metric).fillna(0.0)
            lw = 0.4 + 2.6 * lw  # from 0.4 to 3.0
            gdf_lines = gdf_lines.copy()
            gdf_lines["_linewidth"] = lw
            # Plot each geometry individually so a single float is passed to linewidth (avoids passing a Series)
            for lw_val, geom in zip(gdf_lines["_linewidth"], gdf_lines.geometry):
                try:
                    lw_float = float(lw_val) if lw_val is not None else 0.8
                except Exception:
                    lw_float = 0.8
                gpd.GeoSeries([geom], crs=gdf_lines.crs).plot(
                    ax=ax, color="#9e5959", linewidth=lw_float, alpha=0.7, zorder=1
                )
        else:
            gdf_lines.plot(ax=ax, color="#9e5959", linewidth=0.8, alpha=0.7, zorder=1)

    # Pontos (subestacoes) com categorias de tensao
    class_order = ["< 69 kV", "69-138 kV", "138-230 kV", "230-440 kV", ">= 440 kV"]
    gdf_pts["classe_kv"] = gdf_pts["classe_kv"].astype("category")
    gdf_pts["classe_kv"] = gdf_pts["classe_kv"].cat.set_categories(class_order, ordered=True)

    base_size = 10
    scale_factor = 90
    plot_kwargs: Dict[str, Any] = {
        "ax": ax,
        "markersize": base_size + scale_factor * gdf_pts["cap_norm_0_1"].fillna(0.1),
        "linewidth": 0.2,
        "edgecolor": "#333333",
        "zorder": 2,
    }
    if gdf_pts["classe_kv"].notna().any():
        plot_kwargs.update({
            "column": "classe_kv",
            "legend": True,
            "categorical": True,
            "legend_kwds": {
                "title": "Nivel de Tensao",
                "loc": "lower left",
                "bbox_to_anchor": (0.01, 0.2),
                "frameon": False,
            },
        })
    else:
        print(f"Aviso: Nenhum dado valido em '{COL_KV}'. Mapa nao sera categorizado por tensao.")
        plot_kwargs["color"] = "blue"

    gdf_pts.plot(**plot_kwargs)

    # Texto de disponibilidade
    share = gdf_pts["disp_cat"].value_counts(dropna=False).sort_index()
    legend_text = "Disponibilidade (Contagem):\n" + "\n".join([f"- {k}: {int(v)}" for k, v in share.items()])
    ax.text(
        0.01,
        0.01,
        legend_text,
        transform=ax.transAxes,
        fontsize=9,
        va="bottom",
        ha="left",
        bbox=dict(facecolor="white", edgecolor="#cccccc", boxstyle="round,pad=0.4"),
    )

    ax.axis("off")
    plt.tight_layout()

    # Save
    OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(OUT_PNG, dpi=300)
    plt.close(fig)
    print(f"Mapa salvo em: {OUT_PNG}")

    OUT_CSV_METRICS.parent.mkdir(parents=True, exist_ok=True)
    met_reg.sort_values("REGIAO_NOME").to_csv(OUT_CSV_METRICS, index=False, float_format="%.4f")
    print(f"Metricas regionais salvas em: {OUT_CSV_METRICS}")
    print("--- Processo concluido ---")


if __name__ == "__main__":
    main()
