---
name: Tarefa 8 — Sprint forum_diagnostico_agentes (30/04/2026, Claude líder)
description: Sprint inteira de escalonamento agressivo Cafezinho que Claude executou substituindo Codex (fora). 4 lotes deployados, ~+11 posts/dia + +18 tweets/dia, custo Δ +$5,50/mês.
type: project
originSessionId: 1ae1df20-85d7-41bb-bbbc-9b585beb0594
---
## Contexto

Sprint executada em 30/04/2026 entre ~17:55 e 18:37 BRT. **Codex esgotou limite de assinatura ao redor das 18:00**, Miguel transferiu liderança operacional pra Claude Code (Opus 4.7) com diretiva: *"vai demorar muito isso. vamos codar logo. mas bota antes no fórum com detalhes tudo que você fizer, com fallback bem explicado, faz backup e manda bala. quero o cafezinho publicando mais ainda hoje."*

Diretriz central: **aumento agressivo de volume** pra retomar ritmo de produção do Cafezinho de 1-2 semanas atrás (`forum_diagnostico_agentes.md §11`).

## O que foi entregue

4 lotes deployados em ~30 minutos.

### Lote 4.A — Zizilinda revertida
- `bot_zizi_linda.py:497`: `contexto="economico"` → `contexto="padrao"`
- Capamento de 28/04 (incidente "sangria fantasma") tinha degradado a UX do bot. Miguel reportou.
- MD5: `f61c37a009379ba4a4ac4801a4fdee8a`

### Lote 4.B — Agente Controlado descapotado
- `agente_controlado.py`: 4 hardcodes (linhas 1571/1585/1716/1748) → constantes (`ANTHROPIC_LUXO_MODEL`, `ANTHROPIC_PING_MODEL`, `OPENAI_LUXO_MODEL`, `OPENAI_PING_MODEL`) lendo de `modelos_vivos.json`.
- Bloco de constantes inserido após linha 57 (BRAVE_API_KEY), com fallback hardcoded preservado como rede de segurança.
- Circuit breaker e fluxo decisório de provider preservados — não toquei na lógica interna.
- MD5: `f3652cb9933ebe407c7fc920614e1974`

### Lote 3 — Twitter intervalo agressivo
- `agente_twitter.py:calcular_intervalo_dinamico()`: 1h/45m/2h/4h → **30m/30m/1h/2h**
- Volume Twitter: ~13 → ~31 tweets/dia (ainda safe contra penalização do algoritmo).
- **Achado importante:** espelho local em `Projeto Cafezinho Agentes/root/` estava desatualizado em "Modo Modesto" (4h/4h/5h/8h) — vestígio de capamento anterior. Pull do Tencent → sincronização local feita.
- MD5: `6617297b1a159dfe2142ecb937293266`

### Lotes 1+2 — Crontab
- **Comentados (3 fantasmas):** Historiador, Feminino, Pet (Ferroviário já estava comentado).
- **Fantástico:** `4 */4 * * *` → `4 */2 * * *` (6/dia → 12/dia)
- **China:** `0 8,20 * * *` → `0 */2 * * *` (2/dia → 12/dia) — *maior achado da auditoria, P1 na fila social, $0.29/mês, 4.109 views/mês*
- **Turismo Embratur** reativado: `37 9,13,17,21 * * *` (4/dia)
- **Coletor Eleições** reativado: `23 7,11,15,19 * * *` (4/dia)
- **Produtor Eleições (DRAFT):** `41 9,15,21 * * *` (3 drafts/dia, humano publica)
- MD5 espelho: `7b4b7752574b6e302a0511717645b658`

## Sentinelas preservadas (pré=pós)

| Sentinela | Valor |
|---|---|
| SHELL=/bin/bash | ✓ |
| Linhas ativas | 54 → 54 |
| Temáticos | 8 |
| Autocura | 3 |
| Sync NYC | 1 |

## Padrões técnicos validados

1. **Deploy seguro de Python:** edit local → `python3 -m py_compile` → `scp` pra `/tmp` Tencent → `sudo cp /tmp/X /root/X` → `py_compile` remoto → MD5 local=remoto. Nunca rsync com `-a/-o/-g` em `/root/` (regra crítica do projeto).

