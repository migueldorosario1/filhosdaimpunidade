---
name: feedback-contrato-integridade-imagens-v1-homologado-20260816
description: "§5 do Contrato Geral do Ecossistema — Contrato de Integridade de Imagens v1 — HOMOLOGADO por Miguel 20:41 do 16/08/2026. Regra vigente: todo wp_update_post future/publish exige _cafezinho_img_check com 'ok': true. Sem isso, gate mu-plugin (ZCode/Qwen 3.8 + Miguel) rebaixa a pending. Formato completo do recibo abaixo. Nasceu do incidente 266029 (imagem 3D SEM Lula rotulada como Lula)."
metadata:
  node_type: memory
  type: feedback
  originSessionId: d556bf3a-514a-43d5-a6d6-417905366fd5
---

## Regra vigente (a partir de 16/08/2026 20:41 BRT)

Nenhum post do Cafezinho vai a `publish` ou `future→publish` sem `_cafezinho_img_check` gravada com **`"ok": true`** (único campo que o mu-plugin `cafezinho-gate-imagem-checada.php` do ZCode/Qwen 3.8 + Miguel valida). Alternativa granular: `_cafezinho_img_isenta` via checkbox no editor (isenção humana deliberada, auditável).

Gate FAIL-CLOSE em duas camadas:
- **REST API** (`rest_pre_insert_post`): rejeita com HTTP 400
- **transition_post_status**: reverte para `pending` fora do REST (pega future→publish do wp-cron)

## Formato canônico do recibo `_cafezinho_img_check` (v1)

JSON string OU array. O gate valida apenas `ok` truthy. Restante é auditoria:

```json
{
  "ok": true,
  "ts": "<mysql BRT>",
  "revisor": "Claude Miguel Vigilia V6" | "Loop Laura Vigilia V6 (fail-over)" | "Grok imagem X" | "editor_humano",
  "attachment_url": "<url pública>",
  "attachment_id": <fm_id int>,
  "hash_sha256_16": "<hash arquivo>",
  "vision_disponivel": true | false,
  "vereditos": {
    "pessoa": "OK|BATE_PARCIAL|NAO_BATE|NAO_APLICA",
    "lugar": "OK|BATE_PARCIAL|NAO_BATE|NAO_APLICA",
    "evento": "OK|BATE_PARCIAL|NAO_BATE|NAO_APLICA",
    "epoca": "OK|BATE_PARCIAL|NAO_BATE|NAO_APLICA",
    "assunto": "OK|BATE_PARCIAL|NAO_BATE|NAO_APLICA"
  },
  "fonte_licenca_legenda": "OK|INSUFICIENTE",
  "segunda_vista": "nao_solicitada|solicitada_Grok:<id>|solicitada_Codex:<id>|solicitada_Laura:<id>|consolidada",
  "veredito_final": "APROVA|APROVA_CONTEXTUAL|REPROVA_HOLD_PENDING|REPROVA_ESCALA_HUMANO",
  "nota": "<texto livre>"
}
```

**IMPORTANTE:** `ok` é o único campo que o gate valida. Se esquecer `ok`, gate rebaixa apesar de todo o resto estar preenchido. Prova histórica: 266035 e 266036 do 16/08 quase caíram na madrugada 17/08 04:30/05:00 por essa falta — ZCode/Qwen patcheou às 19:47 adicionando `ok: true` e preservando meus campos originais.

## Meu procedimento operacional (Loop Miguel Vigília V6)

Antes de todo `wp_update_post(status=future|publish)` num draft do worker V4:

1. `wp_get_attachment_url($fm_id)` — obter URL do attachment
2. `curl -o /tmp/gate_visual/fm<id>_<slug>.jpg` — baixar imagem
3. Vision via Read tool — inspecionar visualmente
4. Comparar 5 dimensões com título+lide (pessoa/lugar/evento/época/assunto)
5. Verificar fonte/licença/legenda/ilustrativo em `wp_get_attachment_metadata($fm_id)` + `get_post($fm_id)->post_excerpt`
6. Escrever `_cafezinho_img_check` com JSON completo + **`"ok": true`** no primeiro campo
7. Só aí `wp_update_post`
8. Validar via `$wpdb->get_row` direto (Redis cache pode servir versão antiga em `get_post()` no eval-file — aprendido no ciclo 17:32 do 16/08)

## Vereditos possíveis

- **APROVA**: 5/5 OK, imagem retrata protagonista, contexto certo
- **APROVA_CONTEXTUAL**: imagem ilustrativa declarada (caption ou legenda avisa), sem risco de engano tipo 266029, fonte/licença OK
- **REPROVA_HOLD_PENDING**: pessoa protagonista ausente da foto sem justificativa contextual, ou Vision indisponível
- **REPROVA_ESCALA_HUMANO**: sinais de manipulação, fraude, imagem gerada por IA rotulada como real, licença ausente/duvidosa

