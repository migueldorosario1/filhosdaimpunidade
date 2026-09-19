---
name: feedback-trava-anti-repeticao-94
description: "§94 Trava Anti-Repetição WP — snippet PHP via WPCode rebaixa pra draft posts com slug duplicado em 30min. Universal, pega qualquer agente."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ad62e53a-7337-4799-84ba-ed7ccefc1122
---

🚧 **Trava §94 Anti-Repetição** ativa no Cafezinho via snippet PHP no WPCode desde 2026-06-07 ~01:25 BRT (Miguel autorizou).

**Why:** Em 2026-06-07 ~01:03-01:07 BRT, agente não-identificado publicou 4 posts duplicados sobre Modernização do Metrô SP no Cafezinho (#256720 mantido + #256721/722/723 apagados via DELETE WP REST). Investigação inicial não localizou o culpado nos logs (maestro.log estava parado 21:48-03:00, nenhum log com timestamp 01:03-01:07 BRT exceto agente_instagram que não cria post editorial). Em vez de continuar caçando o agente fantasma, Miguel autorizou trava universal no nível WP.

**How to apply:**
- Snippet PHP roda no hook `transition_post_status` quando post vira `publish` (não dispara em updates de publish→publish)
- Remove sufixos `-2`, `-3` do slug antes de comparar (`preg_replace('/-\d+$/', '', $slug)`)
- Busca posts publish nos últimos 30min com slug-base igual ou começando com `<slug>-`
- Se achar pelo menos 1 duplicata → rebaixa o NOVO pra draft via `$wpdb->update` (evita recursão do hook)
- Motivo salvo em `post_meta._trava_anti_repeticao_motivo` + lista de duplicados em `_trava_anti_repeticao_originais` (JSON)
- Logado em PHP-FPM error log
- Slug muito curto (<8 chars) NÃO dispara — evita falso positivo
- **Reversível:** desativar snippet no WPCode (1 clique)

Localizado no WP: WPCode plugin → snippet "Trava §94 Anti-Repetição (Cafezinho)" → ativo.

**Quando flagrar falso positivo:**
- Aumentar threshold de 30min se um publish legítimo for marcado
- Ajustar tamanho mínimo do slug se necessário
- Mostrar `_trava_anti_repeticao_motivo` do post afetado pro Miguel decidir

Relacionado: [[feedback_cerco_duplicatas_apertado_loop]] (cerco no tick §53, lexical/Jaccard, complementar à trava §94 universal), §93 (Google Indexing API — trava §94 evita pingar duplicatas inúteis ao Google e desperdiçar quota).
