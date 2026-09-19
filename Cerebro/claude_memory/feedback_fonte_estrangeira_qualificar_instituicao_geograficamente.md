---
name: feedback-fonte-estrangeira-qualificar-instituicao-geograficamente
description: "Quando a matéria vem de fonte estrangeira, sempre qualificar geograficamente a instituição com nome genérico na 1ª menção (título e corpo) para evitar ambiguidade"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: cf4e142a-050c-46de-b793-bee2464fc7f7
---

**🌍 Regra de desambiguação geográfica de instituições em matérias de fonte estrangeira:**

Quando a matéria tem **fonte estrangeira** (SCMP, Prensa Latina, The Hindu, Al Jazeera, Xinhua, Reuters, Actualidad RT, etc.) E menciona uma instituição com nome **genérico** que existe em vários países (Tesouro Nacional, Banco Central, Ministério da Fazenda, Suprema Corte, Congresso, Ministério das Relações Exteriores, Câmara dos Deputados, Senado, Guarda Costeira, Marinha, Exército, Polícia Federal, Ministério Público...), **sempre qualificar geograficamente** na 1ª menção do TÍTULO e do CORPO — mesmo que o resto da matéria deixe claro pelo contexto.

Exemplos:
- ❌ "Tesouro Nacional passará a emitir títulos em yuan na China todo ano" (leitor pode ler como Tesouro CHINÊS)
- ✅ "Tesouro Nacional do Brasil passará a emitir títulos em yuan na China todo ano"
- ❌ "Ministério da Fazenda anuncia parceria com Pequim" 
- ✅ "Ministério da Fazenda do Brasil anuncia parceria com Pequim"
- ❌ "Suprema Corte suspende medida presidencial" (em matéria sobre Colômbia)
- ✅ "Suprema Corte da Colômbia suspende medida presidencial"

Corpo pode usar aposto explicativo na 1ª menção: `"o Tesouro Nacional do Brasil — órgão do Ministério da Fazenda responsável pela dívida pública federal — decidiu..."`. Nas menções seguintes, pode voltar ao nome curto (`"o Tesouro"`, `"o governo brasileiro"`) porque o contexto já foi estabelecido.

**Why:** Miguel 06/08/2026 00:15 BRT flagou o post 264426 publicado no ciclo 19:47 de 05/08 com título "Tesouro Nacional passará a emitir títulos em yuan na China todo ano para abrir caminho a empresas" — matéria correta, mas ambiguidade geográfica no título fazia parecer que a notícia era sobre o Tesouro Nacional CHINÊS. A ambiguidade é agravada quando (a) fonte é estrangeira (SCMP), (b) contexto da matéria é o país estrangeiro (China), e (c) instituição tem nome que existe em vários países.

**How to apply:**
- Na checagem dupla V4 (todos os ciclos, DIA e NOITE): sempre que aplicar `Segundo o [SCMP/Prensa Latina/The Hindu/etc]`, revisar título e primeiro parágrafo em busca de instituições brasileiras (ou terceiro país) com nome genérico. Adicionar qualificador geográfico.
- Instituições brasileiras que MAIS pedem qualificação em matérias sobre China/EUA/países estrangeiros: Tesouro Nacional, Banco Central, Ministério da Fazenda, Ministério das Relações Exteriores, Supremo Tribunal Federal (talvez menos, "STF" costuma bastar), Polícia Federal, Ministério Público, Congresso Nacional.
- Instituições estrangeiras que MAIS pedem qualificação em matérias sobre elas: Tesouro americano/chinês, Banco Central Europeu vs Banco Popular da China vs Reserva Federal, Suprema Corte da Colômbia/EUA/Israel, Ministérios de Justiça.
- Regra irmã de [[feedback-checagem-titulo-semantica-e-genero-fonte]] (que já cobre gênero fonte, verbo específico, tempo verbal x data, peso editorial) — agora estende cobertura pra desambiguação geográfica.
- Aplicar retroativamente APENAS se Miguel pedir (correção in-place preserva URL indexada, é reversível via backup).
