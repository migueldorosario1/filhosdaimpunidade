# Fórum — 📉 QUEDA DE PRODUÇÃO/AUDIÊNCIA 31/08: diagnóstico completo + correção do dia-da-semana + normalização 01/09

**Data:** 01/09/2026 11:45 BRT (investigação feita 03:5x→11:26, por voz do Miguel) · **Operador:** ZCode/GLM-5.3 (DSH, sessão direta do Miguel) · **Fontes:** ledger AGY-L, ponte completa (de_laura/de_dell), fórum+memória do maestro 31/08, relatórios DS-N Chefe/Publicidade, contador nginx. **Ordem que originou:** Miguel ~03:5x ("por que publicou tão pouco dia 31? qual é o gargalo? é imagem?") + ~11:3x ("registra tudo. Sempre. Tudo em Fórum").

## 1. Resposta curta à pergunta do Miguel

Não foi uma causa só — **4 problemas empilhados**, e o maior deles NÃO foi imagem: foi o **motor de publicação (AGY-LAURA) mudo por ~9h30** (08:42→18:05) por um lock da ponte. O gargalo de capa (suspeita do Miguel) foi o 2º fator, real e confirmado. O dia fechou com **20 posts** (vs 24 em 30/08 e 28 em 27/08) e um **buraco de publicação das 08:42 às 17:31**.

## 2. Números da produção (régua wp-cli + REST da casa)

| Dia | Posts publicados |
|---|---|
| 27/08 | 28 |
| 28/08 | 22–24 |
| 30/08 | 24 |
| **31/08** | **20** (17 contados às 22:50 + 3 curas pós-meia-noite: 268366 22:55, 268393 23:16, 268334 00:15) |

- Buraco do dia: **nada da esteira entre 08:42 e 17:31** (último post antes: 268406 12:57, direto do Miguel; resgate só às 17:31–18:44).
- Rascunhos novos no dia: 22 — a **escrita** não foi o gargalo.

## 3. As 4 causas-raiz empilhadas (ordem de impacto)

1. **🔴 Lock da ponte calou o motor AGY-L (a maior):** após reboot da máquina Laura 11:05:59, TODAS as rondas :05/:35 puladas por "lock da ponte em uso por ds" — 10 skips seguidos (12:07→16:37), saída rc=0 = **"roda e cala"** (falha silenciosa, ninguém alertado). Última ronda real 08:42; retorno 18:05. Diagnóstico DSL-015/CL-027 (~16:45); causa-raiz fechada na CL-028 (lock de ~11 min da ronda DSL cobrindo a geração LLM inteira); fix DSL-016 17:40 (lock estreito só no trecho git); teste aprovado CL-030 (18:05, 0 skip); **porta pro agy_ronda.ps1 (agy_ronda_new.ps1) AINDA AGUARDA o `copy` de 1 toque do Miguel (CL-035 20:16)**.
2. **🟠 Gargalo de capas (suspeita do Miguel — confirmada como 2º fator):** lei "sem capa = nunca publica" + **Emenda NO-IA ~11:30** (proibida imagem de IA; capa só foto real licenciada) → 5+ posts presos na fila de caça humana (268456/268457/268458/268394/268451, depois 268424) com caçadores ocupados. Cura da noite: 7 receitas de seed armadas (Paes/Natura/Kast/Lula/Altman/Caterpillar/Google). Cura estrutural em andamento: **Banco Ouro V3** (1.214 fotos aprovadas / 474 auto) como camada 1 — degrau 2 (medição em sombra) no ar 02:00.
3. **🟡 Quirk `future`/wp-cron:** posts via REST com data ficavam presos em `future` sem virar — causa-raiz (Ideias-003, 23:16): **evento `publish_future_post` AUSENTE** em transições REST com data incompleta. Prendeu ≥4 posts no dia (268366/268393/268455/268334) e queimava o orçamento 1-post/ciclo do publicador. Cura canônica: `wp_publish_post`.
4. **🟡 Bug triplo do "fluxo fresco" do publicador autônomo** (só descoberto 23:25, adendo 4 do fórum do maestro): meta `zizi_job_id` invisível na REST (faltava mu-plugin) + scan sem `context=edit` + congelamento da fila (1/ciclo elegia sempre o mais antigo + guarda 1h) → o robô autônomo publicou ZERO pelo fluxo fresco o dia todo até o fix.

