# MANIFESTO ZM — Backup da FAXINA DO ZCODE DELL (prévio ao upload)

> **Registro em 06/09/2026 ~19:3x BRT, ANTERIOR ao upload B2** (rito do lote02 Rio: indexar → registrar → copiar → verificar; nada é apagado antes da validação).
> **Autorização:** pedido do Miguel 06/09 ~19:1x (voz): "Tá ficando muito pesado aqui o ZCode… faz uma limpeza… bota tudo no backup lá, leva pro Backblaze. Eu quero esse programa levinho."
> **Executor:** ZCode ZM (Qwen3.8-Max), Dell.

## Diagnóstico (o peso do ZCode)

- `~/.zcode` = **4,7 GB**: `cli/db/db.sqlite` **1,6 GB** (505 sessões; parts: jul 198 MB + ago 735 MB + set 76 MB; freelist 0 = dado real), `cli/agents` 1,2 GB (49/51 dirs >7d), `cli/artifacts` 830 MB (249 dirs >7d = 703 MB), `cli/exec` 709 MB, `cli/log` 64 MB, `cli/plugins` 163 MB (não tocado), `v2` 222 MB (~110 MB em `.bak_fallback/pre_*` do tasks-index + logs 24/08→06/09).
- `~/.config/ZCode` = **744 MB** — 712 MB são caches regeneráveis do browser embutido (`Partitions/zcode-embedded-browser`: Cache 486 MB + Code Cache 204 MB + Service Worker 22 MB).
- `~/.cache/@zcodedesktop-updater/pending` = **141 MB** — `ZCode-3.11.2-linux-x64.deb` JÁ INSTALADO (dpkg `zcode 3.11.2-6792`) = morto.
- Disco geral: 61% (174 GB livres) — o problema é o peso do app (db gigante + milhares de arquivos de sessões velhas), não falta de disco.
- **FORA DE ESCOPO (não tocado):** `~/ZCodeProject` 2,8 GB (moka-app 1,1 GB em sprint ativo de outra sessão — anti-colisão §112; igot 765 MB), caches não-ZCode (`~/.cache`: chrome 2,2 GB, whisper 1,8 GB, huggingface 1,5 GB), `cli/rollout/` (arquivos VIVOS da sessão corrente), `cli/plugins/`.

## Pacotes (staging `~/backup_zcode_faxina_20260906/staging/`)

| Objeto | Bytes | SHA256 | Conteúdo |
|---|---:|---|---|
| zcode_cli_dados.tar.gpg | ~661 MB | `76cbc75e9480dcd578ad433e2b617e3f4319dc20e653646744c163339ade9ec3` | cli/{agents, artifacts, exec, log, image-cache, video-cache, memories, config.json*} + .zcode/{hooks, tmp} + manifest.json + README.txt — 14.833 arquivos (teste decifragem+listagem OK local) |
| zcode_db.sqlite.gpg | ~444 MB | `53ecdfc5a85597b0de2f71355d07f1cfdb53db92c422f0a8eb7d082cd699b53f` | hot backup consistente (API backup SQLite, 10s) do db.sqlite 1.634.856.960 B — sha256 do conteúdo `913ad3d866ae4f79bd8f1fd9a1392453fd404cb983365182cd87920ba801754b` (decifrado e CONFERIDO contra o bruto); 505 sessões / 272.286 parts |
| zcode_v2.tar.gpg | ~53 MB | `1e0979eb378ba9807632fa283ca723c592c6b9cacc4afd380d44620fb72980fe` | .zcode/v2 inteiro (config.json + credentials + tasks-index.sqlite e TODOS os .bak históricos + logs 24/08→06/09) |
| zcode_config.tar.gpg | ~1,7 MB | `9046ddc65fd4d8b32f3c8d49c0524b4f7058a84d68cfbdc44c2c7f8b27643895` | ~/.config/ZCode SEM os caches regeneráveis (perfil, Local Storage, IndexedDB, cookies do browser embutido Incluídos) |
| zcode_updater_deb.tar.gpg | ~141 MB | `21ebb4c7f31600221d15a78bb005684b2b8e63633f13e31ffba46f7dcec834eb` | pending/ZCode-3.11.2-linux-x64.deb + update-info.json |
| manifest.json / README.txt / SHA256SUMS.txt | pequenos | no SHA256SUMS | inventário autossuficiente + instruções de restauração |

## Destino e cifra

