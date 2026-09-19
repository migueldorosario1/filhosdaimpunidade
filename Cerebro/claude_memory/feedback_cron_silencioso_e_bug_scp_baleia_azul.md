---
name: feedback-cron-silencioso-bug-scp-baleia-azul
description: Cron do Baleia Azul (emissor v2) rodou pelo menos 2x com scp:ambiguous target em 18/07 18h e 19/07 08h — nenhum email chegou ao Miguel. Log em /tmp/baleia_azul_envios.log que ninguém monitorava. Fix aplicado 19/07 15:40 BRT.
metadata: 
  node_type: memory
  type: feedback
  author: "Claude Code (Anthropic, claude-opus-4-7)"
  written_at: 2026-07-19 15:45 BRT
  originSessionId: b3501857-e7d4-49f4-83bd-74804874c770
---

**⚠️ ATENÇÃO: memória escrita por Claude Code (Anthropic), NÃO por GLM/Ming (Zhipu AI).**

## Regra

**Cron que grava log em `/tmp/*.log` sem alertar ao vivo é cron silencioso. Toda linha de cron que envia comunicação externa (email, Telegram, WhatsApp) deve ter (a) exit-code check no wrapper, (b) alerta ativo em falha (email de sysadmin, arquivo `AGUARDANDO_MIGUEL.md`, mensagem no canal Trindade), (c) log em local persistente (não `/tmp`), (d) rotação de log.**

**Bugs em scripts de infra que envolvem `scp`, `rsync`, `ssh` com paths contendo ESPAÇO exigem escape em dois níveis: shell local + shell remoto. Sintaxe correta: `"${REMOTE_HOST}:\"${REMOTE_PROJECT}/${FILE}\""` — aspas duplas literais envolvem o path remoto.**

**Why:** Caso fundador em 2026-07-19. Miguel perguntou se Baleia Azul iria por email. Investigação revelou:

1. Emissor `scratch/enviar_baleia_azul_v2.sh` (Codex 17/07) usa `scp` para sincronizar boletim antes de enviar email. Linha 47 original: `scp ... "$PROJETO/$BOLETIM_ATUAL" "$REMOTE_HOST:$REMOTE_PROJECT/$BOLETIM_ATUAL"` — path remoto contém "Projeto Cafezinho Agentes" (com espaços). `scp` interpreta espaço como separador de destinos múltiplos → `scp: ambiguous target`.
2. Log `/tmp/baleia_azul_envios.log` mostra que cron **rodou pelo menos 2x com falha silenciosa antes da descoberta**:
   - `[sáb 18 jul 2026 18:00:06 -03] ERRO: falha ao sincronizar boletim_baleia_azul_20260717.md com o CCTV`
   - `[dom 19 jul 2026 08:00:06 -03] ERRO: falha ao sincronizar boletim_baleia_azul_20260717.md com o CCTV`
3. Codex publicou edição #12 (19/07 11:20 BRT) e sincronizou CCTV manualmente — mas **edição #12 nunca chegou por email ao Miguel**. Nem #11 (17/07 22:41 extraordinária), nem qualquer edição desde 17/07.
4. Ninguém percebeu porque:
   - Log em `/tmp/` (limpo em reboots, não versionado, sem rotação)
   - Cron falhou com exit 3, mas cron por padrão só notifica se `MAILTO` configurado
   - Ninguém monitora `/tmp/baleia_azul_envios.log`
   - Miguel não recebia email mas não sabia que devia esperar

**Fix aplicado 2026-07-19 15:40 BRT** (Claude Code):
- Linha 47 corrigida: `"${REMOTE_HOST}:\"${REMOTE_PROJECT}/${BOLETIM_ATUAL}\""` (aspas duplas escapadas envolvendo path remoto).
- Backup preservado: `scratch/enviar_baleia_azul_v2.sh.bak_pre_scp_fix_20260719_1540` (SHA-256 `1268c1dbee1a0e33f903fdac85badb776b57c522ad6bd4e14a7652c9a32a1c5b`).
- Teste manual 15:36 BRT: emissor rodou exit 0, edição #12 enviada com sucesso pro Gmail do Miguel, caixa de entrada confirmada.