Contexto agravante: dia consumido por construção (5 robôs novos + sprint MOKA o dia inteiro + SEV-1 01:03 contendo repo público com 59 chaves vivas) + incidente de carga no cafezinho-wp 23:14 (load 31, 500/503 transitórios) + wp-json 503 intermitente.

## 4. Audiência 31/08 — ⚠️ CORREÇÃO: foi SEGUNDA-FEIRA, não domingo

- **31/08/2026 = segunda-feira** (provado com `date`; hoje 01/09 = terça). **ERRO ORIGINAL:** o 1º relatório do DS-N Publicidade (01:5x) rotulou o dia como "cheio e saudável p/ um domingo" e chamou hoje de "segunda fria" — dias trocados. Esta sessão repetiu o rótulo sem conferir; **corrigido em conversa pelo Miguel ~11:3x**.
- **LIÇÃO (já registrada pela casa às 06:05 no ledger AGY-L):** dia da semana vem SEMPRE do `date`, nunca de memória nem de relatório alheio.
- Contador nginx (régua): 50.201 navegações · 14.946 distintos · pico 11h = 2.757 · **vale 18h–20h = 727/967/1.340 ≈ −50% vs demais horas acordadas**. Numa **segunda à noite** (horário nobre de notícia) o vale é AINDA mais anômalo do que o relatório original sugeriu — o "saudável p/ domingo" subestimou o estrago.
- LUMINA ~20+ recordes no dia; FAROL 9.035/dia; GA4 enxerga só 17–26% (gap AMP/JS) e atrasa.
- **Conclusão:** a queda que o Miguel viu = **queda de PRODUÇÃO** (20 posts + buraco da tarde) que furou a audiência **no fim do dia** (vale 18h–20h). O dia cheio do contador não nega o susto: o teto de uma segunda com esteira saudável seria maior.
- **Por que o susto pegou a casa desprevenida:** LUMINA é número sem gráfico; GA4 atrasa e subnotifica; o contador tem gráfico por hora mas o Miguel não tinha painel amigável na mão. (Fio condutor do pedido do 4º contador — ver §7.)

## 5. Normalização 01/09 (dados até 11:26)

- **9 posts até 11:15** (268441 03:16 · 268448 06:03 · 268451 06:24 · 268458 06:47 · 268456 07:46 · 268462 08:30 · 268509 09:13 · 268412 09:45 · 268474 10:31 · 268473 11:15 — 9º/10º conforme régua) — ritmo de dia normal.
- Régua 11:00: **3h=4 (piso da banda saudável 4-6) · 12h=16 · 24h=28 — SEM alerta** (24h=28 = esteira cheia de novo).
- Incidente noturno: **reboot do cafezinho-wp 03:31** (causa ainda com ZM; 11ª confirmação de não-recorrência às 11:00) + 2h44 de esteira muda → **alerta de volume 3h=1 → FECHADO 06:35** com a grade matutina.
- Audiência: manhã quente — 804 distintos/896 visitas até 11:00, pico 79 online às 09:30.
- **Resiliência nova provada:** 268473 travou por legenda → o Publicador **pulou para o próximo elegível** (268474) em vez de parar a fila. 5 posts seguidos sem quirk face 2.
- Abertos: quirk face 2 (post_date futuro — ZM, URGENTE); SLA DSC-003 Ronnie Lessa estourado (porta de download do Dell — ver §6); gate de legenda pt-BR no formato da casa (ZM/Publicador).

## 6. Robôs criados 31/08 — estado em 01/09 (todos registrados no fórum do maestro)

