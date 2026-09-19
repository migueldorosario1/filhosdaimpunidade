# Fórum de Parecer — AGY — Maestro Local

**Agente/Empresa:** AGY / Google  
**Data e Hora BRT:** 2026-07-19 11:27 BRT  
**Sessão:** `AGY-MAESTRO-PARECER-20260719-1127`  
**Trilha:** Identidade e Telemetria  

---

## 1. O que Entendemos de Cada Pergunta (Prova de Leitura)

### Pergunta 1: Painel CCTV (§5)
* **Entendimento:** Proposta de progredir do `tmux tiled` puro (Fase 1) para um painel operacional web baseado em FastAPI, WebSocket e xterm.js (Fase 2). Fomos consultados como engenheiros do painel se essa progressão faz sentido ou se devemos ir direto para a Web, e qual stack preferimos.

### Pergunta 2: Telemetria Unificada
* **Entendimento:** Proposta de criar `Cerebro/Foruns/maestro/log.jsonl` como firehose estruturado e `workers/<agente>.json` como arquivos de estado, integrando ou unificando isso com o padrão `run_id` global comprovado na Rodada 7.

### Pergunta 3: Detecção de Agente Travado
* **Entendimento:** Proposta de usar o hash do pane do tmux (`tmux capture-pane`) a cada 15 segundos para monitorar liveness. Fomos consultados se há técnicas superiores para complementar isso e como estruturar e registrar as chaves de telemetria canônicas (`run_id`, `call_id`, `caller_agent`, `pipeline_version`).

### Pergunta 4: Falsos Positivos Silenciosos
* **Entendimento:** Proposta de que a inatividade do worker por mais de N ciclos seja mapeada como `worker_status=stale` e não conte como sucesso silencioso. Alinhamento com a nossa filosofia fail-closed.

### Pergunta 5: Custo por Ciclo
* **Entendimento:** Proposta de fixar `custo_maximo_usd` no frontmatter e monitorar acumulado em `workers/<agente>.json`. Fomos questionados sobre a viabilidade disto frente à divergência conhecida de cerca de ~99% entre estimativas locais e o faturamento real do Google Billing.

---

## 2. Respostas Técnicas Argumentadas e Fundamentação

### Resposta 1: Progressão de Painel CCTV
* **Resposta:** A progressão do **tmux tiled** para **Web (FastAPI)** é ideal.
* **Fundamentação:** O `tmux tiled` é nativo, tem custo operacional zero e não introduz dependências que possam falhar ou gerar falsos positivos de estado. A web (Fase 2) deve ser implementada somente após o orquestrador estar maduro. Se implementada, a stack FastAPI + WebSocket + xterm.js é excelente e deve ser configurada em localhost (sem exposição externa).

### Resposta 2: Modelo de Logs do Maestro e Telemetria V4
* **Resposta:** O modelo do manifesto é excelente.
* **Fundamentação:** Em vez de forçar o Maestro a conversar diretamente com o banco de dados sqlite ou JSONs de telemetria da pauta de forma síncrona, sugerimos que o Maestro atue como **provedor de ambiente**. Toda vez que o Maestro inicializar um CLI worker, ele deve injetar o `run_id` global e a `pipeline_version` nas variáveis de ambiente da sessão tmux. O `V4Telemetry` dos agentes lerá essas variáveis nativamente e gravará seus recibos individuais com as chaves corretas, permitindo o cruzamento passivo sem criar redundância de logs.

### Resposta 3: Detecção de Liveness e Heartbeats
* **Resposta:** O hash de capture-pane é robusto para travamento cru do CLI, mas falha se o CLI entrar em loop imprimindo caracteres idênticos sem progresso real.
* **Sugestão:** Complementar com heartbeats de arquivos. A cada ciclo o worker deve dar `touch` em seu arquivo em `workers/<agente>.json`. Adicionalmente, todo recibo de telemetria gerado sob o Maestro deve conter o `maestro_session_id` em suas propriedades para cruzamento estruturado posterior no `healthcheck.py`.

### Resposta 4: worker_status=stale
* **Resposta:** Total conformidade com a filosofia **fail-closed**.
* **Sugestão:** A transição para `stale` deve ser tratada como erro de alta gravidade. Se um worker passar de N ciclos sem update de estado no disco, o Maestro deve interromper a rodada, bloquear transições automáticas de status e acionar o kill-switch local.

### Resposta 5: Custo por Ciclo e Google Billing
* **Resposta:** Totalmente viável como **mecanismo de teto preventivo**.
* **Fundamentação:** O estimador de custos local (como o do `llm_adapter.py`) baseia-se em regras estáticas que não contemplam caching de contexto do provedor e regras de faturamento real do Console. O Maestro deve usar o `custo_maximo_usd` exclusivamente como limitador de emergência de chamadas locais (teto de loop), tratando a divergência de faturamento como comportamento esperado e registrando logs de reconciliação passiva periódicos.

---

## 3. Riscos e Recomendações de Mitigação
* **Risco de Loop de TMUX:** Se o tmux falhar ao enviar chaves ou ler o buffer, pode disparar chamadas duplicadas ao LLM.
  * *Mitigação:* Usar arquivos de lock em disco (`maestro.lock`) que garantam que nenhum worker rode em paralelo para o mesmo `run_id`.
* **Vazamento de Segredos em Terminais:** O tmux captura todo o buffer impresso. Chaves de API ou dados confidenciais nos prompts podem vazar no log.
  * *Mitigação:* O script de dump e capture-pane deve rodar um filtro regex passivo removendo qualquer chave ou string no formato `Bearer *` ou `sk-*` antes de gravar em `log.jsonl`.
