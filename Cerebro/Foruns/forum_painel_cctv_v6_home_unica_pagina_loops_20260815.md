# Painel CCTV V6 — página Loops (Laura+Miguel), Home única e automação 30/30min

**Data:** 15/08/2026, ~12:45 BRT
**Responsável:** ZCode (Kimi K3)
**Estado:** ✅ entregue, no ar e validado ao vivo

## Ordem do Miguel

1. Colocar no ar os relatórios resumidos do **Loop Laura** e do **Loop Miguel** — uma página só desses relatórios.
2. **Recompactar o painel**: estava disperso, com "Home" (/painel/ estática) e "V6" cumprindo papel de home. Passa a existir **apenas uma Home V6**, com índice de todas as páginas importantes.
3. ZCode (Kimi) fica **responsável permanente** pelo painel, com **tarefa agendada de 30 em 30 minutos** para mantê-lo saudável e atualizado.
4. A cada 30 minutos, enviar ao **Telegram (Ponte Cafezinho)** um relatório do sistema: loop laura, loop miguel, publicações feitas, erros encontrados, audiência, online, % de crédito GLM/Qwen/Kimi.

## O que foi entregue

### 1. Página `/v6/loops` (nova)

- **Loop Laura:** último consolidado do chefe com pills de estado (loop, Claude/Codex/Grok, ordens abertas/concluídas, janela BRT, pill de cadência que amarela se >45min) + corpo integral renderizado; histórico dos últimos 13 consolidados com seleção `?rel=NNN`.
- **Loop Miguel:** fila operacional (INDEX_ATIVO — itens, prioridades com pills, prazos, tickets), alertas de SLA (CRITICO/ATENCAO) e estado da ponta tripla (ESTADO_ATUAL).
- **Fontes no servidor:** `v6_data/foruns/loop_trindade_laura/controle/relatorios_chefe/` e `v6_data/foruns/ponte_trindade_daemon/` — alimentadas pelo rsync local→Tencent já existente (cron `7,37`). Nenhum sync novo foi preciso.
- **APIs JSON novas:** `/v6/api/loops` (resumo dos dois loops) e `/v6/api/resumo` (audiência GA4 + publicações WP) — são o que o relatório do Telegram consome.

### 2. Home V6 única (recompactação)

- NAV deixa de apontar para `/painel/` (estática legada); botão "🏠 Home" agora é a própria V6, sempre dourado.
- Home reescrita como **índice completo**: 13 páginas em 4 grupos (Operação ao vivo · Números · Infraestrutura · Comando), incluindo as que ficavam fora dos cards (Backup, Temáticos, Diretrizes CEO, Servidores) e a nova Loops.
- Nginx: `location = / { return 301 /v6/; }` — a raiz do servidor (era a página "Welcome to nginx!") agora aterrissa na Home V6. Backup `painel.conf.bak_pre_redirect_raiz_20260815`.
- O painel v5 (:8082) e os estáticos `/painel/` seguem no ar pelas URLs diretas — só deixaram de ser a porta de entrada. Aposentadoria definitiva fica para ordem futura.

### 3. Relatório Telegram 30/30min

- Script determinístico `~/bin/cctv_relatorio_30min.py` (local): health-check do painel com **auto-restart via SSH** (`cctv-v6`, cooldown 20min), coleta loops/publicações/audiência/online/erros/créditos e envia pela Ponte Cafezinho.
- Créditos: Kimi/Qwen lidos do `--status` da vigília; GLM via quota oficial Z.ai (reusa função do hook `credito_vigilia.py`).
- Automação ZCode **`automation-e3465bb3-312f-4583-9a72-7f69711fc147`** (a cada 30min, recorrente): roda o script, garante rsync fresco e serviço ativo, registra incidente no Cérebro se não conseguir corrigir.
- **Primeiro envio real: 15/08 12:36 BRT ✅** (🟠 por 1 crítico na fila do Loop Miguel — comportamento correto).

## Validação ao vivo

`/v6/`, `/v6/loops`, `/v6/loops?rel=023`, `/v6/api/loops`, `/v6/api/resumo`, `/v6/baleia`, `/v6/foruns`, `/v6/servidores`, `/v6/backup` — todas HTTP 200 após restart. Raiz `/` → 301 → `/v6/`.