| Robô | Estado hoje 11:26 |
|---|---|
| **DS-N Publicador** (Tencent 15/15) | ⭐ motor da manhã: 6 posts hoje com prova HTTP 200 no relatório do Chefe; fila resiliente |
| **DSN Imagem** (NYC capas 20/20 + caça) | capas da manhã aplicadas (268502/507/512/517/519/530); Banco Ouro V3 medindo em sombra desde 02:00; pendência 15b: relatório diário próprio ainda vazio no INDEX |
| **DS-N Ideias** (30/30) | vivo (estado 10:45); Ideias-003 fechou causa-raiz do quirk; **IDEIA-004 aguarda ✓ do Miguel** |
| **DS YouTube** (Tencent 15/15 + porta Dell */5) | ⚠️ robô saudável, MAS ordem Ronnie Lessa (fala do Miguel 04:20) PENDENTE desde 04:16 — SLA 10:00 estourado por causa da porta do Dell; CL roteou ao ZM; DSC avisou o Miguel 11:01 |
| **DS-N Chefe** (30/30) | rondas 106→119; segurou o diagnóstico da madrugada e a régua |
| **DS-N Publicidade** | 1ª ronda 01:5x entregou a tabela horária que revelou o vale 18h–20h; cadência 2h ainda a confirmar em arquivo |
| Plantão maestro 1/1h (automation) | encerrou na ronda 02:00 (degrau 2 Banco Ouro) — loops oficiais assumiram |

## 7. Lições (para a casa)

1. Falha silenciosa ("roda e cala", rc=0) em tarefa agendada = blindar com verificação de produto (ronda real gerou linha? se não, alerta) — o fix do lock estreito já está validado, falta o `copy` no agy_ronda.
2. Dia da semana SEMPRE do `date` (reincidência: ledger AGY-L 06:05 + esta sessão 11:3x).
3. Susto de audiência em tempo real: cruzar contador×GA4×LUMINA ANTES de declarar queda (regra do node OBSERVABILIDADE § adendo 24/08) — e os instrumentos precisam de gráfico (fio do 4º contador pedido pelo Miguel; pesquisa independente em andamento na sessão).
4. Buraco de produção da tarde vira vale de audiência à noite (18h–20h): a cadeia publicação→audiência tem lag de horas — alerta de volume 3h da régua CL-032 é o detector certo, funcionou (DS-009 01/09).

## 8. REGRA NOVA (ordem permanente do Miguel, 01/09 ~11:35)

> **"Registra tudo. Sempre. Tudo em Fórum."**

Toda investigação/diagnóstico/achado destas sessões DSH a pedido do Miguel vira **fórum datado em `cerebro/Foruns/`** (este arquivo é o 1º da regra) + linha no MONITORAMENTO_DE_TRABALHO §112 + índice semanal. Sem exceção.

— ZCode/GLM-5.3 (DSH) · 01/09/2026 11:45 BRT · commit seletivo no repositório

## ADENDO 1 — segunda × segunda (pedido do Miguel ~11:5x) + spec de gráficos + Baleia 01/09 — 01/09 11:5x BRT

### 1. Comparação com a segunda-feira anterior (24/08)

| Segunda | Posts | Fonte |
|---|---|---|
| **24/08** | **46** ("46 matérias na segunda, madrugada sem furo de grade") | coluna da editora 25/08 (Claude Laura, interina) |
| **31/08** | **20** | wp-cli do maestro (§2) |
| **Variação** | **−57%** | — |

Contexto da série conhecida (repo): dom 23/08 = **44** (recorde na época) · seg 24/08 = **46** · qui 27/08 = 28 · sex 28/08 = 22–24 · dom 30/08 = 24 · **seg 31/08 = 20**. Ou seja: a queda de 31/08 não foi só "menos que ontem" — contra o **mesmo dia da semana** foi um colapso de mais da metade, e a série mostra que a produção já vinha caindo desde 24/08 (46→28→24→20). A percepção do Miguel ("queda muito forte, a gente tava crescendo à beça") está correta e agora quantificada na régua certa (mesmo dia da semana).

Audiência segunda×segunda: o repo NÃO guarda total diário do contador para 24/08 (a série 3h/12h/24h da ponte nasceu ~29/08; painel CCTV/GA4 têm o histórico, fora do alcance desta sessão) — **é exatamente a lacuna que o 4º contador + os gráficos abaixo fecham**.

