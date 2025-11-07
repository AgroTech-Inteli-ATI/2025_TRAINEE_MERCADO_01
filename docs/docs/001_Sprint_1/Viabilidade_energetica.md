---
sidebar_position: 1
slug: /Sprint-1/viabilidade-energética
description: "Viabilidade energética tanto por energia elétrica quanto por gás natural"
---

# Viabilidade energética tanto por energia elétrica quanto por gás natural

## Objetivo

O objetivo é identificar a localização ideal para a fábrica de Termofosfato Magnesiano, priorizando a **viabilidade energética** para a operação do forno de fusão, que requer uma fonte térmica de alta potência (1.350 °C a 1.500 °C)

### Requisito de Demanda Energética

A planta demanda uma infraestrutura energética robusta, com as seguintes estimativas anuais para a produção de 200.000 t/ano:
*   **Rota Elétrica:** Consumo de ~180 GWh/ano, exigindo uma **Subestação Elétrica (SE) dedicada com capacidade ≥ 30 MVA**.
*   **Rota Gás Natural:** Consumo de ~200 milhões Nm³/ano. Esta rota é economicamente mais competitiva (~R$ 50 milhões/ano) do que a rota elétrica (~R$ 90 milhões/ano). - **Embora eu estudei sobre isso, isso nao sera viavel caso nao se posicione em uma cidade com gasoduto disponivel, oq mata o potenciais economias com o frete. mesma coisa o contrario mandar caminhoes de gas para o local**

#### Contexto Regulatário e Mercado Livre de Gás Natural

A implementação da Nova Lei do Gás (Lei nº 14.134/2021) fomenta a abertura do mercado, permitindo que grandes consumidores industriais negociem o fornecimento diretamente com produtores e comercializadores. Esse novo arranjo tende a reduzir custos de suprimento e aumentar a previsibilidade contratual, tornando a rota a gás natural ainda mais atrativa para projetos de alto consumo térmico, como o da Agrominas.

## Metodologia

A metodologia se concentra na análise da infraestrutura de energia elétrica e gás natural na microrregião de Pratápolis, integrando dados de capacidade e disponibilidade.

### Base de Dados e Ferramentas para Análise Energética

1.  **Análise Elétrica:** Mapeamento das subestações da Cemig na microrregião (Pratápolis, Itaú de Minas, Passos, Cássia), avaliando a **Capacidade Instalada (MVA)** e a **Disponibilidade** para suportar a carga de 30 MVA.
2.  **Análise de Gás Natural:** Pesquisa sobre a rede de distribuição da Gasmig, com foco na expansão do gasoduto Centro-Oeste, que atende a região de **Passos/MG**.

### Interpretação do Artigo Científico (Deng et al., 2023)

O artigo **"Harmonized and Open Energy Dataset for Modeling a Highly Renewable Brazilian Power System"** valida a importância de utilizar **dados abertos e espacialmente explícitos** para a modelagem de sistemas de energia. Para o projeto Agrominas, isso reforça a necessidade de analisar a **capacidade instalada (MVA)** e a **disponibilidade** das subestações locais como o principal critério para identificar pontos de conexão viáveis para a demanda de 30 MVA.

## Visualizações

### Capacidade de Transferência de Energia entre Regiões

<p style={{textAlign: 'center'}}>Capacidade de Transferência de Energia entre Regiões</p>
<div style={{margin: 25}}>
    <div style={{textAlign: 'center'}}>
    <img src={require("../../static/img/transmissao.webp").default} />
</div>
</div>
<p style={{textAlign: 'center'}}>Fonte: https://www.nature.com/articles/s41597-023-01992-9#Ack1 </p>

*Figura: Capacidade de transferência de energia entre regiões do Brasil, com linhas de corrente alternada (AC) em azul e corrente contínua de alta tensão (HVDC) em laranja. As espessuras representam a capacidade de fluxo entre os principais nós do Sistema Interligado Nacional (SIN), em gigawatts (GW). Fonte: Deng et al., 2023.*

O mapa sintetiza as conexões de transmissão do SIN, destacando a infraestrutura de alta capacidade entre as regiões Sudeste, Sul e Centro-Oeste, responsáveis pela maior parte do intercâmbio energético nacional. As linhas HVDC, em laranja, são usadas para longas distâncias, garantindo eficiência e menor perda. Essa representação é usada em modelos de planejamento energético para indicar como a energia flui entre blocos regionais, servindo de base para estudos de expansão e segurança do sistema elétrico.

### Capacidade de geração de energia existente e planejada por tipo

<p style={{textAlign: 'center'}}>Capacidade de geração de energia existente e planejada por tipo</p>
<div style={{margin: 25}}>
    <div style={{textAlign: 'center'}}>
    <img src={require("../../static/img/geracao.webp").default} />
</div>
</div>
<p style={{textAlign: 'center'}}>Fonte: https://www.nature.com/articles/s41597-023-01992-9#Ack1 </p>

*Figura: Localização e capacidade das usinas de geração de energia elétrica no Brasil, classificadas por tipo de fonte (hidrelétrica, eólica, solar, térmica, biomassa, nuclear etc.) e tamanho relativo em megawatts (MW). Fonte: Deng et al., 2023.*

A figura apresenta a distribuição espacial das usinas de geração no Brasil. Observa-se a predominância de grandes usinas hidrelétricas no Centro-Sul e de fontes eólicas e solares no Nordeste. As áreas com círculos maiores indicam plantas de maior potência instalada. Esse panorama mostra como o sistema é fortemente concentrado em regiões já integradas à malha de transmissão, e ajuda a compreender onde há maior disponibilidade de energia firme e infraestrutura consolidada.

### Rede de gasodutos exitente e planejada