- `b2:failover-cafezinho1/faxina/zcode-dell/zm_20260906_faxina_zcode/` (mesmo bucket/família das faxinas Rio; sem novo plano/contratação).
- GPG simétrico **AES256 + ZLIB**; passphrase dedicada alias **`ZM_ZCODE_FAXINA_20260906_PASSPHRASE`** espelhada nos **3 cofres** (intake `~/cofre_intake/cofre_intake.env` + `Outros/chaves/agentes_labs/.env.unificado` + `Projeto Cafezinho Agentes/root/.env.unificado`), backups prévios `.bak_pre_zcode_faxina_20260906`, linha no `cofre_intake.meta.tsv`. **sha8 `da3c13f8` conferido 3/3** (valor jamais em documento/chat/git).

## Verificação prevista (antes de qualquer retirada local)

Download integral do B2 → SHA256 dos 5 pacotes vs SHA256SUMS → decifragem → testes: `tar -t` nos 4 tars (contagem de membros) + sha256 do db decifrado vs `913ad3d8…` + sqlite abre o db decifrado e conta 505 sessões → recibo final aqui. Falha em qualquer etapa = lote NÃO validado e NENHUMA retirada.

## Retirada local prevista (só após validação)

1. `cli/agents`, `cli/artifacts`, `cli/exec/sess_*` com mtime >7 dias (preservados os recentes e o que a sessão ativa usa); `cli/log/*.jsonl` exceto 06/09; `cli/config.json.bak_*`.
2. `v2/*.bak_*` (tasks-index + config, ~110 MB) e `v2/logs` até 04/09 (preservados 05-06/09 e os arquivos VIVOS: config.json, credentials.json, setting.json, tasks-index.sqlite).
3. Caches regeneráveis: `~/.config/ZCode/session/{Cache,Code Cache,GPUCache}` + do browser embutido `{Cache,Code Cache,GPUCache,Dawn*,Service Worker,Shared Dictionary,VideoDecodeStats,blob_storage}` (logins/perfil preservados).
4. `~/.cache/@zcodedesktop-updater/pending/*` (3.11.2 já instalado).
5. **Poda do db** (com o app rodando, em lotes pequenos WAL-safe): DELETE parts+messages de sessões com `time_updated < 2026-08-23` (14 dias); linhas de `session`/todo/entry preservadas (histórico visível continua listado; conteúdo integral está no backup).
6. **VACUUM** do db (encolhimento real do arquivo 1,6 GB → ~0,5 GB) só com ZCode FECHADO — script `~/faxina_zcode_vacuum.sh` entregue ao Miguel.

## Recibo final — 06/09/2026 19:5x BRT — LOTE VALIDADO E RETIRADA EXECUTADA

Upload concluído 19:42 BRT (1,268 GiB, 8 objetos, exit 0). **Readback integral** (download completo do B2 no Dell, área isolada `backup_zcode_faxina_20260906/readback/`):

- `sha256sum -c SHA256SUMS.txt`: **7/7 SUCESSO** (5 pacotes + manifest + README).
- Decifragem dos 4 tars: `tar -t` = **14.833** (cli_dados) / **71** (v2) / **249** (config) / **4** (updater) membros.
- `zcode_db.sqlite.gpg` decifrado: sha256 **`913ad3d8…754b` IDÊNTICO** ao bruto; sqlite abre (`integrity_check ok`), **505 sessões / 272.286 parts** conferidos.

Com o lote validado, executada a retirada (rito do manifesto):
1. Arquivos >7d (agents 49, artifacts 249, exec 373+394, logs 6, v2.bak 33+12, config.bak 10) + caches regeneráveis Electron/browser embutido + .deb 3.11.2 instalado → **−3.698 MB**.
2. Poda do db vivo em 23 lotes WAL-safe: **155.816 parts + 42.759 messages** (sessões pré-23/08; linhas de session preservadas; integrity ok; freelist 835 MB).
3. Staging/readback (4,1 GB) apagados; passphrase temporária destruída (shred) — valor permanente só nos 3 cofres.

**Resultado:** `~/.zcode` 4,7→2,1 GB · `~/.config/ZCode` 744→4,9 MB · updater 141→0 MB. Pendente do Miguel: `bash ~/faxina_zcode_vacuum.sh` com ZCode fechado (db 1,6 GB → ~800 MB; ganho total ~4,3 GB). Fórum: `Foruns/forum_faxina_zcode_dell_20260906.md` · Memória: `Memorias/memoria_faxina_zcode_dell_20260906.md`.
