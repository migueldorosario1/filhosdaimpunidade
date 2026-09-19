---
name: feedback-auditoria-contrato-entre-blocos
description: "Em sprint de desacoplamento (mudança de arquitetura em blocos), auditar o CONTRATO ENTRE BLOCOS (chaves, valores enumerados, schema), não só cada bloco isolado. Caso fundador V3 B-049 22/06."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f312988d-5dc6-4ea6-b08a-94b4cada57ec
---

Em auditoria de sprint que reorganiza/desacopla arquitetura em blocos (ex.: produtor → preparador → publicador), **não basta validar cada bloco isolado**. Sempre cruzar o **contrato entre blocos**: chaves enumeradas (`status='escolhida'` vs `'aprovada'`), schemas de dict, tipos esperados, valores defaults, ordem de chamada.

**Why:** Sprint Codex V3 22/06 (editor_final + preparar_midia_pronta) — eu auditei `v3_preparar_midia_pronta.py` (smoke OK, cooldown OK, fallback R2 OK) e `executar_publicador_wp_v3_pending.py` (gates OK, B-007 OK, B-018 OK) **isoladamente**. Perdi o bug V3-B049: preparador gravava `midias_candidatas.status='aprovada'` enquanto publicador L305 exigia `'escolhida'`. AGY-CLI flagrou no parecer paralelo; Codex corrigiu em 19s. Validei a sintaxe das chamadas mas não o valor literal das enumerações.

**How to apply:**
1. Em sprint de desacoplamento, montar mentalmente o **fluxo de dados entre blocos**: bloco A grava o quê em qual tabela → bloco B lê o quê com qual filtro WHERE?
2. Cruzar grep `status='X'` no bloco produtor com grep `status != 'X'` no bloco consumidor — divergência é bug latente.
3. Em fluxos SQLite: olhar TODOS os `INSERT VALUES (...)`, `ON CONFLICT DO UPDATE SET ... = 'X'` no produtor + TODOS `WHERE status = 'X'` / `if x.get("status") != 'X'` no consumidor.
4. Validar não só o dict literal Python mas também o SQL hardcoded (frequentemente o dict é só visual, o SQL é o que persiste).
5. Sempre rodar smoke do **fluxo cruzado** (produtor cria → consumidor lê) — smoke isolado de cada bloco não pega contrato.

Aplicação imediata: próximas auditorias V3 ou de qualquer sprint multi-arquivo, dedicar fase explícita "contrato entre blocos" antes de fechar parecer.
