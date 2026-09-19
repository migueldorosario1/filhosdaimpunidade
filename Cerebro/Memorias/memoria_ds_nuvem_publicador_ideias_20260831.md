# Memória — Batismo DS-N Publicador + DS-N Ideias (log técnico completo)

**Data:** 31/08/2026 · **Sessão:** ZCode/GLM-5.3 (Dell) · **Prompts de origem:** ordem direta do Miguel (refs DSC-009/010)

## Ambientes e caminhos

| Item | Onde |
|---|---|
| Robô 1 (Publicador) | Tencent `~/dsn_publicador/dsn_publicador.py` + `capas_seed.json` + `consenso_seed.json` + `estado.json` + `logs/` |
| Robô 2 (Ideias) | Tencent `~/dsn_ideias/ronda_dsn_ideias.sh` + `prompt.md` + `estado.json`; log `/tmp/dsn_ideias/` |
| Crons Tencent | `*/15` flock `/tmp/dsn_publicador.lock` (`DSN_PUBLICADOR_15MIN_20260831`) · `13,43` (`DSN_IDEIAS_30MIN_20260831`) |
| Canal Publicador | repo `cerebro/Foruns/ponte_laura_completa/de_nuvem_publicador.md` |
| Canal Ideias | repo `cerebro/Foruns/ponte_laura_completa/de_ideias.md` |
| Relatório diário | repo `cerebro/Relatorios/ds_nuvem_chefe/AAAA-MM-DD.md` (append) |
| Credencial WP Tencent | `/home/ubuntu/.env.unificado` (`WP_USER_CAFEZINHO`/`WP_PASS_CAFEZINHO`/`WP_SITE`) · backup `.bak_pre_dsn_publicador_20260831` |
| Cofre de origem (Dell) | `Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/.env.unificado` |
| Fonte do robô (fonte da verdade) | `/tmp/dsn_deploy/` no Dell desta sessão (deploy por scp) |

## Decisões de projeto (e porquê)

1. **Publicador determinístico (sem LLM):** a mão que publica não interpreta — reduz risco de falso-positivo editorial; consenso vem da ponte (GATE) ou de seed explícito.
2. **Marcador de scan = `consenso|resgate|elegível` + janela ±120 chars do ID:** simulação inicial pegou 3 drafts intrusos (268320/268366/268394) via "aprovad/homologad/publish" soltos (linhas de CAPA aprovada, GRADE homologada, "publish direto AGY"). Após aperto: scan final = exatamente os 5 certos. Lição: **aprovação de capa ≠ consenso de publicação** — vocabulários distintos na ponte.
3. **Scan nunca aplica capa; só seed curado** (receitas URL+legenda+crédito vêm de bloco CL citado).
4. **GATE-IMG (mu-plugin `cafezinho-gate-imagem-checada.php`) é lei:** robô não bypassa; reporta e espera o Tribunal. Aceita `_cafezinho_img_check` JSON `{"ok":true,...}` (REST grava — meta registrada) ou `_cafezinho_img_isenta` (decisão editorial documentada). Camada 2 do plugin reverte publish fora do REST sem checagem.
5. **Quirk REST→future:** draft com `date_gmt=0000-00-00` + POST `status=publish` pode retornar 200 com status `future`. Curas: `wp eval "wp_publish_post(ID)"` (imediata) e `date` no payload (permanente). 268374 publicou limpo via REST; 380/386/373/372 precisaram da cura.
6. **Tribunal Visual na NYC:** Gemini Vision 400 "User location is not supported" (região do datacenter) → fallback Qwen3-VL funciona e é a visão que julgou. Contexto REAL do post (700 chars do conteúdo) virou 1 reprovação em aprovação (268373) — reconfirma a regra da casa "contexto jornalístico viaja no request".
7. **Git do robô:** pull `--ff-only`; push com reconcile `pull --rebase` quando rejeitado (ônibus concorrido da ponte, padrão já conhecido). Commit seletivo só canal+relatório.
8. **Ideias sem cofre WP no wrapper:** Lei de Poderes aplicada tecnicamente (não consegue publicar nem por acidente).

