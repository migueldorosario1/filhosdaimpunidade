# 🧠 MEMÓRIA TÉCNICA — Auditoria Geral de Custos, Telemetria e Recuperação de Crons (2026-07-29)

> **Data:** 2026-07-29 ~10:30–11:55 BRT · **Executor:** ZCode (Kimi), sessão interativa com o Chairman Miguel
> **Fórum de decisões:** `Foruns/forum_auditoria_custos_telemetria_recuperacao_crons_20260729.md`
> **Escopo:** (1) auditoria de todos os gastos contínuos (APIs, tokens, assinaturas, servidores) + estado da telemetria; (2) investigação e recuperação dos itens quebrados apontados pela auditoria. Sem exposição de segredos.

---

## 1. METODOLOGIA

- Ritual canônico: `00_CEREBRO_CANONICO.md` → `CEREBRO_INDEX_MASTER.md` → `CEREBRO_NODE_TELEMETRIA.md` (mapa das 4 máquinas) + nodos de chaves/catálogo.
- SSH ao vivo: `nyc` (198.199.121.136, root) e `tencent`/`cingapura` (43.156.151.165:38422, ubuntu) OK; `alibaba` (39.106.184.215) **timeout** → Miguel declarou a máquina **LEGACY/aposentada** (29/07).
- Dados de custo: 29 consolidados diários `/root/agent_data/custos_consolidados/2026-07-*.json` copiados (scp) e agregados localmente; relatório prosa do dia em `/root/agent_data/relatorios_financeiros/2026-07-29.md`; painel público `http://43.156.151.165/v6/custos` respondendo (HTML OK).
- Dois agentes de exploração (auditorias read-only): (a) agentes locais de cron — providers, volumes, telemetria; (b) Cérebro — assinaturas, saldos, preços, incidentes/decisões de custo de julho. Um terceiro investigou Sentinela + bot Telegram.
- Preços validados ao vivo: DeepSeek (`api-docs.deepseek.com`) confirma catálogo: v4-flash $0,14/$0,28 (cache hit $0,0028), v4-pro $0,435/$0,87. OpenAI bloqueou fetch (403) — usada tabela do `CEREBRO_NODE_CATALOGO_MODELOS_LLM.md` (verificado 25/05, compatível c/ tabela pública).

---

## 2. CUSTOS DE API — DADOS REAIS (NYC, julho/2026)

### 2.1 Série diária (por_dia dos consolidados; 29/07 parcial até 13:07 UTC-3)

```
01: 6,37 | 02: 19,90 | 03: 21,57 | 04: 20,18 | 05: 6,57 | 06: 8,95 | 07: 14,76
08: 16,14 | 09: 14,53 | 10: 17,28 | 11: 31,70 | 12: 30,01 | 13: 64,57 | 14: 43,99
15: 38,18 | 16: 20,13 | 17: 20,77 | 18: 14,65 | 19: 14,02 | 20: 3,14 | 21: 2,38
22: 2,08 | 23: 1,82 | 24: 1,60 | 25: 1,41 | 26: 1,18 | 27: 1,87 | 28: 2,41 | 29: 1,31
TOTAL 1–29/jul: US$ 443,47
```
1–15/jul: US$ 354,71 (média US$ 23,65/dia) · 22–28/jul: US$ 13,68 (média **US$ 1,95/dia** → projeção 30d ≈ US$ 59 ≈ R$ 300 @5,10).

### 2.2 Agregado do mês

**Por provider:** openai $203,82 (46,0%) · deepseek $150,91 (34,0%) · alibaba $104,68 (23,6%) · anthropic $13,61 · fal $11,23 · google $10,95 · ideogram $0,48 · perplexity/moonshot/desconhecido <$0,05.
**Por modelo:** gpt-4o-mini $174,49 · deepseek-v4-flash $141,94 · qwen-plus $51,29 · gpt-5-mini $24,81 · claude-sonnet-4-6 $13,61 · fal-ai $11,23 · gemini-2.5-flash $10,70 · deepseek-v4-pro $8,81 · gpt-5.5 $2,41 · gpt-4o $2,01 · qwen-max $0,95 · ideogram $0,48.
**Por agente:** `motor_coletor:curadoria` $380,39 (legado, PAUSADO 19/07) · `autocura_v4_consenso` $15,12 (LLM desativado 19/07) · `agente_comentarista` $13,74 · `gerador_imagem_editorial` $11,71 · `agente_comentarista_v4` $4,17 · `Repetidor_Estatal` $3,34 · `agente_memoria_v9` $2,84 · `curador_social` $2,35 · sociais tw/fio/fb ~$5.