## Backups

- Servidor: `painel_cctv_v6.py.bak_pre_loops_home_20260815` (mesmo diretório do app).
- Nginx: `painel.conf.bak_pre_redirect_raiz_20260815`.
- Cópia local de trabalho: `ZCodeProject/painel_v6_reforma/painel_cctv_v6_SERVIDOR_20260815.py`.

## O que falta / próximos passos

- **Miguel:** abrir http://43.156.151.165/ (cai na Home V6) e homologar visualmente a página Loops e a nova Home; os relatórios Telegram chegam a cada 30min — avisar se quiser outro recorte/cadência.
- Painel v5 e estáticos `/painel/` continuam acessíveis; aposentar só com ordem.
- Cadência exibida depende do rsync `7,37` (atraso estrutural de até ~30min nos consolidados da Laura — aceitável, mas anotado).

## O que preciso de você (Miguel)

Homologação visual e ok na cadência/recorte do relatório Telegram. Nada bloqueante.

## Adendo (~12:55 BRT) — endereço do painel no Telegram

Pedido do Miguel: toda mensagem do relatório 30/30min lembra o endereço do
CCTV. A segunda linha da mensagem passou a ser `📺 Painel: http://43.156.151.165/v6/`.
Enviado e confirmado no Telegram às 12:55.


## Adendo 2 (~13:35 BRT) — Telegram humanizado, telemetria modernizada e críticos resolvidos

**Novas ordens do Miguel (15/08 ~13:00-13:10):**
1. Crítico no relatório NUNCA vem "como se não fosse nada": o agente **age primeiro** e reporta com o que foi feito, se resolveu e se o Miguel precisa fazer algo.
2. Ponte Cafezinho/Telegram fica **exclusiva** do relatório humanizado do CCTV + conversa. As mensagens técnicas da Vigília ("ronda 240") foram **abolicidas** (prompt da automação `automation-647b2f13` atualizado — Telegram removido do escopo dela) e os resumos rotineiros da faxina de taxonomia também (só anomalia grave).
3. Bug colateral descoberto e corrigido: a automação da Vigília tinha `thought_level=''` no `tasks-index.sqlite`, o que **derrubava o CronList inteiro** (erro de validação). Fix: UPDATE para 'max' + backup `tasks-index.sqlite.bak_pre_thought_fix2_20260815`.

**Telemetria — checagem e modernização:**
- O monitor de chaves LLM (`/root/scripts/monitor_chaves_api.py`, Tencent) estava **morto desde 01/07** (sem cron) — o painel mostrava latências de 45 dias atrás sem sinalizar. Reinstalado cron `*/15` (backup `crontab.bak_pre_monitor_chaves_20260815`).
- **GLM (Z.ai) entrou no monitoramento** — teste via endpoint de quota (GET, 0 tokens); chave `ZHIPU_CODING_API_KEY` espelhada no cofre do servidor (Regra Nº 4, backup `.bak_pre_glm_key_20260815`). 1ª coleta: GLM OK 196ms.
- Painel: parser de métricas Prometheus agnóstico à ordem dos labels + notação científica (bug: frescor nunca aparecia); coluna "último check" na tabela de LLMs; estado "falha no teste" real (Kimi API suspensa por saldo, Gemini sem crédito, Mistral 401 — visíveis agora).
- Página Servidores modernizada: sai Alibaba Beijing (inativo desde a override de topologia 11/08), entram Cafezinho News (espelho) e ServerDo WP (origem).

**Críticos da fila Loop Miguel — agidos e fechados (protocolo novo em ação):**
- **Regex V3 amplo** (ticket CRÍTICO): rollback já aplicado pelo Codex ~12:35; ZCode verificou o runtime vivo, rodou os testes obrigatórios (5 frases-meta removidas + 2 contraexemplos jornalísticos intactos, 7/7) e auditou a janela 08:24→12:35: 15 drafts, **zero remoções silenciosas**. Ticket FECHADO com `ref:` exato.
- **Post 265928 com cat residual 20699**: post já limpo (só Política); varredura sistêmica prova **zero** posts V4 com 20699 (caso pontual). Origem identificada: válvula de excesso do agendador V6 (Claude) — conflito §119/§120 × regra 13/08 registrado para decisão editorial. Ticket FECHADO com evidência.


