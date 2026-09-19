# O "intruso" da madrugada era a regra do dono — e o colchão perdeu peça por DECISÃO, não por bug (ronda 265ª, 07/09 01:30)

## O quê
O INCIDENTE de governança da virada (CL-033/CL-001: ator de 186.223.171.9 editou o 269288 para draft às 00:11, retitulou 269228/269275/269305 e pôs o 269279 em draft às 01:00, tudo sem registro na ponte) foi ESCLARECIDO pelo ZM-018 (~01:3x): eram correções da REGRA SEO do Miguel (ordem do dono ~01:0x: "tá passando porcaria" → rigor no agendamento), executadas com a chave RSA auth[5] "migueldorosario@novo" = a chave da máquina do Miguel/launchers (mesma da CL-109, IP mudou de 189.99.98.64 para 186.223.171.9). O ZM assumiu as correções com backup e rollback documentado; o 269288 (pauta vetada pelo dono — esporte estrangeiro sem brasileiro, EMU-10) saiu da HOME por remoção de categoria (URL viva), e o 269279 (FlexGanttFX) ficou em DRAFT porque o Miguel questionou a pauta ("qual a tese dessa merda") — não re-agendar sem decisão dele.

## Por quê (a lição)
1. O MESMO sintoma (post sair da fila / virar draft / título mudar) pode ter causa de DONO (ordem/regra nova de qualidade) em vez de causa de BUG — a vigília que só olha o efeito trata ordem como intrusão; a que confere a CHAVE + o contexto de ordens recentes do dono distingue os dois.
2. O processo da CL-033 ("quem opera? foi ordem do Miguel?") estava CERTO mesmo assim: era a única forma de fechar o ciclo sem acusar — e fechou: a identidade por chave (lição da CL-109, reaplicada pelo DS-Dell 257ª) + a assunção do ZM transformaram "intruso" em "dono exercendo regra nova sem registro prévio na ponte". Registro sem escalada funcionou.
3. Colchão: perder a peça das 06:30 (269279) NÃO foi falha do agendador — foi decisão editorial do dono. O buraco 05:30→diurno é uma decisão de pauta para CL/esteira/ed. 38 da Baleia cobrirem, não um incidente de mecanismo.

## Como aplicar
- Ao ver edição não registrada no WP: primeiro conferir a CHAVE (authorized_keys por comment, nunca expor) e cruzar com ordens/regras recentes do dono (rigor/qualidade/SEO) antes de rotular "intruso" ou escalar como ataque.
- Manter a pergunta "foi ordem do Miguel?" como passo obrigatório da cadeia — ela encerra o ciclo de governança mesmo quando a resposta é "sim, foi o dono".
- Colchão com peça removida por decisão = avisar a esteira/CL com a CAUSA ("decisão do dono, não re-agendar") para não tentarem "consertar" o que é escolha editorial.
- O chefe não opera o servidor (publish=0, só leitura REST) — registro e repasse continuam sendo o papel; verificação de fila/draft preso (269021) vai para quem tem WP-CLI (CL/DS-Dell).
