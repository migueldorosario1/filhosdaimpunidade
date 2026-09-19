# FÓRUM — GSN: LINHA EDITORIAL CONSOLIDADA (diretriz do editor, 29/07/2026)

**Data:** 2026-07-29 ~11:50 BRT · **Agente:** ZCode/Kimi K3 · **Fonte:** palavra direta do editor Miguel no chat
**Contexto:** na esteira do incidente do post PT/pauta mole (`forum_gsn_pauta_mole_pt_20260729.md`), Miguel consolidou a linha editorial do Global South News. Este fórum é a **referência canônica** da linha — espelhada no contrato vivo `agent_data/contratos/globalsouth.md` (§DIRETRIZ DO EDITOR 2026-07-29).

## 1. A linha (palavra do editor)

1. **GSN é 100% EM INGLÊS.** Título, corpo e tags sempre em inglês. Nada em português vai ao ar.
2. **Pauta = GEOPOLÍTICA DURA.** Matérias fortes de geopolítica, em especial:
   - artigos **anti-imperialistas**;
   - favoráveis ao **Irã**, à **China**, à **Rússia**, ao **Brasil** e ao **Sul Global** em geral;
   - **tecnologia** também entra (com peso estratégico — chips, IA, soberania, cadeias).
3. **Pauta mole NÃO entra** (patrimônio/UNESCO, folclore, ritos, esporte, turismo, lifestyle), salvo ângulo geopolítico explícito e central.

## 2. Decisão sobre o legado (Miguel, 29/07 ~11:50)

> "não precisa remover esses outros, porque já devem ter sido indexados. mas vamos evitar."

- Posts moles **antigos** (anteriores a 29/07, em inglês — ex.: Togo wrestling, exorcismo Manila, AFCON) **PERMANECEM no ar**: já indexados pelo Google, remoção prejudicaria SEO.
- O veto vale **daqui para frente** — garantido pelos gates ativos (abaixo).

## 3. Enforcement (como a linha é aplicada no código)

| Camada | Mecanismo |
|---|---|
| Pré-LLM | Veto determinístico de pauta mole no título-fonte (`rejeitado_pauta_mole`) |
| Fila | Score `_forca_editorial()` — hard news (Irã/China/sanções/BRICS/tech estratégica) primeiro |
| Redação | Prompt exige ENGLISH-ONLY quando `language: "en"` |
| Pós-redação | Gate determinístico de idioma (`rejeitado_idioma` — corpo PT nunca sobe) |
| Auditoria LLM | Julga pela LINHA EDITORIAL DO CONTRATO + critério IDIOMA |

Patch: `V4_PATCH_GSN_EN_LINHA_20260729` em `agentes_tematicos/v4/produtor.py` · Config: `hard_geopolitics: true` em `agent_data/configs/globalsouth.json`.

## 4. Ponteiros

- Contrato vivo (sempre atualizado primeiro): `agent_data/contratos/globalsouth.md`
- Incidente de origem: `Foruns/forum_gsn_pauta_mole_pt_20260729.md` · `Memorias/memoria_gsn_pauta_mole_pt_20260729.md` · `BUG-20260729-0300-GSN-PT-PAUTA-MOLE`
- Índice GSN: `CEREBRO_INDEX_GSN.md` (§Registros de linha editorial)
