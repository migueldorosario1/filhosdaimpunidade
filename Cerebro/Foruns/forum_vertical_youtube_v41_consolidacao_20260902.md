# Fórum — Consolidação do Vertical YouTube do V4.1 (ordem do Miguel 02/09 ~23h)

**Sessão:** ZCode/Qwen 3.8 (Dell) · **Data:** 02-03/09/2026 · **Tema Duplo:** memória `memoria_vertical_youtube_v41_consolidacao_20260902.md`

## A ordem do Miguel (voz, 2 linhas)

1. Consolidar o vertical YouTube do V4.1 junto com o coletor DSN de vídeo: o coletor traz link, decupação, thumb, descrição, título — e, se puder, já o texto corrigido por um DeepSeek flash; o V4 ultra-luxo dá o tratamento final ("transformar num post bem escrito").
2. NÃO criar nada do zero: usar "toda a parafernália, os princípios do agente YouTube que a gente já fez — personagens, apresentando com tese". Estudar a história dos agentes YouTube (Cafezinho e GSN). Consertar o único defeito: "errar nome — ele não pode errar nome".
3. "As melhores versões dos agentes YouTube, inclusive a atual, tinham boas instruções — examine e mantenha o que você achar útil."

## Decisões

- O "vertical YouTube do V4.1" É o pipeline `youtube_v2` do NYC (não existe dentro do `v41_ciclo.py`) — honrada a ordem anterior de USAR o pipeline existente sem colidir com a reforma do V4.1.
- Herança das melhores versões: princípios do agente nacional V4 (plano 21/07: PERSONAGENS primeiro, TESE com VILÃO como motor, estrutura tese→contexto→personagens→análise, título forte próprio, linha editorial esquerda pró-Lula) + camada NOMES SEM ERRO (ordem 16/08 + regra 25/08: memória de personagens + na dúvida OMITIR o nome) + regras de atribuição do próprio v2 (não atribuir opinião do entrevistador ao entrevistado).
- Escada de luxo do redator: gpt-5.6-sol → qwen-max (→ qwen3-next) → kimi-k2.5. **Desvio documentado da ordem literal** (GLM 5.3 / Qwen 3.8 / Gemini 3.7): Gemini 3.7 está BLOQUEADO no NYC (IP datacenter) e GLM 5.3 sem saldo no zhipu NYC — kimi-k2.5 é o 3º frontier recomendado pela memória da casa (DSC-014/gemini-bloqueado).
- DeepSeek flash na Tencent = SÓ limpeza (tirar timestamps, pontuar, corrigir grafia de nomes com a lista canônica) — NÃO escreve matéria (ordem intacta: DSN não escreve). Fail-open: sem chave/erro → ficha segue só com a transcrição bruta.

## O que foi feito (com provas)

### NYC (`/root/agents_labs/youtube_v2/`, backup `.bak_pre_vertical_luxo_nomes_20260902` / `.bak_pre_ingestor_rico_20260902`)
1. **Materializador reescrito nos princípios** (11 trocas assertivas, `py_compile` OK): sys-prompt PT/EN ultra-luxo com os 6 princípios; título EMU-2 (1 frase, sem sigla, cargo antes de nome solto); campo `apresentador` no JSON; bloco GRAFIA CANÔNICA (11.230 chars, 248 personagens) injetado no prompt antes da transcrição; **correção pós-LLM** alias→canônico conservadora (self-test: "Fernando Addad"→"Fernando Haddad" ✓, nome canônico intacto ✓); meta `nomes_corrigidos_memoria`.
2. **Escada luxo corrigida** no materializador (envs `YOUTUBE_V2_REDATOR_MODEL/FALLBACK_1/FALLBACK_2`; providers conferidos no roteador global).
3. **Ingestor rico** (4 trocas, self-test OK + retrocompat): `descricao` + `raw_meta_json.thumb` em `videos`; seção "## Texto corrigido" da ficha vira o texto dos `dialogos` quando existir (`metodo=decupagem_texto_corrigido`).
4. **Saneamento:** mock publicavel id 96 → `descartado` (com guarda; era o "1º rascunho" falso da rodagem manual das 21:00 sem `YOUTUBE_V2_LLM_ENABLED=1`); vídeo 9pojT1Svzj4 resetado p/ `transcrito` (o produtor reprocessa com Sol na corrida das 11 UTC/08h BRT, agora com os princípios novos).
5. **Frescor salvo:** 3 vídeos com `published_ts=0` (morte certa no portão de frescor) enriquecidos via oEmbed — todos Judge Napolitano (1 episódio "Ukraine's Economy Is Collapsing" + 2 shorts); `published_ts` = decupado_em (fallback honesto, marcado no `raw_meta_json`).

