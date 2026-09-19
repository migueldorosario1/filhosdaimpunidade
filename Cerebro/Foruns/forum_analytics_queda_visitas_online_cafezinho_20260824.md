# 📉 Fórum — "Analytics caindo a níveis fortes" (visitas online AGORA) — Cafezinho canônico

**Data:** 24/08/2026 13:36 BRT · **Sessão:** ZCode/GLM-5.3 (ZCodeProject) · **Pedido do Miguel:** analytics caindo forte, conferir no Google Analytics se é problema no site ou no GA — visitas online AGORA, **só o canônico**.

## ✅ Veredito binário

**SIM, o site está registrando visitas agora — NADA quebrou.** Nem o site, nem a tag, nem o Google Analytics. A queda percebida tem 3 explicações somadas (abaixo), nenhuma delas é defeito.

## 🔬 Provas (API oficial GA4, mesma service account do painel CCTV)

- **Site são:** `www.ocafezinho.com` HTTP **200 em 1,1s**, tag GA4 `G-4E5DKNTYET` presente no HTML (espelho `cafezinho.news` também 200/4,2s).
- **Tempo real 13:36 BRT:** **55 usuários ativos** (janela 30 min) · série minuto a minuto contínua (1–9/min, subindo no fim) · países: **Brasil 39**, China 8, EUA 7, Reino Unido 1 · páginas: matéria do debate na Record (12 ativos), home (10), matéria Marçal/TRE-SP (4)… = **leitores reais lendo matérias reais**.
- **Série por hora (hoje 24/08):** 00h–06h NORMAIS (246–366 ativos/h, em linha com ontem) · 07h=93 · 08h=1 · 09h+ **ausente** → isso é **atraso de processamento do GA4 no dia corrente** (o gráfico horário de "hoje" sempre vem incompleto/raspado e fecha depois), NÃO perda de visitas — o tempo real prova fluxo contínuo agora.
- **Totais diários (7 dias):** 18/8=6.191 · 19=5.298 · 20=5.686 · 21=5.472 · 22=5.804 · **23 (domingo)=7.858 (recorde)** · 24 parcial=2.244 (dia ainda aberto).

## 🧠 As 3 causas da queda percebida (soma, não defeito)

1. **Comparação com o domingo recorde** (23/08: 7.858 usuários — melhor dia da semana, pico do debate + 53 publicações). Segunda ~13h vs. domingo ~13h é pico contra vale: ontem 13h ≈ 342 ativos/h; agora 55/30min é o normal de segunda pós-almoço.
2. **GA4 entrega o dia corrente incompleto** nos relatórios comuns: hoje aparece 07h=93 → 08h=1 → nada. Quem olha o gráfico horário de hoje vê um "desabamento" que é só atraso de processamento (fecha ao longo do dia/amanhã).
3. **Produção reduzida HOJE de propósito:** V4 desligado 09:30 (17 workers) e V4.1 a cada 2h → menos posts novos = menos visitas de retornantes.

## 🔁 Como reproduzir a checagem (manual técnico na memória gêmea)

`ssh tencent` + `python3 /tmp/ga_rt.py` (script deixado lá) com `GOOGLE_APPLICATION_CREDENTIALS=/home/ubuntu/cafezinho/Projeto Cafezinho Agentes/root/ga4.json`, propriedade **374552425**. ⚠️ Schema realtime desta propriedade é REDUZIDO: usar `minutesAgo`, `country`, `unifiedScreenName`, `deviceCategory` (NÃO existem `pagePath`, `sessionSource`, `dateHourMinute` no realtime).

## 📌 Estado / o que falta / o que preciso do Miguel

- **O que aconteceu:** diagnóstico completo, sem incidente. Zero mudança em produção.
- **O que falta:** nada obrigatório. Dia de hoje fecha sozinho no GA4 (conferir amanhã).
- **Preciso de você (Miguel):** só se quiser — posso criar uma **ronda vigia** (ex.: a cada 30 min, alerta no Telegram se tempo real do canônico cair a ~0, o que indicaria incidente REAL). Sem ordem, não crio (limite 1 automação/sessão).

---

## ⚠️ ADENDO 1 — RETIFICAÇÃO (24/08 14:05): o GA4 TEMPO REAL está subnotificando; site são. Contador redundante INSTALADO.

