---
name: feedback-monitoramento-ler-titulos-conteudo
description: "Durante monitoramento Cafezinho, LER o conteúdo (título + lide) dos posts recentes — não só metadados (featured_media, categoria). Erros factuais graves (Banco Central vs Banco Master) passam batido se Claude só olha estrutura."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: bd63951a-ed35-4ca0-8a29-b1a900604520
---

# Monitoramento Cafezinho — sempre ler título+lide, não só metadados

**Regra:** Em cada tick do loop maestro, ler com atenção o título e o lide (primeiro parágrafo) dos posts recentes — não apenas conferir `featured_media`, `categories`, `status`.

**Why:** Em 27/05/2026 às 23:57 BRT, durante o Tick 4 do loop monitoramento, Miguel pegou um erro factual GRAVE que eu deixei passar: post #252345 publicado como "Dono do **Banco Central** pagou jantar com ouro e chef Salt Bae para aliado de Flávio Bolsonaro" — o correto é **Banco Master** (banco privado de Daniel Vorcaro). Confundir Banco Central (autoridade monetária) com Banco Master (banco privado em escândalo) é difamação ao BC + risco legal sério. Eu estava reportando o post como "§86 violado (sem imagem) + categoria 1 (Uncategorized)" — perdi completamente o erro de conteúdo que era muito mais grave.

**How to apply:** Durante o tick:
- Não basta `print(p['title']['rendered'][:75])` — ler título inteiro com atenção, comparar com conhecimento do mundo (Banco Central vs Banco Master, papa Francisco vs León XIV, presidente vs ex-presidente)
- Spot-check editorial é obrigatório (§90 já fala isso mas eu não aplicava de verdade)
- Erro de conteúdo > erro de metadados na ordem de prioridade do reporte
- Quando flagrar bug técnico, perguntar "e o conteúdo, está OK?" antes de seguir
- Aplicar §66.2 também aos próprios posts publicados (não só aos modelos LLM): "fact-check humano-light antes de declarar tick verde"
