# RUNBOOK — Rodízio do Posto Capador V4.1 (opção b)

**Aprovado:** Miguel 14/09/2026 14:2x BRT chat CLI (após parecer ZM ZM-20260914-003 e recomendação CM-20260914-006).
**Autor:** Claude Miguel (CM · `claude-opus-4-7`).
**Versão:** v1.0 · 14/09/2026 14:2x BRT.
**Substitui:** nenhum (documento novo).

## 1. Por que existe

O passo «capa V4.1» (escolher/gerar imagem + `_thumbnail_id` + `_cafezinho_img_check` + agendamento future) **nunca foi cronizado no Cafezinho** — é trabalho de agente via wp-cli/SSH ou REST (investigação ZM 14/09, [[feedback-pipeline-capa-v41-agente-manual-20260914]]). Quando o operador silencia sem passar bastão, a fila V4.1 acumula sem capa e o site fura (janela 12/09 22:57 → 14/09 05:24 = 30h+ sem capa nova, 13h44min sem publish).

Este RUNBOOK institui **rodízio formal + handoff auditável + integração com alerta automático ZM** para que operador silencioso não vire silêncio operacional.

## 2. Membros aptos ao posto

Somente estes agentes têm autorização Miguel + acesso técnico + treinamento nos 6 gates + Emendas 5/6/11/12 + §86 pra aplicar capa V4.1:

| Slug | Agente | Modelo | Acesso | Emendas dominadas |
|---|---|---|---|---|
| `cm` | Claude Miguel | claude-opus-4-7 | SSH cafezinho-wp root + REST v2 App Password | 5, 6, 11, 12, §86 |
| `agymiguel` | AGY Miguel (Antigravity CLI) | gemini-3.7-flash-high | REST v2 + wp-admin admin conta + bypass Gatekeeper | 5, 6, 11, 12, §86 (comprovado 14/09 Lote 1+2) |
| `cl` | Claude Laura | claude-fable-5-1 | SSH cafezinho-wp `cafezinho-cl` + scripts `/tmp/clNNN.sh` + `/root/cl_funcs.sh` | 5, 6, 11, 12, §86 (histórico) |
| `agylaura` | AGY-LAURA | gemini (Windows) | ordens CL via `/tmp/clNNN.sh` | aplicador secundário (executa scripts CL) |

**Não aptos** (não têm acesso OU não dominam gates OU escopo é outro):
- ZM (papel: infra/investigação/alertas — não aplica capa)
- Astra (papel: revisão pós-publish — pode propor correção, não aplica capa solo)
- Luna (papel: gate único pré-publish — aprova/reprova, não aplica)
- XM/Codex Miguel (papel: auditoria/ronda — read-only)
- Grok Laura (sem crédito desde 28/08 — indisponível)
- ZCode Laura (desligado)
- Agyonor (papel: produção técnica ComexStat/MDIC — não capa V4.1)
- DS-Dell (papel: coleta/diagnóstico — não capa)

## 3. Ordem de turno padrão

Rodízio **por âncora de horário**, não por «minha vez»:

| Faixa BRT | Capador primário | Capador secundário (backup) |
|---|---|---|
| 07:00 – 13:00 | CL | CM |
| 13:00 – 19:00 | CM | AGY-M |
| 19:00 – 23:00 | AGY-M | CL |
| 23:00 – 07:00 (madrugada) | quem estiver acordado; se ninguém, fila acumula até 07:00 | — |

Regras:
- O **primário** é o operador default naquela faixa. Se estiver ativo (heartbeat/state <30min) e sem sinal de saída, quem entra na faixa checa e assume.
- O **secundário** assume se o primário silencia por >45min sem handoff explícito OU se recebe pedido do primário.
- Cada faixa começa com o operador entrando lendo os últimos 5 blocos de `de_dell.md` + a fila V4.1 draft atual (`wp post list --post_status=draft --meta_key=_v4_versao --meta_value=4.1`).
- Fora do horário do primário, qualquer apto pode aplicar capa se detectar fila crescendo — desde que respeite handoff (§4).

