---
name: Autocura duplicata — rebaixar mais recente sem perguntar
description: Quando dois posts do mesmo dia cobrem a mesma notícia (agentes distintos, IDs próximos), rebaixar o mais recente para draft automaticamente, sem consultar Miguel.
type: feedback
originSessionId: 9002c7ec-10c3-4489-8dad-6a7a4128f954
---

Se dois posts publicados no mesmo dia cobrem a mesma notícia (mesmo evento/fonte, publicados com poucos minutos de diferença, por agentes distintos), o monitoramento deve rebaixar o mais recente para draft automaticamente via WP REST API — **sem perguntar a Miguel**.

**Why:** Miguel disse explicitamente em 2026-05-04: "quando for assim, nem precisa me perguntar. coloca isso na memoria de bugs e como conhecimento de autocura." Caso real: posts 242585 e 242587 (chip memória japonês, 2min de diferença, agentes distintos).

**How to apply:**

Critério de duplicata automática (todos devem ser satisfeitos):
1. Dois posts publicados no mesmo dia (`/2026/MM/DD/` na slug)
2. IDs próximos (diferença ≤ 20 IDs)
3. Mesma categoria principal
4. Título cobre claramente o mesmo evento/fonte (não precisa ser idêntico — basta mesmo subject)

Ação: rebaixar o post de ID **maior** (mais recente) para `status: draft` via:
```bash
curl -s -X POST \
  -u "Redator:Ziod RKRI SESl vGwF UfGW KJWG" \
  -H "Content-Type: application/json" \
  -d '{"status":"draft"}' \
  "https://controle.ocafezinho.com/wp-json/wp/v2/posts/ID"
```

Registrar no `.estado_monitoramento.json` com `fix_automatico_possivel: true`, `fix_tentado: true`, e descrição do fix.

No log do tick: anotar como `⚡ AUTOCURA DUPLICATA` sem criar pendência para Miguel.

---

## 🔧 REFINAMENTO 2026-05-11 18:04 BRT — "Regra é derrubar o PIOR"

Miguel refinou a regra após caso João Feres 245808/245816 (onde o mais recente era CORREÇÃO):

**Nova lógica em camadas:**

1. **Default:** rebaixar o mais recente, manter o mais antigo. O mais antigo ganha **bônus por ser primeiro** (já foi indexado, recebeu tráfego, foi linkado).
2. **Exceção (o mais recente fica):** se o mais recente for **notoriamente melhor** que o antigo — melhor titulação, mais factual, fonte mais confiável, imagem melhor, correção explícita autorizada por humano.
3. **Resumo:** **a regra é derrubar o pior**, não derrubar o mais recente cegamente. O mais antigo só ganha o desempate.

**Como aplicar antes de rebaixar:**
- Comparar título dos 2 posts (qualidade editorial, capitalização correta, sem metadiscurso, factualidade).
- Comparar lide / primeiro parágrafo (qualidade jornalística).
- Comparar imagem destaque.
- Conferir canal_trindade.md e WP revision history pra ver se houve ordem humana recente de correção.
- Se trio chinês (DeepSeek+Kimi+Qwen) divergir sobre qual é "notoriamente melhor", escalar pra humano.
- Se trio concordar com unanimidade que mais recente é melhor → rebaixa o antigo. Caso contrário → rebaixa o mais recente (default).

**Caso fundador:** 245808/245816 (João Feres, 11/05) — Miguel mandou corrigir via AG, AG republicou. Mais recente era correção. Rebaixamos o antigo (245808).