### 2. Spec de gráficos (idéia do Miguel, padrão GA4 — para o time do contador/LUMINA)

1. **Gráfico de mesmo dia da semana (padrão GA4):** ao estudar qualquer dia, o gráfico compara com os mesmos dias da semana anteriores (na segunda → últimas ~30 segundas-feiras; na terça → as terças; sempre atualizando). Evita comparar segunda com domingo.
2. **LUMINA com gráfico de dias fechados:** média de usuários online ao longo do dia fechado (dia anterior), em gráfico dos **últimos ~15 dias** — hoje o LUMINA é só número, "sem graça", sem curva.
3. **4º contador:** instalação em andamento EM OUTRA SESSÃO do Miguel — esta sessão NÃO duplica; a spec acima vale para quem implementar (contador novo, LUMINA ou painel CCTV).

### 3. Baleia Azul de hoje (01/09 manhã — como foi)

Fechada às **07:10** pela DS Laura (editora titular), arquivo `baleia_azul/boletim_baleia_azul_20260901_manha.md`: pegou o site no ponto de virada — reboot do servidor 03:31 (causa com ZM), esteira 2h47 em silêncio (03:16→06:03) com alerta de volume tratado sem re-alarme, reabertura 06:03 com o post da OpenAI; "Lula envia último Orçamento" (23:55) encerrou a noite de segunda; pauta do dia = ordem 04:20 do Miguel (Ronnie Lessa/Record, dependendo do DS YouTube/"Deni" + Dell ligado). Pendências com dono listadas (reboot, face 2, BUG-DS-098 camada C, nyc, P3 Banco Ouro, MOKA 015-017, IDEIA-004, arquitetura CL-041). Próxima edição: **tarde, fechamento 19:15**.

— ZCode/GLM-5.3 (DSH) · 01/09/2026 11:55 BRT · commit seletivo no repositório

## ADENDO 2 — implementação dos gráficos no CCTV + liberação SSH Tencent→us65 — 01/09 12:02 BRT

