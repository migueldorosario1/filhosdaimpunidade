# 📣 SPRINT REDES SOCIAIS — Facebook · X (Twitter) · TikTok (criado 31/08/2026 15:44 BRT, ordem do Miguel via DSC)

## O PROBLEMA (palavras do Miguel)
- Dois buracos: Facebook e Twitter (+ TikTok no pacote). Página do Facebook é GRANDE, mas posts mecânicos = visualização ruim. Precisa ser **MUITO criativo e muito bem feito** pra superar o alcance atual.

## A MISSÃO
- **2 posts/dia por rede** (Facebook, X, TikTok) derivados dos posts do Cafezinho **de autoria Miguel do Rosário**.
- **GATILHO:** sempre que o Miguel publicar post de autoria dele no Cafezinho → a casa produz as peças (1 p/ X, 1 p/ Facebook, 1 roteiro p/ TikTok).
- **AUTORIA SEMPRE:** "Miguel do Rosário" — nunca assinatura de robô.
- **PUBLISH = MÃO DO MIGUEL** (ou rascunho na plataforma): nada de robô postando direto — posts saem do dispositivo/IP dele (autêntico pro algoritmo e pro público).

## ARQUITETURA (pipeline)
1. **SENSOR:** agente de ronda (DS-Dell/DS-N) detecta novo post no canônico com autor = Miguel do Rosário (wp-cli/REST).
2. **REDAÇÃO CRIATIVA (o coração):** roteirista da casa (Claude Miguel/DS Laura + revisão CL) produz TRÊS peças do MESMO fato, cada uma nativa da rede:
   - **X (Twitter): 2 TWEETS** (correção do Miguel, IDEIA-001A — NÃO é fio): Tweet 1 = TEXTO LONGO com gancho (se X Premium; sem Premium → ≤280 chars ou imagem-legenda) · Tweet 2 = só o LINK do post. Publicar 1→2 com 2-5 min.
   - **Facebook: POST LONGO** (200-400 palavras): tom de colunista, contexto humano, pergunta pra gerar comentário, imagem própria (capa adaptada, não só link) + **LINK NO 1º COMENTÁRIO, nunca no corpo** (correção IDEIA-001A).
   - **TikTok: ROTEIRO DE VÍDEO** (30-60s): hook 3s, 3 beats, CTA; usa estrutura Moka Vídeo quando pronto.
3. **ENTREGA (one-click pro Miguel):** pacote no Telegram do Miguel (e na GUI): textos prontos pra COPIAR+COLAR + imagem anexada + instruções de 1 linha. Alternativa técnica (fase 2): rascunho direto no Facebook via Page API (post não publicado) e agendamento X via API paga — só com orçamento aprovado antes (regra transparência).
4. **FEEDBACK LOOP:** Miguel responde com alcance/visualização das peças → casa calibra criatividade (métrica: alcance por peça, não volume).

## QUALIDADE (anti-mecânico — a queixa central)
- Proibido: copiar título+link. Obrigatório: gancho próprio por rede, imagem adaptada, voz de colunista.
- Cada peça passa por revisão ( Checklist DSC-005 estilo consultivo) antes de ir pro Telegram.

## DIVISÃO INICIAL
- Sensor: DS-Dell (ronda 30/30, flag AUTORIA_MIGUEL) · Redação: Claude Miguel + DS Laura · Revisão: Claude Laura · Entregador: DSC (Telegram) · Métrica: DS-N Chefe (relatório semanal no arquivo indexado) · Miguel: publica e diz o alcance.

## REGISTRO
- Arquivo dos pacotes entregues: `cerebro/Relatorios/redes_sociais/AAAA-MM-DD.md` (mesma regra DSC-006: nada se perde).