### 2.3 Run-rate atual (relatório financeiro 29/07)

US$ 1,3080/dia · 300 chamadas · projeção 7d US$ 9,16. Top: `gerador_imagem_editorial` $0,84 (fal, 64,2%) · `agente_comentarista_v4` $0,2492 (226 chamadas) · `Repetidor_Estatal` $0,16. Providers do dia: fal $0,84 · deepseek $0,2921 · alibaba $0,2417 · openai $0,0523 · google $0,0027. Anomalias declaradas no próprio relatório: zhipu e brave sem log de uso automatizado; `conciliacao_cartao` e `logs_roteador_llm_dedicados` ausentes (MVP 0).

### 2.4 Inventário de crons verificado ao vivo

- **NYC (root, 32 linhas):** V4 geo/tec/nacional a cada 30min (coletor+intake+draft_worker), `agente_comentarista_v4` **1min** (flock), `auditor_titulos_gpt` 10min + relatório :58, `repetidor_estatal` 2h, `agente_manchete` 2h, `remover_no_home` 2h, `agente_performance` :52, `augusto_fiscal_tokens` 8h, `validador_modelos` 3h, autocura determinística 15:17 + resumo 8h + semanal sex 14h, governança financeira :07 (coletar+relatório), push métricas :07, caetano limpeza 6h, seo_pruning 3:07, daemon_indexador 30min, verificador_indexing 6h janela, pagespeed 9h, gsc 10h, ga4 seg 11h, media_promoter 6h, media_expander 6:47, ceara_hourly 9:15, cicero_hourly 10h, cicero_robo_coleta 2h.
- **Tencent (ubuntu, 8 linhas):** push_metrics 5min, gerar_pulse 10min, cafezinho_hourly 9:45, moka vigia_saldos 9h, banco_ouro busca 30min, classificador banco_ouro :17/:47, moka descadastro 15min. Serviços systemd ativos: cctv-v5, cctv-v6 (8084), painel-editorial, biblioteca-editorial-pilot, midia-ouro-panel. Crontab root não lida (sudo exige senha — lacuna de auditoria).
- **Local (26 linhas, usuário):** jornaisdodia 10:30/12:00, backup_reforma_local :20, sync_foruns_maestro_b2 :05/:35, limpa_diario 4h, cerebro→GitHub 30min, baleia_azul 8h/18h, orquestrador v4 --all 3h/13h, --so-youtube 2:30/12:30, --site ceara/riocarta 8h em 8h, backup_cerebro 3:40, youtube_cafezinho --rodada 8/14/20h --jornal 22:30/23:00/23:30 --forum11 14:30/15:30, sentinela agregador 23:55 (loop DESATIVADO 27/07 por Miguel), rsync fóruns→tencent :07/:37, sync_custos_v6 :12, backups gdrive/livro madrugada.

### 2.5 Agentes LOCAIS sem telemetria de custo (descoberta-chave)

`agentes_tematicos/v4/orquestrador.py` (8 sites) roda ~**68 gerações de artigo/dia** (deepseek-chat 83%, moonshot-v1-128k 15%, glm-4.5-flash 1%) + ~**48 julgamentos visuais/dia** (qwen-vl-plus 77%, gemini-2.5-flash 23%) — medido por contagem de log (174 ciclos desde 21/07). **Não grava `usage`/custo em lugar nenhum** (`nucleo_llm.py` lê a resposta e descarta `usage`); não existe `banco_custos*.jsonl` local ativo (espelhos locais têm US$ 0,0007 em 7 dias, gerado no servidor). `--so-youtube` roda vazio (youtube desabilitado nos 8 configs). Fix proposto: gravar usage no banco_custos (aguarda aprovação).

### 2.6 Custos fixos / assinaturas / saldos (fonte: `CEREBRO_NODE_CHAVES_E_LLMS.md`, fóruns julho, plano Moka)

