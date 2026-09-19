---
name: feedback-gate-fact-check-dia-da-semana
description: "Correção semântica de DATA precisa verificar dia_da_semana também, não só o valor apontado pelo LLM juiz — DeepSeek pode acertar diagnóstico e errar remédio; ver caso fundador draft 263017 27/07/2026"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0c239f1e-08c3-4beb-a91e-5adf020d8159
---

**Regra:** Sempre que uma correção semântica proposta pelo LLM juiz (DeepSeek/GLM/Kimi) tocar uma DATA que aparece com dia_da_semana explícito no texto (formato `<dia_semana>, <dia> de <mês> de <ano>`), verificar via WebSearch TANTO o valor apontado quanto o dia_da_semana. LLM juiz frequentemente acerta que há erro (mês errado, ano errado) mas erra o remédio porque não checa a consistência dia↔dia_da_semana.

**Why:** Caso fundador draft 263017 Cafezinho (27/07/2026 06:00 BRT): Sentinela+DeepSeek propôs `25 de junho → 25 de julho` no texto "domingo, 25 de junho de 2026". Estava certo que era julho (a fonte The Hindu tinha URL `july-27-2026-latest-updates` + contexto de últimos ataques Irã/EUA). Mas 25/07/2026 foi SÁBADO — a proposta teria virado "domingo, 25 de julho de 2026", mantendo inconsistência. Minha checagem via CNN/CBS/NPR/Fox mostrou pausa MÚTUA começou DOMINGO 26/07 (EUA pausou sex+sáb, Irã aderiu domingo). Remédio real: "domingo, 26 de julho". Se eu aplicasse `editar_corpo_publicado` com a proposta bruta do DeepSeek, teria publicado desinformação de forma diferente, não corrigido.

**How to apply:**
- Antes de aplicar patch de data: `date -d 'YYYY-MM-DD' +%A` (Bash) OU inferir via WebSearch pra confirmar dia_da_semana.
- Se dia_semana no texto ≠ dia_semana real da nova data proposta: corrigir AMBOS (mês E dia) baseado no contexto factual do evento (a que evento a data se refere? qual foi a data real do evento?).
- Se ambiguidade sobre qual dia do evento (ex: "pausa começou no final de semana" — foi sex, sáb ou dom?): WebSearch fontes primárias, escolher o dia que faz o texto ficar factualmente correto.
- Nome do padrão: **GATE-FACTUAL-DIA-DA-SEMANA** — extensão sugerida ao gate fact-check bug #37 (Kimi implementou 26/07 13:33 BRT em `~/ferramentas/sentinela/lib/fact_check_gate.py`). Ver ponteiro no canal_trindade `[CHECAGEM-DUPLA-CLAUDE-263017]` 27/07 06:37 BRT.
- Não se aplica a datas SEM dia_semana explícito (ex: "no dia 25 de junho de 2026" sozinho não tem par a verificar — se contexto sugere só mês errado, correção só do mês basta).

**Padrão detectado no LLM juiz (DeepSeek/GLM):** foca no valor que o prompt destaca (a proposta) e ignora a estrutura formal ao redor (o dia_semana). É "correção pontual" sem consistency check. Extensão do gate fact-check ideal: quando `entidade` do gate contém regex `<dia_semana>, <dia> de <mês> de <ano>`, adicionar verificação dupla + rejeitar proposta que só corrija metade.

**Regras irmãs:** [[sempre-pesquisar-web-em-duvida]] (WebSearch antes de qualquer afirmação factual), [[checagem-dupla-editorial-com-autonomia]] (autonomia pra aplicar remédio certo depois de checar), [[nome-proprio-figura-publica-nunca-publish-com-proposta]] (regra irmã de gate factual em publicação).
