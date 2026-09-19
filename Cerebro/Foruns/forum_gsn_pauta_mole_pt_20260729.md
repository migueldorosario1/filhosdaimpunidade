# FÓRUM — GSN: post em PT + pauta mole no ar (29/07/2026)

**Data:** 2026-07-29 ~11:15 BRT · **Agente:** ZCode/Kimi K3 · **Gatilho:** Miguel (chat): "aqui, global south com postagem em português... esse texto é de assunto totalmente sem importância! quem escolheu isso? gsn são matérias fortes de geopolítica"

## 1. O incidente

Em 29/07 às 03:12 BRT o pipeline V4 local publicou no globalsouth.news o artigo **"Comoras tem seis medinas antigas na lista de patrimônio cultural da UNESCO"** — 100% em português (frontmatter `lang: "en"` mentindo) e pauta mole (patrimônio cultural), enquanto ignorava no mesmo banco bruto "Iran missiles target US forces in Jordan" e "China puts the 'squeeze' on Taiwan". Padrão repetia-se desde a migração V4 (20/07): luta livre de Togo (28/7), centro de exorcismo de Manila (27/7), AFCON/Senegal (28/7).

## 2. Quem escolheu (resposta ao Miguel)

**Ninguém — piloto automático V4 local** (cron 03:00 → `orquestrador.py --all`, `agentes_tematicos/v4/`):
1. `coletor.py` puxa os 8 primeiros itens do RSS do **africanews.com** sem filtro editorial algum;
2. `produtor.py` reescrevia com prompt 100% em PT e **nenhuma instrução de idioma** → DeepSeek escreveu em PT;
3. auditor frio julgava "adequação editorial" pelas **guidelines fracas do config** (não pela linha do contrato) → APROVADO;
4. `publicador.py` carimbou `lang: "en"` do config e commitou ("Refatoracao V4" 06:12 UTC) → Vercel.

## 3. Decisões executadas (ordem editorial do Miguel, mesmo chat)

1. **Post derrubado** (git rm post+hero, commit `ba9427b` → push → Vercel). Varredura: era o ÚNICO post em PT no repo (82 arquivos).
2. **Trava de idioma EN (determinística)** no `produtor.py`: prompt passa a exigir ENGLISH (sistema+usuário) quando `language: "en"` + pós-check `_parece_portugues()` (≥5 stopwords PT → `rejeitado_idioma`). Caso INVERSO ao veto de detecção de 29/05 (que era título PT em site PT) — aqui o falso-positivo só atrasa pauta, nunca publica idioma errado.
3. **Gate editorial forte (opt-in `hard_geopolitics: true`, só GSN):** veto determinístico de pauta mole (unesco, heritage, wrestling, exorcism, esporte, festival…) no título-fonte → `rejeitado_pauta_mole` sem gastar LLM; score `_forca_editorial()` (guerra/diplomacia/BRICS/atores/tech estratégica) ordena candidatas — **hard news primeiro** (Irã 9, China 6, Ebola Uganda 0); auditor LLM agora julga pela **LINHA EDITORIAL DO CONTRATO** (não mais pelas guidelines) + critério 7 IDIOMA.
4. **Contrato editorial `globalsouth.md`** ganhou a DIRETRIZ DO EDITOR 2026-07-29 (EN-only; geopolítica dura anti-imperialista pró-Irã/China/Rússia/Brasil/Sul Global; veto pauta mole) — Regra-mãe cumprida.
5. **Demais 7 portais intactos** (gate desligado sem a flag; testado).

## 4. Testes

`py_compile` OK + 6 testes unitários com os casos REAIS do dia (Comoras vetado; Togo/Manila/AFCON/antílopes vetados; Irã×EUA 9 > Uganda 0; corpo PT real detectado; EN legítimo não dispara; portal PT sem flag inalterado). Backup: `produtor.py.bak_pre_gsn_en_gate_20260729`, `globalsouth.json.bak_pre_gsn_en_gate_20260729`.

## 5. Pendências / decisões abertas

- **Feeds RSS**: africanews mantido (fonte de hard news africana também) — o gate filtra a parte mole. Se Miguel quiser, dá para trocar/adicionar feeds mais duros.
- ~~Posts moles ANTIGOS em inglês (Togo, Manila, AFCON) seguem no ar~~ → **DECIDIDO (Miguel, 29/07 ~11:50): permanecem no ar — já indexados pelo Google; o veto vale só para novos posts.** Registrado no contrato §Diretriz 2026-07-29 item 4.
- Rodada das 13:00 BRT de hoje já roda com os gates ativos — observar o próximo batch.

**Memória técnica:** `Memorias/memoria_gsn_pauta_mole_pt_20260729.md` · **Bug:** `BUG-20260729-0300-GSN-PT-PAUTA-MOLE` (BUGS_RESOLVIDOS)
