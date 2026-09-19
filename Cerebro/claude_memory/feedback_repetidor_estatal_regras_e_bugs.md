---
name: feedback-repetidor-estatal-regras-e-bugs
description: "Regras específicas do agente_repetidor_estatal (author 5470, cron 7 */2) — mantém fonte visível/bibliografia, mas tem bug estrutural de duplicação de lead + títulos frequentemente >80 chars"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d556bf3a-514a-43d5-a6d6-417905366fd5
---

`agente_repetidor_estatal.py` é agente do Codex/ZCode no NYC (cron `7 */2 * * *`, author 5470 = "Redação"). Republica matérias de agências oficiais (Agência Brasil, Agência Senado, Agência Gov, Agência Câmara) direto como `publish` — nunca gera draft. Volume típico: ~12 posts/dia.

## Exceção editorial única — mantém fonte visível

**Miguel 13/08/2026 ~09:40 BRT:** *"repetidor estatal tem direito de link visível da fonte. é o único que tem isso."*

- **PODE citar veículo pelo nome**: "segundo a Agência Brasil / Agência Senado / Agência Gov / Agência Câmara" ✅
- **PODE ter bloco "Fonte: <link>" no final** ✅
- **PODE ter links visíveis pra fonte oficial** ✅

Isso NÃO se aplica a nenhum outro agente: worker V4 (5786) segue regra tese+atribuição visível; 5 novas verticais V4 (cats 79/43/582/1271/258) seguem [[feedback-espelho-fontes-invisiveis-regra-editorial]] com fonte INVISÍVEL.

**Como distinguir na auditoria**: `get_post_meta($id, "_agente_origem")` — se `repetidor_estatal`, aplicar exceção; se qualquer outro (v4_*, ausente com autor 5786, etc), aplicar regras normais.

## Bug estrutural conhecido — duplicação de lead

**100% dos 6 posts publicados 13/08 madrugada (265450/265452/265459/265462/265467/265475) tinham o 1º e o 2º parágrafo com o mesmo conteúdo em variação** — o agente gera um "resumo síntese" pré-formatado + o "1º parágrafo original da matéria" e enfileira os dois. Quando são parecidos, leitor vê o mesmo conteúdo repetido.

Correção que aplico ao auditar: manter só o **resumo síntese enriquecido** (que costuma ser mais denso), apagar o 2º parágrafo. Preservar `<em>` e links do resumo.

**Escalação pendente**: cartinha `inbox_trindade/zcode.md` tag `[CLAUDE-BUG-REPETIDOR-ESTATAL-DEDUP-LEAD-20260813]` reportando pra fix upstream no `agente_repetidor_estatal.py`.

## Outros bugs recorrentes observados 13/08

- **Título >80 chars**: 4/6 posts. Aplico regra auditor [[feedback-auditor-titulos-v4-7-regras-canonico]] retro-corrigindo.
- **Bugs factuais** (baixa taxa mas graves): "Teodoro Santos" (sobrenome faltando — real: **Teodoro Silva Santos**, ministro STJ), número de mortos Crimes de Maio "545" (real: **564** — Relatório CNDH). Aplicar WebSearch em nomes próprios e números-chave antes de aceitar.
- **Título com erro semântico** (raro): 265450 "distribuidora" quando o post trata de "fornecedor" — trocar palavra semanticamente correta.
- **Parágrafos duplicados no meio do corpo**: só o lead teve o problema hoje; se voltar a acontecer em outros pontos, adicionar detector heurístico.

## Como aplico no loop Vigília Trindade V6

Slot A (a cada hora XX:00): varredura dos publish do repetidor nas últimas 2h.
- Se `_agente_origem == "repetidor_estatal"` → checar: (1) duplicação de lead, (2) título >80 chars, (3) WebSearch em nome próprio/número-chave se suspeito, (4) título semanticamente correto.
- Corrigir in-place (regra CHURN — WordPress mantém permalink).
- **NÃO remover** bibliografia/fonte visível.
- Log em `bugs_repetidor_YYYY-MM-DD.jsonl`.

## Registro histórico

- 13/08/2026 09:50 BRT: 6/6 posts do dia corrigidos in-place (Miguel autorizou); títulos 88→65/71 chars médios; leads deduplicados; Teodoro Silva Santos completo; 564 mortes corrigido de 545.
- Cartinha enviada pra ZCode reportando bug upstream de duplicação.

Regras irmãs: [[feedback-auditor-titulos-v4-7-regras-canonico]] · [[feedback-espelho-fontes-invisiveis-regra-editorial]] · [[feedback-nunca-churn-publish-draft-seo]].
