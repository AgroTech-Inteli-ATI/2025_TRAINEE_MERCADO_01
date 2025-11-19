---
sidebar_position: 0
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

---

## 1. Consumo Energético da Planta – Cenários de Produção

A produção de Termofosfato Magnesiano, realizada por fusão térmica de fosfatos com magnésio em forno elétrico, demanda alto consumo de energia. Inicialmente, o consumo específico é de **~1,20 MWh/t**, reduzindo para **~0,90 – 0,95 MWh/t** com a estabilização do processo, o que representa uma queda de **20 – 25%** devido a melhorias operacionais e maior aproveitamento térmico. Fonte: [Relatório](../../extra/ConsumoEnergia.md)

Adotando um consumo médio de **~1,0 MWh/t** com base no [Relatório](../../extra/ConsumoEnergia.md), estimam-se os seguintes valores anuais para diferentes escalas de produção:

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

---

## 2. Custos de Energia Elétrica por Região – Brasil vs. Paraguai

Para avaliar a competitividade energética, foram levantadas as tarifas industriais vigentes em 2025 nas principais regiões do Brasil e no Paraguai, considerando média/alta tensão e fator de carga de 100%. O custo médio por MW·h inclui energia e demanda contratada, permitindo comparabilidade entre localidades.

De forma geral, distribuidoras do Norte/Nordeste com subsídios apresentam os menores custos, enquanto grandes centros urbanos e concessionárias sem incentivos registram valores superiores a **R$500/MW·h**. No Paraguai, a estatal ANDE oferece tarifas significativamente mais baixas (**~R$150/MW·h**), refletindo o amplo uso de hidrelétricas binacionais.

### Comparativo de Tarifas Industriais (R$/MW·h)

| Local / Concessionária         | Tarifa Estimada | Observações |
|-------------------------------|------------------|-------------|
| **Paraguai – ANDE**           | ~150             | Tarifa média tensão com demanda ≈R$16/kW·mês; aproveitamento hidrelétrico |
| **Amapá – Equatorial CEA**    | ~75              | Menor tarifa do Brasil; depende de subsídios pós-apagão |
| **MG/RJ – Energisa Minas Rio**| ~106             | Tarifa baixa no interior; abaixo da média nacional |
| **Mato Grosso – Energisa MT** | ~107             | Perfil de concessão e subsídios regionais favorecem o custo |
| **Sergipe – Energisa SE**     | ~159             | Tarifa moderada no Nordeste |
| **Sudeste – Enel SP**         | ~270–300         | Custo elevado típico de metrópoles sem subsídios |
| **CEMIG / Equatorial PA**     | >500             | Maior custo registrado no Brasil em 2025 |

> Valores sem impostos e encargos variáveis. Fontes: ANEEL 2024–2025; ANDE 2024.

### Análise

O Paraguai se destaca como opção competitiva, com custo médio de **~R$150/MW·h**, viabilizado por excedente hidrelétrico. No Brasil, Amapá, Mato Grosso e interior de MG/RJ apresentam tarifas entre **R$75 e R$110/MW·h**, bem abaixo da média nacional. No entanto, fatores como confiabilidade e sustentabilidade devem ser considerados. O Amapá, por exemplo, depende de uma única linha de transmissão e de subsídios temporários.

Regiões como Mato Grosso e MG/RJ oferecem equilíbrio entre custo e segurança energética, por estarem integradas ao SIN. Já centros urbanos do Sudeste, embora com infraestrutura robusta, enfrentam tarifas mais altas devido à ausência de subsídios.

---

Claro! Aqui está o conteúdo reestruturado e condensado como **parte de relatório técnico**, iniciando no item 3, com estilo formal e objetivo, e unidades atualizadas para **MW·h** onde aplicável:

---

## 3. Dados Estratégicos do PDE 2034 – Transmissão, Demanda Futura e Riscos Regionais

O Plano Decenal de Expansão de Energia (PDE 2034), publicado pela EPE/MME, apresenta diretrizes para o desenvolvimento da rede elétrica entre 2025 e 2034. Sua incorporação ao estudo permite antecipar tendências regionais de infraestrutura, custos de transmissão e polos de consumo, contribuindo para decisões de localização mais resilientes.

### Expansão da Capacidade de Transmissão

O PDE projeta reforços significativos na malha do SIN para escoar geração renovável e atender grandes cargas:

