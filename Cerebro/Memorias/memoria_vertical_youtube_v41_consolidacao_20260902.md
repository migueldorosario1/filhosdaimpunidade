# Memória — Consolidação do Vertical YouTube do V4.1 (log técnico)

**Sessão:** ZCode/Qwen 3.8 (Dell) · 02→03/09/2026 · Fórum-irmão: `Foruns/forum_vertical_youtube_v41_consolidacao_20260902.md`

## Contexto da missão
Ordem do Miguel (voz, ~23h 02/09): consolidar o vertical YouTube do V4.1 + coletor DSN rico (link, decupagem, thumb, descrição, título, e se possível texto já corrigido por DeepSeek flash); usar os princípios das melhores versões do agente YouTube (personagens, tese, vilão); estudar a história dos agentes YouTube da casa (Cafezinho + GSN); curar o erro de nome ("ele não pode errar nome"); manter o que for útil das instruções antigas.

Esta sessão deu CONTINUIDADE à infraestrutura montada mais cedo (fórum do maestro adendos 47-57 + memória `dsn-youtube-decupador-alimenta-v41-redator-20260902`): a cadeia DS-N→ficha→ingestor→produtor já existia; faltavam (a) os princípios no redator, (b) a camada de nomes, (c) o coletor rico, (d) a escada luxo certa, (e) saneamento do mock.

## Genealogia estudada (base das decisões)
v1 legado (mai/26, erros fonéticos via Transkriptor) → v3 (jun/26) → v2 NYC (`agents_labs/youtube_v2`) → `youtube_cafezinho.py` V4 nacional Dell (plano 21/07: personagens+tese+vilão; regra Miguel 25/08 de nomes) → temáticos → DS YouTube → GSN V2. 9 incidentes de erro de nome documentados (14/05 fonéticos; 25/07 Nunes Marques→"Nunes Max"; 02-03/08 [[VERIFICAR_NOME]] vazando; 09/08 Restivo→"Rechivo"; 24-25/08 "Fórum 11.6"; 31/08 "Elumano"/"Luizane Lins"; 01/09 Scuderie/Bello/Regina Celi). Instruções mineradas e herdadas: `analisar()` (personagens/vilão/tese), regra dos 3 caminhos de nome (certeza→escrever certo; dúvida→omitir com referência genérica; JAMAIS marcador), ajuste editorial (reforçar partes favoráveis sobre Irã/China/Sul Global), atribuição estrita.

## Mudanças técnicas (arquivo por arquivo)

### NYC `/root/agents_labs/youtube_v2/agente_youtube_v2_materializador.py`
Backup: `.bak_pre_vertical_luxo_nomes_20260902`. Patch `/tmp/patch_materializador_vertical.py` (11 trocas assertivas, todas OK):
1. Infra de personagens: `PERSONAGENS_DB=/root/agent_data/personagens_youtube.json` (248 personagens, portado do Dell via scp) + `_carregar_personagens()` fail-soft + `_bloco_personagens_prompt()` (lista "- Nome (cargo) [a transcricao pode errar como: alias]", teto 20.000 chars; bloco real = 11.230 chars) + `corrigir_nomes_personagens(texto)` conservadora (só substitui alias↔canônico quando NÃO se contêm mutuamente, len≥4, regex `\b` IGNORECASE).
2. sys-prompt PT novo: escriba ULTRA-LUXO + 6 princípios (PERSONAGENS PRIMEIRO; TESE motor com VILÃO — direita=crítica/esquerda=força; estrutura tese→contexto→personagens→análise + título nunca o do vídeo; linha editorial esquerda pró-Lula; NOMES SEM ERRO omitir na dúvida; ASPAS só literais).
3. sys-prompt EN equivalente (CHARACTERS FIRST; THESIS; NAMES ZERO ERRORS; QUOTES verbatim).
4. `_instr_idioma` PT: título EMU-2 ("UMA unica frase, sem sigla, sem dois-pontos; prefira o cargo ao nome solto").
5. Campo `"apresentador"` no formato JSON obrigatório.
6. Bloco "GRAFIA CANONICA DOS PERSONAGENS DA CASA" injetado no f-string antes de `Transcricao:`.
7. Escada luxo: `[("openai","gpt-5.6-sol",1.0), ("alibaba","qwen-max",0.6), ("moonshot","kimi-k2.5",0.6)]` via envs `YOUTUBE_V2_REDATOR_MODEL/FALLBACK_1/FALLBACK_2` (providers conferidos no `/root/agente_roteador_llm.py` linhas 605/675/687; qwen-max→qwen3-next-80b-a3b pelo upgrade gateway do roteador).
8. Pós-`_limpar_json`: loop de correção de nomes em titulo/html/entrevistado/apresentador; tag apresentador usa o campo do LLM antes do `MAP_HOSTS`; meta ganha `nomes_corrigidos_memoria`.
Self-test: bloco 11.230 chars ✓ · "Fernando Addad"→"Fernando Haddad" ✓ · nome canônico não sofre dupla substituição ✓ · `py_compile` ✓.

### NYC `/root/agents_labs/youtube_v2/agente_youtube_v2_ingestor_dsn.py`
Backup: `.bak_pre_ingestor_rico_20260902`. Patch `/tmp/patch_ingestor_dsn.py` (4 trocas OK):
- `parse_ficha` retorna 3-tupla `(meta, transc, texto_corrigido)`; seção `## Texto corrigido` extraída do fim do corpo.
- INSERT `videos` com 14 colunas (+`descricao`, +`raw_meta_json` com thumb/ficha) + UPDATE de enriquecimento p/ linha já existente sem descricao/thumb.
- INSERT `dialogos` usa `texto_corrigido or transc`; `metodo` = `decupagem_texto_corrigido` quando aplicável; `meta_json.tem_texto_corrigido`.
Self-test: ficha rica ✓ · retrocompat (ficha velha sem Texto corrigido) ✓ · `py_compile` ✓.

