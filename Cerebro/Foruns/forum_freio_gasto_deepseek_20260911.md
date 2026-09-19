# 🔎 FÓRUM — FREIO DE GASTO DEEPSEEK: varredura + Lite em todos os DS + plano de economia (11/09/2026)

**Ordem do Miguel (11/09 ~09:1x, texto):** reduzir gasto com DeepSeek ("está gastando muito"); varrer onde está vazando; tirar a ronda do DS Miguel (deixar 4/4h com DeepSeek Lite); mudar TODOS os DeepSeeks dos DS para Lite; checar verticais e temáticos; montar plano de economia.
**Executor:** ZCode/Kimi K3 · sessão 11/09 09:20→ · ref **ZM-20260911-FREIO-DS**.
**Tema Duplo:** esta decisão (fórum) + `Memorias/memoria_freio_gasto_deepseek_20260911.md` (log técnico).

---

## 1. O que a varredura achou (o vazamento)

| Fonte de gasto | Número | Status |
|---|---|---|
| **Ronda DS Miguel (Dell)** `*/30` com `deepseek-v4-flash` + raciocínio ALTO | 48 rondas/dia, sessão completa cada (~US$ 0,3-0,6/ronda no ritmo observado de queda de saldo) | 🔴 MAIOR vazador DeepSeek puro — não logava por evento (lacuna D8: mesma chave dos robôs Tencent) |
| **Ronda DS-N Chefe (Tencent)** `*/30` | 20 rondas até 09:30 hoje; mas custo BAIXO: US$ 0,15/dia medido (prompt já pedia Flash p/ rotina) | 🟡 frequência alta, custo baixo — estava em DESACORDO com a ordem do Miguel de 03/09 (4/4h) |
| **youtube_transcriber_autonomo** (Transkriptor URL-direto) | **US$ 6,00 numa ÚNICA transcrição** de vídeo de 1h (S_Xcwpi2KHc, ~08:07 de 11/09); outra rejeitada por qualidade US$ 0 | 🔴 sem teto de gasto — US$ 6 numa tacada |
| **Fábrica V4.1 Cafezinho (NYC)** | 7d: US$ 31,1 total — v4_1_ciclo US$ 21,0 (67%) + v4_1_redator US$ 7,0; dias de setembro: US$ 20-42/dia no banco (pico 04/09 US$ 41,85) | 🟠 maior centro de custo medido, mas é a REDAÇÃO (Miguel: "62% intocável" 03/09) — só propostas, sem mexida |
| Verticais (Rio Carta/cicero/gsn) e temáticos (159.89.185.209) | banco temático VAZIO desde 01/08 (zero gasto) | 🟢 nada vazando |
| Saldo DeepSeek | US$ 4,45 às 09:15 (âncora); queda US$ 0,61 em 15 min (09:00→09:15) no ritmo das rondas | 🟡 |

## 2. 🔴 ACHADO CRÍTICO — a AUTENTICAÇÃO DeepSeek MORREU às ~09:20-09:30

- Ronda do Chefe das 09:00 OK; âncora de saldo leu US$ 4,45 às 09:15; **às 09:25 a chave do Dell (****806b) e às 09:30 a do Tencent (****8762) retornam "Authentication Fails: invalid"** (duas chaves DIFERENTES, mesma conta).
- Consequência: **todo o parque DeepSeek está PARADO agora** (rondas Dell/Chefe falham por auth; revisores caem no fallback da escada; escuta do Chefe idem). O gasto parou sozinho — mas por BROKEN, não por freio.
- Causas possíveis (não verificáveis daqui): Miguel regenerou a chave no dashboard · conta em estado especial (saldo/faturamento). **AÇÃO MIGUEL:** ver o dashboard da DeepSeek — se gerou chave nova, depositar no cofre (ZCode espelha em todos, Regra 4); se a conta travou por saldo, decidir recarga.

## 3. O que foi EXECUTADO (ordem direta do Miguel — "começa por aí")

Todos com backup `.bak_pre_freio_ds_20260911` e `py_compile` OK (rollback = 1 `cp`):

