# Monitor Cafezinho 30min v2 — manifesto de arranque (revisado)

**Data v1:** 2026-07-19 17:30 BRT (frequência 60min, só leitura)
**Data v2:** 2026-07-19 17:50 BRT (frequência 30min, escrita autorizada, Opus tempo inteiro)
**Autor:** Claude Code / Anthropic (`claude-opus-4-7`), engenheiro-chefe + editor-chefe do Baleia Azul
**Sessão:** `CLAUDE-CHEFE-ECOSSISTEMA-20260719-1020`
**Status:** MANIFESTO V2 PROPOSTO — AGUARDANDO ÚLTIMAS 5 RESPOSTAS DO MIGUEL
**Categoria:** blast radius **muito alto** (escrita em produção autorizada) → aplicação estrita de [[feedback-manifesto-antes-de-acao-grande]] + [[feedback-cron-como-codigo-producao]]

**Alerta de nomenclatura:** Monitor Cafezinho ≠ Maestro Local (que aguarda 13 respostas em `forum_maestro_local_v2_20260719.md`). Monitor é vigilância com autocura de escopo restrito; Maestro é orquestrador multi-CLI genérico.

---

## 0. Diferenças vs v1

| Item | v1 | v2 |
|---|---|---|
| Frequência | `0 * * * *` (1h) | `*/30 * * * *` (30min) — dobra pra **1440 execuções em 30d** |
| Modelo | Sonnet 4.6 padrão + Opus escalada | **Opus 4.7 tempo inteiro** |
| Chamada Claude | Anthropic SDK (API paga) | `~/bin/claude-max.sh` (Plano Max, sem custo de token) |
| Escopo Claude | Só leitura + relatório | **Escrita autorizada:** autocura + correção posts + fact-check |
| Cap financeiro | US$ 8/dia hard-stop | N/A (Plano Max); **cap operacional:** N mudanças em produção por ciclo |
| Duração | 30 dias | 30 dias (idem) |
| Agentes V4 ativos | Só monitorar | Monitorar + coordenar com geopolítica V4 + ciência V4 (religados hoje pelo Miguel) |
| Providers LLM externos | Só Anthropic | Anthropic (Opus, análise) + Gemini (fact-check Grounding) |

## 1. Autorização explícita registrada

Em 2026-07-19 17:45 BRT, no chat Claude Code CLI, Miguel autorizou explicitamente:

> "monitoramento de 30 em 30 minutos, com autocura, corrigindo posts, revisando, lendo, fact-check"
> "pode usar o opus o tempo inteiro. eu tenho assinatura max. preciso usar meu credito"
> Resposta afirmativa à pergunta "Autoriza Monitor Cafezinho fazer autocura+correção de posts+fact-check em modo LLM automatizado 30 em 30min por 30 dias?" → **"Sim, autorizo escrita explícita"**

Isso **complementa** a carta de passagem §21 de 10:20 BRT hoje. Autorização vigente apenas para o Monitor Cafezinho neste manifesto, escopo restrito abaixo. **NÃO** autoriza Claude a publicar posts NOVOS, publicar em Vercel/Telegram, mudar cron em servidor, ou aplicar decisões editoriais fora do escopo autocura/correção.

## 2. Objetivo

A cada 30 minutos, por 30 dias contínuos:

1. **Coletar** UptimeRobot, audiência GA4, publicação WP, crontab NYC+Tencent, Prometheus, estado agentes V4 (geopolítica + ciência)
2. **Analisar** com Opus 4.7: publicação subiu/caiu, audiência subiu/caiu, saúde do site, anomalia em cron
3. **Ler** posts publicados nas últimas 24h (amostra) — verificar título, lide, fact-check
4. **Fact-check** posts amostrados via Gemini Grounding (integração com módulo V4 existente)
5. **Autocurar** correções seguras (§4.1 abaixo): typo, formatação markdown quebrada, categoria errada por regex ancorado em lide, tag errada por padrão factual
6. **Propor** correções semânticas em rascunho (§4.2) sem aplicar automaticamente — Miguel revisa
7. **Alertar** anomalia grave → `AGUARDANDO_MIGUEL.md` + email extra
8. **Reportar** ciclo em `Cerebro/monitoramento_horario/YYYY-MM-DD/HHhMM_ciclo.md`

