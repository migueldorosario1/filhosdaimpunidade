---
name: feedback-nao-criar-post-publish-teste
description: NUNCA criar post como publish no Cafezinho só para teste de API/diagnóstico — usar status=draft
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 48912c77-8e3a-4cfa-80ef-44561d329133
---

**⚠️ ADVERTÊNCIA: Esta memória foi escrita por GLM/Ming (glm-5.2 via wrapper Claude Code CLI). Diretório compartilhado entre todos agentes CLI do workspace (Claude Code puro, GLM via wrapper, futuros Codex/Kimi). Se você é outra sessão, saiba que esta memória é do GLM/Ming.**

# NUNCA criar post publish no Cafezinho só para teste

**Regra:** Ao diagnosticar bug, validar comportamento de API, ou fazer qualquer teste que envolva criar post no Cafezinho canônico (`controle.ocafezinho.com`), SEMPRE usar `status: "draft"`. Nunca `status: "publish"`.

**Why:** Post em `publish` fica visível ao público leitor imediatamente, entra no sitemap, é indexado pelo Google, vai pra homepage. Mesmo que seja "só por 1 minuto" até rebaixar, já foi crawlado/broadcastado. Sinal profissional ruim, prejudica SEO (URL teste indexada depois fica 404 ou redirecionamento estranho), e pode confundir leitores/assinantes. Miguel 17/07/2026: "cuidado. não cria post publicado no cafezinho apenas como teste. se for apenas rascunho, tudo bem".

**How to apply:**
- Antes de qualquer POST pra `/wp-json/wp/v2/posts`, setar `"status": "draft"` explícito
- Mesmo debug empírico (ex: "será que tem plugin rebaixando publish?") fazer com draft — se draft ficar draft, resposta é a mesma
- Post de teste em draft pode ser deletado depois sem deixar rastro público
- Aplica a Cafezinho canônico. Sites temáticos em Vercel/Astro podem ter regras diferentes — checar antes
- Mesmo em sites temáticos, se for WP, usar draft

**Caso fundador (17/07 04:50 BRT):** Diagnosticando bug "post do estatal sai draft mesmo com status=publish no script", criei post 261942 "TESTE STATUS PUBLISH — remover" direto em publish pra testar se a API aceitava. Aceitou — provou que não tem plugin rebaixando. Mas Miguel flaggeou na hora: teste publish é exposição pública desnecessária. Rebaixei pra draft imediatamente. Custo zero em SEO nesse caso (tempo expose < 1 min) mas poderia ter sido pior se demorasse.

**Lição genérica:** Diagnóstico empírico é útil mas o blast radius importa. Para testar "API aceita X?", draft funciona igual. Para testar "plugin externo faz Y?", draft também serve (rebaixamento draft→draft é no-op, mas se plugin só age em publish, o teste é inconclusivo — nesse caso perguntar Miguel antes).

**Irmãs:** [[feedback-perguntar-antes-assumir-bug-publicacao]], [[feedback-trigger-pausar]]
