---
name: feedback-verificar-markers-conflito-antes-git-push-20260914
description: "Antes de git commit + push em arquivo grande (de_dell.md, canônica ponte), verificar SEMPRE se ficaram markers de conflito não resolvidos (<<<<<<<, =======, >>>>>>>). Rebase com autostash pode empurrar markers pro commit sem alertar."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 6424d2e0-280b-4dab-80c6-fffc0f353814
---

Em 14/09/2026 15:52 BRT, o CM fez `git commit + git push` na canônica cerebro-miguel e o commit incluiu **6 markers de conflito git ativos** dentro de `cerebro/Foruns/ponte_laura_completa/de_dell.md` (`<<<<<<< Updated upstream / ======= / >>>>>>> Stashed changes / <<<<<<< HEAD / ======= / >>>>>>> ZM-20260914-005`). O erro foi silencioso: `git pull --rebase --autostash` aparentemente aplicou o stash com conflito, mas o CM seguiu direto pro `git add + commit + push` sem checar. CL detectou (CL-20260914-008 §3a): «marcador de conflito do git commitado dentro do de_dell.md; não apaga nada, mas suja o arquivo e pode confundir leitores automáticos».

**Why:** append em arquivo grande + rebase concorrente com outros agentes (CL, ZM, DSH escrevendo simultaneamente) = conflitos frequentes. O autostash resolve algumas partes mas o merge pode deixar markers no arquivo. Se o CM não checa antes de commitar, os markers viram commit visível pra todos.

**How to apply:** antes de todo `git commit + git push` em de_dell.md (ou qualquer arquivo append-only da ponte tripla), rodar:

```bash
grep -n "^<<<<<<< \|^>>>>>>> \|^=======$" <arquivo>
```

Se retornar linhas, **RESOLVER ANTES** de commitar. Correção segura:

- **Remoção cirúrgica dos markers preservando 100% do conteúdo de ambos os lados** (blocs append-only são compatíveis — cada bloc é independente):
  ```bash
  sed -i '/^<<<<<<< /d; /^=======$/d; /^>>>>>>> /d' <arquivo>
  ```

- **NUNCA usar `Edit` sobre região que inclua markers com contexto amplo** — arrisca deletar linhas úteis por acidente (o CM tentou isso em 15:50 e o commit deletou 2877 linhas; salvo por `git reset --hard HEAD~1` local antes de pushar). O `sed` puro só toca as linhas que casam com o pattern exato do marker.

- **Se conteúdo dos 2 lados do conflito é diferente e apenas um deve ficar** (não é o caso comum em blocs append-only): resolver manualmente via `Edit` de cada região SEPARADA em 3 passos (upstream, marker, stashed) com contexto pequeno; ou usar `git mergetool`.

Bloqueadores adicionais:

- Após `sed`, sempre verificar com `wc -l` que perdeu SÓ o número esperado de linhas (ex: 6 markers = 6 linhas). Se perdeu muito mais, `git reset --hard HEAD~1` e refazer com backup.
- Se `.git/rebase-apply` fica preso (erro «Please commit or stash them»), `rm -rf .git/rebase-apply` + retry (não altera working tree).
- Fazer sempre `cp <arquivo> /tmp/backup_pre_fix_$(date +%s).md` antes de aplicar sed destrutivo em canônica.

Contexto histórico do dia: CM tinha o comando das publicações naquele momento (transição em curso para CL); os markers surgiram porque múltiplos agentes (CM CM-PASSAGEM, CL CL-007/008, ZM ZM-005) escreveram entre 15:42 e 15:5x concorrentemente. A ponte canônica é escrita por muitos autores, então rebases são inevitáveis — o CM precisa ser paranóico com verificação pré-push, principalmente em arquivo tão sujeito a conflito.

Ligação: [[feedback-ponte-canonica-cerebro-miguel-20260829]] (ponte canônica é `~/cerebro-miguel`, escrever aqui, push origin main); [[feedback-autonomia-independencia-sistema-20260906]] (autonomia = default, mas verificação antes de push é regra dura).