## 3. Agentes V4 ativos (contexto crítico)

Miguel religou hoje (2026-07-19, hora exata a confirmar):

- **Agente geopolítica V4** — pipeline V4 completo pra pauta geopolítica
- **Agente ciência V4** — pipeline V4 completo pra pauta científica

Monitor deve:
- Ver estado desses agentes a cada ciclo (processos, últimas execuções, filas)
- Não interferir nos agentes (Monitor não pausa/reativa)
- Reportar se algum desses agentes cai/trava/gera custo anômalo
- Fact-checkar posts publicados por eles

**Miguel: qual endpoint/PID/log path desses agentes pra Monitor observar?** (pergunta Q8 abaixo)

## 4. Escopo de escrita em produção

### 4.1 Correções AUTO-APLICADAS (baixo risco)

Monitor pode editar via REST API WP sem revisão prévia, mas SEMPRE:

- Log da mudança em `Cerebro/monitoramento_horario/mudancas_aplicadas/YYYY-MM-DD.jsonl`
- Diff completo preservado (antes/depois)
- Rollback via API WP com 1 comando (função disponível no Monitor)
- Cap: **10 correções auto-aplicadas por ciclo** (evita massa)

Tipos de correção auto-aplicáveis:
- Typo óbvio ancorado em contradição interna (ex.: "Bnaco" → "Banco" quando lide diz "Banco Central")
- Formatação markdown quebrada (link `[texto)`, imagem sem alt-text — se WP tiver alt no media_id)
- Categoria/tag WP errada por padrão factual (post sobre "petróleo" sem tag "petróleo")
- Data em formato quebrado no lide (padroniza pt-BR: `19 de julho de 2026`)

**Regra derivada do incidente Copa do Mundo post 262153** (auditor GPT alucinou negação): correção só aplica se houver **contradição interna** no próprio post (não busca externa). Aplicação do padrão do §10 e §11 da carta de passagem.

### 4.2 Correções em RASCUNHO (semânticas, aguardam Miguel)

Monitor GRAVA proposta em `Cerebro/monitoramento_horario/propostas_correcao/<post_id>_<slug>.md` mas **não aplica**:

- Reformulação de manchete
- Reescrita de lide
- Adição de contexto que não está no post
- Rebaixamento de categoria
- Despublicação (unpublish) — **JAMAIS auto-aplicada, mesmo em rascunho é sensível**
- Qualquer mudança que altere sentido/tom/ângulo

Miguel revisa `propostas_correcao/` e aplica manual (ou eu aplico após autorização escrita por post).

### 4.3 PROIBIDO em qualquer modo

- Publicar post NOVO
- Despublicar post existente (rebaixar pra draft/rascunho)
- Mudar autor
- Mudar data de publicação
- Mudar featured image
- Modificar cron/systemd em qualquer servidor
- Modificar código de qualquer agente
- Rotacionar credenciais
- Aprovar próprias mudanças (Miguel revisa `mudancas_aplicadas/` diariamente OU Codex faz auditoria amostral semanal)

## 5. Arquitetura técnica

```
~/ferramentas/monitor_cafezinho/
├── scripts/
│   ├── monitor_ciclo.sh          # entry point cron — bash orquestrador
│   ├── coletar_todas_fontes.py   # paralelo 6 fontes + agentes V4
│   ├── analisar_via_claude.sh    # chama ~/bin/claude-max.sh com prompt+payload
│   ├── aplicar_correcoes.py      # aplica correções auto (§4.1) via REST WP
│   ├── gravar_propostas.py       # grava rascunhos (§4.2) em disco
│   ├── verificar_v4_agentes.sh   # observa geopolítica+ciência V4
│   └── kill_switch.sh            # touch ~/MONITOR_PAUSADO ou análise remota
├── config/
│   ├── monitor.env               # WP_APP_PASSWORD, GEMINI_API_KEY, kill-switch path
│   ├── prompts_analise.md        # prompt do Claude externalizado
│   ├── correcoes_seguras.yaml    # regex de correções auto-aplicáveis (versionável)
│   └── posts_amostra_config.yaml # quantos posts revisar por ciclo (padrão: 5)
├── logs/
│   ├── log_execucoes.jsonl       # persistente, rotação diária
│   └── log_mudancas_wp.jsonl     # todo write no WP com diff
└── README.md
```

