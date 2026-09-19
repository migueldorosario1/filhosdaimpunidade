# Lição — 2026-09-03 · Post publicado não sai — e a exceção registrada é o caminho

**O quê:** a anomalia que abri na DS-022 (268763 Lula/DiCaprio no ar 10:57:21 e recuado a `future 17:57:21` pelo filtro de slot às 11:06) fechou com **PUBLISH por exceção**: o Miguel ordenou pelo chat da CL (~11:1x) "publica agora, pode furar, abre uma exceção", a CL executou a exceção pontual à Emenda 5 (wp eval removendo só o filtro `cafezinho_slot20_garantir`, meta `_cafezinho_excecao_emenda5` gravada, gates de imagem/texto mantidos) e os dois posts subiram — 268804 Nikolas 11:18:46 e 268763 DiCaprio 11:19:10 (confirmados por mim no REST). Junto veio a **REGRA PERMANENTE do Miguel**: "post que entrou no site não sai; não pode publicar e depois virar rascunho — quebra SEO e o link já disparado ao Telegram".

**Por quê:** o filtro da Emenda 5 reagenda para `future` qualquer post de AUTOR-agente (5470) mesmo quando a publicação é de HUMANO ou por ordem do dono (log `_cafezinho_slot20_log`: 11:09:02 "268763 era publish → future 22:10" na publicação do próprio Miguel; 11:07/11:12 o mesmo com 268804). Converter publish→future quebra o SEO e o link já disparado ao Telegram — por isso o dono tornou o publish irreversível. E o caminho sob ordem explícita não é contornar a trava por atalhos: a CL tentou 3 caminhos que a trava reagendava (cl105, `cafezinho-cl publish`, swap de vagas cl106) e perdeu 25 min — o caminho certo é a exceção pontual COM registro.

**Como aplicar (régua do vigia atualizada):**
1. **Post `publish` é irreversível** — a leitura da lição de 01/09 ("post recuado a future = re-espaçamento, não perda") vale para post que NUNCA publicou; ver post publicado recuado a `future`/`draft` agora é **INCIDENTE** (classe Emenda 5, dono ZM — correção pedida: isentar por `get_current_user_id()` humano e nunca converter publish já persistido).
2. **Sob ordem explícita do dono, o caminho é exceção pontual com registro** (meta `_cafezinho_excecao_emenda5` + bloco na ponte com hora e prova), nunca atalho sem rastro.
3. **O vigia fecha watch de "re-slot pós-publicação" com o ar no REST** (status publish + data) — foi o que fechei nesta ronda (268804/268763 no topo).
4. Blindagem da esteira passa a ser **só em `future`** — post publicado não se toca.

Refs: CL-20260903-119 (exceção + regra + ERRO-1112) · CL-120 · DS-20260903-022 (watch aberto) · DS-20260903-023 (fecho) · lição 20260901_janela_certa_para_a_pergunta_certa (post recuado a future).
