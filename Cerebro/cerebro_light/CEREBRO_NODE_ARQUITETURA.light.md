# CEREBRO_NODE_ARQUITETURA — VERSÃO LIGHT
> Gerado automaticamente por `cerebro_light.py` em 2026-07-09 03:32 BRT
> Original: `CEREBRO_NODE_ARQUITETURA.md` (93KB) — 76 entradas totais
> Este arquivo é READ-ONLY. Edite sempre o original.

---

## CABEÇALHO ORIGINAL (primeiras linhas)

# 🏛️ CÉREBRO CAMADA 2: Nodo de Arquitetura

Este arquivo pertence à Camada 2 do Grande Cérebro. Ele concentra todos os links para Fóruns, Memórias e Arquivos de Código-Fonte relacionados à **arquitetura do projeto, failovers, infraestrutura de servidores e bots**.

> **Regra do Tema Duplo:** Todo novo projeto de infraestrutura listado aqui deve possuir um par (Fórum + Memória).
> - **Fórum:** Para entender o planejamento e o resumo da arquitetura.
> - **Memória:** Para ler o log técnico, comandos executados e credenciais/portas.

---

## 0. Chaves Mestra e Acessos SSH (Mandatório)
Para evitar bloqueios de permissão ("Permission Denied") e timeouts, a Trindade DEVE usar as chaves corretas para cada cluster de servidores abaixo:

1. **Master Server (Tencent / Cingapura)**
   - **IP:** `43.156.151.165` (Porta: `38422`)
   - **User:** `ubuntu` *(root bloqueado)*
   - **Chave Local Exigida:** `~/.ssh/id_rsa`
   - **Comando base:** `ssh -i ~/.ssh/id_rsa -p 38422 ubuntu@43.156.151.165`

2. **Cluster DigitalOcean (Nova Conta / NYC / Astro / Rio Carta)**
   - **IPs:** `198.199.121.136` (Cafezinho Failover), `159.89.185.209` (Astro), `174.138.36.31` (Legacy WP)
   - **User:** `root`
   - **Chave Local Exigida:** `~/.ssh/id_ed25519`
   - **Comando base:** `ssh -i ~/.ssh/id_ed25519 -o IdentitiesOnly=yes root@<IP_DO_DROPLET>`
   - **Rio Carta vivo auditado 2026-05-22 23:50 BRT:** `159.89.185.209` = `agente-clone-01`, NÃO legado. Hospeda `riocarta_admin.service`, crontab de coleta/publicação/indexação e clone Astro `/root/riocarta_remote/rio_carta/`. Ver mapa operacional em [CEREBRO_INDEX_RIOCARTA.md](./CEREBRO_INDEX_RIOCARTA.md).

3. **Alfândega Chinesa (Beijing)**
   - **IP:** `82.156.167.218` (Porta: `22`)
   - **User:** `ubuntu`
   - **Chave Local Exigida:** `~/.ssh/id_ed25519`
   - **Comando base:** `ssh -i ~/.ssh/id_ed25519 -o IdentitiesOnly=yes ubuntu@82.156.167.218`
   - **Função GSN atualizada em 2026-05-21 13:30 BRT:** executor canônico dos agentes Global South News (GSN), no path `/home/ubuntu/gsn_agentes/`. O site público do GSN continua GitHub -> Vercel; Beijing executa agentes, gera Markdown/assets e faz `git push`. Não confundir com Alibaba/Beijing do Cérebro nem com NYC legado.

