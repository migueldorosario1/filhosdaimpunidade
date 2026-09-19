# Manual de Operação — Agentes YouTube do ecossistema (16/08/2026)

> **Propósito:** documento único para os loops (Miguel e Laura) **entenderem e vigiarem** os agentes YouTube — ordem do Miguel 16/08 ~22:50 ("fazer os dois loops entenderem o agente youtube e ajudarem no que for preciso"). Tema Duplo: `Foruns/forum_loops_vigilia_agente_youtube_20260816.md`.
> **Divisão de responsabilidades no fim do documento (§6).**

## 1. Os agentes YouTube hoje (16/08/2026)

### 1.1 Agente nacional do Cafezinho — 🟢 VIVO (PC do Miguel)
- **Código:** `Projeto Cafezinho Agentes/agentes_cafezinho/youtube_cafezinho.py`
- **Crons (BRT, crontab do Miguel):** `--rodada` 08:00/14:00/20:00 · `--jornal` 22:30/23:00/23:30 · `--forum11` 14:30/15:30
- **Log:** `agent_data/v4_cafezinho_youtube/cron.log` (todos os modos)
- **Canais:** 32 (21 nacionais + 4 geopolítica GSN + 7 IA) em `agent_data/canais_cafezinho_youtube.json` (envelope dict, chave `canais`) + curadoria em `agent_data/curadoria_cafezinho_youtube.json` (regra `escopo_ampliado`: **preferência nacional** — internacional só ganha se claramente superior).
- **Pipeline:** coleta RSS (proxy iProyal, frescor 2h/4h) → curador LLM (cascata DeepSeek→Kimi; fallback heurística) → transcrição (YouTubeTranscriber modo autônomo, idioma por canal; URL-direto → fallback yt-dlp MP3→S3) → análise (bastidor+tese) → redação tier superluxo → **draft/pending no WP** via `controle.ocafezinho.com` (autor histórico 5786; vai para `pending` se houver marcador `[[VERIFICAR_NOME]]`).
- **Categorias WP por canal:** nacionais `[22,28]` (Nacional+Vídeos), GSN `[5003,28]` (Geopolítica+Vídeos), IA `[30,28]` (Tecnologia+Vídeos).
- **Saída esperada:** 1-3 drafts/dia em ritmo normal. **Quem publica: SÓ o Claude (Loop Miguel)** — o agente nunca publica.

### 1.2 Pipeline GSN V2 — 🟢 VIVO (NYC 198.199.121.136)
- **Código:** `/root/agents_labs/youtube_v2/` · **Cron:** `0 11,17 * * *` (UTC) `/root/youtube_v2_pipeline.sh`
- **Log:** `/root/agent_data/youtube_v2_pipeline.log`
- **Canais:** `/root/agent_data/canais_youtube.json` — hoje 7 (Judging Freedom, Glenn Diesen, Dialogue Works, Daniel Davis, Neutrality Studies Français, kremlin, Aaron Maté). Formato `{nome, channel_id, sessao_preferida, ativo}`; **remoção = `ativo:false`** (nunca deletar).
- **Modo DRAFT** (ordem Miguel 16/08): publica como draft e aguarda revisão Loop Miguel + Loop Laura antes do publish.
- **Espelho local:** `agent_data/configs/globalsouth.json` — a gestão pelo painel (item 2) escreve aqui e o cron `sync_youtube_painel.py` reconcilia com o NYC.

### 1.3 Agentes YouTube V4 dos temáticos — 🔴 DESATIVADOS (03/08, ordem do Miguel: "rodava vazio")
- Configs prontos para reativação em `agent_data/configs/{aiatolah,mapario,...}.json` (seção `youtube`). Aiatolah: 3 canais de IA (Diamandis, Moonshots Highlights, Kantrowitz). Mapa Rio: 4 canais de política RJ (BandNews FM Rio, SBT Rio, Prefeitura do Rio, Poder360).
- `ceara_youtube.py` roda `*/2` localmente (Ceará Digital) — lembrete do Miguel de 05/08 segue aberto para formalizar.

