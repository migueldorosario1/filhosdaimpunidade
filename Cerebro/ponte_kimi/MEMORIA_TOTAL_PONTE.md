# 🧠 MEMÓRIA TOTAL PONTE — payload autocontido Claude ↔ Kimi K3

**Versão:** v1 · **Última atualização:** 2026-07-28 17:22 BRT (Claude)
**Próximo refresh trimestral:** 2026-10-28 (revisão profunda + homologação Miguel)
**Refresh diário automático:** meu último ciclo vigília do dia (22h BRT)
**Ponte assinada:** `Cerebro/ponte_kimi/CONTRATO_PONTE_CLAUDE_KIMI.md` §4 (aceite bilateral 27/07)
**Duplo propósito:** (a) Kimi K3 Desktop abre 1× por sessão pra reancorar contexto; (b) Claude injeta este arquivo como `system` message quando chama Kimi K3 via API.

---

## §1 — Contexto ecossistema (5 linhas)

Cafezinho é site editorial brasileiro (`ocafezinho.com`) com **8 sites satélites temáticos** (Rio Carta, Mapa Rio, Global South News, Discover Brazil, Aiatolah, Ceará Digital, Mundo Trilhos, Rail Post). Pipeline principal V4 gera drafts em 3 verticais: **Geopolítica** (worker `v4d_geopolitica_*`), **Nacional** (`v4d_nacional_*`), **Ciência/Tec** (`v4d_ciencia_*`). Drafts saem sempre autor **5786 (`redacao-nova`)** exclusivo V4 desde 27/07/2026 19:58 BRT; Miguel manual usa autor **2018 (`james2017`)** via Antigravity Desktop. Único loop de checagem dupla editorial é meu (Claude Opus 4.7, cron `17,47` das 07-22h + `17` 23-06h). Sentinela DeepSeek publish DESATIVADO desde 27/07 17:15 BRT.

## §2 — Credenciais simbólicas (SEM valor literal — regra `feedback_nunca_chave_literal_em_forum`)

| Variável | Arquivo | Uso |
|---|---|---|
| `WP_APP_PASSWORD_5786` | `~/ferramentas/sentinela/.env` | publicação WP autor 5786 (checagem dupla V4) |
| `WP_SITE` | idem | `https://www.ocafezinho.com` |
| `KIMI_CODE_API_KEY` | `Projeto Cafezinho Agentes/Outros/chaves/kimi_code.env` | **Kimi assinatura Coding** (`api.kimi.com/coding/v1`) — R$ 0, quota Kimi Desktop. Modelo: `k3` |
| `KIMI_PAYGO_API_KEY` | `Projeto Cafezinho Agentes/Outros/chaves/kimi_paygo.env` | **Kimi paygo** (`api.moonshot.ai/v1`) — **PRIMÁRIO** desde 28/07 17:40 BRT (custo real medido R$ 0,02/consulta, ~R$ 12/mês no cap 20/dia). Modelo: `kimi-k3` |

**⚠️ Nomes de modelo diferem por endpoint** (casca de banana verificada 28/07): paygo usa `kimi-k3`; assinatura Coding usa `k3` (ou `k3-256k`, `kimi-for-coding`, `kimi-for-coding-highspeed`). `kimi-k2-turbo-preview` NÃO EXISTE em nenhum canal. Sempre verificar via `GET /models` antes de assumir nomenclatura entre APIs.
| `BRAVE_API_KEY` | `root/.env.unificado` (NYC) | busca temáticos |
| `GEMINI_API_KEY` | idem | Tribunal Visual (fallback Qwen VL desde 28/07) |
| `QWEN_API_KEY` | idem | Cadeia visão V4 + fallback Gemini |

Regra vigilante: **nunca colar valor literal** em fórum/canal/inbox/memória — máscara 4 últimos `KIMI***abc` ou SHA-256 primeiros 8. Debug com `env | grep KEY | wc -l` (só conta).

## §3 — Endereços canônicos (mapa completo)

**Ecosistema (código):**
- Sentinela: `~/ferramentas/sentinela/` (script principal `sentinela_ciclo.py`)
- V4 workers (NYC 198.199.121.136): `Projeto Cafezinho Agentes/root/v4_labs/codigo/v4_vertical_draft_worker.py`
- V4 publicador: `v4_labs/codigo/wordpress_publicador.py` + `flickr_media.py`
- V4 config Flickr: `v4_labs/config/v4_flickr_official_accounts.json` (40+ contas)
- Banco Ouro Mídia (Tencent 43.156.151.165): `/root/V3/robo_banco_ouro_midia_v3.py` + `painel_midia_ouro.py`

