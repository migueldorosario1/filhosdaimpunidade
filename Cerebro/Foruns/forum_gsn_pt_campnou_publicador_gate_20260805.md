# FÓRUM — GSN: post PT/ES no ar DE NOVO (Camp Nou, 02/08) — cura no publicador (05/08/2026)

**Data:** 2026-08-05 ~00:30-01:10 BRT · **Agente:** ZCode/Kimi K3 · **Gatilho:** Miguel (chat): "materia em espanhol no gsn. tem que ser em ingles sempre" (URL do post Camp Nou)

## 1. O incidente

Em 02/08 às 13:23 BRT o pipeline V4 local publicou **"Tragédia no Camp Nou: Obrero muere durante reconstrução do estádio"** — título misto PT/ES, corpo 100% PT, `lang: "en"` mentindo, pauta mole (acidente em obra de estádio de futebol; fonte: seção **/sports/** da Al Jazeera). A varredura de 05/08 achou **um segundo post PT no ar**: "Advogados exigem a libertação do ex-presidente do Níger…" (publicado 30/07, um dia DEPOIS do gate de 29/07 — também vindo da fila legada).

## 2. Causa-raiz (diferente do bug de 29/07)

Os gates `V4_PATCH_GSN_EN_LINHA_20260729` existem e funcionam — **mas só no `produtor.py`**. Os dois posts PT foram aprovados em **25/07 (pré-gate)**, ficaram na fila `auditado.jsonl` como "aprovado" e o **`publicador.py` publicou sem revalidar idioma nem linha editorial** (carimbou `lang:"en"` do config e commitou). Furo de defesa em profundidade: a esteira tinha gate na produção e nenhum na publicação.

## 3. Decisões executadas (ordem editorial permanente: EN-only + geopolítica dura)

1. **Camp Nou derrubado** (git rm post+hero, commit `4dc1074` → Vercel; 404 confirmado). Pauta mole + PT: mesmo tratamento do precedente 29/07.
2. **Níger/Bazoum republicado EM INGLÊS** (era geopolítica dura — o conteúdo servia à linha; só o idioma estava errado): versão PT derrubada, versão EN nova com slug/hero/tags EN (`ed6228a`; 200 confirmado; URL PT antiga 404). Registrado no banco (`aprovado`+`publicado`) p/ dedup.
3. **Gate no publicador** (`V4_PATCH_GSN_EN_PUBLICADOR_20260805`, defesa em profundidade): antes de gastar hero/LLM, revalida (a) idioma PT→`rejeitado_idioma` em qualquer site EN (paridade com produtor); (b) veto pauta mole por título + **veto por URL de seção `/sports/`** (opt-in `hard_geopolitics`, só GSN). Vetado ganha desfecho e sai da fila.
4. **Produtor reforçado:** mesmo veto por URL `/sports/` na entrada (o veto por título não pegava "Worker dies at Camp Nou Stadium").
5. **Purga da fila legada:** 5 itens moles pré-gate (3× UNESCO, boxing, Real Madrid) receberam desfecho `rejeitado_pauta_mole` — a mesma decisão que o gate tomaria, antecipada p/ não travar rodadas. Fila: 36 → 31.
6. **Config:** `soft_veto_keywords` do GSN ganhou `camp nou`, `real madrid`, "boxing" (falso-positivo geopolítico zero; "barcelona" sozinho evitado de propósito).
7. **Demais 7 portais intactos** (testes 5 e 6 provam: railpost EN sem flag e ceará PT-BR inalterados).

## 4. Testes

`py_compile` OK + **7 testes unitários** (post real Camp Nou detectado; EN de /sports/ vetado; hard news EN liberada; PT em railpost EN vetado; /sports/ sem flag intacto; PT-BR intacto; Real Madrid vetado) + **simulação da fila real** (36 → 5 vetados, 31 liberados). Backups: `produtor.py.bak_pre_gsn_en_publicador_gate_20260805`, `publicador.py.bak_…`, `globalsouth.json.bak_…`.

## 5. Pendências

- Fila legada EN (31 itens, 21/07→04/08) segue publicável — alguns são human-interest borderline (Betye Saar, projeto Kinshasa) mas nenhum viola veto determinístico; LLM auditor os aprovou. Se Miguel quiser faxina maior, dá para envelhecer (>7 dias) fora.
- Posts moles ANTIGOS já publicados permanecem (decisão 29/07: já indexados).
- Lição permanente: **todo gate novo precisa nascer nas DUAS pontas da esteira** (produção E publicação) — fila entre elas é zona cega.

**Memória técnica:** `Memorias/memoria_gsn_pt_campnou_publicador_gate_20260805.md` · **Bug:** `BUG-20260802-1323-GSN-PT-PUBLICADOR-SEM-GATE` (BUGS_RESOLVIDOS)
