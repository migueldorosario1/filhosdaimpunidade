# MEMÓRIA TÉCNICA — Tribunal Visual Rio Carta + plano econômico (08/09/2026)

Par do fórum: `Foruns/forum_tribunal_visual_riocarta_20260908.md`.
Sessão: ZCode/Qwen 3.8 no Dell, operando o NYC via ssh (`Host nyc` = 198.199.121.136).

## Arquitetura descoberta (mapa p/ próximas sessões)

- Rio Carta = site Astro em `/root/tematicos/sites-v4/riocarta` no NYC; repo GitHub
  `migueldorosario1/riocarta-v4` branch main; deploy Vercel automático no push.
  (O clone do Dell em `Projeto Cafezinho Agentes/sites-v4` está PARADO em 18/08 — não é
  a fonte do que publica; mexer sempre no NYC.)
- Pipeline: `/root/tematicos/agentes_tematicos/v4/` — `orquestrador.py` → `coletor.py` /
  `produtor.py` (motor genérico; wrappers `riocarta_produtor.py` etc.) / `publicador.py`.
  Configs em `/root/tematicos/agent_data/configs/<site>.json`; contratos em
  `/root/tematicos/agent_data/contratos/<site>.md`.
- Visão: `nucleo_visao.py` — `julgar_imagem()` (cascata gemini → gemini-tencent proxy
  :8778 → qwen-vl-max; FAIL-OPEN histórico) e `confirmar_imagem()` (gate final de 18/08,
  FAIL-CLOSE). `nucleo_visao_fallback.py` = busca Pixabay/Openverse/Unsplash + geração IA.
- Crons NYC (root): `0 12 * * * orquestrador.py --all --sem-youtube`; riocarta tinha
  extras `0 2,20 * * *` (AGORA COMENTADOS, marcador ECONOMIA_RIOCARTA_1DIA_20260908;
  backup `/tmp/crontab.bak_pre_economia_riocarta_20260908`).

## Cadeia de falha do caso Aécio (por que passou)

1. Busca Openverse retorna obra titulada "Aécio Neves - Senador" p/ query de "senado".
2. `julgar_imagem` tem viés pró-aprovação calibrado (bug #34, 25/07: rejeitava demais) —
   "político abraçando eleitor" = "contexto amplo" p/ matéria de eleição; sem regra de
   ESTADO/PESSOA.
3. `confirmar_imagem` (18/08) idem: matéria não nomeia pessoa específica (16 candidatos)
   → "contexto amplo honesto" aprovado.
4. Crédito com o nome errado ficou no frontmatter como prova silenciosa.

## O que foi instalado (arquivos tocados no NYC, backups `.bak_pre_tribunal_20260908`)

- `nucleo_visao.py`: +`_TOKENS_INSTITUICAO`, `_norm_txt()`, `gate_credito_nomes()`,
  `_PROMPT_TRIBUNAL`, `tribunal_imagem()` (fim do arquivo). Regra de geografia do prompt
  calibrada em 2ª rodada: conjunto institucional de Brasília NÃO é "lugar errado" p/
  matérias de Senado/Câmara/eleições federais/estaduais (senão os 2 juízes reprovavam a
  capa honesta do Congresso 2×0).
- `publicador.py`: import de `tribunal_imagem`; bloco opt-in `cfg.get("tribunal_visual")`
  inserido ANTES do gate `confirmar_imagem` (~linha 855): reprova → remove hero +
  `_adiar_por_falta_de_hero` + `continue` (post adiado, não perdido).
- `produtor.py`: +`_norm_acentos_pt()`, `_sentence_case_ptbr()`; regra `regra_titulo` no
  `_prompt_producao` (só pt-BR); aplicação pós-`_sanitizar` em `rodar()`.
  Algoritmo: age só com ≥3 palavras capitalizadas no meio; preserva índice 0, siglas
  (isupper) e palavra cujo token capitalizado aparece no body_markdown (regex com
  lookaround, texto sem acentos); resto lower(). Idempotente.
- `agent_data/configs/riocarta.json`: `"tribunal_visual": true`.
- crontab root: linha `0 2,20` riocarta comentada.
- Repo riocarta-v4: commit `180320f` (hero Congresso + título/legenda/crédito sentence
  case); pré-fix da matéria em `/tmp/materia_20260908_pre_fix.md` (NYC).

## Testes (provas)

- `gate_credito_nomes('Aécio Neves - Senador via Openverse (by)', …)` → False
  ('crédito nomeia pessoa fora da matéria: Aecio Neves'); crédito Congresso → True;
  'YouTube/Sabatina Eleitoral' → True.
- `tribunal_imagem` foto Aécio + crédito velho → False no gate (zero visão); foto Aécio +
  crédito genérico → False 2×0 na visão (regra de político de outro estado funciona SOZINHA).
- `tribunal_imagem` hero Congresso + crédito novo → True 2×0 ("Sede do Senado Federal").
- `_sentence_case_ptbr`: title case da matéria → sentence case exato; nomes próprios
  preservados via corpo; título já correto intocado.
- Vivo: `curl` da URL → `<title>`/`og:title` sentence case; md5(hero servida)=md5(fonte).

## Armadilhas p/ quem retomar

- NÃO mexer no clone Dell do sites-v4 p/ publicar (parado em 18/08; o vivo é o NYC).
- `julgar_imagem` continua FAIL-OPEN p/ sites SEM tribunal (comportamento antigo
  preservado de propósito — mudar isso é decisão do Miguel p/ todos os sites).
- O gate de crédito é substring (não palavra inteira) no título+corpo: proposital p/
  pegar flexões ("senador"⊂"senadora"); falso-positivo possível = post ADIADO (recupera
  na rodada seguinte), nunca publicado errado.
- Créditos de fotógrafo puro ("João Silva via Wikimedia") seriam reprovados pelo gate —
  não aparecem nos 15 formatos reais do banco (YouTube/canal e "assunto via Openverse");
  se aparecerem, cortar também em " foto de "/" por " já está previsto no corte.
- py_compile no NYC exige `/root/venv/bin/python3` (3.12).

## Custos

Tribunal = ≤2 chamadas de visão/hero (gemini-flash + qwen-vl-max), só riocarta por ora,
1 matéria/dia → desprezível. Gate de crédito = 0 chamadas. Desembargador só em 1×1.