**Logs / diários / rastros:**
- Log máquina ciclos Sentinela: `~/ferramentas/sentinela/logs/ciclos.jsonl`
- Log humano cron: `~/ferramentas/sentinela/logs/cron.log`
- Relatório por ciclo: `Cerebro/Foruns/sentinela/YYYY-MM/ciclo_YYYYMMDD_HHMM.md`
- Bugs diários: `Cerebro/monitoramento_horario/bugs_encontrados/bugs_YYYY-MM-DD.jsonl`
- Propostas correção: `Cerebro/monitoramento_horario/propostas_correcao/`
- Backups pré-edit: `Cerebro/monitoramento_horario/backups_edicao/backup_pre_publish_ciclo_HHMM_YYYYMMDD_HHMMSS/`

**Comunicação Trindade:**
- Canal: `Cerebro/Foruns/canal_trindade.md` (ponteiros curtos com tag `[TAG]`)
- Inbox Kimi: `Cerebro/Foruns/inbox_trindade/kimi.md` (ponteiro apontando pra fórum)
- Cartinhas materializadas: `Cerebro/Foruns/cartinhas/cartinha_<destinatario>_<slug>_YYYYMMDD_HHMM.md`
- Fóruns temáticos: `Cerebro/Foruns/forum_<tema>_YYYYMMDD.md`
- Consultas Kimi API (histórico): `Cerebro/Foruns/consultas_kimi_k3_api/consulta_YYYYMMDD_HHMMSS.md`

**Ponte especifica:**
- Contrato: `Cerebro/ponte_kimi/CONTRATO_PONTE_CLAUDE_KIMI.md`
- Estado atual: `Cerebro/ponte_kimi/ESTADO_ATUAL.md`
- Histórico: `Cerebro/ponte_kimi/HISTORICO.md`
- Memória Total (este arquivo): `Cerebro/ponte_kimi/MEMORIA_TOTAL_PONTE.md`

## §4 — Bug atlas — patterns recorrentes (curado, não bruto)

Bugs identificados na produção V4 nas últimas 2 semanas, agrupados por categoria. **Meta:** cada padrão tem sintoma, causa provável, fix cirúrgico meu (Claude), sugestão upstream (Kimi), instâncias últimos 30d.

### 4.1 `CUTOFF_LLM_AUTORIDADE_DESATUALIZADA` (crítico, 7+ instâncias)
- **Sintoma:** worker cita autoridade que já mudou de cargo/morreu (Fachin STF, Bessent Tesouro EUA, Lee Jae-myung Coreia, Mojtaba Khamenei Irã, Keiko Fujimori Peru, Ciro Gomes PSDB) usando nome antigo (Barroso, Yellen, Yoon Suk-yeol, Ali Khamenei, Dina Boluarte, Ciro PDT).
- **Causa:** knowledge cutoff do modelo worker Kimi (data indeterminada mas ≥ 6 meses atrás)
- **Fix meu:** WebSearch obrigatório + replace do nome antigo pelo atual + registro JSONL
- **Sugestão upstream:** gate `WebSearch("<autoridade> <cargo> 2026")` antes de publicar draft com nome de figura pública + verbo de posse/cargo. Lista curta de figuras públicas + cargo atual (BR + mundo) — atualizada trimestralmente
- **Instâncias 30d:** ≥7 (263017 Fachin, 263275 datas Haiti, 263283 Ciro-PSDB, 263299 Lee+Keiko dobrado, 263301 Netanyahu OK etc)

### 4.2 `SIGLA_MINUSCULA_TITULO` (frequência alta, ~10 instâncias)
- **Sintoma:** título gerado com sigla em caixa mista tipo `Sp`, `Pgr`, `Fda`, `Ibm`, `Openai`, `Mpf`, `Unrwa`, `Tv`, `Eua-irã`
- **Causa:** título gerado por LLM com regra de capitalização tipo AP style (primeira letra) sem allowlist de siglas conhecidas
- **Fix meu:** replace pontual (`Tv → TV`, `Openai → OpenAI` etc)
- **Sugestão upstream:** allowlist compartilhada de siglas (BR: PT, PL, MDB, PSDB, PDT, STF, PGR, MPF, UNRWA, TV, EUA, ONU, PIB, CPI, PEC + Mundo: OpenAI, IBM, FDA, NASA, ESA, WHO, IMF, ECB, EU, NATO, BRICS) — regex de post-processing título
- **Instâncias 30d:** ~10

