# MEMÓRIA — Diagnóstico de saúde do ecossistema Cafezinho Media Group (01/08/2026)

**Data-base do diagnóstico:** 1º de agosto de 2026, 10h30 BRT
**Registrado no Cérebro:** 2026-08-01 12:00 BRT por Kimi K3 (ZCode), a pedido do Miguel
**Fórum irmão (Regra do Tema Duplo):** `Foruns/forum_diagnostico_saude_ecossistema_20260801.md`
**NODO Camada 2:** `CEREBRO_NODE_CHECKUPS.md` → CHECKUP-005

**Escopo declarado pelo autor do diagnóstico:** código, configurações, crons e telemetria disponíveis no workspace. Não foram executados smokes pagos contra todas as APIs nem consulta aos servidores remotos; portanto, "sem evidência" não significa necessariamente indisponível.

**Resumo:** o ecossistema está operacional, porém degradado. Os publicadores V4 continuam entregando, mas a geração de artigos novos está instável. A cascata de LLMs perdeu redundância por saldo, quota e respostas inválidas.

---

## 1. LLMs — log completo

| Provider / modelos cadastrados | Saúde | Evidência mais recente | Diagnóstico |
|---|---|---|---|
| Anthropic — Claude Opus 4.8 | 🟢 | Recuperado em 28/07; chamada real bem-sucedida | Operacional novamente. Alto custo; adequado para superluxo/auditoria. |
| Anthropic — Claude Sonnet 4.6 | 🟡 | Circuit breaker antigo por conta indisponível; chamadas via rota AssemblyAI funcionaram | Cadastro diz ativo, mas a rota Anthropic direta precisa novo smoke. |
| Claude Haiku 4.5 | ⚫ | Bloqueado por política financeira | Não operacional por decisão. |
| Claude Opus 4.7 | ⚫ | Bloqueado por custo/política | Não deve entrar em cascata. |
| OpenAI — GPT-5.5 | 🟡 | 88/92 sucessos históricos; hoje retornou conteúdo vazio no YouTube | Principal fallback forte, mas o tratamento de resposta vazia está quebrando o agente YouTube. |
| GPT-4o | 🔴 | Chave inválida registrada; 0/3 sucessos | Cadastro diz ativo, mas telemetria o contradiz. |
| GPT-4o Mini | 🟡 | Fallback final do V4; sem amostra isolada recente | Configurado, porém depende da mesma conta OpenAI. |
| GPT-4o Mini Search Preview | ⚫ | Sem saldo | Inativo. |
| GPT-5 / GPT-5.4 | ⚫ | Bloqueados por healthcheck | Fora da operação. |
| O3 | ⚫ | Bloqueado | Fora da operação. |
| Google — Gemini 3.5 Flash | 🟡 | Juiz visual funciona hoje; estado também registra crédito pré-pago esgotado em 28/07 | Evidência contraditória, possivelmente chaves/projetos diferentes. Precisa normalizar credenciais. |
| Gemini 2.5 Pro | 🟡 | Tribunal visual funcionou em 14/07 | Utilizável, mas sem smoke recente e com histórico de Vision degradado. |
| Gemini 2.5 Flash | 🟡 | Cadastrado ativo; healthcheck Vision anterior degradado | Sem confirmação suficiente de saúde atual. |
| DeepSeek Chat / V4 Flash / V4 Pro | 🔴 | HTTP 402, saldo insuficiente | Toda a família está efetivamente indisponível na cascata temática. |
| Moonshot/Kimi — moonshot-v1-32k/128k | 🔴 | HTTP 429: conta suspensa por saldo insuficiente | Segundo elo da cascata temática está fora. |
| Moonshot v1 8K | ⚫ | Marcado sem saldo | Inativo. |
| Kimi K2.5 | ⚪ | Pendente de teste | Não deve receber tráfego automático. |
| Kimi K2.6 | 🔴 | Bloqueado; histórico de conteúdo vazio | Inadequado para produção atual. |
| Zhipu — GLM 4.5 Flash | 🟡 | Produziu textos hoje, mas houve respostas vazias/JSON inválido | É o gerador predominante atual, porém instável. Precisa retry e validação de conteúdo antes do parse. |
| GLM 4 Plus | 🔴 | Sem saldo e bug de alucinação registrado | Fora da produção. |
| GLM 5.1 / variante sem thinking | ⚪ | Pendentes de teste | Ainda não promovidos. |
| Alibaba — Qwen Plus | 🟡 | 6/6 sucessos na telemetria; hoje fez auditoria, com latência elevada | Fallback funcional. Houve falhas DNS intermitentes. |
| Qwen Max / Qwen3 Max | ⚪ | Cadastrados ativos, sem prova recente | Saúde não confirmada nesta rodada. |
| Qwen VL Plus / VL Max | 🟡 | Configurados para visão; histórico anterior positivo | Não são atualmente a única rota visual; precisam smoke dedicado. |
| xAI — Grok 3 / Grok 4.3 | ⚪ | Cadastrados ativos, sem telemetria recente | Estado operacional desconhecido. |
| Mistral Large | ⚪ | Cadastrado ativo, sem chamada recente | Estado operacional desconhecido. |
| Perplexity Sonar Pro | ⚪ | Cadastrado para fact-check; sem prova recente | Deve ser validado antes de depender dele como gate obrigatório. |
| Sonar Reasoning Pro | ⚫ | Sem saldo | Inativo. |
| Groq Llama 3.1 8B | ⚪ | Pendente de teste | Não operacional na cascata normal. |

