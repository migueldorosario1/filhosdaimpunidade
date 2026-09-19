# 🚨 FÓRUM — PLANO DE EMERGÊNCIA 4 NÍVEIS DE USO + APLICAÇÃO DO PLANO MÍNIMO (11/09/2026)

**Ordem do Miguel (11/09 ~09:4x):** pausar agente YouTube (exceto Cafezinho canônico), pausar todos os temáticos, pausar TODAS as rondas DSN (Chefe, DS Miguel, ideias) e os revisores R1/R2; aplicar as chaves DeepSeek novas (canônica primeiro, com telemetria restrita); criar plano de emergência em 4 níveis que saiba PARAR e VOLTAR sem acúmulo nem desorientação das funções invisíveis; **mudar para o Plano Mínimo AGORA**; caçar fio desencapado.
**Executor:** ZCode/GLM-5.3 · ref **ZM-20260911-EMERGENCIA** · Tema Duplo com `Memorias/memoria_plano_emergencia_4_niveis_20260911.md`.

---

## 1. Os 4 níveis (definição canônica)

| Nível | Posts/dia | O que roda | Cadências-chave |
|---|---|---|---|
| **PRO** | 20-30 | tudo como era: fábrica todos os verticais (geo horária, ciência 12×/d etc), revisores 1×/h, rondas DSN 4/4h (flash), youtube canônico + espelho GSN, temáticos, auditor de títulos, manchete | original dos backups `.bak_pre_plano_minimo_20260911` |
| **BÁSICO** | 5-6 | fábrica 4-6 ciclos/dia (nacional + 2-3 verticais), revisores 1×/h, rondas DSN 4/4h, youtube canônico 2×/d, temático cicero 1×/2h | modelos baratos (flash), sem validador/test-api |
| **MÍNIMO** ⬅️ **ATUAL** | 2-3 | SÓ: fábrica geral 07:25+19:25 e economia 13:35 (com guard kill), youtube do canônico, publicador, dsn_imagem (capas), autocura fila, telemetria/vigia/financeiro, coletores SEM LLM (pauta pronta p/ volta) | verticais secundários + v42 ciclo + rondas DSN + revisores + temáticos + players COMENTADOS/flags |
| **ZERO** | 0 | fábrica kill-flag `v41_ciclo.pause`, youtube canônico off; SOBE SEMPRE: site, backups, telemetria, vigia P11, financeiro, publicador (drenagem), sincronizações | `plano_uso.sh zero` |

**Sobe/desce:** `ssh tencent '/home/ubuntu/bin/plano_uso.sh {status|pro|basico|minimo|zero}'` — comandam o Tencent por flags `.pause` (com histórico em `v6_data/controles/plano_uso_historico.log`) e imprimem o checklist exato de NYC/Dell/159. Backups de religação: NYC `/root/crontab.bak_pre_plano_minimo_20260911` · tencent ubuntu `~/crontab.bak_pre_plano_minimo_20260911` · tencent root `/root/crontab.bak_pre_plano_minimo_20260911` · 159 `/root/crontab.bak_pre_plano_minimo_20260911` · Dell `~/crontab.bak_pre_plano_minimo_20260911`.

## 2. O que foi pausado AGORA (Mínimo aplicado, com provas)

- **Tencent (flags em `v6_data/controles/`):** dsn_chefe, dsn_ideias, dsn_youtube, alimentador_yt (ganhou guard novo), dsn_revisor1, dsn_revisor2, cafezinho_hourly (temático), v41_player, v42_investimento — guards provados (cron pula com flag). Ficam LIGADOS: dsn_publicador, dsn_financeiro, vigia P11, coletor_nacional (sem LLM), moka/farol/lumina/telemetrias.
- **NYC:** v41_ciclo geral `*/2`→`25 7,19` e economia `1-23/2`→`35 13`, ambos com guard `[ -f /root/controles_pause/v41_ciclo.pause ]` (botão-kill do Zero); COMENTADOS: 7 verticais (ciência, geo, meio-amb, esporte, saúde, digital, cultura) + ciclo v42 publicador; flags `/root/controles_pause/`: comentarista, auditor_titulos, manchete, repetidor_estatal, media_promoter, media_expander, cicero_tematicos; comentado `agente_validador_modelos` (fio). Ficam LIGADOS: dsn_imagem (capas), autocura_fila (ordem Miguel: feira nunca vazia), youtube_v2_pipeline + ingestor DSN (canônico), v42 coletores/ingestor (dados, sem LLM), tendencias_intake, SEO/GSC/GA4/índices, autocura saúde, fiscal_tokens.
- **Dell:** ronda_30min (DS Miguel) e consumidor_gsn_fila COMENTADOS (tag `# PAUSA_PLANO_MINIMO_20260911`). LIGADOS: youtube_cafezinho (canônico — ordem), sync_youtube_painel, boletim de custos, jornaisdodia (sem LLM direto), todas as sincronizações Cérebro/Drive.
- **159 (temáticos):** cicero_cron_rotativo (2 janelas) + cicero_remote_publish COMENTADOS; indexador Google segue (sem LLM).

