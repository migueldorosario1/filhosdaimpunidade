# CEREBRO_NODE_GOVERNANCA_REGRAS_VIVAS — VERSÃO LIGHT
> Gerado automaticamente por `cerebro_light.py` em 2026-07-09 03:32 BRT
> Original: `CEREBRO_NODE_GOVERNANCA_REGRAS_VIVAS.md` (417KB) — 542 entradas totais
> Este arquivo é READ-ONLY. Edite sempre o original.

---

## CABEÇALHO ORIGINAL (primeiras linhas)

# CEREBRO_NODE_GOVERNANCA — Regras Vivas
> Gerado por F3 Reforma Cérebro em 2026-05-24 23:25 BRT
> Origem: `CEREBRO_NODE_GOVERNANCA.md` (ORIGINAL INTACTO — este arquivo foi gerado por split)
> Descrição: § numerados vivos: governança, consenso, autocura, editorial, protocolos ativos
> Busca: `python3 cerebro.py --buscar <termo>`

---

## Cabeçalho original (índice/sumário)

# ⚖️ CÉREBRO CAMADA 2: Nodo de Governança

Este arquivo pertence à Camada 2 do Grande Cérebro. Ele concentra todos os links para Fóruns e Memórias relacionados à **Governança de Agentes, Inteligência Financeira e Protocolos de Controle**.

> **Regra do Tema Duplo:** Todo tema aqui listado possui um par (Fórum + Memória).
> - **Fórum:** Para entender a estratégia de governança e regras.
> - **Memória:** Para auditoria do log técnico das implantações de governança.

---

---

## Conteúdo (86 seções)

## 1. Governança Financeira e Roteamento
- 📁 **Tema: Roteamento Inteligente e Fim de Vazamentos**
  - **Fórum:** [forum_modelos_dinamicos.md](./Foruns/forum_modelos_dinamicos.md)
  - **Memória:** [memorias_modelos_dinamicos_governanca_20260502.md](./Memorias/memorias_modelos_dinamicos_governanca_20260502.md)
- 📁 **Tema: Governança Financeira de APIs, Custos e Modelos**
  - **Fórum principal:** [forum_governanca_financeira.md](./Foruns/forum_governanca_financeira.md)
  - **Fórum auxiliar:** [governanca_financeira.md](./Foruns/governanca_financeira.md)
  - **Projeto em feedback:** [projeto_monitoramento_financeiro.md](./Foruns/projeto_monitoramento_financeiro.md)
  - **Relatório de preços LLM:** [relatorio_precos_llm.md](./Foruns/relatorio_precos_llm.md)
  - **Tarefa Codex 17:55:** [tarefa_codex_20260506_1755.md](./Foruns/tarefa_codex_20260506_1755.md)
