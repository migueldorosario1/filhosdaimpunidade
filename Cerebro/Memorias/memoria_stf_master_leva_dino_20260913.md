# Memória — Caso Master: LEVA DINO (PET 16.669) — log técnico (13/09/2026)

Par do fórum `Foruns/forum_stf_master_leva_dino_20260913.md` (a mina editorial está lá). Aqui fica o como-fazer.

## Arquivos

- **Acervo:** `Reportagens/Master/PET_16669/` — 7 arquivos: PET16669_13092026_baixada_pelo_Miguel.pdf (1,5MB) + 13092026_DESPACHO_LEVANTAMENTO_AVOCACAO_id15390366474.pdf (md5 IDÊNTICO ao do Miguel: a2619c1f2a698eb5ac1ca696cb723bf8) + VOLUME_A_150MB.pdf (628 págs, SEM camada de texto — escaneado) + VOLUME_B_61MB.pdf (IPe Barra Funda inteiro EM TEXTO — txt extraído em scratch: `/tmp/volB_ipe_barrunda.txt` 1MB) + decisão 03/09 (Make Up) + andamentos ×2.
- **Origem do Miguel:** `Dia a dia/2026 Set 13/dino_master/PET 16669 13092026.pdf` (mantido lá; cópia no acervo).
- **Scratch:** `ZCodeProject/scratch/stf_111_noite/` — `nota_stf_makeup.html` (nota oficial STF 10/09 da operação Make Up: Frias produtor executivo, R$ 645 mil/60 dias, 29 passaportes, ICB/ANC suspensos, 2 processos da Justiça de SP puxados), `novos/PET_16669_Dino/` (HTMLs das abas), log_16669.txt.
- **Fotos:** `fotos/dino_plenario_RosineiCoutinhoSTF.jpg` (109KB, license 10 = Public Domain Mark confirmado no JSON da página) + adendo no CREDITOS.md.

## Técnica

1. Portal marcou a 16.669 como 'Sigiloso' no detalhe MESMO após o levantamento (status atrasa), MAS serviu as 5 peças do _pecas.txt com o coletor padrão (`coleta.sh 7681816`) — 1ª peça veio no fluxo normal; as 2 GIGANTES (150MB/61MB) e as 2 restantes vieram no retry manual com jar fresco (`downloadPeca.asp?id=1539036{475,476,213739}` + 15390057510). Lição: **peças de 100MB+ baixam OK com --max-time 90** (o tamanho não é problema).
2. PDF de 628 págs sem texto = escaneado (pdftotext vazio em 5 amostras); não gastar tempo com OCR agora.
3. Extração do Volume B: `pdftotext` direto (1MB de texto) + python com `re.sub(r'\s+',' ')` e janelas `.{100}KW.{220}` — achados: 108 milhoes ×38, Go Up ×41, Karina ×144, Nunes ×87, Frias ×39, PCC ×0 (só na PF, não no IPe).
4. Nota oficial do STF (noticias.stf.jus.br) serve de resumo confiável da decisão de 10/09 e cita a íntegra (o PDF do Miguel).

## Pendências

1. VOLUME A: abrir/renderizar para identificar conteúdo (escaneado) — candidato a OCR futuro.
2. Re-coleta da 16.669 quando o status virar 'Público' (podem aparecer MAIS peças — hoje só 5 ids servidos).
3. PET 16.070 (Karina/produtora): segue sigilosa — re-checar (incidente 7594545).
4. Foto CC do Frias/Karina: Agência Câmara não tem Flickr; sem alternativa CC hoje (anotado no CREDITOS).

## Série publicada (14/09)

5 drafts no WP: 270810-270815 (M1-M5, autor 5470, cats 5088/21141/22, capas 270818-822 c/ crédito na legenda, metas §136 OK). Receita WP REST: CF bloqueia urllib (403/1010) → curl c/ UA navegador; mídia exige Content-Disposition attachment filename; creds chaves.sh NYC sem sair do servidor; ref cats/author = post 270323. Textos em Dia a dia/2026 Set 14/dino_master/textos_serie/.
