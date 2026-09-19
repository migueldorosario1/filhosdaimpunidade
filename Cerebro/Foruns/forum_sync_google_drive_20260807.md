# ☁️ FÓRUM — SINCRONIZAR GOOGLE DRIVE (Filhos da Impunidade)

**Data:** 2026-08-07 · **Agente:** ZCode/Kimi K3 · **Commits:** `6112560` (feature) + `d71b8af` (restore) + `efb9cfa` (hardening) — AO VIVO (Vercel HTTP 200, `/api/drive` respondendo)
**Pedido do Miguel (07/08):** "bota um botão também na capa... se você botou um botão de sincronizar com o GitHub, bota um botão também de sincronizar com o Google Drive. Procure lá no Google Drive onde é que tem a gravação, o backup do livro, confere se é o backup certo e aí bota o botão."

## 1. A verificação pedida ("confere se é o backup certo")

**O backup certo é `gdrive:novo livro`** — espelho do projeto inteiro (index.html, revisions.json, custom_rules.json, Fontes/, etc.) alimentado pelo cron local `backup_livro_gdrive.sh` (04:30, rclone copy) + zips diários em `backups/` (último: `livro_backup_20260807_040001.zip`). Prova de identidade: `revisions.json` do Drive **byte-idêntico** (md5 `dd300c459383d23c8958d59eaf53d0ce`) ao do repo GitHub. Achado importante: o `revisions.json` do repo/Drive só tem R1 do cap 1 — **as R#s frescas (R28+) vivem no localStorage do navegador do Miguel**; até hoje só voltavam à nuvem por export manual/agente. O botão novo resolve isso (ver decisão 3).

## 2. Decisões resumidas

1. **Botão "☁️ Sincronizar Google Drive"** no header, ao lado do GitHub (azul-céu, ícone hard-drive). Abre o modal `modal-drive-sync`.
2. **Verificação ao vivo dentro do app:** ao abrir, o modal consulta `/api/drive?op=status` e mostra: ✅ "BACKUP CERTO: pasta 'novo livro'", datas/tamanhos dos 2 JSONs, último zip de backup e hora do servidor. O "confere se é o backup certo" fica permanente, não só desta vez.
3. **🔄 Puxar do Drive:** baixa `revisions.json` + `custom_rules.json` do Drive e mescla com o navegador — **mesma semântica do sync GitHub (local tem prioridade)**.
4. **⬆️ Enviar para o Drive (a parte nova de verdade):** grava as revisões R# locais no Drive — com **snapshot automático** em `backups/` antes de sobrescrever — **e espelha no GitHub via Contents API** (que dispara redeploy e alimenta o sync-GitHub). As duas nuvens ficam frescas de uma vez. Protegido por chave `FDI_SYNC_SECRET` (cofre `.env.unificado`; o app pede 1× e grava no navegador).
5. **Arquitetura:** função serverless nova `api/drive.js` (padrão do `api/kimi.js`). OAuth Google **server-side**: refresh token em env Vercel (`GDRIVE_REFRESH_TOKEN`, origem: rclone.conf local) + client OAuth **público do rclone** (constantes do fonte aberto; o segredo distribuído ofuscado pelo próprio rclone é revelado em runtime com AES-256-CTR — pacote `obscure` portado). **Zero segredo no navegador/JS cliente.**
6. **Patch anti-clobber no cron 04:30** (`backup_livro_gdrive.sh`, backup `.bak_pre_update_flag_20260807`): flag `--update` no rclone copy — sem ela, o espelho local (mais velho) sobrescreveria na madrugada o que o app gravou no Drive (mais novo).
7. **Env vars Vercel** (production): `GDRIVE_REFRESH_TOKEN`, `GITHUB_TOKEN` (do gh CLI), `FDI_SYNC_SECRET` — gravadas via REST API (a CLI 56.0.0 grava valor VAZIO com pipe — bug pego por roundtrip test).

## 3. Incidente do caminho (resolvido e blindado)

No 1º push real, a quota **compartilhada mundialmente** do projeto OAuth público do rclone estourou (403) exatamente na chamada de download — e o JSON de erro do Google, parseável, atravessou o try/catch e foi gravado por cima do `revisions.json`. **Dano revertido em ~10 min** (rclone + git, md5 conferido; snapshot automático também tinha a cópia). **Blindagem (`efb9cfa`):** validação de shape editorial no pull (502, nada repassado) e no push (400, gravação RECUSADA), retry com backoff em quota 403/429, testes server-side 6/6. Registro completo: `BUG-20260807-FDI-DRIVE-PUSH-QUOTA-RClone` no BUGS_RESOLVIDOS.

## 4. Provas

