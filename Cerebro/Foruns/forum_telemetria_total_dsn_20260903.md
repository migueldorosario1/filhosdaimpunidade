# 🤖💰 Fórum — Telemetria TOTAL de custos nos robôs DSN (03/09/2026)

> **Ordem do Miguel (03/09 ~07:15, voz):** "Telemetria em TUDO — todos os DSN, todos os robôs, todas as coletas. O DSN Finanças acompanha tudo e manda relatório toda hora na ronda dele. Depois: análise de onde economizar SEM mexer no luxo da redação. Não muda modelo nenhum por enquanto."
> **Ordem 2 (~08:3x):** bot próprio criado — @Dsnfinancas_bot; "tudo tem que estar no painel de custos ao vivo do CCTV e todos os agentes listados na página agentes".

## Estado: o que está pronto

### Telemetria por evento — cobertura FINAL
| Robô / servidor | Como ficou |
|---|---|
| ds_youtube (Tencent) | ✅ patch na chamada DeepSeek (texto corrigido) |
| dsn_revisor1 + dsn_revisor2 | ✅ patch único no `_req_json` (cobra GLM/xAI/DeepSeek/OpenAI) — R2 PROVADO no painel ($0.22 na 1ª hora) |
| ds_nuvem_chefe (escuta) | ✅ patch após resposta DeepSeek |
| Maíra (maira.service) | ✅ patch com sudo em /usr/local/bin/maira_bot.py |
| Rondas dsh (Chefe */30, Ideias 30/30) | ✅ coletor NOVO `dsn_financeiro/dsh_telemetria_colhe.py` — lê sessions zstd do dsh, data REAL do evento, corr_id (dedup), cache com desconto 26%; hooks no fim das 2 rondas .sh |
| dsn_publicador | ✅ já estava (parado por contrato) |
| dsn_imagem / olho_apurado / auditor gráficos v42 (NYC) | ✅ 1 patch na factory `media_vision_providers.py` (qwen+deepseek+gemini; agente identificado por sys.argv[0]) |
| redator v42 economia (NYC) | ✅ patch em `chamar_llm` |
| V4.1 inteiro + materializador youtube_v2 | ✅ já cobertos pelo `agente_roteador_llm` (registrar_gasto) |
| cicero + gsn — temáticos 159 | ✅ mini-`gerenciador_tokens.py` fail-never instalado + roteadores reativados (estavam DESLIGADOS de propósito) + ponte `cicero_gerenciador_tokens`; rsync 1min já apontado |
| Robôs coletores V4.1 / pulse / radar | ✅ sem LLM (heurístico) — nada a medir |
| Áudio (Groq STT Maíra, AssemblyAI escuta) | ⚠️ lacuna ANOTADA na cobertura (cobrança por minuto, fase 3) |
| Escritório Dell (DSH us65) | ⚠️ mesma chave DeepSeek → coberto pela âncora de saldo (separação exige chave própria — decisão Miguel) |

### Defeitos estruturais achados e curados no caminho
1. **Dedup do DSN-F colapsava registros sem corr_id** (id(r) reutilizado + mesma data) — cura: coletor dsh grava corr_id=sha1 + data real do evento.
2. **Cache DeepSeek superestimado** (cacheRead somado como input full) — cura: `telemetry_log.log_tokens(cache_read_tokens=)` com fator 0,26× ($0,07/1M).
3. **_telegram do DSN-F nunca tinha funcionado** (procurava TELEGRAM_BOT_TOKEN; o env tem TELEGRAM_TOKEN) — cura; e agora lê **TELEGRAM_TOKEN_DSN_FINANCAS** do cofre (bot próprio, fallback ao antigo). Envio provado (2 mensagens de estreia).
4. **Apagador misterioso de jsonl** (mesmo do incidente 02/09) comeu o banco_custos_tencent ~08:0x — cura estrutural: self-heal do DSN-F agora guarda snapshot do banco tencent e restaura se sumir/encolher.
5. **Bot próprio:** token gravado nos 3 cofres (Dell ×2 + Tencent) com backup+hash sha8=1bbc9514 — Regra 4 cumprida sem exibir valor.

### DSN Financeiro — agora reporta "toda hora"
- Ronda */15 no canal (como antes) + **Telegram 1×/hora na 1ª ronda da hora** via @Dsnfinancas_bot (resumo: 7d real, top-4 agentes, saldo DeepSeek, link do painel).
- Relatório diário completo segue saindo após 06:30 + vai pra Baleia Azul.

### Painel CCTV
- `/custos/ao-vivo` e `/custos` 200 OK; agentes novos já aparecem com custo real (dsn_ideias, dsn_revisor2, youtube_v2_materializador na 1ª hora).
- Página `/agentes`: família DSN já listada com "Gasto 7d" real por cartão. **Faltando: v42 economia, olho apurado, youtube_v2, cicero/gsn — patch em curso nesta sessão.**