## 2. Agentes e pipelines ativos — log completo

| Agente / sistema | Saúde | Evidência de 01/08 | Parecer |
|---|---|---|---|
| Orquestrador temático V4 | 🟢 | Cron atualizado às 08h12; ciclos continuam rodando | Locks e isolamento por site estão funcionando. |
| Coletor V4 compartilhado | 🟡 | Coletou notícias em quase todos os sites | Há DNS/RSS intermitente, sobretudo Prensa Latina. |
| Produtor V4 compartilhado | 🔴 | Quase todos os ciclos terminaram com 0 artigos aprovados | Principal gargalo. GLM gera texto, mas auditoria vazia, JSON inválido e "fonte sem texto" impedem promoção. |
| Publicador V4 compartilhado | 🟢 | 9 posts publicados hoje nos sites temáticos | Entrega e seleção de hero continuam funcionando. Parte dos posts veio do estoque auditado, não da produção do próprio ciclo. |
| Juiz visual Gemini | 🟡 | Aprovou e rejeitou imagens corretamente hoje | Funcional, mas com histórico de quota/credencial contraditório e dependência externa elevada. |
| AIatolah | 🟡 | 1 ciclo, 1 publicação; produção nova zerada | Publicador vivo, produtor degradado. |
| Ceará Digital | 🔴 | 3 ciclos, 0 publicações, 3 produções zeradas; JSON GLM inválido | Operação roda, mas não entrega conteúdo novo. |
| Discover Brazil | 🟡 | 1 ciclo, 2 publicações; produção do ciclo zerada | Publicou backlog. Há desvio editorial aparente: matérias sobre China/TravelAI pouco alinhadas ao foco Brasil. |
| Global South News | 🟡 | 1 ciclo, 2 publicações; produção zerada; 1 RSS falhou | Entrega preservada, ingestão parcialmente degradada. |
| Mapa Rio | 🟡 | 1 ciclo, 0 publicações; YouTube limitado a 1/dia | Sem erro fatal, mas baixa produtividade no ciclo atual. |
| Mundo dos Trilhos | 🟡 | 1 ciclo, 2 publicações; produção zerada | Publicador saudável; produtor não renovou estoque. |
| Rail Post | 🟡 | 1 ciclo, 2 publicações; produção zerada | Auditor Qwen barrou erro temporal corretamente; entrega usa backlog. |
| Rio Carta | 🔴 | 3 ciclos, 0 publicações, 3 produções zeradas; JSON GLM inválido | Pipeline vivo, porém sem resultado editorial hoje. |
| YouTube AIatolah | 🟡 | Executa, mas rejeita todos os candidatos recentes | Filtros funcionam; produtividade atual é zero. |
| YouTube Global South | 🟡 | Executa, mas rejeita vídeos por duração/critério | Não está quebrado, mas não entrega. |
| YouTube Mapa Rio | 🟢 | Publicação diária detectada; cooldown funcionando | Melhor saúde entre os agentes de vídeo temáticos. |
| YouTube Ceará, Discover Brazil, Mundo Trilhos, Rail Post e Rio Carta | ⚫ | Desabilitados explicitamente nas configurações | Pausa intencional, não falha. |
| YouTube Cafezinho | 🔴 | Vários tracebacks; GPT-5.5 vazio; conta Kimi suspensa; yt-dlp ausente; Transkriptor instável | Componente mais doente do ecossistema atual. Também há desperdício de US$ 0,36 por transcrição ruim rejeitada. |
| Pipeline editorial V4 Labs/WordPress | 🟢 | 68 testes + 5 subtestes passaram | Núcleo testado de publicação, release, mídia e WordPress está consistente quando executado pelo diretório correto. |
| Vision V4 Labs | 🟡 | Último checkup canônico: 3/7, degraded | Código testado, mas provedores/credenciais ainda são risco operacional. |
| Maestro Distribuição legado/Tencent | 🟡 | Cron configurado a cada 20 minutos; sem log local recente | Configuração existe, mas não há comprovação local de execução atual. |
| Repetidor Estatal | 🟡 | Cron horário registrado | Sem telemetria local recente suficiente. |
| Monitoramento, auditoria, autocura e Prometheus | 🟡 | Vários crons configurados | Boa cobertura arquitetural, mas o snapshot de crontab não prova que todos estão rodando no servidor hoje. |
| Agentes sociais | 🟡 | Coletor social configurado; Instagram e fila antiga pausados | Coleta parcialmente ativa; publicação social permanece reduzida. |
| V3 Política | ⚫ | Coleta, produção e publicador comentados no cron | Pausado intencionalmente. |
| Inventário antigo de ~104 agentes | ⚫/⚪ | Documento canônico é de maio e diverge do parque V4 | Deve ser tratado como histórico até reconciliação com crontab e processos reais. |

