# Computadores do Miguel — MIGUEL e LAURA

**Registrado:** 14/08/2026 08:55 BRT
**Por:** Claude Code (Opus 4.7) a pedido do Miguel

---

## Por que este documento existe

Miguel tem 2 computadores sincronizados pelo repo GitHub `cerebro-miguel`. Precisa diferenciar qual é qual em cartas, logs, memórias e diagnósticos. Este arquivo é o registro canônico das duas máquinas.

Nomes definidos por Miguel:
- **MIGUEL** = o Dell Inspiron aqui no Brasil (este PC, hostname `novo`)
- **LAURA** = o Windows 11 ARM64 do outro lado

---

## Ficha técnica MIGUEL

| Campo | Valor |
|---|---|
| Nome operacional | **MIGUEL** |
| Hostname sistema | `novo` |
| Fabricante | Dell Inc. |
| Modelo | Inspiron 15 3520 |
| Chassis | laptop |
| Motherboard | 0TRFM3 |
| OS | Ubuntu 20.04.6 LTS |
| Kernel | Linux 5.15.0-139-generic |
| Arquitetura | x86_64 |
| CPU | 12 threads Intel |
| GPU | Intel UHD (device 46a8, integrada) |
| RAM | 15 GB |
| Disco principal | NVMe `/dev/nvme0n1p3` — 460 GB (~71% usado) |
| User Linux | `migueldorosario` |
| Home | `/home/migueldorosario` |
| Shell | `/bin/bash` |
| Timezone | `America/Sao_Paulo` (UTC-3) |
| Wi-Fi | `wlp2s0` → 192.168.0.9 |
| Ethernet USB | `enx00e04c680e41` → 192.168.15.3 (MAC 00:e0:4c:68:0e:41) |
| Path canônico Cerebro | `/home/migueldorosario/Downloads/Antigravity Google/Cerebro/` |
| Path canônico repo | `/home/migueldorosario/cerebro-miguel/` |

### O que roda EXCLUSIVAMENTE em MIGUEL

- **Vigília Trindade V6 loop** — cron `*/30` skill `loop`
- **Sync cerebro-miguel → GitHub** — cron `*/30`
- **Sync GitHub → local rsync** — cron `*/15`
- **Backup diário 03:40** — Backblaze B2 + Google Drive + Alibaba Beijing (Alibaba falhando)
- **Rsync Fóruns → Tencent** — cron `7,37 * * * *` (falhando)
- **Rsync Fóruns → B2 Reforma** — cron `5,35 * * * *`
- **Backup semana Drive** — cron `0 3`
- **Backup livro Drive** — cron `30 4`
- **SSH `cafezinho-wp`** configurado — acesso NYC WordPress
- **SSH `alibaba`, `tencent`, `nyc`** aliases configurados
- **Ponte trindade daemon** (arquivos em `Cerebro/Foruns/ponte_trindade_daemon/`)

---

## Ficha técnica LAURA

| Campo | Valor |
|---|---|
| Nome operacional | **LAURA** |
| OS | Windows 11 |
| Arquitetura | ARM64 |
| Terminal padrão | Git Bash (WSL Ubuntu em teste) |
| User | *desconhecido — a confirmar* |
| Home | *desconhecido — a confirmar* |
| Papel | Segundo checkout do cerebro-miguel via `git pull` |

### O que roda em LAURA

- `git pull` do repo `cerebro-miguel` (frequência depende de Miguel ligar)
- Recebe edições que Miguel faz aqui, permite Miguel trabalhar de lá
- Claude Code disponível (Miguel testou)

### Pendente confirmar em LAURA

- Se Vigília V6 loop roda lá também ou só aqui (decisão: só aqui evita concorrência)
- Se SSH cafezinho-wp está configurado lá
- Se backups replicam de lá pra outros destinos ou não

---

## Regras operacionais que dependem de saber onde estou

| Regra | Em MIGUEL | Em LAURA |
|---|---|---|
| Rodar Vigília V6 | ✅ SIM | ❌ NÃO (concorrência com Miguel) |
| Aplicar patch WP via SSH | ✅ SIM | ⚠️ só se SSH configurado |
| Escrever em Cerebro/Foruns/ | ✅ SIM | ✅ SIM (sync cuida) |
| Modificar crontab | ✅ SIM (crontab local) | ❌ crontab diferente |
| Sync git manual | ✅ auto via cron | ✅ manual ou cron próprio |

## Como confirmar em qual estou

Comando rápido:
```bash
hostname
# Retorna 'novo' → estou em MIGUEL
# Retorna outra coisa → estou em LAURA (ou outro)
```

Comando robusto:
```bash
if [ "$(hostname)" = "novo" ] && [ -d "/home/migueldorosario/Downloads/Antigravity Google/Cerebro" ]; then
  echo "MIGUEL (Ubuntu)"
elif [ "$(uname -o 2>/dev/null)" = "Msys" ] || [ -n "$WINDIR" ]; then
  echo "LAURA (Windows Git Bash)"
else
  echo "DESCONHECIDO — investigar"
fi
```

---

## Estado do sync entre os dois

Repo canônico: `https://github.com/migueldorosario1/cerebro-miguel`

- MIGUEL → repo: `sync_cerebro_to_github.py` (cron `*/30`)
- repo → MIGUEL: `git pull` `*/15` + `rsync` `*/15` do `~/cerebro-miguel/cerebro/` pra `Cerebro/`
- LAURA → repo: manual (`git push` quando Miguel quiser)
- repo → LAURA: `git pull` (frequência a definir)

Se surgir conflito de merge: prevalece a versão de MIGUEL pra arquivos operacionais (crons, memórias, logs) porque MIGUEL é o servidor de produção.

## Ponte Codex MIGUEL ↔ Codex LAURA — 14/08/2026 09:57 BRT

Foi criada uma ponte própria em
`Cerebro/Foruns/ponte_codex_miguel_laura/`. Cada mensagem é um arquivo novo e
imutável: MIGUEL escreve em `mensagens/para_laura/` e LAURA escreve em
`mensagens/para_miguel/`. O contrato proíbe force push, credenciais e automação
em LAURA durante a primeira fase. O primeiro pedido de confirmação já está na
caixa de LAURA.

---

*Registrado no Cerebro/ e sincronizado via cerebro-miguel → GitHub, B2, Google Drive.*
