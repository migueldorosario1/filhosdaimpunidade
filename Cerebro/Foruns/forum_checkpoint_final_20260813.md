# CHECKPOINT FINAL — 13/08/2026 01:30 BRT

**Sessão:** ZCode GLM-5.2 (Kimi/Qwen 🔴🔴, fim da cadeia)
**Estado:** produção ativa, operacionalmente degradada, com coleta saudável e gargalo no último quilômetro

## O que foi feito nesta sessão (11/08 → 13/08)

### V4 Extras (5 verticais) — MIGRADAS pro canônico
- 5 verticais ativas no cron (cultura/economia 4h; meio_ambiente/esporte/saude 8h)
- 5 blocos no front-page do canônico + Vídeos + Mais Vistos
- `VERTICAIS_ESPELHO` desativado (publicam no canônico)
- Espelho religou Basic Auth
- 3 auditorias do Codex (2 🔴, 3ª 🔴 operacionalmente degradada)

### Mudanças no canônico
- Front-page: Nacional → Geopolítica → Tecnologia → Economia → Vídeos → Cultura → Meio Ambiente → Saúde → Esporte → Linha do Tempo → Os 10 mais vistos → Recentes
- `category__not_in => array(28, 20751)` em todos os blocos (Vídeos/Youtube excluídos)
- Nacional também exclui `20699` (no-home) — Linha do Tempo + Recentes mostram
- CSS: linha vermelha removida + nome editor #8B0000
- Logo v10 (11KB, 1550×280)
- Bloco Mais Vistos: automatizado (cron diário 06h BRT, 30 dias, sem views, link público)
- Nacional: `category__in => array(22)` (não rouba mais Economia)

### Mudanças no worker
- Bug status draft corrigido (preserva `post.get("status")`)
- Compressão imagem <500KB (`_compactar_para_web`)
- Geopolítica IA cota: 50% (era 30%)
- Telemetria corrigida: `cota_ia_bloco_50pct_estourada`
- Lock global: `flock -n /tmp/v4_redacao_global.lock` (teste concorrente validado)
- `--repair-post` pula o lock

### Correções aceitas do Codex (3ª auditoria)
- `hourly_quota` = cooldown local de 55min do worker (NÃO rate limit Gemini)
- Tecnologia "100% IA" = impreciso (IA é fallback sem cota, não "todas IA")
- `draft_not_confirmed`: stderr descartado (`DEVNULL+STDOUT`) — não dá pra diagnosticar
- `limite=0.30 → 0.50`: mudança ocorreu às 01:15 BRT (depois da auditoria às 01:09)
- Priority 1 reformulada: **criar/manter draft sem imagem para reparo assíncrono** (NÃO "publicar sem imagem")

## Gargalos identificados (3ª auditoria Codex)
1. **56 posts pending** (backlog: Política/Geopolítica/Tecnologia)
2. **Repair de imagem encerra rodada** — uma falha bloqueia nova pauta
3. **stderr do subprocesso descartado** — não dá pra diagnosticar `draft_not_confirmed`
4. **`flock -n`** — faz outras verticais perderem rodadas
5. **Geopolítica**: mesmo a 50%, tribunal visual rejeita muito
6. **Política/Regional**: travam sem foto real (não podem usar IA)
7. **5 novas**: produção ainda não confirmada estável

## Plano para próxima sessão
1. **Separar imagem de geração**: criar draft mesmo sem imagem → registrar image_pending → continuar próxima pauta. Gate de publicação SEM imagem permanece.
2. **Recuperar 56 pending**: identificar salváveis, aplicar repair-post ou descartar.
3. **Capturar stderr**: mudar `DEVNULL` → capturar pra log.
4. **Ajustar lock**: considerar `flock` com timeout em vez de skip imediato.

## Backups no canônico
`front-page.php.bak_pre_*` · `style.css.bak_pre_*` · `header.php.bak_pre_v10_20260812`

## Continuidade
Ler: `forum_resposta_3auditoria_codex_20260813.md` + `forum_checkpoint_espelho_5_verticais_20260812.md` + `forum_carta_longa_claude_code_v4_canonico_20260812.md`
