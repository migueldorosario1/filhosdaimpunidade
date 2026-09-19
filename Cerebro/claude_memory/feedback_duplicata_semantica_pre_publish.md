---
name: feedback-duplicata-semantica-pre-publish
description: "Antes de publicar draft V4, comparar semanticamente com últimos 30 publish (2-3 dias) e desviar duplicata pra pending — não só pós-publish"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: cf4e142a-050c-46de-b793-bee2464fc7f7
---

**⚠️ Checagem duplicata semântica PRÉ-publish V4 — obrigatória em todo ciclo Vigília:**

Antes de aplicar `wp_post {status:"publish"}` em qualquer draft do autor 5786, buscar `/posts?status=publish&per_page=30&orderby=date&order=desc` e comparar título/tema/evento fáctico com esses últimos 30 publicados (cobre ~2-3 dias). Se detectar match semântico (>60% palavras-chave sobrepostas OU mesmo evento fáctico OU mesma pessoa+ação+data), NÃO publicar — aplicar `wp_post {status:"pending"}` e registrar no `bugs_YYYY-MM-DD.jsonl` com `motivo="duplicata_semantica_pre_publish"` + `duplica_de: 264XXX` + `titulo_conflitante`.

**Why:** Miguel 04/08/2026 22:50 BRT na sessão de retomada `zizi`, ao aprovar o processamento noturno de 17 drafts: *"tem post que tá saindo repetido. Dá uma olhada melhor. Doravante avalia se o post não tem um post parecido mesmo tema. Não muda por enquanto, já foi publicado deixa publicado, mas doravante avalia."* Regra irmã de [[feedback-duplicata-pos-publish-vira-pending]] (aquela é pós — este é pré, pega ANTES da URL ser indexada).

**How to apply:**
- Todo ciclo Vigília V5 (DIA + NOITE): antes de decidir publish, chamar `wp_get('/posts?status=publish&per_page=30&_fields=id,title,date,categories')` e cachear em memória do ciclo.
- Comparar cada draft candidato: (a) tokens do título após stopwords, (b) categorias em comum, (c) entidades nomeadas (pessoa+ação+data no corpo).
- Threshold: >60% palavras-chave sobrepostas OU mesma pessoa+ação num intervalo ≤48h OU mesmo evento (ex: 2 drafts sobre "Ormuz reabertura" no mesmo dia → um vai pra pending).
- Desvio: `wp_post {status:"pending"}` (regra irmã: pending, não trash — Miguel pode revisar depois). Miguel decide se recupera ou descarta.
- Reportar no bloco compacto: linha separada `⚠ 264XXX → pending duplicata de 264YYY (tema)`. Não misturar com publish normal.
- **NÃO tocar em publicados repetidos passados** — Miguel foi explícito: "já foi publicado deixa publicado". Só age pra frente (doravante).
- Casos já observados que motivaram a regra: repetição em ciclos anteriores não catalogada num único bug — Miguel notou padrão empírico ao revisar timeline no ocafezinho.com.
