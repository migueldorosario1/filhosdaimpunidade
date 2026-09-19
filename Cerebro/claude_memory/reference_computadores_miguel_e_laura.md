---
name: reference-computadores-miguel-e-laura
description: "Ficha técnica dos 2 computadores do Miguel (Miguel = Dell Inspiron Linux, Laura = Windows ARM64) — usar pra saber em qual estou rodando e diferenciar operações"
metadata: 
  node_type: memory
  type: reference
  originSessionId: d556bf3a-514a-43d5-a6d6-417905366fd5
---

Miguel tem 2 computadores sincronizados pelo repo `cerebro-miguel` (GitHub) — pull/push a cada 15min. Ficha técnica pra reconhecer qual é qual:

## Computador **MIGUEL** (este, `novo`)

- **Hostname:** `novo`
- **Fabricante/Modelo:** Dell Inspiron 15 3520 (laptop)
- **Motherboard:** 0TRFM3
- **OS:** Ubuntu 20.04.6 LTS
- **Kernel:** Linux 5.15.0-139-generic (x86_64)
- **CPU:** 12 threads Intel
- **RAM:** 15GB
- **Disco:** NVMe `/dev/nvme0n1p3` 460GB (~71% usado)
- **GPU:** Intel UHD (Device 46a8, integrada)
- **User:** `migueldorosario`
- **Home:** `/home/migueldorosario`
- **Shell:** `/bin/bash`
- **TZ:** `America/Sao_Paulo` (-03)
- **Wi-Fi:** `wlp2s0` (rede 192.168.0.9)
- **Ethernet USB:** `enx00e04c680e41` (rede 192.168.15.3) — placa USB-Ethernet
- **Path canônico Cerebro:** `/home/migueldorosario/Downloads/Antigravity Google/Cerebro/`
- **Path canônico cerebro-miguel:** `/home/migueldorosario/cerebro-miguel/`

## Computador **LAURA** (Windows)

- **OS:** Windows 11
- **Arquitetura:** ARM64
- **Terminal:** Git Bash (via WSL Ubuntu em teste, mas base é Git Bash)
- **User:** desconhecido — não confirmado ainda
- **Path:** desconhecido — não confirmado ainda
- **Papel:** segundo checkout, receptor de edições via `git pull`

## Como saber em qual estou rodando

Rápido: `hostname` → se retornar `novo` = MIGUEL. Se algo diferente = LAURA (ou outro).

Detalhado:
```bash
hostname                      # novo = MIGUEL
uname -sr                     # Linux 5.15... = MIGUEL
[ -d "/home/migueldorosario" ] && echo MIGUEL || echo LAURA
```

## Sync bidirecional entre os dois

- **Miguel → GitHub:** `sync_cerebro_to_github.py` cron `*/30` (empurra alterações do Cerebro/ pro repo)
- **GitHub → Miguel:** `git pull --quiet` cron `*/15` no `~/cerebro-miguel/`
- **Repo → Cerebro/ local:** rsync `*/15` de `~/cerebro-miguel/cerebro/` pra `Cerebro/`
- **Laura:** puxa via `git pull` (frequência depende de estar ligado)

## Diferenças operacionais que mudam meu comportamento

| Aspecto | MIGUEL | LAURA |
|---|---|---|
| SSH `cafezinho-wp` | ✅ configurado | ⚠️ não confirmado |
| Cron ativo | ✅ dezenas de crons | ⚠️ desconhecido |
| Vigília V6 loop | ✅ ciclo `*/30` roda aqui | ❌ não aqui |
| Backup diário 03:40 | ✅ roda aqui | ❌ |
| Rsync Tencent/B2/Drive | ✅ roda aqui | ❌ |
| ZCode/Kimi bridge | ✅ file-based ativo | ⚠️ não confirmado |
