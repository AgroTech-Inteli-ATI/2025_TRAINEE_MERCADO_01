---
sidebar_position: 3
slug: /Sprint-2/ranking-localidades
description: "Modelo comparativo e ranking preliminar das localidades"
---

# 3.2 Ranking Preliminar das Localidades – Sprint 2

## 1. Objetivo
Gerar um **ranking comparativo de localidades** para implantação da planta de **Termofosfato Magnesiano**, consolidando custos críticos e acesso a mercado.  
O resultado transforma múltiplos fatores (energia, fretes e eventuais custos de fronteira) em **uma pontuação única por local**, orientando priorização para estudos de viabilidade, visitas técnicas e cenários de investimento.

---

## 2. Metodologia – MCDM (Modelo Multicritério)

A pontuação de cada localidade *i* é calculada por soma ponderada das notas normalizadas dos critérios:

Score_i = Σ_k ( w_k × v_ik )

- `w_k` = **peso** do critério *k* (importância relativa).  
- `v_ik` = **nota normalizada (0–1)** da localidade *i* no critério *k*.  
- Critérios considerados: **Energia (E)**, **Frete de Saída (FS)**, **Frete de Matéria-Prima (FM)** e **Fronteira (FR)**.  
- Aplicamos **cenários** (Base, Otimista, Conservador) que ajustam custos e/ou penalizam fronteira.

**Fluxo (planilha):** coleta de custos por site → aplicação de ajustes do cenário → normalização 0–1 → soma ponderada → **ordenação** do ranking.

---

## 3. Pesos Utilizados

### 3.1 Pesos por critério (por cenário)

| Cenário       | Peso de energia | Peso de frete de saída | Peso de frete de matéria-prima | Peso da fronteira |
|---|---:|---:|---:|---:|
| **Base**        | 0,90 | 0,08 | 0,02 | 0,00 |
| **Otimista**    | 0,80 | 0,15 | 0,05 | 0,00 |
| **Conservador** | 0,95 | 0,04 | 0,01 | 0,00 |

### 3.2 Parâmetros de ajuste do cenário

| Cenário       | Custo de energia (ajuste %) | Custo de fretes (ajuste %) | Penalidade de fronteira (R$/t) |
|---|---:|---:|---:|
| **Base**        | 0%   | 0%   | 0 |
| **Otimista**    | −10% | −5%  | 0 |
| **Conservador** | +15% | +10% | 5 |

> **Leitura rápida:** energia domina o modelo; fretes refinam a competitividade; fronteira incide apenas quando aplicável.

---

## 4. Normalização das Variáveis

Após aplicar os ajustes do cenário:

E_ajust = E × (1 + stressE)
FS_ajust = FS × (1 + stressF)
FM_ajust = FM × (1 + stressF)
FR_ajust = FR + penalFR

Como são **custos** (quanto menor, melhor), a normalização é **inversa**:

v = (max − valor) / (max − min)
(se max = min, definir v = 1)


---

## 5. Tabela Comparativa (Localidades × Variáveis)

> Tabela espelho da aba `RANKING`, com valores **ajustados** e **notas normalizadas (0–1)**.

| Localidade (País) | Energia ajustada (R$/t) | Frete de saída ajustado (R$/t) | Frete de MP ajustado (R$/t) | Fronteira ajustada (R$/t) | Nota E | Nota FS | Nota FM | Nota FR | Score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Pratápolis (BR) | 0 | 0 | 0 | 0 | 1,00 | 1,00 | 1,00 | 1,00 | 1,00 |

> À medida que novas localidades (BR/PY) forem incluídas, as notas e o ranking se atualizam automaticamente.

---

## 6. Ranking Final – Sprint 2

**Cenário Base – status atual (dados parciais):**

1. **Pratápolis (BR)** — *provisório; aguardando inclusão das demais localidades e custos completos.*


---

## 7. Interpretação

- **Energia** é o principal discriminador (peso 0,80–0,95). Diferenças de TE/TUSD/demanda podem **inverter posições** rapidamente.  
- **Fretes (FS e FM)** funcionam como **desempate** prático: distância a polos consumidores e a insumos afeta a competitividade marginal.  
- **Fronteira** só pesa quando aplicável (logística internacional); no Base, não há penalidade.  
- **Cenários**:  
  - *Otimista* suaviza custos (E −10%, fretes −5%) e eleva o peso de FS (0,15).  
  - *Conservador* pressiona E (+15%) e fretes (+10%), além de penalizar fronteira (R$ 5/t).

---

## 8. Conclusão Executiva

O ranking multicritério está implementado e reflete a diretriz do parceiro: **energia** como fator crítico (≈ “95% da decisão”) e **logística** como refinamento competitivo.  
Para sair do status provisório, devemos **popular**:

- **ENERGIA**: TE/TUSD/demanda por site convertidos em **R$/t**;  
- **FRETE_SAÍDA**: custos por polo e participação ponderada (**R$/t**);  
- **FRETE_MP**: rotas e composições por insumo (**R$/t**);  
- **RANKING**: inclusão das novas localidades (BR e PY).

Com os dados completos, o modelo entregará um **Top 2–3 por cenário**, orientando CAPEX/OPEX detalhados e a decisão **go/no-go** para due diligence em campo.