## 3. Prioridades registradas no diagnóstico

| Prioridade | Ação recomendada | Impacto |
|---|---|---|
| P0 | Corrigir o YouTube Cafezinho: instalar/configurar yt-dlp, capturar conteúdo vazio do GPT-5.5 e impedir traceback | Recupera o agente mais quebrado e reduz gasto desperdiçado. |
| P0 | Recarregar ou remover DeepSeek e Kimi da cascata enquanto estiverem em 402/429 | Evita latência acumulada de fallbacks sabidamente mortos. |
| P0 | Tratar resposta GLM vazia/JSON inválido com retry e fallback antes de abandonar o item | Ataca diretamente a produção zerada de Ceará e Rio Carta. |
| P1 | Investigar por que artigos gerados e "auditados" terminam em 0 aprovados | Hoje a publicação depende de backlog; o estoque pode acabar. |
| P1 | Unificar as credenciais Gemini e limpar circuit breakers vencidos | Elimina o estado contraditório "juiz funcionando" versus "crédito esgotado". |
| P1 | Corrigir ingestão de fonte sem texto antes da geração | Reduz descartes falsos no gate de fidelidade numérica. |
| P2 | Reconciliar o inventário antigo com V4 e marcar definitivamente ativo, pausado e legado | Evita decisões operacionais baseadas em documentação de maio. |

## 4. Fontes principais do diagnóstico

- `agent_data/v4/cron_v4.log`
- `agent_data/v4_cafezinho_youtube/cron.log`
- `agentes_tematicos/v4/nucleo_llm.py`
- `Projeto Cafezinho Agentes/root/config/llm_ratings.json`
- `Cerebro/CEREBRO_NODE_CHECKUPS.md`

---

*Memória arquivada na íntegra a partir do diagnóstico entregue pelo Miguel nesta sessão ZCode. Conteúdo factual preservado sem alterações editoriais.*
