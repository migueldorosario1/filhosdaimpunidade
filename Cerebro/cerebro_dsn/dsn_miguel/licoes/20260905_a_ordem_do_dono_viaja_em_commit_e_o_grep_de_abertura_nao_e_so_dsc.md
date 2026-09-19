# A ordem do dono viaja em commit com carimbo velho — o grep de abertura não é só DSC-*

**Data:** 05/09/2026 · **Ronda:** 163ª DS-Dell (01:00, série despertar) · **Tipo:** processo/leitura de ordens

## O quê
Abri a 163ª conferindo o ritual de sempre — "sem bloco DSC-* novo desde DSC-20260903-064" — e o relê do origin (fetch + `git log` dos commits recentes que tocam `de_dell.md`) pegou **2 ordens do Miguel que NÃO são DSC-***:
1. **VIDEO_PRO_DSYOUTUBE — sabatina Elmano de Freitas (34Z-rSfvOM4)**: encomenda com conteúdo datado **04/09 19:20** (baixar na porta Dell, transcrever, artigo forte Elmano×Ciro com números reais Quaest/Datafolha, rascunho WP, gate CL, lembrar a Bia) — o commit `b63b1868a` só chegou ao origin **~00:45 de 05/09** (~5h25 depois do carimbo do conteúdo).
2. **ORDEM ASTRA — BLINDAGEM DUPLA**: relay DSH-us65 com conteúdo datado **04/09 20:20** (ZM checa tudo que o Astra produz · DS-N Chefe checa por segurança · **Astra obedece ao DS-N Chefe**, nada executa sem autorização expressa · Miguel instrui direto, sempre pelo conduto do Chefe) — commit `b23918107` no origin **00:58** (~4h38 depois).

As rondas 161ª/162ª (00:00/00:30) leram "sem novidade" porque o grep de abertura só cobria blocos `DSC-*` numerados e os canais CL/XM — e essas ordens viajam como **relay DSH-us65/ORDEM/VIDEO_PRO em commit**, sem número DSC e sem bloco destacado no começo do arquivo.

## Por quê
1. O Miguel fala por vários canais (áudio no bot → INBOX_MIGUEL.md; voz → relay DSH-us65 que posta no de_dell; pedido direto → commits com a identidade migueldorosario1) — o DSC-* numerado é só UM dos formatos.
2. O carimbo de tempo do CONTEÚDO (19:20/20:20) não é o do COMMIT (00:45/00:58): ordem antiga pode parecer nova (ou nova parecer antiga) se o vigia olhar só o texto do bloco ou só a data do commit.
3. O CEO/vigia da ponte é quem faz o registro central das ordens — se ele só procura DSC-*, ordem em outro formato passa despercebida por rondas (foi o caso do Elmano: o bloco VIDEO_PRO já estava no de_dell e eu não o processei nas 161ª/162ª).

## Como aplicar
- **Abertura da ronda**: além do grep `DSC-*`, rodar `git fetch origin && git log origin/main --oneline -N` filtrando por `ORDEM|VIDEO_PRO|relay|DSH` e conferir os **blocos soltos no fim do de_dell.md do origin** (sem prefixo de agente conhecido).
- **Registrar sempre o DONO** da encomenda/ordem (Elmano 34Z → DS YouTube; prompt Astra → ZM posta + Chefe na alçada; etc.), mesmo quando não há ação minha — o registro + reporte de donos é o papel do vigia.
- **"Sem DSC novo" ≠ "sem ordem nova"** — frase de check só vale para o formato DSC; o check de ordens é outro item, com outro verbo.
- Extensão da família de lições "origin vence o clone local" e "ordem do dono viaja em COMMIT (DSC-060, 03/09)": agora com o formato relay DSH-us65 coberto no grep.

## Ref
- Bloco DS-20260905-003 (de_dell.md, item 1 — 2 checks com as 2 ordens).
- Commits: `b63b1868a` (VIDEO_PRO Elmano), `b23918107` (blindagem Astra), `0cf2da3f2` (FALA 00:33 "Pior. Tira o pior").
- Irmãs: licoes/20260903_relance_em_ronda_esbarra_na_fisica_e_whisper_parcial_e_zero.md (ordem viaja em commit, DSC-060), licoes/20260904_o_numero_da_ronda_sai_do_origin_mesmo_com_rondas_paralelas.md.
