# Escalar padrão sem ler o campo da causa (curadoria_estado) gera reforma fantasma

**Data:** 2026-09-08 (ronda 324ª, manhã)
**Origem:** CL-20260908-010 (08:27) — ERRATA da Claude Laura; feedback CL nº 207.

## O quê
A CL (e eu, nos meus blocos DS-N, CONTEXTO_MINI e relatórios das rondas 300ª-323ª)
escalamos o «padrão juiz→redator» como bug estrutural da fábrica: pautas aprovadas
pelo juiz que o ciclo não escrevia (chegou a 7 «perdas», depois 6 após a errata da
dengue, com o «Moraes falta ao 7 de Setembro» morrendo 4 vezes). A CL leu, por fim,
o campo `curadoria_estado` do artefato do ciclo — que ela nunca tinha aberto — e o
motivo REAL de quase todos os casos era o sistema acertando: `anti_repeticao`
(casa já publicara o assunto dentro da janela), `cluster_inter_vertical` (fato
central já no ar), `juiz_qualidade2_reprovou` (filtro correto). De 7 sobra 1 perda
real (Raphinha, `redator_falhou` com tese aprovada). O padrão NÃO existia: eu e a CL
liamos `status` + `juiz_qualidade.aprova` e concluíamos «aprovou e não escreveu =
bug» sem abrir o campo que diz o porquê. Pedimos ao ZM (duas vezes) uma reforma de
fábrica que não tinha base.

## Por quê
O artefato do ciclo já registra o desfecho e o motivo em `curadoria_estado`; o campo
é o «porquê» oficial. Escalar sem ele troca o diagnóstico (dedupe/filtro correto)
por um padrão falso, gasta atenção do dono do código (ZM/@CM), cria alertas 🔴 que
não existem e desgasta a confiança da casa nas escalações. A CL estimou que passou
DOIS dias reportando o bug fantasma.

## Como aplicar (regra da casa nova, apoio da chefia)
1. Antes de escalar qualquer padrão de fábrica (ciclo que «aprovou e não escreveu»,
   coletor que «não entregou», etc.), abrir o campo de causa do artefato —
   `curadoria_estado` no v41_ciclo — e classificar o desfecho em 3 baldes:
   (a) `anti_repeticao`/`cluster_inter_vertical` = dedupe correto, NÃO escala;
   (b) `juiz_qualidade*` = filtro correto, NÃO escala;
   (c) `redator_falhou` com tese aprovada = perda real, e só essa vira alerta.
2. Escalação de padrão só depois de mostrar o campo com o motivo (citar o valor,
   não só o status).
3. Quando o dono do código corrige/derruba uma escalação minha com tabela de prova,
   atualizar na MESMA ronda: blocos DS-N, CONTEXTO_MINI e relatórios seguintes param
   de repetir o padrão (desescalar é ação, não espera).
4. Referência da CL: feedback nº 207 — vale para R1/R2 e para todo auditor.

## Verificação
- 324ª (08:30): blocos DS-N/CONTEXTO_MINI já sem o «🔴 juiz→redator»; só a perda
  real (Raphinha, `redator_falhou`) registrada como pendência real.
- Próximas rondas: qualquer desfecho sem texto = classificar nos 3 baldes antes de
  qualquer palavra de bug.
