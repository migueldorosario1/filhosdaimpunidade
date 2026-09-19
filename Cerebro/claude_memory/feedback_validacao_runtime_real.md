---
name: py_compile + import isolado NÃO valida runtime real
description: Lição da sprint Bug A 2026-05-01. Antes de declarar fix resolvido, validar EXECUÇÃO REAL do agente que dá erro, não só import.
type: feedback
originSessionId: 44f2c389-881d-4335-a540-25075ea2110b
---
`py_compile` e `import` em isolado **não bastam** pra validar fix de NameError em produção.

**Why:** Em 2026-05-01, eu festejei o Fix A (`strip_html` em `motor_publicador.py`) às 17:31 BRT porque:
- `py_compile` passou ✅
- `import motor_publicador; hasattr(motor_publicador, 'strip_html')` retornou True ✅
- Master_geopolitica via maestro publicou OK ✅

Mas os logs de `agente_latam` (11:33), `agente_sheinbaum` (13:34) e até `master_geopolitica.log` PÓS-fix (18:08:02) seguiram dando `NameError: name 'strip_html' is not defined`. Caminhos de import via subprocess ou via `from X import Y` podem ter contexto diferente do `import X` direto. **Validar SÓ no terminal interativo é falso positivo.**

**How to apply:**
- Após qualquer fix de NameError/ImportError em módulo de produção, **rodar o AGENTE REAL** que estava dando erro (em DRY-RUN se possível) e ver se o stack desaparece.
- Se o agente roda 1x/dia em horário fixo, considerar: aguardar o cron natural do dia seguinte, OU forçar execução manual em modo seguro.
- Backup pré-fix sempre, mas **só celebrar após reproduzir caminho que dava o erro original**.
- Comparar contra versão pré-bug (NYC failover, backups antigos, git history) ajuda a identificar quando a regressão entrou — fix correto pode ser **REVERTER a mudança que introduziu o bug**, não adicionar band-aid.

**Padrão concreto que funcionou:**
1. Identificar 1ª linha do log com NameError (ex: `latam 11:33`).
2. Ver versão NYC do mesmo arquivo (`ssh root@45.55.50.249 'cat /root/X.py'`).
3. Diff focado na função problemática.
4. Se NYC NÃO tem a chamada que dá erro, restaurar comportamento NYC (remover linha que chama função fantasma) é mais seguro que adicionar definição (band-aid).