- **Atualização Codex 18:06:** DeepSeek V4 confirmado em docs oficiais (`deepseek-v4-flash`/`deepseek-v4-pro`); preços atuais e fontes oficiais registrados no relatório. Alias legados `deepseek-chat`/`deepseek-reasoner` entram em depreciação em 2026-07-24.
- **Atualização Codex 18:24:** Miguel orientou usar intensivamente DeepSeek V4 durante o desconto ate 2026-05-31, mas com pesquisa de qualidade e teste. Plano passou a exigir benchmark offline, teto de teste pago, roteamento task-by-task, custo por post, conciliacao com cartao e boletim diario de modelos/precos. Loop 24h de Codex/Claude no servidor fica bloqueado ate desenho especifico compatível com §18 e limites de custo.
- **Atualização Codex 18:29:** Miguel corrigiu que o foco nao e "benchmark offline" nem so DeepSeek; a regra reutilizavel e governanca financeira por post e por tarefa para todos os provedores. Cada post deve poder ter log de agentes/modelos, papeis, tokens, USD/BRL e audiencia posterior, mas a transparencia tambem tem custo: Telegram deve receber detalhe so quando for destaque, anomalia, pedido humano ou alta performance. Estado atual: sem pressa e sem codigo; manter debate.
- **Atualização Codex 19:48:** MVP 0 de governança financeira foi deployado manualmente no Tencent em `/root/custos/` com três scripts read-only (`coletar_custos_internos.py`, `gerar_relatorio_financeiro.py`, `prognosticar_tarefa.py`), sem cron novo. Smoke remoto `--dry-run`/`--write --data 2026-05-06` gerou JSON/MD em `/root/agent_data/{custos_consolidados,relatorios_financeiros}/`; total remoto do dia: US$ 69.899814 estimado, 6637 chamadas. `ruff`/`pyflakes` indisponíveis no servidor; `py_compile` e `json.tool` OK. Rollback remoto: remover `/root/custos` e os três artefatos datados de 2026-05-06.
- **Atualização Codex 20:49:** MVP 1 iniciado localmente/default-off: `config/governanca_financeira_mvp1.json` define logs dedicados do roteador, sugestão dry-run de DeepSeek para curadoria/triagem e proteção de fact-check/redação/auditoria; `agente_roteador_llm.py` grava `agent_data/roteador_llm.jsonl` e só reordena para DeepSeek se `deepseek_curadoria.enabled=true`; relatórios de custo ganharam câmbio BCB PTAX cacheado e anomalia relativa 1.5x. Sem deploy Tencent neste tick.
- **Atualização Codex 21:48:** MVP 1 ganhou `modelos_padrao.json` v0.2 local/default-off com `modelos_por_tarefa` e `keyword_gating` desligado para `agente_comentarista`/`agente_china`; novo `root/util_pautas_sensiveis.py` detecta pautas China sensíveis e fontes oficiais chinesas sem LLM/rede; `agente_roteador_llm.py` só força Claude/Anthropic se a feature flag do agente e o `keyword_gating.ativar` estiverem ligados. Sem deploy Tencent.
- **Atualização Codex 01:07 07/05:** Relatório financeiro local agora classifica `qwen*` como provider `alibaba`, `glm-*`/`zhipu` como `zhipu` e mantém `brave`; `config/governanca_financeira_mvp1.json` ganhou watchlist read-only para Zhipu (US$ 3 crédito), Alibaba/Qwen pós-pago e Brave Search (franquia 2000 req/mês). Sem rede/API paga, sem cron novo, sem deploy Tencent; dry-run de 2026-05-07 alerta `provider_sem_log_uso` enquanto não houver log dedicado desses provedores.
- **Atualização Codex 01:18 07/05:** MVP 1 local ganhou `root/util_governanca_financeira.py` e leitura de `agent_data/governanca_financeira_api_usage.jsonl`; `publicador_tematicos.coletar_brave()` registra `brave-search` quando busca real ocorrer; `agente_roteador_llm.py` ganhou suporte inerte a providers OpenAI-compatible `alibaba`/`zhipu` com log dedicado para Qwen/GLM quando uma rota futura os escolher. Sem chamada real de API, sem deploy Tencent e sem cron novo.
- **Atualização Codex 01:35/01:39 07/05:** Com autorização direta de Miguel ("pode codar e subir"), MVP 1 de governança financeira foi deployado no Tencent para `/root` com backup remoto `*.bak_pre_govfin_api_usage_deploy_20260507_0130`; inclui log dedicado fail-open de Brave/Qwen/GLM, watchlist `alibaba`/`zhipu`/`brave`, relatório dry-run e `precos_modelos.json`. Sem cron novo e sem chamada paga. Pós-deploy corrigiu lint trivial com backup `*.bak_pre_pyflakes_cleanup_20260507_013821` e `pyflakes` temporário em `/tmp`. Detalhes, MD5 e rollback em `Foruns/forum_governanca_financeira.md` seção 24.
- **Atualização Codex 02:18 07/05:** Agente China ganhou governança financeira própria no roteador: `agente_china_modelos.json` registra teto `modelo_max_input_usd_1m=3.0` e `modelo_max_output_usd_1m=15.0`, equivalentes ao limite Sonnet luxo ocidental; `util_llm_china.py` pula automaticamente modelos acima do teto, modelos sem custo vetado explícito por nome (`o1`, `o3`, `claude-3-opus`, `claude-opus`) e registra eventos de paraquedas final. DeepSeek V4 Pro virou primário do coletor/produtor; GPT-4o e Claude 3.5 Sonnet ficam só no fim da cascata. Detalhes em `Foruns/forum_agente_china_china_only_20260507.md`.
- **Atualização Codex 14:32 22/05:** Miguel determinou Cafezinho editorial com provedores chineses + Perplexity, mantendo exceções para Agente Qualidade (OpenAI/Claude) e Agente Twitter (Grok em sprint separado). Inventário read-only e plano de consenso em [forum_sprint_politica_chinesa_cafezinho_20260522.md](./Foruns/forum_sprint_politica_chinesa_cafezinho_20260522.md); sem patch/deploy neste tick.
  - **Resumo:** monitoramento de custos, relatorio diario Augusto, prognostico por tarefa, pesquisa de modelos baratos e regras de seguranca para billing/RPA/prints.


