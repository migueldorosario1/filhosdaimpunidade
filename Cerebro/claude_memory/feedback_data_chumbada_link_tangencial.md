---
name: Sem data chumbada no lide + link casual com aderência temática
description: 2 regras editoriais que Miguel firmou em 2026-04-20 vendo drafts dos temáticos. (1) Não forçar "Nesta segunda-feira, 20 de abril de 2026" sem certeza da fonte. (2) Link casual da fonte primária tem que bater com o fato central.
type: feedback
originSessionId: ce520e95-41e3-4a15-9648-a544b965e78a
---
**Regra 1 — DATA NO LIDE SÓ COM CERTEZA DA FONTE PRIMÁRIA**

NUNCA abrir lide com "Nesta segunda-feira, 20 de abril de 2026, o preço do café moído..." chumbado pelo sistema. Isso é risco de alucinação temporal.

- Se a fonte não trouxer data explícita, use **ancoragem implícita**: verbos no presente ("mostra", "revela", "recua"), menção ao mês/período derivável ("em março", "nas últimas semanas"), ou simplesmente omitir tempo.
- A atualidade do post é ancorada pelo próprio link/data de publicação — não precisa carimbar.
- Só citar data explícita quando houver **absoluta certeza** de que vem da fonte primária.

**Why:** Em 2026-04-20 Miguel viu o draft 237300 (Inflação café) e 237297 (Matriz Energética) abrindo com "Nesta segunda-feira, 20 de abril de 2026". Diagnosticou como perigo de alucinação — a data veio do sistema, não do material, e qualquer inferência temporal em cima disso é invenção. O CLAUDE.md tinha regra antiga exigindo data absoluta ("V9 Ancoragem Temporal"); foi revertida.

**Where this was hard-coded pre-fix:**
- `publicador_tematicos.py:300` — regra 2 do prompt V9
- `diretrizes_editoriais.py:40` — regra 5 de "Consciência Temporal"
- CLAUDE.md do projeto — seção 5.2 (declaração)

**How to apply:**
- Ao escrever/revisar prompts editoriais, NUNCA injetar `"Nesta {dia_da_semana}, {data_em_extenso}"` como abertura obrigatória do lide.
- Prefira passar a data do sistema como **contexto disponível** (pra evitar anacronismo), mas regra final é: "data só quando certeza da fonte".
- Se vir qualquer agente futuro abrindo posts com data absoluta sem fonte clara, flag como bug editorial.

---

**Regra 2 — LINK CASUAL DA FONTE PRECISA ADERÊNCIA TEMÁTICA**

O link HTML casual no lide ("conforme apurou a Folha", "segundo a Reuters") deve apontar para fonte que cobre o **FATO CENTRAL** do post, não ângulo lateral.

- Se material bruto tem várias fontes, **escolher a que reporta o fato principal**, não a primeira da lista.
- Se nenhuma fonte do material bruto ancora o fato central, **preferir citar fonte oficial (IBGE, Aneel, ANP, BC) sem link** do que linkar para ângulo tangencial.
- Link tangencial é pior do que nenhum link.

**Why:** Em 2026-04-20 Miguel apontou no draft 237300 (Inflação café) o link casual "De acordo com a Folha de S.Paulo, a queda do consumo nas lojas físicas e a expansão das compras online..." — zero conexão com o tema (café/IBGE). O LLM pegou a primeira URL do material bruto sem verificar aderência.

**Where fixed:**
- `publicador_tematicos.py:302-304` — regra 3b do prompt V9 ganhou seção "ADERÊNCIA TEMÁTICA OBRIGATÓRIA".

**How to apply:**
- Ao criar qualquer agente novo que tenha o padrão de "encaixar fonte primária com link casual", incluir a mesma regra de aderência.
- Se for o caso, podemos evoluir pra: selecionar URL via heurística (entity match entre título final e título do artigo-fonte) antes de passar pro prompt.