1. **DS Miguel (Dell) — ronda 30/30 → 4/4h**: crontab local linha da `ronda_30min.sh` agora `0 */4` (próxima ronda 12:00). Backup `~/crontab.bak_pre_freio_ds_20260911`.
2. **DS Miguel (Dell) — modelo LITE**: `~/.dsh/settings.yaml` `deepseek-v4-flash`+high → **`deepseek-flash`+low** (backup do settings ao lado).
3. **DS-N Chefe (Tencent) — 30/30 → 4/4h**: crontab ubuntu `ronda_dsn.sh` agora `0 */4` (realinha a ordem do Miguel de 03/09, que havia sido revertida sem registro). Backup `~/crontab.bak_pre_freio_ds_20260911` no servidor.
4. **DS-N Chefe — modelo LITE**: criado `~/.dsh/settings.yaml` no Tencent (não existia → rodava no default interno) com `deepseek-flash`+low; prompt do Chefe já mandava "Flash para rotina" — agora o default do harness acompanha.
5. **Revisores R1/R2**: todas as ocorrências `deepseek-chat` → **`deepseek-flash`** (julgamento de evidências das pernas bing-rss/brave).
6. **Escuta do Chefe (`escuta.py`)**: `deepseek-chat` → `deepseek-flash`.
7. **`dsn_router.py`**: degrau `deepseek("deepseek-v4-flash")` → `deepseek("deepseek-flash")` (mantidos `deepseek-v4-pro` para tarefas complexas e `deepseek-v4-flash-vision-exp` para visão — flash puro não tem visão).
8. **BÔNUS — bug do vigia P11 corrigido**: `est[falhas]` (NameError, quebrava o log justamente quando a leitura do saldo falha) → `est["falhas"]`; vigia agora loga certo ("sem leitura (resposta sem USD); falhas seguidas=2").

**"Lite" = `deepseek-flash`**: lista oficial da conta (`/models`) só expõe `deepseek-flash` e `deepseek-v4-pro`; flash é o degrau de entrada (o mesmo que o prompt do Chefe já chamava de barato). Não existe id "deepseek-lite".

## 4. Plano de economia (números e próximos passos)

| # | Ação | Economia estimada | Estado |
|---|---|---|---|
| 1 | Rondas DS Miguel 48→6/dia | **~US$ 13-22/dia** | ✅ FEITO |
| 2 | DS Miguel v4-flash+high → flash+low | ~3-5× mais barato POR ronda (multiplica a linha de cima) | ✅ FEITO |
| 3 | Chefe 48→6/dia | ~US$ 0,13/dia (custo já baixo; disciplina) | ✅ FEITO |
| 4 | Revisores + escuta + router → flash | reduz custo por veredito/escuta | ✅ FEITO |
| 5 | **Transcriber: teto de gasto** (ex.: cap US$ 3/dia OU só vídeos ≤30min OU aprovação prévia >30min) | evita picos de US$ 6+ numa tacada | 🟡 PROPOSTO — aguarda "vai" |
| 6 | Cascata de curadoria da fábrica V4.1 (NYC): 1º degrau deepseek → flash | ~US$ 10/7d (v41_ciclo = 67% do medido) — redação, mexe só com "vai" | 🟡 PROPOSTO |
| 7 | Chave DeepSeek PRÓPRIA para o Dell (separa escritório×robôs; código do reporter_us65 já pronto com flag REGISTRAR_BANCO) | não economiza direto, mas ACABA com a lacuna de medição (sabemos quem gasta o quê) | 🟡 PROPOSTO — pendência D8 antiga |
| 8 | Recarga/regularização da conta DeepSeek | sem isso, NADA do parque DeepSeek roda (nem em Lite) | 🔴 AÇÃO MIGUEL |

**Projeção com 1+2+4 (já valendo quando a auth voltar):** de ~US$ 20-40/dia para **~US$ 4-8/dia** no lado DeepSeek (rondas+revisores+escuta), fora a redação.

## 5. O que aconteceu / o que falta / o que preciso de você (Miguel)

- **O que aconteceu:** freio executado por completo (rondas 4/4h + Lite em 100% dos DS, com backups e compilação); varredura feita (vazadores identificados e medidos); verticais/temáticos conferidos (zerados); vigia P11 consertado.
- **O que falta:** prova de fogo das rondas em flash (próxima janela 12:00, quando a auth voltar); itens 5-7 do plano aguardam "vai"; conferir após a troca se `deepseek-flash` se sai bem nos vereditos dos revisores (escada tem fallback GLM se não).
- **O que preciso de você:** (1) resolver a CHAVE DeepSeek no dashboard (regenerada? travada? — tudo está parado desde ~09:30); (2) dizer "vai" nos itens 5-7 do plano; (3) se regenerar a chave, depositar no cofre que o ZCode espelha na hora (Regra 4).

**Rollback geral:** `cp` dos `.bak_pre_freio_ds_20260911` (Dell: crontab+settings; Tencent: crontab, router, revisores, escuta, vigia `.bak_pre_fix_falhas_20260911`).
