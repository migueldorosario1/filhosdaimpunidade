# 🚨 Fórum — Central de Alertas do Ecossistema (Uptime Kuma + Vigia de Discos)

> **Criada:** 2026-08-06 ~17:30 BRT por ZCode (Kimi K3), ordem do Miguel ("opção 1 é ótima").
> **Onde vive:** droplet `142.93.48.252` (DigitalOcean NYC) — ex-`gsn-youtube-nyc-01`, renasce como **Central de Alertas** (estava ocioso desde mai/2026).
> **Memória técnica (build completo, bugs e fixes):** `Memorias/memoria_central_alertas_20260806.md`.

## Por que existe

Em 06/08, a auditoria de servidores achou **disco 100% no Rio-Carta-Agentes** e **94% no NYC de produção** — e o painel DigitalOcean dizia "tudo saudável" (DO não alerta por padrão). Miguel aprovou transformar o droplet ocioso em central que avisa **no Telegram** (onde ele já vive: Ponte, Baleia, Augusto) antes do próximo susto.

## O que ela faz (v1)

### 1. Uptime Kuma (Docker `uptime-kuma`, bind `127.0.0.1:3001`)
13 monitores ativos, checagem a cada 60s, 2 retentativas, alerta no Telegram via **bot Augusto**:

| Monitor | Tipo | Estado no nascimento |
|---|---|---|
| Cafezinho — Site (www.ocafezinho.com) | https | UP 200 |
| Cafezinho — Controle WP | https | UP 200 |
| cafezinho.news (espelho) | https (aceita 401) | UP 401 |
| Global South News · Mundo Trilhos · Rail Post · Discover Brazil · Mapa Rio · Moka Reader | https ×6 | UP 200 ×6 |
| Painel Tencent (43.156.151.165:80) | http | UP 200 |
| ServerDo WP (190.89.239.65:443) | tcp port | UP |
| NYC-failover (198.199.121.136) · Rio-Carta-Agentes (159.89.185.209) | ping ×2 | UP ×2 |

- **Desativado (documentado):** Moka API `:8420` — **não é pública** (provado por curl externo: timeout — postura correta de segurança). Monitorar ela exige check interno via SSH (roadmap v2 do vigia).
- **Acesso ao painel:** só via túnel SSH — `ssh -L 13001:127.0.0.1:3001 -i ~/.ssh/id_ed25519 root@142.93.48.252` → `http://127.0.0.1:13001`. Usuário `miguel`, senha no cofre: `Outros/chaves/uptime_kuma_central_alertas.env`.

### 2. Vigia de Discos (`/root/vigia_central/vigia_discos.py`, cron :42 de hora em hora)
SSH read-only (`df`) nos 6 servidores vivos: NYC-failover, Rio-Carta-Agentes, Espelho, Tencent, ServerDo + ela mesma.
- 🟠 ≥85% · 🔴 ≥95% · 🟢 ao normalizar · ⚠️ se SSH falhar. Anti-spam: alerta no cruzamento + lembrete 1×/24h.
- Chave SSH própria da central instalada nos 5 alvos (read-only, comando `df`).
- **Primeiro alerta real (nascimento):** 🟠 Rio-Carta-Agentes 87% (pós-faxina — coerente).

## Mensagens de teste que o Miguel recebeu no Telegram (06/08 ~17:05–17:35)

1. **6× "⚠️ sem resposta SSH"** — FALSO ALARME de desenvolvimento (bug no parse do `df`, corrigido; os SSHs sempre funcionaram).
2. **🟠 Rio-Carta-Agentes 87%** — REAL e vigente.
3. **Down do "TESTE2 fim-a-fim"** — prova fim-a-fim Kuma→Telegram (monitor de teste já removido).

## Custos e notas

- Custo incremental: **US$ 0** (droplet já existia; antes ocioso).
- Notificação Kuma: registro `notification` com `config.type='telegram'` (lição: o campo `type` dentro do JSON do config é obrigatório — sem ele "Notification type is not supported").
- Tipo de monitor TCP no Kuma v1 = **`port`** (não `tcp` — senão "Unknown Monitor Type").
- Roadmap v2: health-check interno da Moka API via SSH; watchdog de RAM; status page pública; checks de custo diário se o Baleia não cobrir.

## Arquivos (na central)

- `/root/vigia_central/vigia_discos.py` · `telegram.env` (600) · `estado.json` · `cron.log`
- Docker: container `uptime-kuma`, volume `uptime-kuma` (DB `kuma.db`)
