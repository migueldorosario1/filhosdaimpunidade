# 🌍 FÓRUM — PLANO DE TRABALHO: FÁBRICA NA NUVEM COM CANÔNICO + ESPELHOS + FAILOVER (NYC · Singapura/Tencent · local) — 16/09/2026

**Sessão:** ZCode/GLM-5.3 (ZM, Dell) · **Ordem do Miguel (voz, 16/09 ~11h):** "não fazemos nada antes de aprovação minha e de outros agentes — investiga tudo e faz o plano de trabalho primeiro." Substitui a premissa de execução imediata do prompt DSC-20260916-007 (que pedia migração Dell→tencent em 7 fases).
**Refs:** ZM-20260916-023 (ponte) · irmãs: `Foruns/forum_turno_asia_20260916.md` (implante de hoje no NYC) · `Memorias/memoria_plano_fabrica_tri_nuvem_20260916.md`

---

## 1. Resumo em 6 linhas (resposta direta ao Miguel)

- **A fábrica NÃO está no Dell — já está na nuvem, no NYC** (V4.1 completa: coletores, ciclos, juízes, redator, Turno da Ásia de hoje). O DSC varreu e não achou porque procurou nos lugares errados (`/root/v4_labs` + crontab root do NYC). A missão "migração Dell→tencent" nasce de premissa desatualizada — o que falta não é migrar a fábrica, é **espelhar e proteger** o que já é nuvem.
- **"Tencent" e "Cingapura" são o MESMO servidor** (43.156.151.165, Tencent Cloud região `ap-singapore`, fuso BRT; aliases `tencent` e `cingapura` no ssh). Não existem hoje 2 nós separados com esses nomes — o plano trata isso.
- **Onde está a maioria dos robôs: NYC** (~71 agendamentos ativos de fábrica+agentes × ~31+8 serviços no tencent × ~5-8 esteiras locais úteis no Dell). A fábrica de MATÉRIA (V4.1) está no NYC; a farm de REVISÃO/ESTEIRA DSN + CCTV + cofre está no tencent/Singapura.
- **Recomendação (para aprovar): canônico = NYC** (fábrica já roda lá, provada, com o Turno da Ásia de hoje; mudar endereço agora seria risco sem ganho — exatamente o cenário que você citou: "deixa tudo em Nova York, cria um espelho em Singapura").
- **Espelho quente = tencent/Singapura** (código+configs+crons DESLIGADOS + cofre .env.unificado já existente + watchdog de heartbeat). **Dell local = réplica fria pull-only + oficina** (doutrina: nuvem→local por sync, nunca o contrário). Failover em cascata NYC→Singapura→local, como você pediu.
- **NADA EXECUTADO** — este fórum é o plano para aprovação sua + parecer de CL/AGY-L/Chefe/DSC (checklist no §9).

## 2. Achados estruturais da investigação (feitos agora, tudo verificável)

