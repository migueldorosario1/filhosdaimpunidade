# Fórum — Painel /v6/youtube com abas internas + Transkriptor fora do menu (ZM-20260905-009)

**Ordem do Miguel** (05/09 ~12:1x, depois de ver a /v6/youtube): "melhor mais simples — abas internas: Publicado, Rascunho e Canais (nacionais e internacionais). Remover do menu o transkriptor, porque esse YouTube substituiu o transkriptor."

## O que mudou

**Página `/v6/youtube`** (`~/cafezinho/v6/painel_cctv_v6.py` na Tencent, backup `.bak_abas_youtube_20260905`, commit `7c1db79` no repo cafezinho → origin):
- Card único com **3 abas internas** (JS puro, sem framework): **✅ Publicado (N)** · **📝 Rascunho (N)** · **📺 Canais (N)** — contagens vivas nos botões.
- Aba Publicado: 15 matérias publicadas do Agente Cafezinho (cat 28 do WP, agora clicáveis com link) + sub-bloco dos temáticos pausados (GSN/Aiatolah/Mapa Rio).
- Aba Rascunho: 15 rascunhos no gate (antes misturava 5 publicados + 3 rascunhos na mesma lista), com nota "quem publica é a Claude Laura".
- Aba Canais: 🇧🇷 nacionais + 🌍 internacionais + formulário de adicionar canal (tudo o que era 2 cards empilhados virou 1 aba).
- Card de introdução (agente ativo 08/14/20h + pausados) mantido fora das abas.

**Menu do painel**: entrada `🎙️ Transkriptor` REMOVIDA da NAV (ordem do Miguel — a página continua acessível em `/v6/transkriptor`; não redirecionei a rota porque o pedido foi só o menu).

## Prova

- QA visual por screenshot (chrome headless → analyze_image): menu sem Transkriptor ✓, abas com contagens (15/15/34) ✓, aba Publicado ativa renderizando ✓, zero texto de template vazando ✓, nada quebrado ✓.
- Compilado no python 3.12 da Tencent (o do Dell cai na PEP 701 em código pré-existente — régua: compilar sempre na Tencent); restart via `systemctl restart cctv-v6` ✓.
- Bug intermediário pego no QA: contagens `{len(pub)}` literais (f-string mal montada) — corrigido antes do deploy final.

## Estado / falta

- Pronto e no ar. A rota `/v6/transkriptor` segue viva (só saiu do menu) — se o Miguel quiser redirecionar para /v6/youtube, é 1 linha.
- Rollback: `cp .bak_abas_youtube_20260905` + restart (devolve menu e página antiga).

— ZCode/GLM-5.3 (ZM) · 20260905 12:2x BRT
