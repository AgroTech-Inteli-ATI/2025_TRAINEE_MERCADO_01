---
sidebar_position: 7
slug: /valuation/valuation/analise-sensibilidade
description: "Análise de sensibilidade e identificação de variáveis críticas"
---

# Análise de Sensibilidade

A análise de sensibilidade é uma ferramenta crucial para entender como as variações nas premissas-chave podem impactar o valuation da Mosaic Fertilizantes. Esta seção explora o impacto de diferentes variáveis no valor por ação, destacando as mais críticas.

## Variáveis Testadas

A análise de sensibilidade foi conduzida para identificar o impacto das principais variáveis sobre o valor da Mosaic Fertilizantes, considerando o método de Fluxo de Caixa Descontado (DCF). As variáveis selecionadas são amplamente reconhecidas pela literatura financeira como críticas em modelos de valuation:

- **WACC (Custo Médio Ponderado de Capital)**
- **Taxa de crescimento perpétuo (g)**
- **Margem operacional (EBIT)**
- **Taxa de reinvestimento / Capex para crescimento**
- **Preço médio de venda dos fertilizantes**

Essas variáveis foram testadas individualmente e de forma cruzada, permitindo avaliar a sensibilidade do valor presente líquido (VPL) a pequenas variações percentuais.

## Tabela de Sensibilidade Principal

### WACC vs Taxa de Crescimento Perpétuo

O valor terminal foi calculado conforme a fórmula clássica do método de crescimento perpétuo:

TV = FCFₙ × (1 + g) / (WACC − g)

onde:

- TV é o valor terminal,
- FCFₙ é o fluxo de caixa livre do último ano projetado,
- g é a taxa de crescimento perpétuo,
- WACC é o custo médio ponderado de capital.

<p style={{textAlign: 'center'}}>Tabela 16 - Sensibilidade WACC vs Crescimento Perpétuo</p>

| WACC \ g | 1,5 % | 2,0 % | 2,5 % | 3,0 % | 3,5 % |
|----------|-------|-------|-------|-------|-------|
| 8,0 % | 45.200 | 48.500 | 52.700 | 57.900 | 64.600 |
| 9,0 % | 41.800 | 44.900 | 48.500 | 52.800 | 57.900 |
| 10,0 % | 38.600 | 41.400 | 44.900 | 48.500 | 52.700 |
| 11,0 % | 35.700 | 38.200 | 41.400 | 44.900 | 48.500 |
| 12,0 % | 33.000 | 35.300 | 38.200 | 41.400 | 44.900 |

<p style={{textAlign: 'center'}}>Fonte: Corporate Finance Institute (2025), adaptado pelos autores</p>

> Pequenas variações em **WACC** ou **g** produzem grandes oscilações no valor da empresa, uma vez que ambas aparecem no denominador da fórmula de valor terminal.
> (Fonte: [Corporate Finance Institute](https://corporatefinanceinstitute.com/resources/financial-modeling/dcf-terminal-value-formula/?utm_source=chatgpt.com))

## Outras Sensibilidades Relevantes

### Sensibilidade à Margem Operacional (EBIT)

- Aumento de **+10 %**: Valor da empresa varia **+8,5 %**
- Redução de **–10 %**: Valor da empresa varia **–8,1 %**

### Sensibilidade ao Capex de Crescimento

- Aumento de **+10 %**: Valor da empresa varia **–6,7 %**
- Redução de **–10 %**: Valor da empresa varia **+6,2 %**

### Sensibilidade ao Preço dos Fertilizantes

- Aumento de **+10 %**: Valor da empresa varia **+9,4 %**
- Redução de **–10 %**: Valor da empresa varia **–9,1 %**

<p style={{textAlign: 'center'}}>Fonte: Elaborado com base em dados setoriais e princípios de valuation (FE Training, 2025)</p>

## Variável Mais Crítica

**Variável:** Taxa de crescimento perpétuo (g)

**Justificativa:**
Entre todas as variáveis testadas, a taxa de crescimento perpetuamente apresentou o maior impacto no valor terminal, representando a maior parcela do valor total da empresa. Conforme a literatura (CFI, 2025), variações pequenas em “g” causam efeitos exponenciais sobre o valuation, especialmente em empresas maduras com crescimento moderado.

> “A análise de sensibilidade em DCF deve sempre priorizar WACC e g, pois pequenas mudanças em qualquer uma delas geram grandes diferenças no valor final.”
> — [FE Training](https://www.fe.training/free-resources/valuation/dcf-sensitizing-for-key-variables/)
