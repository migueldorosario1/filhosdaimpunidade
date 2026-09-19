# 🧹 Fórum — Organização do Cérebro + Manutenção Regular (14/08/2026)

**Sessão:** ZCode GLM-5.2 · **Ordem:** Miguel ("faça um plano de organização do cérebro, temos que fazer isso regularmente. investigue o cérebro e proponha.")
**Estado:** ✅ FASES 0–2 CONCLUÍDAS + manutenção quinzenal no ar
**Memória irmã:** `Memorias/memoria_organizacao_cerebro_20260814.md` (Tema Duplo)

## Diagnóstico (investigação com 4 subagentes + leitura direta)

Cérebro: **291M · 3.979 `.md` · 6.111 arquivos**. Sete focos:

1. **Inchaço de backups (77% = 225M):** `Backups/` 144M (~120M frio-movível) + `backup_total_2026/` 81M (**VIVO — cron `*/30` com path hardcoded, NÃO mexer**). Cânone real de conteúdo = repo `~/cerebro-miguel/` (GitHub */30 + B2/Drive/Alibaba 03:40).
2. **Raiz com 80+ `.md`** misturando Camadas 1/2 + cartões-bolso + snapshots datados + memórias de bugs.
3. **4 pastas de memória:** `Memorias/` (cânone ativo) · `MEMORIA/` (legada → fundível) · `claude_memory/` (memória do Claude, complementar — **fica**) · `memorias_provisorias/` (§90, higiene atrasada).
4. **7 arquivos de bugs = 4 sistemas paralelos:** vivos = `NODE_BUGS_ATIVOS`+`RESOLVIDOS`; mortos = `FIXES_INDICE`, `MEMORIA_BUGS_HISTORICA`, `MEMORIA_BUGS_ATUAL`; `NODE_BUGS.md` stub (49 inbound) fica.
5. **14 INDEXes:** `MOKA`×`MOKA_MASTER` ambíguos; órfãos do Master: GSN/VIGIAS/CEARA/INCIDENTES; `INDEX_MIGUEL` link morto.
6. **`Foruns/` 44M crescendo:** `por_data/` morto desde 15/06; 457 `.md` soltos (87% fora do índice); `canal_trindade.md` + 5 cópias; duplicação `legacy/`+`gpt_5_6_sol/`.
7. **Logs append-only nunca rotacionados:** `CEREBRO_NODE_ATUALIZACOES.md` = 5.662 linhas.

## Decisões (aprovadas pelo Miguel)

- **Escopo agora:** Fases 0–2 (Moderada). Fases 3–4 (Foruns/ + rotação de logs) = follow-up.
- **Cadência regular:** quinzenal (casa com a regra dos 15 dias da faxina canônica).
- **Execução:** script automatizado SÓ o seguro + relatório Telegram; destrutivas sempre com "vai" explícito.
- **Alinhamento:** metodologia da faxina canônica (`Memorias/memoria_missao_faxina_diaria_legacy_20260811.md`): 15 dias, inventário, manifesto+SHA, quarentena, autorização explícita, leveza ≠ perda de histórico.

## Descobertas críticas de execução

**1. Sync em cascata (gato-e-rato):** `*/30` `sync_cerebro_to_github.py` copia Cérebro→repo **só adicionando**; `*/15` rsync repo→Cérebro **sem `--delete`** re-cria o que faltar. → Toda RETIRADA exige protocolo duplo: mover no vivo + remover no repo + commit (validado: nada voltou após vários ciclos).

**2. rsync regredi edições recentes (⚠️ IMPORTANTE p/ todas as sessões):** o `rsync -a` do `*/15` copia origem→destino sempre que o arquivo DIFERE (mtime/size) — **não protege destino mais novo** (não é `-u`). Um edit no Cérebro vivo pode ser REVERTIDO pelo rsync seguinte até que o `*/30` atualize o repo (janela ≤15min). **Vítimas nesta sessão:** linha do monitor (07:58, morta pelo rsync 08:00) e adendos deste fórum e da memória irmã (~08:20, mortos pelo rsync 08:30; de novo às 08:45 antes do sync salvar). **Protocolo: após editar qualquer arquivo do Cérebro, forçar o sync imediatamente** (`cd ~/cerebro-miguel && CEREBRO_DRY_RUN=0 python3 scripts/sync_cerebro_to_github.py`).

## Fases

| Fase | Conteúdo | Status |
|---|---|---|
| 0 | Checkpoint git `ba974109` (07:57) + quarentena `_organizacao_cerebro_20260814_0755/` + registros | ✅ |
| 1 | `MEMORIA/`→`Memorias/`; mortos→quarentena; snapshots→`Backups/` | ✅ |
| 2 | `cartoes_bolso/`; INDEXes; `memorias_provisorias` §90; ~124M frio→B2 | ✅ |
| 3 | (follow-up) Foruns/: reviver `por_data/`, rotacionar canal, dedup legacy/gpt_5_6_sol | ⏳ |
| 4 | (follow-up) Rotação `ATUALIZACOES.md` e índices append-only | ⏳ |

## O que aconteceu (log da execução)

### 07:55 — Fase 0 ✅
- Checkpoint git `ba974109` (ponto de restauração, push OK). Quarentena `Cerebro/_organizacao_cerebro_20260814_0755/`. Linha no monitor + Tema Duplo criado.

