# Fórum — GSN: correção de duplicata + trava anti-duplicidade (14/08/2026)

## O que aconteceu
- Miguel reportou (print 14:33) duas matérias quase idênticas na home do GSN: "US revokes Brazil ambassador's visa…" (BBC + Guardian), ambas commitadas às 13:39 do 14/08.
- **Repo canônico de publicação do GSN hoje:** `Projeto Cafezinho Agentes/sites-v4/globalsouth/` → GitHub `migueldorosario1/globalsouth-v4` → Vercel projeto `global-south-news` (push publica automaticamente). O repo `Dados_Frios/Global South News/gsn` (repo `global-south-news`) está STALE/legado — não usar para publicar.

## Decisões
1. **Removida a duplicata** `20260814-us-revokes-brazil-ambassador-s-visa-in-escalating-diplomatic` (fonte Guardian; hero = stock genérica "casal andando no parque" + hero_legenda com keyword-spam de banco de imagens). Mantida a versão BBC (hero = bandeiras internacionais, adequada). Commit `dcac330`; verificado ao vivo: 404 vs 200.
2. **Trava anti-duplicidade implantada** em `sites-v4/globalsouth/scripts/gsn_publish_hourly_batch.mjs` (commit `0ee3fa7`):
   - `findDuplicateTitle`: similaridade de título (Jaccard de tokens + bigramas, stopwords EN) contra TODOS os posts em `src/content/blog`; **bloqueia publicação se ≥ 0,55** (`GSN_DEDUP_THRESHOLD` sobrescreve). Testado: BBC×Guardian = 0,60 (bloqueia); Cuba colapso×restauro = 0,08 (libera).
   - `heroLegendaSpam`: bloqueia hero_legenda com spam de keywords de banco de imagens (≥3 repetições ou ≥4 termos genéricos + legenda longa).
   - Veto é **duro** (throw + log em `logs/gsn_publication_audit.jsonl`), não warning.

## Estado
- Pronto: duplicata fora do ar; trava publicada no repo canônico (deploy automático).
- Falta: nada crítico. Observar próximas rodadas do hourly para falso-positivo (séries de follow-up com títulos parecidos).
- Miguel: só avisar se a trava segurar alguma cobertura legítima de seguimento.

## Lições
- Dois posts da MESMA rodada às 13:39 passaram porque não havia dedup entre itens; agora há.
- Repo `Dados_Frios/.../gsn` e `global-south-news` (GitHub) desatualizados vs. realidade (`sites-v4/globalsouth` + `globalsouth-v4`) — cuidado ao diagnosticar GSN: sempre confirmar de onde vem o deploy.
- Hero com `hero_credit` "Pixabay" + legenda-lista-de-palavras = sinal de stock genérica inadequada.

## Adendo (14/08 ~17:05) — og:image das páginas de colunistas
- Miguel reportou thumb errado em /colunistas/paulo-nogueira-batista-jr/ (og:image = placeholder genérico em TODAS as páginas de colunista).
- Corrigido em `src/pages/colunistas/[author].astro` (commits 7247429 + retrato): cadeia retrato `/autor/<slug>.{jpg,png,webp}` → hero da coluna mais recente → placeholder.
- Retrato PNB Jr. adicionado: Wikimedia Commons CC BY 2.0 ("2015 Paulo Nogueira Batista Jr. (cropped)"), recortado 1200x630, verificado ao vivo (200 + og:image correto).
- Próximo: adicionar retratos em `public/autor/` para os demais colunistas conforme forem aparecendo (fallback hero já vale para todos).

---

## ADENDO — 24/08/2026 22:40 BRT: nova leva de duplicatas (6 posts, 4 vídeos) + trava source_url no consumidor

**Como o Miguel flagrou (print 22:33):** dois posts do Steven Starr quase idênticos na home. Varredura por `source_url` no repo achou furo maior — **4 vídeos publicados 2-3× = 10 posts onde deviam ser 6**:
- Helmer `vVn_DdiBARM` ×3 · Larry Johnson `h2SaRdsG7F0` ×3 · Irã-Hormuz `Xsb7c4Htx20` ×2 · Starr `XLRpWFcFAaY` ×2

**Causa-raiz:** corrida entre publicadores — lote manual da sessão (commit `2e90f5a`, 13:28) × consumidor da fila (`118b102`, cron Dell). A trava de 14/08 (similaridade de título) vive só no publisher horário do NYC (`gsn_publish_hourly_batch.mjs`); o `consumidor_gsn_fila.py` não tinha NENHUMA checagem, e o próprio lote manual saiu com 2 posts do mesmo vídeo. Títulos rewordings diferentes burlariam similaridade anyway — a prova certa é a **URL da fonte**.

**Correção (commit `ac0f3e8`):** 6 duplicatas removidas (mantido o 1º publicado de cada vídeo; heroes `youtube-<id>.jpg` compartilhados — nada órfão). Provas ao vivo: duplicatas 404, mantidos 200, home sem slugs repetidos (cada post 2× = padrão imagem+título).

**Trava nova:** `consumidor_gsn_fila.py` agora faz `git pull --rebase` ANTES de processar e pula (marca NYC + move fila) qualquer vídeo com `source_url` `watch?v=<id>"` já existente em `src/content/blog` (grep -F exato, sem falso-positivo de prefixo). Backup `.bak_pre_dedup_20260824`; sintaxe ok; grep provado contra o Starr mantido.

**Falta/não fazer:** publicações manuais (lotes de sessão) continuam sem trava — regra prática: antes de publicar lote de vídeos no GSN, rodar a mesma varredura `grep -rlF 'watch?v=<id>"' src/content/blog`.
