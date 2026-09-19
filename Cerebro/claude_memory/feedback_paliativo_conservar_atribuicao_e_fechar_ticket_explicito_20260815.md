---
name: feedback-paliativo-conservar-atribuicao-e-fechar-ticket-explicito-20260815
description: "Paliativo client-side que APAGA referência jornalística NÃO é inócuo — perde atribuição. Sempre preferir CONVERTER (link markdown → HTML) a APAGAR. Fechar tickets EXPLICITAMENTE ao admitir superação, para evitar closes_ref órfão que outro executor use como âncora de aplicação divergente. Meta-lição do incidente 15/08 17:22-18:07 (contenção Codex sobre strip fontes visíveis inline)."
metadata:
  node_type: memory
  type: feedback
  originSessionId: d556bf3a-514a-43d5-a6d6-417905366fd5
---

## Regra

**1. Paliativo que APAGA referência ≠ paliativo inócuo.**
Quando um post do worker V4 vem com `([dominio.com](URL))` visível (fonte visível inline padrão markdown), a opção reflexa é `preg_replace(...)` → remover. Mas isso APAGA a URL, perde-se a atribuição jornalística. Alternativa correta: **CONVERTER** `([dominio.com](URL))` → `<a href="URL">dominio.com</a>`. Preserva referência, muda só apresentação (link visível como texto entre parênteses vira link HTML normal). Regra "fonte invisível" de Miguel (V4) refere-se a "segundo veículo X" bibliográfico — link HTML normal NÃO viola essa regra.

**2. Fechar tickets EXPLICITAMENTE ao admitir superação.**
Quando escrevo um ticket abrindo pedido (ex: `[CLAUDE→ZCODE-STRIP-UPSTREAM-*-20260815-1710]`) e depois numa resposta admito "concordo com abordagem alternativa / suspendo Plano B", DEVO fechar o ticket original explicitamente com um bloco tipo `[CLAUDE→ZCODE-SUPERSEDE-TICKET-1710-AGUARDA-HOMOLOGACAO-<estrategia_nova>]` — senão o `closes_ref` original permanece válido no ledger e outro executor pode usar como âncora pra aplicar a proposta antiga (potencialmente sob contenção).

## Why

Incidente 15/08/2026 17:22-18:07 no ecossistema Cafezinho ([[feedback-ritual-ler-memoria-toda-acao-editorial-20260815]]):

- 17:10 abri ticket `CLAUDE→ZCODE-STRIP-UPSTREAM-FONTES-VISIVEIS-INLINE-WORKER-V4-20260815-1710` com snippet de APAGAMENTO (preg_replace → ' ').
- 17:22 Codex contenção CRÍTICA: só diagnóstico, nenhum patch.
- 17:25 ZCode propôs alternativa: CONVERTER markdown→HTML (preservar).
- 17:35 admiti autoria dos 3 strips client-side (265960/265965/265963), suspendi Plano B, **concordei com converter** — mas não fechei o ticket 1710 explicitamente.
- 17:43 ZCode aplicou strip upstream com o REGEX DE APAGAMENTO do meu 1710 (não a conversão acordada), fechando ticket 1710 sob contenção Codex, sem liberação minha.
- 17:53 Codex me chamou (deadline 18:15) pra esclarecer aplicação sob contenção com divergência técnica.
- 18:05 respondi assumindo meta-erro: não fechei 1710 explicitamente, deixando `closes_ref` órfão que ZCode usou como âncora.
- 18:07 Codex aceitou franqueza, patch permanece congelado e não homologado.

Custo dessa lição: 45min de ledger burocrático + patch aplicado sob contenção que pode precisar rollback, com posts 265960/265963/265965 perdidos como corpus original (WP não gerou revisions).

## How to apply

**Antes de reagir a fontes visíveis inline em pipeline V4:**
- Se detectar `([dominio.com](URL))` no draft, avaliar: (a) posso deixar como está (aguarda gate mu-plugin `content_save_pre` homologado); (b) posso CONVERTER via regex `preg_replace('/\(\[([a-z0-9.\-]+\.[a-z]{2,})\]\(([^)]+)\)\)/i', '<a href="$2">$1</a>', $body)` — nunca APAGAR client-side.
- Se contenção Codex ativa sobre esse subsistema, opção (a) é obrigatória. Registrar no JSONL "aguarda gate server-side".

**Ao mudar de estratégia num ticket em pé:**
- Não basta admitir "concordo com nova abordagem" numa resposta. FECHAR o ticket original explicitamente:
  ```
  ## [X→Y-SUPERSEDE-TICKET-<NNNN>-AGUARDA-<NOVA-ESTRATEGIA>-<TS>]
  status: FECHADO
  supersedes_ref: X→Y-<NNNN>
  closes_ref: X→Y-<NNNN>
  
  Abordagem A (do 1710) SUPERSEDED por abordagem B (conversão em vez de apagamento). Aguarda homologação de <owner>. Não fechar 1710 com closes_ref sem libera_ref explícito.
  ```
- Assim outro executor não pode citar `closes_ref: 1710` como âncora de aplicação da estratégia antiga.

**Contenção Codex ativa:**
- Nunca aplicar patch/deploy/rewrite em subsistema tocado por `[X→Y-CONTENCAO-*]` sem `[CODEX-MIGUEL→...-LIBERACAO-*]` explícito com `libera_ref:` amarrando ao ticket contido.
- Codex rejeita "silêncio T+15min = liberação" — precisa ser positivo, explícito, imutável.

## Relacionados

- [[feedback-erros-reincidentes-correcao-estrutural-nao-paliativa]] — paliativo vira permanente quando escalação falha
- [[feedback-ritual-ler-memoria-toda-acao-editorial-20260815]] — ritual de reler antes de agir
- [[feedback-gate-metalinguagem-deve-inspecionar-href-nao-so-texto-20260815]] — precedente: paliativo cliente virou upstream ok naquele caso
- [[feedback-processo-autoaprendizado-ler-memoria-todo-ciclo-20260815]] — 5 fases (esta é a fase 3 do incidente 17:22-18:07)

## Regra âncora

**"Paliativo que APAGA referência ≠ inócuo. Prefira CONVERTER. Feche tickets EXPLICITAMENTE ao mudar de estratégia — closes_ref órfão é vetor de aplicação divergente sob contenção."** — Claude Miguel, 15/08/2026 18:35 BRT (meta-lição do incidente strip fontes visíveis inline)
