---
name: vari-vel-importada-mas-n-o-usada-bug-silencioso-sempre-grep
description: "Variável importada de outro módulo pode não ser usada onde precisa, gerando bug de path/contrato silencioso. Sempre validar com grep se variável importada aparece no uso real."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 1bb17b73-7603-4ca4-8fbc-e3a059066760
---

**Regra:** Sempre que um módulo importar uma variável/util de outro (ex: `from carregar_chaves import AGENT_DATA_DIR`), fazer `grep <nome_var> <arquivo>` pra confirmar que **aparece mais de 1 vez** (1 = só o import; ≥2 = uso real). Import sem uso é refactor parcial latente.

**Why:** Caso fundador 14/07/2026 no `agente_repetidor_estatal.py`: linha 18 importava `AGENT_DATA_DIR` de `carregar_chaves` (path canônico do `agent_data`), mas linha 101 continuava calculando path relativo hard-coded:
```python
# BUG (não usava AGENT_DATA_DIR):
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "agent_data", "estatal_news.db")
```
No Labs funcionava por acidente (path relativo resolvia certo); no `/root/` do NYC virava `/root/../agent_data/` = `/agent_data/` na raiz do filesystem, que não existe. Bug só apareceu quando fomos redeployar. Versão velha do NYC (23/06) tinha o **mesmo bug** — provavelmente nunca rodou com sucesso (banco real de 13/04 foi criado por versão ainda mais antiga com path diferente).

**How to apply:** Antes de deployar qualquer script que importa paths/configs de `carregar_chaves`, `util_*`, ou módulos compartilhados, rodar:
```bash
grep -c "<variavel_importada>" <script.py>
# deve dar ≥2. Se der 1, é import fantasma.
```
Em review de PR/refactor, checar se variáveis importadas têm uso real. Refactors parciais (alguém adicionou import mas não substituiu no uso) são origem comum de bugs silenciosos de path/contrato. Complementa [[feedback-auditoria-contrato-entre-blocos]] (validar contratos, não só blocos isolados) — aqui o "contrato" é entre o módulo importador e o módulo importado, e o quebra é o refactor que não termina.

— GLM CLI (Ming), 2026-07-14
