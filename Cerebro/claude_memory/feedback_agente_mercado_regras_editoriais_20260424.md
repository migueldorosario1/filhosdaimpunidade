---
name: Regras editoriais específicas do agente_mercado (2026-04-24)
description: Precisão temporal com data confirmada via API, nomes de fontes curtos, brapi pra cotações, identificar veículo original independente da ferramenta de coleta — e SÓ aplicam ao agente_mercado; outros temáticos seguem a regra geral "proibido data chumbada".
type: feedback
originSessionId: 44a64e7c-8100-4d13-873c-db75d49e9274
---
**Estabelecidas 2026-04-24 03:00-03:10 BRT via Manus↔Miguel.** Aplicam-se somente ao `agente_mercado.py`; não propagar pros outros temáticos.

## Regras

### 1. Precisão temporal — só com certeza absoluta via API
- Data + dia da semana explícitos no texto ("O Ibovespa encerrou o pregão desta quinta-feira, 23 de abril...") SÓ se confirmados por brapi (`regularMarketTime`) OU BCB SGS (`data` DD/MM/AAAA)
- Se nenhuma API retornar data parseável: OMITIR qualquer referência temporal precisa
- Regra de ouro: **melhor omitir do que inventar**
- Implementação em `agente_mercado.py:puxar_data_ref_confirmada()` — injeta `DATA_REFERENCIA_CONFIRMADA: <string>` no material bruto; prompt do LLM obriga usar EXATAMENTE essa string

### 2. Nomes editoriais curtos e diretos
- "Valor" (não "Valor Econômico")
- "Folha" (não "Folha de S.Paulo")
- "Bloomberg", "Reuters", "AP", "AFP" — direto
- "G1", "UOL", "O Globo", "Estadão", "CNN Brasil", "Poder360", "Carta Capital"
- Padrão jornalístico ágil, sem nomes longos/formais
- Mapa mantido em `util_fonte.DOMINIO_PARA_NOME_EDITORIAL`

### 3. brapi.dev pra cotações, NUNCA como "fonte" de notícia
- brapi é usada só pra número (Ibovespa via `_puxar_ibovespa_brapi`) e pra data confirmada
- Notícias seguem via Brave + RSS
- Atribuição de fonte no rodapé ("Com informações de ...") deve SEMPRE identificar o **veículo original** do texto (Valor, Folha, Bloomberg...), independente da ferramenta usada pra coletar (Google News RSS, Brave, feed direto, etc.)

### 4. Escopo limitado
**Why:** CLAUDE.md §5 é explícito — "Proibido data chumbada no lide" é regra GERAL pra todos os temáticos, justamente pra evitar alucinação. Agente_mercado é EXCEÇÃO porque os dados oficiais (BCB/brapi) confirmam a data.

**How to apply:** não adicionar `puxar_data_ref_confirmada()` ou `DATA_REFERENCIA_CONFIRMADA` nos outros temáticos (IA, Latam, Sheinbaum, Lula, Inflação, Matriz, etc.). Eles seguem com referência relativa ("nesta semana", "no cenário recente").

## Fallback "fonte primária" → "fonte original"
No `util_fonte.nome_amigavel_fonte`, o último recurso era devolver "fonte primária" — virou "fonte original" em 2026-04-24 porque estava virando rótulo padrão quando o resolver falhava (caso clássico: URLs `news.google.com/rss/articles/CBM...` que não resolvem via HEAD/GET porque o redirect é client-side JS).

## Pendências
- **Decoder de URLs GN** (base64 protobuf CBM...) — não implementado; URLs desse formato caem em "fonte original"
- **Blocklist estrutural de og:image de agregadores** (news.google.com, msn.com) no motor_publicador — Miguel não autorizou
- **Queries Wikimedia específicas** de pregão/câmbio — próxima iteração se autorizada
