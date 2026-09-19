# MEMÓRIA — Faxina do ZCode Dell 06/09/2026 (log técnico completo)

> Irmã do fórum `Foruns/forum_faxina_zcode_dell_20260906.md`. Executor: ZM (Qwen3.8-Max). Rito Rio-lote02: manifesto prévio → cifra → upload → readback → retirada.

## 1. Mapa do peso (o que o ZCode acumula — referência futura)

- `~/.zcode/cli/db/db.sqlite` — banco ÚNICO do app (tabelas: session, message, part, todo, session_entry, permission, input_history, local_setting, session_target, workflow_* (VAZIAS — automações NÃO moram aqui), session_task_link (vazia), model_usage, turn_usage, tool_usage, session_input). O peso mora em `part` (1.167 MB de data) + `message` (131 MB) + índices (~170 MB). `part` TEM coluna `session_id` (poda direta sem join). `PRAGMA foreign_keys=0`. page_size 4096, auto_vacuum 0 (VACUUM manual obrigatório para encolher).
- `~/.zcode/cli/agents/sess_*` — transcrições JSONL de subagentes por sessão.
- `~/.zcode/cli/artifacts/sess_*` — arquivos produzidos nas sessões.
- `~/.zcode/cli/exec/sess_*` + `exec/bash-startup/` — saídas de Bash e snapshots de inicialização (1 por chamada, 443 acumulados).
- `~/.zcode/cli/log/zcode-AAAA-MM-DD.jsonl` — log diário do cli (~10 MB/dia).
- `~/.zcode/cli/rollout/model-io-sess_*.jsonl` — 🔴 VIVOS da sessão corrente (não mexer).
- `~/.zcode/v2/` — camada "v2" do DESKTOP (NÃO é legado morto!): config.json, credentials.json, setting.json, tasks-index.sqlite (14 MB, vivo, -wal ativo), logs diários, e o lixo: `tasks-index.sqlite.bak_fallback_*` diários (~8-10 MB/dia!) + `config.json.bak_pre_*` — foi isso que acumulou 110 MB.
- `~/.config/ZCode/session/Partitions/zcode-embedded-browser/` — perfil do browser embutido (Browser Use): Cache 486 MB + Code Cache 204 MB + Service Worker 22 MB = regeneráveis; Local Storage/IndexedDB/WebStorage/cookies = minúsculos e com logins (PRESERVAR).
- `~/.cache/@zcodedesktop-updater/pending/` — .deb baixado pelo auto-update; some sozinho após instalar? NÃO — ficou 141 MB de `ZCode-3.11.2-linux-x64.deb` com a versão já instalada (verificar sempre com `dpkg -l | grep zcode`).
- FORA do ZCode: `~/.cache` = chrome 2,2 GB, whisper 1,8 GB, huggingface 1,5 GB (não tocados).

## 2. Pacotes no B2 (`b2:failover-cafezinho1/faxina/zcode-dell/zm_20260906_faxina_zcode/`)

| Objeto | Bytes | SHA256 |
|---|---:|---|
| zcode_cli_dados.tar.gpg | 692.297.815 | `76cbc75e9480dcd578ad433e2b617e3f4319dc20e653646744c163339ade9ec3` |
| zcode_db.sqlite.gpg | 465.291.548 | `53ecdfc5a85597b0de2f71355d07f1cfdb53db92c422f0a8eb7d082cd699b53f` |
| zcode_v2.tar.gpg | 54.789.954 | `1e0979eb378ba9807632fa283ca723c592c6b9cacc4afd380d44620fb72980fe` |
| zcode_config.tar.gpg | 1.719.538 | `9046ddc65fd4d8b32f3c8d49c0524b4f7058a84d68cfbdc44c2c7f8b27643895` |
| zcode_updater_deb.tar.gpg | 146.943.132 | `21ebb4c7f31600221d15a78bb005684b2b8e63633f13e31ffba46f7dcec834eb` |
| manifest.json | 2.827 | `428f3bde7e6bf1d94043782536e9a79bcfc3845d5be4305413a7d30880f36b5c` |
| README.txt | 874 | `6a0e4a3afa09a27342297c753aa5b99493a16ecacea37ec1dce3b7622289423f` |

