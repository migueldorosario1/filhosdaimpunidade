# Memória — Autolimpeza dos Bancos de Notícias V4 (log técnico completo)

> Tag: `[KIMI-AGENTE-AUTOLIMPEZA-BANCOS-NOTICIAS-V4-REGIONAL]`
> Par (decisões): [forum_autolimpeza_bancos_noticias_v4.md](../Foruns/forum_autolimpeza_bancos_noticias_v4.md)
> Executor: ZCode/Qwen 3.8 · Data: 2026-08-07 · Servidor: NYC (`ssh nyc`, 198.199.121.136)

## 1. Diagnóstico (read-only, 07/08 ~04:00-04:50 BRT)

**Regionais** (5 bancos, `/root/agent_data/v4_verticals/`, criados ~06/08 14:50 UTC):
| banco | candidates | rejections | duplas removíveis | runs | draft_events | tamanho |
|---|---|---|---|---|---|---|
| norte | 287 | 3.136 | 2.529 | 6 | 0 | 13,5MB |
| nordeste | 422 | 3.734 | 2.998 | 6 | 0 | 16,4MB |
| centro_oeste | 185 | 1.672 | 1.285 | 6 | 0 | 7,5MB |
| sudeste | 230 | 1.345 | 1.029 | 6 | 22 | 7,2MB |
| sul | 147 | 1.259 | 987 | 6 | 0 | 5,8MB |

0 candidatos arquiváveis (todos <24h — bancos novos). ~79% das rejections são duplicatas por `(item_key, reason)`; ~92% do motivo é `source_too_old`. `auto_vacuum=0`, modo WAL. Lock compartilhado intake/worker: `/root/agent_data/locks/v4_regional.lock` (cron `/etc/cron.d/v4_regional`: intake :07 horário `flock -n`+timeout 25m; worker 6×/dia `flock -w 900`).

**Temáticos** (mesmo schema, sem coluna `uf`; locks próprios `/tmp/v4_{ciencia,geopolitica,nacional}.lock`, cron a cada 30min):
| banco | candidates | arquiváveis | rejections | removíveis | runs | events | tamanho |
|---|---|---|---|---|---|---|---|
| ciencia_tecnologia_ia | 114 | 20 | 16.669 | 16.167 | 617 | 139 | 96,1MB |
| geopolitica | 1.427 | 880 | 4.923 | 4.812 | 617 | 599 | 43,5MB |
| nacional | 613 | 325 | 2.739 | 2.696 | 596 | 590 | 18,8MB |

Achado: statuses **`editorial_blocked`** (91) e **`discarded`** (1) fora da política → fail-safe preservou (warnings no plano).

**Canônico Cafezinho**: `banco_indice_midia_v3.db` 1,29GB — schema DIFERENTE (`midia_indice` 346.394 linhas + FTS5); fase própria, adapter novo.

**Censo §115 (arquivos sem teto, NYC)**: `log_rotas_llm.jsonl` 167MB; `banco_custos_2026-05/06/07.jsonl` 42/56/34MB; `robo_coleta_*.log` 40-44MB ×4; 797× `briefing_execucao.json.used_*` 8,3MB; `coletor_eleicoes.log` 32MB; `governanca_financeira_api_usage.jsonl` 28MB; etc. Disco 79% (11G livres).

