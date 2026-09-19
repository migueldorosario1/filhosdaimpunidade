---
name: Incidente HTTP 500 AMP for WP — deploy AG sem identificar plugin
description: 2026-05-04 19:08-19:26 BRT — snippets WPCode com hooks AMP genéricos quebraram TODOS os AMP do Cafezinho com HTTP 500; rollback §11 salvou em <10min
type: project
originSessionId: 9002c7ec-10c3-4489-8dad-6a7a4128f954
---
# 🚨 Incidente AG — HTTP 500 em todos os AMP (2026-05-04)

## Linha do tempo (18 minutos)

- **19:08 BRT** — Miguel cola Snippet 1 v1.0 + Snippet 2 CSS no WPCode Lite. Hook usado: `the_content` filter + `is_amp_endpoint()`. Bloco não renderiza.
- **19:13 BRT** — Cola Snippet 1 v1.1 (compat `amp_is_request()`/`is_amp_endpoint()`). Não renderiza.
- **19:18 BRT** — Cola Snippet 1 v2.0 com `ampforwp_modify_the_content`. Claude testa: 0 ocorrências. Abre SOS no canal/fórum.
- **19:20 BRT** — **Codex testa de fora e detecta HTTP 500 em 2 AMPs** (Russia/Ucrânia tréguas + Galileia 4mil anos). Pede rollback imediato §11.
- **19:25 BRT** — Antigravity confirma: Miguel desativou os 2 snippets no WPCode. Crise contida.
- **19:26 BRT** — Claude valida com `curl -I`: AMPs voltaram pra 200 em 5 posts testados. §11 funcionou na primeira aplicação real (deployada 17:51, ~1h30 antes).

## Causa raiz

Plugin AMP do Cafezinho é **"AMP for WP" 1.1.13** (plugin Kaludi), não o AMP oficial do WordPress.org. Snippets usaram hooks genéricos/AMP-oficial:
- `the_content` filter — descartado pelo sanitizer Kaludi
- `ampforwp_modify_the_content` — gera fatal error em combinação com `wp_get_post_categories()` + `get_post()` em loop dentro do contexto AMP do plugin
- `amp_post_template_css` — funciona em AMP oficial, não em AMP for WP

Resultado: fatal PHP em runtime AMP → **HTTP 500 em TODOS os AMP** do portal. Discover deixaria de mostrar matérias se não tivesse rollback rápido.

## Por que não detectei eu mesmo o 500

Meu teste de validação pós-deploy verificou só presença do marcador (`grep cz-continue-lendo`). Como a string não estava no HTML retornado, contei como "bloco não renderizou". **Não conferi HTTP status**. Codex testou `curl -I` e pegou 500 imediatamente — prática que faltou na minha rotina.

## Hook correto identificado por Codex+Antigravity

Pra AMP for WP plugin Kaludi:
- **Conteúdo:** `add_action('ampforwp_after_post_content', $callback)` — action, não filter
- **CSS:** `amp_post_template_css` filter (compat mantida)
- **Estratégia de deploy:** primeiro um marcador HTML mínimo (1 div) pra confirmar hook funciona; só depois subir o bloco completo

## Hipótese AG status

- **Suspensa hoje 04/05** (Antigravity recomendou cabeça fria)
- v3.0 engatilhada pra amanhã cedo com hook correto
- Pacote ainda na Rodada 23+24 do `forum_elevar_audiencia_20260504.md`

## Validação pós-rollback (§11 cumprida)

```
Post 242866: AMP=200
Post 242851: AMP=200
Post 239946 (Galileia top1): AMP=200
Post 242862: AMP=200
Post 242859: AMP=200
```

Audiência GA4 do dia preservada: 9.241 pv (máxima do dia).

## Atores e contribuição

| Quem | Quando | O que fez |
|---|---|---|
| Miguel | 19:08-19:25 | Colou 3 versões; ratificou §11; executou rollback |
| Claude | 19:08-19:26 | Propôs snippets (com hooks errados); abriu SOS; validou pós-rollback |
| Codex | 19:20 | Detectou HTTP 500 de fora em <2min; ditou rollback; sugeriu hook correto |
| Antigravity | 19:25 | Identificou cache + hook canônico + ratificou rollback |

Sistema multi-agente funcionou — sem Codex testando de fora, eu não teria detectado o 500.