## 3. Chaves DeepSeek novas (Regra 4 cumprida — valores NUNCA aqui, só sha8)

- **Canônica (sk-a20c…, sha8 2b0569ed):** APLICADA em `/root/chaves.sh` + `/root/.env.unificado` do NYC e nos cofres do Dell (`Projeto Cafezinho Agentes/root/.env.unificado` ⇄ `Outros/chaves/agentes_labs/.env.unificado`) — todos com `.bak_pre_chave_ds_20260911`. Provada: chat flash RESPOSTA OK.
- **DSN (sk-3d49…, sha8 f5ee9259):** gravada no Tencent (`~/.dsh/deepseek_env` + `~/.env.unificado` ubuntu) e espelhada nos cofres do Dell como `DEEPSEEK_API_KEY_DSN` — robôs DSN estão PAUSADOS, nada gasta; religação já nasce com a chave certa.
- **As duas chaves são da MESMA conta** (saldo único: **US$ 4,25** às 09:49 — o vigia lê e confere). As velhas (****806b/****8762) morreram por regeneração do Miguel; ficam só nos `.bak` (deprecadas de fato).
- **Telemetria restrita (ordem "cuidado muito restrito"):** vigia P11 (*/15) agora lê o saldo da chave ATIVA (patch `DEEPSEEK_API_KEY_VIGIA` primeiro; prova "verde: saldo 4.25" 09:49:46) + DSN-F 2×/dia + boletim de custos 2×/dia + telemetria por evento da fábrica. Nenhuma LLM de vigilância.
- ⚠️ **SALDO BAIXO (US$ 4,25):** no ritmo Mínimo (~US$ 1-3/dia) cobre 1-4 dias — recarregar é a próxima ação do Miguel.

## 4. Fios desencapados encontrados e cortados (auditoria completa)

1. 🔴 **`monitor_chaves_api.py --test-api` (tencent root, */15):** fazia chamada LLM REAL em cada chave de cada provedor — 96×/dia de gasto invisível. `--test-api` REMOVIDO do cron (monitor segue sem gastar).
2. 🔴 **`agente_validador_modelos.py` (NYC, 3h/dia):** chamadas reais de teste em OpenAI/xAI/Mistral — comentado no Mínimo.
3. 🔴 **transcriber Transkriptor (US$ 6/tacada):** protegido por tabela — ds_youtube + alimentador pausados (ninguém encomenda transcrição de 1h). Volta só do Mínimo p/ cima com cap (proposta pendente do fórum do freio).
4. 🟡 **geo 24×/dia + ciência 12×/dia** (ordem de 09/09): pausadas no Mínimo — ao voltar para PRO, revisar se a geo horária compensa o custo (era pós-boost Irã/China/guerra).
5. 🟢 conferido sem gasto: radar_tendências (sem LLM), jornaisdodia (sem LLM direto), boletim (sem LLM), prometheus/farol/lumina/moka (free/sem LLM).

## 5. PARAR sem acúmulo e VOLTAR sem desorientação (a inteligência do plano)

- **Sem acúmulo:** produtores pausados = filas param de CRESCER (ds_youtube/transcrições não enfileiram; coletores SEM LLM seguem enchendo o banco de pautas a custo zero — matéria-prima pronta para a volta; envelopes v42 idem). Crons têm `flock` → pausa longa não vira cascata de execuções atrasadas ao religar. Publicador segue vivo → nada de rascunho represado.
- **Sem desorientação:** (a) flags `.pause` carregam nível+data (quem pausou e por quê); (b) `plano_uso.sh status` dá o estado em 1 comando; (c) histórico auditável `plano_uso_historico.log`; (d) AVISO À CASA publicado na ponte `de_dell.md` (agentes não estranham rondas silenciosas nem "somem" com o Chefe); (e) este fórum + monitoramento carregam o estado da missão; (f) vigia P11 continua lendo saldo → queda anômala dispara Telegram mesmo em Mínimo.
- **Voltar:** 1 comando por nível (`plano_uso.sh`) + checklist impresso + backups de crontab datados. Zero é o único nível que mexe na fábrica viva (flag kill).

