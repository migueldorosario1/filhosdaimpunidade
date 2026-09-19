---
name: Servidores do Cafezinho — nomenclatura vs localização
description: O servidor "Tencent" do Cafezinho fica em Cingapura, não na China; nomenclatura interna "China" se refere à empresa, não ao data center.
type: project
originSessionId: 4d80fcf9-82ab-4e1b-80f4-99384263a443
---
Os dois servidores do Projeto Cafezinho Agentes:

- **Tencent SG (43.156.151.165)** — fisicamente em **Cingapura**. A Tencent é uma empresa chinesa, mas o data center fica em SG. Internamente é apelidado de "China" (ex.: o `watchdog_china.py` pendente na agenda de 2026-04-10).
- **DigitalOcean NYC (45.55.50.249)** — Nova York, failover.

Sincronização: `sincronizar_servidores.sh` faz `rsync` da pasta local `Projeto Cafezinho Agentes/root/` pros dois servidores em `/root/`. Manual, não está em cron.

**Why:** a confusão "nome (China) vs localização (Cingapura)" é fonte de equívocos editoriais e operacionais. Ao discutir failover, watchdogs ou compliance regional, é a localização física que importa, não o apelido.

**How to apply:** quando referenciar o servidor pelo nome "China", lembrar de mencionar "Cingapura" pra não criar mal-entendido. O agente editorial `agente_china.py` é não-relacionado — ele cobre conteúdo sobre a China (país), não tem nada a ver com o servidor.