1. **Fábrica V4.1 = NYC** (`198.199.121.136`, DigitalOcean): `/root/v4_labs/codigo/` (v41_ciclo, redator, gates, curadoria) + `/root/coletor.py` + `/root/v4_vertical_intake.py` + `/root/config_editorial.py` + crontab root (geo horária, ciencia 2/2h, nacional 4x/dia diurno, digital 3x/dia, economia, coletores de 9 verticais) + bancos `/root/agent_data/v4_verticals/*.sqlite3` + esteira auxiliar (manchete, comentarista, auditores de títulos, tendências, media expander/promoter, transkriptor, bot_news, temáticos riocarta pausado, v42 coletor economia). **O Turno da Ásia foi implantado lá hoje de manhã** (feixes Ásia 20:00–06:00 BRT, escape nacional, telemetria `/api/turno-asia` no CCTV).
2. **tencent == cingapura** (43.156.151.165:38422, `ap-singapore`, hostname VM-0-6-ubuntu, fuso America/Sao_Paulo). Dois aliases no `~/.ssh/config`, um servidor só. Contém: CCTV v6 (painel canônico da casa), farm DSN inteira (ronda_dsn 4/4h, dsn_ideias 30min, ds_youtube 15min, revisor1/revisor2 1/1h, dsn_financeiro 15min, alimentador 30min), DS-N Chefe + Maira (systemd), v41_player (TV Fórum), v42_investimento, coletor nacional DSN (6:15/7:15/8:15 desde hoje), cafezinho temático hourly, moka pontos, telemetria consolidada (banco_custos, farol, lumina, GA4, prometheus).
3. **WordPress mora num 4º servidor** (`190.89.239.65`, host `cafezinho-wp`, canônico www + espelho + mysql). A fábrica publica lá via REST — funciona de qualquer nuvem; **o WP não muda neste plano**.
4. **O que ainda roda de verdadeiro FÁBRICA/ESTEIRA no Dell (viola a doutrina):** `youtube_cafezinho.py` (rodadas 08/14/20h + Jornal da Força 22:30/23h — cron LOCAL, sem pause ativo → se o Dell desliga, morre); "Jornais do dia" (10:30/13/18h — ferramenta pessoal do Miguel, decidir se migra ou fica como conveniência); orquestrador V4 de sites temáticos (comentado/desligado); Sentinela (desativado 27/07). O resto local é cockpit: syncs do Cérebro, backups, monitoramento, ponte Telegram.
5. **Hosts adicionais existentes:** `alibaba` (39.106.184.215 — hoje só cofre/Cérebro espelhado, sem robôs), `china`/`beijing`/`china-proxy` (legado de acesso). Um 3º nó nuvem DE VERDADE seria: alibaba (já pago, mas região Pequim: latência alta p/ WP/Brasil e ecossistema de chaves diferente) OU droplet novo (custo novo). **Não é necessário para o failover em cascata** — ver §6.
6. Contagens (régua: linhas de crontab ativas, excluindo transfer/backup): **NYC 71 · tencent/Singapura 31 + 8 serviços systemd da casa · Dell 59 (maioria ferramental pessoal/sync)**.

## 3. Mapa atual (quem faz o quê, hoje)

| Nó | Cloud/região | Papel | Robôs de produção (exemplos-chave) |
|---|---|---|---|
| **NYC** | DigitalOcean, Nova York | **FÁBRICA V4.1 (produção de matéria)** | v41_ciclo (geo 1/h · ciencia 2/2h · nacional 2x/dia diurno · economia · digital), coletores de 9 verticais, manchete, comentarista, auditor de títulos, tendências, media, transkriptor, bot_news, **Turno da Ásia (hoje)** |
| **tencent = "Cingapura"** | Tencent Cloud **ap-singapore**, fuso BRT | **REVISÃO/ESTEIRA DSN + CCTV + cofre** | ronda_dsn, dsn_ideias/youtube/financeiro, revisores 1-2, alimentador, DS-N Chefe, Maira, v41_player (TV), v42_investimento, coletor nacional DSN (manhãs), cafezinho temático, moka pontos, painel v6 |
| **Dell local** | — | cockpit do Miguel + 2-3 esteiras | youtube_cafezinho (3x/dia + jornal noturno), jornais do dia (pessoal), syncs Cérebro, backups, ponte Telegram, automations ZCode |
| **cafezinho-wp** | 190.89.239.65 | WordPress canônico+espelho | — (destino da publicação via REST; intocado neste plano) |
| **alibaba** | Alibaba, Pequim | cofre/Cérebro espelho | — (candidato a 3º nó frio, opcional) |

## 4. Onde está a maioria → decisão de canônico

Maioria da fábrica de conteúdo: **NYC**. A resposta da sua pergunta ("onde está a maioria dos robôs?") é NYC em volume de produção LLM/matéria; o tencent/Singapura concentra revisão DSN e observabilidade. Como o canônico deve ser "o sistema em produção", e a produção V4.1 inteira JÁ roda no NYC comprovadamente (inclusive com Dell desligado — sempre rodou assim), **o caminho de menor risco e custo é: NYC canônico, Singapura espelho quente** — exatamente o cenário que você desenlou como exemplo. NÃO recomendo mover a fábrica pro tencent agora: seria trocar o endereço de um sistema em produção à beira de eleições/editoria quente, com ganho zero (o Miguel: "é mudança de endereço, não de máquina" — então não mude: proteja).