- Conteúdo do db backup: sha256 do sqlite bruto `913ad3d866ae4f79bd8f1fd9a1392453fd404cb983365182cd87920ba801754b` (1.634.856.960 B, 505 sessões, 272.286 parts) — conferido 2× (pré-upload e no readback).
- Passphrase: alias `ZM_ZCODE_FAXINA_20260906_PASSPHRASE`, sha8 `da3c13f8`, nos 3 cofres (intake + agentes_labs + root/.env.unificado), backups `.bak_pre_zcode_faxina_20260906`, linha no `cofre_intake.meta.tsv`. Temp local destruído com shred.
- Readback 19:4x: sha256sum -c 7/7 SUCESSO; tar -t decifrado: 14.833/71/249/4 membros; db decifrado: sha idêntico, integrity ok, 505/272.286.

## 3. Retirada local (executada 19:5x, −3.698 MB)

find mtime +7d: agents 49 dirs, artifacts 249 dirs, exec 373 sess dirs + 394 bash-startup; log: 6 jsonl (ficou só 06/09); cli config.bak 10; v2 `.bak_*` 33 + logs 12 (ficaram 05-06/09); caches Electron (Cache/Code Cache/GPUCache) + browser embutido (Cache/Code Cache/GPUCache/Dawn×2/Service Worker/Shared Dictionary/VideoDecodeStats/blob_storage); updater pending (.deb + update-info.json). Staging+readback (4,1 GB) apagados após validação.

## 4. Poda do db (com o app RODANDO — receita WAL-safe)

```python
# sqlite3 CLI não existe no Dell → python3 módulo sqlite3
con = sqlite3.connect(db, timeout=60); con.execute('PRAGMA busy_timeout=60000')
ids = SELECT id FROM session WHERE time_updated < strftime('%s','2026-08-23')*1000  # 339 de 505
for chunk in batches(ids, 15):
    with con:  # transaction
        DELETE FROM part WHERE session_id IN chunk      # part tem session_id direto
        DELETE FROM message WHERE session_id IN chunk
    sleep(0.05)
PRAGMA wal_checkpoint(FULL); PRAGMA integrity_check  # ok
```
Resultado: 155.816 parts + 42.759 messages em 14,2s; freelist 213.805 páginas (835 MB); arquivo NÃO encolhe (auto_vacuum=0) → VACUUM com app fechado via `~/faxina_zcode_vacuum.sh` (checa pgrep excluindo a si mesmo, backup `.bak_pre_vacuum_*`, integrity antes/depois, checkpoint TRUNCATE).

## 5. Armadilhas anotadas

1. `tar -cf -` só pode aparecer UMA vez (múltiplos `-C dir file…` encadeados no mesmo `-cf -`; "Múltiplos arquivos-tar exigem -M").
2. `hooks/` e `tmp/` ficam na RAIZ de `~/.zcode`, não em `cli/` (tar exit 2 = stat falhou;GNU tar continua os demais).
3. Hot backup de db WAL vivo: `sqlite3.Connection.backup()` de conexão RO — 10s p/ 1,6 GB, snapshot consistente; apagar `-shm/-wal` residuais do destino após fechar.
4. `pgrep -f -i zcode` casa com o PRÓPRIO script (nome no argv) → filtrar `$$` e o nome do script.
5. DELETE grande em db compartilhado com app vivo: NUNCA 1 transação gigante (bloqueia escritas do app) — lotes pequenos + busy_timeout + sleep.
6. `.deb` do updater sobrevive à instalação — checar `dpkg -l` antes de concluir que é pending de verdade.
7. v2 NÃO é legado morto — desktop lê/ escreve lá (config, credentials, tasks-index com -wal ativo); só os `.bak_*` diários são lixo (o app gera `tasks-index.sqlite.bak_fallback_*` todo dia — candidato a rotina de limpeza).

## 6. Números finais

`~/.zcode` 4,7→2,1 GB (db 1,6 GB pendente de VACUUM → ~800 MB; plugins 163 MB intocado; artifacts 128 MB recentes; rollout 19 MB vivo; agents 14 MB recentes) · `~/.config/ZCode` 744→4,9 MB · disco 61%→60% (177 GB livres). Ganho total após VACUUM do Miguel: ~4,3 GB.
