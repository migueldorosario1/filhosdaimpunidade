---
name: feedback-duplicatas-rebaixar-direto-sem-pedir
description: Duplicatas temáticas detectadas no loop §53 (Jaccard ≥0.55 no título OU ≥0.50 no corpo) — rebaixar a mais recente DIRETO sem pedir aval. Doravante.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7a7a5b2d-a19d-40f4-a761-7c1f51789844
---

🔻 **Duplicatas temáticas = rebaixar a mais recente DIRETO via WP API, sem pedir aval.**

**Why:** Miguel autorizou em 03/06 ~23:00 BRT após eu reportar #256000 vs #256033 (mesma decisão STF, fontes diferentes, Jaccard título 0.667): *"quando for assim, rebaixa logo, sem pedir minha autorização. e inicia novo forum para a gente combater duplicata na raiz, antes de publicar"*. Estende [[feedback_cerco_duplicatas_apertado_loop]] que originalmente exigia confirmação.

**How to apply:**
- Limiar de rebaixamento direto: Jaccard título ≥0.55 OU corpo ≥0.55 (ainda inferior ao limiar 0.70 "rebaixar o pior") quando o tema é claramente o mesmo evento factual.
- Default: rebaixar **a mais recente** (preservar o primeiro publicado).
- Exceção: se a mais antiga tiver claramente menos qualidade (sem fonte, com bug, corpo curto), rebaixar a antiga.
- Registrar de/para em `Foruns/registro_erros_qualidade_redacao.md`.

**NÃO vale para:**
- Sangria temática em cluster amplo (Pix/USTR com 6 ângulos distintos) — esses são cobertura ampliada, não duplicata.
- Posts já com `status=draft` — não tem o que rebaixar.

Relacionado: [[feedback_cerco_duplicatas_apertado_loop]] · [[feedback_revisor_ler_tudo_rebaixar_so_se_muito_estranho]] · [[feedback_capitalizacao_corrigir_direto_sem_pedir]]