## 2. Implementação
- Artefato: `/root/v4_regional_db_archiver.py` (NYC) — cópia local `ZCodeProject/v4_archiver/`.
- Registro `BANKS`: 5 regionais + 3 temáticos (grupo/lock por banco); `V4_ARCHIVER_ROOT` redireciona a base (testes/sandbox).
- Modos: `--dry-run` (padrão, read-only) · `--stats` · `--verify-archive` · `--restore-test` · `--canary --database X` (execução completa em CÓPIA via `VACUUM INTO`, lock privado) · `--execute --authorization-ref REF` (recusa sem ref).
- Arquivo: `jsonl.zst` (zstd CLI `-10 -T0`) + manifest; diretório `archive/<banco>/AAAA/MM/DD/`; revalidação re-descomprime e confere 2 sha256 + contagem.
- Restauração: `restore_into(src, arquivos, destino)` — recria schema do sqlite_master + `INSERT OR IGNORE` (sem `rid`).
- Transação: `BEGIN IMMEDIATE`; delete de candidatos re-checa frescura DENTRO da transação (`coalesce(last_seen,collected,first_seen) < cutoff`); tombstones `INSERT OR REPLACE`; rejections ganha colunas `first_seen_at/last_seen_at/seen_count` (ALTER) + sobreviventes via tabela temp `_surv`; rollback automático em exceção.
- Recibo v0.1.1 por `--execute`: reason_code `retention_archive_v4_v1`, drop-file `DROP_kimi_*` em `archive/_receipts/` (NYC); dreno ao Tencent inbox/kimi feito por operador.

## 3. Testes offline — 6/6 (local e NYC venv 3.12.3)
Banco sintético de mesmo schema: (1) plano/dry-run read-only + seleções corretas; (2) execute sintético (apaga só o planejado, tombstones, dedup agregado, integrity ok, verify+restore OK, manifest confere, espaço recuperado >0); (3) canário não toca o original; (4) corrupção de arquivo detectada; (5) guardas CLI (`--execute` sem ref, `--canary` sem banco); (6) schema sem coluna `uf` (temáticos).

## 4. Dry-run real (07/08 ~04:52 BRT)
Regionais: 0 candidatos arquiváveis; 8.828 linhas de rejections removíveis (11.146 → 2.318 sobreviventes). Temáticos: 1.225 candidatos arquiváveis (929 preservados + 92 fail-safe), 23.675 linhas de rejections removíveis (97,3%), 826 runs e 76 events fora da janela.

## 5. Canários (cópias, fora de produção)
- `regional_sul`: 5,83MB → 2,05MB (−65%); rejections 1.259→272; integrity ok.
- `geopolitica`: 43,42MB → 5,71MB (−87%); candidates 1.427→547 (880 arquivados c/ tombstones); rejections 4.923→111; runs 617→335; events 599→569; integrity ok.
- Verificação independente pós-canário: originais intactos (contagens batem, sem tabela de tombstones); arquivos revalidados; restore-test re-executado com sucesso a partir dos manifests.

## 6. Bug encontrado e corrigido (prova do valor do canário)
1º canário de geopolitica abortou com rollback: código assumia coluna `uf` em candidates (só existe nos regionais). Corrigido (`uf` opcional no tombstone) + teste de regressão nº 6. Nada foi apagado; original intacto.

## 7. Comandos
```bash
# dry-run (padrão) / censo
/root/venv/bin/python3 /root/v4_regional_db_archiver.py --dry-run --grupo regional
# canário (cópia)
/root/venv/bin/python3 /root/v4_regional_db_archiver.py --canary --database geopolitica
# execução real (SÓ com autorização explícita do Miguel)
/root/venv/bin/python3 /root/v4_regional_db_archiver.py --execute --grupo regional --authorization-ref "MIGUEL-2026xxxx-pode-aplicar-regionais"
# rollback (restaura linhas do manifest no banco; tombstones permanecem p/ auditoria)
/root/venv/bin/python3 -c "import sys,json;sys.path.insert(0,'/root');import v4_regional_db_archiver as A;from pathlib import Path;m=json.loads(Path('<manifest>').read_text());A.restore_into(A.BANKS['<banco>']['db'],m['arquivos'],A.BANKS['<banco>']['db'])"
```

## 8. Autorização (carta §12, respeitada integralmente)
Autorizado e feito: diagnóstico, desenho, implementação, testes offline, dry-run real, canários. Proposta de 1º lote: 5 regionais (risco mínimo — só dedup de rejections). **~10:07 BRT: Miguel autorizou ("sim, pode fazer") + ordenou agente diário por voz e reafirmou "não jogar nada fora".**

