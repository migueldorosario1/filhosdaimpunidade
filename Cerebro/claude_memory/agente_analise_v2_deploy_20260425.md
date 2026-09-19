---
name: Agente Análise V2 — deploy completo 2026-04-25 ~10h BRT
description: 9 tarefas executadas (§15.6/15.7/15.8/§18/§19/§20 do forum). Pipeline LIVE com Top 30, Opus elite, cron 2x/dia. Validação real OK no post 239614. Tarefa 2 PAUSADA — aguarda fim da Tarefa 1 (mudanças estruturais em outro escopo) antes de qualquer mudança nova.
type: project
originSessionId: 372483cf-746c-41be-98b2-407f880fb471
---
**Status:** Tarefa 2 (Agente Análise) PAUSADA por decisão Miguel 25/04 ~10:08 BRT. Mudanças estruturais em outro escopo (Tarefa 1) precisam terminar antes. NÃO codar mais nada do Análise sem ok explícito.

## Estado deployado em produção (Cingapura `/root/`)

### Arquivos novos / modificados

| Arquivo | MD5 servidor | Mudança |
|---|---|---|
| `/root/agente_analise.py` | `dca94d9...` | `_bootstrap_historico` aponta pro `banco_top30.json` (com fallback defensivo pro corpus amplo) |
| `/root/preparar_top30.py` | `1812d1d...` | NOVO — converter Top 30 .md → banco_top30.json |
| `/root/analise/camada1_escuta.py` | `4ee620c...` | Renomes: `CURADORIA_MANUAL` → `CURADORIA_DIA`, fonte `"curadoria_manual"` → `"curadoria_dia"`. Docstring §15.8 explícita |
| `/root/analise/camada4_redacao.py` | `f31ed4b...` | `LIMITE_PALAVRAS 700-1200`, `LIMITE_PERIODOS=3`, rewrite prompt sincronizado, **`_montar_few_shots` injeta 10 exemplos do Top 30** (~6KB) |
| `/root/analise/llm_router.py` | `7bca67d...` | `_HARDCODE_ELITE` + `_CASCATA_OPUS` (4.7→4.5→4.1). `papel="padrao"` SOBE pra Opus. NUNCA cai em Sonnet pra papéis luxo |
| `/root/analise/wp_publisher.py` | `7552f12...` | Bloco `<details>` Matriz REMOVIDO (§15.7). Corpo do post = só Prosa Camada 4 |
| `/root/analise/mayra_whatsapp_notifier.py` | `ce44ebc...` | Frase `"Diga _publique_ ou _descarte_"` removida (§15.8). Mayra é só notificadora passiva |
| `/root/agent_data_analise/banco_top30.json` | `6f2a31e...` | NOVO — 30 posts, 26.493 palavras totais, média 883 |

MD5s validados local↔servidor.

### Crontab

- **`13 11,18 * * *`** `/root/run_analise.sh` (era `13 */3` = 8x/dia, agora 2x/dia conforme §15.6)
- Próximos disparos automáticos: 11h13 e 18h13 BRT
- Backup pré-mudança: `/root/crontab_backup_pre_analise_2x_20260425_0958.txt`

### Histórico (`/root/agent_data_analise/historico.db`)

- **DELETE seletivo** dos 7320 rows com `fonte=miguel_bootstrap` (corpus amplo legado descartado conforme §19)
- Preservado 1 row de `fonte=agente_analise`
- REINSERIDOS 30 rows do `banco_top30.json` via `bootstrap_do_corpus`
- Total atual: **31 rows** (1 do agente + 30 do Top 30)
- Backup pré-rebootstrap: `/root/agent_data_analise/historico.db.bkp-pre-rebootstrap-20260425_0959`

### Validação em produção (run real)

- Run `20260425_1001_62cfe9` → **post 239614**
- Título: "Ataque ao Irã revela ensaio dos EUA para nova guerra híbrida global"
- 799 palavras, lentes geopolítica+econômica
- Anti-repetição: `sim.hist.max=0.0286` (quebrou STF/golpismo)
- Fact-check Perplexity: **APROVADO** ativo (§15.4 fix funciona)
- Roteador: Opus 4.7 deu HTTP 400 → caiu em **Opus 4.5** sem tocar Sonnet (§20 cumprido)
- Auditoria Grok-4: PUBLICAR_COM_RETOQUES, FC 6/10, alucinação MÉDIO, **estilo 7/10** (subiu de 6/10), viés Sul Global ✓

## Backups defensivos no servidor (NÃO apagar)

- `/root/crontab_backup_pre_analise_2x_20260425_0958.txt`
- `/root/backup_analise_v2_20260425_<HHMM>/` (6 .py snapshot pré-deploy)
- `/root/agent_data_analise/historico.db.bkp-pre-rebootstrap-20260425_0959`

## Pendências em aberto (NÃO mexer enquanto Tarefa 2 estiver pausada)

- Migrar status `draft` → `publish` com gate Grok-4 (Opção C), só após 24-48h de estabilidade (§18.A)
- `MIGUEL_WHATSAPP_ID` no `.env.unificado` (Mayra está silenciosa)
- Camada 5 Distribuição (carrossel IG / thread X / thumb YT) — V2

## Ineficiências observadas (anotação, não fix)

- Roteador faz 2 tentativas Opus por chamada (4.7 → 400 → 4.5). Custo OK pra qualidade (§20), mas log fica barulhento.
- `_reescrever_paragrafo_longo` chama Opus a cada parágrafo longo. Em texto com 5+ longos, são 5+ chamadas Opus extras.
- Acompanhar `snapshot_custos_*.json` pra calibrar.

## Documentação completa

- `Projeto Cafezinho Agentes/root/forum_agenteanalise.md` §21 — relatório de deploy completo
- Forum único agora (12KB redundante na raiz foi fundido em §16, virou `.bkp-pre-fusao-20260425_0856`)
