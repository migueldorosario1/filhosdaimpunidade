# MEMÓRIA TÉCNICA — GSN: post PT + pauta mole (2026-07-29)

**Bug:** BUG-20260729-0300-GSN-PT-PAUTA-MOLE ✅ RESOLVIDO
**Fórum (decisões):** `Foruns/forum_gsn_pauta_mole_pt_20260729.md`
**Agente:** ZCode/Kimi K3 · **Duração:** ~11:05–11:40 BRT

## Cadeia de diagnóstico (passo a passo)

1. **Cérebro:** `CEREBRO_INDEX_GSN.md` — GSN = EN-only, GitHub→Vercel; errata 27/07: executor NYC; ATUALIZACOES 23/07: pipeline antigo NYC DESLIGADO, repo `global-south-news` fora do ar (último commit 24/07).
2. **Site no ar ≠ repo antigo:** DNS Vercel OK, mas artigo Comoras NÃO existia no repo `global-south-news`. Repo vivo = **`globalsouth-v4`** (migração 20/07). Commit `63ea0c2a` 2026-07-29T06:12Z por "Refatoracao V4".
3. **Frontmatter do post:** `lang: "en"` com corpo 100% PT; `source_url` = africanews.com/2026/07/25/six-ancient-medinas…
4. **Executor real:** cron LOCAL (`crontab -l`): `0 3,13 * * * orquestrador.py --all` em `agentes_tematicos/v4/`. Log `agent_data/v4/cron_v4.log` confirmou: rodada 03:08–03:12 BRT, coletor pegou 17 itens (incl. Irã×EUA e China×Taiwan), produtor DeepSeek aprovou 5 (Ebola Uganda, antílopes UNESCO…), publicador soltou Síria/ONU + Comoras.
5. **Causas raiz (código):**
   - `coletor.py:74` — `feed.entries[:8]` sem filtro editorial;
   - `produtor.py:_prompt_producao` — prompt 100% PT, zero instrução de idioma; campo `language` do config nunca era usado;
   - `produtor.py:_auditar` critério 5 — usava `guidelines` fracas do config; sem critério de idioma;
   - `globalsouth.json` — categoria "Culture" válida; feed africanews;
   - `publicador.py` — `lang:` do frontmatter vem do config, sem validar corpo.

## Patch aplicado — `V4_PATCH_GSN_EN_LINHA_20260729`

Arquivos (backups `.bak_pre_gsn_en_gate_20260729`):
- `agentes_tematicos/v4/produtor.py`:
  - `_PT_STOPWORDS` + `_parece_portugues()` (≥5 hits/3000 chars → PT; alta precisão, falso-positivo só atrasa);
  - `_SOFT_VETO_DEFAULT` + `_HARD_NEWS_TERMS` + `_forca_editorial(cfg,titulo,texto)` → -1 veto mole; score título×3 + corpo×1;
  - `_prompt_producao`: bloco ENGLISH-ONLY no sistema E no usuário quando `language=="en"`;
  - `_auditar(..., contrato="")`: com `hard_geopolitics`, critério 5 = LINHA EDITORIAL DO CONTRATO (1500 chars) + reprova pauta mole; critério 7 IDIOMA (EN-only);
  - `rodar()`: puxa MAX_ITENS×3, ordena por score desc, corta em MAX_ITENS; veto mole ANTES de gastar LLM (`rejeitado_pauta_mole`); gate de idioma pós-geração (`rejeitado_idioma`); ambos registram no banco auditado (fail-visible).
- `agent_data/configs/globalsouth.json`: `hard_geopolitics: true` + `soft_veto_keywords` (19 termos).
- `agent_data/contratos/globalsouth.md`: DIRETRIZ DO EDITOR 2026-07-29 (EN-only + geopolítica dura + veto pauta mole).

## Remoção do post

`git rm` post + hero em `sites-v4/globalsouth`, commit `ba9427b` → push. Varredura heurística nos 82 posts do repo: Comoras era o único em PT.

## Testes (todos verdes)

Comoras/UNESCO → -1 ✅ · Togo wrestling → -1 ✅ · Manila exorcism → -1 ✅ · AFCON → -1 ✅ · antílopes UNESCO → -1 ✅ · Irã×EUA=9, China×Taiwan=6, Uganda Ebola=0 (ordenação) ✅ · corpo PT real detectado ✅ · EN legítimo não dispara ✅ · prompt exige EN sistema+usuário ✅ · portal PT sem flag inalterado ✅ · `py_compile` ✅

## Lições

1. **Config sem enforcement é decoração:** o contrato editorial era perfeito, mas nada no código o aplicava — o auditor julgava por guidelines de 2 linhas.
2. **Prompt no idioma errado vence a instrução implícita:** prompt 100% PT produz saída PT mesmo com persona EN.
3. **FIFO mata hard news:** sem score, os 5 slots de LLM foram para Ebola/antílopes enquanto Irã×EUA esperava.
4. **Frontmatter `lang` precisa refletir o corpo** — carimbo do config sem validação = metadado mentiroso (SEO/hreflang).
5. Decisão 29/05 (sem detecção determinística de idioma) era para TÍTULO PT em site PT — caso inverso; aqui a detecção é segura e foi adotada com threshold alto.

## Adendo 29/07 ~11:55 BRT — decisão do editor sobre o legado

Miguel decidiu: posts moles ANTIGOS em EN (Togo wrestling, exorcismo Manila, AFCON) **PERMANECEM** no ar — já indexados pelo Google, remoção prejudicaria SEO. Veto à pauta mole vale só para novos posts (gates ativos). Registrado no contrato `globalsouth.md` §Diretriz 2026-07-29 item 4 e consolidado no fórum canônico `Foruns/forum_gsn_linha_editorial_diretriz_20260729.md`.
