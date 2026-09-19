---
name: escopo-fontes-oficiais-br-completo
description: "Fontes oficiais brasileiras têm escopo amplo — nunca reduzir ao \"mais óbvio\" sozinho. ComexStat=comércio exterior TOTAL Brasil×todos países×todos produtos; IBGE=inflação+desemprego+PIB+PNAD+atividade+agro+demografia; BCB=centenas de séries; FRED=idem."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: beb43678-1786-4fd7-84cc-38077fa7ec3a
---

Fontes oficiais brasileiras (e equivalentes estrangeiras) têm escopo amplo e multidimensional. Nunca começar um desenho de coletor limitando a fonte ao "que parece mais óbvio" num primeiro recorte.

**Escopos corretos** (referência rápida):

- **ComexStat (MDIC/SECEX)**: Comércio exterior TOTAL do Brasil — exportações + importações, com TODOS os países (China, EUA, Argentina, UE, Mercosul, etc.), TODOS os produtos (código NCM), por UF de origem/destino, por via de transporte. Não é "só Brasil-China".
- **IBGE**: Sistema estatístico completo. Inclui: inflação (IPCA + IPCA-15 + INPC), mercado de trabalho (PNAD Contínua = desemprego + renda + informalidade), contas nacionais (PIB trimestral + anual), indicadores de atividade (PMC comércio, PMS serviços, PIA indústria), agro (PAM lavouras, PPM pecuária, PEVS extrativa), demografia (Censo + estimativas anuais). Não é "só inflação".
- **BCB SGS**: Centenas de séries além de Selic + câmbio: dívida pública, reservas internacionais, crédito (bens pessoais, veículos, imóveis), expectativas de mercado (Focus), institucionais financeiras, etc.
- **FRED (Fed Reserve)**: Equivalente americano — Fed Funds + CPI + desemprego + PCE + GDP + centenas de outras.
- **ANP**: Petróleo + gás + combustíveis + biocombustíveis + preços de revenda.

**Why:** Miguel corrigiu 2026-06-19 18:10 BRT quando propus `coletor_ibge.py` reduzido a IPCA/IPCA-15/PIB e falei de `coletor_comexstat.py` como se fosse Brasil-China. Frase dele: "Não, mas o Comercio State não é só Comércio Exterior Brasil-China. É o Comércio Exterior total do Brasil, com todos os países do mundo, todos os produtos do Brasil. O IBGE não é só inflação, é também desemprego, são várias coisas. Você sabe, né?"

**How to apply:**
- Ao desenhar qualquer coletor/schema de fonte oficial, primeiro enumerar TODAS as séries/indicações relevantes (wiki/websearch se preciso) antes de delimitar escopo.
- Apresentar ao Miguel o leque completo primeiro e perguntar quais entram no MVP vs Fase 2 — não decidir sozinho o recorte.
- Em schemas SQLite: tabelas ComexStat/UN Comtrade precisam de granularidade multidimensional (data, país, produto/NCM, UF), NÃO são séries temporais simples.
- Em schemas IBGE: no mínimo incluir PNAD Contínua (desemprego) junto com IPCA + PIB — são as 3 pautas macro mais quentes editorialmente.
- Relacionado: [[reference_reforma_arquitetura_produtor_unico_diretrizes_json]] e o desenho da Sprint Criativos V1 (`forum_agentes_criativos_estatistico_brutas_plus_20260619.md`).