- **Com valor:** GLM Coding Plan Max **US$ 144/mês** (renova 17/ago/2026; 622,69M tokens GLM-5.2 consumidos no painel) · Transkriptor ~US$ 30/mês · Vercel Pro US$ 20/mês · Brave ~US$ 5/mês (upgrade 26/07) · Backblaze B2 ~US$ 0,03/mês (camada 3) · Apple Developer US$ 99/ano (futuro, pendente) · domínio Moka ~R$ 40/ano (pago).
- **Sem valor documentado (lacuna):** Kimi for Coding Max (assinatura "Allegretto", endpoint `api.kimi.com/coding/v1`), Claude/Anthropic Max, DigitalOcean (4 droplets: NYC 198.199.121.136, 159.89.185.209 RC-Astro, 174.138.36.31 RC-WP, 159.65.177.60 lab), Tencent Singapura, ServerDo.in (WP Cafezinho, 190.89.239.65:51439), Google Drive 30 TB, plano SearchAPI.io.
- **Saldos paygo:** Kimi ~US$ 22 (conta REATIVADA 29/07 — §3.1) · Zhipu US$ 0 (erro 1113; só glm-4.7-flash grátis) · AssemblyAI US$ 47,75 autopay (29/05) · xAI/Grok US$ 3,54 (22/05) · Gemini recarregado 29/07 c/ `BANCO_OURO_GEMINI_BUDGET_DIARIO`=40 visões (corte ~99%, fórum ouro_precision) · Anthropic recarregado 25/05 (sangria US$ 15–20/dia estancada pelo deploy F0a).
- **Incidentes de custo julho (histórico):** motor_coletor runaway US$ 380 (pausa 19/07, 141.779 chamadas/mês) · autocura V4 US$ 15,12 zerada · Gemini R$ 98 sem conciliação (18/07) · Kimi 13 chamadas pagas fora do manifesto (18/07) · estouro teto gpt-5.5 em teste E2E (18/07) · hard-stop US$ 5/dia proposto pelo Maestro (19/07).

---

## 3. INVESTIGAÇÕES E RECUPERAÇÕES — LOG TÉCNICO

### 3.1 Kimi paygo — teste pós-recarga (29/07 ~11:45 BRT)

Fonte da chave: `Projeto Cafezinho Agentes/Outros/chaves/kimi_paygo.env` (`KIMI_PAYGO_API_KEY`; valor não copiado).
- `GET https://api.moonshot.ai/v1/models` → 200, lista `kimi-k3` (supports_image_in, video_in, reasoning, dynamic_tools).
- `POST /v1/chat/completions` (kimi-k3, max_tokens 5) → 200, `usage: prompt 91 + completion 5 = 96`.
**Veredito: conta OPERACIONAL.** A suspensão HTTP 429 "account is suspended" vista nos logs de 28–29/07 (rodadas 08:00) está superada.

### 3.2 Curador Cafezinho — por que caiu em heurística

`youtube_cafezinho.py`: `_kimi_paygo_key()` (linha 231) tenta `KIMI_PAYGO_API_KEY` (arquivo) → `get_key("KIMI_API_KEY")` → `get_key("MOONSHOT_API_KEY")`. As 3 chaves são da **mesma conta Moonshot paygo** → suspensão derrubou a cadeia inteira; qualquer falha → `_score` heurístico (docstring linha 238: "Qualquer falha → cai para a ordem heurística"). Não existe fallback cross-provider no curador (diferente do `nucleo_llm.py`: deepseek→kimi→glm→qwen→openai, tiers em `config/llm_tiers.json`). Proposta registrada no fórum §2.2.

### 3.3 Recuperação dos 5 arquivos (janela da deleção: 28/07 12:00 → 29/07 ~10:30)

Evidências da janela: `sync_jornais.log` mostra jornaisdodia.sh OK às 12:00 de 28/07 (417 MiB subidos às 10:37); `.pyc` do util_youtube_transcript compilado 27/07 16:33 (fonte de **27.887 bytes**); baleia rodou 28/07 (bloqueado por "edição ausente", provando que existia).
Busca em todo `/home/migueldorosario`: nenhuma cópia viva dos 5 arquivos fora de git/backups. Inocentados: `limpa_diario.sh` (só `rm` em caches: chrome, mesa, /tmp openclaw/transcritor/node) e `backup_reforma_local.sh` (só `b2 sync` upload). `git status` limpo → deleções não passaram por commit; autor desconhecido (hipótese: sessão de agente em "limpeza").

