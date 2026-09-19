# 🧠 Memória — MISSÃO ACELERAÇÃO DSC: credencial Telegram + ronda DSN + bônus — 30/08/2026

> Log técnico completo. Par de Tema Duplo: `Foruns/forum_dsc_credencial_terminal_telegram_20260830.md`.
> Executor: ZM · ZCode/GLM-5.3 (Dell). Ordem: prompt único do Miguel 30/08 ~14:05 BRT (refs DSC-016/023/024/025).

## Arquivos tocados (todos com backup)

| Onde | Arquivo | Ação | Backup |
|---|---|---|---|
| Tencent (ubuntu) | `~/.env.unificado` | +2 linhas (token+chat_id) | `.bak_pre_dsc_bot_20260830_1407` |
| Tencent (root) | `/root/.env.unificado` | +2 linhas | `.bak_pre_dsc_bot_20260830_1407` |
| Tencent | `~/ronda_dsn.sh` | export cirúrgico das 2 vars | `.bak_pre_dsc_telegram_20260830` |
| Tencent | `~/ronda_dsn_prompt.md` | seção 0b TERMINAL TELEGRAM | `.bak_pre_dsc_telegram_20260830` |
| Tencent | `/etc/ssh/sshd_config` | +Port 22 (mantém 38422) | `.bak_pre_port22_20260830` |
| Tencent | ufw | allow from 190.89.239.65 to port 22 | (regra aditiva; regras antigas intactas) |
| Dell | `Projeto Cafezinho Agentes/root/.env.unificado` | +2 linhas (Regra 4) | `.bak_pre_dsc_bot_20260830_1410` |
| Dell | `Outros/chaves/agentes_labs/.env.unificado` | +2 linhas (Regra 4) | `.bak_pre_dsc_bot_20260830_1410` |
| Dell | ponte `de_dell.md` (vivo) | fix marcadores + linha ZM | `.bak_pre_conflito_20260830_1415` |

## Provas

- **sendMessage teste**: ok=True, message_id=18, 20260830 14:14 BRT ("🤖 DSN no ar!").
- **rota B**: ok=True, message_id=19, 14:11 BRT; sha8 `f0aaa272cec` (printf '%s' SEM \n) = hash canônico conhecido da `DEEPSEEK_CAFEZINHO_CANONICO`.
- **porta 22**: `sudo ss -tlnp` mostra sshd em 0.0.0.0:22 E :38422; teste `/dev/tcp/43.156.151.165/22` a partir do us65 → ABERTA.
- **ronda_dsn.sh**: `bash -n` sintaxe OK; grep confirma export das 2 vars; prompt contém "TERMINAL TELEGRAM DSC".
- **1ª ronda com 0b**: 14:30 BRT — verificar `/tmp/ronda_dsn/20260830.log` na Tencent (deve citar INBOX/telegram).

## Arquitetura do terminal Telegram (decisão central)

- `getUpdates` do @dscelular_bot tem **consumidor ÚNICO**: daemon `/usr/local/bin/dsc-minibot.py` (root, cafezinho-wp/us65 190.89.239.65, PID ativo). Ele replica → `cerebro/Foruns/ponte_laura_completa/telegram_dsc/INBOX_MIGUEL.md` e entrega `RESPOSTAS.md` → Telegram.
- DSN (Tencent, 30/30) = ouvinte principal: LÊ o INBOX (réplica do getUpdates) e ESCREVE em RESPOSTAS.md; pode ENVIAR direto (sendMessage com TELEGRAM_TOKEN_DSC_BOT/DSC_BOT_CHAT_ID exportadas pela ronda). **NUNCA chamar getUpdates no DSN** — 2 consumidores roubam updates um do outro (offset confirmatório).
- Fila de resposta (DSC-024): DSN (40 min) → DS Laura → ZCode → Claude Laura → Claude Miguel → AGY → Codex.

## Comandos-chave (receita)

- Patch cirúrgico no ronda_dsn.sh (só as 2 vars, não o cofre inteiro — evita interferir no roteador de LLM do DSN):
  `if [ -f "$HOME/.env.unificado" ]; then for _l in $(grep -E "^(TELEGRAM_TOKEN_DSC_BOT|DSC_BOT_CHAT_ID)=" "$HOME/.env.unificado"); do export "$_l"; done; fi`
- Porta extra no sshd: acrescentar `Port 38422` + `Port 22` (DUAS diretrizes = escuta nas duas), `sshd -t` ANTES do reload.
- Envio direto do DSN: `curl -s -X POST https://api.telegram.org/bot$TELEGRAM_TOKEN_DSC_BOT/sendMessage -d chat_id=$DSC_BOT_CHAT_ID --data-urlencode text=...`

## Incidentes do caminho (lições)

