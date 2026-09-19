# Memória técnica — Organização do Cérebro + Manutenção Regular (14/08/2026)

**Sessão:** ZCode GLM-5.2 · **Ordem:** Miguel — plano de organização do Cérebro, para virar manutenção regular.
**Estado:** ✅ Fases 0–2 concluídas + manutenção quinzenal no ar · **Fórum irmão:** `Foruns/forum_organizacao_cerebro_manutencao_regular_20260814.md`

## Contexto e método

Investigação do Cérebro canônico (`Downloads/Antigravity Google/Cerebro/`) com 4 subagentes varrendo: pastas de memória, fragmentação de bugs/INDEXes, redundância de backups, organização de `Foruns/`. Diagnóstico completo no fórum irmão. Plano aprovado pelo Miguel: **Fases 0–2 agora + manutenção quinzenal automatizada + Fases 3–4 como follow-up**.

## Mecânica do sync (essencial para qualquer sessão que organize o Cérebro)

```
*/30  sync_cerebro_to_github.py  Cérebro → ~/cerebro-miguel/cerebro/ (SÓ ADICIONA) → git push
*/15  rsync -a (sem --delete)    ~/cerebro-miguel/cerebro/ → Cérebro (RE-CRIA o que faltar)
7,37  rsync -a --delete          Cerebro/Foruns/ → tencent (painel V6 — tirou do Foruns/, sumiu do painel)
```

**Protocolo de retirada (dupla):** (1) `mv` no Cérebro → quarentena com manifesto+SHA; (2) remover do repo `cerebro-miguel/cerebro/` + commit + push — no mesmo bloco rápido. Validado: nada voltou.

**⚠️ Protocolo de EDIÇÃO (novo, descoberto nesta sessão):** o rsync `*/15` copia repo→Cérebro sempre que o arquivo difere por mtime/size — **regredi edições mais novas do vivo** (janela ≤15min até o `*/30` atualizar o repo). Vítimas: linha do monitor às 08:00 e adendos deste Tema Duplo às 08:30/08:45 (recuperados por reescrita + sync forçado). **Depois de editar qualquer arquivo do Cérebro: rodar `cd ~/cerebro-miguel && CEREBRO_DRY_RUN=0 python3 scripts/sync_cerebro_to_github.py`.**

**Checkpoint de restauração desta sessão:** commit `ba974109` (2026-08-14 07:57).

## Execução

### Fase 0 — Fundação (07:55-07:58) ✅
Quarentena `Cerebro/_organizacao_cerebro_20260814_0755/`; checkpoint git forçado (`ba974109`) + push; linha no monitor; Tema Duplo criado.

### Fase 1 — Consolidações seguras (~08:02) ✅
- `MEMORIA/`→`Memorias/`: 29 `.md` (121→150), zero colisão (comm no `comm`), `relatorios/`→`Memorias/memoria_legada_relatorios/`; `.log/.json`→quarentena; redirecionador `_MOVIDO_PARA_Memorias.md` por 1 ciclo; sed `MEMORIA/`→`Memorias/` nos .md da raiz. Commit `8e40c7b`.
- Mortos→quarentena com MANIFESTO SHA (`_organizacao_.../arquivos_mortos/`): `NODE_BUGS_FIXES_INDICE` (0 refs), `MEMORIA_BUGS_HISTORICA` (vazio), `MEMORIA_BUGS_ATUAL` (estagnado jun), `CEREBRO_INDEX_MIGUEL` (espelho órfão). Commit `f3de9da`.
- Snapshots monitoramento 07/08+09/08 → `Backups/monitoramentos_arquivados/`; rodapé do vivo re-linkado; Master: 2 links mortos→nota.

### Fase 2 — Raiz + desinchaço (~08:12) ✅
- `cartoes_bolso/` (6 cartões; refs sedadas); `INDEX_MOKA`→`INDEX_MOKA_LOG` (~12 refs; divisão de papéis no Master) — commit `ee63119`; GSN/VIGIAS/CEARA reconectados ao Master; `INDEX_INCIDENTES_20260522`→quarentena; `memorias_provisorias/` §90: 8 arquivos jun-jul→`Backups/memorias_provisorias/` — commit `6097b99`.
- **Backups frios ~124M→B2** `b2:failover-cafezinho1/faxina/local/cerebro/2026-08/`: tar 27M SHA `89e60588…`, **verificado por download-reversa + sha256 comparado ANTES da retirada local**; inventário 1.776 linhas SHA/arquivo; `Backups/README_ARQUIVO_B2.md` c/ restauração. **Cérebro 291M→162M; Backups/ 144M→13M; raiz 80+→67 .md.** Vivos de ago intocados.

### Validação + automação (~08:15) ✅
- Anti-gato-e-rato ✅ (vários ciclos */15, nada voltou); crons intactos (dashboard 08:00 OK); 20 links Master pré-quebrados = débito Fase 3 (`maestro_viva` corrigido).
- `scripts/manutencao_cerebro.sh` testado (rodada limpa 08:13, relatório `Relatos/manutencao_cerebro_202608.md`) + cron `0 5 1,15 * *`. Só o seguro; candidatos >15d só lista; retirada dupla c/ desfaz-em-falha-de-push; nunca apaga; sync no final (anti-regressão rsync). Limitação: mtime 29/07=migração→falsos candidatos.
- Entrada no `CEREBRO_NODE_ATUALIZACOES.md` (~08:25).

### Incidente escrita concorrente (~08:30-08:50) ⚠️ resolvido
Monitor/fórum/memória regredidos pelo rsync `*/15` (detalhe no fórum). Reescritos + sync forçado. Retiradas estruturais NÃO foram afetadas (protocolo duplo com commit é imune).

## O que falta / próximos passos
- **Fases 3–4** (Foruns/: reviver `por_data/` p/ 457 soltos, rotacionar `canal_trindade.md`+5 cópias, dedup `legacy/`+`gpt_5_6_sol/`, separar JSONs; rotação `ATUALIZACOES.md`) — sessão própria, plano no fórum.
- **20 links pré-quebrados do Master** — limpar na Fase 3.
- Manutenção quinzenal automática (`0 5 1,15 * *`).

## O que preciso de você (Miguel)
- **"Vai" opcional:** descer a quarentena `_organizacao_cerebro_20260814_0755/` (5 mortos + 2 não-md + manifestos) ao B2 e retirá-la do vivo (~300K).
- **"Vai" quando quiser:** Fases 3–4 em sessão própria.
