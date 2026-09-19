---
name: project-yt-v2-a2-dois-agentes-pt-en-20260620
description: "Decisão arquitetural YouTube V2 (Miguel 20/06 13:50 BRT): A2 — dois agentes separados (en + pt), ambos publicam Cafezinho PT. EN mantém tradução DeepSeek (estado atual D2 PASS), PT é clone novo sem tradução com canais BR institucionais. Cost guard segue desativado por design."
metadata: 
  node_type: memory
  type: project
  originSessionId: 94bb006f-7e8f-4abb-a70e-312694d7ec88
---

**Arquitetura YouTube V2 = A2 (dois agentes separados PT/EN), sancionada por Miguel 2026-06-20 13:50 BRT no chat.**

## Decisão

| Agente | Canais | Fonte | Output | Portal | Estado |
|---|---|---|---|---|---|
| `agente_youtube_en_v2*` | 4 americanos: Judging Freedom, Glenn Diesen, Dialogue Works, Daniel Davis/Deep Dive | inglês | **português (DeepSeek traduz/reescreve)** | Cafezinho PT (`controle.ocafezinho.com`) | ✅ JÁ RODANDO — renomeação do atual (cron `0 * * * *` no Tencent) |
| `agente_youtube_pt_v2*` | BR institucional: Lula, TV Senado, TV Câmara, PT, Canal Gov (de `Legacy20260610/root/agent_data/canais_youtube_institucionais.json`) | português | português direto (sem camada de tradução) | Cafezinho PT | 🚧 A CONSTRUIR — clone do EN, cron sugerido `30 * * * *` (escalona com EN no `:00`) |

Bancos separados: `youtube_dialogos_en.sqlite` + `youtube_dialogos_pt.sqlite`. Prompts separados.

## Estado atual confirmado (20/06 13:50 BRT)

- D2 PASS = post #259946 ("Ataques a Moscou elevam pressão sobre Putin...") via Daniel Davis 8min
- Cron `0 * * * *` rodando `/root/youtube_v2_pipeline.sh` (Kimi configurou)
- Proxy IPRoyal essencial (Tencent IP datacenter bloqueado pelo YouTube)
- Cost guard DESATIVADO por design Miguel (anti-loop é via cache Transkriptor TTL 14d + ledger SQLite UNIQUE)

## Teto pra próximos D2 (se reativarem cost guard)

- $0.50/vídeo (cobre Daniel Davis 8min $0.40 com folga)
- $5/dia
- Cost guard hoje só registra `registrar_gasto()` no banco pra transparência, sem bloqueio

## Engenheiros

- **Coder**: 🟦 Kimi (Engenheiro-Chefe YT V2, assumiu hoje)
- **Peer review**: 👑 Claude/Daemon (eu)
- **Coordenação histórica**: Codex (do tempo AGY-CLI)

## Why

Miguel: "tem o agente YouTube que a gente tem que decidir se faz separado português e inglês" (chat 13:35 BRT). Com base no estado atual do código (`canais_youtube.json` no Tencent só tem os 4 EN; canais BR institucionais existem em arquivo separado nunca integrado), e em peer review entre opções A1 (unificado) / A2 (separado) / A3 (adiar), Miguel escolheu A2 com EN mantendo destino Cafezinho PT.

## How to apply

1. Ao falar de YouTube V2, sempre referir como **dois agentes distintos** (não "o agente YouTube" no singular).
2. Nunca propor reunificar PT+EN num único agente — decisão tomada após análise comparativa.
3. Cost guard segue desativado — não reativar sem AUTH Miguel (já discutido — anti-loop tem mecanismos próprios).
4. Renomear arquivos /root/ (Fase 1) precisa ACK Miguel antes (afeta produção rodando).
5. Quando Sprint Política V2 chegar a Mídia Inicial determinística (Etapa 2H), considerar reaproveitar mecanismos de tribunal de mídia pro YT V2 também (mesma família arquitetural).

Relacionado: [[reference-iproyal-proxy-youtube-yt-dlp-bypass]], [[reference-categoria-youtube-id-20751-obrigatoria]], [[feedback-marcacao-obrigatoria-legado-reforma-todo-comentario]]
