---
sidebar_position: 2
slug: /Sprint-2/frete-saida
description: "Modelo de cálculo e consolidação do frete de saída (site → polos consumidores)"
---

# 3.1 Frete de Saída – Sprint 2

## 1) Objetivo
Calcular o **custo logístico de distribuição** do produto (site → polos consumidores) em **R$/t**, de forma simples e auditável.
Os resultados alimentam o **ranking preliminar de localidades** (peso “frete de saída”) e permitem testar **cenários** (Base/Otimista/Conservador).

---

## 2) Escopo e premissas
- Modal: **rodoviário** (carreta/graneleiro 9 eixos como referência).
- Tarifa média: **R$/t·km** (parametrizada em `PARAMS_GERAIS`).
- **Pedágios**: somatório por rota convertido para **R$/t** (capacidade útil do veículo).
- Sem ICMS/seguro/diárias nesta etapa (entram no P&L posterior).
- Polos desta sprint (ex.): **Sorriso/MT, Rio Verde/GO, Luís E. Magalhães/BA, Rondonópolis/MT, Ribeirão Preto/SP**.

---

## 3) Estrutura da planilha (`FRETE_SAIDA`)
| Coluna | O que representa | Fórmula/exemplo |
|---|---|---|
| `SITE` | Origem (ex.: Pratápolis) | — |
| `POLO` | Destino consumidor | — |
| `DISTÂNCIA (km)` | Km rodoviários (Maps/Earth) | — |
| `R$/t·km` | Tarifa média do frete | — |
| `Pedágio (R$/t)` | Soma de praças convertido p/ R$/t | — |
| `CUSTO FRETE (R$/t)` | Custo da rota por tonelada | `=DISTÂNCIA*R$/t·km + Pedágio` |
| `Participação (%)` | Relevância do polo na demanda | — |
| `Sazonalidade (0–1)` | Atividade do polo | — |
| `Peso Efetivo` | Multiplicador de mercado | `=Participação*Sazonalidade` |
| `Custo Ponderado (R$/t)` | Custo × peso efetivo | `=CUSTO FRETE*Peso Efetivo` |

---

## 4) Fórmulas (modelo)
- `Custo_Base_R$/t = Dist_km × Tarifa_R$/t·km`
- `Custo_Frete_R$/t = (Dist_km × Tarifa_R$/t·km) + Pedágio_R$/t`
- `Peso_Efetivo = Participação_% × Sazonalidade`
- `Custo_Ponderado = Custo_Frete_R$/t × Peso_Efetivo`

---

## 5) Exemplo auditável (da planilha)
**Origem:** Pratápolis → **Destino:** Sorriso (MT)
**Distância:** 1.750 km · **Tarifa:** 0,28 R$/t·km · **Pedágio:** 4,50 R$/t · **Participação:** 12% · **Sazonalidade:** 1,0

- `Custo_Frete_R$/t = 1.750 × 0,28 + 4,50 = 494,50`
- `Peso_Efetivo = 12 × 1,0 = 12`
- `Custo_Ponderado = 494,50 × 12 = 5.934`

> Repita o raciocínio para **Rio Verde/GO, Luís E. Magalhães/BA, Rondonópolis/MT, Ribeirão Preto/SP** com os valores da sua planilha.

---

## 6) Integração com o ranking
- A aba `FRETE_SAIDA` consolida um **valor por site** (ex.: SOMASE do `Custo Ponderado (R$/t)`), que alimenta **“Frete de Saída (R$/t)”** na aba `RANKING`.
- No `RANKING`, o frete de saída recebe **nota (0–1)** via **normalização inversa** e é ponderado pelo **peso do cenário** (`wFS`).

**Normalização (menor custo → nota maior):**
- `FS_ajust = FS × (1 + stressF)`
- `v_FS = (max(FS_ajust) − FS_ajust_site) / (max(FS_ajust) − min(FS_ajust))`
- `Score += wFS × v_FS`

---

## 7) Cenários (BASE · OTIMISTA · CONSERVADOR)
Ajustes sugeridos (parametrizados em `PARAMS_GERAIS`):

| Cenário | Tarifa (R$/t·km) | Sazonalidade (ex.) | Uso típico |
|---|---|---|---|
| **BASE** | Parâmetro corrente | 1,00 | Referência |
| **OTIMISTA** | −5% | 0,9–1,0 | Mercado/negociação favoráveis |
| **CONSERVADOR** | +10% | 0,7–0,9 | Diesel alto/pico de demanda |

**Efeito de cenário:**
- `Tarifa_cenário = Tarifa × (1 + stressF)`
- `FS_ajust = (Dist_km × Tarifa_cenário) + Pedágio_R$/t`

---

## 8) Checklist de qualidade
- **Distâncias** conferidas (Maps/Earth) com rota coerente.
- **Pedágios** atualizados (concessionárias/ANTT) convertidos para **R$/t**.
- **Tarifa R$/t·km** consistente com benchmark de mercado/ANTT.
- **Participação e Sazonalidade** revisadas com a célula de mercado.
- **Auditoria**: refazer manualmente 1 rota por sprint (transparência e aderência).

---

## 9) Fontes e referências
- **Documento de método desta sprint**
  [`Sprint 2 – Documento Acadêmico De Análise Econômica E Estratégica (agrominas) (1).pdf`](/mnt/data/Sprint 2 – Documento Acadêmico De Análise Econômica E Estratégica (agrominas) (1).pdf)

- **Diretrizes do parceiro (kick-off / hipóteses)**
  [`[ATI_AGROMINAS] Trainees ATI - SPRINT REVIEW 1.pdf`](/mnt/data/[ATI_AGROMINAS] Trainees ATI - SPRINT REVIEW 1.pdf)

- **KML do site/área (base para rotas)**
  [`LIMEIRA 1.kml`](/mnt/data/LIMEIRA 1.kml) · [`LIMEIRA 2.kml`](/mnt/data/LIMEIRA 2.kml)

- **Medição de distância**
  Google Maps – Medir distância: https://support.google.com/maps/answer/1628031
  Google Earth – Medir distâncias e áreas: https://support.google.com/earth/answer/9010337

- **Benchmark regulatório (referência de custos)**
  ANTT – Calculadora do Piso Mínimo do Frete: https://www.gov.br/antt/pt-br/assuntos/rodovias/controle-de-cargas/piso-minimo-do-frete/calculadora-do-piso-minimo
