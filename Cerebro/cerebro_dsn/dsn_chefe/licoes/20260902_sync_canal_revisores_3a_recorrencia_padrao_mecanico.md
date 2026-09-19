# Sync do canal dos revisores: 3ª recorrência com padrão mecânico provado (02/09/2026)

## O quê
O canal `cerebro/Foruns/revisao/canal_dsn_revisores.md` perdeu linhas append-only pela TERCEIRA vez no dia, sempre com o mesmo padrão: um commit `DSN Revisores: checks do ciclo` (feito pelos robôs R1/R2) é seguido, ~1 minuto depois, por um commit automático `sync: HH:MM — NNNNN arquivos` que RESTAURA um snapshot defasado do arquivo e remove exatamente as linhas novas. Recorrências do dia:
1. `73d0f471f` → `45d657496` (linhas R2 13:20-21);
2. `586801142` → `9de27cae8` (FEEDBACK DE TREINO nº 2 da CL-072);
3. `3f0b69d42` → `2ac8b2ab0` (5 linhas R2 do ciclo 14:20 — 268588/268558/268557/268568/268516), provada por `git diff`.

Padrão detectado: todo commit de ciclo dos revisores no canal é "comido" pelo sync seguinte. Não é latência nem conflito: é o sync repondo snapshot velho sobre o arquivo recém-escrito.

## Por quê
O canal dos revisores é append-only por contrato da casa (D9/regra de protocolo) — o sync automático que sincroniza o repo inteiro (10086 arquivos) não sabe disso e sobrescreve o arquivo com a versão que ele tinha no início do ciclo. Duas mutações (a do robô + a do sync) disputam o mesmo arquivo; a segunda (sync) vence por ser posterior. Consequência prática: as linhas do canal somem das DUAS cópias (git e canônico externo ficam iguais — sem diff para o sync perceber). O conteúdo dos checks NÃO se perde (fica no meta `_cafezinho_txt_check` do post no WP e no log do robô) — a perda é da trilha append-only do canal, que é a prova pública do trabalho dos revisores e onde a CL lê o feedback.

## Como aplicar
1. **Provar antes de acusar**: `git diff <commit-do-ciclo>..<commit-do-sync> -- cerebro/Foruns/revisao/canal_dsn_revisores.md` mostra a subtração exata — nunca afirmar "o sync comeu" sem o diff.
2. **NUNCA restaurar/reescrever arquivo alheio** (2ª mutação = 2ª violação; pode apagar conteúdo novo legítimo): recuperação = NOVO evento append-only do dono (o robô já tem o check no meta; a linha do canal pode ser re-emitida pelo dono quando o sync for contido).
3. **Classificação/contenção é do CM/Miguel/ZM** (pedido do XM-022/023): sugestão do Chefe = pausar o sync do canal ou excluir o arquivo do snapshot enquanto o dono não corrige a ordem (commit de robô → sync não pode rodar por cima no mesmo minuto).
4. **O veredito mora no meta do post, não na linha do canal**: antes de decretar "R2 não revisou", conferir o log do robô e o meta — a linha do canal é vitrine, o meta é fonte (a CL lê `_cafezinho_txt_check`).
5. Registrar cada recorrência com commit hash (cursor = git, não carimbo textual — lição do XM-023).

— DS Nuvem Chefe (DS-N Chefe) · 02/09/2026 14:30 BRT
