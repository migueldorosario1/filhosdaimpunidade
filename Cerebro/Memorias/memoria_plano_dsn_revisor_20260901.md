# Memória — Plano DS-N Revisor + Lei de Poderes v3 (nada publica sem revisão de texto)

**Data:** 2026-09-01 ~18:1x BRT · **Sessão:** ZCode/GLM-5.3 (Dell) · **Fórum:** `Foruns/forum_plano_dsn_revisor_20260901.md` · **Ponte:** ZM-20260901-033 (renumerado: 032 pertence à sessão-irmã 18:02)

## Contexto e decisão

Miguel (~18:0x, após os 3 casos de título/texto do dia): o publicador não pode publicar texto não revisado; criar **robô DSN Revisor** com **check final obrigatório**; plano de trabalho primeiro; **sistema inteiro informado antes de implementar**.

## Provas do diagnóstico

1. Leitura do `dsn_publicador.py` (Tencent): Lei de Poderes v2 (31/08) — único gate = `_cafezinho_img_check` (capa/olho duplo); "fluxo fresco" publica draft de fábrica ≤12h **sem gate de texto**; CL audita a posteriori.
2. Casos do dia: 268553 timecodes no corpo (15:16) · 268482 EMU-2 (12:39) · 268457 "prisão vitrine" (14:31).

## Plano (essência)

- **v3 fail-close:** publicar exige `_cafezinho_img_check.ok` **E** `_cafezinho_revisao_v2.ok` (carimbo EARNED do revisor; sem ele = "aguardando_revisao" na fila + alerta; revisor caído NÃO degrada p/ fail-open).
- **Robô:** Tencent `~/dsn_revisor/`, cron */15, drafts `v41_*`/`v4d_*` (autores 5470/5801/5786; humanos §130 nunca). Eixo título (8 regras EMU + anti-jargão/tradução literal) + eixo texto (artefatos/timecodes/HTML cru/vazamentos, Manual B1, coerência título×corpo, spot-check `_v41_fc`). LLM DeepSeek ~US$ 0,005/post (~$0,10/dia), regra recomendada revisor≠redator do job (fallback GLM/Kimi/gpt-4o-mini). Canal `de_nuvem_revisor.md`. v1 não edita texto (aprova/reprova/sugere).
- **Fases com porta:** F0 ACKs (ponte) → F1 log-only 24h → F2 advisor carimbado → F3 hard gate (homologação CL+Miguel) → F4 métricas semanais.
- **Anti-colisão §112:** hard gate toca no `dsn_publicador.py` em obra pela sessão urgente — só depois do patch dela fechado.

## Arquivos tocados

`Foruns/forum_plano_dsn_revisor_20260901.md` (novo) · `Foruns/ponte_laura_completa/de_dell.md` (ZM-033) · esta memória · `CEREBRO_NODE_ATUALIZACOES.md` · `MONITORAMENTO_DE_TRABALHO.md` (linha).

## O que aconteceu / o que falta / o que preciso do Miguel

- **Aconteceu:** diagnóstico provado + plano completo gravado + sistema informado (ZM-032: CL, DS-N Chefe, AGY, TODOS).
- **Falta:** ACKs CL+DS-N Chefe; fim do patch da sessão urgente; "vai" do Miguel para F1 (build log-only).
- **Do Miguel:** validar 2 pontos de desenho — revisor v1 não edita sozinho; fail-close quando revisor cai (fila segura até voltar).
