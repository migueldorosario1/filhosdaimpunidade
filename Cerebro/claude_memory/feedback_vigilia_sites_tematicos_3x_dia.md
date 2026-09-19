---
name: feedback-vigilia-sites-tematicos-3x-dia
description: "A partir de 07/08/2026 04:15 BRT, loop Vigília inclui checagem dos 8 sites temáticos (Astro/Markdown) 3× ao dia — 04h madrugada, 11h manhã, 19h tarde. Se travar, pedir ajuda ao ZCode pela ponte. Objetivo: publicando? textos ok? fotos ok?"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7a8b86e8-615f-48dd-924d-5e86f182a869
---

**A partir de 07/08/2026 04:15 BRT, meu loop Vigília ganha 3ª camada: checagem dos 8 sites temáticos Cafezinho 3× ao dia — 04h (madrugada), 11h (manhã), 19h (tarde/noite BRT).**

**Why:** Miguel 07/08 ~04:10 BRT (áudio): "acrescenta no loop vigília de noite... faz uma vez à noite, quatro da manhã pode fazer agora com agora, de dia faz umas duas vezes, de manhã 11 da manhã e de tarde 19 horas... incluindo o loop vigília para você verificar os sites temáticos se atualizaram. Qualquer coisa pede ajuda também ao time pela ponte ao ZCode. Faz agora um monitoramento ver se está publicando está tudo certo, confere seus textos publicados, ver se as fotos estão corretas, faz por todos os sites temáticos."

**Os 8 sites temáticos (v4 local):**
| Nome | URL | Tecnologia |
|---|---|---|
| aiatolah | https://aiatolah.com | Astro |
| ceara | https://ceara.digital | Astro |
| discoverbrazil | https://discoverbrazil.news | Astro |
| globalsouth | https://globalsouth.news | Astro |
| mapario | http://mapario.com.br | Astro (timeout intermitente detectado 07/08 04:15) |
| mundotrilhos | https://mundotrilhos.com | Astro |
| railpost | https://railpost.news | Astro (timeout intermitente detectado 07/08 04:15) |
| riocarta | https://riocarta.com | Astro |

**Cronograma canônico** (BRT):
- **04:15 BRT** (madrugada) — janela pós ciclo NOITE V4
- **11:15 BRT** (manhã) — janela pós ciclo DIA V4 :17 das 11h
- **19:15 BRT** (tarde/noite) — janela pós ciclo DIA V4 :17 das 19h

Cada checagem: ~10 min de trabalho concentrado.

**O que checar em cada rodada:**
1. **HTTP status** raiz de cada site (200/308 = OK; timeout/5xx = problema).
2. **Publicando?** Datas recentes visíveis no HTML da home (últimas 24-48h).
3. **Textos ok?** Amostrar 1-2 posts recentes por site, verificar: erros gramaticais óbvios, HTML quebrado, `{{VERIFICAR_NOME}}` literal, fonte em grito ("SEGUNDO O G1"), links quebrados.
4. **Fotos corretas?** Cada post recente deve ter hero image não-placeholder (`blog-placeholder-*.jpg` do Astro template = alarme). Verificar caption/crédito.

**Sinais de alarme (escalação obrigatória):**
- Site sem publish em ≥48h → provável trava do worker → ZCode via ponte.
- Site com hero placeholder Astro (`blog-placeholder-*.jpg`) em post real → gate Ponte v3 violado → ZCode via ponte.
- Site com HTTP timeout persistente (3 tentativas) → infraestrutura → ZCode via ponte.
- `{{VERIFICAR_NOME}}` literal → bug worker YT-Cafezinho conhecido (feedback_bug_placeholder_verificar_nome_worker_yt) — escalar via ponte.

**Ponte com ZCode/Qwen 3.8** (regra Miguel 07/08 04:10):
- ZCode tem acesso direto aos SQLite dos 8 sites temáticos + logs cron + banco mídia + Tencent master.
- Escalar via `inbox_trindade/kimi.md` (Kimi Desktop) OU via canal com tag `[CLAUDE-VIGILIA-TEMATICOS-ESCALACAO-ZCODE-<slug>]`.
- Formato: 3-5 linhas: (a) site + sintoma, (b) hipótese, (c) o que já checei, (d) o que preciso do ZCode (query SQLite, log cron, restart cron, etc.).
- Sem urgência agressiva — se ZCode tá dormindo, deixar mensagem e retomar no ciclo seguinte.

**Registro obrigatório de cada rodada:**
- `Cerebro/monitoramento_horario/vigilia_tematicos/vigilia_tematicos_YYYY-MM-DD.md` (um arquivo por dia com 3 seções — 04h/11h/19h).
- Cada rodada: tabela `Site | HTTP | Publish 24h | Fotos ok | Textos ok | Escalação?`.
- Escalações ao ZCode: log em JSONL correcoes_YYYY-MM-DD.jsonl com schema R4 (`decision_state=proposed`, `origem=machine_autocure`, `actor_roles.proposer=[claude-opus]`).

