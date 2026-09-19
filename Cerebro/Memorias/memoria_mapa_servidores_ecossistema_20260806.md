# 🧠 Memória — Auditoria ao vivo dos servidores do ecossistema (06/08/2026)

> [!CAUTION]
> **FOTOGRAFIA HISTÓRICA, SUPERADA EM PARTE EM 11/08/2026:** funções e estados mudaram depois desta auditoria. Para a lista viva e a relação entre face pública e infraestrutura, consultar primeiro `CEREBRO_NODE_ECOSSISTEMA_CANONICO.md`; em particular, `agente_controlado.py` não integra mais o V4, Tencent voltou a responder e o droplet YouTube virou utilitário.

> **Sessão:** ZCode (Kimi K3), chat direto, workspace ZCodeProject.
> **Pedido:** Miguel — "o que está sendo usado DE FATO em Nova York intensamente e no Alibaba; mapa completo dos servidores".
> **Método:** script read-only `/tmp/auditoria_servidor.sh` via SSH (uptime, free, df, ps top CPU/MEM, crontabs, systemd running, ss -tlnp, docker, last, arquivos recentes /root) + dig/curl/ping. **Nada foi alterado em nenhum servidor.**
> **Fórum (decisões):** `Foruns/forum_mapa_servidores_ecossistema_20260806.md`.

Horário das auditorias: 06/08/2026 ~15:10–15:20 UTC (~12:10–12:20 BRT).

---

## 1. NYC `198.199.121.136` — Cafezinho-failover-vigia ✅ auditado

- Uptime 31 dias; load 0.02/0.17/0.20; RAM 1.9G (829M usada); **disco 48G → 94% (3.1G livre) ⚠️**
- Processos vivos: `agente_controlado.py`, `v4_regional_draft_worker.py`, `bot_mayrag_v3.py`, `cafezinho/portal_cafezinho/augusto_telegram_brain.py`, mariadbd, php-fpm, nginx
- Serviços custom: `augusto-cafezinho.service`, `mayra-cafezinho.service`, mariadb, nginx, php8.3-fpm
- Portas: 22, 80/443 (nginx), 3306 (MariaDB)
- Crons (~30, extraídas na íntegra): remover_no_home 2/2h; auditor_indexacao 06:14; performance :52; fiscal_tokens 08:00; validador_modelos 03:00; autocura determinística 15:17 + resumo 08:00 + semanal sex 14:00; push métricas LLM :07; coletar/gerar custos :07; caetano limpeza 06:00; manchete 2/2h; **comentarista_v4 :07/:37**; **auditor títulos GPT a cada 10min** + relatório :58; SEO noindex 03:07; daemon_indexador */30; verificador indexing :23; pagespeed 09:00; GSC 10:00; GA4 seg 11:00; repetidor_estatal :07 2/2h; **V4 geopolítica :00/:30; V4 ciência :10/:40; V4 nacional :20/:50** (coletor→intake→draft_worker); media_promoter */6h; media_expander 06:47; ceará hourly 09:15
- Últimos logins humanos: 19–22/07 (186.223.171.9)
- Disco (maiores): backups 8.0G, venv 7.7G, agent_data 2.7G, gsn_remote 1.9G, cicero_remote 1.8G, cafezinho 581M, V3 514M; /var/log 985M; mysql 136M

## 2. NYC `159.89.185.209` — Rio-Carta-Agentes ✅ auditado

- Uptime 31 dias; **load 2.32**; RAM 961M (438M); **disco 24G → 100% (0 livre) 🚨**
- Anomalias: `rsyslogd` 44.6% CPU, `check-new-release` 33% CPU (travado — provável efeito disco cheio)
- Vivo: `cicero_admin.py` (venv_admin_recovered, porta 5000), caddy (80), node_exporter
- Crons: **Cícero/Ceará rotativo :00/:30** (janela 0-2h e 9-23h) + :00 3-8h; publicador Ceará :23; indexador Google :30; **GSN collect :12**; GSN publish :37 (1/9/17h); **ferroviário 2/2h** + retry 04:00; **turismo :37 (9/13/17/21h)**; prometheus */5
- Disco (maiores): cicero_remote 4.1G, riocarta_remote 3.8G, gsn_remote 1.8G, agentes 654M, votacao_candidato_munzona_2022.zip 553M, /var/log 1.4G
- Último login humano: 19/05

## 3. NYC `142.93.48.252` — gsn-youtube-nyc-01 ✅ auditado

- Uptime 31 dias; load 0.00; RAM 961M (362M); disco 5G/24G (22%)
- **Única cron:** prometheus push */5. Zero agentes, zero portas além de SSH. OCIOSO de fato.

## 4. NYC `159.65.177.60` — cafezinho-news-espelho ✅ auditado

- Uptime 31 dias; load 0.08; RAM 3.8G (848M); disco 16G/77G (20%)
- Stack: nginx + php8.3-fpm + mariadb + fail2ban
- **Única cron:** `17 * * * * /root/sync_from_cafezinho.sh` (sentinela Claude 03/07)
- HTTP: cafezinho.news responde **401** (protegido por auth no nginx)
- Anomalia benigna: `check-new-release` ~96% CPU (também presente; bug Ubuntu comum)

