# [CLAUDE-F2-CONSTRUCAO-AUTOCURA-V4-MIDIA]

**Data:** 2026-08-07 02:30 BRT
**De:** Claude Code (Anthropic, `claude-opus-4-7`), ambiente `claude-code`, sessão iniciada 06/08 16:21 BRT
**Para:** Miguel do Rosário + Trindade (Grok, Antigravity, Kimi K3, Codex)
**Referência:** carta convocatória Miguel via Kimi K3 07/08 ~02:20 BRT

---

## Veredito: **ACEITO** integralmente + previsão REAL de entrega

**Não repito o erro da minha R1** ("48h" apresentado como concretude sem código). Estimativa realista abaixo com margens.

---

## 1. Entregável meu confirmado

**`gate_pre_publish.py` v0.1** com 3 gates independentes (feature flags), modo shadow, emitindo recibos v0.1.1 validados pelo `receipt_validator.py` do Kimi K3 em `inbox/claude/`.

### Escopo dos 3 gates (fielmente conforme carta Miguel)

| Gate | Sinal detectado | Ação L1 | Ação se ambíguo |
|---|---|---|---|
| **1. `link_publico_controle_para_ocafezinho`** | `resp['link']` contém `controle.ocafezinho.com` | `.replace()` determinístico + curl HEAD verify 200 | não há ambíguo (é match binário) |
| **2. `ia_em_vertical_proibido`** | featured `slug` matches `v4-featured-*` OU `caption` contém `Flux Pro`/`Ilustração` E vertical ∈ `{nacional, regional_*, temáticos, yt, opiniao}` | pending + tag `[PONTE-CLAUDE-KIMI-IMAGEM]` + recibo `reason_code: FEATURED_MEDIA_AI_IN_FORBIDDEN_VERTICAL` | pending humano |
| **3. `html_anchor_split_word`** | regex `<a[^>]*>[a-z]{1,4}</a>[a-z]` no corpo (âncora colada dentro de palavra) | **unwrap determinístico**: mover âncora pra ANTES ou DEPOIS da palavra completa (preserva 100% palavras do worker V4) + recibo `reason_code: HTML_ANCHOR_STRIPPED` | pending (reescrita NUNCA é L1 — carta Miguel explícita) |

### Não-escopo (explícito, pra evitar drift)
- ❌ Sem gate de duplicata semântica (fica pra v0.2 quando spec estiver madura)
- ❌ Sem gate de tempo verbal / gênero fonte (não é limpeza determinística, é editorial)
- ❌ Sem chamadas de LLM (gate é puro determinístico local)
- ❌ Sem escrita no `ledger/` (só drop-file em `inbox/claude/` conforme contrato §2)

---

## 2. Matriz de prontidão (schema R4)

| Campo | Resposta REAL |
|---|---|
| **Artefato** | `gate_pre_publish.py` v0.1 + `test_gate_pre_publish.py` |
| **Estado real** | **planned** (spec detalhada, zero código escrito) |
| **Path** | `/home/migueldorosario/ferramentas/sentinela/gate_pre_publish.py` + `test_gate_pre_publish.py` |
| **Escrita** | zero — nenhum arquivo criado ainda |
| **Dependências** | (a) `sentinela_ciclo.py` (existe); (b) `/home/migueldorosario/ZCodeProject/media_ledger/receipt_validator.py` (existe, validado pelo Kimi K3 com 18/18 testes); (c) meu JSONL `bugs_2026-08-06.jsonl` (54 entradas) + `bugs_2026-08-07.jsonl` (fresh) — fonte de casos de teste |
| **Testes planejados** | (a) unit tests por gate (positive + negative + edge cases); (b) integration test rodando contra últimos 30 publish/pending do meu JSONL 06-07/08 com aceite **≥90% concordância** com decisões manuais; (c) validação de cada recibo emitido via `receipt_validator.py --strict` |
| **Custo runtime** | Desprezível (string ops + regex + `curl -I`); estimado <100ms por publish |
| **Rollback** | 3 flags `.env` independentes (`GATE_LINK_PUBLICO=on/off`, `GATE_IA_VERTICAL=on/off`, `GATE_HTML_ANCHOR=on/off`); todas off = comportamento antigo (meu loop atual sem gate). Documentação em README próprio. |
| **reason_codes usados** | `LINK_ADMIN_REPORTED`, `FEATURED_MEDIA_AI_IN_FORBIDDEN_VERTICAL`, `HTML_ANCHOR_STRIPPED` (taxonomia v0.1.1) |
| **Quem pode ativar** | Miguel via decisão explícita (`[MIGUEL-AUTORIZA-GATE-X-YYYY-MM-DD-HH:MM]` no canal) |
| **Modo entrega inicial** | **shadow only** — gate rodará, decidirá, emitirá recibo em `inbox/claude/`, mas NÃO fará wp_post (meu loop Vigília continua fazendo publish manual em paralelo até Miguel homologar) |
| **Bloqueio atual** | Zero (contrato inbox + validator estão prontos, tenho referências, tenho dados de teste no meu JSONL) — **posso começar dev agora** |

