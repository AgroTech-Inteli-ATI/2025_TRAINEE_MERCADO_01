import pandas as pd

# le arquivo csv
df = pd.read_csv("data/producao-agricola.csv", sep=";", encoding="utf-8", skiprows=4)

# limpa aspas e espaços
df.columns = df.columns.str.replace('"', '').str.strip()
df = df.map(lambda x: str(x).replace('"', '').strip() if isinstance(x, str) else x)

# renomeia colunas
df.columns = ["Municipio", "Total", "Cafe", "Cana", "Milho", "Soja"]

# converte colunas numéricas
for col in ["Cafe", "Cana", "Milho", "Soja"]:
    df[col] = (
        df[col]
        .replace(["-", "..."], 0)
        .replace(",", ".", regex=True)
        .astype(float)
    )

# normaliza (0–1)
for col in ["Soja", "Milho", "Cana", "Cafe"]:
    max_value = df[col].max()
    df[col + "_norm"] = df[col] / max_value if max_value > 0 else 0

# calcula índice DPF com pesos arredondados
df["DPF"] = (
    0.45 * df["Soja_norm"]
    + 0.25 * df["Milho_norm"]
    + 0.20 * df["Cana_norm"]
    + 0.10 * df["Cafe_norm"]
)

# classificação
def classificar(dpf):
    if dpf > 0.75:
        return "A - Muito Alto"
    elif dpf > 0.5:
        return "B - Alto"
    elif dpf > 0.25:
        return "C - Médio"
    else:
        return "D - Baixo"

df["Classificacao"] = df["DPF"].apply(classificar)

resultado = df.sort_values(by="DPF", ascending=False)
resultado.to_csv("data/resultado_polos_agricolas.csv", index=False, encoding="utf-8-sig")

print("\nop 10 municípios:")
print(resultado[["Municipio", "DPF", "Classificacao"]].head(10))

# análise exploratória
print("\nEstatísticas básicas por cultura (hectares plantados):\n")
stats = df[["Soja", "Milho", "Cana", "Cafe"]].describe().round(2)
print(stats.loc[["mean", "max"]])

# salva estatísticas em CSV
stats.to_csv("data/estatisticas_culturas.csv", encoding="utf-8-sig")

import matplotlib.pyplot as plt

# calcula médias por cultura
media_culturas = df[["Soja", "Milho", "Cana", "Cafe"]].mean().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
media_culturas.plot(kind="bar", color=["#74c476", "#a1d99b", "#31a354", "#006d2c"])
plt.title("Média de Área Plantada por Cultura (ha)")
plt.ylabel("Hectares (média por município)")
plt.xlabel("Cultura")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("data/media_culturas.png")
plt.close()