# 🧹 MEMÓRIA TÉCNICA — FAXINA PONTUAL 3 SERVIDORES (07/08/2026)

Fórum correspondente: [forum_faxina_pontual_3_servidores_20260807.md](../Foruns/forum_faxina_pontual_3_servidores_20260807.md)
Autorização: Miguel por voz ~12h (bucket failover-cafezinho1; "desde que tudo indexado"; retenção/git gc ok; zumbis = ficha primeiro).

## Protocolo executado (regra de ouro)
indexar → copiar p/ B2 → verificar → apagar. Toda exclusão teve prova prévia (`rclone lsjson` byte-size == `stat -c%s`, ou contagem de arquivos ==). Caches regeneráveis: delete direto + linha no manifesto.

## rio-ag (159.89.185.209) — 87% → 83%
1. **npm cache purge**: 1.049.250.300 → 187.232.271 bytes (−862MB). Regenerável.
2. **audit ceara**: `/root/cicero_remote/cicero/logs/ceara_publication_audit.jsonl` (214MB, repo VIVO do cicero) → `gzip` → `/root/faxina_20260807/ceara_publication_audit_20260807.jsonl.gz` (4.990.648 B) → `b2:failover-cafezinho1/faxina/rio-ag/logs/2026-08/` → lsjson 4.990.648 ✅ → `truncate -s 0` no jsonl + `rm` do gz. (cicero segue escrevendo no arquivo truncado — fd preservado.)
3. **git gc --prune=now** nos 3 repos (todos `main` == `origin/main`, tree limpa antes): riocarta 2.518.116.232→idem; cicero 2.406.127.884; gsn 1.431.778.470→1.430.854.859. Packs já eficientes — ganho marginal.
4. **rclone**: não existia → instalado binário local via scp `/usr/local/bin/rclone` + config mínima (só seção `[b2]`, 600, sem exibição de segredo). `rclone lsd b2:` → failover-cafezinho1 ✅.
- Nota: `/root/gsn_remote` do rio-ag = clone espelho do bot legado (1,43G .git) — mantido (não estava na lista autorizada; avaliar na faxina contínua).

## NYC (198.199.121.136) — 79% → 61% (−9GB+)
Staging `/root/faxina_20260807/`. rclone `b2:` já existia.
1. **Logs ativos → B2 + truncate**: `log_rotas_llm.jsonl` 167.132.279 B + `robo_coleta_{militar,fantastico,turismo,sobrenatural}.log` (44,0+43,4+41,4+40,3 MB) → gz nomeados `*_20260807.gz` → `faxina/nyc/logs/2026-08/` → 5/5 size match → `truncate -s 0`.
2. **815× `briefing_execucao.json.used_*`** (28/07–05/08) → `briefing_used_20260807.tar.gz` (1.567.422 B) → `faxina/nyc/diversos/2026-08/` → match → delete.
3. **`.bak` >7d** (16 arquivos, centenas de KB; lista `lista_bak_antigos.txt` junto no B2) → tar → match → delete. Proteção extra: `grep -v banco_imagens` antes do rm (o `.bak` de hoje do banco_imagens_reais.db nem estava na lista por `-mtime +7`).
4. **Caches regeneráveis**: `.cache/pip` 4.434.043.657 B + `.cache/puppeteer` 655.009.253 B → rm direto, indexado.
5. **`/root/backups` 1,6G** (snapshots jun/26: banco_pos_agy_quebrado, pre_ricardo_couto, imagens_reais_backup, ruins_r2 + 1633 arquivos) → `faxina/nyc/backups-locais/2026-08/` → verificação: remoto 1633 arquivos/1.655.542.568 B vs local 1633/1.655.542.996 B — delta 428 B = 16 symlinks do snapshot `politica_v2_pre_deploy` que rclone não segue (NOTICE logado) → delete.
6. **`/root/gsn_remote`** (bot legado morto desde 23/07; 227 commits locais nunca empurrados) → `gsn_remote_20260807.tar.gz` 1.705.066.688 B → `faxina/nyc/repos-mortos/2026-08/` → size match ✅ → delete repo+tar.
7. `gsn_hourly_cron.log` (143MB do censo): **não encontrado** em profundidade 3 nem dentro do gsn_remote — provavelmente já removido no desligamento de 23/07. Sem ação.
- Colisão evitada: sessão Qwen tem plano próprio p/ NYC (Fase A enxutice) ainda aguardando "pode aplicar" — conferi mtimes/estado antes: nada havia sido tocado; escopos desta faxina não intersectam o archiver de bancos dela.

## Tencent (43.156.151.165) — EM CURSO
- `/root/backups` 9,2G → `b2:failover-cafezinho1/faxina/tencent/backups-locais/2026-08/` via `sudo nohup rclone copy` (PID 3186630, log `/root/faxina_20260807/upload_b2.log`). rclone já tinha remote `b2:` (config root; login é `ubuntu`+sudo).
- **Próximo passo:** aguardar fim → `rclone size` remoto vs `du -sb`/`find | wc -l` local → delete local → manifesto → sincronizar manifesto ao Cérebro.

## Manifestos (indexação exigida pelo Miguel)
Cada servidor: `/root/faxina_20260807/MANIFESTO_FAXINA.jsonl` (1 linha por item: ts, servidor, item, classe, tamanho, ação, b2, auth `MIGUEL-20260807-VOZ-FAXINA-PONTUAL`). Espelhos: `Cerebro/Memorias/faxina_20260807/MANIFESTO_FAXINA_{rio-ag,nyc}.jsonl`.

## Convenção B2 firmada
`b2:failover-cafezinho1/faxina/<servidor>/<classe>/<aaaa-mm>/` — classes: `logs`, `diversos`, `backups-locais`, `repos-mortos`.

## Lições
- `rclone copy` aceita UMA origem só (não múltiplos arquivos soltos) — usar loop ou filtros.
- rio-ag e Tencent não tinham rclone/config; o padrão "scp binário + config mínima 600 sem exibir segredo" funciona (rio-ag). Na Tencent o login é `ubuntu` com sudo — a config já existia em `/root`.
- `du -sb` vs `rclone size`: symlinks contam no du e não no rclone — verificar contagem de arquivos e justificar o delta antes de apagar.
- gc em repo já "gordo de verdade" (objetos reais) quase não libera espaço; gc resolve pack inchado/reflog, não histórico grande.
