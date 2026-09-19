# ⏸️ CHECKPOINT — Grande Reforma: Smoke Tests Pausados

> **Data/Hora:** 13 de junho de 2026, ~14:40 BRT  
> **Status:** ⏸️ PAUSADO — Computador do Miguel vai desligar  
> **Último executor:** Kimi (Maestro Diagnóstico)  
> **Próximo passo:** Aguardar instruções do Miguel e da Trindade

---

## 📍 Onde Paramos

Os **smoke tests de deploy lado a lado na Tencent** foram iniciados e **pausados** a pedido do Miguel para auditoria da Trindade.

### ✅ O que já foi feito:

| # | Teste | Status | Resultado |
|---|-------|--------|-----------|
| 0 | Baseline + Snapshot | ✅ | Servidor estável, 4 processos, crontab backup (114 linhas), snapshot PID 274072 |
| 1 | Criar estrutura | ✅ | `/root/cafezinho/` criado com todas as subpastas |
| 2 | Transferir banco 17 MB | ✅ | 20.000 registros, integridade OK |
| 3 | Validar acorde.sh | 🟡 | Funciona, mas caminhos desatualizados (aponta para legado) |
| 4 | Auditoria banco | ✅ | Zero duplicatas, campos completos, FK OK |
| 5 | Dry-run maestro | ⏸️ | NÃO EXECUTADO |
| 6 | Drafts WP | ⏸️ | NÃO EXECUTADO |
| 7 | Verificar painel WP | ⏸️ | NÃO EXECUTADO |
| 8 | Dry-run GSN | ⏸️ | NÃO EXECUTADO |

### ⚠️ Problemas pendentes:

1. **Código do staging é do legado** — Não tem os patches de `WP_STATUS_GLOBAL` e `BANCO_MIDIA_DB`
2. **Snapshot em background** — PID 274072, status desconhecido
3. **Permissões** — Banco `644` (deveria ser `640`), pasta `755` (deveria ser `750`)
4. **`.env.unificado`** — Ainda não foi criado no staging

---

## 🎯 O que precisa acontecer QUANDO VOLTARMOS

### 🔴 URGENTE — Bloqueante #1 da Migração (prioridade máxima)
**Snapshot Kimi PID 274072** — estimado terminar ~14:46 BRT
1. [ ] Confirmar término: `ls -lh /root/snapshot_root_pre_reforma_20260613.tar.gz`
2. [ ] Calcular SHA256: `sha256sum /root/snapshot_root_pre_reforma_20260613.tar.gz`
3. [ ] Upload B2: enviar para `Cafezinho-pos-grande-reforma-jun2026/pre_deploy_snapshots/20260613/`
4. [ ] Validar upload e registrar checksum no fórum

> ⚠️ **Este é o bloqueante #1 da migração.** Sem o snapshot pré-deploy salvo no B2, não podemos prosseguir com segurança.

### 🟡 Antes de retomar smoke tests:
5. [ ] Aplicar patches nos scripts do staging (Codex/Antigravity):
   - [ ] `BANCO_MIDIA_DB` nos 7 scripts SQLite
   - [ ] `WP_STATUS_GLOBAL` no `motor_publicador.py`
   - [ ] Atualizar `acorde.sh` para apontar `/root/Cerebro/`
6. [ ] Ajustar permissões (Claude): pasta `750`, SQLite `640`
7. [ ] Criar `/root/cafezinho/portal_cafezinho/.env.unificado` com:
   ```env
   BANCO_MIDIA_DB="/root/cafezinho/dados_agentes/banco_midia/banco_imagens_reais.db"
   WP_STATUS="draft"
   AGENT_DATA_DIR="/root/cafezinho/dados_agentes"
   ```

### 🟢 Depois retomar smoke tests:
8. [ ] Teste 5 — Dry-run maestro
9. [ ] Teste 6 — Drafts no WP (com aprovação do Miguel)
10. [ ] Teste 7 — Verificar painel WP
11. [ ] Teste 8 — Dry-run GSN

---

## 📁 Fóruns Relacionados

- `forum_plano_migracao_duplicada_lado_a_lado_tencent_20260613.md` — Plano de deploy
- `forum_smoke_tests_tencent_executados_20260613.md` — Resultados detalhados dos testes
- `forum_grande_reforma_balanco_geral_e_consolidacao_20260613.md` — Consolidação geral
- `forum_organizacao_unificacao_cerebro_20260613.md` — Unificação do Cérebro

---

## 📝 Estado da Grande Reforma

```
FASE 0 — Diagnóstico:     ✅ Concluído
FASE 1 — Backup:          ✅ Concluído (B2 snapshot)
FASE 2 — Organização:     ✅ Concluído (Cérebro unificado na raiz)
FASE 3 — Smoke Tests:     🔄 Em andamento (4/8 concluídos, PAUSADO)
FASE 4 — Patches Segurança: ⏳ Pendente
FASE 5 — Validação WP:    ⏳ Pendente
FASE 6 — Virada Chave:    ⏳ Pendente
```

---

> **Quando voltar:** Resumir este checkpoint para o Miguel, aguardar aprovação para aplicar patches e retomar smoke tests.

— Kimi (Maestro Diagnóstico) — Checkpoint 13/06/2026 14:40 BRT