**Regras irmãs:**
- [[feedback-loop-vigilia-opus-v5]] (loop DIA/NOITE V4 principal — não muda)
- [[feedback-ponte-claude-kimi-arquivo-por-turno]] (ponte imagens Ponte v3)
- [[feedback-ponte-imagens-v2-teto-ia-20pct-por-bloco]] (regra Ponte v3 vigente aplicada também aos temáticos)
- [[feedback-contar-publish-por-autor-5786]] (V4 principal — métrica separada da temáticos)

**Estado inicial (07/08 04:15 BRT — primeira rodada):**
- ✅ 6/8 sites publicaram nas últimas 24-48h (ceara, discoverbrazil, globalsouth, mundotrilhos, riocarta com datas 06-07/08; aiatolah SEM datas recentes visíveis)
- ⚠️ 2/8 sites com timeout intermitente (railpost, mapario) — retry no próximo ciclo (11:15) antes de escalar
- 🚨 og:image das homes é placeholder do template Astro em todos — verificar se é só a home ou se posts individuais também estão sem hero (crítico se sim)

**Anti-pattern a evitar:**
- Fazer checagem só via HTML scraping (frágil) sem escalar ao ZCode quando algo travar — ele tem acesso interno (SQLite, cron) que resolve muito mais rápido.
- Confundir métrica de sites temáticos com V4 principal (autor 5786 no cafezinho). Métricas SEPARADAS.
- Iniciar rodada nova sem terminar registro da anterior no arquivo `vigilia_tematicos_YYYY-MM-DD.md`.


---

## Metodologia refinada 07/08/2026 10:55 BRT — Kimi ZCode verificou minha 1ª rodada e apontou 4 fixes de metodologia

Após eu escalar 3 "sinais" da rodada 10:04 BRT (aiatolah parado, bug template Astro, railpost+mapario offline), Kimi verificou de dentro (SSH Tencent+NYC+droplet, repos, RDAP) e provou que **os 3 eram falso positivo**. Retificação por supersessão emitida no ledger. Aprendizado real:

**4 sugestões metodológicas do Kimi (adotar SEMPRE):**

1. **Amostra de posts ≥3 (nunca só 2 primeiros)** — home de sites Astro pode ter seções fixas/pinadas no topo (ex: aiatolah tem "🎥 Frontier Broadcasts" congelada). Meu `post_urls_amostra[:2]` pegou só os pinned; posts frescos estavam na seção "📡 Latest Reports". Fix: parsear seções OU pegar 3-5 posts pra reduzir viés.

2. **Hero check: ignorar 1º `<img>` (é logo do header)** — todos os 5 sites têm (a) 1º `<img>` = `class="logo-img"` do header; (b) 2º `<img>` = hero real `src=/hero/<slug>.jpg`. Meu regex `<img[^>]*src=...>` pegava o 1º = logo. **Fix correto:** procurar `<img>` cujo `src` COMEÇA em `/hero/` OU cujo `src` == og:image. Layouts `.astro` dos 5 sites conferidos linha a linha: todos usam `{heroImage && <img src={heroImage}>}` corretamente. **Não copiar template do riocarta — não há bug.**

3. **Timeout/308: retry com `-L` + confirmar por 2ª rota antes de alarmar** — 308 sem `-L` = redirect ignorado + fetch timeout. Meu script chamou `urlopen` sem seguir redirect explicitamente OU stack TCP local teve hang transitório. Kimi reproduziu 1× localmente (TLS hang 1º try, OK 2º). **Fix:** (a) sempre `-L` / `follow_redirect=True`; (b) se timeout, retry 1× antes de reportar; (c) se ainda timeout, confirmar via 2ª rota (ping SSH remoto ou consultar Kuma) antes de escalar.

4. **Fallback `onerror` (ex: ceará `fallback_ceara.png`) NÃO é bug** — é rede de segurança do template. Ceará renderiza fallback SE o hero real der 404. Meu diagnóstico "fallback exibido = bug" estava errado. **Fix:** antes de declarar bug, checar HTTP do próprio `/hero/<slug>.jpg` (`curl -I`). Se 200, fallback é só safety net inativo — não é bug real.

**Regra permanente adicionada:** antes de escalar sinal ao ZCode via ponte, aplicar os 4 checks acima. Se ainda parecer problema real, aí sim escalar. Reduz taxa de falso positivo.

**Achado lateral real do Kimi** (fora dos meus 3): post do ceará sobre Anvisa está com foto de estação de hidratação da Berlin Marathon (alt em alemão) — **bug de SELEÇÃO de imagem do juiz V4**, não de template. Registrado por Kimi na fila das trocas que aguardam OK do Miguel. Reforça que problemas reais aparecem — só que eu detectei os errados.

**Recibos v0.1.1 dos 3 sinais originais** (rcpt_20260807_101904_*): permanecem no ledger mas ganharão recibo de **supersessão** com `metadata.ref` apontando pra cada um, `decision_state=superseded`. Nunca deletar — append-only.

**Boas práticas gerais adotadas:**
- Escalar via ponte só quando confidence>90% pós-checks.
- Retificar em recibo separado quando ZCode/Kimi provar falso positivo.
- Corpus Ouro aprende com falso positivo tanto quanto com bug real.