## 2. Gestão de canais pelo Painel CCTV (16/08)
- **Página `/v6/youtube`** (Cafezinho) + cards 📺 nas páginas dos temáticos GSN/Aiatolah/Mapa Rio. Miguel adiciona/remove canais ali.
- Arquitetura caixa de entrada: painel grava pedidos na Tencent (`youtube_canais/pedidos/`) → **cron local `*/5` `agentes_cafezinho/sync_youtube_painel.py`** resolve/valida por RSS oficial → aplica nos JSONs locais (fonte de verdade) com backup → devolve estado canônico ao painel → GSN também reconcilia o NYC.
- **Pedido parado >15 min = problema no sync local** (ver runbook §5).

## 3. Dependências críticas
- **Proxy iProyal** (`util_proxy_iproyal.py`, cofre `YOUTUBE_PROXY_MODE=always` sem aspas): acesso ao YouTube a partir do PC do Miguel (bloqueio local) — coleta RSS, páginas de canal e fallback de transcrição. **Intermitência do proxy = 1º suspeito de qualquer parada.**
- **Transkriptor:** transcrição automática; cobra $6 até em rejeição de qualidade; fallback yt-dlp MP3→S3 já funciona sozinho.
- **WP:** `controle.ocafezinho.com` (auth = resolução `or` das chaves `WP_USER_CAFEZINHO`/`WP_PASS_CAFEZINHO` do cofre — nunca expor valores).
- **DNS do PC do Miguel:** soluça à noite (corrigido 15/08 p/ 1.1.1.1; retry em tudo).

## 4. Modos de falha conhecidos (por que a vigília existe)
| Incidente | Quando | Lição |
|---|---|---|
| Cron do NYC SUMIU (crontab editado por fora) | ~10/08, descoberto 16/08 | Bloco Vídeos parou 6 dias sem ninguém notar → **vigília de presença de cron é obrigatória** |
| 5 de 6 channel_ids do Aiatolah inválidos (404) | até 16/08 | ID de memória/LLM não é confiável; RSS 200 + título do feed é a prova final |
| Transkriptor URL-direto status=Failed | 16/08 | Fallback yt-dlp MP3 resolveu sozinho — não mexer, só observar |
| Proxy iProyal intermitente | recorrente | Cascata de provedores já tenta vários; falha persistente = checar assinatura/cofre |
| Draft 266153 com autor 5786 (repetidor estatal) | 16/08 | Comportamento histórico das credenciais desde julho; loops revisam antes do publish |

## 5. Runbook de verificação (comandos)
```bash
# NACIONAL (PC do Miguel)
crontab -l | grep -c youtube_cafezinho.py        # esperado: 6 linhas
tail -40 "$WS/agent_data/v4_cafezinho_youtube/cron.log"   # fresco (<26h)

# GSN (NYC)
ssh nyc 'crontab -l | grep youtube_v2_pipeline'   # esperado: 0 11,17 UTC
ssh nyc 'tail -5 /root/agent_data/youtube_v2_pipeline.log'  # fresco (<26h)

# SYNC DO PAINEL (caixa de entrada)
ssh tencent 'ls /home/ubuntu/cafezinho/v6/youtube_canais/pedidos/ | wc -l'  # 0 = fila andando
crontab -l | grep sync_youtube_painel             # esperado: */5

# SAÚDE GERAL DOS DRAFTS (WP)
# drafts de origem YouTube entram sem imagem pendente (thumb já vem do vídeo) e cats 28+
```
**Árvore de decisão:** cron ausente → re-add com backup (já feito 1× no NYC em 16/08, backup `.bak_pre_youtube_readd_20260816`). Log velho com cron presente → rodar 1 rodada manual e ler o erro. Proxy → `python3 util_proxy_iproyal.py --resumo`. Sem capacidade de resolver → registrar em `Cerebro/monitoramento_horario/bugs_encontrados/` + monitor de trabalho; o relatório CCTV 30/30min leva o alerta ao Miguel em linguagem humana.