## 2. A Trindade (Fórum, Memória, Canal)
- 📁 **Tema: Protocolos Universais de Agentes Autônomos**
  - **Fórum:** [forum_trindade_protocolos.md](./Foruns/forum_trindade_protocolos.md)
  - **Memória:** [memorias_tutorial_trindade_20260502.md](./Memorias/memorias_tutorial_trindade_20260502.md)
  - **Minuta viva:** Leis Gerais da Inteligência Compartilhada v0.1, abertas para revisão de Claude Code e Antigravity.


## 3. Regra Democrática da Trindade (Consenso vs Maioria)
- 📁 **Tema: Orquestração de Decisões do Cérebro Compartilhado**
  - **Fórum:** [forum_cerebro_imortal.md](./Foruns/forum_cerebro_imortal.md)
  - **A Regra:** Toda decisão arquitetural crítica exige **consenso absoluto** entre Antigravity, Claude Code e Codex. Sem consenso, o humano (Miguel) decide. Decisões não-críticas exigem maioria simples (2 a 1).
- 📁 **Tema: Autonomia Total / Conselho Autônomo**

---

## ⏩ 537 entradas antigas omitidas
> Para ver o histórico completo, leia `CEREBRO_NODE_GOVERNANCA_REGRAS_VIVAS.md` diretamente.
> Busca rápida: `python3 cerebro.py --buscar <termo>`

---

## ÚLTIMAS 5 ENTRADAS

### Ação executada (§92 cheio)

Crontab Tencent SG modificado 13:00 BRT — 4 entradas comentadas com prefixo `# PAUSADO_AGENTE_CRIATIVO_ECONOMIA_20260619_1300`:

1. `0 6 * * *` BCB SGS (Selic/IPCA diário)
2. `0 7 5 * *` IBGE SIDRA (mensal dia 5)
3. `5 7 5 * *` Comexstat (mensal dia 5)
4. `*/5 * * * *` ingestor_estatistico

**Backup pré-pausa**: `/root/backups/crontab_root_pre_pausa_estatistico_20260619_1258.txt`
**Patch**: via `sed` in-place (não `open(w)`, não HEREDOC)
**Sanity**: SHELL=bash ✅ · autocura ✅ · sync_nyc_leve ✅ · robo_coleta_geopolitica ✅ · total ativas 92→88 (-4)
**Rollback**: `sudo crontab /root/backups/crontab_root_pre_pausa_estatistico_20260619_1258.txt`

---

### Estado preservado

- Código `/root/agente_estatistico/*.py` intocado
- Banco `/root/agent_data/stats/banco_estatistico.db` intocado
- 6+ dias de JSONs em `raw/payloads/` intocados (consultáveis se preciso pra debug ou alimentação futura)

---

### Regra (vinculante)

**Coletor de dados estruturados (BCB/IBGE/Comexstat/Fred/GACC/Eurostat/etc) não deve rodar enquanto não houver produtor criativo de economia consumindo.** Religar caso a caso quando o agente criativo correspondente publicar pelo menos 1 matéria de teste.

---

### Visão futura (não-vinculante, mas direção editorial)

Agente criativo de economia será **estritamente original** (zero "com base em matéria publicada"). Lead parte do dado bruto, comparação cross-país obrigatória (BCB×FED, Comexstat×GACC, IPCA×CPI), enquadramento anti-imperialista por arquitetura, gráfico embutido como argumento, auditor de cálculo obrigatório, 1-2 matérias/dia.

---

### Vínculos

- Fórum vivo: `Projeto Cafezinho Agentes/Foruns/forum_agentes_criativos_estatistico_brutas_plus_20260619.md` (adendo Daemon 13:00 BRT)
- Backup crontab: `/root/backups/crontab_root_pre_pausa_estatistico_20260619_1258.txt`
- Investigação outros desencapados: parcial, em curso (próximos ticks §53)

— 👑 Claude (Daemon)

---

## PONTEIROS
- Original completo: [`CEREBRO_NODE_GOVERNANCA_REGRAS_VIVAS.md`](./CEREBRO_NODE_GOVERNANCA_REGRAS_VIVAS.md)
- Índice geral: [`indice_cerebro.json`](./indice_cerebro.json)
- Busca: `python3 cerebro.py --buscar <termo>`
- Validador: `python3 validar_cerebro.py`