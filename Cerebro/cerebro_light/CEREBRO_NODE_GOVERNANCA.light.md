# CEREBRO_NODE_GOVERNANCA — VERSÃO LIGHT
> Gerado automaticamente por `cerebro_light.py` em 2026-05-24 23:09 BRT
> Original: `CEREBRO_NODE_GOVERNANCA.md` (395KB) — 423 entradas totais
> Este arquivo é READ-ONLY. Edite sempre o original.

---

## CABEÇALHO ORIGINAL (primeiras linhas)

# ⚖️ CÉREBRO CAMADA 2: Nodo de Governança

Este arquivo pertence à Camada 2 do Grande Cérebro. Ele concentra todos os links para Fóruns e Memórias relacionados à **Governança de Agentes, Inteligência Financeira e Protocolos de Controle**.

> **Regra do Tema Duplo:** Todo tema aqui listado possui um par (Fórum + Memória).
> - **Fórum:** Para entender a estratégia de governança e regras.
> - **Memória:** Para auditoria do log técnico das implantações de governança.

---

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
  - **Fórum:** [forum_autonomia_total_100_por_cento.md](./Foruns/forum_autonomia_total_100_por_cento.md)
  - **Status 2026-05-09:** proposta em análise, não aprovada para deploy. DeepSeek e Codex vetaram a autonomia 100% como apresentada e recomendam transição gradual com veto humano preservado para ações críticas, ledger imutável, cost guard por agente, rollback testado e revisão formal do §18 antes de qualquer loop/decisão 24h.
  - **Atualização 2026-05-09 17:25 BRT:** Miguel esclareceu que "100% autônomo" era força de expressão; o modelo governado passa a ser **Autonomia Supervisionada**, com Miguel no loop diário e como circuito de veto/botão vermelho via Telegram. DeepSeek e Claude revisaram o veto para aprovação condicionada às salvaguardas: heartbeat bidirecional, ACK humano em alertas críticos, comandos globais de emergência, ledger de decisões, cost guard por agente, rollback testado e limites de reinicialização/autocura. A proposta original sem humano continua vetada.

## 4. Reforma da Memória — Antecessor Conceitual do Cérebro Imortal
- 📁 **Tema: Os 5 Pilares (Indexador, Sincronia Unificada, Taxonomia, Autocura/Lixeira, Integração com a Trindade)**
  - **Fórum (proposta original 2026-05-03):** [forum_reforma_memoria_v1.md](./Foruns/forum_reforma_memoria_v1.md)
  - **Documento mestre derivado:** [PROJETO_CEREBRO_IMORTAL.md](./PROJETO_CEREBRO_IMORTAL.md)

## 5. Incidente de Governança — Antigravity Editou .py Críticos (Quarentena)
- 📁 **Tema: Violação do protocolo "Antigravity diagnostica, Claude coda" em 2026-05-02**
  - **Memória:** [memoria_auditoria_autocura.md](./Memorias/memoria_auditoria_autocura.md)
  - **Resumo:** Antigravity inseriu filtro programático em `agente_autocura_v4.py` e `agente_observador.py` localmente sem aprovação. Mudanças sob quarentena, sem deploy. Claude Code precisa auditar e decidir reversão ou aprovação.

## 6. Regra de Emergência de Produção
- **Princípio:** Em queda de produção, incidente de publicação, risco de dois masters simultâneos ou risco financeiro imediato, qualquer agente pode executar ação conservadora e reversível **sem aguardar consenso** — desde que faça backup/rollback antes e registre no fórum imediatamente depois.

---

## ⏩ 418 entradas antigas omitidas
> Para ver o histórico completo, leia `CEREBRO_NODE_GOVERNANCA.md` diretamente.
> Busca rápida: `python3 cerebro.py --buscar <termo>`

---

## ÚLTIMAS 5 ENTRADAS

### Root cause estrutural identificado pelo Maestro (auditoria `fact_check_perplexity.py`)

O payload atual da chamada Perplexity **NÃO inclui `search_recency_filter`**:

```python
payload = {
    "model": "sonar-pro",
    "messages": [...],
    "temperature": 0.1,
    "max_tokens": 800,
}
```