## 4. Handoff auditável — protocolo

**Duas mecânicas obrigatórias** pra cada capa aplicada:

### 4.1 Meta persistente no post

Toda aplicação de capa V4.1 grava (em ADIÇÃO às metas dos 6 gates + Emenda 6):

```
_cafezinho_capa_operador = <slug>       # cm | agymiguel | cl | agylaura
_cafezinho_capa_ts_brt   = YYYY-MM-DD HH:MM  # timestamp BRT da aplicação
_cafezinho_capa_metodo   = wpcli|rest|wpadmin  # canal técnico usado
_cafezinho_capa_fonte    = <origem imagem>  # url wikimedia/agência OU ilustração-IA-<gerador>
_cafezinho_capa_handoff  = <slug-anterior>|inicial|solo  # de quem recebeu OU inicial se abrindo turno
```

Exemplo real (posts AGY-M 14/09 hoje): `_publicado_por=agymiguel` (já grava; ampliar com estas metas). Retroativo NÃO é obrigatório — só a partir da adoção.

### 4.2 Bloc na ponte a cada entrada/saída de turno

**Entrada de turno** (obrigatório em cada faixa de 3-6h ou quando assume backup):

```
[YYYY/MM/DD HH:MM BRT] CAPA-ENTRA-<SLUG>-YYYYMMDD-NNN
Capador assumindo: <slug>
Turno anterior: <slug-anterior> (last capa PID <N> HH:MM) | ou "faixa vazia madrugada"
Fila V4.1 agora: <N> drafts sem thumb (mais velho ID <PID> há <Xh>)
Próximas ~2h: pretendo capar/publicar M/agendar future/passar bastão às HH:MM
— <slug> · <modelo> · YYYY-MM-DD HH:MM BRT
```

**Saída de turno** (obrigatório antes de encerrar sessão):

```
[YYYY/MM/DD HH:MM BRT] CAPA-SAI-<SLUG>-YYYYMMDD-NNN
Capador saindo: <slug>
Balanço do turno: <N> capas aplicadas (IDs listados), <M> descartes, <K> ainda pending sem thumb
Fila deixada: <N> drafts sem thumb (mais velho ID <PID> há <Xh>)
Próximo primário: <slug-próxima-faixa>
Pendências passadas: <lista curta se houver>
— <slug> · <modelo> · YYYY-MM-DD HH:MM BRT
```

**Handoff mid-turno** (quando primário pede ajuda ao secundário OU secundário assume por gatilho):

```
[YYYY/MM/DD HH:MM BRT] CAPA-HANDOFF-<SLUG>-YYYYMMDD-NNN
De: <slug-anterior> Para: <slug-novo>
Motivo: <descanso|silêncio 45min|fila estourou|erro técnico|ordem Miguel>
Estado no handoff: <N> drafts sem thumb (IDs listados)
Último post capado: <PID> HH:MM
— <slug-anterior> · <modelo> · YYYY-MM-DD HH:MM BRT
```

## 5. Checklist mínimo por capa (6 gates + Emendas + §86)

Antes de gravar `_thumbnail_id` + `_cafezinho_img_check` num draft V4.1, o operador confirma:

1. **v4_versao=4.1** (`wp post meta get <PID> _v4_versao` = `4.1`).
2. **post_date < 72h** (`wp post get <PID> --field=post_date` vs `date`).
3. **thumb candidato tem MD5 único** — não usar imagem que já tem MD5 registrado em outro post publicado (Emenda 6, §86 v1.1.0 devolve HTTP 400).
4. **imgcheck aprovada:** aplicar `_cafezinho_img_check = APROVADA` + `_cafezinho_featured_carimbo = <MD5>`.
5. **dedup 72h SQL:** query rápida `wp db query "SELECT ID FROM wp_posts WHERE post_status='publish' AND post_title LIKE '%<termo-chave>%' AND post_date >= NOW() - INTERVAL 72 HOUR"` — se hit, verificar se é canibal.
6. **Regional só pesquisa/bastidor** (regra 22/08 [[feedback-regional-pesquisa-eleitoral-ou-bastidor-20260822]]).

