import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

SHAPE_PATH = "https://github.com/tbrugz/geodata-br/raw/master/geojson/geojs-100-mun.json"

df = pd.read_csv("data/resultado_polos_agricolas.csv")

# limpa nomes pra casar com shapefile
df["Municipio_limpo"] = df["Municipio"].str.replace(r"\s*\(.*\)", "", regex=True).str.strip().str.upper()

gdf_municipios = gpd.read_file(SHAPE_PATH)

# tenta achar o nome do campo com nome do município
nome_coluna = None
for col in gdf_municipios.columns:
    if any(keyword in col.lower() for keyword in ["mun", "nome", "name"]):
        nome_coluna = col
        break


gdf_municipios[nome_coluna] = gdf_municipios[nome_coluna].str.upper().str.strip()

# faz merge
gdf_merge = gdf_municipios.merge(df, left_on=nome_coluna, right_on="Municipio_limpo", how="left")

fig, ax = plt.subplots(figsize=(12, 10))
gdf_municipios.plot(ax=ax, color="#f0f0f0", linewidth=0.2, edgecolor="#999999")

gdf_merge.dropna(subset=["DPF"]).plot(
    column="DPF",
    cmap="YlGn",
    linewidth=0.3,
    ax=ax,
    edgecolor="grey",
    legend=True,
    legend_kwds={
        "label": "Índice DPF (Demanda Potencial de Fertilizantes)",
        "shrink": 0.7,
    },
)

ax.set_title(
    "Mapa de Calor – Potencial de Demanda de Fertilizantes (DPF)",
    fontweight="bold",
    fontsize=14,
    pad=15,
)
ax.axis("off")

plt.tight_layout()
plt.savefig("data/heatmap_dpf.png", dpi=300)
plt.show()