## Adendo 3 (16/08 ~09:45 BRT) — fix Ceará Digital + "última matéria" nos temáticos

- **Bug reportado pelo Miguel:** Ceará Digital constava "falha" na Central dos Temáticos. Causa: URL configurada era `https://www.cearadigital.news` (domínio inexistente). Canônico no Cérebro (`CEREBRO_INDEX_CEARA.md`): `https://ceara.digital` (Vercel projeto `cicero`). Corrigido na config TEMATICOS do painel.
- **Pedido novo do Miguel:** cada card da Central mostra a **última matéria publicada** com data + selo de frescor (hoje/ontem = 🟢, 2-3 dias = 🟡, 4+ = 🔴). Implementado em `_ultima_materia_tematico()` — data do slug `YYYYMMDD` na homepage (fallback RSS pubDate), cache 30min. Precisão de hora não existe nos sites (meta `datePublished` é só dia) — frescor é por dia.
- **Deploy:** backup `painel_cctv_v6.py.bak_pre_ceara_url_ultima_materia_20260816`; validado ao vivo: 7/7 online, 6 com matéria hoje, 1 ontem. Ceará: ● online 200/30ms, última 16/08 hoje.

---

## ADENDO 17/08 ~01:40 — FREIO DE CUSTOS: relatório CCTV de 30/30min → 8/8h (ordem do Miguel)

O Miguel mandou puxar o freio dos custos: a automação do relatório CCTV
(`automation-e3465bb3`, a que manda o resumo humanizado ao Telegram) passou de
**30/30min para 8/8h** (cron `0 * * * *` + interval 8h; disparos 09:00 / 17:00 / 01:00
BRT). Prompt atualizado (título "CCTV 8/8h…", ronda 8/8h, janela da YT-PATRULHA ~8h)
e as menções "relatório CCTV 30/30min" nos prompts da Caçadora, Faxina e Vigília
corrigidas para 8/8h (REPLACE no tasks-index.sqlite). **Impacto:** alertas críticos
agora aparecem no Telegram em até ~8h (a patrulha da Caçadora continua horária e a
Vigília segue de 30/30min registrando no Cérebro — sem Telegram). Sem rollback
registrado (mudança via CronUpdate, reversível com interval 30min).

---

## ADENDO 18/08 ~01:50 — título do relatório corrigido p/ cadência real (ordem do Miguel)

O Miguel apontou: o resumo CCTV chegava com título "resumo 30min" (defasado da
cadência nova). Fix: `~/bin/cctv_relatorio_30min.py` agora gera título DINÂMICO
pela hora real — "🟢 CCTV · resumo (1/1h)" de dia e "resumo noturno (4/4h)" nas
rondas das 22h/02h/06h (helper `_rotulo_cadencia()`, docstring atualizada). Prompt
da automação CCTV e as menções "CCTV 8/8h" nas 3 automações-irmãs alinhados p/
1/1h (REPLACE no tasks-index.sqlite). Regra: o título do relatório sempre reflete
a cadência vigente do cron.

---

## ADENDO 18/08 ~17:50 — SKIP LOOP LAURA (ordem do Miguel)

Ordem do Miguel (18/08 ~17:40): "pode dar o skip no loop enquanto o pc laura zcode
laura loop laura estiver operacional. se eles caíram aí voce volta a trabalhar".
Implementado: (1) `cctv_relatorio_30min.py` agora OMITE a linha da Laura quando o
consolidado dela tem <180min (operacional; o loop oscila entre 30-75min e vértices
ativos atrasam o consolidado sem queda — 120min gerava falso "caído"); só reporta
"🔴 Laura: consolidado com >3h de atraso" ou "sem dados (API)". Backup
`.bak_pre_skip_laura_20260818`. (2) Prompt da automação CCTV ganhou a regra SKIP
LOOP LAURA: pular/investigar/comentar só se a linha 🔴 aparecer — aí diagnostica,
pinga os inboxes do loop e reporta. Economia de tokens + menos ruído no Telegram.
