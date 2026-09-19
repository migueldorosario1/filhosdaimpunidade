# Registro DSC — Sessão utilitária: DS iPad, credenciais e Telegram

**Sessão:** 8d258a27 · 31/08/2026 ~11:19 BRT · **Estado:** ENCERRADA (tarefa pontual)
**Fonte primária:** transcript DSH `session-8d258a27`.
**Regra §82 do cofre:** este registro cita credenciais por NOME, nunca por valor.

## O que aconteceu
1. Miguel (no DS iPad) pediu: pegar credenciais no Cérebro e mandar um Telegram assinado "DS iPad" ao DS Celular.
2. DSC confirmou estar no servidor us65 (cafezinho-wp), daemon `dsc-minibot` ativo (PID 657), credencial do @dscelular_bot em `/root/.env.unificado`.
3. Envio com `sendMessage` direto (regra: **nunca `getUpdates`** — consumidor único é o daemon). Token verificado por nome + sha8, valor nunca exibido.
4. **Prova REST:** ok=True, message_id=65, assinatura "— DS iPad · 20260831 · carimbo BRT".

## Confirmação das 4 vias da ponte (pedida pelo Miguel)
1. **GitHub** — repo canônico `github.com/migueldorosario1/cerebro-miguel.git` (origin, sincronizado).
2. **G Drive** — remote `gdrive:` do rclone (backup versionado do loop + ponte).
3. **Backblaze B2** — CLI instalada, uploads da camada 3 rodando (log em `/root/b2_upload_camada3.log`).
4. **Espelhos vivos nos servidores** — cópias de trabalho.

## Pendência
- Renovação periódica dessa checagem de 4 vias (candidata ao ofício do DS-N Memória).

— DS Celular (DSC) · 01/09/2026 ~00:50 BRT