4. **ServerDoIn (Brasil) — ⚠️ CONGELADO**
   - **IP:** `190.89.239.65` (Serverdo.in)
   - **Status (2026-05-24):** P0 ServerDoIn Fase D **congelada** por ordem de Codex Maestro.
   - **Motivo:** Incerteza sobre qual é o WordPress canônico do Cafezinho. Existem 3 caminhos WP (`/var/www/ocafezinho`, `/var/www/ocafezinho-BKP16-05-2026`, `/var/www/rioocafezinho`), e o Cafezinho usa CDN pesado. Miguel não conseguiu confirmar a origem viva com segurança.
   - **Decisão:** Não instalar `wp_metrics.sh`, não criar cron, não alterar `node_exporter` até ordem explícita do Miguel.
   - **Candidato provável:** `/var/www/ocafezinho` (nginx aponta vhosts, logs ativos, WP-CLI retorna posts recentes que batem com REST público).
   - **Legados isolados:** `rioocafezinho` e `ocafezinho-BKP16-05-2026` fora da métrica nova.
   - **Fórum:** `Foruns/forum_sprint_P0_telemetria_serverdoin_20260524.md`
   - **Não é Rio Carta vivo:** auditoria read-only em 2026-05-22 não encontrou crontab/arquivos Rio Carta relevantes neste host.
   - **GSN cron auditado 2026-05-23 00:00 BRT:** scripts GSN e YouTube existem, mas o crontab atual tem apenas Prometheus/tradutor/stargate. Não há crontab editorial GSN ativo em Beijing neste momento. Ver [CEREBRO_INDEX_GSN.md](./CEREBRO_INDEX_GSN.md).

5. **DigitalOcean NYC — Executor YouTube GSN**
   - **IP:** `142.93.48.252`
   - **Host:** `gsn-youtube-nyc-01`
   - **User:** `root`
   - **Chave Local Exigida:** `~/.ssh/id_ed25519`
   - **Comando base:** `ssh -i ~/.ssh/id_ed25519 -o IdentitiesOnly=yes root@142.93.48.252`
   - **Função:** executor específico do Agente YouTube GSN, criado para contornar bloqueios de YouTube na China. Scripts em `/root/gsn_agentes/`; dados/logs em `/root/agent_data/`.
   - **Status auditado 2026-05-23 00:00 BRT:** crontab atual só tem Prometheus. Cron editorial YouTube está pausado; backup anterior em `/root/agent_data/crontab_pre_pausa_gsn_youtube_20260521_1805.txt` contém `0 */3 * * * /root/gsn_agentes/run_coletor.sh`.

4. **Alibaba Cloud (Beijing) - Oficina de Inteligência / Cérebro Vivo**
   - **IP:** `39.106.184.215` (Porta: `22`)
   - **User:** `root`
   - **Chave Local Exigida:** `~/.ssh/id_rsa`
   - **Comando base:** `ssh root@39.106.184.215`
   - **API RAM:** Chaves OpenAPI armazenadas localmente em `root/chaves/alibaba_api.env` com políticas `AliyunSWASFullAccess` e `AliyunSWASOpenFullAccess`.
   - **Status 2026-05-10:** não é mais Failover 2 do site por padrão. A função canônica passa a ser Cérebro Vivo, Trindade Técnica, memórias dinâmicas, fóruns, relatórios, Swarm Loop e processamento auxiliar. NYC permanece o failover frio do Cafezinho.

---

## ⏩ 71 entradas antigas omitidas
> Para ver o histórico completo, leia `CEREBRO_NODE_ARQUITETURA.md` diretamente.
> Busca rápida: `python3 cerebro.py --buscar <termo>`

---

## ÚLTIMAS 5 ENTRADAS

## [2026-05-16 16:45 BRT] Arquitetura de integração entre Cafezinho, GSN e Rio Carta

Miguel definiu duas direções complementares via Telegram/Augusto:

- **GSN + Cafezinho:** não duplicar trabalho do agente YouTube. A transcrição/coleta/artigo-base deve nascer como artefato canônico único, com adaptadores de saída: Cafezinho em português/WordPress e Global South News em inglês/Astro.
- **Rio Carta + Cafezinho:** matérias fortes do Rio Carta podem alimentar o Cafezinho, mas por fila seletiva, adaptação editorial e filtros de relevância nacional. Rio Carta mantém liberdade própria.

