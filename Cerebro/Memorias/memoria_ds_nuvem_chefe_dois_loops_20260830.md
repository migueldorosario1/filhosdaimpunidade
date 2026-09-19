# 🧠 Memória — DS Nuvem Chefe: 2 loops (arquitetura + cutover) — 30/08/2026

> Par do Tema Duplo: `Foruns/forum_ds_nuvem_chefe_dois_loops_20260830.md`. Executor: ZM · ZCode/GLM-5.3. Ordem Miguel 30/08 ~15:1x (DSC-024/028/029/031/032).

## Arquitetura dos 2 loops

- **LOOP A · ESCUTA** — `~/ds_nuvem_chefe/escuta.py` (Tencent, ubuntu) + systemd `ds-nuvem-chefe-escuta` (Restart=always, RestartSec=10). No ar 15:26 BRT.
- **LOOP B · RONDA 30/30** — `~/ronda_dsn.sh` + `~/ronda_dsn_prompt.md` (renomeado; backups `.bak_pre_chefe_20260830`).

## Loop A — o que faz, item a item (ordem → implementação)

| Ordem | Implementação |
|---|---|
| Long polling timeout=25 | `getUpdates(offset+1, timeout=25)` em loop com `sleep 1` — quase contínuo, custo zero |
| Resposta flash em segundos | DeepSeek `deepseek-chat` (persona chefe + CONTEXTO_MINI lido fresco) + sendMessage assinado `— DS Nuvem Chefe (DS-N Chefe) · AAAAMMDD HH:MM:SS BRT` |
| Nunca sigla solta / perguntar erro de ditado | gravado no system prompt do flash (DSC-030/032) e nas regras duras da ronda |
| Silêncio ocioso | nada posta; heartbeat 1×/h no log LOCAL `~/ds_nuvem_chefe/escuta.log` |
| Offset persistido, nunca 2× | gravado ANTES de processar; herdado do daemon us65 (747773836) no cutover |
| Erro de API → backoff 30s | `except` geral → log + sleep 30 |
| Custo/consumo | `~/ds_nuvem_chefe/consumo_tokens.log` 1 linha/dia (`AAAAMMDD resp=N tok=T usd~X`, ~US$0.4/M blended) |
| Defesas da casa preservadas | interceptação `sk-` → cofre 600 (`chaves_interceptadas.md` + `ultima_chave_cofrada`; valor NUNCA em log/ponte §82) · áudio → `audios/<epoch>.ogg` + INBOX · INBOX commit seletivo + push |

## Cutover do consumidor único (decisão-chave)

- `getUpdates` tem UM consumidor: agora o Loop A (Tencent). Daemon `dsc-minibot` (us65) parou de escutar via flag `/root/.dsc_poller_na_tencent` (patch: `u = {}` quando flag existe) e SEGUE como carteiro do RESPOSTAS.md. Backups: daemon `.bak_pre_cutover_escuta_20260830`; patch em `/tmp/patch_daemon_cutover.py` (us65).
- **Reversão:** apagar flag + `systemctl restart dsc-minibot` + `sudo systemctl stop ds-nuvem-chefe-escuta` (na Tencent).
- **Por quê:** 2 consumidores de getUpdates roubam updates pelo offset (regra da casa, provada na análise DSC-024).

## Arquivos novos (Tencent)

```
~/ds_nuvem_chefe/escuta.py            # Loop A (0700 escuta.py? não: escuta.py 600, pasta 700)
~/ds_nuvem_chefe/offset.txt           # 600, offset corrente
~/ds_nuvem_chefe/escuta.log           # log local (msgs, lat, heartbeat 1x/h)
~/ds_nuvem_chefe/consumo_tokens.log   # 1 linha/dia
~/ds_nuvem_chefe/chaves_interceptadas.md  # 600, sem valores
~/ds_nuvem_chefe/audios/*.ogg         # áudios do Miguel
/etc/systemd/system/ds-nuvem-chefe-escuta.service
```

## Renome (DSC-031) — onde tocou

- `~/ronda_dsn_prompt.md`: título, identidade (promoção a chefe + nota anti-SNFF), 0b reescrita (Loop A responde flash; ronda cuida de ordens/perguntas completas; fila 40min segue), regras de fala DSC-030/032. Backup `.bak_pre_chefe_20260830`.
- `CONTEXTO_MINI.md` (repo): a casa já tinha aplicado o nome oficial + nota anti-SNFF; ZM acrescentou os 2 loops (commit cf1bc8269).
- Assinatura do Loop A: formato exato da ordem.

## Provas

- Serviço `active` desde 15:26:14; log "LOOP A · ESCUTA no ar… offset inicial=747773836".
- Daemon us65 `active` como carteiro (journal sem erros pós-cutover; entrega RESPOSTAS intacta — log `entregue:`).
- Latência flash: pipeline pronto; cada resposta registra `lat=Xs` no escuta.log; número real reportado na ponte quando o Miguel mandar o teste (pedido enviado, msg #27).

## Lições

1. Cutover de consumidor único precisa HERDAR o offset (senão o consumidor novo reprocessa pendentes antigos).
2. Flag-file é a forma mais reversível de desativar um ramo de daemon sem reescrever.
3. O erro de ditado (SNFF) tinha VIRADO TEXTO da casa (CONTEXTO_MINI) — renome tem que varrer os arquivos de memória, não só o código.

— ZM · ZCode/GLM-5.3 · 20260830 15:30 BRT