## 6. O que aconteceu / o que falta / o que preciso de você (Miguel)

- **Aconteceu:** Mínimo 100% aplicado e provado nos 4 hosts; chaves novas aplicadas (canônica ativa e provada; DSN pronta nos cofres para religação); 2 fios de gasto invisível cortados; transcriber blindado; vigia de saldo de volta (verde 4.25); plano 4 níveis com mecanismo de troca e religação documentada.
- **Falta:** provar 1º ciclo da fábrica mínima hoje 13:35 (economia) e 19:25 (geral) — conferir 2-3 posts/dia e telemetria registrando a chave nova; no BÁSICO/PRO futuros, decidir cap do transcriber e retorno da geo horária.
- **Preciso de você:** (1) RECARREGAR DeepSeek — US$ 4,25 cobre 1-4 dias de Mínimo; (2) confirmar se mantemos Mínimo por quanto tempo; (3) ao subir de nível, dizer só "sobe para básico/pro" que o plano_uso executa.

---

## 7. ADENDO ~10:4x — trocas de FRONTIER no Mínimo (ordem Miguel) + pesquisa de preço

- **Nacional (frontier Anthropic): claude-fable-5 → claude-sonnet-4-6.** Fonte da verdade: `contratos/v4_rotas_llm_limpas_v1.json` (contexto `v4_ultra_luxo_redacao_nacional`, degrau anthropic_luxo). O "fable" era o topo de luxo do ULTRA_LUXO de 02/09.
- **Geral (tese/redação/curadoria): gpt-5.6-sol → gpt-5.5 no topo** (contexto `v4_ultra_luxo_redacao`; sol rebaixado a 2º degrau de emergência). Contextos normais já eram gpt-5.5.
- **Pesquisa de preço (pedido "ver se é mais barato mesmo"):** gpt-5.5 e gpt-5.6-sol têm a MESMA tabela (US$ 5/30 por 1M) — MAS o Sol cobra taxa de cache-write de US$ 6,25/1M e há relatos de menor eficiência de tokens (mais tokens pela mesma tarefa = conta real maior). Conclusão: 5.5 não é mais barato NA TABELA, mas tende a sair mais barato NA CONTA REAL. Alternativas realmente mais baratas para considerar no futuro: gpt-5.6 Terra (US$ 2,5/15) e Luna (US$ 1/6). Fontes: OpenAI pricing, CloudZero, Aireiter (links na memória).
- Provas: seleção nacional = anthropic/claude-sonnet-4-6; economia redação+curadoria = openai/gpt-5.5; assert do teste de contrato atualizado e PASSANDO; bateria 238/72 idêntica ao backup (72 falhas pré-existentes de fixture, ex.: "deepseek-v4-pro" em v4_vertical_redactor_runtime.py). Backups: `.bak_pre_plano_minimo_20260911` em llm_providers.json, v4_rotas_llm_limpas_v1.json e test_contracts.py (todos NYC). Rollback = restaurar os 3.
- Arquivos tocados: `config/llm_providers.json` (topos luxo: sonnet / gpt-5.5), `contratos/v4_rotas_llm_limpas_v1.json` (as duas filas ultra_luxo), `contratos/mapa_v4_contexto_llm.json` (nota sem anacronismo), `codigo/test_contracts.py` (assert sonnet, linha 1283).

## 8. 📝 ANOTAÇÕES PARA A VOLTA AO PRO — desperdícios a cortar (ordem Miguel "anota tudo isso")