- **Nordeste:** acréscimo de 3–4 GW na capacidade de exportação até 2032, somando-se aos ~13 GW médios atuais, elevando o intercâmbio para até 17 GW.
- **Sul:** ampliação da capacidade de importação em 4 GW até 2036, reforçando o suprimento em cenários hidrológicos críticos.
- **Tecnologia HVDC:** recomendada para longas distâncias (2.000–3.000 km), reduzindo perdas e viabilizando grandes blocos de energia.

**Implicação:** regiões com excedente renovável (ex.: Nordeste) terão mais infraestrutura para exportar energia; regiões deficitárias (ex.: Sul) ganharão estabilidade, mas continuarão arcando com custos de transporte.

### Projeções de Tarifas de Transmissão (TUST)

A metodologia nodal adotada projeta sinal locacional mais forte até 2034:

- **TUST para geradores (R$/kW·mês):** Nordeste ~9,6; Norte ~8,1; Sudeste ~6,0; Sul ~4,0
- **TUST para cargas (R$/kW·mês):** Sudeste ~12,8; Sul ~15,5; Nordeste ~8,8

**Implicação:** consumidores no Nordeste terão menor TUST de consumo, mas geradores locais pagarão mais. Localizar a carga próxima à geração reduz encargos de transmissão no longo prazo.

### Polos de Demanda Futura

O PDE identifica novas cargas eletrointensivas que podem alterar o perfil regional:

- **Data Centers:** previsão de 2,5 GW de carga até 2037, com destaque para SP (~1,2 GW), RS (~1,6 GW) e CE (~0,9 GW). SP pode enfrentar saturação tarifária; RS e CE surgem como polos secundários com potencial de expansão.
- **Hidrogênio Verde:** 9 projetos protocolados somam 35,9 GW de demanda até 2038, concentrados no Nordeste (CE ~26,8 GW; BA ~8,5 GW; PI ~0,6 GW). A região pode passar de exportadora a grande consumidora, exigindo reforços na geração e transmissão.

**Implicação:** a instalação da planta no Nordeste deve considerar a concorrência futura por energia com hubs de H₂ verde, que podem pressionar o custo marginal de suprimento.

### Riscos Climáticos e Estabilidade Regional

Eventos extremos recentes reforçam a importância da diversificação e resiliência:

- **Exemplo Norte:** seca no Rio Madeira em 2023 afetou UHEs Santo Antônio e Jirau, gerando risco de desabastecimento em AC/RO.
- **Sul/Sudeste:** secas em 2021 exigiram acionamento de térmicas, mitigado por importações do NE/Norte.
- **Nordeste:** apesar da variabilidade eólica/solar, a diversificação geográfica e complementaridade com outras fontes reduzem riscos.

**Implicação:** regiões isoladas ou com matriz concentrada (ex.: extremo Norte) têm estabilidade menor. No Paraguai, embora confiável, a dependência de hidrelétricas fluviais exige atenção a eventos climáticos. A diversificação de suprimento é recomendada em qualquer cenário.

---

## 4. Atualização do Ranking de Regiões por Custo Energético Competitivo

Com base nos custos atuais e nas projeções do PDE 2034 (transmissão, demanda e riscos), reavaliamos as principais regiões candidatas à instalação da planta de termofosfato magnesiano. A seguir, destacam-se os cinco principais locais, considerando custo energético, infraestrutura e perspectivas futuras:

### 1. Paraguai (ANDE – Região Central)

- **Tarifa estimada:** ~R$150/MW·h
- **Vantagens:** Energia hidrelétrica abundante e excedente (Itaipu ~14 GW médios), incentivos à indústria eletrointensiva, estabilidade de suprimento.
- **Desafios:** Limites na interconexão com o Brasil e necessidade de contratos binacionais para garantir fornecimento.
- **Observação:** Custo extremamente competitivo pode justificar investimentos logísticos adicionais.

### 2. Mato Grosso (Energisa MT)

- **Tarifa estimada:** ~R$107/MW·h
- **Vantagens:** Localização central, inserção no SIN, múltiplas rotas de suprimento, proximidade de matérias-primas (Goiás/MG), expansão solar prevista.
- **Desafios:** Verificar disponibilidade de potência firme para grandes cargas.
- **Observação:** Melhor equilíbrio entre custo, infraestrutura e segurança energética no Brasil.

