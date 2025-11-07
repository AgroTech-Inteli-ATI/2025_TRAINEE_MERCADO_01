---
sidebar_position: 4
slug: /Sprint-1/Variaveis_Criterios
description: "Documento de requisitos iniciais (dados, variáveis e critérios de decisão)"
---

# Documento de Variáveis e Critérios de Decisão

## Objetivo
Selecionar as melhores localidades para implantar a planta de **Termofosfato Magnesiano**, priorizando **viabilidade econômica** (custo por tonelada entregue), **acesso a energia barata e disponível**, **logística de insumos e mercado** e **potencial de demanda** (DPF).

## Metodologia
A seleção das variáveis foi guiada pelos objetivos definidos no TAP e nas reuniões de kickoff com a Agrominas, priorizando **energia barata e disponível**, **proximidade das jazidas minerais** e **demanda agrícola regional**.  
A abordagem utiliza um **modelo de decisão multicritério ponderado (MCDM)**, onde cada variável é normalizada em escala **0–1** e ponderada conforme seu peso relativo na estrutura de custos e operação.

A pontuação final de cada localidade é obtida por:

```text
Score_i = Σ (w_k * v_ik)
```

onde:  
- `w_k` = peso do critério `k`;  
- `v_ik` = valor normalizado da variável `k` para a localidade `i`.  

Variáveis de custo têm sentido **inverso** (menor = melhor), enquanto variáveis de potencial mantêm sentido **direto** (maior = melhor).


## Estrutura de Variáveis e Critérios

| Grupo | Variável | Fonte | Tipo | Peso | Critério de Avaliação |
|:--|:--|:--|:--:|:--:|:--|
| **Energia** | Tarifa média de energia industrial (R$/MWh) | ANEEL - Subestações | Custo ↓ | 25% | **Menores tarifas recebem maior nota.** Escala normalizada (1 – valor/valor_max). Representa o maior componente do custo industrial (≈ R$ 500/t). |
| **Energia** | Capacidade disponível das subestações (MVA útil) | ANEEL - ONS | Potencial ↑ | 10% | **Maior disponibilidade = maior nota.** Mede segurança de fornecimento e potencial de expansão elétrica. |
| **Matéria-prima** | Distância média às jazidas de Fosfato (km) | Agrominas - IBGE | Custo ↓ | 10% | **Menor distância = menor custo logístico.** Pontuação invertida. |
| **Matéria-prima** | Distância média às jazidas de Dunito (km) | Agrominas | Custo ↓ | 5% | **Menor distância = melhor nota.** Complementa o critério de suprimento mineral. |
| **Logística** | Distância média aos polos agrícolas (km) | IBGE - CONAB | Custo ↓ | 15% | **Proximidade aos polos DPF aumenta pontuação.** Utiliza distância geodésica ponderada pelos polos A e B. |
| **Mercado** | Índice DPF (Demanda Potencial de Fertilizantes) | IBGE - MAPA | Potencial ↑ | 15% | **Maior DPF = maior potencial de mercado.** Calculado a partir das áreas de soja, milho, cana e café. |
| **Infraestrutura** | Proximidade de rodovias e portos (km) | DNIT - OpenStreetMap | Potencial ↑ | 10% | **Menor distância = maior acessibilidade.** Considera logística de exportação e escoamento nacional. |
| **Execução** | Zoneamento industrial e incentivos fiscais | Gov. estaduais - SEDE - SEDETEC | Potencial ↑ | 5% | **Pontuação qualitativa (0–1).** Locais com incentivos e área industrial = 1, sem = 0. |
| **Sustentabilidade** | Disponibilidade hídrica e uso do solo compatível | ANA - IBGE | Potencial ↑ | 5% | **Pontuação qualitativa (0–1).** Considera risco ambiental e compatibilidade com uso do solo. |

**Total:** 100 %


## Justificativa dos Pesos
Os pesos foram definidos com base na **estrutura estimada de custos do Termofosfato Magnesiano** (dados fornecidos pela Agrominas) e na relevância estratégica de cada grupo de decisão:

- **Energia (35%)** → Processo altamente intensivo em energia (≈ **R$ 500/t**). Preço e disponibilidade são determinantes para competitividade.  
- **Matéria-prima (15%)** → Fosfato (≈ **R$ 600/t**) e Dunito (≈ **R$ 100/t**) representam quase metade do custo produtivo, tornando a proximidade logística essencial.  
- **Logística (15%)** → Frete de insumos e distribuição final impactam até 25% do custo total.  
- **Mercado (15%)** → A demanda regional (índice DPF) assegura o escoamento do produto e reduz risco de ociosidade.  
- **Infraestrutura, execução e sustentabilidade (20%)** → Refletem a capacidade real de implantação e operação com menor risco regulatório.


## Critérios de Classificação Final

Cada localidade analisada será enquadrada conforme seu **Score** final em quatro níveis de atratividade:

| Faixa | Classificação | Interpretação |
|:--:|:--|:--|
| > 0.75 | **Nível A: Muito Alto** | Localidades altamente favoráveis (custo competitivo e alta demanda) |
| 0.50 – 0.75 | **Nível B: Alto** | Boa viabilidade, pequenas limitações de custo ou logística |
| 0.25 – 0.50 | **Nível C: Médio** | Localidades viáveis, mas com restrições de custo ou distância |
| < 0.25 | **Nível D: Baixo** | Regiões menos atrativas sob os critérios técnicos e econômicos |

## Referências
- **ANEEL.** Banco de Subestações e Tarifas por Distribuidora. Disponível em: [https://dados.aneel.gov.br](https://dados.aneel.gov.br). Acesso em: 06 nov. 2025.  
- **IBGE.** Produção Agrícola Municipal – PAM 2023. Disponível em: [https://sidra.ibge.gov.br/tabela/5457](https://sidra.ibge.gov.br/tabela/5457). Acesso em: 06 nov. 2025.  
- **MAPA.** *Plano Nacional de Fertilizantes 2050.* Brasília: Ministério da Agricultura, Pecuária e Abastecimento, 2022. Disponível em: [https://www.gov.br/agricultura/pt-br/assuntos/insumos-agropecuarios/insumos-agricolas/fertilizantes](https://www.gov.br/agricultura/pt-br/assuntos/insumos-agropecuarios/insumos-agricolas/fertilizantes). Acesso em: 06 nov. 2025.  
- **CONAB.** Séries Históricas de Produção Agrícola. Disponível em: [https://www.conab.gov.br](https://www.conab.gov.br). Acesso em: 06 nov. 2025.  
- **ANA.** Atlas das Águas – Recursos Hídricos e Uso do Solo. Disponível em: [https://www.gov.br/ana](https://www.gov.br/ana). Acesso em: 06 nov. 2025.  
- **DNIT.** Mapas Rodoviários Federais. Disponível em: [https://www.gov.br/dnit](https://www.gov.br/dnit). Acesso em: 06 nov. 2025.  
- **AGROMINAS.** Dados internos sobre jazidas de Fosfato e Dunito, fornecidos para a Sprint 1 do projeto.  