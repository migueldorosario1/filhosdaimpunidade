# 🧠 MEMÓRIA — SINCRONIZAR GOOGLE DRIVE (log técnico completo)

**Data:** 2026-08-07 ~10:50→11:35 BRT · **Agente:** ZCode/Kimi K3 · **Repo:** `filhosdaimpunidade` (`~/ZCodeProject/filhosdaimpunidade`) · **Commits:** `6112560` feature → `d71b8af` restore → `efb9cfa` hardening (+ mirror commits de push `b6e9352`/`6b2cdaa`) · **AO VIVO** (HEAD==origin, Vercel 200, `/api/drive` operante).

## 1. Investigação do backup (o pedido "confere se é o backup certo")

- `rclone lsd gdrive:` → pasta **`novo livro`** (a mesma citada no NODE_LIVRO: "Espelho Drive, sync diário 04:30").
- Conteúdo: espelho completo do projeto (index.html, revisions.json, custom_rules.json, CLAUDE.md, Fontes/, capitulos/, backups/…). File IDs: pasta `1MGdnx-6jg3nhulk1AC8J4KivViMwFVe2`; backups `1aQDV2fvqKViAlXklPj2pSuIcxpJY_elU`; revisions.json `1_4bU2bc0o30lOOdN6REWjuAs6FxxE-Jh`; custom_rules.json `1QOgSBRc9UNfNFtKcKoFUuowH9SipYviF`.
- **Prova de identidade:** md5 do revisions.json do Drive == do repo (`dd300c459383d23c8958d59eaf53d0ce`, 5146 bytes). Último zip: `livro_backup_20260807_040001.zip`.
- **Topologia descoberta:** cron 04:00 `backup_livro_diario.py` (manifesto+zips) e 04:30 `backup_livro_gdrive.sh` (`rclone copy espelho_local → gdrive:novo livro` + `git add/commit/push` do espelho). Espelho local = `~/Downloads/Antigravity Google/Outros/novo livro` (clone do mesmo repo). ⚠️ Espelho não faz `git pull` — divergência pré-existente anotada como pendência.
- **Achado de frescor:** revisions.json nuvem = só R1 (28/07); as R#s atuais (R28 etc.) estão no localStorage do navegador. O botão novo fecha esse ciclo.

## 2. Arquitetura implementada

### 2.1 Serverless `api/drive.js` (novo, padrão `api/kimi.js`)
- `GET ?op=status` → pasta + metadados dos 2 JSONs + último zip (`orderBy=name desc` — nome é timestamp) + hora do servidor.
- `GET ?op=pull` → `alt=media` dos 2 JSONs, com **validação de shape** (502 sem repassar se inválido).
- `POST ?op=push` (header `x-sync-key` == env `FDI_SYNC_SECRET`, senão 401) → **valida shape** (400 recusa lixo) → snapshot `backups/revisions_snapshot_<ts>.json` → `PATCH upload/drive/v3/files/{id}?uploadType=media` ×2 → **Contents API GitHub** (`revisions.json` + `custom_rules.json`, GET sha → PUT base64) → resposta consolidada.
- **OAuth:** refresh token em `GDRIVE_REFRESH_TOKEN` (Vercel env, origem rclone.conf). Client público do rclone: `RCLONE_CLIENT_ID` + `RCLONE_ENCRYPTED_SECRET` extraídos do fonte aberto `backend/drive/drive.go@v1.73.2`; segredo revelado em runtime via porta do pacote `fs/config/obscure` (AES-256-CTR, chave pública fixa de 32 bytes, IV = 16 primeiros bytes do payload base64url). Verificado localmente: access_token 256 chars, pasta "novo livro" lida.
- **Retry de quota** `withQuotaRetry` (waits 0/6s/15s; hook `FDI_RETRY_WAITS`) cobrindo download/upload/snapshot; `isQuotaError` = /quota|rate.?limit|429/i. Detalhe pegado em teste: o `res.ok` do download precisa estar DENTRO do retry (fetch não lança em 403).
- CORS allowlist idêntica ao kimi.js. Teto de pacote 4MB.
- Env vars gravadas via **REST API v10** (`upsert=true`) — a CLI 56.0.0 (`vercel env add` com pipe) grava valor **vazio** (bug provado por roundtrip `TESTE_ROUNDTRIP`; vars vazias apagadas e recriadas pela API). Token da CLI em `~/.local/share/com.vercel.cli/auth.json`.