| # | Arquivo | Fonte da restauração | Notas |
|---|---|---|---|
| 1 | `Projeto Cafezinho Agentes/agents_labs/youtube_v2/util_youtube_transcript.py` | git `184e41da` ("Clean slate 2026-06-20", 26.838 B = linhagem v3_decoupled 23/06) | Delta de ~1 KB (27.887 − 26.838) de patches 23/06→27/07 **perdido**; `.pyc` (20.938 B, 27/07 16:33) guardado em `__pycache__` p/ eventual decompilação pycdc. Import testado OK: `from util_youtube_transcript import YouTubeTranscriber` c/ pyenv 3.10.13 e sys.path do youtube_cafezinho |
| 2 | `scratch/enviar_baleia_azul_v2.sh` | `scratch/enviar_baleia_azul_v2.sh.bak_pre_scp_fix_20260719_1540` (4.364 B, sanitizada) | chmod +x; `bash -n` OK; dir remoto `/home/ubuntu/cafezinho/Projeto Cafezinho Agentes` existe; `mail` presente no Tencent. Telegram segue guardado por `TELEGRAM_BOT_TOKEN` ausente (graceful) |
| 3 | `Outros/Jornais do dia/jornaisdodia.sh` | git `d971fcd0` (712 B) | Idêntico ao comportamento do log (rclone copy --include "*.pdf" --ignore-existing → `gdrive:Jornais do dia`). chmod +x; `bash -n` OK. PDFs continuam chegando na pasta (últimos: edições 27/07) |
| 4 | `scratch/limpa_diario.sh` | git `d971fcd0` | chmod +x; `bash -n` OK |
| 5 | `scratch/backup_reforma_local.sh` | git `d971fcd0` | chmod +x; `bash -n` OK (b2 sync; refs legadas `A_GRANDE_REFORMA_LOCAL_20260610` falham graciosamente) |

Não executado: nenhum dos scripts foi disparado manualmente (evitar custo/envio fora de hora); próximas rodadas naturais: jornais 12:00, youtube_cafezinho --rodada 14:00, baleia 18:00.

### 3.4 Sentinela — estado real e migração (diagnóstico que estava vencido)

