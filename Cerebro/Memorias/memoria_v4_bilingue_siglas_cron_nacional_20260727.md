# Memória técnica — V4: filtro ciência bilíngue + siglas BR + cron nacional 30min (2026-07-27)

**Agente:** Kimi K3 (ZCode) · **Autorização:** Miguel, 2026-07-27 ~13:20 BRT (chat ZCode: "sim, autorizo, desde que siga protocolos de segurança, backup, rollback, manifesto, indexação no cérebro e fórum")
**Fórum canônico (decisões):** `Cerebro/Foruns/forum_kimi_travas_v4_nacional_e_ciencia_20260727.md` §12–§14
**Servidor:** NYC `198.199.121.136` (Cafezinho-failover-vigia)

---

## 1. Contexto

Travas de volume editorial V4 em 27/07: Ciência/Tec 0 posts/dia e Nacional 1 publicado/dia. Diagnóstico (fórum §12): filtro tec×geo PT-only contra fontes EN matando 100% das pautas ciência (166 únicas/6d); nacional com cron legado 2h + burn por guarda de siglas BR.

## 2. Patches (tags de auditoria no código)

| Tag | Arquivo | Mudança |
|---|---|---|
| `V4_PATCH_BILINGUE_20260727` | `/root/v4_vertical_intake.py` e `/root/v4_vertical_draft_worker.py` | Tuplas de termos estendidas com equivalentes EN (bloco aditivo; nada removido). Gate de nexus e threshold ≥4 intactos (Opção A). |
| `V4_PATCH_SIGLAS_BR_20260727` | `/root/v4_vertical_draft_worker.py` `validate_title_clarity` | `common` += PL, PT, PF, PGR, MDB, PSDB, PSB, PSL, PP, PSD, INSS, STJ, TSE, MPF, TCU, CPI, PEC, IBGE, FGV; `opaque_defined` passa a respeitar a allowlist. |
| `V4_NACIONAL_30MIN_20260727` | crontab NYC | Legado `59 */2` + `19 1-23/2` comentados (`# SUBSTITUIDO_KIMI_20260727_30MIN`); nova linha `20,50 * * * *` flock `/tmp/v4_nacional.lock` cadeia coletor→intake→worker. |

**Decisões de desenho relevantes:**
- Matching é por **substring** — termos EN ambíguos foram excluídos deliberadamente: "ai" (casa em "said"), "model", "curbs", "restrictions". Listas finais no fórum §14.2.
- Reprocessamento do backlog **replicou a lógica do intake** (mesmas checagens fail-closed, POLICY tecnologia=168h, mesmo SQL) em vez de UPDATE direto: 166→17 aptas→7 inseridas (10 já existiam, 13 velhas). Estoque ciência 0→7 `new`.
- Borderline conhecido: "Taylor Farms diarrhea outbreak" (s6) passou (precisão 16/17) — sinalizado pra revisão editorial.

## 3. AUTOCURA

- **Backup:** `/root/agent_data/backups/pre_kimi_bilingue_siglas_cron_20260727_154731/` (+`SHA256SUMS.txt`) — worker, intake, coletor, crontab, 2 sqlite.
- **Smoke unitário:** 10/10 PASS (`/tmp/kimi_smoke_unit.py` no NYC): EN nexus≥4, ciência pura=0, PT regressão OK, siglas BR passam, sigla opaca (ABCDF) segue barrada.
- **Smoke live:** intake tecnologia accepted 2/33 (era 1/33); crontab verificado pós-install.
- **Hashes pós:** worker sha256 `a24e6c14…`/md5 `734f9c9e…`; intake sha256 `53915c8e…`/md5 `7cb43649…`. Espelho local `Projeto Cafezinho Agentes/root/` sincronizado.
- **Rollback:** fórum §14.8 (cp dos .bak; `crontab crontab.bak`; UPDATE das 7 rows).

## 4. Incidente operacional (resolvido, lição registrada)

Run manual do worker nacional morta pelo **timeout 240s do operador** com redator em voo → candidato travado `processing`. Verificado via WP API: **sem órfão** (morto antes de criar post). Limpeza: candidato→`new`, evento→`failed` documentado. **Lição:** smoke manual de worker com `timeout ≥ 900s` ou sem timeout; pipeline **não tem** reset de `processing` no startup (gap conhecido).

## 5. Bugs registrados

- ✅ `BUG-20260727-V4-CIENCIA-CEGUEIRA-IDIOMA` (RESOLVIDO) — listas PT-only vs fontes EN; 0% aprovação em 166 pautas/6d.
- ✅ `BUG-20260727-V4-NACIONAL-SIGLAS-BR` (RESOLVIDO) — guarda de siglas sem allowlist BR; 13 burns na janela; `opaque_defined` ignorava allowlist.
- 🔴 `BUG-20260727-V4-GUARDA-TITULO-POS-CRIACAO` (ATIVO, baixa) — `validate_title_clarity` roda pós-criação; `editorial_blocked` deixa draft WP vivo (ex: 263074).

## 6. Monitoramento

Ciência `:10/:40` deve produzir o 1º draft do dia (7 em `new`, scores 6–10). Nacional `:20/:50` com burn de siglas ~0. Meta: ciência sair do zero; nacional >3 drafts/dia.