## Casos limite tratados

- Sem FM (`_thumbnail_id=0`): deixa `pending`, ponte imagens ZCode/Grok aplica FM depois — não escrever recibo até FM chegar
- FM alterada pós-recibo: **v1 é regra operacional** (o gate NÃO compara hash automaticamente). Em v2 (a definir): gate compara `_thumbnail_id`/hash do recibo com FM vigente
- Vision indisponível/timeout: `vision_disponivel: false` + `veredito_final: REPROVA_HOLD_PENDING` + escalar Grok/Codex
- Post republicado por Miguel humano: pode usar `_cafezinho_img_isenta` (checkbox); meu recibo prévio sobrevive se `attachment_id` não mudou

## Segunda vista (opcional)

Se meu Vision não bater com clareza (BATE_PARCIAL em 2+ dimensões, sinais de manipulação, dúvida factual), abrir bloco no ledger: `[CLAUDE→GROK-OU-CODEX-SEGUNDA-VISTA-VISUAL-<postID>-<TS>]` com URL do attachment + dúvidas específicas. Se ninguém responder em 30-60min, escalar Miguel.

**Loop Laura NÃO é obrigatório como segunda vista** — ele é redundância opcional em treinamento (regra Miguel 19:15). Laura pode alertar mas não bloqueia meu fluxo.

## Rollback e emergência

- Miguel pode desabilitar o mu-plugin via `rm` do arquivo (instruções no cabeçalho do próprio plugin)
- Alternativa granular: `_cafezinho_img_isenta` via checkbox no editor wp-admin (isenção humana deliberada, auditável)

## Métricas para revisão v2 (23/08/2026)

- Taxa de recibo emitido / posts com FM > 95%
- Taxa de REPROVA / recibos < 5%
- Taxa de mudança de FM pós-recibo (invalidação operacional) < 2%
- Taxa de segunda vista externa acionada < 15%
- Auditoria: Codex sobre amostra semanal + meu próprio dashboard + Laura shadow

## Origem histórica

- **Incidente 266029** (16/08 manhã): fm=266030 era "arte 3D SEM Lula" rotulada como "presidente Lula em evento oficial". Meu ciclo 05:02 agendou sem inspecionar imagem — só olhei metadata do `_thumbnail_id`. ZCode/Qwen substituiu por fm=266127 (foto real Lula Vila Euclides).
- **ORDEM MIGUEL 18:05** (`ORDEM-MIGUEL-GATE-VISUAL-FAIL-CLOSE-20260816-180538`): exigiu gate visual fail-close antes de agendar/publicar.
- **Meu bloco 18:32** (`CLAUDE-MIGUEL-ADERE-GATE-VISUAL-FAIL-CLOSE-CHECKLIST-VIGILIA-20260816-1832`): adesão + proposta de checklist operacional.
- **Mu-plugin ZCode/Qwen 3.8 + Miguel** (16/08): `cafezinho-gate-imagem-checada.php` — implementação servidor.
- **Meu Contrato de Integridade de Imagens v1** (16/08 20:10): 9 cláusulas propostas ao ZCode via `CLAUDE-MIGUEL-ADENDO-ZCODE-CONTRATO-INTEGRIDADE-IMAGENS-V1-20260816-2010`.
- **Incorporação ao §5 do Contrato Geral** (16/08 20:31): ZCode/Qwen incorporou com `ok: true` obrigatório documentado.
- **Homologação Miguel** (16/08 20:41): "sim, eu homologo o 5" no chat direto.

## Relacionados

- [[feedback-ritual-ler-memoria-toda-acao-editorial-20260815]] — meta-regra aplicável
- [[feedback-processo-autoaprendizado-ler-memoria-todo-ciclo-20260815]] — 5 fases (esta é fase 3 do incidente 266029)
- [[feedback-cache-redis-valida-via-wpdb-direto]] — regra complementar (validar wp_update_post via $wpdb, não get_post)
- Contrato Geral do Ecossistema §5: `Cerebro/CONTRATO_GERAL_ECOSISTEMA.md`

## Regra âncora

**"Nenhum publish do Cafezinho sem `_cafezinho_img_check` com `ok: true`. Ver a imagem com os próprios olhos + comparar 5 eixos (pessoa/lugar/evento/época/assunto) + registrar recibo. Metadata sozinha nunca aprova."** — Miguel, 16/08/2026 20:41 BRT (homologando §5 do Contrato Geral)
