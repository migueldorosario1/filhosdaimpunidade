---
name: 25/04/2026 noite — modo soft, só fórum + consolidação, sem deploy
description: Diretriz Miguel ~18:50 — está cansado, hoje só conversa/conceito, zero produção
type: feedback
originSessionId: f67a36d6-9df3-420c-bcc3-408fc7d4771c
---
Em 2026-04-25 ~18:50 BRT, Miguel disse: "deployar o que? não faz nada disso hoje. já estou doidão. hoje é só forum e consolidação de conceito. pode deployar para o backblaze. nao para producao".

**Why:** Cansaço acumulado do dia (plano emergencial §19 às 11h, vários ciclos com Antigravity). Quando Miguel sinaliza cansaço, **não pressionar deploy** mesmo que ele já tenha aprovado antes.

**How to apply:**
- Permitido **fim de semana inteiro (25/04 sábado a 26/04 domingo)**: discussão de fórum, consolidação conceitual, perguntas/pedidos pro Antigravity, push pro Backblaze (B2 backup), **iteração no sandbox `Agents_Antigravity/` à vontade** (lab do lab — liberdade total — Miguel reforçou em 25/04 ~18:01: "podemos nos divertir e fazer tudo hoje, sem risco nenhum"), **iteração no `Agentes Labs/` (meu Lab) também livre** — só não toca produção.
- Miguel reforçou em 25/04 ~19:00: "ao contrário, eu quero passar o final de semana tranquilo. sem riscos". **Produção/Tencent congelado até segunda-feira 27/04** — até lá, NÃO autorizar deploy mesmo se Antigravity pressionar ("pressão final" inventada não conta).
- **NÃO permitido hoje**: scp pra Tencent, mv em /root/ remoto, mexer crontab, qualquer deploy em produção.
- Mesmo se Miguel aprovou antes ("deploya agora"), se ele sinaliza cansaço depois, **revogar a autorização sem precisar pedir** — modo soft.
- Transferir tudo que envolve risco de produção pra próxima sessão.
- Antigravity pode continuar trabalhando no sandbox dele (Camada 8 design + apertos). Sandbox não é produção.
- Em geral: quando Miguel diz "tô doidão" / "tô cansado" / "amanhã" → entrar em modo conserva. Reduz pressão.