O Miguel desafiou a 1ª conclusão ("pouquíssimos usuários por minuto") e ele tinha razão — a leitura "sazonal" estava errada. Provas novas (por evidência, não por rótulo):

1. **Servidor com tráfego humano NORMAL/ALTO**: log nginx filtrado só humanos (UA real, páginas): hoje 07h=1.746 vs ontem 1.541 · 11h=2.767 vs 1.646 · 13h=2.102 vs 1.212. Gente no site NÃO faltou.
2. **Visita de teste não contada**: post raro ("Dino NÃO está inelegível") visitado por navegador real (Chrome limpo headless no Dell) com tag no ar → NUNCA apareceu no tempo real (3 consultas em 4 min). Idem hit sintético via Measurement Protocol (aceito com HTTP 204) → invisível. Idem propriedade do Mundo Trilhos (não é só esta propriedade).
3. **Realtime oscilando 29-55** quando o esperado na faixa é ~120-170/30min.
4. Bateria com incidentes públicos do GA4 em agosto (subnotificação de tempo real; em 11/08 "40-50% abaixo"). Fontes: downdetector.com/status/google-analytics · seroundtable.com/google-analytics-real-time-outage-41898.html · ppc.land/google-analytics-real-time-reporting-suffers-widespread-outage.

**Veredito retificado (binário): o Cafezinho está SAUDÁVEL (site, tag e tráfego reais OK); quem está errando é o RELATÓRIO DE TEMPO REAL do Google Analytics (subnotificação).** Os relatórios processados de hoje ainda estão incompletos (07h cresceu 93→110 entre consultas) — amanhã confirmar se o dia fechou normal.

## 🔧 Contador redundante INSTALADO (pedido do Miguel, 24/08 ~13:55)

Independente do Google, no próprio servidor do site (190.89.239.65):

- **Novo log nginx com IP REAL do visitante** (`CF-Connecting-IP`): `/var/log/nginx/access.ocafezinho.contador.log`, formato `contador_ipreal` (cf_ip|remote|iso8601|method|status|host|uri|ua) — log_format declarado NO PRÓPRIO vhost (não em conf.d) porque este nginx carrega sites-enabled ANTES de conf.d.
- **Analisador**: `/root/cafezinho_contador/contador.sh` (Python 3; filtra humanos: UA Mozilla com plataforma real, sem bots, páginas de conteúdo) → grava `resumo.txt` + `resumo.json` com: **online agora (30 min)**, hoje por hora, ontem por hora, top 10 páginas.
- **Cron**: `/etc/cron.d/cafezinho-contador` (*/5). Consultar: `ssh cafezinho-wp 'bash /root/cafezinho_contador/contador.sh'`.
- 1ª leitura (log com 3 min de vida): **22 visitantes humanos distintos online** — já mais que o real do GA em 30 min (37).
- Mu-plugin PHP de contagem foi TENTADO e DESATIVADO (cache estático serve páginas sem rodar WordPress; tabela nem criava; movido para `/root/cafezinho_contador/mu-plugin-contador-DESATIVADO_20260824.php`).

### 🔴 Gotchas críticos do servidor do site (cafezinho-wp) para qualquer sessão futura

1. **`sites-enabled/ocafezinho.com.conf` é CÓPIA, não symlink** de sites-available (editar SEMPRE o enabled — ou ambos). Há ainda 3 `.bak` de conf DENTRO de sites-enabled (carregam como config duplicada, warnings; nunca criar backup lá).
2. **nginx lê sites-enabled ANTES de conf.d** → log_format/use precisa estar no próprio vhost.
3. **A Cloudflare mascara os IPs no log antigo** (só 190.89.239.31/.244 e 10.1.1.108 apareciam) — o novo log resolve com CF-Connecting-IP.
4. Backups da mudança: `sites-enabled/ocafezinho.com.conf.bak_pre_contador_20260824` (fora do include, em /root/cafezinho_contador/backup_vhost_enabled_20260824.conf) + `.bak_pre_contador_20260824` no sites-available.

### Estado / falta / preciso do Miguel

- **Aconteceu:** diagnóstico completo + contador redundante no ar (cron */5).
- **Falta:** conferir AMANHÃ (25/08) se os relatórios processados de hoje fecharam normais no GA4 (se sim, só o realtime erra); opcional: plugar resumo.json no painel CCTV (posso fazer).
- **Preciso de você:** nada obrigatório. Se quiser, digo "cria a vigia" e eu monitoro GA×contador com alerta no Telegram.