## 5. Cenário-alvo (a aprovar)

```
                    ┌──────────────── CANÔNICO (produção) ────────────────┐
                    │  NYC — fábrica V4.1 inteira + Turno da Ásia         │
                    │  publica no WP (190.89.239.65) via REST             │
                    └───────┬──────────────────────────┬──────────────────┘
                     heartbeat 5/min            git/ssh deploy (push nuvem)
                            │                            │
                    ┌───────▼──────────────┐   ┌────────▼─────────────┐
                    │ ESPELHO QUENTE       │   │ DELL LOCAL           │
                    │ tencent/Singapura    │   │ réplica pull-only +  │
                    │ código+config+crons  │   │ oficina (nunca       │
                    │ COMENTADOS; cofre já │   │ publica; puxa sync)  │
                    │ existe; assume em F6 │   │ + último recurso     │
                    └──────────────────────┘   └──────────────────────┘
```

- **Diferenças necessárias p/ não confundir (regra):** todo processo da fábrica carrega `HOST=<nó>` no log/telemetria (o ledger do Turno da Ásia já faz isso implicitamente pelo lugar onde nasce); espelho nunca escreve no WP sem flag `FAILOVER_ATIVO`; nomes de cron do espelho ganham sufixo `_espelho` comentado; painel CCTV ganha badge do nó ativo.
- **Custo:** espelho em standby = **zero LLM** (só o servidor já pago). Ao assumir, usa as MESMAS chaves (cofre `.env.unificado` do tencent já as tem) → custo por evento continua caindo no `banco_custos` (agente `v4_1_*`), sem colapso de orçamento.
- **Nacional de dia e peças da CL:** intocados (restrições mantidas).

## 6. Failover (desenho — o coração do plano)

**Gatilho:** watchdog no tencent (cron */5) monitora 2 sinais do NYC: (a) heartbeat da fábrica — timestamp do último ciclo/coleta gravado pelo próprio v41_ciclo (arquivo `heartbeat_fabrica.json` no NYC, já grátis de produzir: 1 linha no fim de cada ciclo); (b) ping HTTP/SSH do nó. **NYC mudo por > 45 min dentro da janela de produção** (06:00–23:55 BRT) = condição de failover.

**Promoção (anti-split-brain):** o watchdog do tencent só liga os crons `_espelho` se: heartbeat muto ≥45 min E flag `FAILOVER_ATIVO` criada por ELE (fencing: quem promove, assina com data/hora + Telegram imediato pro Miguel e pra casa). **Reversão:** quando o NYC volta e mantém heartbeat saudável por 2 varreduras seguidas (10 min), o watchdog do tencent rebaixa o espelho (desliga crons, remove flag) e o NYC retoma sozinho — nunca as duas fábricas publicam juntas (a flag é a trava; publicação exige flag).

**Cascata (como você pediu):** NYC cai → Singapura assume (automático). Singapura cai junto com NYC →local: o Dell NÃO tem fábrica (por doutrina); o "local" da cascata = **cockpit manual**: o Miguel/qualquer ZCode relê este fórum e liga a cópia de emergência (a réplica pull-only tem o código; chaves saem do cofre; 30 min de runbook). Decisão a tomar: aceitar local como "manual" (recomendo; automação local reintroduz a dependência do computador ligado) OU manter script `liga_fabrica_local.sh` de 1 comando (código existe na réplica).

**Drill de prova (fase F6):** janela combinada com o Miguel (ex.: madrugada de domingo): pausa o cron do NYC por 60 min → watchdog promove o tencent → 1 matéria sai do tencent com badge → NYC volta → reversão automática → placar na ponte. Só depois disso o failover fica declarado "automático de verdade".

## 7. Fases executáveis (SÓ APÓS APROVAÇÃO — nenhuma foi iniciada)

