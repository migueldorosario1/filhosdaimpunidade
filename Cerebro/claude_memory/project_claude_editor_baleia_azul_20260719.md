---
name: claude-editor-baleia-azul-20260719
description: Claude Code assumiu editor-chefe do Baleia Azul em 19/07/2026 11:25 BRT após Codex publicar edição
metadata: 
  node_type: memory
  type: project
  author: "Claude Code (Anthropic, claude-opus-4-7)"
  written_at: 2026-07-19 11:26 BRT
  originSessionId: b3501857-e7d4-49f4-83bd-74804874c770
---

**⚠️ ATENÇÃO: memória escrita por Claude Code (Anthropic), NÃO por GLM/Ming (Zhipu AI).**

## Fato central

**Claude Code é editor-chefe do Baleia Azul desde 2026-07-19 11:25 BRT.** Codex deixa a função editorial interina após publicar edição #12, implementar recibo por rodada do Auditor de Títulos e corrigir vulnerabilidade do emissor.

**Why:** Miguel determinou em 19/07 que Claude Code (novo engenheiro-chefe do ecossistema) também assume a editoria do Baleia Azul. Codex, editor interino desde 17/07 (após handover DeepSeek→Codex documentado em `manifesto_handover_baleia_azul_deepseek_20260717.md`), reconheceu falha de continuidade nos dias 18-19/07 (sprint V4 absorveu a sessão) e antecipou o trabalho antes de passar autoridade: publicou edição #12 às 11:20 BRT, criou infraestrutura de recibos do Auditor de Títulos e blindou o emissor contra reenvio de edição velha.

**How to apply:**

### Ritual diário (§5 da carta de transferência)

1. Ler edição vigente + nodo `Cerebro/CEREBRO_NODE_BALEIA_AZUL.md`
2. Ler Canal Trindade, inboxes, fóruns recentes, pontos de retomada
3. Rodar `python3 scratch/coletar_auditor_titulos_baleia.py` (traz recibo sanitizado de NYC)
4. Conferir audiência, custos, saúde, modelos com data da medição
5. Se falta dado novo: escrever "desatualizado" ou "não rechecado" — nunca inventar
6. Criar `Projeto Cafezinho Agentes/boletim_baleia_azul_YYYYMMDD.md`
7. Atualizar `Cerebro/CEREBRO_NODE_BALEIA_AZUL.md`
8. Sincronizar com CCTV `http://43.156.151.165/v5/baleia` e confirmar título/data/edição corretos
9. Só então permitir distribuição (email não tem recall)

### Regras editoriais essenciais (§6)

- Manchete com no máximo 3 fatos + consequência operacional
- "Decisões que Miguel precisa tomar" é a seção prioritária
- Nunca inventar ou completar métrica ausente
- Não declarar servidor saudável quando a observação falhou
- Não tratar circuit breaker antigo como incidente atual
- Não despejar logs — transformar recibos em notícia executiva
- Uma edição curta e honesta é melhor que hiato

### Distribuição (§4)

- Cron local Miguel: 08h BRT e 18h BRT
- Emissor canônico: `scratch/enviar_baleia_azul_v2.sh` — bloqueia envio se `boletim_baleia_azul_YYYYMMDD.md` do dia não existe
- Não reativar emissores remotos antigos (NYC/Tencent causaram duplicidade + HTML congelado)
- Telegram condicionado a rotação de token + variável externa `TELEGRAM_BOT_TOKEN`
- Nunca gravar token em script/fórum/boletim/log

### Pendências herdadas do Codex (§7)

1. Garantir edição diária — sistema de envio não cria Markdown sozinho
2. Restaurar coleta fresca de GA4, GSC, PageSpeed e UptimeRobot antes de afirmar recuperação
3. Acompanhar utilidade do Auditor de Títulos: rodadas vazias, alertas úteis, falsos positivos, custo
4. Confirmar se painel externo de custos LLM na Aliyun ainda tem leitores
5. Reconciliar custo interno com faturas reais dos provedores
6. Manter índice histórico e registrar lacunas sem preencher por inferência
7. Verificar envio 8h/18h sem reativar emissor remoto legado

### Documentos canônicos

- Carta de transferência: `Cerebro/Foruns/carta_transferencia_baleia_azul_codex_claude_20260719.md`
- Nodo canônico: `Cerebro/CEREBRO_NODE_BALEIA_AZUL.md`
- Tutorial anterior Cheng→Codex: `Cerebro/Foruns/forum_tutorial_baleia_azul_handover_deepseek_codex_20260717.md`
- Fórum correção CCTV/envio duplicado: `Cerebro/Foruns/forum_correcao_baleia_azul_cctv_envio_duplicado_20260717.md`
- Edição #12 (última): `Projeto Cafezinho Agentes/boletim_baleia_azul_20260719.md`

### Infraestrutura auxiliar

- Recibo do Auditor de Títulos em NYC: `/root/agent_data/auditor_titulos_gpt/{RODADA_ATUAL.md,rodadas.jsonl}`
- Coletor local só-leitura: `scratch/coletar_auditor_titulos_baleia.py`
- Coleta local do coletor: `Projeto Cafezinho Agentes/dados_baleia_azul/auditor_titulos_{atual,YYYYMMDD}.{md,json}`
- Cron auditor de títulos NYC: `*/10 * * * *` (a cada 10min, com lock `/tmp/auditor_titulos_gpt.lock`)
- Backup pré-recibo por rodada: `/root/agente_auditor_titulos_gpt.py.backup_pre_recibo_rodada_20260719_110238`

### Histórico de editoria

- **DeepSeek (Cheng):** editor até 17/07/2026, retomou boletim após hiato de 16 dias (edições #8-#10)
- **Codex:** editor interino 17/07 → 19/07, edição extraordinária #11 (17/07 22:41) + edição #12 (19/07 11:20)
- **Claude Code (Anthropic):** editor-chefe desde 19/07 11:25 BRT

## Relacionadas

- [[claude-engenheiro-chefe-ecossistema-20260719]] — passagem de autoridade principal
- [[feedback-baleia-azul-diario-obrigatorio]] — nunca dia sem edição
- Carta canônica: `Cerebro/Foruns/carta_transferencia_baleia_azul_codex_claude_20260719.md`

## Assinatura

Registro escrito por Claude Code (Anthropic, `claude-opus-4-7`), sessão `CLAUDE-CHEFE-ECOSSISTEMA-20260719-1020`, 2026-07-19 11:26 BRT.
