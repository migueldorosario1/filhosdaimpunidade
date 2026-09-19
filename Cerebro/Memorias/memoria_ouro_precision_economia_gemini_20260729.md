# 🧠 MEMÓRIA TÉCNICA — "OURO PRECISION": tombstone + Qwen-first + budget diário + frescor V4 (2026-07-29)

**Sessão:** Kimi K3 Desktop (ZCode), 29/07 02:10→03:50 BRT · **Autorização:** Miguel (chat, decisões citadas no fórum irmão)
**Fórum irmão:** `Cerebro/Foruns/forum_ouro_precision_economia_gemini_20260729.md`
**Relacionada:** `memoria_foto_na_hora_flickr_20260728.md` (§8.11 — incidentes de visão que motivaram esta sprint)

## 1. Diagnóstico (consultas ao banco real, 29/07 ~02:20 BRT)

- `rejeicoes_ouro` 7d: `gemini_vision_erro` **20.248** linhas / **153** URLs únicas (132,3 tentativas/foto); `bytes_baixo` 4.169/21 (198×); `gemini_quarentena_humana` 4.128/125 (33×); `titulo_institucional_generico` 943/6 (157×); `dimensao_baixa:800x431` 302/1 (302×).
- Auditoria dHash (script `/tmp/ouro_dhash_audit_r2.py`, dHash 64-bit PIL puro, Hamming ≤5, 618/618 fotos via `painel_midia_ouro.r2_get_object`): **594 clusters, excedente 24 (4%)**. Clusters: Lula 26/06 (4x+3x), Trump 07/05 (3×2x), Alckmin (3x+2x), Haddad (2×2x), Hugo Motta (2×2x), Flavio (2x), Câmara (2x).
- Acervo: 618 fotos (uso_automatico 137, revisao_humana 410, nao_classificado 46, bloqueada 25). Top: Alckmin 95, Lula 93, Haddad 88. Lacunas: Putin 1, Macron 2, Pichai 1, tech ~0.
- Causa raiz do desperdício: **nenhuma memória de processamento no robô** — dedup por hash acontecia em `processar_candidata` DEPOIS da chamada de visão; coletor (`agente_midia_oficial_externa_v3.py`) não filtra contra o banco.

## 2. Implementação (arquivo: `/root/V3/robo_banco_ouro_midia_v3.py`, Tencent)

Backup: `/root/V3/robo_banco_ouro_midia_v3.py.bak_pre_ouro_precision_20260729` (SHA pré `3275b595…a380`; SHA pós `7d4723aa…c5e8`).

### M1 — Tombstone `ouro_processadas`

- Tabela nova (init_db): `url_origem PK, entidade, motivo, veredito('permanente'|'transitorio'), tentativas, primeira_em, ultima_em, prox_tentativa_em` + índice em `prox_tentativa_em`.
- `registrar_rejeicao` ganhou hook: toda rejeição vira/atualiza tombstone. Permanentes (prefixos: sem_url, sem_titulo_descricao_legenda, entidade_nao_confirmada_no_texto, sem_nome_pessoa_na_legenda_descricao, titulo_institucional_generico, dimensao_baixa, bytes_baixo, gemini_quarentena_humana, gemini_rejeitou, gemini_sem_decisao_aprovadora, contrato_reprovou) → `prox_tentativa_em='9999-12-31'`. Transitórios (gemini_vision_erro, erro:* etc.) → backoff (1h, 6h, 24h, 7d, 30d) por nº de tentativas.
- Trava precoce em `processar_candidata` (antes de baixar bytes e de qualquer visão): `url_ja_no_banco` (url + `variantes_url`) → "duplicada"; `tombstone_bloqueia` → status novo **"tombada"** (contador próprio no resumo do ciclo).
- **Backfill executado 29/07 02:52:** 407 URLs (269 permanentes + 138 transitórias). Transitórias da pane de crédito receberam backoff **zerado** (tentativas=1, prox=agora) — pane de infra não é culpa da foto.

### M2 — Cascata Qwen-first

- Flag `BANCO_OURO_QWEN_FIRST` (default "1"; "0" restaura legado Gemini-first).
- Fluxo novo em `analisar_imagem_gemini_banco_ouro(conn, ...)`: Qwen primeiro; se `status=ok` E `decisao ∈ {APROVAR, QUARENTENA_HUMANA, REJEITAR}` → usa e marca `via=qwen_primario`. Senão (erro/moderação/sem decisão) → Gemini via `_chamar_gemini_com_budget` → marca `via=gemini_fallback_qwen` + `erro_qwen_original`. Falha dupla → `status=erro` (tombstone transitório).
- Resposta vazia/inválida do Qwen (`extrair_json` retorna {}) agora é detectada como falha (`sem_decisao_valida`) e cai pro Gemini — antes virava "gemini_sem_decisao_aprovadora" silenciosamente.
- `_chamar_gemini`: SDK novo (`google.genai`) → legado (`google.generativeai`), levanta exceção; wrapper com budget trata e devolve dict.
- **A/B ao vivo (12 fotos Lula/Haddad, `/tmp/ab_qwen_gemini.py`): 11/12 = 92% paridade.** Única divergência: Qwen QUARENTENA × Gemini APROVAR (conservador = direção segura). Validado.

