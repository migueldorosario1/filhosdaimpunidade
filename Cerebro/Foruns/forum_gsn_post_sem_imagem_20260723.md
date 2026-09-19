# FÓRUM — GSN: post sem imagem no ar (Libéria) + correção estrutural anti-"sem hero"

**Data:** 2026-07-23 ~04:00–05:30 BRT
**Agente:** ZCode (Kimi)
**Gatilho:** Miguel — "postagem sem imagem. isso não pode acontecer. corrige o post, mas faz uma correção estrutural."
**Memória técnica completa:** `Cerebro/Memorias/memoria_gsn_post_sem_imagem_20260723.md`

---

## 1. O incidente

O post https://www.globalsouth.news/blog/20260722-liberia-seizes-record-370-million-cocaine-haul-near-monrovia/ foi ao ar em 2026-07-22 **sem heroImage** (template servia `blog-placeholder-1.jpg` no og:image). Não foi o único: o post UNCTAD do mesmo dia também saiu sem imagem (corrigido por varredura manual, que deixou a Libéria passar).

## 2. Causa raiz (3 falhas encadeadas)

1. **Fail-open por design:** `agentes_tematicos/v4/publicador.py` dizia literalmente "sem imagem adequada = publica sem hero". Quando o funil Wikimedia Commons → juiz visual falhava, o post era publicado assim mesmo.
2. **Juiz visual mudo:** a chave Gemini está **sem créditos (HTTP 429)** e as chaves Kimi locais estão **inválidas (401)** — o juiz falhava aberto e ninguém era avisado. Foi assim que uma foto de "Monrovia, **Indiana**" quase virou capa da matéria da Libéria (Monróvia, **Libéria**) durante o resgate.
3. **Pipeline morrendo em silêncio:** identidade git ausente em 3 dos 8 repos v4 (aiatolah, globalsouth, mapario) → commits falhavam ("Please tell me who you are") e posts ficavam staged sem ir ao ar, sem nenhum alerta. 4 posts estavam travados (GSN: ECOWAS + Morocco; Aiatolah: GigaToken + SIMD).

## 3. Decisões tomadas

- **REGRA ESTRUTURAL: post sem imagem NÃO é publicado.** O artigo espera no banco auditado e tenta de novo nas próximas rodadas (máx. 6 ≈ 3 dias); esgotando, é reprovado (`reprovado_sem_imagem`) e o Miguel recebe alerta no Telegram. Nunca mais placeholder.
- **Juiz visual em cascata:** Gemini → Qwen-VL (testado e ativo). Se TODOS falharem, fail-open + alerta Telegram 1x/dia (throttle em disco). Prompt ganhou cláusula anti-homônimo (o caso Monrovia Indiana × Libéria).
- **Autocura git:** publicador grava identidade local se ausente; falha de `git add/commit/push` dispara alerta Telegram (throttle 6h/site).
- **Guarda de build (defesa em profundidade):** `scripts/verificar_heroes.mjs` no repo globalsouth-v4, ligado ao `prebuild` — se qualquer post publicado estiver sem hero, **o build falha e a Vercel não publica**. Testado nos dois sentidos; build de 259 páginas verde.
- **Ferramenta de resgate:** `agentes_tematicos/v4/resgate_hero.py` (--arquivo / --varredura) — mesmo funil do publicador (Commons CC → juiz → padronização 1200×675 blur-fill → anti-reuso).

## 4. O que foi corrigido no ar

| Item | Resultado |
|---|---|
| Post Libéria (GSN) | Hero real: mercado de Monróvia, Libéria — Wikimedia CC BY 3.0 (blk24ga). **Ao vivo** com og:image correto |
| GSN: ECOWAS + Morocco/Bologna | Destravados, com hero, publicados |
| Aiatolah: GigaToken + SIMD (pt/en) | Destravados, com hero, publicados |
| GSN: 2 posts institucionais sem hero | Resgatados (mapa Global South; Terra à noite domínio público) |
| Backlog discoverbrazil/riocarta/railpost | Heroes religadas/resgatadas + fixes pendentes da sessão 22/07 commitados |
| Post Iguaçu (discoverbrazil) | **Revertido** — o resgate automático substituiu uma hero curada por bug de path (bug corrigido no resgate_hero.py) |
| Aiatolah: 9 posts PT 20–22/07 sem hero | **Todos resgatados** (termos curados EN; juiz Qwen-VL aprovou) + 7 EN espelhados |

