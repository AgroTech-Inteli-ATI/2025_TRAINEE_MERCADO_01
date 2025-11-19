---
sidebar_position: 5
slug: /Sprint-2/capex-breakeven
description: "Estimativa inicial de CAPEX e Break-even"
---

# 3.4 Estimativa Inicial de CAPEX e Break-even – Sprint 2

## 1. Objetivo

Um dos entregáveis definidos no Plano de Trabalho para o projeto Agrominas é o “Documento com estimativa inicial de CAPEX e break‑even”. O Termo de Abertura do Projeto (TAP) também reforça que cabe à equipe estimar os investimentos necessários na planta de produção de fertilizantes (CAPEX) e o ponto de equilíbrio econômico (break‑even). Como ainda não existe um projeto de engenharia detalhado, este documento apresenta estimativas de ordem de grandeza baseadas em preços de mercado para equipamentos semelhantes e em fatores de capital típicos para plantas industriais de processamento mineral.

---

## 2. Estrutura do CAPEX Considerada

Para cada equipamento principal do processo foram pesquisados preços em fontes primárias (fabricantes ou distribuidores) e em listas de preços de equipamentos usados. Os valores foram convertidos para reais usando uma taxa de câmbio de R$ 5,00 por US$ (Já no Google Sheets está no valor do dia 19/11, *5,340207075*). A Tabela 1 resume as principais referências utilizadas para cada item:

| Equipamento                               | Evidência de preço                                                                                                                                                                                                 | Faixa de preço ou valor escolhido                                                                  |
|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| **Forno rotativo**                        | Artigo técnico sobre fornos de cimento informa que o custo de aquisição de um forno rotativo varia de **US$ 400 000 a US$ 1 500 000**, sendo que um forno de porte médio custa entre US$ 800 000 e US$ 1,2 milhão. | Adotou‑se **US$ 1 000 000** (cerca de R$ 5,0 milhões) como custo de um forno de porte médio.       |
| **Sistema de moagem (moinho de bolas)**   | A tabela de preços da Mt Baker Mining & Metals apresenta moinhos de bolas de 3 × 6 ft por US$ 49 940 e de 5 × 10 ft por US$ 152 940.                                                                               | Considerou‑se o moinho de 5 × 10 ft como representativo (**US$ 150 000** ≈ R$ 750 000).            |
| **Peneiramento (tela vibratória)**        | Blog técnico sobre peneiras vibratórias cita que telas circulares custam de **US$ 799 a US$ 3 899** e que peneiras lineares podem chegar a **US$ 11 099**.                                                         | Para estimar um equipamento industrial de peneiramento considerou‑se **US$ 10 000** (≈ R$ 50 000). |
| **Sistema de ensaque**                    | O site da IWI Concrete Equipment oferece um **bag filler** (ensacadora) usado com capacidade de 300 sacos/hora por **US$ 15 500**.                                                                                 | Optou‑se por **US$ 15 500** (≈ R$ 77 500).                                                         |
| **Subestação/transformador**              | Guia de preços da Taishan Transformer indica que transformadores de potência de 1 a 10 MVA custam entre **US$ 30 000 e US$ 300 000**.                                                                              | Adotado **US$ 100 000** (≈ R$ 500 000) para uma subestação e transformador de média potência.      |
| **Sistema de ar comprimido (compressor)** | Anúncio da Midwest Air Compressor LLC informa que um compressor rotativo de 100 hp custa **US$ 29 990**.                                                                                                           | Utilizou‑se **US$ 29 990** (≈ R$ 149 950).                                                         |

A soma dos preços de aquisição fornece o custo de equipamentos comprados (E). Para obter o capital fixo instalado (CAPEX total) é necessário incluir custos de instalação, edificações, utilidades, engenharia e contingências. Um guia de engenharia de custos mostra que o custo de instalação de equipamentos pode representar cerca de 47 % do custo de equipamentos, enquanto outras parcelas (instrumentação, tubulações, elétrica, edifícios, obras civis, utilidades e serviços) totalizam cerca de 100 % a 200 % do custo de equipamentos. Adicionalmente, os custos indiretos de engenharia, administração da construção e contingências podem representar mais 20 % – 50 %. Como nesta fase os dados são preliminares, assumiu‑se que o CAPEX total é 3,5 × E (ponto médio da faixa sugerida).

---

## 3. Cálculo do CAPEX