### NYC banco `/root/agent_data/youtube_dialogos.sqlite` (saneamento, script `/tmp/sanea_vertical_nyc.py`)
- `publicaveis` id 96 (mock da rodagem manual 21:00 sem `YOUTUBE_V2_LLM_ENABLED=1`, ainda `pronto` = viraria rascunho-lixo na corrida das 08h): `status='descartado'` + `ultimo_erro` anotado (guarda: só se modelos_json LIKE '%mock%' AND status='pronto').
- `videos` 9pojT1Svzj4: `status='noticia_publicavel'` (falha de aspas Jaccard do material do Sol das 19:2x) → reset p/ `transcrito`, `ultimo_erro=NULL` — reprocessa na corrida das 11 UTC com o prompt novo.
- 3 vídeos com `published_ts=0` (morte certa no frescor) sem ficha com data → enriquecidos via oEmbed (`/tmp/enriquece_videos_sem_meta.py`): mnQ-Cf5YphQ = "Ukraine's Economy Is Collapsing" · dEUUkZz_Xrs = "US Attacks Iran: Futile, Costly, and Deceitful? #shorts" · BWAEcQThHGE = "Trump's Strait Claim: 0 FOR 4 in War Objectives! #shorts" — todos Judge Napolitano. `published_ts` = decupado_em (fallback marcado em `raw_meta_json.published_ts_origem`).
- Resultado: 8 vídeos frescos `transcrito` prontos p/ o produtor das 11 UTC.

### Tencent `/home/ubuntu/ds_youtube/alimentador_fila.py`
Backup: `.bak_pre_coletor_rico_20260902`. 4 trocas OK: ns `media` (mrss) no RSS; entry captura `media:description` + thumb `i.ytimg.com/vi/<vid>/maxresdefault.jpg`; tuple vira 6 campos; manifest `<vid>.json` ganha `descricao` (linha única ≤800) + `thumb`. Cache `alimentador_canais.json` limpo (entrada suja "UC... # Judging Freedom" removida). Cron: :05/:35.

### Tencent `/home/ubuntu/ds_youtube/ds_youtube.py`
Backup: `.bak_pre_coletor_rico_20260902`. Helpers novos antes de `gerar_ficha_decupagem`:
- `_chave_deepseek()`: lê `DEEPSEEK_CAFEZINHO_CANONICO` do `~/.env.unificado` (nunca imprime).
- `_personagens_relevantes(transc)`: filtra os personagens cujos tokens (≥4 chars) aparecem no texto; teto 6.000 chars.
- `texto_corrigido_flash(transc)`: deepseek-chat temp 0.1 max_tokens 8000 timeout 240s; remove timestamps antes de enviar; janela 400–28.000 chars; guarda anti-truncamento (saída < 50% do entrada → descarta); FAIL-OPEN total ("" em qualquer falha).
- `gerar_ficha_decupagem`: frontmatter ganha `descricao:` (info.json `description` ou manifest `descricao`, linha única ≤800) + `thumb:` (info.json `thumbnail` ou maxresdefault); corpo ganha `\n## Texto corrigido\n\n<texto>\n` quando o flash devolve algo. Cron: :07/:22/:37/:52.
- `personagens_youtube.json` portado p/ `~/ds_youtube/` (248 personagens).
Self-test ao vivo: RSS 6-tupla Record News (desc 346 chars) ✓ · `_personagens_relevantes` ✓ · flash real limpou timestamps/acentuação E corrigiu "fernando addad"→"Fernando Haddad" ✓.

## Gotchas novos (aprendidos nesta sessão)
- Patch assertivo (count==1 senão exit 1) com gravação SÓ no fim = atômico; a 1ª âncora do fim do prompt errou (`Transcricao:\n"""` ≠ real `Transcricao:\n{transcricao}\n"""`) e o script falhou sem tocar o arquivo — inspecionar o texto real antes de ancorar.
- Heredoc SSH com aspas simples dentro de comando ssh já aspeado quebra tudo → scripts sempre via scp+execução de arquivo.
- `sqlite3` CLI não existe no NYC → sempre python3 -c/heredoc com módulo sqlite3.
- Vídeos do DSN sem manifest nem info.json chegam SEM canal/título/data (3 casos) → oEmbed resolve canal/título; data cai no fallback decupado_em.
- Mocks de teste ficam `pronto` na tabela `publicaveis` e o auditor/publicador os pegam na próxima corrida — sanear SEMPRE (UPDATE com guarda + anotar em ultimo_erro).

## Observação
- RSS do Judging Freedom retornando HTTP 404 da Tencent (23:3x) — canal mais produtivo do vertical; BBC/Al Jazeera/Record OK. Provável bloqueio intermitente de IP (Tencent = datacenter). Se persistir: rota via fetcher Dell residencial.

## Estado final / o que falta
- Tudo patcheado, compilado e testado nos 2 servidores; cadeia pronta p/ a corrida das 11 UTC (08h BRT) de 03/09.
- Falta: conferir a corrida de 03/09 (materiais do Sol com princípios novos); decisão do Miguel sobre aspas de shorts (Whisper vs limiar); 3 handles de canal a corrigir; 404 do Judging Freedom monitorado.
— ZCode/Qwen 3.8 · 02-03/09/2026
