# Maestro Local — orquestrador multi-CLI de agentes IA (fork Primeline)

**Direção:** Miguel do Rosário
**Engenheiro responsável do manifesto:** Claude Code (Anthropic, `claude-opus-4-7`)
**Data:** 2026-07-19 09:45 BRT
**Sessão:** `CLAUDE-MAESTRO-LOCAL-MANIFESTO-20260719-0945`
**Status:** MANIFESTO PROPOSTO — AGUARDANDO REVISÃO DO MIGUEL

**Alerta de identidade:** Claude Code = Anthropic; NÃO é GLM/Ming (Zhipu AI). Este manifesto foi escrito pelo Claude Code, não pelos outros agentes.

---

## 1. Motivação

O sprint V4 (Rodadas R3→R7) provou que a Trindade+aliados (Codex, GLM, Grok, Kimi, Qwen, DeepSeek, AGY) consegue trabalho técnico rigoroso quando cada agente atua na sua trilha. Falta uma peça: a **ativação sincronizada**.

Hoje o fluxo é:

1. Miguel abre um CLI de cada vez, cola prompt, espera resposta, cola próximo prompt em outro CLI. Ciclo linear, humano no meio de tudo.
2. Codex coordena via fóruns markdown, mas cada agente só "acorda" quando Miguel digita algo no CLI dele.
3. Claude Code é o único com wrapper que faz preload automático de contexto ao entrar (`~/bin/claude` puxa snapshot + fóruns + agenda + lembretes).

**O gargalo é humano.** Miguel precisa estar disponível pra ativar cada engenheiro entre rodadas. Se ele dorme, o sprint para. Se ele viaja, quebra.

**Objetivo do Maestro Local:** substituir Miguel apenas na função de ativação (não de decisão editorial ou aprovação de risco). Claude Code, acordado por cron a cada 15 ou 30 minutos, lê estado atual, decide qual agente deve rodar qual sprint agora, aciona o CLI de cada um simulando digitação humana, monitora, registra e volta a dormir.

Miguel mantém: decisão editorial, aprovação de risco, deploy, publicação, autorização de gasto acima de threshold, poder de kill-switch, intervenção manual em qualquer painel a qualquer momento.

Miguel delega: ativação de CLI, distribuição de sprints entre agentes, monitoramento de idle/travado/rate-limit, registro de ciclo, coordenação de handoff entre agentes.

## 2. Referência e escolha da base

Pesquisa registrada em conversa 2026-07-19 09:35 BRT. Três projetos avaliados; matriz completa em `~/ferramentas/hive_exploracao/` (repos clonados). Resumo:

| Base | Linhas | Stack | Escolha |
|---|---:|---|---|
| `Jedward23/Tmux-Orchestrator` | 230 | Bash+Py | ❌ primitivo, path macOS hardcoded, sem detecção de travado |
| `awslabs/cli-agent-orchestrator` | ~48.500 | Python pesado (FastAPI/MCP/SQLite/JWT) | ❌ over-engineered pra caso; canhão em mosca |
| **`primeline-ai/claude-tmux-orchestration`** | **830** | **Bash puro + jq** | ✅ **BASE ESCOLHIDA** |

Filosofia do Primeline bate 1:1 com a do workspace: bash puro, arquivos como estado, zero SaaS, zero dependência pesada, visibilidade total via tmux attach.

**Cross-pollinate**: os `providers/*.py` do awslabs (11 arquivos) documentam o regex de "prompt idle" de cada CLI (`❯` claude, `›+•` codex, prompts kimi/qwen). Copiar só esses regex resolve o problema de generalizar Primeline pra multi-provider.

**Referência comercial que Miguel dispensou:** os produtos "Hive" (hive-ai.dev, hivecli.com, hivecode.app) — todos são open source mas genéricos demais e alguns exigem instalar telemetria/permissões invasivas. Maestro Local não vai depender de nenhum.

## 3. Arquitetura

### 3.1 Diretório canônico