### Tencent (`~/ds_youtube/`, backups `.bak_pre_coletor_rico_20260902`)
6. **Alimentador** (`alimentador_fila.py`): RSS agora captura `media:description` (ns mrss) + thumb; manifest `<vid>.json` ganha `descricao` (linha única ≤800) e `thumb`. Self-test ao vivo: Record News desc 346 chars ✓. Cache limpo (1 entrada suja removida).
7. **Decupador** (`ds_youtube.py`): ficha ganha `descricao:` + `thumb:` no frontmatter e seção **"## Texto corrigido"** via DeepSeek flash (chave `DEEPSEEK_CAFEZINHO_CANONICO`, teto 28.000 chars, fail-open). Self-test ao vivo: flash limpou timestamps/acentos E corrigiu "fernando addad"→"Fernando Haddad" usando `personagens_youtube.json` (portado p/ Tencent, 248 personagens).

### Estado da cadeia agora
- **8 vídeos frescos transcritos** no banco do NYC à espera do produtor (4 Judging Freedom incl. o resetado, 1 Record News "News 19 Horas" 02/09, 3 enriquecidos via oEmbed) — a corrida das **11 UTC (08h BRT) de 03/09** escreve os materiais já com os princípios novos.
- Cadeia completa: alimentador (Tencent :05/:35) → fetcher Dell → DSN decupa + texto corrigido (:07/:22/:37/:52) → ficha no repo → ingestor NYC (:55) → pipeline NYC (11/17 UTC: produtor→auditor→publicador draft-only) → R1/R2 → CL publica.

## Observações / riscos
- **Judging Freedom RSS dá 404 da Tencent** agora (23:3x) — era o canal mais produtivo; BBC/Al Jazeera/Record seguem OK. Pode ser bloqueio intermitente de IP; monitorar nas próximas rondas do alimentador.
- Validações de aspas seguem ativas: citação tem que estar LITERAL na transcrição (o caso 9pojT1Svzj4 foi rejeitado por Jaccard — o reset dá 2ª chance com o prompt novo de aspas estritas).
- `## Texto corrigido` só para transcrições 400–28.000 chars (fora disso, fail-open e o redator usa a bruta).

## O que falta / próximos passos
1. Conferir a corrida das 08h BRT de 03/09: materiais escritos com Sol + princípios, nomes corretos, validador de aspas passando.
2. Se o 404 do Judging Freedom persistir na Tencent: testar via proxy/fetcher Dell (residencial).
3. Decisão pendente do Miguel: afrouxar limiar de aspas p/ shorts OU áudio+Whisper no fetcher (adendo 54b).
4.handles que falharam: @GlennDiesen, @DeepDiveDanielDavis, @FRANCE24English (achar os certos).

## Rollback
- NYC: `cp agente_youtube_v2_materializador.py.bak_pre_vertical_luxo_nomes_20260902 agente_youtube_v2_materializador.py` (+ idem ingestor `.bak_pre_ingestor_rico_20260902`); saneamento do banco = reverter os 2 UPDATEs ( histórico no fórum).
- Tencent: restaurar `ds_youtube.py.bak_pre_coletor_rico_20260902` e `alimentador_fila.py.bak_pre_coletor_rico_20260902`.
— ZCode/Qwen 3.8 · 02/09/2026 ~23:5x BRT
