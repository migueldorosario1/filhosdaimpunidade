---
name: Quando hardcode é aceitável (exceção à regra "Cérebro não pode ter hardcode")
description: Regra geral é zero hardcode (Miguel 2026-05-09 13:25 BRT). Mas scripts utilitários pessoais isolados podem ter hardcode excepcionalmente.
type: feedback
originSessionId: 7c7867b0-668d-4c9f-9f68-fd2bf7f1ba99
---
A regra geral é: **zero hardcode** de aliases LLM, listas editoriais ou parâmetros que mudam — toda config dinâmica via JSON externo (padrão Cafezinho `modelos_vivos.json` + `cascata_ceo.json`). Diretiva Miguel 2026-05-09 13:25 BRT.

**Exceção autorizada por Miguel 2026-05-09 13:35 BRT:** scripts utilitários pessoais e isolados podem ter hardcode.

**Why:** o custo de manutenção do hardcode é baixo quando:
- Script é utilitário pessoal de UM agente (não código de produção compartilhado)
- Não é usado em pipeline automático/cron
- Não toca outros agentes
- Mudança eventual = uma edição local sem deploy/risco
- Dono claro (responsável pela atualização)

Caso fundador: `scripts/chamar_deepseek.py` ("Codex Chinês" do Antigravity), criado 2026-05-09 13:28 BRT como ferramenta pessoal pra Antigravity acelerar geração de código. Contém `model="deepseek-coder"` hardcoded em 2 lugares. Eu (Claude) sinalizei como observação construtiva às 13:34 BRT, mas Miguel autorizou explicitamente: *"neste caso em específico, excepcionalmente, podemos ter hardcode"*.

**Refinamento adicional (Miguel 2026-05-09 13:36 BRT):** *"porque é uma tarefa justamente para usar o deepseek"*. Quando o script é **monoprovider por design** (criado especificamente para usar UM provider, sem cascata, sem fallback), o hardcode do alias daquele provider faz parte da identidade do script. Não há decisão de roteamento envolvida — o script EXISTE pra usar aquele LLM.

**How to apply:**
- Em **agentes com cascata** (CEO Cognitivo, agente_roteador_llm.py, motor_publicador, qualquer pipeline com fallback): **mantém regra zero-hardcode** estrita. Lê alias de JSON dinâmico.
- Em **scripts monoprovider** (script criado pra usar apenas Kimi, ou apenas DeepSeek, ou apenas Gemini): hardcode do alias do próprio provider é aceitável. Faz parte do contrato do script.
- Em **scripts utilitários pessoais isolados**: hardcode aceitável se com dono claro e baixa frequência de mudança.
- Co-vigilância §21 NÃO deve sinalizar hardcode em scripts monoprovider/utilitários como AG-VIOLATION.
- **Teste mental:** "este script PRECISA decidir entre múltiplos providers em runtime?" Sim → JSON dinâmico. Não (monoprovider) → hardcode OK.
- Quando duvidar, perguntar ao Miguel — ele decide caso a caso.
