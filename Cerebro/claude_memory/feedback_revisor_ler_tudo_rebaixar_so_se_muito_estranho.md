---
name: feedback-revisor-ler-tudo-rebaixar-so-se-muito-estranho
description: "No loop §90, cada tick lê na íntegra (título+corpo) cada post publicado desde o tick anterior, faz relatório e age como revisor — mas só rebaixa pra rascunho se algo MUITO estranho"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d7137897-dcad-4847-af64-a409ee24938c
---

No loop de monitoramento §90, a partir de 2026-06-01 21:15 BRT (Miguel), cada tick deve:
1. **Ler na íntegra** (título + corpo completo via WP API `content.rendered`) cada post publicado desde o tick anterior — não só o título.
2. **Fazer relatório** por post: veredicto de 1 linha checando vazamento de prompt/meta-discurso LLM, alucinação/factualidade, linha editorial anti-imperialista (nada contra Rússia/Irã/Sul Global — [[feedback_linha_editorial_anti_imperialista_russia_inegociavel]]), categoria correta, padrão-ouro editorial.
3. **Agir como revisor:** se notar algo MUITO estranho → rebaixar pra rascunho via WP API (`status: draft`).

**Why:** Miguel quer vigilância de conteúdo real, não só de métricas/logs. Mas tem medo de despublicar à toa: "cuidado! só se tiver algo muito estranho mesmo! não quero despublicar nada a toa". Casa com [[feedback_soltar_posts_nao_prender]] (soltar-posts-não-prender) e [[feedback_verificar_conteudo_real_wp_ao_flagrar]].

**How to apply:** O limiar de rebaixamento é ALTO. Só rebaixar em casos graves e inequívocos: recusa LLM publicada como título/texto, vazamento de prompt, alucinação factual grave, conteúdo contra Rússia/Sul Global. Para qualquer coisa duvidosa-mas-não-grave (categoria genérica faltando, fecho fraco, lide imperfeito) → REPORTAR no relatório, NÃO rebaixar. Antes de rebaixar, confirmar o conteúdo real no WP (não confiar em log). Título/categoria publicados = domínio editorial de Miguel; rebaixamento é exceção, não rotina.