**Emendas por tipo de tema:**
- **Geopolítica/eleição/pessoa nomeada:** foto jornalística RECENTE da pessoa real, agência ou Wikimedia Commons CC (Emenda 12 26/08). Nunca canibal institucional. Legenda descreve pixels (CL-011).
- **Tecnologia/IA/abstrato:** capa IA gerada OK, crédito «Ilustração: Cafezinho / <gerador>» na legenda (Emenda 11 26/08). Sem texto dentro da capa.
- **Charge/humor:** sem texto dentro (regra Miguel).
- **Sujeito atacado por foto datada:** blacklist figuras políticas datadas (Ricardo Barros, Osmar Terra, Mandetta, Teich, Pazuello, Queiroga — regra 22/08 267037) em attachments recentes.

**Cadência entre publish (Emenda 5 12/09 AGY-M-guard `cafezinho-slot-20min.php`):** mínimo 20min entre publicações. Use `post_status=future` com agendamento em slot livre se o próximo post cair <20min do último.

**Marca de origem obrigatória** (ZM-20260912-003): `_publicado_por = <slug>` (cm | agymiguel | cl | agylaura) na MESMA chamada do publish.

## 6. Emergência (bypass do rodízio)

Situações que quebram o rodízio e permitem qualquer apto assumir imediatamente:

- **Fila V4.1 ≥5 drafts sem thumb** OU **draft mais velho ≥12h sem thumb** (nível-2 alerta ZM). Não esperar handoff.
- **Furo publish >2h em hora comercial (07-23 BRT)** — regra 29/08 alerta autocura V4 [[feedback-alerta-ponte-cafezinho-telegram-autocura-v4-20260829]].
- **Ordem direta Miguel** no chat/Telegram anulando rodízio.
- **Ping do alerta ZM** endereçado ao operador esperado que não responde em 30min.

Nesses casos: aplicar capa direto + gravar meta `_cafezinho_capa_handoff = emergencia_<motivo>_YYYYMMDD_HHMM` + postar bloc `CAPA-HANDOFF-<SLUG>-YYYYMMDD-NNN` com motivo=emergência explicando por que quebrou rodízio.

## 7. Integração com alerta ZM (opção b — parte técnica)

ZM implementa cron a cada 30min que detecta:
- Nível-1 LEMBRETE: draft V4.1 ≥6h sem thumb → bloc `ALERTA-CAPA-V41-YYYYMMDD-HHMM` na ponte endereçado @capador_da_faixa + @todos_aptos.
- Nível-2 URGENTE: draft ≥12h sem thumb OU fila ≥5 → bloc + Telegram `@pontecafezinhobot`.

Quando alerta chega, o operador da faixa atual tem 30min pra:
- Aplicar capa (situação normal — sinal de que voltou a operar), OU
- Postar bloc respondendo (motivo do delay + ETA), OU
- Passar bastão via `CAPA-HANDOFF-...`

Se 30min sem resposta, secundário da faixa assume (emergência §6).

Ledger ZM em `~/cerebro-miguel/cerebro/monitoramento_horario/alertas_capa_v41/YYYY-MM-DD.jsonl`.

## 8. Métricas de monitoramento (semanal)

Toda sexta-feira 18:00 BRT, capador ativo da faixa gera:
- Total capas aplicadas por operador na semana (via `wp post meta list` filtrando `_cafezinho_capa_operador`).
- Média idade do draft na hora da aplicação (target <4h).
- Nº de alertas ZM emitidos (target <=3/dia).
- Nº de handoffs de emergência (target 0).

Relatório em `~/cerebro-miguel/cerebro/monitoramento_horario/rodizio_capador/YYYY-MM-DD.md`.

## 9. NÃO faz parte do escopo deste RUNBOOK

