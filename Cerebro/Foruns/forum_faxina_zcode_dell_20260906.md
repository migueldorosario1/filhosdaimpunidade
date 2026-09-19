# FÓRUM — Faxina do ZCode Dell (06/09/2026): "quero esse programa levinho"

> **Origem:** pedido do Miguel 06/09/2026 ~19:1x BRT (voz): "Tá ficando muito pesado aqui o ZCode… Não tem que fazer uma limpeza?… Bota tudo no backup lá. Leva pro Backblazer. Eu quero esse programa aqui levinho."
> **Executor:** ZCode ZM (**Qwen3.8-Max**), Dell. Rito = mesmo do lote02 da faxina Rio (manifesto prévio → cifra → upload → readback → retirada).
> **Memória-irmã (log técnico):** `Memorias/memoria_faxina_zcode_dell_20260906.md` · **Manifesto do backup:** `Memorias/MANIFESTO_ZM_BACKUP_ZCODE_20260906.md`

## Diagnóstico (antes)

| Área | Peso | O que era |
|---|---:|---|
| `~/.zcode/cli/db/db.sqlite` | 1,6 GB | 505 sessões; parts: jul 198 MB + ago 735 MB + set 76 MB; freelist 0 (dado real, não lixo) |
| `~/.zcode/cli/agents` | 1,2 GB | transcrições de subagentes; 49/51 dirs >7 dias |
| `~/.zcode/cli/artifacts` | 830 MB | arquivos de sessões; 249 dirs >7d = 703 MB |
| `~/.zcode/cli/exec` | 709 MB | saídas de bash + 443 snapshots de startup |
| `~/.zcode/v2` | 222 MB | ~110 MB em `.bak_fallback/pre_*` do tasks-index + logs 24/08→ |
| `~/.config/ZCode` | 744 MB | 712 MB = caches regeneráveis do browser embutido (Cache 486 + Code Cache 204 + SW 22) |
| updater `pending/` | 141 MB | `ZCode-3.11.2-linux-x64.deb` com o 3.11.2 JÁ instalado (dpkg 3.11.2-6792) = morto |
| **Total ZCode** | **~5,6 GB** | disco geral OK (61%, 174 GB livres) — o peso era do app, não do disco |

## Decisões

1. **Backup ANTES de qualquer retirada**, cifrado GPG AES256+ZLIB, passphrase dedicada alias `ZM_ZCODE_FAXINA_20260906_PASSPHRASE` espelhada nos 3 cofres (Regra 4; sha8 `da3c13f8`; backups `.bak_pre_zcode_faxina_20260906`; valor nunca em chat/git).
2. **Destino:** `b2:failover-cafezinho1/faxina/zcode-dell/zm_20260906_faxina_zcode/` (bucket da casa, sem contratação nova).
3. **Cortes:** arquivos de sessão >7 dias; db = conteúdo (parts/messages) de sessões com `time_updated < 23/08` (14 dias), **linhas de session preservadas** (histórico continua listado no app); caches regeneráveis todos; `.deb` já instalado.
4. **NÃO tocados:** `cli/rollout/` (vivo da sessão corrente), `cli/plugins/`, `cli/memories/`, `hooks/` (backup sim, permanecem), perfil/logins do browser embutido, `~/ZCodeProject` (moka-app em sprint ativo de outra sessão — anti-colisão §112), caches não-ZCode (chrome/whisper/huggingface).
5. **VACUUM do db só com ZCode FECHADO** (encolhimento real do arquivo) — script `~/faxina_zcode_vacuum.sh` entregue; poda em lotes (15 sessões/transaction, busy_timeout 60s) é WAL-safe com o app rodando.

## Execução (linha do tempo)

- 19:11 diagnóstico + linha no MONITORAMENTO.
- 19:2x passphrase nos 3 cofres (sha8 conferido 3/3) + hot backup do db (API backup do SQLite, 10s, sha256 `913ad3d8…`).
- 19:26-19:31 5 pacotes `.gpg` prontos (cli_dados 661 MB/14.833 arquivos · db 444 MB · v2 53 MB · config 1,7 MB · updater 141 MB) + manifest.json/README autossuficientes + SHA256SUMS.
- 19:31 MANIFESTO prévio publicado no GitHub (commit `953d5edba`).
- 19:33-19:42 upload B2 (1,268 GiB, exit 0, 8 objetos).
- 19:4x **READBACK VALIDADO:** download integral → sha256 7/7 SUCESSO → decifragem: tars 14.833/71/249/4 membros → db decifrado sha256 IDÊNTICO + `integrity_check ok` + 505 sessões/272.286 parts.
- 19:5x retirada local: **3.698 MB liberados** (49 agents + 249 artifacts + 373 exec sess + 394 bash-startup + 6 logs + 10 config.bak + 33 v2.bak + 12 v2 logs + caches Electron/browser + .deb).
- 19:5x poda do db: **155.816 parts + 42.759 messages** apagados em 14,2s (23 lotes), 505 sessões preservadas, `integrity ok`, freelist 213.805 páginas = **835 MB** internos livres.
- 19:5x staging/readback (4,1 GB temporários) apagados; passphrase temp destruída.

## Resultado (depois)

- `~/.zcode`: **4,7 GB → 2,1 GB** · `~/.config/ZCode`: **744 MB → 4,9 MB** · updater: **141 MB → 0**.
- **Ganho líquido no disco: ~3,5 GB** (df: 174 → 177 GB livres) **+ ~800 MB adicionais quando o Miguel rodar o VACUUM** (db 1,6 GB → ~800 MB; `~/.zcode` total cairá para ~1,3 GB).

## Estado da missão

- **O que aconteceu:** diagnóstico, backup integral cifrado e VALIDADO no B2, retirada local executada, db podado (conteúdo velho), app intacto e funcionando durante tudo (poda WAL-safe).
- **O que falta (Miguel):** quando puder, **fechar o ZCode e rodar `bash ~/faxina_zcode_vacuum.sh`** (2 min; encolhe o db de verdade; script faz backup próprio `.bak_pre_vacuum_*` antes e integrity_check depois — se o ZCode reabrir normal, o .bak pode ser apagado).
- **O que preciso de você (decisões opcionais, sem ação minha sem "vai"):** (a) caches NÃO-ZCode: google-chrome 2,2 GB (cache, regenerável), whisper 1,8 GB + huggingface 1,5 GB (modelos — apagar força re-download); (b) `~/ZCodeProject` 2,8 GB: moka-app 1,1 GB e igot 765 MB são na maior parte `node_modules`/`.next` (reconstruíveis) — só mexer quando o sprint Moka Play Store fechar; (c) manter rotina: esta faxina pode virar mensal (mesmo rito).