### 4.3 `MINUSCULA_POS_VIRGULA` em nome próprio (~5 instâncias)
- **Sintoma:** vírgula seguida de nome próprio em minúscula: `, donald Trump`, `, israel aprovou`, `, nvidia, Meta`
- **Causa:** LLM tratou vírgula como separador que reinicia sentença; nome caiu minúsculo
- **Fix meu:** regex `,\s+([a-z][a-zà-ú]+)\s+([A-Z])` + capitalize
- **Sugestão upstream:** post-processing regex no corpo antes de salvar draft
- **Instâncias 30d:** ~5

### 4.4 `FONTE_EM_GRITO` (~8 instâncias)
- **Sintoma:** anchor text da fonte em CAIXA ALTA (`>REVISTAFORUM</a>`, `>TECNOBLOG</a>`, `>ACTUALIDAD</a>`, `>ARSTECHNICA</a>`, `>CANALTECH</a>`)
- **Causa:** LLM copiou nome do domínio literal (`revistaforum.com.br → REVISTAFORUM`)
- **Fix meu:** replace nome-humanizado (`REVISTAFORUM → Revista Fórum`)
- **Sugestão upstream:** mapa domínio→nome humanizado no `util_fonte.py` (já parcialmente feito 26/07 pra The Hindu etc)
- **Instâncias 30d:** ~8

### 4.5 `DATA_ESPECIFICA_TROCADA_NO_TEXTO` (2 instâncias, novo pattern)
- **Sintoma:** LLM inventa dia do mês próximo ao correto (`12 de março` vs `7 de março`; `5 de agosto` vs `15 de agosto`)
- **Causa:** alucinação de número dentro de contexto factual real (não é cutoff — é geração aleatória)
- **Fix meu:** WebSearch pra bater data real + replace
- **Sugestão upstream:** gate `WebSearch` obrigatório em drafts com padrão "dia + preposição + mês" que envolvam evento factual (posse, publicação, prazo eleitoral)
- **Instâncias 30d:** 2 (263275, 263283)

### 4.6 `AGENTE_V4_NAO_POPULA_META_ZIZI` (1 instância, novo)
- **Sintoma:** draft autor 5786 sem `zizi_job_id`, sem `_agente_origem` (cat 2403 "Redação", vídeo TV Fórum transcrito)
- **Causa:** pipeline não-V4 (redação/vídeo?) usando mesmo autor 5786 sem popular meta
- **Fix meu:** publicar + escalar Kimi via fórum
- **Sugestão upstream:** produtor V4 (todos verticais) DEVE popular `_agente_origem=worker_v4_<vertical>` + `zizi_job_id=v4d_<vertical>_<hash>` sempre. Se pipeline vídeo/redação existe fora do V4, popular meta próprio (`_agente_origem=videocaster_v1`)
- **Instâncias 30d:** 1 (263288, primeiro caso pós-migração 5786-exclusivo)

### 4.7 `V4_PRODUTOR_GEROU_2_DRAFTS_MESMO_JOB_ID` (1 instância, novo)
- **Sintoma:** 2 drafts com mesmo `meta.zizi_job_id` (`v4d_ciencia_8e6c3e8b18dd4cf7`) — 1 completo + 1 defeituoso
- **Causa suspeita:** race condition no worker (retry sem idempotência? 2 processos concorrentes?)
- **Fix meu:** publicar o completo + WP DELETE do defeituoso
- **Sugestão upstream:** worker deve verificar existência de draft com mesmo `zizi_job_id` antes de criar novo (dedup por meta)
- **Instâncias 30d:** 1 (263303 defeituoso vs 263304 completo)

## §5 — Últimos 12 incidentes brutos (tail JSONL agregado)

Formato: `ts | post_id | vertical | tipo | fix`

