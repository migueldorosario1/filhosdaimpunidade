---
name: feedback-no-home-remover-se-tem-imagem-real
description: "Ao publicar/agendar post com featured_media presente, remover cat 20699 (No home) — Miguel quer ver tudo na home canônica"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d556bf3a-514a-43d5-a6d6-417905366fd5
---

Miguel 13/08/2026 ~13:15 BRT: *"textos com imagem real podem ir entrando no site sem o no-home, para a gente ver tudo"*.

## Regra

Ao publicar ou agendar um post no canônico `ocafezinho.com`:
- Se `_thumbnail_id > 0` (tem featured_media) → **remover cat 20699 (No home)** se presente.
- Se não tem featured_media → **manter cat 20699** (post não aparece na home até ganhar imagem).

## Aplicabilidade universal

Vale para TODOS os agentes:
- Worker V4 (autor 5786) — se worker publicou draft com cat 20699 + fm, tirar 20699 antes de publish.
- Repetidor estatal (autor 5470) — sempre tem imagem real de agência; se aparecer 20699 (raro), tirar.
- Lote Kimi K3 (Ago/13) — já aplicado 12:00 BRT.
- Novos posts das 5 verticais V4 (cats 79/43/582/1271/258) — mesmo padrão.

## Como aplicar

No fluxo do loop Vigília Trindade V6:
1. Ao processar um draft para agendamento (`post_status=future`), rodar `wp_get_post_categories($id)` + `get_post_meta($id, "_thumbnail_id")`.
2. Se `_thumbnail_id > 0` e `20699 in cats` → `wp_set_post_categories($id, array_diff($cats, [20699]))`.
3. Executar a mesma checagem ao corrigir publish do repetidor in-place.
4. Log JSONL registra `nohome_removed: true` quando aplicado.

Snippet PHP:
```php
$cats = wp_get_post_categories($id);
$fm = (int) get_post_meta($id, "_thumbnail_id", true);
if ($fm > 0 && in_array(20699, $cats)) {
  wp_set_post_categories($id, array_values(array_diff($cats, [20699])), false);
}
```

## Interpretação da "imagem real"

Miguel disse "imagem real" — em prática, uso `_thumbnail_id > 0` como proxy simples. Não distingo IA de foto real neste primeiro momento porque:
- Repetidor: sempre foto de agência (real por definição)
- Worker V4 (`v4-featured-*.jpg`): pipeline hoje passa por tribunal visual + preferência Flickr/Banco Ouro; IA é minoria
- Kimi K3 aplicou lote 13/08 todo com foto real Wikipedia/USNavy/NASA

Se aparecer post com featured_media claramente placeholder/IA problemática, mantenho cat 20699 e escalo Miguel. Mas critério padrão = tem thumb, tira No home.

## Verificação pós-publish

Após patch: `get_post_categories($id)` deve retornar sem 20699. Se ficou vazio (sem cats), NÃO deixar assim — o post precisa de pelo menos uma cat de vertical. Reverter e escalar Miguel.

## Retroativo (13/08 13:15 BRT)

Auditei os 19 posts que toquei nesta sessão (V4 ontem 22:26 + repetidor hoje + lote Kimi + 3 MD_LINK): **0 posts com cat 20699 + featured_media**. Nada a retro-corrigir.

Regras irmãs: [[feedback-vigilia-nunca-publicar-batch-agendar-madrugada]] · [[feedback-nunca-churn-publish-draft-seo]] · [[feedback-wp-update-post-edit-date-obrigatorio-para-agendamento]].
