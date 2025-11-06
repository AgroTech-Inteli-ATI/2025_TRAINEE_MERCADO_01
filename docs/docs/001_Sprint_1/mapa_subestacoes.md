---
sidebar_position: 1
slug: /Sprint-1/Subestacoes_Energia
description: "Mapeamento das subestações de energia elétrica e disponibilidade por região"
---

# Mapeamento das Subestações de Energia Elétrica

## Objetivo

Identificar, classificar e mapear as principais subestações de energia elétrica do Brasil, avaliando sua distribuição regional e disponibilidade operacional. Esta análise compõe o diagnóstico territorial da Sprint 1 e subsidia o ranqueamento de localidades na Sprint 2.

## Metodologia

1. Coleta de dados públicos
    Fontes utilizadas:
    - ONS (Operador Nacional do Sistema Elétrico) — dados da rede básica e subestações de transmissão;
    - EPE (Empresa de Pesquisa Energética) — camadas geoespaciais do Sistema Interligado Nacional (SIN);
    - ANEEL (Agência Nacional de Energia Elétrica) — base geográfica das distribuidoras e infraestrutura elétrica.

2. Tratamento e padronização dos dados
    - Extração e limpeza dos shapefiles em Python (geopandas, pandas);
    - Normalização das variáveis de capacidade (MVA) e nível de tensão (kV);
    - Georreferenciamento no sistema SIRGAS 2000;
    - Classificação regional e cálculo da disponibilidade média;
    - Agrupamento por região (N, NE, CO, SE, S);
    - Cálculo da densidade de subestações por km² e da capacidade instalada média;
    - Categorização de disponibilidade:
      - Alta: > 80% da capacidade operacional;
      - Média: 50–80%;
      - Baixa: < 50%.

3. Geração do mapa
    O mapa foi produzido em Python/Matplotlib (arquivo: `src/plot_substations.py`):
    - União das bases geográficas do ONS e EPE;
    - Visualização das subestações por nível de tensão (cores distintas);
    - Inclusão de camadas de linhas de transmissão e fronteiras regionais.
    Exportação automática em `data/mapa_subestacoes.png`.

## Resultados:
1. **mapa**



2. **tabela**
| Região        | Nº de Subestações | Capacidade Média (MVA) | Disponibilidade Média | Classificação |
|---------------|-------------------:|-----------------------:|----------------------:|---------------|
| Sudeste       |             |                     |                   |          |
| Sul           |                 |                     |                    |          |
| Centro-Oeste  |                 |                     |                   |          |
| Nordeste      |                 |                     |                   |          |
| Norte         |                 |                    |                   |  |

## Interpretação

-