```
~/ferramentas/maestro/
├── scripts/
│   ├── orch-bootstrap.sh          # idempotente, cron chama isso
│   ├── heartbeat.sh               # loop principal do maestro (chama Claude a cada N min)
│   ├── spawn-agent.sh             # abre painel tmux + inicia CLI de um agente
│   ├── rate-limit-watchdog.sh     # detecta 429/overloaded, recupera
│   ├── painel_cctv.sh             # aplica layout tiled + attach
│   └── kill-switch.sh             # para tudo, preserva estado
├── config/
│   ├── agentes.json               # mapa CLI → wrapper, flags, regex idle, rate-limit patterns
│   ├── prompts_engenheiro_chefe.md # prompts que Claude usa pra decidir sprint
│   └── cron.conf                  # linhas de crontab (referência, não instalado auto)
├── providers/
│   ├── claude.regex               # ❯ idle, prompts de erro Anthropic
│   ├── glm.regex                  # prompts Z.ai
│   ├── codex.regex                # › + • idle, prompts OpenAI
│   ├── grok.regex                 # prompts xAI
│   ├── kimi.regex                 # prompts Moonshot
│   ├── qwen.regex                 # prompts DashScope
│   ├── deepseek.regex             # prompts DeepSeek
│   └── mistral.regex              # prompts Mistral
└── README.md                      # setup, kill-switch, troubleshooting
```

Estado do maestro NÃO fica em `~/ferramentas/maestro/`. Vai pra:

```
/home/migueldorosario/Downloads/Antigravity Google/Cerebro/Foruns/maestro/
├── session.json                   # estado atual (agentes ativos, ciclo N, última decisão)
├── workers/
│   ├── claude.json                # status, PID tmux, última msg, updated_at
│   ├── glm.json
│   ├── codex.json
│   └── ...
├── inbox/                         # mensagens agente→agente (pareado com inbox_trindade)
│   ├── claude/
│   ├── glm/
│   └── ...
├── ciclos/
│   ├── log_20260719_0930.md       # o que cada ciclo decidiu, quem acionou, resultado
│   └── ...
└── log.jsonl                      # firehose estruturado (grep-friendly)
```

**Motivo dessa separação:**

- Código executável fica em `~/ferramentas/maestro/` — não polui workspace, não vai pra backup Drive, não interfere no sprint V4.
- Estado/memória fica dentro do workspace em `Cerebro/Foruns/maestro/` — segue [[project_reorganizacao_foruns_unificados_20260717]], integra com resto do subcérebro, versionável, backup Drive natural, buscável via `busca "maestro"`.

### 3.2 Fluxo de um ciclo

```
CRON (*/15 * * * *)
    ↓
orch-bootstrap.sh
    ├── Verifica se sessão tmux `maestro` existe
    │       ├── Não existe → cria com painel principal
    │       └── Existe → segue
    ├── Verifica kill-switch (~/MAESTRO_PAUSADO ou Cerebro/Foruns/maestro/PAUSADO)
    │       └── Se existe → sai, log "pausado"
    ├── Verifica heartbeat stale (>N min sem update)
    │       └── Se stale → kill heartbeat anterior, respawn
    └── Chama heartbeat.sh se não estiver rodando
            ↓
heartbeat.sh (loop principal)
    ├── ciclo N++
    ├── Chama ~/bin/claude com prompt "novo ciclo maestro N; leia Cerebro/Foruns/maestro/session.json; decida"
    │   (usa wrapper pra preservar preload: snapshot + fóruns + agenda)
    │       ↓
    │   Claude (engenheiro-chefe) faz:
    │       a) Read session.json + últimos ciclos + canal_trindade (últimas 200 linhas)
    │       b) Read inbox_trindade/*.md pra ver ordens pendentes
    │       c) Decide: quem trabalha, o quê, qual sprint
    │       d) Grava sprint_para_<agente>.md dentro do respectivo workers/<agente>/
    │       e) Chama spawn-agent.sh <agente> pra cada engenheiro que deve rodar
    │       f) Atualiza session.json com decisão do ciclo
    │       g) Grava ciclos/log_YYYYMMDD_HHMM.md
    │       h) Sai
    ├── Verifica idle/travado dos agentes ativos (capture-pane + regex por CLI)
    │       ├── Idle há >N min → considera pronto, coleta resultado
    │       ├── Travado (mesmo output N ciclos) → registra em log.jsonl como warn
    │       └── Rate-limited (regex match no output) → dispara rate-limit-watchdog.sh
    ├── Espera interruptible_sleep (adaptativo: 30s se atividade, 120s se calmo, 300s se muito calmo)
    └── Loop
            ↓
spawn-agent.sh <agente>
    ├── tmux new-window -t maestro -n <agente> (se não existir)
    ├── tmux send-keys -t maestro:<agente> "cd <workdir> && ~/bin/<agente>" Enter
    ├── Espera prompt idle aparecer (regex do provider)
    ├── tmux load-buffer <caminho_do_sprint_para_agente.md>
    ├── tmux paste-buffer -t maestro:<agente>
    ├── tmux send-keys -t maestro:<agente> Enter
    ├── Atualiza workers/<agente>.json com PID + status + updated_at
    └── Retorna imediatamente (agente trabalha assíncrono)
            ↓
painel_cctv.sh (chamado uma vez ao arrancar sessão)
    ├── tmux select-layout -t maestro tiled
    └── (Miguel: tmux attach maestro → vê grid de painéis)
```

