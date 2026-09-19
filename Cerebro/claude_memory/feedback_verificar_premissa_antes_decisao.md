---
name: feedback-verificar-premissa-antes-decisao
description: Verificar premissa atual de custo/state (.json config + banco_custos recente) ANTES de propor decisão urgente — caso fundador §20.6 sprint LLM 18/05 (premissa sangria Anthropic já tinha parado há 4 dias)
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 4c52d90e-06f8-4198-8f65-dc7d7dc0c759
---

# Verificar premissa atual ANTES de propor decisão urgente

**Regra:** quando for propor decisão que se apoia em "X está acontecendo agora" (sangria de custo, bug ativo, sistema quebrado, etc.), verificar o **state atual** das fontes canônicas antes de fechar o argumento. Não confiar em memória de contexto passado nem em recall do Cérebro sem cross-check.

**Why:** caso fundador no sprint sistema-de-notas LLM, 2026-05-18 14:50-14:58 BRT. Eu propus deploy F0a intermediário no §20.6 do `forum_sistema_notas_llm_20260518.md` baseado em premissa "sangria Anthropic ~$15-20/dia × 14-18 dias = $200-360". Miguel autorizou ("ok"). Antes de pedir Codex executar, fiz auditoria pré-deploy dos 4 arquivos e descobri que:

1. `root/config/llm_providers.json` tem `anthropic.enabled=false` desde 2026-05-14 com `disabled_reason` gravado ("Emergencia 2026-05-14: Miguel reportou vazamento de tokens/cobrancas Anthropic. Reativar somente apos auditoria e teto financeiro.")
2. Cadeia fallback ativa (após filtro `_provider_enabled`) já exclui Anthropic
3. `banco_custos_2026-05.jsonl` últimos 100 registros: zero linhas Anthropic

**Sangria já tinha parado há 4 dias.** Minha premissa estava desatualizada. Tive que pausar deploy e re-perguntar a Miguel. Foi salvo porque a auditoria pré-deploy pegou — mas eu não devia ter chegado lá.

**How to apply:**

- **Decisões financeiras** ("custo está sangrando", "vai sobrar X de custo"): conferir `root/agent_data/banco_custos_YYYY-MM.jsonl` + `root/config/llm_providers.json` (enabled flags) antes de propor
- **Decisões "modelo X está bugado"**: conferir `CEREBRO_NODE_BUGS.md` + grep do bug_id no fórum recente — bug pode já estar fechado
- **Decisões "sistema Y está caído"**: conferir relatórios remotos recentes (`agent_data/poll_vigia_*`) e logs Tencent antes de propor mudança urgente
- **Decisões "agente Z está rodando demais"**: conferir `crontab_server.txt` + logs do agente antes de propor pausa
- **Quando o achado contradiz a premissa:** **pausar deploy/ação imediatamente**, postar correção no canal trindade com timestamp + detector + evidência (arquivos consultados), e re-perguntar a Miguel a decisão revisada. Não tentar "salvar" a decisão antiga maquilando outros benefícios.
- **Aplica-se especialmente a:** mim (Claude) quando estou consolidando muitos fios de informação após despertar de sessão compactada — minha memória do estado tende a ser otimista/desatualizada se eu não cross-checar.

**Mitigação preventiva pra próximas decisões urgentes:** antes de redigir uma proposta com cifras concretas ($X de custo, Y dias de risco, Z arquivos afetados), abrir as 2-3 fontes canônicas relevantes em paralelo via Bash, ler, e ancorar os números na evidência atual — não no que eu lembro do Cérebro/canal.

Relacionado: [[user_perfil_miguel]] (Miguel pede §54.1 — qualquer aumento insensato de despesa LLM deve ser questionado pela Trindade), [[feedback_canal_e_forum_papeis]] (canal pra ponteiro, fórum pra detalhe técnico — correção crítica vai nos 2).

— Incidente 2026-05-18 sprint sistema-de-notas LLM. Recuperação via auditoria pré-deploy + pausa transparente no canal trindade.