## 6. Divisão de responsabilidades (ordem do Miguel 16/08 ~22:50)
- **ZCode (parte do Loop Miguel — fábricas):** vigília operacional na caçadora de imagens (PASSO 6, */30): presença de crons + frescor de logs + fila do painel; corrige o que for do escopo fábrica (cron, proxy, configs, canais via painel); nunca publica.
- **Loop Miguel (Claude, chefe único de publicação):** entende este manual; prioriza revisão dos drafts YouTube (nacionais e GSN); escala ao Miguel se ficar 2 slots seguidos sem produção nova; único que promove a publish (gate de imagem fail-close vale: draft YouTube já vem com thumb, mas a meta `_cafezinho_img_check` precisa existir para publicar).
- **Loop Laura (redundância integral do Loop Miguel):** os dois loops são IGUAIS em desenho e capacidade (esclarecimento do Miguel 16/08 ~23:40); a única diferença é que **só o Loop Miguel (canônico) pode modificar arquivos** — a Laura opera `SHADOW_READ_ONLY`: observa, sugere e aponta soluções, sem escrita. Está sendo preparada para ASSUMIR INTEGRALMENTE caso o Loop Miguel falhe (protocolo de fail-over: `Foruns/forum_protocolo_failover_loop_miguel_laura_20260816.md`). Nos drafts YouTube especificamente: segunda opinião editorial (especialmente GSN em inglês — experiência aprovada 10/10/7 em 13/08) e vigília reserva (mesmos checks do PASSO 6 quando acionada) — sempre em modo leitura/sugestão.
- **Miguel:** gestão de canais pelo painel + veto final + decisões de reativação dos temáticos.

## 7. 🧠 Camada NOMES SEM ERRO (websearch + memória) — 16/08/2026

Ordem do Miguel: "personagens, tese, tudo isso também está sendo visto pelos
agentes youtube. não pode errar os nomes. por isso tem que ter websearch e memoria."

- **Módulo:** `Projeto Cafezinho Agentes/agentes_cafezinho/verifica_nomes.py`
  (memória + websearch Brave/DDG + veredito LLM; `--selftest`).
- **Memória:** `agent_data/personagens_youtube.json` (81 personagens seed;
  auto-alimentada a cada verificação; `.bak` rolante).
- **Fluxo:** análise → extração de nomes → memória (custo zero) → websearch
  (teto 8/rascunho) → veredito (confirmado/duvidoso/inexistente) → dossiê
  comanda a redação → meta WP `cafezinho_nomes_check` + auditoria
  `agent_data/v4_cafezinho_youtube/nomes_<video_id>.json`.
- **Para os Loops (revisão de drafts YouTube):** leiam a meta
  `cafezinho_nomes_check` (wp-cli: `wp post meta get <id> cafezinho_nomes_check`)
  — ela lista cada nome, o status e a grafia canônica usada. Nome com status
  duvidoso NO TEXTO = rejeitar o draft.
- **Fail-soft:** qualquer falha da camada → vale a regra tradicional do bug #31
  (conhecimento do LLM + omissão na dúvida). Nunca bloqueia rascunho.
- **Pendente:** levar a mesma camada ao GSN V2 no NYC.
- Detalhe técnico completo: `Memorias/memoria_nomes_agentes_youtube_websearch_memoria_20260816.md`;
  decisão: `Foruns/forum_nomes_agentes_youtube_websearch_memoria_20260816.md`.

## 8. 🧭 Diretriz de DEPURAÇÃO EDITORIAL (Miguel, 16/08/2026 ~23:10)

Vídeos que contenham críticas ao Irã, à China ou ao Sul Global **podem** ser
usados pelo agente. No post, na tese e na manchete: IGNORAR por completo os
trechos críticos (não citar, não mencionar, não refutar — para o post não
existem) e REFORÇAR apenas as partes favoráveis ao Irã/China/Sul Global e
anti-imperialistas (EUA/OTAN/Israel). Implementada em
`youtube_cafezinho.py::_nota_depuracao_editorial` (analisar + redigir) e na
regra `escopo_ampliado` da curadoria (curador não descarta candidato por ter
críticas). Canal símbolo do regime: **Fareed Zakaria GPS (CNN)** —
UCs_6LFfjAH7Yv2QrQ0ddb6g, 33º canal do rol (16/08). Fórum:
`Foruns/forum_depuracao_editorial_gps_post_duplo_20260816.md`.