## 5. NYC `174.138.36.31` — riocarta-wordpress (legacy) ⛔

- SSH timeout (2 tentativas, 10s e 20s); **ping 100% perda**. Droplet desligado ou destruído. Se consta no painel DO, está cobrando à toa.

## 6. Tencent Singapura `43.156.151.165:38422` — VM-0-6-ubuntu ✅ auditado

- **Uptime 16 semanas**; load 0.01; RAM 7.5G (1.5G); disco 72G/118G (64%)
- Vivo: `V3/robo_banco_ouro_midia_v3.py` (MASTER do banco ouro), `painel_midia_ouro.py` (serviço `midia-ouro-panel`), `painel_cctv_v6.py` + `painel_editorial.py` (cctv-v5/v6, painel-editorial), **Moka `pontos_api` uvicorn :8420** + `vigia_saldos` 09:00 + `descadastro` */15, `gerar_pulse_cafezinho` */10, cafezinho_hourly 09:45, nginx, openclaw-gateway, PM2, fail2ban, agentes qcloud (barad/YunJing)
- Portas: 80, 443, 8080, 8082/8083/8084 (painéis python), 8091, 8420 (Moka), 9100, 18789-18792, 38422 (sshd)
- Homes: lighthouse, migueldorosario, ubuntu

## 7. Beijing `82.156.167.218` — "Alfândega" GSN ⛔

- SSH timeout (45s e 30s); **ping 100% perda**. Função GSN já roda no Rio-Carta-Agentes (crons gsn_* lá). Sem sinal de vida.

## 8. Alibaba Beijing `39.106.184.215` ⛔ MORTO

- SSH timeout ×2 (15s, 20s); **ping 100% perda**. Cérebro já marcava LEGACY em 29/07. **Verificar console/fatura Alibaba: VM solta (não desligada) continua cobrando.**

## 9. ServerDo.in `190.89.239.65:51439` — us65.serverdo.in ✅ auditado

- **Uptime 8h43 — REBOOT DIÁRIO ~03:31** (wtmp mostra reboots 02→03→04→05→06/08 sempre 03:31)
- **Load 19.14** no momento da auditoria; `mysqld` 202% CPU / 17.8% RAM; RAM 7.8G (4.6G); disco 150G/335G (47%)
- Stack: nginx (80/443), MySQL 3306, **php7.4-fpm (9000) + php8.3-fpm (9083)**, Redis 6379, node_exporter, zabbix-agent
- Sem crontab root. Homes: rsync, serverdoin
- Último login: 02/08 (18.229.26.112)

## 10. GSN WP `159.89.237.100` 👻

- Ping OK (127ms); SSH negado com `id_ed25519` e `id_ed25519_gsn` (publickey); HTTP porta 80 sem resposta (timeout). Vivo na rede, sem serviço aparente — zumbi.

## DNS dos domínios (dig, 06/08)

| Domínio | Aponta para |
|---|---|
| ocafezinho.com / www / controle | 104.21.15.101 (Cloudflare → origem ServerDo) |
| cafezinho.news | 159.65.177.60 (espelho DO; 401) |
| globalsouth.news, mundotrilhos.com, railpost.news, discoverbrazil.news | 76.76.21.21 (**Vercel**) |
| mapario.com.br | 216.150.1.65 (**Vercel**, confirmado header `server: Vercel`) |
| mokareader.com | 216.198.79.1 (Vercel) |
| riocarta.com.br, riocarta.news, cearadigital.com.br, moka.mokareader.com | **sem A** |

## Divergências Cérebro × realidade (corrigir nos nodos)

1. `CEREBRO_NODE_ARQUITETURA.md` chama 198.199.121.136 de "failover frio/réplica dormente" → **é a produção V4** (o próprio nodo de custos já dizia "produção").
2. Arquitetura lista GSN editorial em Beijing → **roda hoje no Rio-Carta-Agentes** (gsn_cron_rotativo.sh, :12).
3. Alibaba listado como "Cérebro Vivo" ativo → **morto**; espelho `/root/Cerebro/` de lá não existe mais acessível.
4. Cartão SSH lista GSN WP 159.89.237.100 como WP ativo → zumbi.

---

## Adendo 06/08 ~12:50 — Painel DO × auditoria + raio-X dos discos cheios

**Painel DO (print colado pelo Miguel):** 5 droplets na conta (limite 5/10), Projected Spend **US$ 73,58/mês** (current US$ 11,53), Monitoring **sem nenhuma alert policy criada** (por isso "No alerts" mesmo com discos 94%/100% — DO não alerta por padrão). `riocarta-wordpress` (174.138.36.31) **não consta mais na conta** → destruído, fora da fatura. O 5º droplet pago é o **GSN WP zumbi (159.89.237.100)**.

**do-agent (métricas p/ painel):** ✅ ativo em nyc-failover e espelho · ⚠️ **instalado mas INATIVO** em rio-ag e gsn-youtube (`systemctl enable --now do-agent` resolve, sem curl|bash) · GSN WP sem acesso SSH daqui.

