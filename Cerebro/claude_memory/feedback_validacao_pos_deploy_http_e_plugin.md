---
name: Validação pós-deploy DEVE incluir HTTP status + identificar plugin antes de hookear
description: Lição do incidente AMP for WP 500 (2026-05-04) — duas regras inegociáveis pra deploy em ambiente WP/CMS terceiro
type: feedback
originSessionId: 9002c7ec-10c3-4489-8dad-6a7a4128f954
---
# Regras pós-incidente HTTP 500 AMP for WP (2026-05-04 19:26 BRT)

## Regra 1 — Validação pós-deploy SEMPRE inclui HTTP status

**Why:** No incidente AG de 04/05, validei só presença de marcador (`grep cz-continue-lendo` no body) e contei "0 ocorrências = bloco não renderizou". Mas o servidor estava retornando HTTP 500 em todos os AMP — fatal PHP no runtime. Codex pegou de fora com `curl -I` em <2min porque incluiu HTTP status na validação. Eu não.

**How to apply:** Toda validação pós-deploy de snippet/filter/hook em ambiente WP/CMS deve **começar** por `curl -I <url>` em ≥3 URLs típicas (homepage + 2 posts ou 1 post + 1 AMP) e confirmar 200/301/302. **Só depois** verificar presença/ausência do marcador. Falha silenciosa de marcador é diferente de HTTP 500 — segundo é incidente §11 instantâneo.

Rotina mínima:
```bash
for url in "${urls[@]}"; do
  status=$(curl -sI "$url" | head -1 | awk '{print $2}')
  echo "$url: $status"
done
```

## Regra 2 — Identificar plugin/versão ANTES de hookear

**Why:** Propus snippet AG usando `the_content` (hook WP genérico) sem confirmar qual plugin AMP estava em uso. Era "AMP for WP 1.1.13" (Kaludi), não o AMP oficial — plugin tem sanitizer próprio que descarta filter genérico e gera fatal com `ampforwp_modify_the_content` em combinação errada. Resultado: HTTP 500 em todo o AMP.

**How to apply:** Antes de propor qualquer snippet/filter/action pra plugin terceiro:
1. **Identificar plugin** via `curl -sL <url> | grep -oE '<meta[^>]+generator[^>]*>'` ou inspecionar `wp-admin > Plugins` (Miguel).
2. **Identificar versão** — APIs mudam entre majors.
3. **Usar hook canônico do plugin específico**, não hook genérico. Buscar docs/source do plugin se possível.
4. **Estratégia incremental:** primeiro deploy = marcador HTML mínimo (1 `<div data-ag-test="1">`) pra confirmar hook funciona. Só depois subir lógica completa.

Não assumir que hook X funciona "porque é WordPress padrão" — plugins de output (AMP, AMP for WP, custom themes) frequentemente substituem o pipeline de renderização.

## Aplicação a outros casos

Vale também pra:
- Deploys em qualquer plugin de cache (WP Rocket, W3TC) — usam hooks próprios
- Deploys em themes premium customizados — `the_content` pode estar substituído
- Deploys em multisite — `is_singular()` pode comportar diferente

## Origem

Incidente AG de 2026-05-04 19:08-19:26 BRT. Detalhes em `bug_critico_amp_for_wp_500_20260504.md`. §11 (deployada 17:51 BRT mesmo dia) salvou audiência noturna em <10min.

## §12 derivada (Miguel, 2026-05-04 19:30 BRT)

> "Erramos hoje em deixar Claude agir sozinho. Não podemos fazer nada arriscado sem consenso entre os 3 agentes e análise de risco."

§12 deployada no `CEREBRO_NODE_GOVERNANCA.md`: **consenso de hipótese ≠ consenso de código**. Toda mudança arriscada exige (1) revisão linha-a-linha por ≥1 dos outros 2 agentes, (2) análise de risco explícita pré-deploy (blast radius + sintomas + plugins terceiros), (3) smoke test quando viável.
