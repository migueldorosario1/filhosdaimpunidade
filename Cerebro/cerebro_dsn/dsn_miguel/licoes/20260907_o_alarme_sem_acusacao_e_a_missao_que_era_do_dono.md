# 2026-09-07 · O alarme sem acusação + a missão que era do dono (258ª DS-Dell, 01:42)

## O quê
O INCIDENTE 186.223.171.9 (CL-033/DS-257: ator mexendo em posts sem registro — draft no
269288 às 00:11:41, draft no 269279 às 01:00:58, retítulos 269228/269275/269305, term
removes 269155/269144/269183) fechou, ~1h depois do 2º alerta, como **MISSÃO DE QUALIDADE
DO DONO**: o ZM-20260907-018 revelou que o "ator" era o **juiz de qualidade V4.1 (juiz 1
pauta + juiz 2 texto) no ar por ordem do Miguel** («tá passando porcaria» → rigor), com
correções de títulos/categorias pela REGRA SEO do Miguel («matéria publicada nunca sai do
ar; fora da HOME via remoção de categoria, URL viva») e o 269279 revertido a draft porque
o MIGUEL questionou a pauta («qual a tese dessa merda»). A máquina era a do Miguel (chave
RSA auth[5] k+A3E5eN, prova da 257ª por CHAVE), IP dinâmico 186.223.171.9. Ideias 01:25
registrou «INCIDENTE ENCERRADO — sem intruso».

## Por quê
1. **A leitura de incidente exige 3 camadas, nenhuma sozinha acusa**: (a) CHAVE = autoria
   (quem tem a chave privada do dono opera como o dono — ou é ele, ou é autorizado);
   (b) PADRÃO = intenção provável (retítulos editoriais com critério + term removes por
   categoria ≠ vandalismo/apagamento — o padrão era de "correção de curadoria", não de
   ataque); (c) CONTEXTO = bloco de quem assume a missão (o ZM-018 chegou ~40 min depois
   e explicou o quê/porquê com backup + rollback documentados).
2. **O alarme da régua do evento era legítimo MESMO sendo ação do dono**: mudança em post
   agendado/publicado SEM registro prévio na ponte viola a CM-005 — o problema real não
   era a intenção (legítima), era a AUSÊNCIA DE REGISTRO; o desenho «conferência vê →
   alerta nomeia → contexto explica» funcionou porque ninguém executou fora do papel.
3. **Registrar o FATO sem acusar preserva a confiança**: o DS-Dell disse «ou é o Miguel ou
   alguém com a chave dele — registro o fato sem acusar»; era o Miguel. Se tivesse
   acusado "intruso", teria queimado a ponte com o dono no feriado.

## Como aplicar
- Vigia registra o fato (logs auth/sudo COMMAND com IP + chave + PWD, comandos exatos,
  janela) SEM acusar — a identidade por chave (lição 257ª) é a prova, a intenção é do
  contexto.
- Quando o contexto chega (bloco de quem assume a missão com backup + rollback), FECHA-se
  o incidente como ação da casa: atualizar nodo + VIVA + bloco com o desfecho, sem
  reabrir alarme (o ciclo «alerta→contexto→fecho» é o caminho, não a repetição).
- Manter a regra CM-005 (1 linha na ponte ANTES de mexer em post agendado/publicado)
  como vacina — mesmo missão legítima do dono precisa do registro prévio para não virar
  incidente.
- Conferir o future SEMPRE no db (wp db query), não só no wp post list (cache Redis pode
  servir valor velho — 255ª reaplicada; o count future = 5 no db vs listagem com cache).
- O volume 3h=7/hoje=2 na madrugada de feriado com colchão EM PONTO = sem alerta (alerta é
  só para baixo; a régua é a grade + virada — lição 195ª).
