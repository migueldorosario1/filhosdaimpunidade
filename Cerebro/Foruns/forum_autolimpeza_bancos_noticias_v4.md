# Fórum — Autolimpeza e Arquivamento dos Bancos de Notícias V4 (retenção universal §115)

> Tag: `[KIMI-AGENTE-AUTOLIMPEZA-BANCOS-NOTICIAS-V4-REGIONAL]`
> Par técnico (log completo): [memorias_autolimpeza_bancos_noticias_v4_20260807.md](../Memorias/memorias_autolimpeza_bancos_noticias_v4_20260807.md)
> Regra mãe: §115 RETENÇÃO UNIVERSAL (nodo de governança)

## Origem
Carta do Miguel (07/08) pedindo agente de arquivamento/autolimpeza para os 5 bancos regionais do V4 (NYC), + ordem do mesmo dia: **"essa regra vale para todos os bancos (regionais, temáticos, canônico Cafezinho) e nenhum arquivo pode crescer indefinidamente"** → registrada como regra viva §115.

## Decisões
1. **Política `retencao-v4-v1`** (versionada; mudar retenção = nova versão + autorização):
   - candidatos: preserva `new/processing/drafted/image_pending` (pautas ativas, WP não confirmado) e qualquer linha vista há <24h; arquiva terminais (`stale_expired`, `duplicate`, `duplicate_blocked`, `rejected_editorial`) com >24h; **status desconhecido = fail-safe preserva + alerta**.
   - rejections: dedup por `(item_key, reason)` — sobrevive a 1ª ocorrência com `first_seen_at/last_seen_at/seen_count`; arquivo guarda TODAS as linhas (fidelidade).
   - runs e draft_events: janela 7 dias; eventos `repair*` e `image_pending` preservados sempre.
   - Apagou candidato terminal → grava **tombstone** (`candidate_tombstones`) para auditoria/dedup futura.
2. **Nada some**: tudo vai para `jsonl.zst` + manifest (sha256, contagens, cutoffs, procedimento de restauração) em `archive/<banco>/AAAA/MM/DD/`.
3. **Ordem obrigatória**: medir → selecionar → arquivar → validar → testar restauração → lock (mesmo flock do intake/worker, nunca force-kill) → transação → commit → integrity_check → WAL checkpoint → VACUUM → medir → recibo.
4. **Execução escalonada**: dry-run → canário (cópia) → 1º lote real → demais lotes; cada lote exige "pode aplicar" explícito do Miguel. Sem cron nesta fase.

## Estado (07/08 ~10:50 BRT, ZCode/Qwen 3.8)
- ✅ Diagnóstico completo (8 bancos + censo de arquivos sem teto na NYC).
- ✅ Agente implementado: NYC `/root/v4_regional_db_archiver.py` (read-only por padrão; mutação exige `--execute --authorization-ref`).
- ✅ 6/6 testes offline (banco sintético) — local e no venv de produção NYC.
- ✅ Dry-run nos 8 bancos reais; 2 canários completos: `regional_sul` (−65%) e `geopolitica` (−87%), originais intactos, restauração re-testada com sucesso.
- ✅ **1º LOTE REAL EXECUTADO (10:38 BRT)** — autorização `MIGUEL-20260807-PODE-APLICAR-REGIONAIS`: 5 regionais limpos, **85,6MB → 19,4MB** (−66,2MB), 17.838 linhas de rejeições duplicadas arquivadas, 0 candidatas tocadas (todas <24h), integridade ok nos 5, verify-archive 5/5 OK, restore-test real OK (regional_sul 2.314 linhas 100% restauráveis), tombstones=0.
- ✅ **AGENTE DIÁRIO INSTALADO** (ordem do Miguel por voz, 07/08 ~10:05): cron NYC `/etc/cron.d/v4_autolimpeza`, diário 07:35 UTC (04:35 BRT), `--all` (8 bancos), lock próprio `flock -n`, timeout 40m, log sobrescrito (§115). Linha exata testada em modo leitura antes de armar (rc=0). Ref autorização: `MIGUEL-20260807-CRON-DIARIO`. 1ª corrida: 08/08 04:35 BRT.
- ✅ Recibo da execução drenado no media_ledger (recibo nº 17, 17/17 válidos) — Tencent + espelho local.
- 🔒 **Política "não jogar nada fora" SEGURA** (Miguel): tudo arquivado antes de qualquer remoção; restauração provada; arquivo inteiro ≈ 12MB (inclui canários) — guardar é barato (~1–3MB/dia).

## Pendências / decisões futuras
- **`editorial_blocked` (91+) e `discarded`** nos temáticos: statuses fora da política; fail-safe preservou todos. Decidir se são terminais (política v1.1) — sem pressa, nada se perde.
- **Temáticos serão limpos pela 1ª corrida do cron** (08/08 04:35 BRT): ~22 mil linhas duplicadas + candidatos terminais >24h prontos no dry-run. Monitorar essa 1ª corrida.
- Banco canônico Cafezinho (schema diferente — adapter novo), arquivos soltos sem teto (logs/JSONL ~700MB).
- **Proposta taxonomia v0.1.2**: reason_code `RETENTION_ARCHIVE_EXECUTED` (hoje o recibo usa `null` explícito, conforme schema permite; códigos novos só entram por proposta versionada).
- Recibo v0.1.1 é emitido automaticamente a cada `--execute` (staging NYC → inbox/kimi do media_ledger, dreno manual).
