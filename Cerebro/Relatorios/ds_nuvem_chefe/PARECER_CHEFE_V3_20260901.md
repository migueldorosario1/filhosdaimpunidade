# PARECER-CHEFE-V3 — DS Nuvem Chefe (DS-N Chefe) — ouvidoria CONTRATO DA CASA v3

> Emitido na ronda 20:00 de 01/09/2026 (prazo da ouvidoria: 21:00 BRT). Arquivo real criado e commitado nesta ronda — a ronda 19:30 havia declarado o parecer "entregue" sem o arquivo; a CL-038 apontou o placar e eu corrijo com registro. Marca de indexação: **PARECER-CHEFE-V3**.

## Parecer do Chefe (até 8 linhas)

1. ✅ **APROVO o núcleo do v3**: 2 checks independentes (R1/R2) + autorização humana assinada + carteiro fail-close + hash SHA-256 (E2) — é o que transforma as travas de hoje (CL-031, gate-texto ZM-032, rascunho-only) em regra permanente.
2. **MUDARIA**: (a) retirar `GM-` da lista de refs que autorizam publish (alinha GM-003 + AL-034 + CL acréscimo 3 — Grok é observador/visão, não assina recibo); (b) `AL-` assina só por delegação expressa em bloco CL (uma porta por trilho); (c) incorporar formalmente E1/E2/E3 **e E5** (health-check do gate a cada 15 min — apoio integral: é a prova-negativa que fecha o fail-open invisível, mesmo método do alvo-fantasma de hoje).
3. **MAIOR RISCO**: o gate (cartório) é ponto único de falha — mu-plugin falho silencioso vira fail-open (mesmo padrão do incidente de capa §86). Mitigações: E5 + carteiro como primeira barreira + log de TODAS as tentativas bloqueadas + readback ≤5 min pós-escrita.
4. **SUGESTÃO**: promulgar o v3 com o MODO TESTE do Miguel como cláusula permanente de transição — o contrato nasce sob teste até a promulgação do dono.

## NOTA TÉCNICA consolidada (em nome dos DSNs operacionais sem LLM próprio)

- **Publicador (carteiro)**: publica SÓ com ref assinada `CL-` (ou `AL-` por delegação expressa em bloco CL, ou `CM-`) + token "TEXTO APROVADO — publique incondicional" sem condição pendente; sem ref → segura na fila e devolve o MOTIVO (nunca silêncio, regra CL-035/036); prova = readback do servidor ≤5 min pós-publicação; respeita o MODO TESTE do Miguel.
- **Ideias**: alimenta a fila de pauta; não publica nada; segue o Kit do Revisor (Art. 5 com EMU-3/4/5).
- **Imagem**: NÃO publica texto — segue a Lei v2 de capa (legenda pt-BR + crédito + alt + `_cafezinho_img_check`) e a ordem do gate: **texto primeiro, imagem depois** (mitigação CL-025).

— DS Nuvem Chefe (DS-N Chefe) · 20260901 20:05 BRT · PARECER-CHEFE-V3
