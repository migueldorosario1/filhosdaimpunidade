# CEREBRO_NODE_OBSERVABILIDADE — VERSÃO LIGHT
> Gerado automaticamente por `cerebro_light.py` em 2026-07-09 03:32 BRT
> Original: `CEREBRO_NODE_OBSERVABILIDADE.md` (36KB) — 64 entradas totais
> Este arquivo é READ-ONLY. Edite sempre o original.

---

## CABEÇALHO ORIGINAL (primeiras linhas)

# CEREBRO_NODE_OBSERVABILIDADE

**Função:** Registro canônico de observabilidade, métricas e monitoramento da infraestrutura da Trindade. Serve como índice de ferramentas de métricas (Prometheus, Grafana, node_exporter), políticas de cota, credenciais seguras e checklists de rollback.

**Regra de segurança:** Nenhuma credencial real é armazenada neste arquivo. Segredos vão para cofres isolados (ver seção 1). Este node registra apenas paths, finalidades, owners e fingerprints.

---

## 1. Cofre de Credenciais

### 1.1 Alibaba Cloud (Prometheus + Infraestrutura)

**Local do cofre:** `Projeto Cafezinho Agentes/root/agent_data/alibaba_cofre/`
- `cofre_alibaba_ledger_*.jsonl` — histórico de credenciais
- `cofre_alibaba_manifest_*.json` — manifesto de itens do cofre

**Arquivo de chaves de API:** `Projeto Cafezinho Agentes/root/chaves/alibaba_api.env`
- Contém: Access Key ID, Access Key Secret, Region, Instance ID, IP
- Owner: Miguel (CEO) / Codex Maestro
- Última rotação: 2026-05-10

**Política de acesso:**
- Leitura: Codex Maestro, Claude Monitor (para validação)
- Escrita: Miguel (CEO) apenas
- Nunca exponha em fórum/canal/código aberto

### 1.2 Prometheus Alibaba Cloud — Managed Service (CANÔNICO ATUAL 2026-07-08)

**⚠️ Migrado de conta 2026-07-08:** conta antiga (`5799...755-beijing`) tornou-se legado. Cluster produção agora aponta pra conta nova (workspace `Prometheus-Aiatolah`).

**Serviço:** Alibaba Cloud Managed Service for Prometheus V2
**Região:** `ap-southeast-1` (Singapore) — mudou de `cn-beijing`
**Workspace ID:** `default-cms-5083281701361235-ap-southeast-1` (fingerprint: `5083...1235-ap-southeast-1`)
**Instance ID:** `rw-3c86...3258` (fingerprint completo em `alibaba_prometheus.env`)
**Instance Version:** V2 (a antiga era V1)
**Cota:** 50 GB/mês (gratuita, acordo Miguel-Alibaba)

**Método de auth:** HTTP Basic Auth com AK/SK de RAM user (`prometheus-agent`).
- **Password-free access NÃO funciona em V2** — tentado 2026-07-08 sem sucesso, write sempre retorna 401 mesmo com IP whitelist correta. Read funciona com whitelist. É bug/limitação V2 confirmada.
- Whitelist Read cadastrada mesmo assim como camada defense-in-depth: `43.156.151.165/32`, `39.106.184.215/32`, `159.89.185.209/32`, `186.223.171.9/32` (IP local Miguel).
- AK ID fingerprint: `LTAI...dQ3U` (últimos 4 chars)
- Policy anexada: `AliyunPrometheusFullAccess`

**Cofre Prometheus (migração Claude Code, 2026-07-08 11:05 BRT):**
- Arquivo (em cada servidor): `<home>/prometheus_agent/alibaba_prometheus.env` (`chmod 600`)
- Contém: AK_ID, AK_SECRET, PUSHGATEWAY_URL, READ_URL, Workspace ID, Instance ID
- Owner: Miguel / Claude Code
- **NÃO existe no repo local git-tracked** — só nos 3 servidores
- Backups pré-migração dos scripts: `push_metrics.py.bak_pre_migracao_20260708` (Cingapura + Alibaba Cérebro)

**Formato de push (importante):**
- Usar `prometheus_client.push_to_gateway()` com `handler=basic_auth_handler`
- **NÃO usar curl direto com text/plain** — Alibaba V2 retorna HTTP 200 falso positivo (aceita mas não persiste). Só o formato completo com `# HELP`/`# TYPE` da lib é indexado. Lição §9 reforçada.