### 3.3 Contrato de handoff (sprint pra agente)

Cada `sprint_para_<agente>.md` que Claude grava no ciclo tem formato fixo pra o agente entender rápido:

```markdown
---
ciclo: 42
maestro_ordem_em: 2026-07-19T09:45:00-03:00
agente: codex
tarefa: R7 revisão do patch Qwen Vision
prazo_estimado: 30min
retorno_esperado: RESULTADO ou AGUARDANDO_MIGUEL
custo_maximo_usd: 0.50
---

# Sprint para Codex — ciclo 42

## O que fazer
[…]

## Arquivos reservados
[…]

## Como responder
Quando terminar, grave RESULTADO em `workers/codex.json` campo `ultimo_resultado`.
Se travou ou precisa de Miguel, grave AGUARDANDO_MIGUEL + motivo.
```

### 3.4 Provider config (agentes.json)

Mapa central de como cada CLI se comporta:

```json
{
  "claude": {
    "wrapper": "~/bin/claude",
    "flags": ["--dangerously-skip-permissions"],
    "regex_idle": "❯ $",
    "regex_busy": "^(⚒|◐|◑|◒|◓) ",
    "regex_rate_limit": ["429", "overloaded_error", "rate_limit"],
    "rate_limit_wait_seconds": 65,
    "rate_limit_retry_message": "Retry your exact previous command. This is NOT a bug, was transient rate limit."
  },
  "glm": {
    "wrapper": "~/bin/glm",
    "flags": [],
    "regex_idle": "❯ $",
    "regex_busy": "^(⚒|◐|◑|◒|◓) ",
    "regex_rate_limit": ["429", "quota_exceeded"],
    "rate_limit_wait_seconds": 60,
    "rate_limit_retry_message": "Retry exact command; transient Z.ai limit."
  },
  "codex": {
    "wrapper": "codex",
    "flags": [],
    "regex_idle": "› $",
    "regex_busy": "•",
    "regex_rate_limit": ["429", "rate_limit_exceeded"],
    "rate_limit_wait_seconds": 30,
    "rate_limit_retry_message": "Retry; transient OpenAI limit."
  },
  "grok": { … },
  "kimi": { … },
  "qwen": { … },
  "deepseek": { … },
  "mistral": { … }
}
```

Regex serão preenchidos a partir dos `providers/*.py` do awslabs.

## 4. Papéis e limites

### 4.1 Claude Code (engenheiro-chefe do maestro)

**Pode:**
- Ler qualquer arquivo do workspace (fóruns, snapshots, agenda, configs V4)
- Decidir qual agente ativa em cada ciclo
- Escrever `sprint_para_<agente>.md`
- Chamar `spawn-agent.sh <agente>`
- Escrever em `Cerebro/Foruns/maestro/` (session, ciclos, workers, inbox)
- Escrever em `canal_trindade.md` no formato de sinal do maestro

**NÃO pode (sem autorização Miguel):**
- Publicar conteúdo público (WP, Vercel, Telegram, WhatsApp)
- SSH em servidor (NYC, Tencent, ServerDo.in, cafezinho.news)
- Rodar cron novo em produção
- Autorizar gasto acima de US$ 5/ciclo
- Aprovar próprio trabalho (só Codex ou Miguel aprovam)
- Rename estrutural (Fase 6, silos, etc. — bloqueado pelo sprint V4)