**Ordem do Miguel (~12:0x):** os gráficos de comparação por dia têm que estar **no painel CCTV** (http://43.156.151.165/v6/), nas páginas **FAROL, LUMINA e GA4**.

**Mapa levantado (12:0x):**
- Painel CCTV v6 = `painel_cctv_v6.py` na **Tencent** (43.156.151.165:38422, user ubuntu). Esta sessão roda no **us65.serverdo.in = cafezinho-wp (190.89.239.65)** — o servidor do WP, do contador e do LUMINA.
- SSH us65→Tencent: porta 38422 alcançável, mas **chave local não autorizada** (id_rsa 2023 root@serverdoin recusada). A autorização DSC-023 (Miguel, 30/08: liberar SSH Tencent p/ us65) nunca foi materializada — DS-095/DS-Dell ficou de entregar a chave.
- **Dados locais disponíveis (matéria-prima dos gráficos):** `/root/cafezinho_contador/historico.csv` (2.282 linhas desde 24/08 14:30, pontos ~5min: online/navegações do dia/distintos) + LUMINA = leitura do **banco Matomo** via `/root/lumina_resumo.php` (endpoint JSON token-protected consumido pelo CCTV /v6/lumina) + push do contador pro painel: `POST http://43.156.151.165/v6/api/audiencia-receber` (X-Token, fail-soft).

**Ação (12:01):** prompt pronto enviado ao Telegram do Miguel (`telegram_dsc/RESPOSTAS.md` 12:01:30) pra colar no ZCode do Dell — 1 linha idempotente que acrescenta a chave pública root@serverdoin ao authorized_keys do ubuntu na Tencent (c/ rollback escrito). Aviso na ponte: ZM-20260901-030 (de_dell.md 12:02). **Próximo passo assim que liberado:** testar SSH → mapear `painel_cctv_v6.py` (páginas FAROL/LUMINA/GA4 + fontes) → implementar gráficos por dia com comparação de mesmo dia da semana → backup `.bak_pre_graficos_dias_20260901` + py_compile + restart + prova HTTP.

— ZCode/GLM-5.3 (us65) · 01/09/2026 12:02 BRT

## ADENDO 3 — 📊 GRÁFICOS POR DIA DA SEMANA NO AR nas 3 páginas do CCTV — 01/09 13:05 BRT ✅

**Ordem do Miguel (~12:0x):** "o gráfico tem que estar lá no CCTV no painel na página do farol do lumina e do ga4 — bota gráficos por dia pra comparar". **FEITO.**

### Caminho até lá (registro honesto)
1. **SSH us65→Tencent liberado pelo ZM** (DSC-023, 30/08 → cumprida 01/09): 1ª tentativa 12:05 falhou silenciosamente — a cola do Telegram **amassou 1 caractere** da chave (570 vs 569 chars, `ssh-keygen` dizia "not a public key file"). Cura: ZM instalou a linha íntegra direto do repo (`Foruns/ponte_zm_dsc/us65_pubkey.pub`, commit 61ef72f35) — **via repo não amassa**. Lição: credencial longa via Telegram = frágil; via git = à prova.
2. **Canal ZM↔us65** (`Foruns/ponte_zm_dsc/`): meu lado em de_dsc.md (CHECK ZD-001 + respostas às 4 perguntas + fingerprint SHA256:3040GN…). Identidade esclarecida: eu sou a sessão DSH do us65, não o DS Celular.
3. Deploy com ritual da casa: **backup** `painel_cctv_v6.py.bak_graficos_dias_semana_20260901` → `py_compile` no Python **3.12 da Tencent** (o 3.10 local rejeita f-strings pré-existentes — compilar sempre LÁ) → `systemctl restart cctv-v6` → prova HTTP.

### O que entrou (funções novas no `painel_cctv_v6.py`)
- `svg_mesmo_dow(serie, rotulo)` + `_serie_mesmo_dow` + `_dow_plural`: **o gráfico padrão GA4** — barras dos últimos ≤30 MESMOS dias da semana, dourada = mais recente, linha verde tracejada = média do dia da semana, delta colorido ±% vs média. SVG puro, sem JS, estilo da casa. Degrada bonito: com 1 ponto mostra "começa agora — completa uma barra a cada semana".
- `_farol_serie_diaria(campo)`: dias FECHADOS do FAROL (última leitura cumulativa do dia; hoje fora, igual GA4).
- `_umami_serie_diaria` + `_umami_svg_media_hora(15)`: série diária e **curva média por hora do dia** (dias fechados) do LUMINA.
- Páginas: GA4 `/v6/audiencia` (card novo), FAROL `/v6/audiencia-redundante`, LUMINA `/v6/lumina` (2 blocos novos).

### Raio-X do Umami (achado de brinde)
- Esta versão devolve timestamp na chave **`x`**, não `t` — o gráfico **24h existente estava lendo `t` e mostrando "aguardando beacons"**; consertado junto (agora lê `x` OR `t`) → 24h ressuscitado.
- `unit=hour` só responde horas em **janelas ≤24h** (em 15 dias ele diariza) → a média-hora fatia os 15 dias em 15 chamadas de 24h, agrega por hora-do-dia BRT e **cacheia 10 min** (`lumina_media_hora_15d.json`).

### Provas (curl na Tencent, 13:0x)
- `/v6/audiencia` → **HTTP 200** · "14 últimas segundas · média 8.5k views · mais recente (31/08): 2.345"
- `/v6/audiencia-redundante` → **HTTP 200** · "2 últimas segundas · média 7.1k visitantes distintos · mais recente (31/08): 9.434" ← **a própria queda de 31/08 virou gráfico: segunda 24/08 × segunda 31/08**
- `/v6/lumina` → **HTTP 200** · "pageviews/hora (média) · 6 dias fechados (hora BRT)" · pico **às 10h** · "1 última segunda · média 3.5k visitas · 31/08: 3.550" · 47 `<rect>` (curva nova + 24h vivo)
- Marca de rastreio no HTML das 3: `<!-- graficos_dias_semana_20260901 -->`
- Auto-atualiza a cada visita; cada semana nova acrescenta uma barra por dia da semana.

— ZCode/GLM-5.3 (us65) · 01/09/2026 13:05 BRT
