# 🗂️ Triagem da Velharia — 117 rascunhos da esteira (4+ dias) — 01/09/2026 08:0x BRT

**Maestro:** ZCode/GLM-5.3 · **Fonte:** SQL no banco do Cafezinho (drafts COM `zizi_job_id` — o legado de 2013-2025, outros 2.253 drafts, é um problema separado de arquivamento histórico).

## Números
| Faixa | Quantidade | Leitura |
|---|---|---|
| 4-7 dias | 2 | Salváveis com checagem rápida |
| 8-15 dias | 71 | Maioria perecível; poucos duráveis |
| 16+ dias | 44 | Quase tudo perecível (mais antigo: 31/03, inclusive um "Test") |

## O que a amostra mostra
- **Perecíveis dominantes** (hard news morta): Irã×EUA/Ormuz de abril-julho, "ataca Springsteen", CPI do Mastic, lobby pró-Israel, Flávio articula com EUA etc. — o fato central já não é notícia; publicar em setembro fere o FRESCOR (regra viva da casa) e o Google pune conteúdo reciclado.
- **Duráveis possíveis** (análise/opinião): "A pauta sem nome e a crise da representação", "A espiral do silêncio ataca outra vez" — temas que não envelhecem; ainda assim exigem atualização de dados.
- **Lixo técnico**: 229614 "Test" e eventuais vazios.

## Recomendação do maestro (decisão é do Miguel — nada foi apagado)
1. **A) ARQUIVAR os perecíveis de 16+ dias (44)** — mover para status arquivado/trash com backup da lista (reversível); limpa a fila mental da editoria.
2. **B) Os 71 de 8-15 dias:** editoria (CM/CL) marca até 10 candidatos duráveis → revalidação de fato central → os demais entram no lote A na próxima triagem.
3. **C) Os 2 de 4-7 dias:** revalidação rápida na ronda (fato ainda vive? capa? publica; morreu? lote A).
- **Regra mantida:** NUNCA publicar velharia sem revalidar o fato central (FRESCOR-V5, teto hard news 24h).
- Legado 2013-2025 (2.253): proposta separada de arquivamento histórico em massa (decisão futura do Miguel).

## Comandos prontos (a executar só com "vai")
- Listar IDs do lote A: SQL por faixa 16+ dias com zizi.
- Arquivar com prova: `wp post update <ids> --status=trash` (backup CSV antes; reversível por 30 dias na lixeira do WP).