## Análise de gastos (7d, DSN-F ronda 73): total US$ 41,26
| Quem | Modelo | US$ 7d | Leitura |
|---|---|---|---|
| v4_1_redator | gpt-5.5 | 25,39 (62%) | 🔒 REDAÇÃO ULTRA-LUXO — intocável por ordem |
| dsn_chefe_ronda | deepseek-chat | ~14,5/dia medido no nascimento (2h20) | 🔴 MAIOR CENTRO DE CUSTO FORA A REDAÇÃO — ronda faz ~150 chamadas/vez; âncora de saldo sugere ~$20/dia no pool; refino de medição em curso |
| Repetidor_Estatal | **gpt-4o** | 5,06 | 🔴 SUPER LUXO p/ tarefa mecânica — troca por deepseek-chat/glm-5-turbo economiza ~$21/mês |
| v4_1_ciclo | glm-5-turbo + sonnet + sol | 6,09 | 🟢 já econômico na curadoria; sonnet = decisão editorial (nacional) |
| agente_comentarista | gpt-4o-mini | 1,65 | 🟡 ok; descer p/ glm-5-turbo pouparia ~$6/mês |
| tribunal_visual | qwen3-vl | 0,17 | 🟢 barato |
| v42/youtube/imagem | vários | < 0,8 | 🟢 centavos |

## O que falta
1. Patch da página `/agentes` (v42, olho, youtube_v2, cicero/gsn) — em curso.
2. Decisão do Miguel sobre as 2 trocas recomendadas (Repetidor Estatal gpt-4o→econômico; cadência/contexto da ronda do Chefe).
3. Fase 3: medidor de áudio (Groq/AssemblyAI) por minuto.
4. Vigilância 24h do banco do 159 (nasce na próxima rodada do cicero, minutos 0/30).

**Rollback de tudo:** cada arquivo tem `.bak_pre_telemetria_dsn_20260903` (e _f3/_f4/_f5/_f6 no DSN-F); coletor dsh = apagar 1 linha no fim das 2 rondas; 159 = restaurar 2 .bak e apagar 2 módulos novos.


## ADENDO 08:5x — ordens do Miguel executadas/respondidas

1. **"os DSN/DS em geral não entram na medição?"** — ENTRAM: todos os DSN da nuvem foram instrumentados nesta sessão (chefe/ideias/revisores/Maíra/YouTube/publicador) e já aparecem no painel. O que NÃO separa: os DS do escritório (us65/celular) por dividirem a MESMA chave DeepSeek dos robôs — a âncora de saldo cobre o total; a separação exige chave própria (decisão do Miguel; código do reporter_us65 já está pronto, flag REGISTRAR_BANCO).
2. **"descer o Repetidor Estatal p/ deepseek-chat"** — ✅ APLICADO 08:47 (NYC `agente_repetidor_estatal.py`, `.bak_pre_repetidor_ds_20260903`): ranker + reescrita tentam deepseek-chat forçado; fallback = cascata econômica (nunca sem LLM). Smoke test deepseek-chat respondeu OK com custo registrado. Economia estimada ~US$ 21/mês.
3. **Tese e curadoria — quem faz e com qual modelo:** TESE = frontier gpt-5.6-sol (ultra-luxo) lendo LINHA EDITORIAL + MANUAL desde 02/09 (já é o topo); fallback GLM→DeepSeek→Moonshot. CURADORIA/verificações intermediárias = glm-5-turbo (815 chamadas, US$ 2,70/7d) — é o triador braçal: classifica/ranqueia/checa formato, NÃO editorialista. **Opção de subida (aguarda "vai"):** curadoria de importância/ângulo → deepseek-chat ou glm-5.3 = +~US$ 15/mês; tese segue frontier.


## ADENDO 2 (08:5x) — "vai" do Miguel: CURADORIA SUBIU p/ deepseek-chat
- ✅ APLICADO: `_verifier_llm_json` (NYC `v4_vertical_draft_worker.py`, `.bak_pre_curadoria_ds_20260903`) ganhou ESTÁGIO 0 com **deepseek-chat** — a curadoria/verificação do V4.1 e o tribunal diário agora pensam primeiro com DeepSeek V3; cadeia antiga (GLM→DS→Kimi) intacta como fallback; modelo trocável pela env `V4_CURADORIA_MODEL` sem deploy.
- Prova E2E: smoke `curadoria_smoke | deepseek | deepseek-chat | ok` no ledger de telemetria.
- Resposta ao Miguel: sim, deepseek-chat é melhor que glm-5-turbo para julgamento editorial (instrução complexa, PT-BR formal, raciocínio de ângulo); turbo segue como fallback barato. Custo estimado da subida: +US$ 12–15/mês (de $2,70 p/ ~$6/7d na curadoria).


## ADENDO 3 (09:0x) — cascata da curadoria conforme ordem + chave Mistral
- ✅ CASCATA NO AR no `_verifier_llm_json`: **deepseek-chat → glm-5.3 → mistral-large-latest → kimi-k3**; se os 4 falharem, a cadeia antiga (GLM-turbo → DS-pro → kimi-k2.5) segue de última linha. Loop enxuto, telemetria por estágio, envs `V4_CURADORIA_MODEL{,_GLM,_MISTRAL,_K3}` trocam modelo sem deploy. Smoke provado: respondeu via deepseek-chat.
- 🔴 **MISTRAL SEM CRÉDITO:** 3 chaves diferentes nos cofres (Dell sha8 2a8d35f0, Tencent 3892c1d7, NYC f0b8581f); NYC=401 (morta), Tencent=402 (chave VÁLIDA, conta sem billing). O estágio Mistral fica na cascata e falha rápido; quando o Miguel recarregar no console.mistral.ai ele volta a valer sozinho. glm-5.3 testado OK; kimi-k3 existe (429 agora = limite da conta Moonshot, não erro de nome).