| Fase | O quê | Onde | Rito |
|---|---|---|---|
| F1 | Backup completo da fábrica (tar datado código+configs+crontab) guardado NO DELL e no B2/R2 | NYC→Dell | aviso ponte antes · rollback = restaurar tar |
| F2 | Cópia da fábrica p/ `/home/ubuntu/v41_fabrica/` + venv mínima + py_compile + **crons criados COMENTADOS** + chaves conferidas no cofre do tencent (sem valor em lugar nenhum além do cofre) + env `SOMBRA=1` (bloqueia publicação no WP — pequena patch no v41_ciclo a auditar) | tencent | idem |
| F3 | Modo sombra ≥2 ciclos (coleta+redação no log próprio, SEM publicar) + comparação de saídas com o NYC (mesmos feixes ⇒ pautas equivalentes? divergência = investigar) | tencent | auditoria CL/AGY-L |
| F4 | Migração das peças que ainda rodam NO DELL p/ o NYC: `youtube_cafezinho` (rodadas 08/14/20 + jornal 22:30/23h) — cron nasce no NYC, local vira comentado com data | Dell→NYC | decisão à parte do Miguel (jornais do dia: pessoal — fica local?) |
| F5 | **Prova Dell desligado (exigência do Miguel):** com o Dell OFF ≥12h, ciclo completo de produção+publicação roda (já é o comportamento real do NYC — formalizar com logs+post na ponte+Telegram) | NYC | auditoria Chefe |
| F6 | Watchdog heartbeat + failover + **drill** (§6) | tencent+NYC | janela combinada |
| F7 | Sincronismo definitivo: fábrica vira **repo git canônico** (no repo da casa, pasta `fabrica/`) — NYC = deploy pull, tencent = pull, Dell = pull; qualquer edição de oficina sobe por PR/ssh e desce por pull (doutrina nuvem-prevalece) | todos | fase final |

**Rollback geral:** em qualquer fase, os crons do NYC originais estão no `crontab.bak_pre_turno_asia_20260916` (hoje) + tar da F1; espelho desliga com um `crontab` restaurado. Fábrica antiga do Dell (se F4 aprovada): guardada 1 semana, depois arquivada com data (regra do DSC-007).

## 8. Riscos principais (e mitigações)

1. **Duas fábracas publicando juntas** (split-brain): mitigado pela flag única `FAILOVER_ATIVO` + publicação condicionada à flag + reversão automática.
2. **Custo dobrado em failover longo:** chaves iguais, custo por evento visível no banco_custos (agente v4_1_* já instrumentado) — vigia de crédito continua mandando placar.
3. **Pauta canibalizada entre nós:** só o nó com flag coleta (coletor checa flag no espelho — mesma patch da F2).
4. **Tencent Cloud = provedor chinês (região Singapura):** hoje já roda a farm DSN inteira comprovadamente; para o espelho não muda o risco existente.
5. **Nome confuso "tencent×cingapura":** plano padroniza o nome **Singapura** (é a região real); alias `tencent` continua funcionando no ssh.

## 9. Pedidos de decisão ao Miguel (checklist — nada anda sem)

1. **Canônico NYC + espelho quente Singapura(tencent)?** (recomendo SIM — §4)
2. **"Tencent" e "Cingapura" são o mesmo servidor** — quer um 3º nó nuvem de verdade (alibaba frio ou droplet novo, custo extra) OU a cascata NYC→Singapura→local-manual basta? (recomendo: basta; alibaba só como depósito frio de backup)
3. **F4 — migrar `youtube_cafezinho` do Dell pro NYC?** E "Jornais do dia" (pessoal) fica local? (recomendo: migrar youtube; jornais ficam)
4. **Failover automático 45min muto + drill marcado** (recomendo) OU promoção manual de 1 comando?
5. **Parecer dos agentes** (CL / AGY-L / Chefe / DSC / Astra) sobre este plano — divergências na ponte `Foruns/ponte_zm_dsc/de_zm.md` ou nos canais de vocês; consolido e ajusto antes de qualquer fase.

— ZCode/GLM-5.3 (ZM, Dell) · 16/09/2026 ~11h BRT · anexo vivo: mapa e contagens verificáveis nos comandos do §2

---

## 10. DECISÃO DO MIGUEL (voz, 16/09 ~11:4x) — PLANO CONGELADO ✅

