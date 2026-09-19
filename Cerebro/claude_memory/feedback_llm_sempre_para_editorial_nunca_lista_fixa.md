---
name: feedback-llm-sempre-para-editorial-nunca-lista-fixa
description: "Decisão EDITORIAL sempre via LLM — nunca lista fixa/hardcode/solução mecânica. Determinístico só serve para organização interna, não para output editorial que o leitor vê."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d7137897-dcad-4847-af64-a409ee24938c
---

Para qualquer **decisão editorial** (categoria, título, forma do texto que o leitor vê), usar **SEMPRE LLM**. **Nunca** lista fixa de palavras, hardcode, dicionário keyword→categoria, ou solução mecânica.

**Why:** Miguel (2026-06-02 ~06:00 BRT), reagindo ao guard de categoria por keyword proposto pelo Qwen (resgatar categoria "Redação" genérica via dicionário de palavras-chave). Princípio: *"não quero lista fixa. prefiro llm, sempre. temos que evitar sempre listas fixas, hardcodes, soluções mecânicas. mesmo as determinísticas apenas são boas para organização interna, não para soluções editoriais."* Listas fixas são frágeis e descaracterizam a curadoria editorial.

**How to apply:**
- **Determinístico = OK** para **organização interna** (dedupe, logging, roteamento de dados, validação de schema, estrutura de arquivos, contadores, triggers internos).
- **Determinístico = NÃO** para **output editorial** que o leitor vê (escolha de categoria, conteúdo do título, forma/estrutura do texto publicado).
- Categoria "Redação" genérica em fontes asiáticas → resolver melhorando o **prompt do classificador LLM** (exemplos/contexto de categorias) ou **re-promptando o LLM** na desistência, NÃO com dicionário keyword→categoria.
- Título longo → a **reformulação** já é LLM (bom); um contador de palavras pode servir só como **gatilho interno** que dispara o re-prompt LLM, nunca para reescrever o título mecanicamente.
- Forma de parágrafo → preferir a regra **no prompt do redator** (C1, LLM escreve certo na origem) em vez do normalizador determinístico (C2), pois a forma publicada é editorial.
- Casa com [[project_arquitetura_3_camadas_diretrizes]] ("política em código" vale p/ plumbing/veto de princípio, não p/ substituir curadoria) e [[feedback_nao_censurar_vocabulario_so_principios]].
