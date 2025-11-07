---
sidebar_position: 2
slug: /Sprint-1/polos-consumidores
description: "Identificação dos principais polos agrícolas consumidores"
---

# Identificação dos Polos Agrícolas Consumidores

## Objetivo
**Mapear e classificar** os principais polos agrícolas consumidores de **fertilizantes** no Brasil e Paraguai, com base na **relevância produtiva, intensidade de uso de fertilizantes e potencial logístico** para escoamento.
Esta análise compõe o **diagnóstico territorial da Sprint 1**, subsidiando a etapa de **ranqueamento de localidades na Sprint 2**.

## Metodologia

A identificação dos polos agrícolas foi realizada em três etapas principais:

1. **Coleta de dados públicos**
   Os dados de área plantada e produção foram obtidos a partir da base **SIDRA - IBGE (PAM 2024)**, considerando as culturas de maior consumo de fertilizantes (IBGE, 2025):
   - Soja
   - Milho
   - Cana-de-açúcar
   - Café

   Essas quatro culturas representam mais de **73% da demanda nacional de fertilizantes** (MAPA, 2022a).

2. **Cálculo do Índice de Demanda Potencial de Fertilizantes (DPF)**
   Para cada município, foi calculado um índice composto que pondera a importância relativa de cada cultura.
   A fórmula final utilizada foi:

   ```text
   DPF_i = 0.45 * S_soja + 0.25 * S_milho + 0.20 * S_cana + 0.10 * S_cafe
   ```

   Onde `S_c` representa a área plantada normalizada (0–1) da cultura *c*.

   Os pesos foram definidos com base na participação estimada das culturas de soja, milho e cana-de-açúcar (MAPA, 2022b)

3. **Implementação em Python**
   O índice foi calculado utilizando **Pandas** para tratamento de dados e normalização.
   O script completo encontra-se em `src/calculate_dpf.py`, e segue o fluxo:

   - Leitura e limpeza do CSV (`producao-agricola.csv`)
   - Conversão de valores e normalização (0–1) por cultura
   - Cálculo ponderado do DPF
   - Classificação final dos municípios em faixas:
     - **A** → DPF > 0,75 (Muito alto)
     - **B** → 0,50–0,75 (Alto)
     - **C** → 0,25–0,50 (Médio)
     - **D** → < 0,25 (Baixo)

---

### Análise Exploratória das Culturas

Antes da geração do mapa, foi realizada uma **análise exploratória dos dados de produção agrícola** para verificar a representatividade das principais culturas consideradas no índice DPF.  
O **gráfico de barras** abaixo apresenta a **média de área plantada por cultura** nos municípios brasileiros analisados:

<p style={{textAlign: 'center'}}>Figura 1 - Média de área plantada por cultura (ha)</p>

<div style={{margin: 25}}>
    <div style={{textAlign: 'center'}}>
        <img src={require("../../static/img/media_culturas.png").default} style={{width: 800}} alt="Mapa das jazidas" />
        <br />
    </div>
</div>
<p style={{textAlign: 'center'}}>Fonte: Os autores (2025)</p>

Essa visualização evidencia que as culturas de **soja e milho** concentram a maior parte da área cultivada nacionalmente, seguidas por **cana-de-açúcar** e **café**.  
Tal comportamento **reforça a coerência dos pesos atribuídos** na fórmula do DPF - 0,45 para soja e 0,25 para milho, uma vez que essas culturas são as **principais consumidoras de fertilizantes** no país.

--- 

## Geração do Heatmap

Para representar espacialmente os resultados, foi criado um script em **Python/Matplotlib** (`src/plot_heatmap.py`) que:

- Integra os resultados do DPF com o **shapefile municipal do IBGE** (via repositório público [tbrugz/geodata-br](https://github.com/tbrugz/geodata-br));
- Realiza o *merge* automático entre nomes de municípios e o mapa;
- Gera um **mapa de calor (heatmap)** com gradação em verde (cmap = `YlGn`), proporcional ao índice DPF;
- Exporta automaticamente a imagem final como `data/heatmap_dpf.png`.

O resultado visual evidencia os polos agrícolas de maior demanda de fertilizantes, concentrados principalmente no **Centro-Oeste (MT, GO)** e **MATOPIBA (BA, PI, MA, TO)**.

<p style={{textAlign: 'center'}}>Figura 1 - Heatmap dos polos agrícolas com maior demanda de fertilizantes</p>
<div style={{margin: 25}}>
    <div style={{textAlign: 'center'}}>
        <img src={require("../../static/img/heatmap_dpf.png").default} style={{width: 800}} alt="Heatmap de demanda" />
        <br />
    </div>
</div>
<p style={{textAlign: 'center'}}>Fonte: Os autores (2025)</p>

<div style="text-align:center">
  <p style="margin-bottom:8px;"><strong>Figura 2 - Heatmap dos polos agrícolas com maior demanda de fertilizantes</strong></p>
  <img src="../../static/img/heatmap_dpf.png" style="display:block; margin:0 auto; width:700px; max-width:100%; height:auto;" />
  <p style="text-align:center; margin-top:8px; font-size:0.9em;">Fonte: Os autores (2025)</p>
</div>

---

## Principais Resultados

Os dez municípios com maior DPF foram:

| Município | DPF | Classificação |
|------------|------|----------------|
| Sorriso (MT) | 0,703 | B - Alto |
| Rio Verde (GO) | 0,528 | B - Alto |
| Nova Ubiratã (MT) | 0,475 | C - Médio |
| Nova Mutum (MT) | 0,451 | C - Médio |
| Jataí (GO) | 0,435 | C - Médio |
| Diamantino (MT) | 0,433 | C - Médio |
| Querência (MT) | 0,433 | C - Médio |
| Campo Novo do Parecis (MT) | 0,432 | C - Médio |
| São Desidério (BA) | 0,403 | C - Médio |
| Formosa do Rio Preto (BA) | 0,397 | C - Médio |

---

## Interpretação

Os resultados confirmam o padrão esperado de concentração da demanda de fertilizantes nas regiões de **produção intensiva de grãos**:

- **Sorriso (MT)** e **Rio Verde (GO)** surgem como polos de maior demanda, refletindo suas extensas áreas de soja e milho e sua infraestrutura consolidada de escoamento.
- O **MATOPIBA** apresenta forte crescimento, destacando-se como nova fronteira agrícola e potencial área de expansão de mercado.
- No eixo **Triângulo Mineiro – Oeste da Bahia**, há alta correlação entre produção agrícola e proximidade das jazidas de **fosfato e dunito da Agrominas**, o que reforça a viabilidade para implantação da planta de termofosfato.

---

## Próximos Passos

- Cruzar o mapa DPF com variáveis de **energia e logística** (distância às jazidas e subestações elétricas) na Sprint 2;
- Aplicar o modelo de **pontuação multicritério (Score_i)** com base nas variáveis e pesos definidos no documento de critérios;
- Refinar a análise espacial com shapefiles estaduais de infraestrutura e rede rodoviária (DNIT).

---

## Referências
- IBGE – Instituto Brasileiro de Geografia e Estatística. Tabela 5457: Área plantada ou destinada à colheita, área colhida, quantidade produzida, rendimento médio e valor da produção das lavouras temporárias e permanentes. IBGE, 2025. Disponível em: https://sidra.ibge.gov.br/tabela/5457. Acesso em: 05 de novembro de 2025.
- a) BRASIL. Ministério da Agricultura, Pecuária e Abastecimento. Plano Nacional de Fertilizantes 2050. Brasília: MAPA, 2022. Disponível em: https://www.gov.br/agricultura/pt-br/assuntos/insumos-agropecuarios/insumos-agricolas/fertilizantes/plano-nacional-de-fertilizantes. Acesso em: 05 nov. 2025.
- b) BRASIL. Ministério da Agricultura, Pecuária e Abastecimento. Plano Nacional de Fertilizantes 2050. Brasília: MAPA, 2022. Disponível em: https://www.gov.br/agricultura/pt-br/assuntos/insumos-agropecuarios/insumos-agricolas/fertilizantes/statistics-sect-setor. Acesso em: 06 nov. 2025.
- Repositório público “tbrugz/geodata-br” (shapefile GeoJSON de municípios brasileiros)
