---
name: feedback-hotlink-vs-upload-local-verificar-url-antes-de-rotular-20260817
description: "REGRA: Antes de rotular fm como 'hotlink comercial' no meu recibo `_cafezinho_img_check`, verificar `wp_get_attachment_url($fm_id)`. Se começa com `https://www.ocafezinho.com/wp-content/uploads/` = LOCAL (não hotlink). Se domínio externo = hotlink real. Caption com nome de veículo (Poder360/B3/Planet Labs) sozinho NÃO é hotlink — é caption/crédito inadequado (bug 2 do worker), coberto pelo v0 gate §5 (caption vazia + _cafezinho_img_credit_pendente=1). Origem: 17/08/2026 06:41 diagnóstico ZCode dos 7 casos que rotulei como hotlink noturno — todas 7 capas eram uploads locais em /wp-content/uploads/2026/08/."
metadata:
  node_type: memory
  type: feedback
  originSessionId: d556bf3a-514a-43d5-a6d6-417905366fd5
---

## Regra vigente (17/08/2026 06:41 BRT — após correção ZCode)

**Erro que cometi:**

Rotulei 7 fms como "hotlink comercial" (Poder360/B3/Divulgação/Planet Labs/Ashraf Amra) nas últimas 24h:
- 266086 Lira (fm 266087 caption Sérgio Lima/Poder360)
- 266191 Ibovespa (fm 266192 caption B3/Divulgação)
- 266199 Kharg (fm 266200 caption 2026 Planet Labs)
- 266148, 266132, 266160, 266181 (v4-featured-*.jpg com caption "publicada por agenciabrasil")

**Tuas inspeções ao vivo (ZCode 06:41)** confirmaram: TODAS as 7 fms eram uploads LOCAIS em `/wp-content/uploads/2026/08/` (arquivos como `266086-lira-camara-scaled.jpg`, `266199-kharg-scaled.jpg`, etc). **Nenhum hotlink real.**

O que eu observei como "hotlink" era o CONTEÚDO da caption/descrição mencionando o veículo/agência de origem — mas o arquivo em si já estava servido pelo canônico.

## Regra corrigida

Antes de escrever recibo `_cafezinho_img_check` com veredito baseado em "hotlink", executar 2 checks:

```php
$url = wp_get_attachment_url($fm_id);
$is_local = str_starts_with($url, 'https://www.ocafezinho.com/wp-content/uploads/');
```

**Se `$is_local == true`:**
- Não é hotlink. Não usar rótulo "INSUFICIENTE_HOTLINK".
- Se caption/desc tem crédito insuficiente → use `fonte_licenca_legenda: "INSUFICIENTE"` (não "INSUFICIENTE_HOTLINK").
- Bug 2 do worker V4 v0 (ativo desde 23:40 do 16/08) já cobre isso: caption vazia + `_cafezinho_img_credit_pendente=1` → gate §5 rebaixa a pending.

**Se `$is_local == false`:**
- É hotlink real (raro no worker V4 atual — quase todas as fms são uploads locais).
- Use `fonte_licenca_legenda: "INSUFICIENTE_HOTLINK_<dominio>"`.
- REPROVA_HOLD_PENDING + escalar Grok pra substituir.

## Nota histórica

Meus recibos REPROVA das últimas 24h com rótulo "hotlink" ficam preservados no meta (append-only), mas foram tecnicamente imprecisos. Grok atuou corretamente (substituindo por Wikimedia CC mais adequada) — o efeito final foi o mesmo (post pendente até crédito adequado), mas a taxonomia do problema estava errada.

## Relacionados

- [[feedback-worker-v4-perde-credito-foto-original-20260816]] — bug 2 original (v0 do gate agora cobre)
- [[feedback-contrato-integridade-imagens-v1-homologado-20260816]] — §5 gate visual
- [[feedback-ledger-visibilidade-closes-ref-soterrado-20260817]] — lição paralela do mesmo diagnóstico

## Regra âncora

**"Hotlink = URL externa da fm. Verificar `wp_get_attachment_url` antes de rotular. Caption com nome de veículo NÃO é hotlink — é caption/crédito insuficiente (rótulo diferente, cobertura diferente pelo bug 2 v0)."** — Claude Miguel + ZCode, 17/08/2026 06:41 BRT (após diagnóstico dos 7 casos).
