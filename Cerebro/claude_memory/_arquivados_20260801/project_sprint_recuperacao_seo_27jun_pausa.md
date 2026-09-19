---
name: project-sprint-recuperacao-seo-27jun-pausa
description: Sprint recuperação SEO Cafezinho CONCLUÍDA 27/jun 17:25 BRT — snippet noindex ATIVO + smoke test passou 3/3. Falta só monitorar Search Console nas próximas 4-12 semanas.
metadata: 
  node_type: memory
  type: project
  originSessionId: 938ec415-ffd7-4244-9eb7-ff612fa44246
---

✅ **Sprint recuperação SEO Cafezinho — CONCLUÍDA com sucesso 27/jun 17:25 BRT. Snippet noindex 358 URLs ATIVO em produção via Code Snippets do wp-admin de https://controle.ocafezinho.com/. Smoke test passou nos 3 cenários (clickbait noindex / geopolítica protegida / homepage OK). Próximo: monitoramento Search Console 4-12 semanas (sem ação imediata).**

**Why:** Cafezinho perdeu 98,91% do Discover (111.614 → 0 cliques/dia entre 15/abr e 15/jun) por excesso de matérias clickbait fora-do-nicho. Trindade Round 2 unânime: podar via noindex,follow. Sprint executado em 4 horas (13h → 17:25 BRT).

**How to apply:**

- **Próxima sessão:** primeira ação é checar Google Search Console (Indexação > "Excluído por noindex") nas próximas semanas. Métrica deve subir de ~zero para ~358 ao longo de 30-60 dias.

- **Sprint concluído 9/9 etapas (mecanismo via Code Snippets, não mu-plugin):**
  1. ✅ Passo 1 — Triagem T1 (38 URLs): 0 falso positivo
  2. ✅ Passo 3a — Buscar post IDs WP REST (352 OK em 9,4min)
  3. ✅ Passo 3b — Rebuscar 5 erros + investigar 3 NOT_FOUND
  4. ✅ Passo 3c — Mu-plugin (136 linhas) + snippet adaptado (110 linhas, 358 IDs)
  5. ✅ Passo 3d — Validação PHP estrutural
  6. ✅ Passo 3e — Apresentado pra Miguel
  7. ✅ Passo 3f — Snippet COLADO E ATIVADO no Code Snippets (SSH no servidor ServerDo.in falhou, mudou pra Code Snippets que já estava ativo)
  8. ✅ Passo 3g — Smoke test passou 3/3:
     - NASA SR-1 (clickbait): header `x-robots-tag: noindex, follow` + meta `<meta name='robots' content='noindex, follow' />`
     - Russia/Oreshnik (geopolítica protegida): NÃO tem noindex, mantém `index, follow`
     - Homepage: HTTP 200 OK, zero erros PHP, 321 ocorrências de "cafezinho" (renderizou normal)
  9. ⏳ Passo 3h — Monitorar Search Console 4-12 semanas (passivo, sem ação)

- **Arquivo do snippet em produção:** `Projeto Cafezinho Agentes/wordpress_mu_plugins_staging/code-snippet-noindex-pronto-para-colar.php`

- **Para reverter (se necessário):** abrir Code Snippets em https://controle.ocafezinho.com/wp-admin/admin.php?page=snippets → desativar o snippet "Cafezinho Noindex Pruning 358 URLs (recovery SEO 2026-06-27)" (1 clique).

- **Para adicionar mais URLs depois (T2/T3 do bucket):** editar o snippet no Code Snippets, adicionar IDs no array `$GLOBALS['cafezinho_noindex_ids']`, salvar e ativar.

- **Decisões editoriais tomadas:**
  - Bucket 0 (gate de nicho) ADIADO — volta gradual + V3 humanizado torna desnecessário agora
  - Sprint B (validação backlinks) PULADO — simplifica para noindex puro em todos os 358
  - Sprint concentrado em Claude Code (sem delegar Trindade nesta execução)
  - Chocolate Senado: MANTIDO indexado (Miguel: "é post normal")
  - Christof Koch consciência cósmica: noindex confirmado

- **Trindade Round 2 (consenso 7/7):** podar é necessário, matriz híbrida, proteger geopolítica core, faseado, Discover viral não volta, aceitar perda permanente do clickbait.

- **Credencial usada e descartada:** SSH `root@190.89.239.3:51439` (ServerDo.in) — senha foi salva temp em `/tmp/.sshcred` (modo 600) e DELETADA. Auth falhou (typo na senha ou senha trocada). Recomendado Miguel trocar senha por precaução.

- **Métricas-alvo de recuperação (3-6 meses):**
  - Search orgânico: de ~2.500/dia (atual deprimido) para ~4.000-4.500/dia (pré-queda foi 4.700)
  - Discover: 0 → 1.000-3.000/dia (não voltar pros 111k tóxicos)
  - Brand search (`o cafezinho`): permaneceu intacto em 26.818, prova que Google não queimou o domínio

[[reference-wp-servidor-real-cafezinho]] — WP em ServerDo.in (190.89.239.65), Tencent só tem agentes.

[[reference-bucket0-adiado-volta-quando-reescalar]] — Bucket 0 está pronto se Miguel decidir reescalar agentes futuramente.