Estado no workspace:
```
Cerebro/monitoramento_horario/
├── 2026-07-19/
│   ├── 18h00_ciclo.md            # relatório humano
│   ├── 18h00_dados.json          # payload bruto
│   ├── 18h30_ciclo.md
│   └── ...
├── mudancas_aplicadas/
│   ├── 2026-07-19.jsonl          # cada correção auto com diff
│   └── ...
├── propostas_correcao/
│   ├── 262170_manchete_reformulada.md
│   └── ...
├── AGUARDANDO_MIGUEL.md          # alertas ativos
├── SNAPSHOTS_CRON/               # diff cron NYC + Tencent por hora
└── observadores_v4/              # snapshots agentes geopolítica+ciência
```

## 6. Fluxo por ciclo (com escrita)

```
CRON `*/30 * * * *`
    ↓
monitor_ciclo.sh:
    1. Verifica ~/MONITOR_PAUSADO → sai
    2. flock (evita concorrência)
    3. Coleta paralela 6 fontes + agentes V4 (30s timeout)
    4. Amostra 5 posts publicados nas últimas 24h (config)
    5. Prepara payload JSON: dados + posts amostrados + últimos 3 ciclos
    6. Chama ~/bin/claude-max.sh com prompt externo + payload
       → Claude retorna JSON: {analise, correcoes_auto[], propostas_rascunho[], severidade, alerta}
    7. Se correcoes_auto tem itens (≤10):
       - Cada uma: rodar Gemini Grounding se envolve fato factual
       - Se Grounding confirma OU se é typo/formatação (não precisa Grounding):
         - aplicar via REST WP (PUT /wp-json/wp/v2/posts/<id>)
         - log em mudancas_aplicadas/YYYY-MM-DD.jsonl com diff completo
       - Se Grounding contradiz: mover pra propostas_rascunho
    8. Se propostas_rascunho tem itens:
       - Cada uma vira arquivo em propostas_correcao/
       - Não aplica
    9. Se severidade = 🚨:
       - Append AGUARDANDO_MIGUEL.md
       - Email extra pro Miguel (via emissor Baleia)
    10. Grava relatório YYYY-MM-DD/HHhMM_ciclo.md
    11. Log em logs/log_execucoes.jsonl
    12. Sai
```

## 7. Riscos e mitigações (expandidos)

Todos os 8 riscos do v1 continuam. Adiciono 8 novos por causa da escrita:

| ID | Risco | Mitigação |
|---|---|---|
| M-09 | Auto-correção em massa (bug de regex aplica em 100 posts) | Cap 10 correções/ciclo hardcoded no `aplicar_correcoes.py` |
| M-10 | Correção alucina (auditor GPT copa mundo 262153) | (a) contradição interna obrigatória, (b) Grounding pra factuais, (c) rollback com 1 comando |
| M-11 | Post editado ao vivo pelo humano enquanto Monitor edita | Verificar `modified_gmt` antes de PUT; se mudou desde read, aborta e reagenda |
| M-12 | Diff perdido → rollback impossível | log `mudancas_aplicadas/YYYY-MM-DD.jsonl` com estado antes+depois; verificar via `jq empty` após grava |
| M-13 | Plano Max hit limit | monitor_ciclo detecta erro rate-limit → grava ciclo como "LLM_UNAVAILABLE", tenta próximo ciclo; alerta se 5 consecutivos falharem |
| M-14 | WP App Password vazado | credencial em `~/ferramentas/monitor_cafezinho/config/monitor.env` chmod 600 (padrão bug scp corrigido hoje); filtro regex antes de log |
| M-15 | Miguel não revisa `mudancas_aplicadas/` → correções erradas acumulam | Baleia Azul diário 8h destaca "N correções auto ontem"; se Miguel não revisar em 3 dias, Monitor pausa auto |
| M-16 | Fact-check via Gemini estoura crédito de novo (R$ 98 do 18/07) | Cap 20 Grounding queries/ciclo; monitorar `motor_coletor:curadoria` que não deve reaparecer (11 coletores V3 pausados) |

