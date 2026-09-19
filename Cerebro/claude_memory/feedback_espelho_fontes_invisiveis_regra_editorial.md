---
name: feedback-espelho-fontes-invisiveis-regra-editorial
description: Posts das 5 verticais V4 novas (cats 79/43/582/1271/258) NUNCA citam veículo pelo nome no corpo — link silencioso em palavra-chave. Escopo MIGRADO para o canônico ocafezinho.com em 12/08 ~17:45 BRT
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d917262a-1c40-4990-942c-4a2a8b497e3d
---

**ATUALIZAÇÃO 12/08 ~17:45 BRT:** regra MIGROU do espelho pro canônico junto com as 5 verticais. Vale agora nas cats **79 (Cultura) / 43 (Economia) / 582 (Meio Ambiente) / 1271 (Esporte) / 258 (Saúde)** no `ocafezinho.com`. As 3 verticais antigas do canônico (nacional cat 22, geopolitica cat 5003, ciência cat variados) SEGUEM com atribuição visível — a regra fontes invisíveis é só pras 5 novas. Detalhes migração: [[project-v4-5-verticais-canonico-migradas-20260812]].

**Nos posts das 5 verticais V4 (Cultura, Economia, Meio Ambiente, Esporte, Saúde) publicados no canônico ocafezinho.com NUNCA citar veículo pelo nome no corpo. Fonte é INVISÍVEL — link silencioso em palavra-chave.**

**Why:** regra editorial oficial dos contratos `v4_{cultura,economia,meio_ambiente,esporte,saude}_v1.md` em `/root/v4_labs/contratos/` no NYC. Miguel explicitou na cartinha Fase 0 (`Foruns/cartinhas/cartinha_claude_code_fase0_v4_espelho_20260812.md`, 12/08/2026 16:50 BRT): *"NUNCA citar veículo pelo nome nos posts. Link silencioso em palavra-chave."* Motivação editorial: as verticais novas devem parecer curadoria própria do Cafezinho, não agregador que empresta autoridade a fonte externa; leitor não pode se sentir "empurrado" pra outro site.

**How to apply:**

1. **Ao revisar draft do espelho (cats 79/43/582/1271/258),** grepar por padrões: `"segundo o|segundo a|de acordo com|conforme o|conforme a|reportou o|noticiou a|informou o|informa a"` + nome de veículo (`Agência Brasil`, `InfoMoney`, `GE`, `O Eco`, `Mongabay`, `CONASS`, `Reuters`, `AFP`, `Bloomberg`, `Folha`, `Estadão`, `G1`, `UOL`, `Metrópoles`, `Fórum` etc.). Se achar, remover a citação + inserir link silencioso na palavra-chave relevante do próprio texto.
2. **Exemplo before/after:**
   - ❌ *"Segundo a Agência Brasil, a inflação de julho ficou em 0,3%."*
   - ✅ *"A [inflação de julho](URL-da-fonte) ficou em 0,3%."*
3. **Aspa literal citando pessoa (fonte primária)** = PERMITIDA e recomendada — o veto é só pra citação de veículo. `"Vou vetar", disse Lula` OK. `Segundo o G1, Lula vai vetar` NÃO OK.
4. **Log:** anotar em `bugs_espelho_YYYY-MM-DD.jsonl` como `bug_corrigido: "fonte_visivel_removida"` — permite métrica de reincidência do worker.
5. **Feedback loop:** se a taxa de reincidência ficar alta (>30% dos drafts), amostrar 10 exemplos e mandar via `inbox_trindade/zcode.md` pra ZCode afinar o `write_briefing` dos contratos `v4_*_v1.md`.

**Escopo:** vigente no canônico `ocafezinho.com` a partir de 12/08 ~17:45 BRT apenas nas 5 verticais novas (cats 79/43/582/1271/258). Regras irmãs: [[project-v4-5-verticais-canonico-migradas-20260812]], [[feedback-modo-enxuto-preservar-worker-v4]].

**Contraste com as verticais antigas do canônico:** as 3 verticais tradicionais (nacional cat 22, geopolitica cat 5003, ciência) SEGUEM com atribuição visível — regra tese/FSLP + fonte nomeada. Não confundir escopos: no MESMO site (ocafezinho.com), cats 22/5003 = fonte visível, cats 79/43/582/1271/258 = fonte invisível.