## 9. 🌐 Regra IDIOMA PT INTEGRAL — tudo em português, inclusive as aspas (Miguel, 17/08/2026)

Ordem do Miguel ao ver trechos em inglês no ar: "o agente youtube tem trechos em ingles,
corrige lá e nunca mais faça isso. tudo tem que ser em portugues! os trechos são as aspas".

- **Regra:** título, corpo e ASPAS DIRETAS sempre em PORTUGUÊS. Vídeo em inglês →
  traduzir as falas citadas com fidelidade (tradução completa, sem resumo, sem mistura).
- **Implementação (2 camadas, 17/08 ~16:00):**
  1. Regra no prompt de redação (`youtube_cafezinho.py`): "NUNCA deixe trecho em inglês
     no post, nem entre aspas".
  2. Guarda heurística `_tem_aspas_ingles()` no `publicar_draft`/`atualizar_draft`:
     citação com ≥2 stopwords EN rebaixa o post para `pending` (revisão humana) —
     aspas em inglês NÃO chegam a público automaticamente. Backup `.bak_pre_gate_imagem_20260817`
     (mesmo backup do patch do gate).
- **Backfill:** post 266172 tinha 6 aspas em inglês (vídeo Dialogue Works) — todas
  traduzidas e o post atualizado no ar (verificado: zero aspas EN). Varredura completa
  dos posts do agente (cat 28 + "Transkriptor"): só o 266172 tinha.
- **Relacionado:** o pipeline GSN V2 (NYC) publica EN para o GSN (por design), mas o
  bug de roteamento que o faz gravar EN no WP do Cafezinho segue atribuído ao Claude
  (bug `yt_patrulha_post_en_no_wp_cafezinho_20260817_0215.md`).
- Fórum: `Foruns/forum_regra_idioma_pt_integral_agente_youtube_20260817.md` + memória técnica.

## 10. 🛑 FREIO ANTI-DESPERDÍCIO — quem não publica não transcreve (Miguel, 22/08/2026)

Ordem do Miguel: "não está conseguindo publicar → para de usar o transcripto →
para até resolver. Não pode acumular transcrição sem usar." Implementado e no ar
(no agente nacional; detalhes em `Foruns/forum_agente_youtube_antidesperdicio_20260822.md`):

- **Cache de transcrição** em disco (`agent_data/v4_cafezinho_youtube/transc_<video_id>.json`):
  reprocessamento custa ZERO — transcrição paga nunca mais é jogada fora.
- **Pendentes recuperáveis** (`pendentes_youtube.json`): falha pós-transcrição
  (análise/nomes/redação/WP) não mata mais a rodada; vira pendente e a próxima
  rodada recupera do cache antes de gastar com vídeo novo (3 tentativas cada).
- **Cascata consertada** (`agentes_tematicos/v4/nucleo_llm.py::gerar_json`):
  resposta vazia/inválida de um LLM agora CAI para o próximo da cadeia (era
  Traceback — 26× no log, causa da perda de 22/08 20h).
- **BREAKER editorial** (todas as rodadas do cron): ≥4 rascunhos YouTube
  aguardando revisão no WP = agente NÃO transcreve vídeo novo até a fila andar
  (teto via env `YOUTUBE_FILA_REVISAO_MAX`; WP fora = fail-open). **Recuperação
  de pendentes continua rodando mesmo com breaker ativo.**
- **Kill switch manual**: `touch agent_data/v4_cafezinho_youtube/PAUSAR_TRANSCRICAO`
  para a transcrição nova (loops/Miguel); remover o arquivo retoma.

**Para os loops:** a fila de revisão que destrava o breaker é de vocês
(publicação exclusiva CM, 2ª opinião Laura). GSN V2 NYC: cron ausente desde
19/08 e 27 drafts acumulados — não reativar até a fila andar (decisão conjunta).