### 4.2 Outros agentes (workers)

Continuam com identidade canônica de sempre (ver `IDENTIDADE_CANONICA.md`). Maestro só ativa, não altera papel de cada um. Se agente recusa sprint ou responde AGUARDANDO_MIGUEL, maestro registra e não força.

### 4.3 Miguel

**Sempre pode:**
- `touch ~/MAESTRO_PAUSADO` — próximo ciclo sai imediatamente, agentes rodando terminam
- `tmux attach maestro` — vê tudo ao vivo, digita em qualquer painel pra intervir
- Editar `config/agentes.json` — mudar comportamento sem tocar código
- `~/ferramentas/maestro/scripts/kill-switch.sh` — mata sessão tmux e heartbeat, preserva estado em disco

## 5. Visibilidade CCTV

### 5.1 Fase 1 (MVP) — tmux tiled

Painel único acessível via `tmux attach maestro`. Layout automático em grid:

```
┌────────────┬────────────┬────────────┐
│ claude     │ codex      │ glm        │
├────────────┼────────────┼────────────┤
│ grok       │ kimi       │ qwen       │
├────────────┼────────────┴────────────┤
│ maestro (log ao vivo, decisões)     │
└──────────────────────────────────────┘
```

`Ctrl-B seta` navega entre painéis. Digitar em qualquer painel = intervenção manual. Zero dependência extra.

### 5.2 Fase 2 (opcional) — Web CCTV

Se Miguel quiser ver do celular ou monitor secundário: FastAPI + WebSocket + xterm.js (padrão do `agentglass` referenciado na pesquisa). Cada agente vira uma iframe xterm ao vivo. Só implementar se demanda real aparecer.

## 6. Fases de implementação