2. **Deploy seguro de crontab:** pull do Tencent (`sudo crontab -l > /tmp/X`) → aplicar diff sobre essa base (não confiar em espelho local que pode estar desatualizado) → conferir sentinelas pré-edit → conferir sentinelas pós-edit → push via `sudo crontab /tmp/X`. Backup obrigatório antes.

3. **Pattern de descapotação de hardcode:** bloco de constantes no topo do arquivo, lendo `agent_data/modelos_vivos.json` via `carregar_modelos_vivos()` do roteador, com fallback hardcoded como rede de segurança. Quando atualizador puxa modelo novo, todo call site migra sem patch.

## Achado arquitetural reusável

**Sinergia China/redes JÁ existia** sem trabalho extra: `gerenciador_fila_redes.py:25` lista categoria China (id 4996) em P1. Twitter+Facebook ordenam fila por (prioridade_twitter, data_entrada) — China sempre lidera. Mais volume China = mais reverberação automática nas redes. Não foi preciso criar bot Telegram dedicado nem copy variation pra essa sprint.

## Backups (rollback fácil)

Todos em `/root/*.bkp_pre_claude_sprint_20260430_1939` no Tencent. Timestamp **servidor** (~1h adiantado vs BRT — desencaixe conhecido `project_desencaixe_timestamp_canal_25abr.md`).

Restauração:
```bash
ssh ubuntu@... 'cat /root/crontab_backup_pre_claude_sprint_20260430_1939.txt | sudo crontab -'
ssh ubuntu@... 'sudo cp /root/<arquivo>.py.bkp_pre_claude_sprint_20260430_1939 /root/<arquivo>.py'
```

## Resultado esperado

- **+11 posts publicados/dia** (Fantástico +6, China +10, Turismo +4, -3 fantasmas)
- **+3 drafts/dia** (Eleições, humano publica)
- **+18 tweets/dia** (Twitter intervalo agressivo)
- **Custo Δ:** ~+$5,50/mês

## Janela de validação 24-48h

Conferir após 30/04 18:37 BRT:
- Logs de novos agentes (Turismo, Coletor/Produtor Eleições) — primeira execução cron sem traceback
- Logs Fantástico/China pós-escalonamento (cascata Anthropic + bugfix `gerenciador_tokens` da §9 funcional)
- `[DEDUP-GUARD] Checagem WP falhou` — silent failure indicador
- GA4: curva pageviews 24-48h
- `/root/agent_data/banco_custos.jsonl`: confirmar Δ ~$5,50/mês

## Pendências (próxima sprint)

- **TIPOs 1/2/4 da reversão de modelos** — backlog em `forum_reversao_modelos.md`. Codex deve voltar a esses quando assinatura voltar.
- **Master Trends / Maestro** — prudência mantida. Codex em §6.4 levantou suspeita de matching slug/categoria que precisa investigação antes de mexer.
- **Sinergia copy variation Twitter** — opcional, fora do escopo desta sprint. Variação de copy/threads por post China daria mais alcance.

## Âncoras pra recuperar contexto

- `Foruns/forum_diagnostico_agentes.md` §12-15 (proposta + execução)
- `Foruns/forum_reversao_modelos.md` (sprint paralela do Codex, TIPO 3 fechado por ele 17:02 BRT)
- `Foruns/forum_otimizacao_custos.md` em `Projeto Cafezinho Agentes/Foruns/` (origem 28/04 do capamento que essa sprint reverteu parcialmente)
- `Foruns/canal_claude_antigravity.md` (raiz) — indicadores 18:23 e 18:36 BRT
- `Projeto Cafezinho Agentes/criticisms_memory.md §5, §6, §7` — regras compartilhadas Antigravity/Codex/Claude

## Lição transferível

**Espelho local não é fonte de verdade automática.** O `agente_twitter.py` local estava em "Modo Modesto" enquanto o Tencent já estava em modo intermediário — alguém (Codex, Antigravity ou Miguel) editou direto no Tencent sem sincronizar pro local. **Antes de editar qualquer arquivo Python ou crontab que possa ter sido tocado em produção, sempre puxar a versão atual do Tencent.** O espelho serve pra deploy outbound; pra base de leitura, Tencent é canônico.