**Instância antiga (LEGACY):**
- Workspace: `default-cms-5799673946330755-cn-beijing`
- Instance: `rw-debc...99cd4`
- Status: mantida por 24h como fallback via env var `PROMETHEUS_LEGACY_ENDPOINT` (opcional, não configurado por padrão)
- Após 2026-07-09: pode ser desligada por Miguel


---

## ⏩ 59 entradas antigas omitidas
> Para ver o histórico completo, leia `CEREBRO_NODE_OBSERVABILIDADE.md` diretamente.
> Busca rápida: `python3 cerebro.py --buscar <termo>`

---

## ÚLTIMAS 5 ENTRADAS

### 17.4 Solução aplicada

**A. SSH config (`~/.ssh/config`) — `IdentityAgent none` em todos os 8 hosts:**

```
Host tencent
    HostName 43.156.151.165
    Port 38422
    User ubuntu
    IdentityFile ~/.ssh/id_rsa
    IdentitiesOnly yes
    IdentityAgent none          # ← solução AGY-CLI
    ServerAliveInterval 60
    StrictHostKeyChecking no
```

Aplicado em 2026-06-19 03:37 BRT pelo Daemon via Python script. Backup: `~/.ssh/config.bak_pre_identity_agent_none_20260619_0336`. Hosts afetados: `nyc`, `china-install`, `china-proxy`, `china`, `cingapura`, `beijing`, `tencent`, `alibaba`.

**B. MTU local — opções:**
- **B1 (atual, conservadora):** MTU 1360 fixo na interface `enx00e04c680e41`. Reduz eficiência ~10% em tráfego grande, mas zero risco.
- **B2 (recomendação futura):** MTU 1500 + `n

> *(... 186 chars omitidos — ler original)*

---

### 17.5 Validação

Após aplicação:
- `ssh tencent` → OK · uptime 69d · instantâneo ✅
- `ssh nyc` → OK · ubuntu-s-1vcpu-2gb-nyc1 ✅
- `ssh alibaba` → OK · iZ2ze82jxyxjztl5fpi651Z ✅

---

### 17.6 Crédito

- **AGY-CLI** (Antigravity CLI · Sprint 5 Auditoria Técnica) diagnosticou a causa raiz dupla
- **Kimi** abriu o caso 01:30 BRT em `forum_diagnostico_ssh_trindade_20260619.md`
- **Daemon** investigou 7 hipóteses (firewall · fail2ban · KEX · MTU básico · cipher · ISP · Tata) · descartou todas · escalou ao AGY-CLI 03:05 BRT
- **Miguel** aplicou MTU 1360 + autorizou Daemon aplicar IdentityAgent none na config

---

### 17.7 Documentos canônicos

- 📄 `Projeto Cafezinho Agentes/Foruns/carta_agy_cli_misterio_ssh_bloqueado_20260619.md` (cartinha + resposta AGY §11 + solução)
- 📄 `Projeto Cafezinho Agentes/Foruns/forum_diagnostico_ssh_trindade_20260619.md` (caso aberto Kimi)
- 🧠 Memória [[reference-ssh-identity-agent-none-mtu-1360]] (referência permanente Daemon)
- 📋 Backup config: `~/.ssh/config.bak_pre_identity_agent_none_20260619_0336`

---

### 17.8 Regra operacional

**Se SSH voltar a travar no KEX/preauth no futuro:**
1. Verificar primeiro que `~/.ssh/config` ainda tem `IdentityAgent none` em todos hosts
2. Se sim, suspeitar MTU degradado novamente → aplicar `sudo ip link set dev <interface> mtu 1360`
3. Se persistir, ativar `tcp_mtu_probing=1` (B2 acima)
4. Se ainda persistir, escalar AGY-CLI ou abrir ticket Tencent
5. Operação degradada via WP API + DNS direto `8.8.8.8` permanece viável durante incidente

---

## PONTEIROS
- Original completo: [`CEREBRO_NODE_OBSERVABILIDADE.md`](./CEREBRO_NODE_OBSERVABILIDADE.md)
- Índice geral: [`indice_cerebro.json`](./indice_cerebro.json)
- Busca: `python3 cerebro.py --buscar <termo>`
- Validador: `python3 validar_cerebro.py`