### M5 — Budget diário Gemini

- Tabela `ouro_visao_diaria(dia PK, qwen, gemini)`; `visao_budget_registrar` conta só chamadas **bem-sucedidas**; `visao_budget_permite_gemini` barra acima de `BANCO_OURO_GEMINI_BUDGET_DIARIO` (default **40**; configurável no `/root/.env.unificado`).
- Budget estourado → `status=erro` → tombstone transitório (retenta após backoff/meia-noite — não vira permanente).
- Log por ciclo: `visao hoje (YYYY-MM-DD): qwen=X gemini=Y budget_diario_gemini=40` + campos `visao_qwen_hoje`/`visao_gemini_hoje` no resumo JSON.
- Qwen fora de cap (custo ~zero no tier DashScope atual).

### V4 — Frescor na seleção (espelho local `v4_labs/codigo/`)

- `media_sources.py::frescor_bonus(data, agora=None)`: ≤7d +30 · ≤14d +20 · ≤30d +10 · ≤60d +5 · mais velha/inválida 0. Parsing ISO e "YYYY-MM-DD HH:MM:SS".
- `collect_ouro_sqlite`: SELECTs ganham `m.data_foto`; ordenação passa a ser `score + frescor_bonus(data_foto)` (antes: score puro). Não altera `candidate.score` (ordem, não qualidade).
- `media_audit.py::V4AuditedMediaStore.search`: sort passa a `-(final_score + frescor_bonus(timestamp)), -visual_confidence` (import de `frescor_bonus` de media_sources).
- Fixture do teste de contrato (`test_contracts.py::_create_ouro_fixture_db`) ganhou coluna `data_foto` (alinhada ao schema real).
- **Suite V4 completa: 566 passed / 0 failed** (75s). Teste direcionado das 8 faixas de frescor: PASS.

## 3. Ciclo supervisionado (29/07 02:56→03:01 BRT, comando do cron manual)

- Candidatas: 154 → **duplicadas 101 · tombadas 52 · rejeitadas 1 · aprovadas 0 · erros 0**.
- Visão no ciclo: **qwen=0, gemini=1** (a 1 processada era foto nova do Xi: Qwen moderou `data_inspection` → Gemini decidiu dentro do budget → rejeitou → tombstonada). Comportamento exatamente como desenhado.
- Ciclo anterior pré-patch (01:52): 154 candidatas, 100 rejeitadas (~100 chamadas). **Corte ~99% por ciclo.** Duração ~5min (antes batia no timeout de 25m).
- Cron permanece intocado (`*/30` via `rodar_banco_ouro_midia_controlado.sh`; flock evita sobreposição).

## 4. Estado dos arquivos

- Servidor Tencent: `robo_banco_ouro_midia_v3.py` (patched, backup carimbado), DB `banco_midia_ouro_v3.db` (+tabelas `ouro_processadas`, `ouro_visao_diaria`).
- Espelho local: `v4_labs/codigo/media_sources.py`, `media_audit.py`, `test_contracts.py` (frescor) — backups: n/a (arquivos versionáveis; hashes registrados no canal).
- Scripts de evidência (locais): `/tmp/ouro_dhash_audit_r2.py` (auditoria near-dup), `/tmp/ab_qwen_gemini.py` (paridade).

## 5. Pendências

1. Deploy NYC dos patches V4 (melhor-esforço §8.11 + frescor) — protocolo ouro (sync + ciclo supervisionado).
2. M3 pHash sombra 48h → calibrar limiar → ativar. M4 quota de cobertura aguarda OK Miguel.
3. Painel Banco Ouro: card "💰 visão hoje" lendo `ouro_visao_diaria`; clusterização de near-dups na fila humana (M6, fase 2 — Lula 26/06: 7 cards → 1 grupo).
4. Monitorar moderação Qwen para outros líderes (Putin/Kim) — fallback Gemini cobre, mas gasta budget.
5. `vision_response_invalid` Qwen em fotos grandes (3/5 no caso Lula) — investigar truncamento/schema; encolhe pool elegível do V4.
