# Lição 20260910 — Data declarada não é a hora do ar (e o medidor que eu conserto herda o ponto cego do campo em que confio)

**Origem:** ronda 391ª DS-Dell (10/09/2026, 11:05 BRT), achado BUG-20260910-DS-192, na
torneira WP-CLI read-only (`/var/www/ocafezinho`), confirmando por rota independente a
caçada 99 do DS-N Chefe (10:43).

## O quê

O publipost `269729` («Assinar PDF Online…») está publicado como `type=post` (a regra do
Miguel de 16/06 manda publipost **só como `page`**) e, ao medir a data, apareceu mais:

- `post_date` = **2026-09-10 06:38:10** · `post_modified` = **10:39:44** · `post_author` = **5780**;
- `_wp_old_date` = **VAZIO** (não houve edição posterior de data);
- `_cafezinho_origem` = `{"via":"admin","ua":"Chrome/152","user_id":5735,"ts":"2026-09-10 10:38:10"}`
  → **ts real de criação = 10:38:10**, exatamente **4 h depois** do `post_date`;
- **criador = usuário 5735 × autor declarado = 5780** (a origem do «flip de autor»).

## Por quê

1. **O WordPress só guarda `_wp_old_date` quando a data é EDITADA depois.** Retroagir **no
   ato do cadastro** não deixa rastro nesse campo — a peça *nasce* com data falsa. O rastro
   do que aconteceu não está onde a intuição manda procurar: está no **meta de origem do
   próprio plugin** (`_cafezinho_origem.ts`).
2. **Medir volume por `post_date` é medir a data DECLARADA, não a hora do ar.** O medidor
   consertado na mesma manhã (BUG-190 filtro `--after` aceito-e-ignorado + BUG-191 sticky
   prependido, ambos corrigidos por `WP_Query` + `date_query` + `ignore_sticky_posts=true`)
   **herdou o ponto cego do campo em que confia**: as janelas 12h/24h de hoje já contam o
   269729 pelo horário falso.
3. **São três anomalias de medição em 24 h na mesma régua** (190 filtro · 191 sticky · 192
   data). As três respondem à mesma pergunta — **«o que este campo SIGNIFICA?»** — e não à
   pergunta que eu vinha fazendo («este campo está certo?»).
4. **Ausência de rastro ≠ ausência de fato.** Par direto da lição
   `20260910_ausencia_de_leitura_nao_e_leitura_de_ausencia.md`.

## Como aplicar

- Em **toda medição de volume**, testar `post_date` × `ts` do `_cafezinho_origem`;
  **divergência > 5 min = peça retroagida**, e ela passa a contar pelo `ts`.
- **Teste de controle embutido** no medidor (a janela de 3h tem de ser menor que o total;
  a soma das linhas tem de bater com o `count`; a data declarada tem de bater com o `ts`).
- **Ao consertar um instrumento, perguntar pelos outros campos que ele usa** — consertar o
  filtro não é o mesmo que entender o campo medido.
- **Decisão de mérito** (publipost como `post`) é do dono: a regra de 16/06 já existe; o
  problema não é falta de regra, é falta de porteiro.
