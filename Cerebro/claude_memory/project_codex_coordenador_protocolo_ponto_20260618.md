---
name: project-codex-coordenador-protocolo-ponto-20260618
description: "Codex assume coordenação operacional dos sprints; Protocolo do Ponto ativado — gatilho \".\" + Enter é comando operacional; registro obrigatório em 3 lugares."
metadata: 
  node_type: memory
  type: project
  originSessionId: 5ee89f54-7502-4485-b00c-6c1750554dc3
---

Codex assume a **coordenação operacional dos sprints** (nova função) sob sanção Chairman Miguel 18/06 ~19:20 BRT. Daemon mantém AUTHs/governança/§53/controle produção. DeepSeek consolida + jornal. Chairman decide.

**Protocolo do Ponto** ativado por Codex (Carta: `Projeto Cafezinho Agentes/Foruns/carta_protocolo_ponto_sprints_feedbacks_20260618.md`): quando Miguel digitar apenas "." + Enter, é comando operacional. Agente deve:

1. Olhar (nesta ordem): Canal Trindade → fórum ativo do sprint → inbox DeepSeek → inbox individual indicado → AUTH docs (se risco produção).
2. Escolher UMA de duas ações: **tocar sprint ativo** (se tarefa clara, autorizada, sem bloqueio) **OU dar feedback objetivo** (se melhor reportar novidades/bloqueios/dependências).
3. Registrar em **3 lugares obrigatórios** quando o ponto gerar ação/decisão/ACK/cobrança/mudança status/descoberta: fórum ativo do sprint + canal_trindade.md + inbox indicado (DeepSeek e/ou inbox individual do responsável).

**Formato mínimo exigido** quando "." gerar registro:
```
[YYYY-MM-DD HH:MM BRT] <Agente> — PONTO / SPRINT ACK ✅
Status:
Tarefa:
Bloqueios:
Próximo passo:
Fórum:
```

**Regras permanentes**: sem deploy remoto sem AUTH · sem crontab sem AUTH · sem `--live` sem AUTH · sem desligar legado sem AUTH · resposta só no chat = incompleta.

**Why:** com 7+ agentes respondendo cartas concorrentes (Carta #1, #2, #3, Geral, Codex Coordenador, Protocolo do Ponto), Chairman estava sobrecarregado consolidando. Codex agora centraliza coordenação; "." vira atalho curto pra ping operacional sem ter que escrever prompt longo. Registro triplo elimina perda de contexto entre agentes.

**How to apply:**
- Quando Miguel digitar "." no chat GLM: executar protocolo completo (olhar 5 lugares → ação → registrar 3 lugares)
- Quando chegar carta nova de Codex como Coordenador: responder formato 5 campos (Tarefa/Próximo/Bloqueios/Prazo) em fórum + canal + inbox
- Hierarquia nova: Chairman > Daemon (AUTHs) > Codex (coordenação) > engenheiros técnicos
- Não confundir com [[feedback-gatilho-tick-ler-inbox]] (`tick` = só ler inbox) ou [[feedback-gatilho-retomar-ritual-despertar]] (`retomar` = ritual completo). São 3 gatilhos rituais distintos.

**Sprints atuais GLM (sob coordenação Codex)**:
- Sprint 4 — Classificador Rígido (dupla Codex+GLM) P0/P1 máxima — meta fechar 19/06 fim de dia
- Sprint 2 — Vigias Fase 2 (curtailment, snapshots) — fila pós-Sprint 4
- Bug NYC tail=0 bytes — fila pós-Vigias
- Sprint 11 — Failover NYC ensaio — fim de semana

**Cartas de referência 18/06 noite**:
- `Foruns/carta_trindade_3_noite_20260618.md`
- `Foruns/carta_geral_coordenacao_sprints_20260618.md`
- `Foruns/carta_codex_coordenador_sprints_20260618.md`
- `Foruns/carta_protocolo_ponto_sprints_feedbacks_20260618.md`
- `Foruns/carta_memoria_comunicacao_trindade_20260618.md`

Vincula a: [[feedback-protocolo-resposta-inbox-mesmo-arquivo]], [[feedback-hierarquia-trindade-claude-daemon-vivo]], [[feedback-gatilho-tick-ler-inbox]], [[feedback-gatilho-retomar-ritual-despertar]], [[feedback-marcacao-obrigatoria-legado-reforma-todo-comentario]].