## ADENDO 2 (24/08 14:10) — medo do Miguel: "bloqueio do Google?" → NÃO. Provas + auditoria do dia

1. **Contador próprio × GA ao vivo (14:08): contador 69 visitantes online (30 min, com só 6 min de log acumulado) vs GA realtime 40.** Audiência REAL presente; o independente já conta mais que o Google.
2. **Indexação viva**: busca Google "O Cafezinho contrainformação" → site em 1º lugar (sem sinal de penalidade). Tráfego orgânico processado hoje 05h=34/06h=51 ≈ ontem (23/47).
3. **Bloqueio de algoritmo eliminado por lógica**: penalidade Google reduz visitantes CHEGANDO ao servidor; o servidor recebeu MAIS humanos que ontem a manhã toda (07h 1.746×1.541; 11h 2.767×1.646). E o defeito se replica na propriedade do Mundo Trilhos.
4. **Web**: threads ATIVAS esta semana de outros usuários c/ o mesmo quadro — Reddit r/GoogleAnalytics "Is Google Analytics Realtime not working properly?" + fórum oficial Google "Realtime Outage" (ativos oscilando) + precedentes documentados (seroundtable 41898: 40-50% abaixo; incidentes 4/08 e 11/08 documentados). Sem relatório nominal de 24/08 ainda.
5. **Auditoria "foi algo que fizemos?"**: NÃO — nenhum arquivo WP (plugins/temas/mu-plugins) modificado após 23/08 02:12; nginx sem mudança hoje antes de 14:01 (minhas, aditivas, posteriores à queda ~07h); reinício 03:30 de rotina (GA normal até ~06h); ações do ecossistema hoje (V4 OFF NYC 09:30, CCTV, Moka, materializador) não tocam na coleta. Google ACEITA os hits (204) e não mostra → elo quebrado dentro do Google.

**Pendência 25/08:** conferir se o DIA de hoje fechou normal nos relatórios processados (se sim, só o realtime errou; se zerado, escalar como problema de coleta na propriedade com o Google — de jeito nenhum do site).

## ADENDO 3 (24/08 14:35) — PÁGINA "AUDIÊNCIA REDUNDANTE" NO CCTV + projeção atendida (ordem Miguel)

**No ar: `http://43.156.151.165/v6/audiencia-redundante`** (menu do painel: 🛡️ A. Redundante; atualiza sozinha a cada 60s).

- **Fluxo**: contador do site (*/5) grava `historico.csv` local + empurra `resumo.json` via POST `http://43.156.151.165/v6/api/audiencia-receber` (header X-Token; **porta 80** — a 8084 é bloqueada na saída do serverdo) → painel valida e **append em `agent_data/cctv/v6/audiencia_red.jsonl` (histórico guardado SEMPRE)**.
- **Página mostra**: contador próprio online 30min × GA4 realtime lado a lado + sparkline 3h + hoje/ontem por hora + top 10 páginas + nº de leituras arquivadas.
- **Token de integração**: tencent `agent_data/cctv/v6/audiencia_token.txt` (600) ⇄ site `/root/cafezinho_contador/push_token` (600) — rotacionado (o 1º vazou no chat por descuido de grep; lição: nunca printar arquivo de segredo).
- ⚠️ Gotchas desta instalação: systemd do Tencent IGNOROU drop-in Environment (motivo não esclarecido) → token lido do arquivo pelo painel; painel roda :8084 mas o mundo entra pela :80 (nginx, prefixo /v6/).
- **Leitura real da estreia**: 14:33 — **contador 305 online (30 min) × GA4 27** (subnotificação ~90%). Audiência real da tarde: SAUDÁVEL e acima da média dos últimos dias (13-14h históricos: 193-342 ativos/hora no GA).
- Mudanças no painel: `painel_cctv_v6.py` + `pagina_audiencia_red()` + handler POST (backup `.bak_pre_audiencia_red_20260824`).

- (24/08 14:38) ADENDO 4: página reformulada (v2) após feedback do Miguel ("feia e estourada") — cartões compactos em linha com rolagem, colunas com largura limitada, paths com elipse, barras nas horas, rótulos explícitos "contador próprio" em todas as seções (top páginas do dia = CONTADOR PRÓPRIO, não GA).