1. **geo 24×/dia + ciência 12×/dia** — cadências altíssimas herdadas (boost Irã/China/guerra de 09/09): no PRO, avaliar geo 6-12×/dia e ciência 4-6×/dia.
2. **`monitor_chaves_api --test-api`** — NUNCA religar: 96 chamadas LLM reais/dia invisíveis (uma por chave ativa). Monitor sem teste segue completo.
3. **`agente_validador_modelos`** — testes reais diários: religar no máximo 1×/semana, ou sob demanda.
4. **Transcriber Transkriptor** — antes de religar ds_youtube/alimentador: cap de US$/dia (sugestão US$ 3) + só vídeo ≤30 min (a tacada de US$ 6 foi vídeo de 1h).
5. **gpt-5.6-sol** — manter fora do topo (taxa cache-write + ineficiência); luxo OpenAI no PRO vale avaliar gpt-5.6 Terra (2,5/15, metade do preço do 5.5).
6. **claude-fable-5** — rebaixado fora da fila; religar só com ordem explícita do Miguel.
7. ✅ **FEITO 11/09 11:4x** (vai do Miguel: pode mudar sim, dentro do Mínimo) — deepseek-chat → deepseek-flash nos 8 .py vivos da fábrica NYC (v41_ciclo ×2, redator_economia_v4, repetidor_estatal ×6, media_expander, gerador_imagem, painel_despesas, fiscal_tokens, roteador_llm; backups .bak_pre_flash_20260911, py_compile OK, 0 restantes). **🔁 REGRA DE VOLTA (ordem Miguel): quando voltar ao PRO, o 1º degrau volta a deepseek-chat nos 8 arquivos** (o plano_uso.sh pro imprime este lembrete; Básico mantém flash). **Mapa exato (varredura 11/09 ~11:4x, 11 .py vivos com deepseek-chat no NYC):** no Mínimo, GASTAM hoje: `v41_ciclo.py` (cascata de curadoria) e `gerador_imagem_editorial.py` (capas); pausados hoje (trocar junto na subida): `redator_economia_v4.py` (v42), `agente_repetidor_estatal.py`, `v4_media_expander.py`; medição (trocar nome só p/ consistência): `augusto_fiscal_tokens.py`, `gerador_painel_despesas.py`, `agente_roteador_llm.py`; inativos: 2 backups 20260405. As 2.237 menções do v4_labs são ~98% artefatos (logs/sqlite/JSONs de ciclo) — NÃO mexer.
8. **Rondas DSN** — manter 4/4h com flash (nunca mais 30/30); ronda do Chefe custa ~US$ 0,15/dia em flash.
9. **Chave DeepSeek própria para o Dell** — separa gasto escritório×robôs e acaba com a lacuna de medição (reporter_us65.py flag REGISTRAR_BANCO pronta).
10. **ULTRA_LUXO (02/09)** — suspenso; no PRO, revisar editoria por editoria se o topo de luxo compensa vs Terra/Luna/sonnet.

## 9. ADENDO ~11:0x — vigília de qualidade pós-troca (ordem Miguel "avisa na ponte")

- Ordem do Miguel: avisar a casa na ponte e MANDAR O ASTRA apertar o cerco — a queda proposital de inteligência dos modelos escritores (fable→sonnet; sol→gpt-5.5) será compensada por revisão mais dura: ASTRA na pós-publicação + CLAUDE LAURA (Clúdulaura) na revisão editorial.
- Publicado: ordem completa no `ponte_laura_completa/de_astra.md` (ZM-20260911-CERCO-QUALIDADE, 3 partes: checar queda / apertar cerco / repassar à CL com confirmação) + aviso geral no `de_dell.md` (toda a casa reporta falha com evidência; queda sistêmica 3+ = 🔴 para o Miguel decidir se volta modelo caro).
- Regra de validade: enquanto durar o Plano Mínimo; mudança de nível será avisada na ponte.


## 10. ADENDO ~12:0x — checagem "a fonte secou" (CL) a pedido do Miguel

- Veredito: **NADA quebrou**. O silêncio da fábrica pós-10:35 é a cadência Mínima (3 ciclos/dia); log do v41_ciclo limpo até lá (juiz julgando, zero auth error). Verticais pausados por cron comentado com tag (não quebra).
- **1 fio real consertado**: `/root/.env` do NYC ficou com a chave VELHA na troca da manhã (a fábrica lê `/root/.env.unificado`, que estava certo — mas qualquer outro leitor do `.env` falharia auth). Trocado com backup `.bak_pre_chave_ds_20260911`. Chave nova PROVADA ponta a ponta carregando o `.env.unificado` exatamente como o v41_ciclo faz (flash respondeu OK).
- Esteira WP: hoje coberta até 18:30 (4 peças: 14:30/16:00/17:15/18:30) + drafts novos no banco (269973/269975...); amanhã passa a 2-3 peças/dia — CL instruída no de_laura.md a recalibrar o colchão dela (2-3 slots).
- Banco de pautas: alimentação segue (coletor_nacional tencent + tendencias_intake + autocura_fila, todos sem LLM); o *.db de 0 bytes em dados/ é artefato de glob antigo (lixo inerte, não banco).