## 9. 1º lote REAL executado (07/08 13:38 UTC / 10:38 BRT)
Autorização: `MIGUEL-20260807-PODE-APLICAR-REGIONAIS`. Comando: `--execute --grupo regional`.
- Espera de lock: intake regional estava rodando (13:07 UTC); **lição**: poll via `pgrep -f v4_regional_intake` casa com o próprio shell — usar `fuser`/`flock` para checar lock, não pgrep com o nome na própria cmdline.
- Resultados (5 bancos, rc=0, erros={}):

| banco | rejections antes→depois | linhas arquivadas | tamanho antes→depois |
|---|---|---|---|
| centro_oeste | 3.034→464 | 2.570 | 12,7→3,1MB |
| nordeste | 6.867→791 | 6.076 | 28,1→6,0MB |
| norte | 5.752→643 | 5.109 | 23,3→4,5MB |
| sudeste | 2.433→341 | 2.092 | 11,6→3,5MB |
| sul | 2.314→323 | 1.991 | 9,9→2,3MB |
| **TOTAL** | **20.400→2.562** | **17.838** | **85,6→19,4MB (−66,2MB)** |

- 0 candidatas arquivadas (todas <24h) → tombstones=0 nos 5. integrity_check ok nos 5; verify-archive 5/5 OK; restore-test REAL (regional_sul): 2.314/2.314 linhas restauradas OK.
- Execução interrompida antes (~10:10) pela chegada da mensagem de voz do Miguel: verificado pós — transações atômicas, NADA apagado pela corrida abortada (só arquivo órfão de archive do centro_oeste, preservado).
- Robustez para o modo diário (aplicada antes do lote): lock wait 180s→900s (igual ao worker); `--execute` tolera falha por banco (erros isolados, exit 1, demais bancos seguem).

## 10. Agente diário (cron) — ordem do Miguel
Arquivo NYC `/etc/cron.d/v4_autolimpeza` (644 root:root): diário **07:35 UTC (04:35 BRT)**, `flock -n /root/agent_data/locks/v4_autolimpeza.lock`, `timeout 40m`, `--all --execute --authorization-ref MIGUEL-20260807-CRON-DIARIO`, log `archive/autolimpeza_cron.log` SOBRESCRITO (§115). Janela: após intake (:07, máx 25min) e antes do worker (10:00 UTC). Linha exata testada em dry-run antes de armar: rc=0, plano dos 8 bancos no log. Cópia local: `ZCodeProject/v4_archiver/v4_autolimpeza.cron`.
- 1ª corrida 08/08 04:35 BRT limpará os temáticos pela 1ª vez (dry-run atual: ciencia 16.520 + geopolitica 4.888 + nacional ~1k linhas duplicadas; ~1.100 candidatos terminais >24h). **Monitorar.**

## 11. Recibo no ledger + aprendizado de taxonomia
- Recibo emitido pelo agente usou reason_code inventado (`retention_archive_v4_v1`) → validator recusou (fora da taxonomia v0.1.1). **Correção**: `reason_code: null` explícito (schema permite) + **PROPOSTA** registrada de código `RETENTION_ARCHIVE_EXECUTED` para v0.1.2. DROP inválido preservado em NYC com sufixo `.invalido_reason_code_fora_taxonomia`.
- Recibo reemitido (mesmo gerador, mesmos dados): `rcpt_20260807_134505_kimi_autolimpeza_v4` → drenado inbox/kimi → writer --once → **ledger 17 recibos, 17/17 válidos**; espelho local `ZCodeProject/media_ledger/ledger/` sincronizado.

## 12. Resposta "é pesado guardar tudo?" (medido, não estimado)
Canário geopolitica: arquivo total 1,2MB zstd (880 cand + 4.923 rej + 282 runs + 30 events). Arquivo inteiro pós-lote 1: **12MB** (inclui 2 canários + órfão). Projeção ~1–3MB/dia ≈ ~50MB/mês; disco NYC com 11G livres. **Não é pesado.**