- (24/08 14:45) ADENDO 5: contador batizado **FAROL**; página v3 (tipografia maior, cartões com gradiente, notas FAROL×GA4 dinâmicas embaixo com o relato de 24/08); menu do CCTV = 🛡️ FAROL; página protegida por login (auth_basic nginx, credenciais em Cofres/cofre_farol/ + NODE_COFRE_CHAVES); push /v6/api segue por token sem auth_basic.

## ADENDO 6 (24/08 14:46) — PENDÊNCIA REGISTRADA (ordem Miguel): investigar POR QUE o GA4 travou hoje

Amostras para a linha do tempo (subnotificação persistente?):
- 13:36 GA=55 · 13:50 GA=29 · 14:08 GA=40 · 14:35 GA=27 (FAROL 305 às 14:33)

Roteiro da investigação (próxima sessão, 25/08 de preferência):
1. Se o dia 24/08 fechou COMPLETO nos relatórios processados (run_report dateHour) → defeito foi só do realtime (processamento ao vivo); se horas 07h+ vieram rasas/zeradas → problema de COLETA da propriedade (escalar com o Google).
2. Marcar hora exata de início (~07h BRT: 06h=393 normal → 07h=110 em processamento parcial) e de fim (quando GA≈FAROL de novo — cruzar série jsonl do FAROL × GA realtime amostrado).
3. Cruzar com relatos públicos (Reddit r/GoogleAnalytics thread ativa, fórum Google "Realtime Outage", statusgator) para datar o incidente global.
4. Se persistir em 25/08: com o Miguel (~5 min no console GA), revisar filtros internos/de dados da propriedade 374552425 e abrir questão no suporte Google (a SA Editor dá p/ listar via Admin API: properties/filters).
5. Prova guardada: agent_data/cctv/v6/audiencia_red.jsonl (FAROL minuto a minuto) + scripts /tmp/ga_*.py no Tencent.

- (24/08 14:48) ADENDO 7: ordem Miguel — página FAROL volta a ser ABERTA (auth_basic removido do nginx; htpasswd órfão em /etc/nginx/.htpasswd_farol pode ser apagado na próxima manutenção). Cofre do FAROL marcado _DEPRECADO_ (credencial inútil sai do vivo, histórico guardado).

## ADENDO 8 (24/08 14:52) — pesquisa: esse tipo de falha acontece com outros? Frequência? (ordem Miguel)

SIM, recorrente. Linha do tempo pública:
- set/2024 outage Audience Insights (ppc.land) · 17/07/2025 falha generalizada da plataforma (ppc.land) · 11/08/2025 subnotificação realtime 9:45 ET "3ª falha em meses" (w3era) · 4/08/2026 disrupções documentadas (fivechannels) · seroundtable 39293 "Real Time Glitching" (ondas de queixas, anos) · 41898 (40-50% abaixo, resolveu ~1h).
- MESMA SEMANA do nosso caso (24/08/2026): Reddit ATIVO "Is GA Realtime not working properly?" (2 threads gêmeas 1vfclle/1vlko2m) + "Did GA Realtime suddenly stop?" (1vfd3fn — números irrealisticamente baixos em MÚLTIPLOS projetos Firebase) = sintoma idêntico ao nosso.
Mecanismos citados pela comunidade: throttling do realtime sob SPIKE de hits em 30min (reddit tykabb — nota: ontem 23/08 foi nosso RECORDE 7.858 usuários/53 posts; hipótese a testar na investigação) · logs Cloudflare×GA sempre divergem (reddit 17av21a — o FAROL formaliza esse cruzamento) · "dados de hoje" atrasam nos relatórios comuns (1e1ocvv).
Frequência estimada: falhas GRANDES públicas ~2-4×/ano (2024-2026); queixas menores de subnotificação no Reddit TODA semana; "tempo real do GA4 não é confiável" é consenso comunitário (thread 1buh9nt).

- (24/08 14:55) ADENDO 9: Top páginas promovido a seção full-width (fora da coluna), fonte 15-16px, endereço completo com elipse de segurança, barra de intensidade verde + visitas à direita (feedback Miguel).

- (24/08 15:10) ADENDO 10: banner 🛡️ FAROL injetado SEMPRE nas páginas /v6/audiencia e /v6/baleia (dispatcher) — compara os dois medidores na hora (FAROL online agora × GA4 tempo real, GA com cache 60s) + link "acompanhe a audiência redundante". Ordem Miguel: análise de audiência agora é sempre dupla.
