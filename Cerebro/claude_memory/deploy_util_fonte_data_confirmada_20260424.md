---
name: Deploys 2026-04-24 — util_fonte editorial + data confirmada mercado + Flickr B3
description: 3 mudanças em produção Tencent Cingapura — util_fonte.py com dicionário editorial+resolver, agente_mercado.py com puxar_data_ref_confirmada, robo_coleta_imagens.py com NSIDs bovespa+b3socialmedia. Post 238816 imagem destacada trocada (239031 em vez de 238815 que era logo Google News).
type: project
originSessionId: 44a64e7c-8100-4d13-873c-db75d49e9274
---
**Deploy 2026-04-24 02:30 BRT.** Todas as mudanças ativas antes do cron `agente_mercado` das 15:30 do mesmo dia.

## Contexto
Miguel via Manus identificou no post 238816 (agente_mercado de 23/04) que a featured image era literalmente o **logo do Google News** (webp 300x300 cartões coloridos). Pediu troca + auditoria de conteúdo + novas regras editoriais.

**Why:** primeiro post premium com nova config brapi+BCB (pós-migração yfinance de 2026-04-23) mostrou dois buracos: (1) og:image de agregador passa direto pelo Tribunal Visual, (2) banco SQLite de 103k imagens não tinha hits bons pra Ibovespa/B3/Bovespa.

**How to apply:** auditar próximos posts do agente_mercado pra verificar se as 3 correções funcionaram.

## Mudanças deployadas

### 1. util_fonte.py (3.503 → 7.140 bytes)
- Dicionário `DOMINIO_PARA_NOME_EDITORIAL` com 50+ veículos (nomes editoriais curtos conforme regra de Miguel)
- Função `resolver_url_final(url, timeout=6)` segue redirects (HEAD→GET fallback)
- Detecta agregadores via `_DOMINIOS_AGREGADOR` (news.google.com, msn.com, yahoo, flipboard, smartnews, feedly)
- Se URL é agregador, resolve antes de mapear
- Fallback "fonte primária" virou "fonte original"
- Backup: `util_fonte.py.bak_pre_resolver_20260424_022957`

### 2. agente_mercado.py (7.801 → 11.156 bytes)
- `puxar_data_ref_confirmada()` consulta brapi (`regularMarketTime`) → BCB fallback
- Converte pra "quinta-feira, 23 de abril de 2026" via tabelas PT-BR hardcoded (sem locale)
- Injeta `DATA_REFERENCIA_CONFIRMADA: <string>` no cabeçalho do material bruto
- Prompt pro LLM: regra dura "use EXATAMENTE essa string, NÃO invente, NÃO aproxime"
- Se brapi+BCB falharem: prompt muda pra "use apenas 'no fechamento desta sessão' / 'no pregão de hoje'"
- Backup: `agente_mercado.py.bak_pre_data_confirmada_20260424_022957`

### 3. robo_coleta_imagens.py — FLICKR_PERFIS_NSID
- `bovespa`: `7936086@N04` (3 fotos únicas) — conta "Bovespa" oficial antiga no Flickr
- `b3socialmedia`: `56348594@N07` (0 fotos hoje, monitora futuro)
- Coleta rodada 2026-04-24 02:31 BRT: +3 fotos no banco (103706 → 103709)
- **Limitação descoberta:** B3 mantém quase nada no Flickr. Fonte melhor seria Agência Brasil, Getty free, ou WMC com queries específicas
- Backup: `robo_coleta_imagens.py.bak_pre_b3_20260424_022957`

## Também feito
- **Post 238816:** featured_media trocado de 238815 (logo GN) para **239031** (sede B3 São Paulo por Rafael Matsunaga via WMC, CC BY 2.0, 1600x849px)
- **Banco alimentado parcial (opção B):** 14 queries WMC financeiras rodadas, +94 imagens (só ~10 relevantes, principalmente BCB sobre Selic). Queries "Bolsa de Valores B3 / dólar real moeda / Selic taxa juros / Banco Central Brasil" estavam no coletor desde antes mas nunca haviam rodado (count=0) — mistério não investigado

## Testes em produção pós-deploy
- `util_fonte.nome_amigavel_fonte("https://valor.globo.com/...")` → "Valor" ✅
- `util_fonte.nome_amigavel_fonte("https://reuters.com/...")` → "Reuters" ✅
- `agente_mercado.puxar_data_ref_confirmada()` → "sexta-feira, 24 de abril de 2026" ✅ (data atual da brapi)

## Fact-check do post 238816 (23/04 15:30)
3 pontos duvidosos verificados via WebSearch:
- ✅ Copom 28-29/04/2026 (278ª reunião)
- ✅ Petróleo >US$100 (Brent 103,03 / WTI 93,72 em 23/04)
- ✅ Tensão Ormuz + EUA-Irã (marinha interceptando petroleiros iranianos)

Sem alucinação no texto — problema era só a imagem.

## Pendências não autorizadas
- Opção D: blocklist estrutural de og:image de agregadores no `motor_publicador`
- Decoder CBM-base64 de URLs `news.google.com/rss/articles/`
- Queries WMC mais específicas pra pregão/câmbio
