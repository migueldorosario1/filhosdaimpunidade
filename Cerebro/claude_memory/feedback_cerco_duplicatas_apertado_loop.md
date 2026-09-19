---
name: feedback-cerco-duplicatas-apertado-loop
description: "No loop §90, detecção de duplicatas usa similaridade de título E corpo (Jaccard) em janela de ~40 posts — não só título exato. Duplicata confirmada → rebaixar o mais recente (ou o pior)"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d7137897-dcad-4847-af64-a409ee24938c
---

No loop §90, a partir de 2026-06-01 21:20 BRT (Miguel: "aperta o cerco contra duplicatas. rebaixa o mais recente, ou o pior."), a detecção de duplicatas deve ser ROBUSTA, não o grep de título exato nos últimos 10.

**Método por tick:**
- Janela ~40 posts publicados recentes (`per_page=40`, com `content`).
- Normalizar título e corpo (NFKD sem acento, lowercase, remover stopwords PT/EN).
- Calcular Jaccard de tokens de **título E corpo** entre todos os pares.
- **🔴 DUPLICATA FORTE:** titulo_jac ≥ 0.70 OU corpo_jac ≥ 0.70 OU título normalizado idêntico → **rebaixar** via WP API (`status: draft`).
- **🟡 Suspeita (0.55–0.70):** reportar, NÃO rebaixar automático — pode ser tema parecido legítimo (ex: 2 pesquisas eleitorais distintas, 2 ângulos da mesma notícia).

**Qual rebaixar:** default = **o mais recente** (preserva a cópia que já indexou/ganhou tração no Google). Exceção: se o mais antigo for nitidamente PIOR (menos completo, imagem ruim, categoria errada) → rebaixar o pior.

**Why:** Miguel quer cerco apertado. Rebaixar duplicata NÃO viola [[feedback_soltar_posts_nao_prender]] (o conteúdo segue publicado na outra cópia — não é reter algo que seria publicado). Mas o limiar alto (0.70) e a faixa de suspeita evitam rebaixar temas só parecidos. Casa com [[feedback_revisor_ler_tudo_rebaixar_so_se_muito_estranho]].

**How to apply:** Substituir o check de título-exato-10-posts pela detecção Jaccard-40-posts em cada tick. 2026-06-01 21:20: rodei a primeira vez, 0 duplicatas nos 40 recentes (anti-duplicata da coleta, Jaccard 0.60, está segurando).