```
2026-07-27T23:28 | 263181 | ?          | sigla_hifen_minuscula_titulo         | 'Eua-irã' → 'EUA-Irã'
2026-07-27T23:28 | 263186 | ?          | grito_fonte_arstechnica              | '>ARSTECHNICA</a>' → '>Ars Technica</a>'
2026-07-28T13:19 | 263275 | ?          | data_errada_texto                    | '12 de março' → '7 de março'
2026-07-28T14:22 | 263285 | geopolitica| SEM_BUG_FACTUAL                      | publish direto
2026-07-28T14:22 | 263283 | nacional   | MULTIPLO_DATA_PARTIDO_TITULO         | Tv→TV, 5ago→15ago, Ciro PDT→PSDB
2026-07-28T14:22 | 263288 | ?cat2403   | AGENTE_V4_SEM_META + Transcriptor    | Millet→Milei
2026-07-28T15:20 | 263297 | geopolitica| SEM_BUG_FACTUAL                      | publish direto
2026-07-28T15:20 | 263291 | nacional   | FONTE_EM_GRITO                       | REVISTAFORUM→Revista Fórum
2026-07-28T16:21 | 263299 | nacional   | CUTOFF_LLM_AUTORIDADE_DUPLA          | Yoon→Lee Jae-myung + Boluarte→Keiko Fujimori
2026-07-28T16:51 | 263304 | ciencia    | FONTE_EM_GRITO                       | CANALTECH→Canaltech
2026-07-28T16:51 | 263303 | ciencia    | DRAFT_DUPLICADO_DEFEITUOSO           | WP DELETE trash
2026-07-28T16:51 | 263301 | geopolitica| MINUSCULA_POS_VIRGULA                | donald Trump→Donald Trump
```

## §6 — Fila aberta pra ti decidir

1. **Perguntas cartinha 27/07 16:55** (5 pontos ainda em aberto — só #1 tem ganho imediato):
   - #1 patch upstream `MINUSCULA_POS_VIRGULA` + `FONTE_EM_GRITO`
   - #2 estoque Ciência pós-fix bilíngue saudável?
   - #3 `sentinela_tematicos_cron.sh` deploy complementar Haiku?
   - #4 `agente_roteador_llm.py` vivo ou legado?
   - #5 heads-up Antigravity conta WP dedicada (RESOLVIDO 27/07 19:58)

2. **Bugs cartinha 28/07 14:35** (2 pontos):
   - A. Nacional Zema — cutoff filiação partidária (Ciro PDT→PSDB) + data inventada (5→15 agosto)
   - B. Redação/vídeo — primeiro draft autor 5786 sem meta V4

3. **Diagnóstico infra grande** (cartinha 27/07 16:15) — 10 seções, prio real do teu tempo

4. ~~**Painel Banco Ouro** (deployado 28/07 15:02 Tencent) — auditoria diff opcional~~ ✅ Kimi executou auditoria 28/07 16:50 BRT (`[KIMI-AUDITORIA-PAINEL-FOTO-NA-HORA]`)

## §7 — Padrões operacionais vigentes (regras curtas)

- **Autor 5786 = SEMPRE agente V4** (nunca humano). Sem `zizi_job_id` = bug estrutural, reportar Kimi.
- **Duplicata em publicado** → status=`pending` (não draft, não trash). Regra `feedback_duplicata_pos_publish_vira_pending`.
- **Nacional com cat 20699** = no-home NORMAL (score policy, não bug).
- **WebSearch obrigatório** antes de afirmar fato do mundo real (regra `feedback_sempre_pesquisar_web_em_duvida`).
- **Backup SHA-256 + rollback trivial** em toda edição (regra AUTOCURA contrato §2/§3).
- **Não retroativar** — nunca mexer em posts já publicados nem drafts antigos autor 5470 (regra `feedback_kimi_stop_retroativo`).
- **Chaves nunca literais** em fórum/canal/inbox/memória (regra `feedback_nunca_chave_literal_em_forum`).

---

**Refresh log:**
- v1 · 2026-07-28 17:22 BRT — Claude, versão inicial pós-decisão Miguel (Opção A assinatura Coding primária + paygo fallback).
- v1.1 · 2026-07-28 17:55 BRT — Claude, aplicando 3 correções apontadas por Kimi K3 Desktop na cartinha `cartinha_claude_modo_b_operante_fix_paygo_k3_20260728_1750.md` §7: (1) "7 satélites" → "8 satélites" (lista tinha 8 nomes); (2) auditoria diff painel marcada done (Kimi executou 16:50 BRT); (3) §2 credenciais ganha nota sobre nomes de modelo diferirem por endpoint. **Reversão diretriz Miguel 17:40 BRT:** paygo primário (custo real R$ 0,02/consulta), assinatura Coding blindada como fallback emergência.

**Notas pra Kimi K3 API (quando este arquivo for injetado como `system`):**
- Omitir `temperature` no request (k3 trava em 1, API rejeita outro valor).
- Prefira responder no formato estruturado esperado (Markdown com headers §, listas, tabelas).
- Se algo aqui parecer defasado, sinalizar no início da resposta com `⚠️ MEMORIA_TOTAL_PONTE potencialmente defasada em: <ponto>`.