### ~08:02 — Fase 1 ✅
- **`MEMORIA/`→`Memorias/`:** 29 `.md` (121→150 na canônica), zero colisão; `relatorios/`→`Memorias/memoria_legada_relatorios/`; `.log/.json`→quarentena; redirecionador por 1 ciclo; refs da raiz sedadas. Commit `8e40c7b`.
- **Mortos→quarentena** (MANIFESTO SHA-256 em `_organizacao_cerebro_20260814_0755/arquivos_mortos/`): `NODE_BUGS_FIXES_INDICE` (0 refs) · `MEMORIA_BUGS_HISTORICA` (vazio) · `MEMORIA_BUGS_ATUAL` (jun) · `INDEX_MIGUEL` (espelho órfão). Commit `f3de9da`.
- **Snapshots de monitoramento** (07/08, 09/08) → `Backups/monitoramentos_arquivados/` + rodapé do vivo re-linkado.
- **Master:** 2 links mortos da seção "🌌 0" substituídos por nota (`INDEX_MIGUEL` + `PROJETO_CEREBRO_IMORTAL.md` inexistente).

### ~08:12 — Fase 2 ✅
- **`cartoes_bolso/`:** 6 cartões fora da raiz; refs `Cerebro/CARTAO_BOLSO_`→`Cerebro/cartoes_bolso/…` sedadas em todo o Cérebro vivo. Commit `ee63119`.
- **`INDEX_MOKA`→`INDEX_MOKA_LOG`:** desambiguação documentada no Master (LOG detalhado × HANDOFF no `MOKA_MASTER`); ~12 refs atualizadas. Mesmo commit.
- **Reconexão Camada 1:** `INDEX_GSN` (ativo), `INDEX_VIGIAS` (draft 17/06), `INDEX_CEARA` no Master; `INDEX_INCIDENTES_20260522` (snapshot, 0 refs)→quarentena. Mesmo commit.
- **`memorias_provisorias/` §90:** 8 arquivos jun-jul (>15d, não-slots-vivos) → `Backups/memorias_provisorias/`; refs atualizadas. Commit `6097b99`.
- **Backups frios → B2:** 9 pastas + 3 soltos (≤30/07, ~124M — incl. `backup_cerebro_20260728_164635` 25M e `telemetria_custos_20260728` 86M) → `b2:failover-cafezinho1/faxina/local/cerebro/2026-08/`: pacote 27M SHA-256 `89e60588…` **verificado byte a byte por download-reversa antes da retirada local**; inventário integral 1.776 linhas com SHA por arquivo; `Backups/README_ARQUIVO_B2.md` documenta restauração. Pastas vivas de ago intocadas.

### ~08:15 — Validação ✅
- **Anti-gato-e-rato ✅:** vários ciclos do rsync `*/15` passaram; nada retirado voltou (protocolo duplo funciona).
- **Crons intactos ✅:** `backup_total_2026/` intocado (dashboard 08:00 OK); Foruns→Tencent só ganhou este fórum.
- **Raiz: 80+ → 67 `.md`.**
- **Débito Fase 3:** 20 links do Master PRÉ-quebrados (fóruns mai-jun, `treinamento/`, `root/agent_data/` — extintos na reforma de arquivos 22/07; não tocados nesta passada). Corrigido apenas `memoria_maestro_viva`→`memorias_provisorias/`.

### ~08:17 — Manutenção regular no ar ✅
- **`scripts/manutencao_cerebro.sh`**: criado, `bash -n` verde, **testado em rodada limpa** (08:13 — `Relatos/manutencao_cerebro_202608.md` + Telegram). Só executa o seguro (snapshots de monitoramento da raiz, MEMORIA residual, redirecionador expirado >14d); candidatos >15d apenas LISTA; retirada dupla com desfaz-em-falha-de-push; **nunca apaga**. Ao final chama o sync Cérebro→repo (proteção contra a regressão do rsync `*/15`).
- **Cron instalado:** `0 5 1,15 * *` → `~/log/manutencao_cerebro.log`.
- **Limitação conhecida:** mtime 29/07 01:0x é da migração em massa → falsos "candidatos" no relatório; candidato ≠ autorização (decisão sempre do Miguel).

### ~08:30-08:50 — Incidente de escrita concorrente ⚠️ (resolvido)
Linha do monitor e adendos deste fórum/memória foram regredidos pelo rsync `*/15` (ver "Descoberta 2"). Nada estrutural perdido — todas as RETIRADAS usaram protocolo duplo com commit (imunes à regressão). Fórum e memória reescritos; monitor re-marcado ✅; sync forçado após cada edição. **Lição para todas as sessões: editar Cérebro ⇒ sync imediato.**

## Estado final

| Métrica | Antes | Depois |
|---|---|---|
| Tamanho do Cérebro | 291M | **162M** |
| `.md` na raiz | 80+ | **67** |
| Pastas de memória | 4 (1 legada) | 3 consolidadas |
| Sistemas de bugs | 4 paralelos (7 arq.) | 1 vivo (ATIVOS+RESOLVIDOS+stub) |
| INDEXes órfãos da Camada 1 | 4 | 0 |
| `Backups/` | 144M misto | 13M só vivos (+frio no B2 c/ manifesto) |
| Manutenção regular | — | quinzenal automática (cron `1,15` 05:00) |

**Próximos passos:** Fases 3–4 (Foruns/ + rotação de logs) em sessão própria — plano completo aqui. **Pendências Miguel:** (1) "vai" opcional p/ quarentena `_organizacao_cerebro_20260814_0755/` descer ao B2; (2) "vai" p/ Fases 3–4.