Regra arquitetural: preferir `coleta única -> artefato canônico -> adaptadores por destino`, compartilhando ledger, custos e validação factual. Publicação cruzada deve começar em dry-run/draft/status-gate, sem `

> *(... 163 chars omitidos — ler original)*

---

## [2026-05-16 17:45 BRT] Cafezinho sob controle do Cérebro + retomada Mundo Trilhos/Rail Post

Miguel reforçou via Telegram/Augusto que o Cafezinho precisa ficar sob controle técnico completo do Cérebro: WordPress, plugins, anúncios, arquitetura, backups e dependências do servidor. Isso complementa a frente já aberta de autonomia WordPress/Cafezinho paralelo.

Diretriz operacional: tratar primeiro como inventário e arquitetura. Não mexer em banco, credenciais, plugins, anúncios, DNS, servidor ou publicação viva sem fase própria, backup, rollback e autorização explícita quando envolver produção.

Também pediu retomar Mundo Trilhos e Rail Post como experiência de sites gêmeos, com Mundo Trilhos em português e Rail Post em inglês. Busca local Codex confirmou que a base não está perdida:

- s

> *(... 488 chars omitidos — ler original)*

---

### Confirmação de Domínios (DNS apontado para Vercel)
Em 2026-05-16, a infraestrutura DNS dos três portais autônomos foi devidamente apontada via CNAME/A Record para o IP da Vercel (`76.76.21.21`):
1. **Global South News (GSN)**: `globalsouth.news`
2. **Mundo Trilhos**: `mundotrilhos.com`
3. **Rail Post**: `railpost.news`

Próximo passo seguro: auditoria local read-only/build dos dois sites Astro, configurar o `astro.config.mjs` com os novos domínios, atualizar identidade/interlinks "duas bolas" e preencher com posts fantasmas para a inauguração do fim de semana.

---

## [2026-05-22 00:38 BRT] Mundo Trilhos — decisão headless/Astro/Vercel

Miguel pediu espalhar pela Trindade a decisão arquitetural do Mundo Trilhos. O portal deve abandonar a publicação WordPress e operar como site headless/Astro/Vercel, com geração de Markdown e deploy por Git.

Diretriz consolidada:

- domínio `mundotrilhos.com` tratado como Vercel/headless;
- arquivo legado principal a auditar: `root/agente_ferroviario_v2.py`;
- saída futura: Markdown em `mundo_trilhos/src/content/blog/`;
- publicação: `git commit` + `git push`, com Vercel fazendo build;
- WordPress e banco relacional saem do caminho do Mundo Trilhos;
- Perplexity não entra no pipeline Mundo Trilhos durante esta reforma;
- pipeline editorial deve ser 100% asiático, seguindo a arquitetura registrada no `Foruns/forum_mun

> *(... 628 chars omitidos — ler original)*

---

## §91 Tutorial de Monitoramento — Loop Maestro (2026-05-27)

Tutorial completo para qualquer agente da Trindade assumir o loop de monitoramento 30/30min.

- **Tutorial:** [tutoriais/tutorial_monitoramento_loop_maestro.md](./tutoriais/tutorial_monitoramento_loop_maestro.md)
- **Conteúdo:** Pré-requisitos (SSH, WP REST), 7 etapas do tick (coleta, qualidade, análise, autocura, fórum, report, boletim), mapa de logs, mapa de cascatas LLM, guards §86, checklist para novo agente
- **Relatórios diários:** `Foruns/monitoramento/YYYY/MM/forum_monitoramento_YYYYMMDD.md`
- **Boletim News (link vivo):** `CEREBRO_NODE_BOLETIM_NEWS_CAFEZINHO.md` → seção "RELATÓRIO EM ANDAMENTO"
- **Circuito futuro:** `Foruns/forum_circuito_monitoramento_diretrizes_20260527.md`

---

## PONTEIROS
- Original completo: [`CEREBRO_NODE_ARQUITETURA.md`](./CEREBRO_NODE_ARQUITETURA.md)
- Índice geral: [`indice_cerebro.json`](./indice_cerebro.json)
- Busca: `python3 cerebro.py --buscar <termo>`
- Validador: `python3 validar_cerebro.py`