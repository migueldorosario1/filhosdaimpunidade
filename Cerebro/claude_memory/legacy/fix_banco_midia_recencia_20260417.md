---
name: Banco de mídia prioriza fotos recentes (2026-04-17)
description: Scoring do gerenciador_imagens ganhou bônus/penalidade por data_foto; Tribunal Visual recebe idade da foto e rejeita fotos 2+ anos em pauta corrente.
type: project
originSessionId: 82c307d7-bd07-4c7a-8ed2-9e86b6fa4e22
---
Em 2026-04-17 Miguel pediu que o banco de mídia priorize fotos RECENTES, especialmente pra pautas sobre Lula e política nacional. Antes, o scoring textual colocava foto de 2010 no mesmo patamar de foto de 2026.

## Fix em `gerenciador_imagens.py`

**Bônus de recência no scoring** (antes de enviar ao Tribunal):

| Idade da foto | Bônus no score |
|---|---|
| ≤ 30 dias | +60 |
| ≤ 90 dias | +40 |
| ≤ 180 dias | +25 |
| ≤ 365 dias | +10 |
| ≤ 2 anos | 0 |
| 2-5 anos | -15 |
| > 5 anos | -30 |

- Bônus só se somado quando `score_textual > 0` (não bonifica rejeitadas).
- Tupla candidata cresceu: `(score_total, intersecao, dias, reg)`.
- Ordenação final: `(score DESC, intersecao DESC, dias ASC)` — empate textual → mais nova ganha.
- Log mostra idade: `⚖️ Julgando candidata com Score Textual 120 (Keywords: 3, Idade: 238d atrás)`.
- `data_foto` e `dias` passados ao Tribunal Visual como parte do `contexto_original`.

## Fix em `agente_roteador_llm.py` (prompt do Tribunal)

Adicionada regra 6 no bloco "REPROVE AUTOMATICAMENTE quando":

> **6. RECÊNCIA E CONTEXTO TEMPORAL.** Os metadados frequentemente trazem a data real da foto. Se a matéria trata de FATO CORRENTE (pronunciamento desta semana, reunião de hoje, conflito ativo) e a foto é de 2+ anos atrás retratando OUTRO evento específico — REPROVE. Exceção: retrato/plano neutro da pessoa (Lula sério, Putin em pronunciamento) é OK para ilustrar atitude/declaração recente, desde que aparência e vestimenta não destoem. Para pautas HISTÓRICAS (aniversário, retrospectiva, "há X anos"), fotos antigas são ideais.

## Teste pós-fix

Busca "Lula pronunciamento" + resumo "discurso desta semana sobre o Irã":
- Antes: aprovava foto de 02.12.2023 (Lula com Keir Starmer em Dubai), legenda admitia "em Dubai 2023".
- Depois: **reprova todas as 4 candidatas antigas** do banco. Cai no fallback (gerador cartoon).

Consequência: se o banco não tem foto recente do tema, cai no cartoon. O `robo_coleta_imagens` (15,45 * * * *) precisa continuar enchendo o banco.

## Limite conhecido

O campo `data_foto` no banco SQLite vem de:
- **Flickr:** `dateupload` (upload no Flickr) — geralmente bate com a data do evento
- **Wikimedia:** `timestamp` da foto no Wikimedia — às vezes é upload muito posterior ao evento real (ex: foto de 2023 uploadada em 2025)

No segundo caso, `dias` pode estar otimista (mostra a foto como mais nova do que realmente é). O Tribunal Visual mitiga isso ao ver a foto — detecta vestimenta antiga, envelhecimento, etc.

## Backups

- `/root/gerenciador_imagens.py.bak_20260417_1320`
- `/root/agente_roteador_llm.py.bak_20260417_1320` (mais backups do mesmo dia também existentes)

## How to apply

- Para endurecer mais, aumentar os bônus (60→80 no último mês) ou reduzir a janela (30→14 dias).
- Para afrouxar quando o banco ficar pobre, reduzir penalidades (-30→-10 pra >5 anos).
- Se pauta for sobre evento histórico, o prompt do Vision já tem exceção ("pautas HISTÓRICAS, fotos antigas são ideais").
