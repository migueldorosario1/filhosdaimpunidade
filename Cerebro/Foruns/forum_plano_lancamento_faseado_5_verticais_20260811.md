# Fórum — Plano de lançamento FASEADO: 1 vertical/dia (12→16/08/2026)

**Data:** 2026-08-11 ~19:25 BRT
**Sessão:** ZCode GLM-5.2 (arquiteto da frente)
**Decisão Miguel (11/08):** "hoje à noite já temos outra missão. vamos lançar uma nova vertical por dia." → **NÃO ligar nada hoje**; lançar 1 vertical/dia a partir de **12/08 à noite**.

> Estado técnico já está **PRONTO** (memória `memoria_v4_5_verticais_encanamento_local_20260811.md`). Este fórum é o **runbook** dos 5 dias de lançamento.

---

## Estado técnico (confirmado, 11/08) — pronto para lançar
- ✅ 8 correções da 1ª auditoria do Codex + 2 da 2ª (lock global + quarentena 21) + fontes RSS válidas (volume recuperado: 9-19 new/vertical)
- ✅ Contratos carregando certo (v4_economia etc., rota premium v4_super_luxo_redacao)
- ✅ Banco de Mídia Ouro consulta as 5 novas; cultura com bloqueio absoluto de IA
- ✅ Lock global de redação (flock /tmp/v4_redacao_global.lock) — teste concorrente validado
- ✅ py_compile OK, deploy íntegro, backups no servidor (`/root/.bak_pre_*`)
- ⏳ Cron **desligado** (ligar 1 vertical por dia, abaixo)

## Pré-requisito antes do Dia 1 (recomendado, temos tempo)
- **3ª auditoria do Codex** — ele disse que seria "curta e objetiva" agora que as 4 condições estão atendidas (quarentena, recoleta, lock global, cron+teste de lock mostrados). Peço a ele nas próximas horas (hoje ainda).

## Ordem de lançamento + justificativa (do mais robusto ao mais delicado)

| Dia | Data | Vertical | candidatas new | Por que esta ordem |
|---|---|---|---|---|
| **1** | 12/08 (noite) | **Economia** (cat 43) | 19 | Maior volume · texto só · sem complexidade de imagem IA |
| **2** | 13/08 | **Cultura** (cat 79) | 11 | Briefing nobre pré-existente · **sem IA** (Flickr+V4) |
| **3** | 14/08 | **Meio Ambiente** (cat 582) | 15 | Volume bom · RSS O Eco/Mongabay sólidos |
| **4** | 15/08 | **Saúde** (cat 258) | 9 | Sem alarmismo/negacionismo · lastro Min Saúde/OPAS |
| **5** | 16/08 | **Esporte** (cat 1271) | 18 | Fact-check rigoroso (placar) · escopo geral |

> **Ordem confirmada pelo Miguel (11/08):** economia → cultura → meio ambiente → saúde → esporte.

## Runbook de cada dia (o que fazer ao lançar uma vertical)

1. **Adicionar a 1 linha no crontab do NYC** (comando abaixo, por vertical).
2. **Confirmar** que o worker rodou (log): `tail /root/agent_data/v4_verticals/<vertical>_drafts.log`.
3. **Monitorar 24h**: quantos drafts gerados no WP, qualidade do texto, imagem resolvida (real vs image_pending).
4. **Aprovar/publicar** os melhores drafts no WP (ou ajustar contrato se o tom sair errado).
5. **Critério de sucesso** (abaixo) → se verde, no dia seguinte somar a próxima vertical.
6. **Rollback** se problema: comentar/remover a linha do cron (pára imediato); bancos e rascunhos preservados.

## Cron — linhas exatas (adicionar 1 por dia no `crontab -e` do NYC)

Padrão (igual às 3 ativas): `flock -n /tmp/v4_<vertical>.lock` envolve coletor + intake + worker. O worker ainda tem o lock **global** interno de redação.

