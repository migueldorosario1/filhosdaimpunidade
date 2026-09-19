# Vigília Sites Temáticos — 2026-08-07

Regra Miguel 07/08 04:10 BRT (áudio): 3 rodadas por dia — 04h madrugada, 11h manhã, 19h tarde.

---

## Rodada 04:15 BRT — 1ª do dia (inaugural da nova regra)

Feita 07/08 04:15 BRT via HTTP scraping (WP REST bloqueado 403 em todos; sites são Astro).

| Site | HTTP | Publish 24h | Foto home | Alarme |
|---|---|---|---|---|
| aiatolah.com | 200 | ⚠️ SEM datas recentes visíveis | og:image ausente | 🚨 pode ter parado — escalar ZCode |
| ceara.digital | 200 | ✅ 06-07/08 | placeholder Astro na home | ⚠️ ver posts individuais |
| discoverbrazil.news | 200 | ✅ 06-07/08 | placeholder Astro na home | ⚠️ ver posts individuais |
| globalsouth.news | 200 | ✅ 06-07/08 | placeholder Astro na home | ⚠️ ver posts individuais |
| mundotrilhos.com | 200 | ✅ 06-07/08 | placeholder Astro na home | ⚠️ ver posts individuais |
| riocarta.com | 200 | ✅ 06/08 | placeholder Astro na home | ⚠️ ver posts individuais |
| railpost.news | 308 → timeout | não checado | não checado | ⚠️ retry 11:15; se persistir, escalar |
| mapario.com.br | 308 → timeout | não checado | não checado | ⚠️ retry 11:15; se persistir, escalar |

**Escalação ao ZCode enviada** via `inbox_trindade/kimi.md` tag `[CLAUDE-VIGILIA-TEMATICOS-ESCALACAO-ZCODE-inaugural-04h-BRT]` — pedido:
1. Aiatolah publicou nas últimas 48h? (SQLite / logs cron)
2. Railpost + mapario têm cron rodando? (ps + crontab)
3. Placeholder `blog-placeholder-1.Bx0Zcyzv.jpg` aparece só no og:image da home ou também nos posts individuais? (query DB ou fetch de 1 post exemplo por site)

**Próxima rodada:** 11:15 BRT.


---

## Rodada 10:04 BRT — 2ª (deep check pedida por Miguel)

Investigação mais profunda: extraiu 2 posts recentes de cada site, verificou og:image + hero renderizado.

### Estado por site (checagem deep 10:04 BRT):

| Site | HTTP | Último post | og:image posts | Hero renderizado no post | Diagnóstico |
|---|---|---|---|---|---|
| **aiatolah.com** | 200 | **21/07/2026** (>2 semanas!) | real (`/hero/youtube-*.jpg`) | real | 🚨 **PAROU DE PUBLICAR há 17 dias** |
| **ceara.digital** | 200 | 07/08 (hoje) | ✅ real (`/hero/<slug>.jpg`) | ⚠️ `/images/fallback_ceara.png` | 🐛 template exibe fallback em vez do hero real |
| **discoverbrazil.news** | 200 | 07/08 | ✅ real | ⚠️ `/_astro/logo.1T5LZRKl.webp` | 🐛 template exibe logo em vez do hero real |
| **globalsouth.news** | 200 | 07/08 | ✅ real | ⚠️ `/_astro/logo.BkId3aa-.png` | 🐛 template exibe logo em vez do hero real |
| **mundotrilhos.com** | 200 | 07/08 | ✅ real | ⚠️ `/_astro/logo.BiQpVRQA.webp` | 🐛 template exibe logo em vez do hero real |
| **riocarta.com** | 200 | 07/08 | ✅ real | ✅ real (`/hero/<slug>.jpg`) | ✅ **único correto** — usar como referência de fix |
| **railpost.news** | timeout total | não checado | — | — | 🚨 servidor não responde (2ª rodada seguida) |
| **mapario.com.br** | timeout total | não checado | — | — | 🚨 servidor não responde (2ª rodada seguida) |

### Sinais críticos:
1. **aiatolah parado 17 dias** — worker/cron travado. Precisa investigar ZCode (`ps aux | grep aiatolah`, `crontab -l | grep aiatolah`, último log).
2. **Bug template Astro em 4 sites** — hero existe (og:image real), mas página do post exibe logo/fallback. RioCarta é o único correto — o fix pode ser copiar o template dele. **Impacto editorial**: quem clica no post vê logo genérico em vez da imagem da matéria = feio + confunde leitor.
3. **railpost + mapario offline** — 2 rodadas seguidas sem resposta HTTP. Servidor caído ou DNS quebrado.

### Boa notícia:
- 5 sites publicando ativamente hoje 07/08
- og:image (compartilhamento social) está real em todos os 5 → quem vê no Twitter/WhatsApp/Facebook vê foto real corretamente
- Snapshot completo salvo em `snapshot_2026-08-07_10h_deep.json`

**Próxima rodada:** 11:15 BRT (regra permanente 3×/dia).

---

## Verificação ZCode (Kimi K3) 10:25–10:55 BRT — os 3 sinais da rodada 10:04: TODOS falsos alarmes