### 2.2 Cliente (`index.html`)
- Botão header "☁️ Sincronizar Google Drive" (sky-100, `hard-drive-download`) após o botão GitHub.
- Modal `modal-drive-sync`: painel de status ao vivo (veredito "✅ BACKUP CERTO"), 🔄 Puxar (mescla remoto-base/local-vence — mesma semântica de `syncWithGitHubRepository`), ⬆️ Enviar (coleta idêntica a `exportRevisionsBundle`; chave pedida 1× via prompt, persistida em `fdi_drive_sync_key`; 401 → esquece e orienta), 📥 Baixar pacote (reuso), 📂 link da pasta. Log de operações no rodapé do modal.
- **Nenhum segredo no cliente** (teste 9 da suíte garante por grep de fonte).

### 2.3 Cron anti-clobber
`bin/backup_livro_gdrive.sh`: `rclone copy ... --update` (backup `.bak_pre_update_flag_20260807`). Sem `--update`, o rclone copia quando size/modtime diferem MESMO se o destino é mais novo → clobberaria os pushes do app. Com `--update`: destino mais novo é preservado.

## 3. Incidente BUG-20260807-FDI-DRIVE-PUSH-QUOTA-RClone (linha do tempo)

1. ~14:16 deploy OK; `op=status`/`op=pull` ao vivo OK; push sem chave → 401 OK.
2. ~14:17 1º push real: corpo montado por shell quebrou (substituição com aspas) E a chamada ao Drive tomou 403 de quota do projeto público do rclone → falha visível.
3. ~14:18 2º push: durante janela de quota, o `op=pull` (que montou o body) recebeu **JSON de erro do Google**; try/catch de parse engoliu; push gravou error-JSON no Drive (revisions 1325B, rules `[]`) e espelhou no GitHub (`f426e7f`/`df3aba1`).
4. ~14:20 detecção imediata (sizes na resposta ≠ esperado). Restore: Drive via `rclone copyto` (retries nativos) md5 conferido; GitHub via commit `d71b8af` da working tree íntegra. Snapshot automático `revisions_snapshot_20260807141832.json` também tinha a cópia boa (a proteção funcionou).
5. Hardening `efb9cfa` + testes server 6/6 + push real idempotente final: 200, conteúdo semanticamente idêntico ao original.

**Lições:** (1) erro de API em JSON parseável fura try/catch de parse — validar `res.ok` + shape semântico; (2) quota de credencial pública compartilhada exige retry; (3) snapshot pré-escrita se pagou na 1ª semana; (4) CLI Vercel 56 grava env vazia por pipe — usar REST API; (5) montar JSON por shell-string é frágil — sempre arquivo.

## 4. Testes

- `scratch/teste_drive_sync.js` (cliente, DOM-stub) **9/9**: abre modal+status; status erro honesto; pull mescla c/ prioridade local (R2 local vence, R1 remoto entra; regras unidas sem duplicar); push coleta R#s+regras, header de chave, snapshot+commit no log; 401 esquece chave; vazio não chama rede; fonte: botão/modal/ações/link/sem-segredo.
- `scratch/teste_api_drive.js` (server, handler real importado) **6/6**: sem chave→401 sem rede; lixo→400 sem tocar Drive/GitHub; válido→snapshot+2 uploads+2 commits; quota→3 retries→502 limpo; HTML no lugar de JSON→502; caminho feliz íntegro.
- Regressões: `teste_upload_versao.js` 14/14, `teste_central_fontes.js` 23/23.

## 5. Onde está o quê (ponteiros)

- Env vars Vercel (production, projeto `filhosdaimpunidade`): `GDRIVE_REFRESH_TOKEN`, `GITHUB_TOKEN`, `FDI_SYNC_SECRET`.
- Cofre canônico local (`Outros/chaves/agentes_labs/.env.unificado`): `FDI_SYNC_SECRET` (sha8 `4e11a074`). Refresh token = o mesmo do `gdrive:` do rclone.conf.
- Backup do script cron: `bin/backup_livro_gdrive.sh.bak_pre_update_flag_20260807`.
- Bug: `CEREBRO_NODE_BUGS_RESOLVIDOS.md` → `BUG-20260807-FDI-DRIVE-PUSH-QUOTA-RClone`.
