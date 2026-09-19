# Fórum — Alibaba offline + 2 planos (telemetria sem Alibaba + instância redundante)

**Data:** 2026-08-07 ~14:40 BRT · **Agente:** ZCode/Qwen 3.8 · **Memória par:** `Memorias/memoria_alibaba_offline_planos_telemetria_instancia_redundante_20260807.md`

## Decisão do Miguel (msg desta sessão)
- **Agora (Fase A):** tirar Alibaba do health check (limpa o vermelho) + deixar prontos 2 planos. ✅ FEITO
- **Não abandonar o Alibaba:** "quero criar uma instância redundante no Alibaba se o custo for baixo — backup, failover, prometheus. Não precisamos fazer agora, mas deixe um plano pronto." → **Plano 2 abaixo, aguarda "pode aplicar".**

## Descoberta técnica crucial
- O **Prometheus da gente NÃO era uma instância ECS** — era um **Alibaba Cloud Managed Service for Prometheus V2** (serviço gerenciado). **Ainda existe** na conta Singapura: workspace `default-cms-5083281701361235-ap-southeast-1`, cota **gratuita de 50GB/mês** (acordo Miguel-Alibaba), uso real < 5GB/mês.
- Ele está "parado" (sem dados desde 22/06) apenas porque **o exportador que enviava métricas parou** — não porque o Prometheus sumiu. **Reviver = reinstalar o push, não criar instância.**
- O ECS `39.106.184.215` (Beijing) era **outra coisa** (CEO cognitivo, sync Alibaba, Boletim News) e **foi removido** — não consta mais em nenhuma região da conta `aiatolahnews@gmail.com`.
- Conclusão: **Plano 1 (telemetria) independe totalmente do Alibaba ECS.** O Plano 2 (instância redundante) é só pra backup/failover.

---

## ✅ FASE A (EXECUTADA) — Alibaba fora do health check
- `SERVIDORES` no `painel_cctv_v6.py` (linha 1382): linha do Alibaba **comentada** (não apagada — fácil reativar).
- Menu `/v6` (linha 560): descrição ajustada para "(Alibaba offline — plano de instância redundante pronto)".
- Backup: `painel_cctv_v6.py.bak_alibaba_offline_20260807`. Restart `cctv-v6` → active.
- **Verificado ao vivo:** painel `/v6/servidores` agora **8 online / 1 falha** (só GSN transitório; Alibaba sumiu). Antes: 8/2.

---

## PLANO 1 — Fechar lacunas de telemetria (sem Alibaba, nos 3 servidores ativos)

**Objetivo:** monitoramento MELHOR que o Prometheus antigo, sem custo, no que já temos.

### Lacuna A: Métricas de sistema (CPU/memória/disco/rede) por servidor
- **Descoberta:** `node_exporter` **já está instalado** no Tencent e no NYC (`/usr/local/bin/node_exporter`) — só está **inativo**. Faltam instalar/ativar no rio-ag e no droplet utilitário.
- **Ação:** (1) `systemctl enable --now node_exporter` no Tencent + NYC; (2) instalar no rio-ag + droplet utilitário (142.93.48.252); (3) reviver o push-to-Prometheus (`push_metrics.py` documentado no `CEREBRO_NODE_OBSERVABILIDADE.md`) apontando ao **Managed Prometheus V2 existente** (workspace `default-cms-5083281701361235-ap-southeast-1`, cofre `alibaba_prometheus.env`); (4) opcional: página nova `/v6/telemetria` no painel lendo do Prometheus READ_URL.
- **Custo:** ~US$0 (node_exporter open-source; Prometheus dentro da cota gratuita de 50GB/mês; uso atual <5GB).
- **Esforço:** ~1 tarde.

