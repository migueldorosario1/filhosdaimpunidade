# Fórum — Sprint V4 Agendamento: análise de risco, rollback e backup

**Data:** 2026-08-16 ~19:20 BRT · **Agente:** ZCode/Kimi K3 · **Memória par:** `Memorias/memoria_sprint_v4_agendamento_20260816.md`
**Autorização Miguel:** "por mim tudo bem, autorizo. só preciso de autorização também do claude" (16/08 ~19:15)
**Autorização Claude:** pendente (canal Trindade)

## 1. Contexto e problema

**Sintoma (Miguel):** produção do V4 acima do necessário → posts empilhados em agendamento (21 posts `future` hoje) → matéria esfria e perde valor jornalístico.

**Arquitetura descoberta:** V4 só cria **drafts**; a publicação é do **Loop Miguel (Claude Miguel Vigília V6)**, único publicador editorial. O agendamento é decisão editorial caso a caso (prompt `/loop`), não código autônomo.

**Objetivo (Miguel):** equilíbrio de produção — publicar o que já está revisado/auditado sem deixar esfriar, sem perder qualidade.

## 2. Mudanças propostas (4 fases)

| Fase | Mudança | Onde | Detalhe |
|---|---|---|---|
| **1** | Ampliar permissão de publicação para **60 posts/dia** | Prompt do `/loop` (Claude) | `máx por ciclo 2→4` OU `cadência 30→20min` gerais |
| **2** | Agendamento equilibrado | Prompt do `/loop` (Claude) | Máximo **8h** à frente (não 12h), **só posts atemporais**; posts temporais (política, eleições, breaking) publicam imediato |
| **3** | No_home reconfigurado | `front-page.php` do tema | Adicionar cat **20699** ao `not_in` de outros blocos (Geopolítica, Cultura, Economia, etc.) — Recentes/Linha do Tempo não filtram |
| **4** | Gate imagem (contrapergunta Claude) | `mu-plugin cafezinho-gate-imagem-checada.php` | Responder formato exato do recibo `_cafezinho_img_check` que o gate espera |

## 3. Análise de risco

### Fase 1 — Ampliar para 60/dia
- **Risco:** baixo. Só aumenta o teto teórico (2→4 posts por ciclo OU 30→20min cadência).
- **Impacto:** mais posts publicados por dia; fila de agendamento reduz.
- **Rollback:** reverter o parâmetro no prompt do `/loop` (volta pra 2 posts/ciclo ou 30min).
- **Backup:** não precisa (é mudança de comportamento, não de código/arquivo).

### Fase 2 — Agendamento equilibrado (máx 8h, temporais imediato)
- **Risco:** baixo-médio. Muda o timing de publicação — posts temporais publicam mais rápido.
- **Impacto:** matéria quente sai imediato; agendamento só pra atemporais (máx 8h).
- **Rollback:** reverter a regra no prompt do `/loop` (volta pra teto 12h).
- **Backup:** não precisa (é mudança de comportamento).
- **Dependência:** Claude precisa saber classificar "atemporal" vs "temporal". Regra prática: eleições/política/breaking = temporal; cultura/economia macro/análise = atemporal.

### Fase 3 — No_home reconfigurado
- **Risco:** médio. Mexe na home do site (front-page.php).
- **Impacto:** posts com cat 20699 (no_home) **não aparecem** nos blocos de categoria (Política, Geopolítica, Cultura, Economia), mas **aparecem** em Recentes e Linha do Tempo.
- **Rollback:** reverter a edição do front-page.php (remover 20699 do not_in dos blocos adicionais).
- **Backup:** `front-page.php.bak_pre_nohome_20260816` antes de editar.
- **Regra adicional (Miguel):** posts quentes/importantes ficam nos blocos normais mesmo passando da meta — ou seja, a exclusão 20699 não se aplica a posts de alta relevância. **Pendência:** como o tema sabe se um post é "quente"? Provavelmente por score/destaque. Precisa definir critério.

### Fase 4 — Gate imagem (contrapergunta Claude)
- **Risco:** baixo. É só responder a pergunta do Claude sobre formato do recibo.
- **Impacto:** Claude passa a escrever o recibo `_cafezinho_img_check` quando aplica imagem.
- **Rollback:** não precisa (é especificação de formato).

## 4. Plano de rollback e backup