- Geração de capa via IA cronizada com revisão de visão automatizada — opção (a) do parecer ZM, migração futura só depois de shadow test 1-2 semanas com carimbo `_cafezinho_visao_teste=<hash>` sem publicar solo (por causa do risco Gate 267037 22/08 foto Ricardo Barros).
- Pipeline V4 legacy (autor 5786 sem `_v4_versao=4.1`) — regra 29/08 gate 6 já bloqueia; RUNBOOK cobre só V4.1.
- Pipeline humano Redação (autor 5780 via wp-admin) — Gabriel/Miguel humano têm outro fluxo (mas Astra revisa pós-publish tudo, AST-002 hoje mostrou o bug 270785 «É importante que este site trate…» = valor do gate pós).

## 10. Turno inicial (14/09/2026)

**Vigência a partir de 14:2x BRT, 14/09/2026.**

Faixa 13-19 BRT em curso → **CM (Claude Miguel) capador primário**.
Secundário: AGY-M (que já executou Lote 1+2 hoje, comprovado apto).

Enquanto CL está em missão Dark Horse M1-M5 (autorização Miguel 13:5x, escopo isolado), CL não entra no rodízio até concluir a série e postar CL-20260914-NNN de balanço.

Próxima faixa 19-23 BRT → **AGY-M primário**, CL secundário (se voltar da série).
Faixa madrugada 23-07 → **quem estiver acordado** (não obrigar rondinha). Alerta ZM cobre o gap.
Faixa 07-13 BRT → **CL primário** (se voltar em modo pleno), CM secundário.

## Revisões deste RUNBOOK

Miguel autoriza mudança de qualquer regra. Agentes propõem via bloc `RUNBOOK-CAPA-PROPOSTA-YYYYMMDD-NNN` na ponte + fórum próprio se mudança grande. Aprovação Miguel → nova versão vX.Y aqui + entrada em MEMORY.md.

Ligação com regras vigentes:
- [[feedback-pipeline-capa-v41-agente-manual-20260914]] (motivador do RUNBOOK)
- [[feedback-checagem-dupla-antes-publish-v41-20260829]] (6 gates)
- [[feedback-alerta-ponte-cafezinho-telegram-autocura-v4-20260829]] (autocura + Telegram)
- [[feedback-cm-substitui-cl-se-parar-20260912]] (protocolo emergência CL)
- [[feedback-autonomia-independencia-sistema-20260906]] (autonomia máxima)
- [[feedback-checagem-dupla-antes-publish-v41-20260829]] · [[feedback-gate-img-check-valida-filename-e-title-attachment-20260822]] · [[feedback-regional-pesquisa-eleitoral-ou-bastidor-20260822]]

—
RUNBOOK v1.0 · Claude Miguel (CM · `claude-opus-4-7`) · 14/09/2026 14:2x BRT

## 11. Adendo ZM 14/09 ~16:2x — alerta v1.6: ESCALADA AUTOMÁTICA (ordem Miguel: sem pedir autorização, sem incomodá-lo) + MANUAL DA CAPA

- **Nível-1 (≥6h):** bloc `ALERTA-CAPA-V41-*` → capador da faixa age.
- **Nível-2 (≥12h OU fila ≥5):** bloc `ESCALACAO-CAPA-V41-*` chamando TODOS os aptos (@AGY-Miguel + @AGY-LAURA + @CL + @CM) com ordem direta de APLICAR a capa — quem pegar primeiro aplica; ACK 30min ou o próximo assume (emergência §6).
- **Nível-3 (≥24h E fila persistente ≥6h após escalada anterior):** ÚNICO momento em que o Miguel é incomodado no Telegram (1 aviso/6h; bootstrap 16:17 de 14/09). Não deixe chegar aqui.
- **MANUAL COMPLETO para achar/aplicar capa:** `Estilo/MANUAL_DA_CAPA_CAFEZINHO.md` — 4 rotas (banco de mídia V4 no NYC, fontes abertas Flickr/Commons com links, biblioteca do próprio WP, IA para tecnologia), licenças pode/não-pode, regras editoriais, passo-a-passo wp-cli (img_check ANTES do thumbnail, §86, cache Rocket).
