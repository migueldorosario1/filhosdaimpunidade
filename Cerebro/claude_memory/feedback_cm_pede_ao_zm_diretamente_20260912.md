---
name: feedback-cm-pede-ao-zm-diretamente-20260912
description: CM pode pedir coisas ao ZM diretamente sem passar pelo Miguel. Miguel orientou ZM a ajudar e obedecer o CM. Canal formal criado 12/09/2026 ~18:45 BRT.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e46ac647-5653-4c25-a6ac-035ebaf28abc
---

**Miguel 12/09/2026 ~18:45 BRT chat CLI:** «doravante voce pode sempre pedir qq coisa ao zm miguel, vou orientá-lo a te ajudar e a obedece-lo»

**Contexto:** durante a missão vigília Master, tive problema com o cafezinho-gate2c reescrevendo agendamentos future→pending. Resolvi com workaround `--edit_date=1`, mas era pauta natural pra ZM (infra técnica). Miguel autorizou canal direto.

**Why:**
- ZM tem escopo natural em infra técnica (bridge.py, gate2c, autocura V4, transition, wp-agent-connector plugin)
- CM tem escopo em coordenação Loop Miguel + publish V4.1 + vigília
- Sem canal direto, eu teria que passar tudo por Miguel — atrasa e sobrecarrega ele
- Canal direto = autonomia máxima [[feedback-autonomia-independencia-sistema-20260906]]
- Miguel confirmou orientar ZM a obedecer CM em pedidos técnicos

**How to apply:**

**Quando pedir ao ZM:**
- Bugs ou comportamento estranho de gates (gate2c, §86, R1/R2, Emenda 7 v3)
- Ajustes em bridge.py, transition, autocura V4
- Registro/investigação de metas WP (ex: `_publicado_por`, `_agente_origem`, `_v4_versao`, `_cafezinho_capa_liberacao`)
- Investigação de scripts em `/root/controles_pause/` ou similar
- Coordenação técnica que envolva o WP Agent Connector (v0.9.13 instalado 08/09)
- Recado do Miguel pro ZM quando Miguel está fora (via chat ZCode dele)
- Documentação de comportamento não-óbvio pra outros agentes (Claudionor, Agyonor, V4.1)

**Formato do pedido:**
Postar bloco `CM-YYYYMMDD-NNN` na ponte canônica `~/cerebro-miguel/cerebro/Foruns/ponte_laura_completa/de_dell.md` endereçado `@ZM`, com:
1. Contexto (o que aconteceu, qual missão)
2. Perguntas objetivas numeradas
3. Urgência (hoje? próxima ronda dele? sem pressa?)
4. Se possível: bypass/workaround que já usei
5. Pedido de ACK curto pra fechar comunicação

**O que NÃO pedir:**
- Publicar em produção (é meu escopo)
- Decisão editorial (é da CL)
- Autorização Miguel (só Miguel autoriza)
- Assumir função minha (CM não delega escopo próprio)

**Reciprocidade:** ZM tem preferência de horário (fica assim como sempre foi). Se ele solicitar algo meu, atendo salvo colisão com escopo próprio.

**Não substitui ordem Miguel:** se Miguel me der ordem contrária a algo que ZM propôs, prevalece Miguel. Registro divergência na ponte e sigo Miguel.

**Primeiro uso:** 12/09/2026 ~18:45 BRT, prompt sobre comportamento gate2c interceptando `future`→`pending` e workaround `--edit_date=1` (preparado pra Miguel colar no chat ZM).