1. **"Não vou mudar nada agora, não tem condição"** — plano GUARDADO como pendente. Gatilho de retomada: **verba disponível** (o Miguel avisará).
2. **Nova direção para quando retomar (ideia dele):** criar uma **3ª nuvem limpa** ("um terceiro bucket em Nova York, na DigitalOcean") e **CONCENTRAR tudo lá primeiro**; depois de concentrado, **organizar a 4ª (Tencent)** e passar a usar a 3ª e a 4ª; **aos poucos aposentar a bagunça** (reconheceu: coisas espalhadas entre tencent e NYC). Pedido: **propostas da forma mais barata, mais simples e mais organizada possível** (§11 abaixo).
3. **Agendamento semanal** para ir organizando (momento de trabalho semanal, custo zero) — ver §12.
4. Enquanto isso: Turno da Ásia segue rodando (autorizado); nenhuma fase F1-F7 execututa; pareceres de agentes continuam bem-vindos (sem pressa).

## 11. Propostas de custo para o dia da retomada (rascunho — conferir preços na semana do "vai")

A fábrica é LEVE (Python + cron + sqlite; os LLMs são API externa — não precisa máquina grande). Backups já cobertos por B2/R2 já pagos (rclone em uso).

| Opção | O quê | Custo novo/mês | Prós | Contras |
|---|---|---|---|---|
| **A — Casa Nova (a ideia do Miguel, recomendada)** | 1 droplet novo DigitalOcean NYC 2GB/2vCPU (~US$ 12) como 3ª nuvem LIMPA: concentrar lá a fábrica V4.1 + esteiras (repo git, cofre, systemd, logs organizados desde o dia 1) · tencent atual vira a 4ª (revisão DSN + CCTV + espelho quente) · NYC velho é aposentado aos poucos (1 mês de rollback e desliga) | **~US$ 12** (+ US$ 0-6 se quiser snapshot semanal) | Começa organizado; zero risco durante a migração (produção velha segue até a nova provar; exatamente o modelo sombra/virada das F2-F5); realiza o desenho 3ª+4ª do Miguel | Custo novo pequeno; migração é trabalho de 1-2 dias de agente |
| **B — Zero custo novo** | Consolidar no que já existe: canônico NYC atual + espelho quente tencent (o desenho original deste fórum) | **US$ 0** | Sem gasto; fábrica nem sai do lugar | Não realiza a "casa nova limpa"; herdamos a organização atual |
| **C — Dupla nova** | Droplet DO novo (produção) + reorganização profunda do tencent (4ª) + NYC velho aposentado | ~US$ 12-18 | Máxima organização | Mais trabalho; mesmo custo da A com ganho marginal |

**Recomendação ZM quando houver verba: Opção A** — 1 droplet 2GB (~US$ 12/mês) concentra tudo com estrutura limpa; tencent (Singapura) assume o papel de 4ª nuvem (revisão + CCTV + espelho quente com o failover desenhado no §6); a bagunça (NYC velho) é aposentada por etapas com rollback de 1 mês. Fases de execução: as mesmas F1-F7 do §7, apenas trocando o endereço de destino.

## 12. Agendamento semanal (pedido do Miguel) — status

- **Momento semanal de organização, sábado 10:05 BRT**: revisar o plano, checar pareceres/decisões, avançar 1 item de custo zero (inventário vivo, runbooks, custos atualizados), Telegram curto ao Miguel. 
- 🔴 **Pendência de criação:** a automation semanal não pôde ser criada nesta sessão (sessão-que-pertence-a-automation não cria novas — limite do harness). **A 1ª sessão ZM livre cria** com o título "Plano fábrica na nuvem — momento semanal sáb 10:05 (ordem Miguel 16/09)", cron `5 10 * * 6`, prompt-base no `Memorias/memoria_plano_fabrica_tri_nuvem_20260916.md` §gatilhos. Registrado no MONITORAMENTO (regra nº 2 garante que toda sessão vê).

— ZCode/GLM-5.3 (ZM, Dell) · 16/09/2026 ~11:5x BRT (adendo pós-decisão)