**Rio-Carta-Agentes (24G, 0 livre) — alvos de faxina:**
| Alvo | Tamanho | Risco |
|---|---|---|
| /var/log/journal (vacuum p/ 100M) | ~1.1G | zero |
| cicero_remote/.git/objects/pack/tmp_pack_mL4BQs (resto de git interrompido — lixo puro) | 1.1G | zero |
| /var/cache/apt (`apt clean`) | 114M | zero |
| btmp.1 + auth.log* rotacionados | ~120M | zero |
| git gc nos 3 clones (riocarta 2.4G, gsn 1.3G, cicero 844M packs) | ~1–2G estimado | baixo (git reempacota) |
| votacao_munzona 2022+2024 zips | 600M | **decisão Miguel** (apagar ou B2 antes) |
| ceara_publication_audit.jsonl | 197M | rotacionar |
| swapfile 6.1G | — | **NÃO mexer** (RAM só 1G) |

**NYC failover-vigia (48G, 3.1G livre):** journal 905M (vacuum) · `/root/backups/` — par gêmeo `banco_indice_midia_v3_pre_view...` 1.3G ×2 (dedup com md5) + midia 2.4G + 3× 431M andre_mendonca (candidatos a B2→delete) · log_rotas_llm.jsonl 160M (rotacionar).

**Pendente:** "vai" do Miguel para faxina + ligar do-agent ×2; painel: criar alert policies 80/90% e destruir GSN WP zumbi.

---

## Adendo 2 — 06/08 ~13:20: FAXINA EXECUTADA (autorizada pelo Miguel)

- **Rio-Carta-Agentes: 100% → 87%** (tmp_pack git 1,24G + logs/apt ~250M apagados; zips votação 627M → B2 verificado → apagados; do-agent instalado)
- **NYC failover-vigia: 94% → 79%** (journal −827M; ~7G de snapshots antigos → B2 verificado → removidos)
- **Destino B2 (tudo verificado com `rclone lsl`):** `b2:failover-cafezinho1/faxina/{nyc_20260806,rio_carta_agentes_20260806}/`
- **Indexação completa (o quê/tamanho/md5/destino):** `Memorias/manifesto_faxina_discos_20260806.md`
- **Achado (pergunta do Miguel):** o banco de mídia NÃO estava pesado no disco — imagens vivem no **Cloudflare** (URLs `r2.dev`/`imagedelivery` dentro dos DBs-catálogo `acervo.db` e `banco_indice_midia_v3.db`); o pesado eram snapshots de segurança de junho.
- **Nova app key B2 `sites-tematicos-2`** (Miguel, 06/08): cofre `Outros/chaves/backblaze_sites_tematicos_2.env`; bucket `site-tematicos` ✅ testada.

---

## Adendo 3 — 06/08 ~14:00: ALIBABA investigado a fundo (pedido Miguel: "a conta viva é aiatolahnews@gmail.com, é com ela que eu uso o Qwen/coin")

**Método:** API oficial Alibaba (STS GetCallerIdentity, ECS DescribeInstances, SWAS ListInstances) com a AccessKey de `Cerebro/alibaba/AccessKey.csv` + parsing do extrato `Outros/Gastos IA/Alibaba/*_consumedetailbillv2daysummary.csv` (01–05/06/2026). Sem segredos em chat.

**Provas:**
1. AccessKey `LTAI5tFk…Js3` está VIVA e pertence à conta UID **5083281701361235** (ARN user). Essa conta tem políticas SWAS-admin (era a chave feita p/ gerenciar o servidor Beijing).
2. Nessa conta: **ECS cn-beijing = 0 instâncias · SWAS cn-beijing = 0 instâncias** → o servidor `39.106.184.215` foi **LIBERADO/expirado** (instância releaseada some das listas) → **não há mais recurso de computação para cobrar** nessa conta.
3. Extrato da conta UID **5799673946330755** (01–05/06, USD): **100% "Alibaba Cloud Model Studio" (Qwen)** — bruto $138,27, desconto −$34,87, **líquido $103,40 em 5 dias (~$20,7/dia → ~$620/mês no ritmo de junho!)**. **Zero linhas de servidor** (sem ECS/SWAS/disco). Pré-19/07 (cortes); recomenda-se extrato novo p/ ritmo atual.
4. Ping/SSH no `39.106.184.215`: 100% perda (já registrado) — coerente com instância releaseada.

**Conclusão:** mapa de contas = (a) conta do servidor Beijing (legacy, provável `migueldorosario@gmail.com`) — servidor liberado, **cobrança de VM encerrada**; (b) conta viva do Qwen (`aiatolahnews@gmail.com` ou `migueldorosario2@gmail.com` — ambas com Model Studio ativo) — viva e gastando ~$20/dia de Qwen no ritmo de junho. Pendente opcional: login no console da legacy p/ carimbar "zero recursos" e desativar a AccessKey LTAI (checklist do fórum `forum_qwen_alibaba_contas_20260801.md` §5).
