---
sidebar_position: 2
slug: /Sprint-2/custos-consolidados
description: "Planilha e documentação dos custos consolidados da Sprint 2"
---

# Planilha de Custos Consolidados - Sprint 2

## Objetivo
Esta seção detalha a composição completa dos custos associados à operação industrial da planta de termofosfato, incorporando os três grupos principais de custos operacionais diretos:

- Custo da matéria-prima entregue
- Custo de energia elétrica por região candidata
- Custo logístico de distribuição para acesso ao mercado agrícola

A metodologia adotada reflete as correções e orientações da Sprint Review 1, conforme registrado no arquivo
`Considerações_Sprint1.md`.

---

## Custo da Matéria-Prima Entregue (MP + Frete)

A análise considera as três matérias-primas essenciais:
1. Fosfato (67% participação no termo final)
2. Dunito (33% participação)
3. Sílica (quantidade auxiliar, baixo custo)

### Metodologia

O custo total da MP entregue é calculado como:

``VALOR_TOTAL_MP_ENTREGUE = PREÇO_MP_BASE + (DISTÂNCIA × TARIFA_R$/t.km)``

Onde:

- PREÇO_MP_BASE:
  - Fosfato: R$ 900/t
  - Dunito: R$ 300/t
   - Sílica: R$ 150/t

- Tarifa de frete rodoviário:
  - R$ 0,03 / t . km (valor conservador baseado em tabelas ANTT e benchmarking interno)

As distâncias foram obtidas via análise geográfica e rotas rodoviárias (Google Maps).