- Testes Node: cliente **9/9** (`teste_drive_sync.js`) + server **6/6** (`teste_api_drive.js`) + regressões (upload-versão 14/14, central-fontes 23/23).
- Ao vivo: `op=status` ✅ (pasta, JSONs, zip do dia) · `op=pull` íntegro ✅ · push sem chave → 401 ✅ · push real idempotente → 200, snapshot + commits GitHub ✅.

## 5. Adendo — 2ª onda de quota (mesmo dia, ~15:20): o `op=status` entra na blindagem

Miguel abriu o modal e a verificação ao vivo tomou 403 de quota (a mesma quota "Queries/min" compartilhada mundialmente do projeto OAuth público do rclone). **Sem dano a dados** — falha só de leitura. Causa: o retry do hardening `efb9cfa` cobria apenas download/upload/snapshot; as 4 queries de metadados do status e o token OAuth estavam fora. **Correção (commit `67b9007`, AO VIVO):** retry em todas as chamadas do status + token (budget 4 tentativas c/ jitter ±20%, ~39s — cabe no maxDuration=60), **cache de 60s no status** (↻ atualizar e pós-sync usam `nocache=1`), flag `quotaCongested` e mensagem cliente honesta ("quota compartilhada congestionada — tente em 1–2 min", sem culpar env vars à toa) + hint "(cache de até 60s)". Testes server 6→**11/11**; verificado ao vivo (`"cached":true` na 2ª chamada; chamada que pegou quota completou dentro do budget). Registro: adendo do `BUG-20260807-FDI-DRIVE-PUSH-QUOTA-RClone` no BUGS_RESOLVIDOS.

## Pendências / próximos passos

- [ ] Miguel digitar a chave `FDI_SYNC_SECRET` no 1º envio pelo app (está no cofre; o app pede 1× e grava no navegador).
- [ ] Opcional futuro: projeto Google Cloud PRÓPRIO (client OAuth dedicado) para sair da quota compartilhada do rclone — hoje mitigado por retry.
- [ ] Espelho local `Outros/novo livro` não faz `git pull` nos crons (diverge do origin quando agentes empurram de outros clones) — divergência pré-existente, fora do escopo de hoje.

**Memória técnica:** `Memorias/memoria_sync_google_drive_20260807.md`

## 6. Adendo — orientação ao Miguel no modal (~17:00, 07/08)

Miguel perguntou (áudio) qual opção do modal **sobe** o trabalho dele para o Drive e relatou que o envio pede uma chave que ele não tem. Resposta dada:

1. **`↻ atualizar` só LÊ** — atualiza o painel de estado do backup (pasta, datas dos JSONs, zip). Não envia nada.
2. **Quem SOBE o trabalho é o botão "⬆️ Enviar revisões deste navegador para o Google Drive"** — grava as R# locais no Drive (com snapshot) e espelha no GitHub. O "🔄 Puxar" é a direção inversa (Drive → navegador).
3. **Chave:** valor nunca vai no chat (regra do Cofre) — apontado o caminho: variável `FDI_SYNC_SECRET` no `Outros/chaves/agentes_labs/.env.unificado`. Ele copia o valor, cola 1× no app e o navegador guarda para sempre (`localStorage fdi_drive_sync_key`; se o servidor recusar, o app esquece e pede de novo).
4. **"O ideal era não ter chave" (Miguel):** a chave foi MANTIDA — o `/api/drive` é público na internet e o push escreve no Drive e no GitHub; sem a chave, qualquer pessoa/bot poderia sobrescrever o `revisions.json` com payload de shape válido (shape-guard valida formato, não autoria). Custo é único (1× por navegador). Se o Miguel insistir, remove-se — registrado aqui para a decisão ser visível.

## 7. Adendo — incidente 2 (mesmo dia, ~17:18) e o 401 do Miguel

- **Incidente `BUG-20260807-FDI-DRIVE-PUSH-EMPTYSHAPE`:** durante a verificação ao vivo da chave, payload de teste sem o campo `revisions` passou vacuamente pelo shape-guard e gravou `{}` no Drive/GitHub. Restaurado em ~7 min (snapshot automático + rclone; commit `565b601`); blindagem no commit `4197f82` (revisions ausente/vazio → 400; suíte server 13/13; verificado ao vivo).
- **O 401 do Miguel:** a chave do cofre foi VALIDADA ao vivo (com ela a auth passa; chave errada reproduz exatamente a mensagem "Chave de sincronização recusada"). Conclusão: o texto colado veio diferente — causa mais provável: copiar a linha inteira `FDI_SYNC_SECRET=...` incluindo o nome da variável. Orientação corrigida: `grep '^FDI_SYNC_SECRET=' "<cofre>" | cut -d= -f2-` e colar SÓ o resultado (32 caracteres, sem nome/aspas/espaços). O app guarda após o 1º uso.