## 8. Duração e expiração

- **Início:** 2026-07-19 (a confirmar horário, resposta Q10)
- **Fim automático:** 2026-08-18 23:59 BRT (30 dias exatos, hardcoded no script; após, cron sai silencioso)
- **Renovação:** manual pelo Miguel via edição do arquivo `EXPIRATION_DATE` no config
- **Kill-switch:** `touch ~/MONITOR_PAUSADO` (imediato)

## 9. Rollback (5 níveis, herdado do v1)

Igual v1 §9. Adicional: rollback de correções WP aplicadas via `aplicar_correcoes.py --rollback <mudanca_id>` que reverte diff usando estado gravado em `mudancas_aplicadas/`.

## 10. Perguntas ao Miguel (v2 — 6 restantes)

**Q3 (herdado)** — Hard stop diário: N/A porque Max é sem custo por chamada. Mas **cap operacional de mudanças em produção por dia**? Sugiro 100 correções auto-aplicadas/dia. OK?

**Q4 (herdado, ainda válido)** — Alerta anomalia: email extra IMEDIATO pra `migueldorosario@gmail.com` OU só `AGUARDANDO_MIGUEL.md` pro próximo Baleia consumir?

**Q5 (herdado)** — Início: HOJE 18h/19h/20h ou amanhã 8h junto com Baleia #13?

**Q6 (herdado, ajustado)** — 30 dias exatos (até 2026-08-18) ou avaliar em 7 dias?

**Q7 (herdado)** — Prometheus: você tem endpoint específico? Ou parser HTML do painel?

**Q8 (novo)** — Agentes V4 religados (geopolítica + ciência): qual PID/path/log/endpoint desses agentes pra Monitor observar? Ou você prefere que eu SSH em NYC e faça auto-detect por processos python contendo "geopolitica" e "ciencia"?

## 11. Aceite (v2)

Ao aprovar, Miguel autoriza:

- [x] Autorização escrita explícita registrada (§1)
- [ ] Criar `~/ferramentas/monitor_cafezinho/`
- [ ] Testar 6 coletores + observador V4 + verificação Grounding + PUT WP com post-teste-draft
- [ ] Instalar cron `*/30 * * * *` no crontab local Miguel
- [ ] Rodar 30 dias com kill-switch ativo
- [ ] Aplicar correções auto (cap 10/ciclo, 100/dia)
- [ ] Gravar propostas semânticas em disco (sem aplicar)
- [ ] Alertar anomalia grave via email + `AGUARDANDO_MIGUEL.md`
- [ ] Fact-check via Gemini Grounding em posts amostrados
- [ ] Baleia Azul diário 8h/18h destaca "N correções auto no dia anterior + M propostas rascunho aguardando revisão"

Após aceite + resposta às 6 perguntas: F0 arranca em ~60min (setup) e primeiro ciclo dispara na próxima meia hora cheia.

## 12. Auditoria e revisão

- **Codex** — auditor semanal amostral (Miguel pode delegar por escrito quando quiser)
- **DeepSeek** — pode fazer auditoria quinzenal das correções aplicadas
- **Miguel** — revisão diária de `mudancas_aplicadas/YYYY-MM-DD.jsonl` recomendada (Baleia destaca)

---

*Manifesto v2 gravado por Claude Code (`claude-opus-4-7`), Anthropic, sessão `CLAUDE-CHEFE-ECOSSISTEMA-20260719-1020`, em 2026-07-19 17:50 BRT.*
*Substitui manifesto v1 do mesmo dia 17:30 BRT.*
*Distinto de Maestro Local, Autocura V4 (determinística), Auditor de Títulos GPT (10min), Fact-check Gemini standalone.*

**AGUARDANDO 6 RESPOSTAS FINAIS DO MIGUEL — Q3, Q4, Q5, Q6, Q7, Q8 em §10.**
