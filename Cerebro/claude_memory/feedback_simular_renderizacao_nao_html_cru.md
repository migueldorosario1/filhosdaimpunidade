---
name: simular-renderizacao-nao-html-cru
description: "Ao auditar conteúdo WP/checkup, simular a renderização (o que o leitor vê) — ler HTML cru gera falso positivo (ex: <script> de newsletter é invisível)"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d7137897-dcad-4847-af64-a409ee24938c
---

Ao auditar posts (checkup de qualidade), **simular a renderização real** antes de classificar um achado: remover `<script>...</script>`, depois stripar todas as tags → avaliar o TEXTO VISÍVEL ao leitor. NÃO classificar defeito a partir do HTML/JSON cru.

**Why:** No checkup Lote 2 (02/06/2026), Kimi E Qwen, em auditoria cega independente, alegaram "13 posts com script Mailchimp vazado no corpo" como achado que o Claude teria perdido — celebrado como validação da tripla cega. Era **falso positivo compartilhado**: o `<script>` está em tag real → executa e é INVISÍVEL ao leitor (widget legítimo de newsletter `cafezinho-mc-form-ajax`). A leitura original do Claude ("contido nas tags") estava certa. Os dois erraram por ler o HTML cru sem renderizar. Detectado ao aplicar simulação de render no Lote 3. Miguel mandou "corrigir tudo agora" (cérebro + relatório + avisar Kimi/Qwen).

**How to apply:** Vale para QUALQUER auditoria de conteúdo publicado. Distinguir: (a) `<script>`/`<p>` em tag real = invisível, geralmente legítimo; (b) `&lt;script&gt;`/`&lt;p&gt;` escapado = VISÍVEL como texto = defeito real (família #254854); (c) template/legenda/crédito ("Ilustração editorial sobre {título}", "Cafezinho / Wan 2.6") que sobrevive ao strip de tags = vazamento visível = defeito. Reforça [[feedback_verificar_conteudo_real_wp_ao_flagrar]] e a regra de ouro: determinística ≠ ler o post, e ler HTML cru ≠ renderizar.
