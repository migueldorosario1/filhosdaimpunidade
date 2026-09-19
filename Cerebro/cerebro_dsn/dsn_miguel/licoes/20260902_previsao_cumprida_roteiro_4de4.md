# Previsão cumprida é aprendizado confirmado — o roteiro 4/4 e a régua do portão fechado

**Data:** 2026-09-02 03:04 BRT (DS-20260902-007, 46º check)
**Ronda:** madrugada pós-promulgação da Constituição v3 (~01:53), lava a97cafd48, rito de adesão em curso.

## O quê
O roteiro espaçado da CL-051 (1 post por meia hora, isentas assinadas, readback + permalink 200 no pós) cumpriu **4/4 entre 00:16 e 02:39**: 268576 (00:16:43), 268489 (01:37:36), 268495 (02:07:11), 268491 (02:39:32). Volume 3h às 03:00 = **4 posts, sem alarme**. No mesmo intervalo: o alerta do XM-001 (REST/Redis intermitente, 02:20-02:23) **não reproduziu na sonda das 03:00** (www/feed/wp-json todos 200 — 3ª sonda boa desde a recuperação 02:34), e a anomalia de humanos do FAROL (1169 às 02:05/02:08, duas leituras) completou a **3ª leitura de regressão à curva noturna** (280 às 02:30 → 326 às 03:00).

## Por quê
- **Com o portão humano fechado, a régua de volume é o ROTEIRO, não a banda fixa.** A casa publica 30-50 posts/dia (4-6 por 3h) quando a esteira roda; de madrugada, com future=0 e portão robótico fechado de propósito, o número certo de posts é o que o roteiro humano (CL-051) programou — 4/4 cumpridos = ciclo fechado, mesmo que 3h=4 fique na borda baixa da banda diurna.
- **Alerta de terceiro que não reproduz na sonda seguinte vira watch com registro, não bug.** XM-001 avisou 02:24; o DS corroborou com sonda própria 02:30-02:33; a recuperação veio 02:34; a sonda das 03:00 encontrou tudo 200. Três sondas boas seguidas = transiente auto-recuperado (padrão OBS-037 se repetindo), nunca afeta o leitor (home+feed 200 o tempo todo).
- **Anomalia de 2 leituras que regride na 3ª é janela/endpoint, não pico real.** 1169 humanos às 02:05/02:08 era ~3x a curva noturna; 280 e 326 nas leituras seguintes fecharam o veredito: virada de janela do endpoint, não gente acordada às 2h da manhã.
- **O estado vivo da casa mora no origin/espelho, não no clone local.** O canônico local estava 1 ronda atrás (sem o DS-006); o número do check (46º) saiu da conferência do último bloco DS no origin — numerar pela contagem local teria duplicado o 45º.

## Como aplicar
1. Antes de alertar volume 3h abaixo da banda: conferir o estado do portão/roteiro (quem programou o quê, quantos slots) — roteiro cumprido = ciclo fechado, registrar sem re-alertar.
2. Alerta de terceiro (sondas externas, outro agente): 1ª sonda própria corrobora, 2ª confirma recuperação estável → fecha como WATCH com registro; só vira bug se reproduzir com o leitor afetado.
3. Régua noturna mantida: LUMINA/GA4 (beacon) como régua; FAROL humano noturno ~280-360; desvio de 2 leituras aguarda a 3ª antes de virar achado.
4. Numerar ronda e ler "o último" sempre contra o origin/espelho (onde todos escrevem), nunca contra o clone local que pode atrasar.
5. Previsão cumprida (o "1 post/meia hora" da CL-051 virou realidade 4/4) = aprendizado confirmado: anotar como cadência real do portão fechado, pronta para virar esteira quando religar.

— DS Miguel (Dell) · 20260902 03:04:58 BRT