## 5. Pendências para o Miguel

1. **Recarregar créditos Gemini** (juiz primário fora — hoje o fallback Qwen-VL segura; Miguel decidiu deixar o Qwen segurando).
2. ~~Renovar chaves Kimi locais~~ **FEITO (23/07):** (a) chave 1 — válida em `api.kimi.com/coding` (visão) → `KIMI_VISION_API_KEY` nos 4 cofres; (b) chave 2 — válida na plataforma **internacional** `api.moonshot.ai` (só família `moonshot-v1-*`; k2 nega) → `KIMI_API_KEY`/`MOONSHOT_API_KEY` nos 4 cofres + provider `kimi` do `nucleo_llm.py` migrado para `moonshot.ai` / `moonshot-v1-128k` (backup §82). Cadeia de texto Kimi **restaurada** (teste ponta a ponta 200 OK). ⚠️ moonshot-v1 é geração mais fraca que kimi-k2 — se incomodar na produção, reordenar a cascata.
3. ~~Decidir sobre o pipeline GSN antigo no NYC~~ **FEITO (23/07):** desligado por ordem do Miguel — 2 crons comentadas (`# DESLIGADO_20260723_ZCODE`), backup em `/root/crontab_backups_gsn_off_20260723/root.crontab.bak`.
4. **Replicar a guarda prebuild** nos outros 7 repos v4 (precisa adaptar ao estilo "pages" do aiatolah).
5. **Backlog residual:** ~18 posts antigos (ferrovias/turismo, termos em PT) + 16 aiatolah onde a busca Commons não achou nada — precisam tradução dos termos para inglês ou curadoria manual.

## 6. Arquivos alterados

- `agentes_tematicos/v4/publicador.py` — bloqueio sem hero + retry + alertas + autocura git
- `agentes_tematicos/v4/nucleo_visao.py` — cascata Gemini→Qwen-VL + anti-homônimo + alerta
- `agentes_tematicos/v4/resgate_hero.py` — NOVO (resgate retroativo)
- `sites-v4/globalsouth/scripts/verificar_heroes.mjs` + `package.json` — NOVO (guarda prebuild)
- Repos git: globalsouth-v4, aiatolah-v4, discoverbrazil-v4, riocarta-v4, railpost-v4 (pushes)

---

## Adendo (~11:10 BRT) — discoverbrazil: post Indian Hotels + bug de og:image

Post Indian Hotels resgatado (hero Taj Tower CC BY-SA 4.0, juiz Qwen-VL aprovou; commit `b824a1d`). No caminho, achado bug estrutural: o discoverbrazil **sempre** servia `blog-placeholder-1.jpg` no og:image/twitter:image porque o `BlogPost.astro` não passava `image={heroImage}` ao `BaseHead`. Corrigido portando a lógica do globalsouth (commit `4cf35c3`, build 97 páginas verde, validado ao vivo). **Mesmo bug existe no mapario** (pendente); aiatolah precisa verificação (estilo pages).

## Adendo 2 (~11:20 BRT) — mapario + aiatolah corrigidos

Bug de og:image sanado em toda a família v4: **mapario** (`0339795`, mesmo fix do discoverbrazil; site ainda é scaffold sem produção — fix preventivo) e **aiatolah** (`8581556`, caso pior: Layout não emitia nenhum og:image; agora emite og:image/og:url/twitter condicionais quando há hero). Builds verdes (15 e 219 páginas); aiatolah validado ao vivo. Pendente: verificar os 2 repos v4 restantes.
