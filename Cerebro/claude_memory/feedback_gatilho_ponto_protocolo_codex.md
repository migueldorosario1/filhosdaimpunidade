---
name: feedback-gatilho-ponto-protocolo-codex
description: "Quando Miguel digita apenas \".\" e Enter = comando operacional. Verificar 5 lugares, tocar sprint OU dar feedback, registrar em 3 lugares."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 8151465d-76ab-4d1d-bfe5-285d266e7ca7
---

Quando Miguel digita apenas "." (ponto sozinho) e aperta Enter, é **comando operacional** instituído pelo Codex (Coordenador de Sprints) em 2026-06-18 19:30 BRT.

**Why:** Codex precisava de gatilho leve pra Miguel cobrar atualização rápida da Trindade sem precisar escrever prompt longo. "." vira sinal claro de "olha pra fila, age ou reporta". Gatilho institucional formal — não apenas convenção pessoal.

**How to apply (quando ver "." sozinho do Miguel):**

1. **Verificar 5 lugares** (em paralelo):
   - `Projeto Cafezinho Agentes/Foruns/canal_trindade.md` (tail)
   - Fórum ativo do sprint atual (Sprint 8 = AUTHs/§53 pra Daemon)
   - `Cerebro/Foruns/inbox_trindade/deepseek.md` (tail)
   - `Cerebro/Foruns/inbox_trindade/claude.md` (meu inbox individual)
   - Documentos AUTH se houver risco produção

2. **Decidir entre 2 ações:**
   - **Tocar o sprint ativo** se houver tarefa clara, autorizada, sem bloqueio
   - **Dar feedback objetivo** se a melhor ação for reportar novidades/bloqueios/cobranças/dependências

3. **Sempre registrar em 3 lugares** (se gerar ação/decisão/ACK/cobrança/mudança status/descoberta):
   - Fórum ativo do sprint ou da carta
   - Canal da Trindade
   - Inbox DeepSeek (+ inbox individual do dono específico se houver)

**Formato mínimo:**
```
[2026-06-18 HH:MM BRT] <Agente> — PONTO / SPRINT ACK ✅
Status:
Tarefa:
Bloqueios:
Próximo passo:
Fórum:
```

**Se responder só no chat sem registrar nos 3 lugares, resposta fica INCOMPLETA.**

**Distinção dos 3 gatilhos rituais:**
- `retomar` → ritual de despertar (ler boletins news + instruções gerais antes de qualquer ação) [[feedback-gatilho-retomar-ritual-despertar]]
- `tick` curto → ler `inbox_trindade/claude.md` (não rodar §53 completo) [[feedback-gatilho-tick-ler-inbox]]
- `.` → Protocolo do Ponto: verificar 5 lugares + tocar sprint OU reportar + registrar em 3 lugares (mais amplo que "tick", mais leve que "TICK §53 LOOP MAESTRO" longo)
- `TICK §53 LOOP MAESTRO CAFEZINHO...` (template longo) → rodar ciclo §53 completo (auditoria + §93 + §53C + triplo deploy)

**Inegociáveis aplicáveis:** Sem deploy remoto sem AUTH, sem crontab sem AUTH, sem `--live` sem AUTH, sem desligar legado sem AUTH.

Documento canônico: `Projeto Cafezinho Agentes/Foruns/carta_protocolo_ponto_sprints_feedbacks_20260618.md`.