1. **Sync varreu meu append no vivo**: editei `de_dell.md` VIVO às 14:14; o sync repo→vivo reconciliou por volta de 14:16 e apagou meu bloco (repo era mais novo). **Lição: ponte se edita no REPO + commit imediato; o vivo se atualiza DEPOIS.** (Família DS-031.)
2. **Marcadores de conflito no vivo 2× no período**: rebase interrompido com `pull --rebase` silencioso (`>/dev/null 2>&1` engole o conflito). Resolução append-only: manter os dois lados, tirar só os 3 marcadores. Recomendação futura: o script de ronda deveria logar falha de pull.
3. **Regra 4 na prática**: credencial nasceu na Tencent e foi espelhada nos 2 cofres-irmãos do Dell sem perguntar (ordem permanente). No cafezinho-wp NÃO foi preciso (daemon tem token próprio funcionando).
4. **Duplicata de rota B**: ordem minha (~14:05) e execução do DS-Dell (14:03) cruzaram no ar — Miguel recebeu 2× a mesma chave (sha8 idêntico). Inofensivo, mas mostra que CHECK na ponte antes de executar missão "pendente" evita duplicata.

## O que aconteceu / o que falta / o que preciso do Miguel

- **O que aconteceu**: credencial nos 4 cofres + teste Telegram provado + ronda DSN com terminal Telegram configurada + us65→tencent:22 aberta e provada + rota B entregue + fix da ponte viva.
- **O que falta**: 1ª ronda DSN pós-0b (14:30) validar INBOX no log; Miguel repassar a chave ao @dscelular_bot (cofre automático); decisão "vai" p/ apertar ufw 22; DSC-013 (palavra-chave gpg).
- **O que preciso do Miguel**: confirmar recebimento dos 2 recados; "vai" (ou não) do aperto da porta 22.

— ZM · ZCode/GLM-5.3 · 20260830 14:20 BRT

---

# 🧠 ADENDO — sprint robô-ponte: testes, fixes e provas — 30/08 14:52 BRT (ZM)

## Daemon analisado (`/usr/local/bin/dsc-minibot.py`, us65, systemd `dsc-minibot`, Restart=always)

- Loop 20s + getUpdates long-poll 20s; offset persistido `/root/.dsc_minibot_offset`; repo de trabalho `/root/Cerebro`.
- Ramos: áudio (getFile→download→ack→INBOX→sync) · texto (sk- intercept ANTES de tudo → `/root/.dsc_deepseek_key` 600 → continue; ack com ETA da ronda DSN e aviso da fila 40min; camada LLM se chave existir; INBOX→commit→pull --rebase→push) · entrega RESPOSTAS (regex `## [ts · agente] RESPOSTA_PRO_MIGUEL`, dedup SENT_FILE).
- **Bugs achos pelo ZM**: (1) NameError `ts` no ramo de áudio (13:55, corrigido pelo DSC 14:40 — `ts=brt()` movido p/ antes do try); (2) dedup SENT_FILE `.split()` tokenizado → 1 duplicata por restart (Miguel recebeu a resposta do DS-N 2×) — FIX ZM `.splitlines()` + log `entregue:` no journal; SENT_FILE deduplicado (1 linha); restart 14:48 `active`. Backup `.bak_pre_zm_fix_20260830`.
- **Artefatos de teste**: `/tmp/t6_intercept_test.py` (sandbox da interceptação — reutilizável) e `/tmp/patch_minibot.py` (patch aplicado).

## Provas coletadas

- T1: commits AUTO `9214e424e` (13:38:07) e `a34de091e` (13:38:09) vs blocos 13:38:04/13:38:09 → replica+commit ≤3s; ack síncrono antes.
- T2: `/root/.dsc_audios/1788108927.ogg` = Ogg/Opus mono 48kHz (áudio real do Miguel); bloco INBOX recuperado pelo ZM (commit 14:48, assinatura explícita — NÃO falsificado como AUTO).
- T3: push 14:48:33 → journal `entregue: ZM 2026-08-30 14:48:30 BRT` às 14:49:05 = **32s**; SENT_FILE `2026-08-30 14:48:30 BRTZM`.
- T6: script sandbox 3 asserts (estrutura/comportamento/repo) — PASS; cofre real intacto.
- Cérebro: chamada idêntica à do daemon respondeu "o que tá rolando na casa hoje?" corretamente (persona + contexto + limites).
- getUpdates consumidor único confirmado (daemon); DSN instruído a NUNCA consumir (offset rouba updates).

## Comandos úteis (receita)

- Journal do robô: `ssh cafezinho-wp 'journalctl -u dsc-minibot -n 20 --no-pager'`
- Latência de entrega: comparar `git push` (Dell) × linha `entregue:` no journal (us65).
- Estado: `cat /root/.dsc_minibot_sent` (entregues), `ls /root/.dsc_deepseek_key` (IA armada?), `ls /root/.dsc_audios` (áudios).

## Lições

1. Teste de fogo de daemon com estado em arquivo DEVE incluir restart (bug de dedup só aparecia lá).
2. Regex de dedup + persistência precisam da MESMA granularidade (linha inteira vs tokens).
3. `code.find()` pega a 1ª ocorrência — em código com ramos parecidos, buscar a partir da âncora certa (assert estrutural do T6 falhou 1× por isso).
4. Não falsificar bloco AUTO: recuperação de histórico perdido entra assinada pelo recuperador.
