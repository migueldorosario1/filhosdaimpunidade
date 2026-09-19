---
name: manifesto-antes-de-acao-grande
description: "Toda operação de blast radius alto (reorganização, backup em massa, delete, rename estrutural, migração) requer MANIFESTO detalhado antes da ação. Miguel pode conceder autonomia total baseado no manifesto, sem interrupções, desde que nada seja apagado (só movido pra legacy)."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 37e2f19f-f9dc-43d8-a2fa-f9029a716a89
---

# 🛡️ Manifesto antes de ação grande

**Regra:** antes de qualquer operação de blast radius alto (reorganizar/backup/delete/rename estrutural/migrar), gerar **manifesto detalhado** que permita reverter tudo.

**Why:** Miguel autoriza autonomia total baseado no manifesto. Sem manifesto rigoroso, sessão paralisa em pedidos de confirmação; com manifesto rigoroso, agente executa até o fim sem interrupção. Precedente 17/07/2026: reorganização de 22+ itens do workspace pra `~/legacy/` unificado — cada movimento gerou MANIFEST.md + inventario.json + entrada em INDEX.md mestre. Miguel: "faça um manifesto muito detalhado, pode fazer isso sozinho, sem interrupções, sem precisar da minha intermediação. seria o ideal para mim. desde que voce nao apague nada, mas mova para legacy e anote tudo num manifesto, que por sua vez é indexado no cérebro, não temos risco, entao voce pode seguir sozinho até o fim".

**How to apply:**

1. **Manifesto por item** — cada arquivo/dir movido gera `MANIFEST.md` com: origem completa, data mv, tamanho, count, MD5 dos maiores, comando exato pra restaurar
2. **INDEX mestre** — linha resumo por item, grep-friendly
3. **Inventário machine-readable** — `inventario.json` por item com todos os arquivos + tamanhos
4. **MOVE only, never DELETE** — nada é apagado; tudo vai pra `~/legacy/` (ou destino similar)
5. **Backup de rede de segurança** — antes de operações mais críticas (rename estrutural, migração), backup extra em cloud (Drive/B2)
6. **Consultar manifesto Miguel** antes de julgar "antigo por timestamp isolado" — pode haver plano em curso (ex: V4.1) sem mods recentes

**Ferramentas:**
- Script canônico: `/home/migueldorosario/legacy/scripts/mover_pra_legacy.py`
- INDEX mestre: `/home/migueldorosario/legacy/INDEX.md`
- Buscador pra recuperar itens: `busca "<slug>" --sistema legacy_unificado`

**Reversibilidade:**
```bash
# Restaurar item específico
mv "/home/migueldorosario/legacy/<slug>" "<path_original_do_MANIFEST>"

# Ver todos movimentos
cat /home/migueldorosario/legacy/INDEX.md

# Buscar item movido
busca "<termo>" --sistema legacy_unificado
```

Irmã de [[project_sprint_reorganizacao_workspace_20260717]] que é o caso de aplicação.