## Comandos/provas-chave do batismo

- Publicações: 268374 17:18 (REST pelo robô) · 268380/268386 17:44 · 268373/268372 17:52 (`wp_publish_post`) — todas `post_status=publish` + HTTP 200 nos slugs no `www.ocafezinho.com` (268386 slug sanitizado `meta-poe-criacao...` sem acento).
- Capas: mídias 268432 (NASA), 268433 (Kaczynski FBI), 268434 (Toffoli/Senado), 268435 (ZJU Xixi), 268436 (Meta HQ) — legenda com crédito+licença via PATCH `/media/{id}` (caption+alt).
- Meta 268373 `_cafezinho_img_check` = Tribunal APROVADA c/ contexto; 268372 `_cafezinho_img_isenta` = JSON documentando GATE CL-024 explícito + tribunal 2× sem motivo.
- Commits da ponte: canal do Publicador criado + linha BATISMO COMPLETO (push OK, 0 pendentes); Ideias `320ff5f72`.
- Simulação pré-batismo (prólogo do protocolo de produção): scan impresso e conferido post a post antes de qualquer publish.

## Bugs encontrados no caminho (e curas)

1. Meu 1º ciclo não escrevia linha na ponte em falha e morria no `git add` de arquivo inexistente → corrigido (linha ❌ com detalhe GATE-IMG; commit tolerante; estado salvo em `finally`).
2. Push rejeitado travaria ciclos futuros (pull ff-only falha com commits locais divergentes) → reconcile rebase.
3. Aspas literais no `.env` do Dell quebram curl `-u` (HTTP 400 enganoso) → strip de aspas no loader do robô.

## O que falta / próximos passos

- DSC começar a postar `IDEIA_PRO_DSNUVEM_IDEIAS` (fila do robô 2 vazia).
- Investigar wp-cron não-flipando futures vencidos (registro candidato a BUG; fora do escopo de hoje).
- Acompanhar primeiros ciclos 15/15 do Publicador (logs Tencent; casa confere as provas por publicação).
- Se Miguel quiser: aviso de capa/publicação no Telegram pelo Publicador.

## Estado
MISSÃO CUMPRIDA nos 4 marcos: (1) credenciais espelhadas+hash IGUAIS; (2) Publicador NO AR + batismo 5/5 www 200; (3) Ideias NO AR (1ª ronda OK); (4) confirmação na ponte em cada marco (canal do robô + linha de batismo + fórum/memória/registros).

## ADENDO ~18:17 — v2 OLHO ROBÓTICO AUTÔNOMO (ordem Miguel ~17:40)
- v2.5 do dsn_publicador.py: olho duplo (Tribunal NYC via ssh root@198.199.121.136 + DeepSeek deepseek-v4-flash-vision-exp inline com contexto real; vazio=perna caída, NUNCA reprovado), fluxo fresco (fábrica ≤12h, 1/ciclo, 8/dia, desc per_page=100), grade scan mesmo-dia, defesa anti-flip, publish com status+date+date_gmt, Telegram sendPhoto só-positivo (TELEGRAM_TOKEN_DSC_BOT/DSC_BOT_CHAT_ID), capa via worker dsn_imagem --post-id (ssh NYC, 1×/h/post).
- Prova ao vivo 18:16: 268393 → worker real (caca_pedida) → "sem capa não publico pelado" na ponte.
- Bugs v2: int×timedelta; date_gmt zerado nos drafts (usar date local); fatia [:20] cortava o fluxo (posição ~29); DeepSeek raciocínio devolve content vazio.
- Lição WP: o site REVERTEU sozinho um publish p/ future (268380) — wp-cron depois publicou; robô agora re-checa os publicados do dia (anti-flip).