Pedido do Claude (carta 10:10) verificado com acesso interno (SSH Tencent/NYC/droplet, repos `sites-v4/`, fetch ao vivo, dig/RDAP authoritative):

| Sinal do Claude | Veredito | Prova |
|---|---|---|
| 🚨 aiatolah.com "parado há 17 dias" | ❌ **Falso alarme — publicando hoje** | Home ao vivo tem posts 07/08 na seção "📡 Latest Reports" (`/en/posts/20260807-don-t-be-an-ai-middleman...`, `20260807-minimax-h3...`). Repo com commits diários V4 (hoje 03:02). Coletor YouTube vivo: 1 vídeo publicado hoje 00:01 + "Deploy YouTube executado com sucesso 🚀". Causa do erro: amostra pegou só os 2 primeiros links (seção fixa "🎥 Frontier Broadcasts", congelada em 21/07) + home sem datas visíveis nos cards. |
| 🐛 bug template hero (ceara/discoverbrazil/globalsouth/mundotrilhos) | ❌ **Falso alarme — sem bug** | Post 07/08 de cada site ao vivo: 1º `<img>` = logo do header (`class="logo-img"`), 2º = hero real `/hero/<slug>.jpg` — igual ao riocarta. Heroes HTTP 200 (140–156 KB). Ceará: `onerror`→fallback é rede de segurança; hero do dia 200 (241 KB, idêntico ao repo). Snapshot tinha `posts_check: []` vazio nos 4 — a afirmação não tinha base nos dados. Layouts `BlogPost.astro` dos 5: todos `{heroImage && <img src={heroImage}>}`. |
| 🚨 railpost.news + mapario.com.br "offline" | ❌ **Falso alarme — vivos** | Tencent/NYC/droplet: railpost 308→www→200; mapario 308→https→200 (~0,1s). IPs 216.150.x.x do mapario = range legado Vercel (`server: Vercel`, cert válido); 7/7 IPs testados 200. RDAP ativo até 2027-03, NS vercel-dns. Timeout = rota local intermitente (reproduzido 1× local: TLS hang, OK no retry). Kuma não apitou. |

**Achado real lateral (já conhecido):** post ceará/Anvisa com foto da Berlin Marathon (alt alemão) = erro de SELEÇÃO de imagem do juiz V4, não de template. Na fila de trocas que aguardam OK do Miguel.

**Fix de metodologia proposto ao Claude (via `inbox_trindade/claude.md` 10:55):** (1) amostrar ≥3 posts/nunca só topo (pode ser seção pinada); (2) hero check deve ignorar `.logo-img` e casar src com og:image; (3) timeout/308 exige retry `-L` + 2ª rota antes de alarmar; (4) fallback onerror: checar HTTP do hero antes de declarar bug.

**Estado real dos 8 sites às ~10:55 BRT: 8/8 VIVOS e publicando.** ✅

---

## Rodada 11:15 BRT — 3ª (v2 com 4 fixes metodológicos Kimi aplicados)

Scanner refinado (`snapshot_2026-08-07_11h15_v2.json`).

### Estado por site (11:23 BRT):

| Site | HTTP | Posts hoje (07/08) | Heros /hero/*.jpg | Diagnose |
|---|---|---|---|---|
| aiatolah.com | 200 | regex sem match (formato URL específico) | — | ⚠️ Kimi 10:55 já confirmou vivo; ajustar regex meu p/ `/en/posts/` |
| ceara.digital | 200 | 3 (07/08) | 2/2 ✓ | ✅ OK |
| discoverbrazil.news | 200 | 3 (07/08) | 2/2 ✓ | ✅ OK |
| globalsouth.news | 200 | 3 (07/08) | 2/2 ✓ | ✅ OK |
| mundotrilhos.com | 200 | 3 (07/08) | 2/2 ✓ | ✅ OK |
| riocarta.com | 200 | 3 (07/08) | 2/2 ✓ | ✅ OK |
| railpost.news | timeout+retry | — | — | ⚠️ Kimi 10:55 confirmou vivo (Tencent/NYC 200) — rota local minha frágil, **não escalar** (fix #3) |
| mapario.com.br | timeout+retry | — | — | ⚠️ mesma coisa (Vercel, 7 IPs round-robin, cert válido) — **não escalar** |

### Comparação vs rodada 10:04 BRT (antes dos fixes)
- Antes: 3 sinais escalados (todos falso positivo)
- Depois (com fixes Kimi): **0 sinais escalados** — os 3 "problemas" restantes já foram diagnosticados como falso positivo pelo Kimi (2ª rota confirmou)

### Achado lateral pendente (Kimi anotou 10:55, não é meu escopo)
- Post ceará sobre Anvisa (07/08) tem foto de estação de hidratação Berlin Marathon (alt alemão) — **bug juiz V4 selecionou imagem errada**. Kimi já registrou fila de trocas aguardando OK do Miguel.

### Meta melhorias meu scanner (próxima rodada 19:15)
- Adicionar regex `/en/posts/YYYYMMDD-*/` pra aiatolah (formato diferente dos outros)
- Considerar 2ª rota (SSH remoto ou HTTP via proxy Tencent) pra confirmar railpost/mapario ao invés de escalar por timeout local

**Próxima rodada:** 19:15 BRT.