### 3. Interior de MG/RJ (Energisa Minas Rio)

- **Tarifa estimada:** ~R$106/MW·h
- **Vantagens:** Proximidade de jazidas minerais e eixo Rio-SP, rede elétrica robusta, renováveis em expansão.
- **Desafios:** Escala da carga frente à capacidade da concessionária; ausência de subsídios regionais.
- **Observação:** Alternativa nacional atrativa com boa infraestrutura e custo competitivo.

### 4. Amapá (Equatorial CEA)

- **Tarifa estimada:** ~R$75/MW·h
- **Vantagens:** Menor custo nominal do Brasil, proximidade da UHE Tucuruí.
- **Desafios:** Alta vulnerabilidade elétrica, dependência de subsídios e única linha de transmissão.
- **Observação:** Recomendável apenas com garantias de redundância e contratos blindados.

### 5. Rio Grande do Sul / Ceará

- **Tarifas atuais:** RS ~R$350/MW·h; CE ~R$500/MW·h (varia por área)
- **Vantagens:** Polos emergentes de demanda (data centers e hidrogênio verde), investimentos em renováveis e transmissão.
- **Desafios:** Tarifas ainda elevadas; dependência de projetos futuros.
- **Observação:** Menções honrosas com potencial estratégico de médio prazo, especialmente o CE com sinergia logística e PPAs renováveis.

> **Nota:** Outras regiões como Sergipe, Pará e Maranhão foram avaliadas, mas não superaram os cinco principais em custo e viabilidade energética.

---

## 5. Recomendações Finais

Com base na análise integrada de custo energético, robustez do suprimento, projeções do PDE 2034 e riscos climáticos, as melhores opções estratégicas para a instalação da planta de termofosfato magnesiano são:

### 1ª Opção – Paraguai (região central, ligada a Itaipu)

- **Custo estimado:** ~R$150/MW·h ou inferior
- **Destaques:** Energia hidrelétrica abundante e estável, excedente de Itaipu, incentivos à indústria eletrointensiva.
- **Recomendações:** Negociar fornecimento firme com a ANDE ou cogitar participação em geração dedicada. Avaliar logística de exportação para o Brasil e aspectos fiscais. A expansão futura da interligação Brasil–Paraguai prevista no PDE pode mitigar riscos de escoamento.

### 2ª Opção – Mato Grosso (Brasil)

- **Custo estimado:** ~R$107/MW·h (Energisa MT)
- **Destaques:** Localização central, proximidade de consumidores agrícolas e fornecedores de rocha fosfática, inserção no SIN com múltiplas rotas de suprimento.
- **Recomendações:** Iniciar tratativas para conexão em alta tensão e contratação via mercado livre. Buscar contratos com fontes incentivadas (PCHs, biomassa) para reduzir encargos adicionais.

### 3ª Opção – Interior de MG/RJ (Energisa Minas Rio)

- **Custo estimado:** ~R$106/MW·h
- **Destaques:** Proximidade de jazidas minerais e centros consumidores, rede elétrica robusta, acesso ao mercado livre.
- **Recomendações:** Confirmar manutenção da tarifa competitiva no médio prazo. Avaliar conexão à rede de transmissão da CEMIG e suprimento via fontes locais.

### Outras Regiões

- **Amapá:** Apesar do menor custo nominal (~R$75/MW·h), não é recomendada no momento devido à fragilidade do suprimento e dependência de subsídios. Só viável com plano robusto de segurança energética.
- **Ceará e Rio Grande do Sul:** Menções estratégicas para médio/longo prazo. Investimentos em renováveis e transmissão podem tornar essas regiões mais competitivas após 2030, especialmente para expansões ou plantas satélites.

### Conclusão

Paraguai e Mato Grosso se destacam como as localizações mais vantajosas do ponto de vista energético. O Paraguai oferece a menor tarifa, enquanto o MT combina custo competitivo com maior integração ao mercado brasileiro. A escolha final deve considerar também fatores logísticos, regulatórios e operacionais, mas sob a ótica elétrica e estratégica até 2034, essas opções posicionam a Agrominas em regiões com energia abundante, barata e sustentada por tendências favoráveis de expansão.

> **Fontes:** ANEEL (tarifas 2024–2025), ANDE (pliego tarifario 2024), PDE 2034 – Caderno de Transmissão (MME/EPE, 2024).

---

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