<p style={{textAlign: 'center'}}>Capacidade de geração de energia existente e planejada por tipo</p>
<div style={{margin: 25}}>
    <div style={{textAlign: 'center'}}>
    <img src={require("../../static/img/gas.png").default} />
</div>
</div>
<p style={{textAlign: 'center'}}>Fonte: https://www.epe.gov.br/pt/abcdenergia/planejamento-energetico-e-a-epe </p>

*Figura: Infraestrutura nacional de transporte de gás natural, com gasodutos existentes, em construção e planejados, terminais de GNL e áreas de concessão de distribuição estadual. Fonte: EPE, 2016.*

O mapa apresenta a rede de gasodutos de transporte e terminais de gás natural liquefeito (GNL), evidenciando a concentração da malha no Sudeste e Nordeste. As linhas contínuas indicam gasodutos em operação, enquanto as tracejadas mostram projetos em construção ou avaliação. A figura também traz as áreas de concessão das principais distribuidoras estaduais, como Gasmig, Comgás e Cegás, que estruturam o acesso regional ao gás natural no país.

## Estrutura de Variáveis e Critérios

O pilar **Energia** é o principal fator de desempate na escolha da localização:

| Variável (Pilar) | Critério de Avaliação | Requisito Mínimo / Fator de Ponderação |
| :--- | :--- | :--- |
| **Energia Elétrica** | Capacidade da Subestação (SE) | **≥ 30 MVA** (Fator Eliminatório) |
| | Tensão de Conexão | Alta Tensão (AT) ou Média Tensão (MT) |
| **Gás Natural** | Acesso à rede canalizada (Gasmig) | **Proximidade do gasoduto (Passos/MG)** (Alto Peso, rota mais competitiva) |
| **Infraestrutura** | Proximidade de Polo Técnico/Mão de Obra | Proximidade de Passos/MG (Mão de obra com experiência em processos térmicos) |

## Critérios de Classificação Final

O critério de classificação final é a **viabilidade e o custo da infraestrutura energética**.

### Fatores de Desempate Energético

1.  **Acesso ao Gás Natural:** A rota a gás natural é a mais competitiva economicamente. A proximidade do vetor de expansão da Gasmig (Passos) é um diferencial estratégico, tornando as localidades com menor distância de Passos mais atrativas.
2.  **Capacidade de Carga Elétrica:** A confirmação de capacidade disponível (MVA) nas subestações locais acima do requisito de 30 MVA é essencial. Localidades como **Itaú de Minas** e **Passos** possuem subestações de maior porte ou estão em eixos de reforço de rede.
3. **Distância**.

## Resultados

| Posição | Localidade (Município) | Fator Crítico (Energia) | Vantagem Energética Revisada |
| :--- | :--- | :--- | :--- |
| **1** | **Pratápolis (MG) - Zona Industrial** | Necessidade de confirmação da capacidade final (≥ 30 MVA). | Reforço recente na subestação local. Máxima proximidade da matéria-prima. |
| **2** | **Itaú de Minas (MG)** | **Capacidade da SE local (≥ 30 MVA) a ser confirmada.** | Proximidade da SE e da matéria-prima. |
| **3** | **Passos (MG) - Eixo Industrial Sul** | Distância da mina (aprox. 60 km) aumenta custo logístico. | **Infraestrutura de transmissão de 138 kV (125 MVA) na região.** Forte incentivo fiscal (ver documento separado). |
| **4** | **Cássia (MG) - Eixo Rodoviário** | Distância da mina (aprox. 30-40 km). | Acesso à infraestrutura elétrica (SE e UFV) e proximidade da linha de transmissão de 138 kV. |

**Recomendação:** A decisão final deve ser baseada na **confirmação da capacidade de 30 MVA** nas subestações de Pratápolis e Itaú de Minas. Caso a capacidade não seja confirmada, a opção de Passos, apesar do custo logístico, torna-se mais atrativa devido à infraestrutura de transmissão regional e ao forte apoio governamental (ver documento separado).

## Referências

- Agrominas Fertilizantes. *Estudo de Localização – Fábrica de Termofosfato Magnesiano (200.000 t/ano)*. Documento de Projeto, 2025.
- Deng, Y., Cao, K.K., Hu, W.X. et al. *Harmonized and Open Energy Dataset for Modeling a Highly Renewable Brazilian Power System*. Sci Data 10, 187 (2023). Disponível em: https://www.nature.com/articles/s41597-023-01992-9.
- Agrominas Fertilizantes. *[ATI]ENTREGÁVEISAGROMINAS1.pdf*. Documento de Entregáveis, 2025.
- Gasmig. *Obras da Linha Tronco gasoduto Centro-Oeste estão na etapa final*. Notícia Institucional, 2025.
- Decreto nº 11.388, de 16/10/1968. *Declara de utilidade pública, para efeito de desapropriação, terrenos necessários à construção da subestação de energia elétrica da cidade de Itaú de Minas*. Legislação Mineira.
- Ministério de Minas e Energia (MME). *Portaria SPE nº 001/2017*. Documento de Distribuição, 2017.
- Planejamento Energético e a EPE. Disponivel em: https://www.epe.gov.br/pt/abcdenergia/planejamento-energetico-e-a-epe

## Creditos

Este documento foi elaborado com foco na análise da infraestrutura energética e logística, integrando os dados de projeto da Agrominas Fertilizantes e AgroTech Inteli.

A metodologia de análise geoespacial e a ênfase na utilização de dados abertos e espacialmente explícitos para a tomada de decisão em sistemas de energia foram inspiradas e validadas pelo trabalho de **Deng, Y. et al. (2023)**, publicado na *Scientific Data* (Nature), conforme citado na seção de Metodologia.