- **Desligamento intencional:** crons do loop comentados 27/07 ~16:15–17:15 BRT por ordem Miguel (execução Claude Code; backup `/tmp/crontab_backup_pre_desliga_sentinela_20260727_161554.txt`). Tags canal: `[SENTINELA-DEEPSEEK-PUBLISH-OFF] 2026-07-27 17:15 BRT`. Último ciclo `20260727_1600` em `ferramentas/sentinela/logs/ciclos.jsonl` (507 ciclos totais). Agregador 23:55 segue ativo (28/07: "nenhum ciclo, nada a fazer" — correto).
- **Novo papel:** análise (relatórios), sem publish (publish = Opus + Haiku observador). Fonte: `Foruns/forum_kimi_diagnostico_infraestrutura_autocura_20260727.md` §3.8 + cartinha `cartinha_kimi_diagnostico_infraestrutura_20260727_1615.md`.
- **Opções:** A) Local — acoplamento fácil c/ Opus, mas morre c/ PC e consome RAM · B) NYC — 24/7; comunicação bidirecional via git sync (reuso do cron cerebro→GitHub 30min; opção b1 do Claude) · C) Híbrido. **Recomendação entregue: B (NYC)** — análise tolera latência de 30min; PC do Miguel alivia RAM; NYC já sustenta 32 crons. Pendentes associados: estudo de RAM (§3.8-c) e deploy de `sentinela_tematicos_cron.sh` (§3.7). Sem evidência de sentinela_ciclo.py em NYC/Tencent ("NÃO propagado" — `CEREBRO_NODE_ATUALIZACOES.md`, bug #37). **Decisão final: Miguel.**

### 3.5 Bot Telegram pendente de rotação — identidade completa

- **Bot:** Augusto — `@cafezinhoantigravitybot` ("CEO Antigravidade", bot ID 8778689199), chat privado Miguel `1894890759`. Prova: emissor antigo `.bak_pre_nyc_20260710_190740` tinha token hardcoded c/ mesmo prefixo numérico documentado como `TELEGRAM_TOKEN_AUGUSTO` em `CEREBRO_NODE_COMUNICACAO.md` e `CEREBRO_NODE_BUGS_RESOLVIDOS.md` §D4.
- **Motivo:** token exposto em claro nos scripts do Baleia Azul; sanitização Codex 17/07 (`forum_correcao_baleia_azul_cctv_envio_duplicado_20260717.md`; reconfirmado 19/07 na `carta_transferencia_baleia_azul_codex_claude_20260719.md` e `CEREBRO_NODE_BALEIA_AZUL.md`). Pendência canônica data de **17/07** (não 26/07).
- **Estado:** emissor restaurado espera `TELEGRAM_BOT_TOKEN` do ambiente; `.env.unificado` local tem apenas `TELEGRAM_TOKEN`, `TELEGRAM_TOKEN_AUGUSTO`, `TELEGRAM_TOKEN_ZIZI`, `TELEGRAM_TOKEN_MILLER` (sem `TELEGRAM_BOT_TOKEN`) → envio segue suspenso por design (warning no log).
- **Ação (só Miguel):** BotFather → `/revoke` → novo token → gravar `TELEGRAM_BOT_TOKEN` no `.env.unificado` local e `/root/.env.unificado` (Tencent) + opcionalmente atualizar `TELEGRAM_TOKEN_AUGUSTO`. Regra permanente: nunca gravar token em script, fórum, boletim ou log.

---

## 4. RECOMENDAÇÕES ENTREGUES (aguardando decisão/aprovação do Chairman)

1. Rotacionar token Augusto (BotFather) — destrava Telegram do Baleia.
2. Documentar valores dos fixos: Kimi Coding Max, Claude Max, DigitalOcean, Tencent, ServerDo.in.
3. Sentinela → NYC (recomendado) — comunicação via git sync 30min.
4. Curador Cafezinho na cascata multi-provider do `nucleo_llm` (fim da heurística por conta suspensa).
5. Revisar GLM Coding Max US$ 144/mês antes de 17/ago (622M tokens usados → se paga SE a quota for usada).
6. Avaliar consolidação dos 4 droplets DO (Rio Carta ×2).
7. Instrumentar `usage`→banco_custos no `nucleo_llm.py` local (fecha lacuna de telemetria dos temáticos; ~1 tarde de trabalho).
8. Alerta Telegram "custo/dia > cap" (já no roadmap da telemetria; ausência dele permitiu os US$ 380 do motor_coletor).
9. Prevenção de deleções: commitar scripts vivos de cron no git (HEAD atual não os rastreia).
10. Migrar endpoint Prometheus (estava no Alibaba, agora legacy) ou desligar pushers.

## 5. CUSTO DESTA AUDITORIA (transparência)

Sessão interativa ZCode/Kimi (assinatura, não paygo) + 3 subagentes de exploração (~3,9M tokens de quota de assinatura). Chamadas paygo: 1 teste kimi-k3 (96 tokens, desprezível). Nenhum outro custo API.

---
## 6. CORRIGENDA 2026-07-29 12:05 BRT — Token Augusto válido; causa raiz = nome de variável

**Contestação do Chairman:** "tenho certeza que o Augusto token NÃO precisa rotacionar, ele estava funcionando até ontem". Verificação completa (ele estava certo):

**Inventário de credenciais Telegram** (`.env.unificado` local, mtime 27/07 04:42; 10 tokens, todos 46 chars): `TELEGRAM_TOKEN` (prefixo 877868919…) · `TELEGRAM_TOKEN_AUGUSTO` (prefixo 877868919… — **mesmo bot**) · `TELEGRAM_TOKEN_ZIZI` · `_MILLER` · `_GABRIEL` · `_MUNDO_TRILHOS` · `TELEGRAM_MAURA_FIXED_TOKEN` · `TELEGRAM_BOT_SECRETARIA_TOKEN` · `TELEGRAM_TOKEN_MAYRA_PRAIA` · `TELEGRAM_TOKEN_MAPARIO_MAIRA`.

**Testes ao vivo (API Telegram):**
1. `getMe` c/ `TELEGRAM_TOKEN_AUGUSTO` → `{"ok":true,"result":{"id":8778689199,"first_name":"CEO Antigravidade","username":"cafezinhoantigravitybot",...}}` — TOKEN VÁLIDO.
2. `getMe` c/ `TELEGRAM_TOKEN` → mesmo id 8778689199 (variável duplicada do mesmo bot).
3. `sendMessage` real ao chat `1894890759` (Miguel) → **entregue, `message_id` 5052** (~12:04 BRT).
4. Token vazado de 17/07: valor sanitizado dos `.bak` (grep sem matches) → comparação de valores impossível; funcionalmente irrelevante: o token ATUAL funciona.

**Causa raiz definitiva do silêncio Telegram do Baleia (17/07→29/07):** o script lia `${TELEGRAM_BOT_TOKEN}` — variável **inexistente** no `.env.unificado`. A credencial válida existia sob `TELEGRAM_TOKEN_AUGUSTO` e `TELEGRAM_TOKEN`. Ou seja: bug de NOME DE VARIÁVEL introduzido na sanitização de 17/07, não credencial morta. A "rotação pendente" dos registros era recomendação de segurança que se fossilizou como bloqueio.

**Fix aplicado em `scratch/enviar_baleia_azul_v2.sh` (12:05):**
```bash
TG_TOKEN="${TELEGRAM_BOT_TOKEN:-${TELEGRAM_TOKEN_AUGUSTO:-${TELEGRAM_TOKEN:-}}}"
```
Verificações: `bash -n` OK; cascata testada com `.env.unificado` sourced → resolve token prefixo 877868919… (46 chars). Próximo envio real: **18h de hoje**.

**Lição registrada:** sanitização de segredos deve SEMPRE manter o caminho funcional da credencial (renomear var exige atualizar TODOS os consumidores; checklist de consumers antes de declarar "suspenso até rotação"). Rotação no BotFather permanece como higiene opcional (decisão Miguel), não bloqueio.

---
## 7. PARTE 3 — Log técnico 01/08 (vigia ativo, fiscal corrigido, escalada de imagens, unificação de threads)

### 7.1 Vigia de custos 30min (criado 30/07 20:09, cron `*/30` tag `VIGIA_CUSTOS_BALEIA_20260730`)
- Script: `~/bin/vigia_custos_baleia.sh`. Fontes: consolidados NYC via ssh + `/user/balance` DeepSeek + arquivos locais (edição Baleia, log de envios).
- Condições: ontem > US$ 5 (cap Maestro) · ontem > 1,5× média 7d · fiscal não rodou (após 9h) · edição ausente (após 8h) · nenhum envio no dia (após 19h) · **saldo DeepSeek < US$ 2** (01/08, 1×/dia após 08h). Anti-spam: 1×/dia/condição (`/tmp/vigia_custos_alertas.state`). Log: `~/log/vigia_custos.log`.
- Alertas reais já disparados: 30/07 (anomalia + edição + envio), 31/07 (edição), 01/08 (edição + cap; falha ssh transitória 10:00, recuperada 10:30).

### 7.2 Fix do fiscal 7d/30d (aplicado 01/08 ~10:50, produção NYC)
- Backup: `/root/augusto_fiscal_tokens.py.bak_pre_fix_7d30d_20260730`.
- Patch autocontido: função `_soma_consolidados(dias)` dentro de `gerar_auditoria_matinal()` soma os `por_dia` dos JSONs diários; substitui as chamadas `load_or_collect(root, ontem, 7|30)` que não agregavam. Biblioteca compartilhada `custos/gerar_relatorio_financeiro.py` NÃO tocada.
- Verificação sem envio: relatório gerado com ontem US$ 6,40 · 7d US$ 26,58 · 30d US$ 455,50 (coerente com a série diária). Relatório das 08h (cron) já saiu correto no Telegram do Miguel.

### 7.3 Escalada de custo de imagens (28/07→01/08)
- Série: 28/07 US$ 2,41 (48 imgs) · 29/07 US$ 4,09 (93) · 30/07 US$ 9,22 (397) · 31/07 US$ 6,40 (~180) · 01/08: US$ 5,41 às 13:07 UTC / US$ 5,68 às 14:07 UTC (189 imgs; ritmo caiu p/ ~6/h no fim do dia — onda arrefecendo).
- Driver: `gerador_imagem_editorial` (fal-ai ~US$ 0,035/img) + `v4_prompt_visual` 1:1. Hipótese dominante: backfill da onda V4 Regional (27 UFs) + regeneração de heroes (regra "sem texto" 29/07) — sessões paralelas. Correlato: inbox Claude→KimiDesktop 31/07 ("8 posts agendados falharam por falta de featured_media").
- Governança da resposta: parecer Codex 13:40 (opção c — observar 24h) + critérios de promoção p/ cap reversível de 60 imgs/dia (>60 imgs/dia, ou >US$ 5/dia, ou 401 reaparecer). **Aceito por ZCode; verificação agendada: consolidado 02/08 02:07 UTC.**

### 7.4 Chave Kimi vision — causa raiz e fix (01/08 11:20–11:45)
- Sintoma: `[visual_judge] kimi_vision_http_401` em 100% dos julgamentos → fallback pago Qwen-VL/qwen-max.
- Cadeia: worker lê `os.environ["KIMI_VISION_API_KEY"]` (cron faz `. /root/chaves.sh`); endpoint no código correto (`api.kimi.com/coding/v1`); **NYC tinha a chave velha** `sk-kimi-4K…` (72ch) em `chaves.sh` e `.env.unificado`; cofre local tinha a válida `sk-kimi-xQ…` (teste 200).
- Fix: sincronização por stdin pipe (sem eco do segredo), backups `chaves.sh.bak_kimi_vision_20260801` + `.env.unificado.bak_kimi_vision_20260801`; teste de endpoint a partir do NYC: **HTTP 200**; ciclos reais pós-14:20 UTC com **zero 401s** (nacional 14:22, geopolítica 15:30).

### 7.5 Curador Cafezinho — cascata + flash (decisões Miguel 01/08)
- Implementação (`youtube_cafezinho.py`, backup `...bak_curador_cascata_20260801`): cascata `deepseek` → `kimi-k3` paygo → heurística; configs `deepseek_primeiro` (default true), `model_deepseek` (default `deepseek-v4-flash` desde 14:30 — Miguel aprovou; flash = 3× mais barato que o alias Pro, preços validados ao vivo).
- Testes reais: deepseek-chat (nota 8) e deepseek-v4-flash (nota 8,5) ranquearam corretamente; kimi-k3 fallback testado 200 em 29/07 e 01/08.
- Custo estimado do curador: ~US$ 0,15/mês (antes ~US$ 3/mês em kimi-k3).

### 7.6 Saldo DeepSeek — mistério da recarga (aberto)
- Medições (`/user/balance`, chave `fe52ae94` — idêntica local e NYC): 11:55 US$ 1,21 → 15:05 US$ 1,20 → 14:30 US$ 1,15. **Recarga afirmada por Miguel (~14h, "a beça") não visível.** Miguel afirma ter conta única → hipóteses: pagamento em processamento (boleto 1–2 dias úteis) ou recarga feita em outra plataforma (OpenRouter/Assembly). Aguardando método/hora/comprovante. Roteador V4 deu `quota_exhausted cooldown 219min` em 01/08 ~13:52 UTC (coerente com saldo baixo).
- Vigia cobre esse saldo 1×/dia (< US$ 2 → Telegram).

### 7.7 Unificação de threads (ordem Miguel 01/08)
- Esta memória/fórum (auditoria) ↔ `Foruns/forum_unificacao_cofre_chaves_20260801.md` (CHECKUP-005, fingerprint 96 vars, plano 5 fases) passaram a se referenciar: Adendo 4 aqui; §6 lá. Insumos entregues ao Cofre Único: winner `KIMI_VISION_API_KEY=sk-kimi-xQ…`; órfão `KIMI_PAYGO_API_KEY` (kimi_paygo.env); dependências novas do curador; alerta saldo DeepSeek.
- Resposta ao Codex postada (Adendo 4 + ACK `inbox_trindade/kimi.md` 14:10): zero 401/fallback pós-fix; 189 imgs; US$ 5,68 @14:07 UTC; ritmo ~6/h.

---
*Memória registrada conforme Regra do Tema Duplo (par: Fórum de decisões). Catalogação: `CEREBRO_NODE_TELEMETRIA.md` + `CEREBRO_NODE_ATUALIZACOES.md`.*