| Fase | Escopo | Estimativa | Bloqueio |
|---|---|---|---|
| **F1** | Fork Primeline, generalizar `spawn-agent.sh` pra receber `AGENT_CLI` param, mapa `agentes.json` só com claude+glm | 2-3h | nenhum |
| **F2** | Copiar regex idle dos providers awslabs pra `providers/*.regex`, expandir agentes.json pros 7 CLIs | 1-2h | F1 |
| **F3** | Adaptar `heartbeat.sh` pra chamar `~/bin/claude` com prompt engenheiro-chefe (não `/orchestrate-cycle` slash-command do Primeline) | 2h | F2 |
| **F4** | Contratos de handoff (sprint_para_<agente>.md com frontmatter), workers/*.json, session.json | 2h | F3 |
| **F5** | Cron `*/15 * * * *` + orch-bootstrap idempotente + kill-switch | 1h | F4 |
| **F6** | Teste ponta-a-ponta com 2 agentes (claude engenheiro-chefe + codex worker) rodando sprint fake em rascunho | 2h | F5 |
| **F7** | Painel CCTV script (`painel_cctv.sh` layout tiled) + README setup | 1h | F6 |
| **F8** | Expandir teste pros 7 agentes reais, validar rate-limit-watchdog com cada provedor | 3-4h | F7 |
| **F9** | (opcional) Web CCTV FastAPI + xterm.js | 4-6h | F8 |

**Total F1→F8:** 14-18h de trabalho meu. Código próprio esperado: ~500-800 linhas (bash + Python leve). Fork Primeline: ~830 linhas mantidas com adaptações.

**F9 é opcional** e só entra se Miguel pedir depois. Fase 1-8 já entrega CCTV via tmux (que é o que Miguel pediu).

## 7. Riscos e mitigações

### 7.1 Riscos técnicos

- **R-T-01: Wrappers `~/bin/claude`/`~/bin/glm` com preload podem gerar loop.** Se Claude é chamado dentro de spawn-agent que é chamado por Claude anterior, preload vai puxar snapshot que menciona "novo ciclo maestro" — Claude pode achar que precisa iniciar outro ciclo em vez de trabalhar no atual. **Mitigação:** flag `MAESTRO_CICLO=1` no env ao chamar; wrapper detecta e pula preload (ou usa preload reduzido). Testar em F3.

- **R-T-02: `--dangerously-skip-permissions` não é universal.** GLM/Kimi/Qwen/Grok podem não aceitar. **Mitigação:** `agentes.json` tem lista `flags` por agente; se agente não aceita, deixar vazio e aceitar prompts de permissão via `tmux send-keys y Enter` (heurística).

- **R-T-03: Regex idle pode falhar em CLI que Miguel atualizar depois.** Se `claude` mudar prompt de `❯` pra outra coisa, heartbeat trava. **Mitigação:** regex em arquivo separado (`providers/*.regex`), Miguel edita sem tocar código. Bug loud (fail-closed): se nenhum regex match em N ciclos, alerta em log e pula agente.

- **R-T-04: Rate-limit em cascata.** Se Anthropic bater 429, Claude engenheiro-chefe também trava (ele é worker do próprio maestro). **Mitigação:** heartbeat detecta se o próprio Claude engenheiro-chefe caiu em rate-limit; se sim, ciclo pula (não força retry, espera próximo cron). Registra em log.

- **R-T-05: Ciclo demora mais que 15min.** Se heartbeat ainda estiver rodando quando próximo cron dispara, dois heartbeats concorrem. **Mitigação:** `orch-bootstrap.sh` usa `flock` ou lock file; se lock ativo, novo cron sai silencioso.

### 7.2 Riscos operacionais

- **R-O-01: Colisão com sprint V4 do Codex.** Codex é engenheiro-chefe do V4, Claude vira engenheiro-chefe do Maestro. Papéis podem conflitar. **Mitigação:** Maestro NÃO decide arquitetura editorial V4 (isso é do Codex). Maestro só distribui rodadas que o Codex já autorizou. Codex mantém veto sobre qualquer sprint que Maestro tentar acionar em `root/v4_labs/`.

- **R-O-02: Custo silencioso.** Agentes rodando em loop podem gerar chamadas pagas repetidas. **Mitigação:** cada sprint tem `custo_maximo_usd` no frontmatter; workers/<agente>.json rastreia gasto acumulado do ciclo; se exceder, próximo ciclo pula esse agente e alerta Miguel. Integra com auditoria Gemini R$ 98 (que já ensinou lição — ver `auditoria_gasto_gemini_98_reais_20260719.md`).

- **R-O-03: Identidade confundida.** Agente pode achar que é outro (repetição do incidente `carta_repreensao_agy_identidade_e_escopo_20260717`). **Mitigação:** sprint_para_<agente>.md sempre começa com `Você é <agente>, empresa <empresa>. NÃO é <outros>.` Reforça `IDENTIDADE_CANONICA.md`.

- **R-O-04: Miguel dorme, maestro faz besteira.** Ciclo autônomo pode aprovar coisa errada, publicar draft indevido, rodar teste caro. **Mitigação:** lista rígida "NÃO pode sem autorização Miguel" (§4.1). Publicação pública sempre bloqueada. Custo/ciclo capado. Rollback via kill-switch + `git status` mostra tudo que mudou.

- **R-O-05: Cron falha silenciosamente.** Se `orch-bootstrap.sh` quebra, Miguel só descobre olhando. **Mitigação:** cada bootstrap grava `Cerebro/Foruns/maestro/ciclos/log_bootstrap_YYYYMMDD.md`; wrapper `~/bin/claude` de próxima sessão avisa Miguel se bootstrap falhou nas últimas N horas.

## 8. Rollback

Nível 1 — pausar temporário: `touch ~/MAESTRO_PAUSADO` (próximo ciclo sai).
Nível 2 — matar sessão atual: `~/ferramentas/maestro/scripts/kill-switch.sh` (mata tmux + heartbeat, preserva estado).
Nível 3 — remover cron: `crontab -e` deleta linha do maestro.
Nível 4 — remover código: `rm -rf ~/ferramentas/maestro/`. Estado em `Cerebro/Foruns/maestro/` fica preservado (é histórico).
Nível 5 — remover estado histórico: `mv "Cerebro/Foruns/maestro/" ~/legacy/maestro_removido_$(date +%Y%m%d)/` seguindo [[feedback_manifesto_antes_de_acao_grande]].

Todos os níveis são reversíveis exceto 5 (que preserva em legacy, também reversível).

## 9. Integração com sprint V4 e canal Trindade

O maestro NÃO substitui o Codex como engenheiro-chefe do V4. Divisão de trabalho:

- **Codex:** decide arquitetura V4, abre/fecha rodadas, aprova patches canônicos, gate final antes de deploy.
- **Maestro (Claude):** entre rodadas ou entre commits do Codex, mantém agentes ativos, executa sprints que Codex já autorizou, coleta resultados, sinaliza no canal Trindade.
- **Miguel:** direção editorial, aprovação de risco, kill-switch.

Sinal do maestro no canal Trindade tem prefixo dedicado:

```
[MAESTRO] ciclo 42 | 2026-07-19 10:15 BRT | ativados: codex, kimi | pendente: grok (idle há 45min) | custo ciclo: US$ 0.03
```

Codex pode responder no canal Trindade com `[MAESTRO-PAUSE codex]` pra suspender ativação de agente específico enquanto ele resolve algo canônico.

## 10. Perguntas abertas pro Miguel (bloqueiam início)

Sem resposta a estas 5 perguntas, não começo F1. Marcam decisões que não posso tomar sozinho:

**P1 — Frequência do ciclo:** 15min, 30min ou adaptativo (15 quando ativo, 60 quando calmo)?

**P2 — Agentes na fase 1:** só claude+codex+glm (mais estáveis) OU incluir kimi+grok+qwen+deepseek desde o começo?

**P3 — Escopo autorizado do maestro em produção:** APENAS labs `root/v4_labs/**` OU também `Projeto Cafezinho Agentes/**` OU também sites temáticos (Rio Carta etc.)?

**P4 — Publicação:** confirmo que maestro NUNCA publica em WP, Vercel, Telegram, WhatsApp mesmo com autorização de agente. Só Miguel autoriza publicação. Correto?

**P5 — Interação Miguel↔Maestro:** quando maestro precisa de decisão urgente (custo alto, risco), como avisa? (a) mensagem em `Cerebro/Foruns/maestro/AGUARDANDO_MIGUEL.md`, (b) notificação WhatsApp via API, (c) mensagem em canal Trindade com prefixo `[MAESTRO-ATENCAO-MIGUEL]`, (d) todas?

## 11. Aceite proposto

Ao aprovar este manifesto, Miguel autoriza:

- [x] Fork de `primeline-ai/claude-tmux-orchestration` em `~/ferramentas/maestro/`
- [x] Cópia de regex dos `providers/*.py` de `awslabs/cli-agent-orchestrator`
- [x] Criação de `Cerebro/Foruns/maestro/` como diretório de estado
- [x] Fases F1→F5 sem interrupção (ciclo mínimo funcionando)
- [ ] Fase F6→F7 depois de F5 aprovada por Miguel
- [ ] Fase F8 (multi-provider real) só depois de F7 aprovada
- [ ] Cron `*/15 * * * *` só depois de F8 aprovada

Ativação do primeiro ciclo em produção requer nova autorização explícita de Miguel após F8.

## 12. Referências

- Pesquisa base: conversa 2026-07-19 09:35 BRT (Claude Code + agente WebSearch)
- Repos clonados: `~/ferramentas/hive_exploracao/` (tmux_orchestrator, aws_cli_orchestrator, primeline_claude_tmux)
- Filosofia manifesto: [[feedback_manifesto_antes_de_acao_grande]]
- Identidade agentes: [[feedback_memoria_identifica_autoria_glm]] + `IDENTIDADE_CANONICA.md`
- Custo lição aprendida: `auditoria_gasto_gemini_98_reais_20260719.md`
- Sprint V4 ativo: `forum_rodada7_tribunal_visual_qwen_gemini_v4_20260719.md`

---

*Manifesto gravado por Claude Code (`claude-opus-4-7`), Anthropic, sessão `CLAUDE-MAESTRO-LOCAL-MANIFESTO-20260719-0945`, em 2026-07-19 09:45 BRT.*
*Distinto de GLM/Ming (Zhipu AI), de Codex (OpenAI), de Grok (xAI).*

**AGUARDANDO REVISÃO DO MIGUEL — 5 perguntas em §10 bloqueiam início.**
