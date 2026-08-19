# YT-PATRULHA — achados no agente YouTube nacional — 16/08/2026 ~22:58

Tag: `YT-PATRULHA` · Origem: sessão ZCode/Qwen 3.8 (implementação da camada de nomes)

## 1. 🔴 Kimi paygo SUSPENSO (HTTP 429) — RESOLVIDO nesta sessão
`_jornal_confirmar_llm` (confirmação da edição do Jornal da Fórum / Fórum Onze e
Meia) usava SÓ Kimi paygo. Log 16/08 22:30: `HTTP 429: Your account org-6a7a...
is suspended`. Sem rede de segurança, o post diário fixo do Jornal ficaria sem
edição confirmada. **Correção aplicada:** cascata DeepSeek→Kimi
(`_chat_json_cascata` em `youtube_cafezinho.py`, mesma lógica do curador).
Backup: `youtube_cafezinho.py.bak_pre_verifica_nomes_20260816`.
**Ação Miguel:** nenhuma. (Se a conta paygo foi descontinuada de propósito,
a cascata já opera sem ela; se foi bloqueio indevido, vale reativar no console
da Moonshot.)

## 2. 🟡 Fallback yt-dlp do Transkriptor sem binário no cron
Log 16/08 22h: `yt-dlp exception: [Errno 2] No such file or directory: 'yt-dlp'`
quando o Transkriptor tenta o fallback S3/yt-dlp. O `rodar_yt_dlp` do agente
resolve o binário por conta própria, mas o fallback interno do
`util_youtube_transcript` chama `yt-dlp` seco (PATH do cron não tem).
Sintoma: vídeo com transcrição URL-direto Failed fica sem transcrição nenhuma.
**Não corrigido ainda** (escopo de outra peça); candidato a fix no próximo
toque no util (usar o mesmo binário/env do rodar_yt_dlp).

## 3. 🟡 Proxy iProyal: rajada bot_check na rodada 22h
`[proxy] todos os provedores falharam (bot_check)` em uma tentativa da rodada
curada. Intermitência conhecida do iProyal (lição registrada na memória
agente-youtube-reativado-20260816); a rodada seguinte tende a normalizar.
Se repetir por 3+ rodadas seguidas, tratar como 🔴 (1º suspeito de parada).

## Contexto da sessão
Na mesma sessão entrou a camada NOMES SEM ERRO (websearch Brave + memória de
personagens) no agente — fórum: `Foruns/forum_nomes_agentes_youtube_websearch_memoria_20260816.md`.


---

## ADENDO 16/08/2026 ~23:55 BRT — rodada PATRULHA ZCode/Qwen 3.8 (PASSO 6)

Tag: `YT-PATRULHA` · Origem: caçadora de imagens (automation-e1b2d648), PASSO 6.

### Status da patrulha desta rodada (🟢/🟡 sem ação nova)

- **NACIONAL (local):** cron do agente presente (6 linhas) e disparando. Achados 2 e 3 acima CONFIRMADOS e ainda em aberto (yt-dlp fora do PATH do cron; proxy intermitente mas saudável — 49 operações salvas na janela). Nenhum 🔴 novo.
- **GSN (NYC):** cron `0 11,17` presente; última execução limpa 17:00 UTC. 🟢
- **Painel (Tencent):** 0 pedidos pendentes. 🟢

### 4. 🟠 IMG-GATE — capa do post 266125 REPROVADA pelo Tribunal (novo)

Varredura PASSO 4.5 da caçadora encontrou 2 posts future com capa sem meta de checagem:
- **266120** (aeroporto Guarulhos, media 266124) → Tribunal **APROVOU**; meta `_cafezinho_img_check` ok:true gravada 23:45.
- **266125** (lateral do MAC Niterói, media 266126, "Debate na FLIN 2026...") → Tribunal **REPROVOU** (imagem não aderente ao título/excerpt); meta ok:false gravada 23:45. **O gate fail-close segura o publish deste post até a capa ser trocada.** Quem for publicar o 266125 (Loop Miguel/Claude) precisa trocar a capa antes. Nada foi apagado.

### 5. 🟠 INFRA — canônico sob pico de carga 23:25–23:40, Redis flapping (novo)

Durante a rodada: wp-cli falhou intermitentemente com `RedisException: socket error on read socket` (~23:28–23:35); `redis-cli ping` PONG (uptime 20h, serviço estável); load médio 13→22 em 8 CPUs; **causa identificada: processo wp-cli de OUTRA sessão** (`wp post list --search=TESTE META`, ~2,3 GB RSS, ~2 min de CPU) pressionando MySQL (335%) + Redis (monothread sob contenção). **Site SEMPRE no ar externamente** (www=200/301). O processo terminou e o load normalizou; wp-cli voltou a funcionar sem retry. **Sem ação corretiva necessária** (não reiniciei nada). Lição: pico de carga noturno = olhar `top` antes de culpar o Redis.
