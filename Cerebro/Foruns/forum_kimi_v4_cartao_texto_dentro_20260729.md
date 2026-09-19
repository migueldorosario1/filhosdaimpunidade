# Fórum — Cartões V4 com texto dentro: regressão do bug #26 e cura em duas frentes (2026-07-29)

**Agente:** Kimi K3 (ZCode) · **Gatilho:** reclamação direta do Miguel nesta sessão
**Autorização:** pedido explícito do Miguel ("Não dá pra você...?") — escopo: código do worker; sem tocar em posts publicados (oferta separada aguardando OK).

## §1 Sintoma
Cartões gerados (fal.ai/Flux Pro) continuam saindo com texto renderizado dentro — feio e geralmente truncado/errado. Miguel já havia proibido em 24/07 (bug #26: "não pode ter jamais texto dentro da imagem porque em geral trunca").

## §2 Evidência (29/07, após o fix #26)
| Post | Hora | Texto vazado no cartão |
|---|---|---|
| 263415 (Irã/Ormuz) | 10:01 | "IRAIN" no casco do petroleiro (grafia errada) |
| 263409 (Apib/STF) | 09:21 | pergaminho "SUSPREME JUSTICE AND TRUTH" (grafia errada) |

## §3 Por que ainda acontecia (3 causas)
1. **Regra tóxica no tribunal:** `audit_generated_cartoon()` instruía o juiz visual a PERMITIR texto em flux-pro/fal.ai ("expressamente permitidas... jamais bloqueie pela mera presença de texto") — anulava o fix #26, que só mexeu no prompt do gerador.
2. **Prompt não garante:** "ABSOLUTELY NO TEXT" é probabilístico; estilo "charge de jornal vintage" puxa texto da distribuição de treino. Sem verificação pós-geração, texto vaza.
3. **Juiz fora do ar + fail-open:** `KIMI_VISION_API_KEY` expirada (401) e exceção na auditoria aprova a imagem — nada era inspecionado.

## §4 Cura deployada (NYC `/root/v4_vertical_draft_worker.py`)
- **Fix 1 — REGRA DE TEXTO inquebrável:** qualquer letra/palavra/número/legenda/placa/balão/cartaz/pergaminho com escrita/nome em casco/assinatura/logo/marca d'água = `hard_block=true` SEMPRE, qualquer gerador, mesmo texto correto/bonito; na dúvida, é texto. Título e legenda vivem no HTML.
- **Fix 2 — juiz em cadeia:** `_visual_judge()` = Kimi → `_qwen_visual()` (qwen-vl-plus via rota MaaS V3, chaves `.env.unificado`, 200 OK do NYC). 2 call sites migrados.
- **Fail-closed:** com hard_block, o retry loop (4x) regenera com feedback anti-texto; esgotado, o draft fica SEM imagem — nunca mais publica cartão com texto.

## §5 Validação ao vivo
- Cartão SUSPREME → `approved=False`, `bloqueio_grave: imagem contém texto visível` ✅
- Cartão limpo (pomba/mesa rachada) → `approved=True` ✅
- Fallback Kimi(401)→Qwen-VL acionado e logado ✅

## §6 Backups / hashes
- Antes: `2a52c600…5687b` → fix1 `243d4a3b…3906` → fix2 `4a683f44…0f659`
- Backups NYC: `.bak_kimi_notext_audit_20260729_151012`, `.bak_kimi_judge_fallback_20260729_*`; espelho local sincronizado (`.bak_kimi_notext_judge_20260729`)

## §7 Pendências
- **Miguel:** renovar `KIMI_VISION_API_KEY` (BUG-20260729-KIMI-VISION-KEY-401, mitigado).
- **Oferecido:** regenerar in-place os cartões dos posts 263415 e 263409 (preservando status=publish, precedente #26 downstream) — aguardando OK.
- **Sugerido (futuro):** mesmo gate de texto no `gerador_imagem_editorial.py` legado (enxame) — hoje ele só tem a proteção de prompt; sem juiz pós-geração.