Sem esse parâmetro, Perplexity Sonar (que **tem busca em tempo real, não tem cutoff estático**) varre TODO o histórico web. Para pauta como "pesquisa Datafolha 22/05/2026", Perplexity puxa **pesquisas Datafolha antigas** (de outros anos), não acha a desta sexta-feira, conclui "pesquisa não existe" e veta.

Cascateia para Qwen 2ª camada (`_segunda_opiniao_qwen`) que **não tem busca web** — Qwen apenas confirma o veto Perplexity por concordância semântica (Qwen sabe que pesquisa Datafolha tradicional 

> *(... 344 chars omitidos — ler original)*

---

### Regra inviolável §88

**1. `search_recency_filter` OBRIGATÓRIO em chamadas Perplexity para fact-check editorial.**

Padrão: `"search_recency_filter": "day"` para fact-check de matéria publicada em até 24h. Sem isso, Perplexity pode varrer fontes antigas e vetar pauta real por "ausência de evidência" (que na verdade é evidência fora do horizonte temporal correto).

**2. Quando Perplexity vetar pauta com `data_evento <24h`, WebSearch externa OBRIGATÓRIA antes do Qwen 2ª camada.**

Pipeline corrigido:
```
Perplexity sonar-pro (com search_recency_filter=day)
  └─ Se VETO + pauta_quente → WebSearch externa (Brave/Google)
        └─ Se WebSearch CONFIRMA evento → derrubar veto, aprovar
        └─ Se WebSearch NÃO confirma → Qwen 2ª camada (status atual)
  └─ Se VETO + pauta_antiga → Qwen 2ª 

> *(... 269 chars omitidos — ler original)*

---

### Why

Detecção humana é insubstituível em pauta quente. Miguel pegou em 1 mensagem o que toda a camada técnica (Perplexity + Qwen + Maestro inicial) perdeu. O sistema não pode depender disso — fact-check de pauta <24h precisa de redundância de busca, não só de modelos. Modelos sem busca web não podem julgar a posteriori se um evento de hoje existiu; precisam de busca externa.

---

### How to apply

**Implementação prioritária (patch §6.B, autocura §51 complexa):**

1. Adicionar `"search_recency_filter": "day"` ao payload em `fact_check_perplexity.py:280-300` (linha do payload Perplexity)
2. Smoke test com pauta Datafolha (rascunho 522) — esperar `aprovado=True`
3. Adicionar branch WebSearch externa em `fact_check()` quando `aprovado=False` E `secao=eleicoes|nacional` (pauta quente)
4. Implementar `repeated_veto_same_topic` watchdog em `motor_publicador.py` ou `agente_eleicoes_produtor.py`

**Codador:** Claude ou Codex (§13 ordem chegada)
**Auditoria:** consenso §51 complexo — exige aval Codex ou Trindade técnica 2/3
**Backup obrigatório:** `fact_check_perplexity.py.bak_pre_search_recency_<timestamp>`
**Rollback:** restaurar backup + remover linha adicionada
**Smoke 

> *(... 96 chars omitidos — ler original)*

---

### Relacionado

- [[BUG-20260522-PERPLEXITY-FALSO-NEGATIVO-DATAFOLHA]] em `CEREBRO_NODE_BUGS.md`
- [[bug_critico_vazamento_recusa_llm_20260502]] (precedente fact-check falso positivo)
- §6 CLAUDE.md (Fact-Checking Failsafe — pipeline original)
- §17 (Cérebro como Guarda Financeiro — custo extra WebSearch a calcular)
- §51 (autocura complexa exige consenso)

— Inscrito por Claude Maestro · 2026-05-23 00:30 BRT (ordem direta Miguel)

---

## PONTEIROS
- Original completo: [`CEREBRO_NODE_GOVERNANCA.md`](./CEREBRO_NODE_GOVERNANCA.md)
- Índice geral: [`indice_cerebro.json`](./indice_cerebro.json)
- Busca: `python3 cerebro.py --buscar <termo>`
- Validador: `python3 validar_cerebro.py`