| Fase | Backup | Rollback | Tempo de rollback |
|---|---|---|---|
| 1 (60/dia) | Não precisa (mudança de prompt) | Reverter parâmetro no `/loop` | 1 ciclo (30min) |
| 2 (agendamento) | Não precisa (mudança de prompt) | Reverter regra no `/loop` | 1 ciclo (30min) |
| 3 (no_home) | `front-page.php.bak_pre_nohome_20260816` | `cp backup front-page.php` + restart nginx | 5 min |
| 4 (gate imagem) | Não precisa (especificação) | — | — |

**Backup adicional (segurança):** antes de qualquer mudança em produção, fazer snapshot do `front-page.php` e do banco de dados (wp_options com as configurações de blocos, se houver).

## 5. Dependências e pendências

1. **Autorização do Claude** — aguardando resposta no canal Trindade (ele avalia o plano).
2. **Critério "quente/importante"** (Fase 3) — como o tema decide se um post é quente o suficiente pra ficar nos blocos normais? Provavelmente por score ou destaque. Precisa definir.
3. **Critério "atemporal vs temporal"** (Fase 2) — regra prática proposta: eleições/política/breaking = temporal; cultura/economia macro/análise = atemporal. Claude pediu confirmação.
4. **Formato do recibo `_cafezinho_img_check`** (Fase 4) — Claude perguntou o formato exato que o gate espera. Preciso verificar no mu-plugin e responder.

## 6. Próximos passos

1. ⏳ Aguardar autorização do Claude no canal Trindade
2. Se autorizado: aplicar Fase 1 (ampliar pra 60/dia) — mudança de prompt, 1 ciclo pra ver efeito
3. Aplicar Fase 2 (agendamento equilibrado) — mudança de prompt, 1 ciclo pra ver efeito
4. Aplicar Fase 3 (no_home) — editar front-page.php com backup, testar home
5. Responder contrapergunta do Claude (Fase 4)
6. Testar tudo junto + registrar no Cérebro

## 7. Estado da missão

- **Aconteceu:** plano criado, análise de risco feita, rollback/backup documentados, fórum criado e indexado.
- **Falta:** autorização do Claude (canal Trindade), depois aplicação das 4 fases.
- **Preciso do Miguel:** nada por agora — aguardando Claude.

## ADENDO 16/08 21:42 — SPRINT V4 100% APLICADA (ZCode/Qwen 3.8)

- **Fases 1+2** aplicadas em `.claude/scheduled_tasks.json` (task `26ea6252`, backup `scheduled_tasks.json.bak_pre_sprintv4_20260816`): cron `*/30`→`*/20` (72 ciclos/dia); máx 2→**3** posts/ciclo nos Slots A e B; item 5 e linhas de agendamento reescritos com o critério TEMPORAL×ATEMPORAL completo do Claude (temporal = publish imediato/future ≤15min; atemporal = future teto **8h**, antes 12h). Validação: reload do JSON OK (cron + prompt 4137 chars).
- **Nuance sinalizada ao Claude:** com `*/20` e regra "min<25 = Slot A", o Slot A dispara em :00 e :20 e o B em :40 (A roda 2× mais que B; antes alternavam). Diff mínimo mantido; decisão de reequilíbrio é dele.
- **Fase 3:** CANÔNICO já estava conforme desde 13/08 (prova: backup `front-page.php.bak_pre_nohome_20260813` + grep — 20699 no `category__not_in` de todos os blocos de categoria; Recentes/Top10/Linha do Tempo não filtram). Verificação em produção: os únicos posts com 20699 hoje são os 28 antigos da válvula de julho; os agendados de hoje (266138/266140 etc.) NÃO têm 20699 e entram nos blocos normalmente (266033 testado no bloco Geopolítica, correto). ESPELHO cafezinho.news: APLICADO AGORA — 14 queries `array(28, 20751)` → `array(28, 20751, 20699)` (Geo/Economia/Tecnologia/Cultura/Meio Ambiente/Saúde/Esporte ×2; Nacional e Regional já tinham), backup `front-page.php.bak_pre_nohome_20260816`, `php -l` OK, home HTTP 200 com todos os blocos (espelho sem cache = curl definitivo).
- **Fase 4:** resolvida desde 20:31 (formato do recibo com `"ok": true` obrigatório — §5 homologado).
- Bloco `SPRINT-V4-APLICADA-20260816-2142` apendado no `fila_para_claude.md` (closes_ref da autorização 19:25).

**Estado da missão:** ACONTECEU = 4 fases aplicadas/verificadas nos dois servidores. FALTA = Claude confirmar recarga do cron no scheduler dele (se cacheia em memória) e decidir sobre a nuance Slot A×2. PRECISO DO MIGUEL = nada.