```
# Dia 1 — ECONOMIA (12/08) — 19 new · texto só
35 */4 * * * /usr/bin/flock -n /tmp/v4_economia.lock /bin/bash -lc 'cd /root && . /root/chaves.sh && /root/venv/bin/python3 /root/coletor.py eco >> /root/agent_data/v4_verticals/economia_cron.log 2>&1; /root/venv/bin/python3 /root/v4_vertical_intake.py economia >> /root/agent_data/v4_verticals/economia_cron.log 2>&1; /root/venv/bin/python3 /root/v4_vertical_draft_worker.py economia >> /root/agent_data/v4_verticals/economia_drafts.log 2>&1'

# Dia 2 — CULTURA (13/08) — 11 new · SEM IA (Flickr+V4)
5  */4 * * * /usr/bin/flock -n /tmp/v4_cultura.lock /bin/bash -lc 'cd /root && . /root/chaves.sh && /root/venv/bin/python3 /root/coletor.py cul >> /root/agent_data/v4_verticals/cultura_cron.log 2>&1; /root/venv/bin/python3 /root/v4_vertical_intake.py cultura >> /root/agent_data/v4_verticals/cultura_cron.log 2>&1; /root/venv/bin/python3 /root/v4_vertical_draft_worker.py cultura >> /root/agent_data/v4_verticals/cultura_drafts.log 2>&1'

# Dia 3 — MEIO AMBIENTE (14/08) — 15 new
15 1,9,17 * * * /usr/bin/flock -n /tmp/v4_meio_ambiente.lock /bin/bash -lc 'cd /root && . /root/chaves.sh && /root/venv/bin/python3 /root/coletor.py amb >> /root/agent_data/v4_verticals/meio_ambiente_cron.log 2>&1; /root/venv/bin/python3 /root/v4_vertical_intake.py meio_ambiente >> /root/agent_data/v4_verticals/meio_ambiente_cron.log 2>&1; /root/venv/bin/python3 /root/v4_vertical_draft_worker.py meio_ambiente >> /root/agent_data/v4_verticals/meio_ambiente_drafts.log 2>&1'

# Dia 4 — SAÚDE (15/08) — 9 new · sem alarmismo
15 3,11,19 * * * /usr/bin/flock -n /tmp/v4_saude.lock /bin/bash -lc 'cd /root && . /root/chaves.sh && /root/venv/bin/python3 /root/coletor.py sad >> /root/agent_data/v4_verticals/saude_cron.log 2>&1; /root/venv/bin/python3 /root/v4_vertical_intake.py saude >> /root/agent_data/v4_verticals/saude_cron.log 2>&1; /root/venv/bin/python3 /root/v4_vertical_draft_worker.py saude >> /root/agent_data/v4_verticals/saude_drafts.log 2>&1'

# Dia 5 — ESPORTE (16/08) — 18 new · fact-check placar
15 2,10,18 * * * /usr/bin/flock -n /tmp/v4_esporte.lock /bin/bash -lc 'cd /root && . /root/chaves.sh && /root/venv/bin/python3 /root/coletor.py esp >> /root/agent_data/v4_verticals/esporte_cron.log 2>&1; /root/venv/bin/python3 /root/v4_vertical_intake.py esporte >> /root/agent_data/v4_verticals/esporte_cron.log 2>&1; /root/venv/bin/python3 /root/v4_vertical_draft_worker.py esporte >> /root/agent_data/v4_verticals/esporte_drafts.log 2>&1'
```

> Cadências: cultura/economia 4h; meio_ambiente/esporte/saude 8h (3x/dia). Lock global cuida da concorrência entre as 8 verticais.

## Critérios de sucesso por vertical (24h após ligar)
- **Volume**: ≥ 3 drafts gerados (status draft no WP) nas primeiras 24h.
- **Qualidade**: tom alinhado ao contrato (ex.: economia = dado concreto + consequência material; sem catastrofismo em saúde/meio ambiente).
- **Imagem**: ≥ 50% dos drafts com imagem resolvida (real: Banco Ouro/WP/Flickr/Commons); o resto em `image_pending` (Ponte Claude-Kimi caça).
- **Sem erros**: sem `worker_exception`, sem queda do LLM adapter, sem estouro de cota de IA (cultura: zero IA).

## Rollback (por vertical)
- **Parar**: comentar/remover a linha do cron daquela vertical (pára em até 4-8h, no próximo disparo).
- **Reverter deploy**: backups em `/root/.bak_pre_v4_novas_20260811/` (contratos/mapa/código) e `/root/.bak_pre_quarentena_20260811/` (bancos).
- **Limpar drafts ruins**: os drafts ficam no WP como `draft` (não publicados) — pode excluir manualmente.

## Pendências fase 2 (não bloqueiam o lançamento)
- Fallback não-silencioso de editoria nobre no `V4LLMAdapter` (erro em vez de cair no repetidor).
- Orientação de parágrafos no núcleo canônico (`v4_nucleo_editorial_redacao_v1.md`).
- Resolver redirect do Google News (opcional — RSS diretos já cobrem).
- TTL do estoque por section (hoje padrão 6h; alinhar a 4h/8h).

## Continuidade
A cada dia de lançamento, atualizar este fórum (data + resultado) e o `MONITORAMENTO_DE_TRABALHO.md`. O Codex pode auditar cada vertical pós-lançamento (monitorando os primeiros drafts em vez de pré-ligação).
