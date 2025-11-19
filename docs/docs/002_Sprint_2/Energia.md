---
sidebar_position: 1
slug: /Sprint-2/Revisão-Energia
description: "Mudança na análize de preços de energia no Brasil e Paraguai incluindo o PDE 2034"
---

## Introdução
**Este relatório apresenta a atualização da Viabilidade energética por energia elétrica** da planta de **Termofosfato Magnesiano da Agrominas**, incorporando correções metodológicas e novas informações estratégicas sobre **custos e disponibilidade de energia**. Foram revisadas as **tarifas elétricas regionais** no Brasil e no Paraguai e integradas as **projeções do PDE 2034**.

As estimativas de consumo energético foram padronizadas para os cenários **50.000, 100.000 e 200.000 t/ano** e expressas em **MWh**, com correção das inconsistências entre potência e energia e explicitação das conversões adotadas (por exemplo, **MW médio → MWh/ano**). A **metodologia de cálculo do custo total em R$/kWh** está detalhada, incluindo a **soma dos componentes de energia e demanda** e a aplicação do **fator de carga 100%** para converter encargos de demanda em custo por energia consumida, assegurando comparabilidade entre estruturas tarifárias.

Realizou‑se uma **reavaliação comparativa dos custos por região** com critérios uniformes e foi elaborado um **ranking atualizado** considerando **tarifas, expansão de transmissão e riscos climáticos**. O relatório analisa impactos de restrições e expansão da rede sobre custo e segurança do suprimento e conclui com **recomendações fundamentadas** e referências oficiais para verificação.

Principais pontos:
- **Todas as estimativas de consumo** padronizadas para **MWh**.
- **Fontes tarifárias revisadas** com referência oficial para cada valor.
- **Custo total recalculado = energia + demanda convertida pelo fator de carga 100%**.
- **Ranking e recomendações** baseados em cálculos detalhados e riscos regionais.
- Referências oficiais (ANEEL, ANDE, PDE 2034) documentam os pressupostos.

Por exemplo:
- **1 MW médio por ano = 8.760 MWh/ano**
- Custo de demanda (R$/kW) → convertido para R$/kWh assumindo uso contínuo da demanda.
---

## 1. Consumo Energético da Planta – Cenários de Produção

A produção de Termofosfato Magnesiano, realizada por fusão térmica de fosfatos com magnésio em forno elétrico, demanda alto consumo de energia. Inicialmente, o consumo específico é de **~1,20 MWh/t**, reduzindo para **~0,90 – 0,95 MWh/t** com a estabilização do processo, o que representa uma queda de **20 – 25%** devido a melhorias operacionais e maior aproveitamento térmico. Fonte: [Relatório](../../extra/ConsumoEnergia.md)

Adotando um consumo médio de **~1,0 MWh/t**, estimam-se os seguintes valores anuais para diferentes escalas de produção:

| Produção (t/ano) | Consumo (MWh/ano) | Potência Média (MW) |
|------------------|-------------------|----------------------|
| 50.000           | ≈ 50.000          | ≈ 5,7                |
| 100.000          | ≈ 100.000         | ≈ 11,4               |
| 200.000          | ≈ 200.000         | ≈ 22,8               |

> **Nota:** 1 MW médio = 8.760 MWh/ano.

Considerando variações operacionais, os intervalos de consumo são:

- **50 mil t/ano:** 45–60 GWh/ano (5 – 7 MW médios)
- **100 mil t/ano:** 90-129 GWh/ano (10,3 – 14,7 MW médios)
- **200 mil t/ano:** 180–240 GWh/ano (20 – 28 MW médios)

Essas estimativas padronizadas facilitam o planejamento energético e a comparação entre cenários de produção.

---

Se quiser, posso adaptar esse conteúdo para apresentação ou incluir projeções de custo.


## Referências

1. Agência Nacional de Energia Elétrica – ANEEL. Portal de Tarifas e Resoluções Homologatórias (2024–2025).
   https://www.gov.br/aneel/pt-br/assuntos/tarifas

2. ANEEL – Ranking das Tarifas por Distribuidora.
   https://www.gov.br/aneel/pt-br/assuntos/tarifas/ranking-das-tarifas

3. ANDE – Administración Nacional de Electricidad. Tarifas Industriais (Média Tensão – 23 kV).
   https://www.ande.gov.py/tarifas_vigentes.php

4. ANDE – Pliego Tarifario Nº 21 (Atualizado em 27/11/2024).
   https://www.ande.gov.py/docs/tarifas/Pliego%20de%20Tarifas%20Nro%2021%20-%20Version%20Actualizada%2027-11-2024.pdf

5. Ministério de Minas e Energia (MME) / Empresa de Pesquisa Energética (EPE).
   [*PDE 2034 – Plano Decenal de Expansão de Energia*](../../extra/PDE2034.pdf)
   (Caderno de Transmissão: limites de intercâmbio, reforços NE–SE–S, capacidade de escoamento.)

6. ONS – Operador Nacional do Sistema Elétrico. Mapas do SIN.
   http://www.ons.org.br/paginas/sobre-o-sin/mapas

7. ONS – IPDO – Informativo Preliminar Diário da Operação (edições citadas no relatório).
   https://www.ons.org.br/AcervoDigitalDocumentosEPublicacoes

8. Documento interno: **Comparativo de Tarifas Industriais de Energia Elétrica (2025) – Brasil e Paraguai**.
   Arquivo fornecido pelo usuário – base usada para cálculos de R$/kWh, TE, TUSD/TUST e demanda.

9. Base de dados interna: **pesquisa_paralela_energia_industrial.csv**.
   (Faixa de consumo energético utilizada: 0,9–1,2 MWh/t; valores típicos de ramp-up vs. operação estável.)

10. IPT / FINEP. Estudos técnicos sobre consumo energético em processos térmicos e fertilizantes fosfatados.

11. OSTI.gov – Office of Scientific and Technical Information.
    *Estudos técnicos sobre consumo energético em fertilizantes e processos térmicos.*
    https://www.osti.gov/

12. Lista Completa de URLs – Pesquisa sobre Energia Industrial. Documento auxiliar  utilizado na validação das fontes. Em [URLs — Energia (Sprint 2)](../../extra/Urls.md)