Com base nos preços de Tabela 1, obteve‑se E ≈ R$ 6,53 milhões. Aplicando o fator de capital de 3,5 vezes, **o CAPEX total estimado é ≈ R$ 22,85 milhões**. A planilha “CAPEX” do arquivo Excel acompanha o detalhamento por item e o cálculo do capital total. Apesar de ser uma estimativa de ordem de grandeza, esses valores já incluem equipamentos principais (forno, moagem, peneiramento, ensaque), utilidades (subestação e compressor) e margens para instalações civis, engenharia e contingências.

---

## 4. Cálculo do Break-even

A estimativa de payback (break-even) considera o **CAPEX aproximado de R$ 22,9 milhões** e a margem operacional gerada pela venda de fertilizante termofosfato.

A fórmula utilizada é:

**Break-even (anos) = CAPEX / Margem operacional anual**

A margem operacional anual é obtida multiplicando-se a margem por tonelada pela produção anual de **100 000 t**.

A margem por tonelada depende do custo variável total. A página de energia do projeto informa que a usina consome cerca de **1,0 MWh/t** (com intervalos de 0,9–0,95 MWh/t) e apresenta uma tabela com tarifas de energia de regiões diferentes:

- **75 R$/MWh** – Amapá
- **106 R$/MWh** – MG/RJ
- **300 R$/MWh** – Sudeste (Enel SP)

Com base nesses valores, adotaram-se três cenários de custo de energia. Os demais custos variáveis foram mantidos:

- Matéria-prima: **R$ 150/t**
- Embalagem: **R$ 20/t**
- Mão-de-obra: **R$ 50/t**

Custos fixos anuais estimados em **R$ 4,29 milhões** (10% do CAPEX para depreciação e manutenção + R$ 2 milhões de despesas gerais).

### Exemplo – Cenário Médio

- Energia: **106 R$/MWh**
- Custo variável total: **R$ 326/t**
  (150 + 20 + 50 + 106 × 1 MWh/t)
- Custo total unitário: **R$ 368,85/t**
- Preço de venda: **R$ 400/t**
- Margem: **R$ 31,15/t**
- Margem anual: **R$ 3,12 milhões**
- Payback: **~7,33 anos**

---

## 5. Sensibilidade do Break-even

A tabela a seguir apresenta três cenários para a margem, associados a diferentes custos de energia. Os demais parâmetros foram mantidos.

### Tabela de Sensibilidade do Break-even

| Cenário        | Energia (R$/MWh) | Custo variável (R$/t) | Custo total unitário (R$/t) | Margem (R$/t) | Margem anual (R$ milhões) | Break-even (anos) |
|----------------|------------------|------------------------|-----------------------------|----------------|-----------------------------|--------------------|
| Margem Alta    | 75               | 295                    | 337,85                      | 62,15          | 6,22                        | 3,68               |
| Margem Média   | 106              | 326                    | 368,85                      | 31,15          | 3,12                        | 7,33               |
| Margem Baixa   | 300              | 520                    | 562,85                      | −162,85        | −16,28                      | inviável           |

> Os valores de margem anual são calculados multiplicando-se a margem por tonelada por 100 000 t/ano e dividindo por 1 000 000 para obter milhões de reais.

---

## 6. Interpretação dos Resultados

Os resultados mostram que o **custo de energia é o principal determinante da viabilidade econômica**:

- **Margem Alta (energia barata)** – Com energia a 75 R$/MWh (como no Amapá ou Paraguai), o projeto gera margem de **62,15 R$/t** e cerca de **R$ 6,2 milhões anuais**. O payback ocorre em aproximadamente **3,7 anos**, tornando o investimento atrativo.

- **Margem Média (energia intermediária)** – Com tarifa de 106 R$/MWh (padrão MG/RJ), a margem cai para **31,15 R$/t** e o tempo de payback sobe para **7,3 anos**. Ainda é viável, mas a recuperação do investimento é bem mais lenta.

- **Margem Baixa (energia cara)** – Com energia a 300 R$/MWh (Enel SP), o custo total supera o preço de venda, gerando **margem negativa** e prejuízo anual de aproximadamente **R$ 16 milhões**. Nesse cenário, o projeto é **inviável** e não alcança break-even.

> Embora ajustes em outros custos variáveis ou aumento no preço de venda possam melhorar a margem, a sensibilidade indica que **mesmo ajustes modestos não compensam o alto custo de energia**.