---

## 3. Previsão REAL de entrega

**Compromisso: até 2026-08-08 23:59 BRT** (~45h corridas a partir de agora, com folga de 6h antes do deadline 09/08 06:00 sugerido).

### Cronograma detalhado (18h de dev efetivo distribuído)

| Bloco | Tarefas | Est. |
|---|---|---|
| **07/08 03:00-05:00** | Skeleton do módulo + gate 1 (link público, o mais simples) + unit tests + primeiro recibo válido pelo validator do Kimi | 2h |
| **07/08 (ciclos vigília)** | Gate 2 (IA em vertical proibido) — regex slug/caption + detecção vertical por `zizi_job_id`/`categories` + unit tests | intermitente ~3h |
| **08/08 madrugada (NOITE)** | Gate 3 (HTML unwrap determinístico) — casos: (a) 1 âncora simples, (b) múltiplas âncoras, (c) âncora no meio de palavra composta ("porta-voz"), (d) case sensitivity, (e) fallback ambíguo → pending | 4h |
| **08/08 08:00-14:00** | Integration test contra últimos 30 publish/pending do JSONL 06-07/08; iterar até ≥90% concordância; documentar divergências (casos edge que fogem do gate — vira roadmap v0.2) | 4h |
| **08/08 15:00-20:00** | Feature flags + README + drop-file emission (formato correto: `DROP_claude_YYYYMMDD_HHMMSS_seq.jsonl` atomic write via `.tmp` + rename) + smoke test rodando end-to-end (gate detecta → recibo → drop em `inbox/claude/` → validator OK) | 3h |
| **08/08 21:00-23:59** | Emitir recibo `delivered` no ledger + carta de entrega + buffer pra correções de última hora | 2h |

### Risco no cronograma
- **Alto**: interrupções pra loop Vigília (ciclos DIA :17/:47 + NOITE :17). Mitigação: escrevo gate 1+2 em blocos entre ciclos; gate 3 e testes em blocos longos madrugada/tarde.
- **Médio**: complexidade real do gate 3 (HTML) — se casos edge do meu JSONL revelarem padrões complexos, pode estourar. Mitigação: se >6h, corto escopo pro caso mais comum (âncora simples dentro de palavra) e documento outros como `KNOWN_LIMITATIONS`.
- **Baixo**: mudanças no `receipt_validator.py` do Kimi. Mitigação: fixo commit SHA da versão que uso.

### Se travar
- Se não conseguir 09/08 06:00: escalação obrigatória via `inbox_trindade/miguel.md` com tag `[CLAUDE-F2-DELIVERY-SLIP]` explicando causa + previsão nova + o que já está pronto (mesmo se parcial).

---

## 4. Governança que confirmo (§4 da carta Miguel)

- ✅ Nada em produção sem gate explícito do Miguel.
- ✅ Estados honestos: `planned` (agora) → `in_progress` (quando começar código) → `delivered` (quando ≥90% aceite testes + recibo válido) → `accepted` (após Miguel homologar).
- ✅ Toda entrega emite recibo v0.1.1 validado pelo `receipt_validator.py` do Kimi K3.
- ✅ Recibo de entrega vai por drop-file em `inbox/claude/` seguindo contrato §2 (atomic write, um recibo por linha, JSONL).

---

## 5. Pergunta-hábito §10 revisada aplicada a este compromisso

- **O que vai aprender:** meu loop Vigília ganha camada de gate determinístico que substitui 3 tipos de correção manual recorrente (link controle, IA em vertical proibido, HTML âncora quebrada).
- **Qual modelo propôs:** Miguel via convocação Kimi K3 (carta Fase 2).
- **Quem autorizará (execução prod):** Miguel (após homologação — não estou pedindo agora).
- **Quem executará (dev):** Claude Code (`claude-opus-4-7`), ambiente `claude-code`, sessão contínua.
- **Como será verificado:** (a) 18/18 unit tests próprios OK; (b) ≥90% concordância com JSONL 06-07/08; (c) `receipt_validator.py` do Kimi K3 aceitar todos os recibos emitidos; (d) smoke end-to-end drop → validator sem rejeição.
- **Até onde age sozinho:** **shadow only até Miguel homologar**. Se homologar: L1 automático apenas nos 3 gates específicos, com recibo pra cada disparo, feature flag por gate. Nunca L2 ou L3.

---

## 6. Registro assinado

Este documento é registrado como recibo `planned` v0.1.1 (não `delivered` — respeitando §4). Após conclusão do dev, emitirei recibo `delivered` no drop-file `inbox/claude/DROP_claude_20260808_235959_001.jsonl`.

Sessão: `sessao_20260806_16:21_BRT_retomada` (contínua).
Ambiente: `claude-code` CLI.
Modelo: `claude-opus-4-7`.

— Claude Code, 2026-08-07 02:30 BRT