**How to apply:**

### 1. Padrão universal para scp/rsync/ssh com paths contendo espaço

```bash
# ERRADO — scp interpreta espaço como separador
scp arquivo user@host:/path com espaço/arquivo

# CERTO — aspas duplas literais envolvem path remoto (duplo escape shell)
scp arquivo "user@host:\"/path com espaço/arquivo\""

# Alternativa CERTA — escapar cada espaço com \ literal
scp arquivo "user@host:/path\\ com\\ espaço/arquivo"
```

### 2. Toda cron de comunicação externa deve alertar em falha

Padrão mínimo:

```bash
#!/bin/bash
LOG="/var/log/meu_script.log"  # persistente, NÃO /tmp
LOCK="/tmp/meu_script.lock"

exec > >(tee -a "$LOG") 2>&1

if ! flock -n 200; then
    echo "[$(date)] AVISO: lock ocupado, saindo" >&2
    exit 0
fi 200>"$LOCK"

if ! comando_principal; then
    echo "[$(date)] ERRO CRÍTICO em comando_principal" >&2
    # Alerta ativo — pelo menos UM dos abaixo:
    echo "$(date) $HOSTNAME falhou: <detalhes>" >> "$WORKSPACE/AGUARDANDO_MIGUEL.md"
    curl -fsS -X POST "$WEBHOOK_URL" -d "..."  # se webhook disponível
    exit 1
fi
```

### 3. Log persistente + rotação

- Nunca gravar log de cron em `/tmp/` — usar `/var/log/<script>.log`, `~/.local/log/`, ou dentro do workspace.
- Configurar logrotate ou implementar rotação manual (>10MB → arquivar).
- Log deve conter timestamp completo (não só `date` sem `-Iseconds`).

### 4. Verificação de saúde diária/semanal

- Editor-chefe do Baleia Azul (Claude Code desde 19/07) DEVE verificar `/tmp/baleia_azul_envios.log` OU log persistente equivalente antes de cada edição.
- Adicionar ao ritual §5 da carta de transferência: "0. Verificar log do emissor pra confirmar que edições anteriores realmente saíram."

### 5. Fallback ativo

- Se emissor primário falha, tentar secundário (msmtp local + SMTP Gmail com App Password).
- Notificar Miguel imediatamente por canal alternativo (arquivo, webhook, Telegram).
- Nunca deixar "falhou silenciosamente" ser aceitável para comunicação externa.

## Consequência histórica

Última edição do Baleia Azul que Miguel efetivamente recebeu por email: pré-17/07 (data exata desconhecida — cron pode ter quebrado antes). Edições #10 (17/07), #11 extraordinária (17/07 22:41), #12 (19/07 Codex) — **todas geradas, todas no CCTV, nenhuma no email do Miguel** até fix de 19/07 15:40 BRT.

Miguel operou dias sem receber o boletim diário achando que estava chegando. Só descobriu porque perguntou "vai por email né?". Isso é falha institucional grave — Baleia Azul é a primeira leitura de despertar, e não estava chegando.

## Relacionadas

- [[feedback-cron-como-codigo-producao]] — cron é código de produção
- [[feedback-baleia-azul-diario-obrigatorio]] — nunca dia sem edição (agora expandido: nunca dia sem entrega confirmada)
- [[claude-editor-baleia-azul-20260719]] — nova editoria
- Carta transferência editorial: `Cerebro/Foruns/carta_transferencia_baleia_azul_codex_claude_20260719.md`

## Assinatura

Registro escrito por Claude Code (Anthropic, `claude-opus-4-7`), sessão `CLAUDE-CHEFE-ECOSSISTEMA-20260719-1020`, 2026-07-19 15:45 BRT.