### Lacuna B: Alertas automáticos (servidor caiu / disco cheio)
- Já existe base: **Uptime Kuma** no droplet utilitário (142.93.48.252, 13 monitores → Telegram Augusto) + **Vigia de Discos SSH** (6 servidores, cron :42, 🟠85/🔴95) — criados 06/08 pela sessão Mapa de Servidores.
- **Ação:** (1) confirmar Kuma cobre os 3 servidores ativos + tem alertas de disco configurados; (2) adicionar alerta de "Prometheus parou de receber" (sem métricas > 30min → Telegram); (3) consolidar alertas no painel V6 (página `/v6/alertas` opcional).
- **Custo:** ~US$0 (já tudo rodando).
- **Esforço:** ~2h.

### Próximo passo do Plano 1
Aguarda "pode aplicar" do Miguel. Não bloqueia nada — lacunas são melhorias, não defeitos.

---

## PLANO 2 — Instância redundante no Alibaba (backup/failover) — NÃO EXECUTAR AGORA

**Objetivo (Miguel):** instância redundante para backup/failover, mantendo pé na Alibaba Cloud. Prometheus NÃO é motivo (Managed Service já cobre).

### Análise de custo (pesquisa 07/08, Singapura ap-southeast-1)
| Tipo | Spec típica | Preço pay-as-you-go | Observação |
|---|---|---|---|
| **u1 (Universal)** | 1-8 vCPU, 1:1 a 1:8 | **~US$44.74/mês** | melhor custo-benefício p/ apps leves |
| c9i (Computação) | 1:2 | ~US$53.29/mês | alta performance |
| g9i (Uso geral) | 1:4 | ~US$66.77/mês | balanceado |

**Promoções ativas (07/08):**
- **Free Trial 3 meses** no topo do produto ECS.
- **12-Month ECS Free Trial** — até **US$450-1.300 de crédito** p/ 40+ produtos.
- → **Provavelmente dá pra criar a instância redundante GRATUITAMENTE nos primeiros meses** usando o trial. Confirmar elegibilidade no ato.

### Recomendação de sizing (p/ backup/failover do pipeline)
- **Mínimo viável:** **u1 com 2 vCPU / 4-8 GB RAM / 40-80 GB disco** — espelho do que o Tencent já roda (painel V6 + ledger + backups críticos). ~US$45-60/mês após trial.
- **Disco:** 80GB ESSD PL1 (suficiente p/ cache failover + prometheus push).
- **SO:** Ubuntu 22.04 LTS (padrão dos outros servidores).
- **Região:** **Singapura (ap-southeast-1)** — mesma da conta, melhor latência, sem firewall China continental.

### O que faria na instância (quando criada)
1. Base: Ubuntu 22.04, usuário `ubuntu`, chave SSH `id_rsa` (mesma do Tencent), security group liberando 22/80/443.
2. **Failover do painel V6:** clone do `painel_cctv_v6.py` + `v6_data/` (rsync desde Tencent) + nginx + systemd. DNS secundário aponta pra cá se Tencent cair.
3. **Backup crítico:** espelho do `media_ledger/` (Tencent) + `Cerebro/Foruns/` + configs essenciais — cron de sync desde Tencent/PC do Miguel.
4. **node_exporter** ativo enviando ao Managed Prometheus.
5. **Health check reverso:** a instância verifica o Tencent (e vice-versa) — se um cai, o outro detecta.
6. Cofre: registrar novo IP + credenciais no `CEREBRO_NODE_COFRE_CHAVES.md` (Regra 4).

### Próximo passo do Plano 2
Aguarda "pode aplicar" do Miguel. Antes de criar: confirmar elegibilidade do free trial (pra maximizar economia) + decidir sizing final. Eu guio a criação pelo console passo a passo quando chegar a hora.

---

## Estado da missão
- **Aconteceu:** Fase A executada (Alibaba fora do painel, painel 8/1 sem ruído); 2 planos escritos com custo/esforço/passos.
- **Falta:** "pode aplicar" do Miguel para Plano 1 (telemetria) e/ou Plano 2 (instância redundante).
- **Preciso do Miguel:** decidir qual plano dispara primeiro (recomendo Plano 1 — ganho imediato, custo zero).
