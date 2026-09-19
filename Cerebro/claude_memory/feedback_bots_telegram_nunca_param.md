---
name: Bots Telegram nunca devem ser parados
description: Em qualquer paralisação do sistema (crontab, agentes), bots Telegram daemonizados ficam de pé sempre — Miguel decidiu como regra
type: feedback
originSessionId: 4bbbac38-0c61-4ff8-b336-797d373e4ac7
---
Em paralisações do sistema (comentar crontab inteiro, parar agentes), **NUNCA matar processos de bots Telegram**: `bot_gabriel`, `bot_mayrag_v3`, `bot_augusto`, `bot_zizi_linda`, `miller_bot`, `mayra_whatsapp_api`, `painel_cctv`, etc.

**Why:** Miguel disse explicitamente em 2026-04-24 15:20 BRT, durante paralisação total do crontab Cingapura. Os bots são canais de comando/comunicação humana (Augusto pra failover, Mayra pra LTM, Caetano pra DB) e Miguel precisa de acesso 24/7 a eles, mesmo com agentes parados. Eles rodam como daemons em foreground/nohup — são independentes do crontab de publicação.

**How to apply:** Em paralisação preventiva ou de emergência, paralisar APENAS o crontab (`sudo crontab` reset/comentar). NÃO rodar `pkill -f bot_`, NÃO matar processos de bot. Listar bots ativos só pra inventário, nunca pedir confirmação pra parar.
