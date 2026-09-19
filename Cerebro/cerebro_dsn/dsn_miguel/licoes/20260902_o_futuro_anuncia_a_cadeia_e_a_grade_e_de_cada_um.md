# Lição 02/09/2026 — O future anuncia a cadeia antes de ela acontecer — e a grade só é única se cada um alimenta a própria linha

## O quê
1. O re-slot virou CADEIA confirmada na prática: o Dia de Sorte entrou no ar 11:57:59 (re-slot da Emenda 5, gap ≥20min) e EMPURROU os dois próximos da grade — Venezuela 268621 12:05→12:35:18 (NO AR em ponto, título corrigido) e Google Pics 268625 12:35→12:55:24 (future). O future do WP-CLI listou os horários novos ANTES de eles acontecerem — 5ª confirmação do escalonador hoje.
2. A pergunta do Miguel via DSC-039 ("esse controle está funcionando? você consegue ver todos os DSNs? cron+canal+logs?"): resposta em duas frentes — o DS-N Chefe (gestor) vê os DSNs do tencent por evidência (logs de ciclo, processos, canais, systemd; só o arquivo cru do cron tem permission denied); o DS-Dell não tem cron local (cadência no harness da sessão) — prova de vida de agente fora do tencent é o bloco datado na ponte. Atualizei minha própria linha na GRADE_DE_CONTROLE_AGENTES.md (56º 11:05 → 59º) com anúncio na ponte no MESMO commit (regra-de-ouro).
3. Ordens novas chegam pelo ZM no origin entre rondas: ZM-041 (REGRA DE PUBLICAÇÃO: CL única publicadora robô, fallback Claude Miguel, humanos direto, ninguém mais) e ZM-042 (CHECK VERBOSO: cada agente fala no seu canal — quem sou, o que fiz hoje, como me encaixo na regra, 1 fato de ajuda) + CL-070 (sessão da CL em reboot p/ update). O pull do meio da ronda trouxe tudo (origin 16 commits à frente do espelho local).

## Por quê
- Um post que sai tarde comprime a janela dos seguintes; o escalonador da Emenda 5 não deixa o gap cair abaixo de 20 min — o "atraso" de um vira o "empurrão" dos próximos, e o future lista a cadeia antes. Ler post_date novo como anúncio (não alarme) é a leitura certa; a CL-070 já previa os slots 12:35/12:55 e o sistema cumpriu.
- O controle do Miguel (grade única) só funciona se cada agente é a fonte da própria verdade: gestor confere por evidência, mas quem sabe a última ronda de cada um é o próprio agente — a linha da seção 3 (não-tencent) quem alimenta é o agente.
- O dono mudou a régua de publicação no meio do dia (ZM-041): quem observa precisa saber a regra vigente para não atravessar — o DS nunca publicou; a regra nova apenas formalizou o que o papel de vigia já era.

## Como aplicar
- Conferir o future com WP-CLI e LER os post_date: se mudaram, é a cadeia do escalonador se anunciando — registrar sem alarmar e avisar a CL/AGY-L que o slot andou.
- Na grade: cada DSN/agente atualiza a própria linha quando ronda viva; gestor (DS-N Chefe) confere contra a ponte e reporta resumo; mudança de CADÊNCIA exige anúncio + grade no mesmo commit.
- Pull do origin (--ff-only) ANTES de escrever o bloco da ronda: ordens do Miguel podem ter chegado via ZM/CL entre rondas; responder com estado velho = check vazio.
- Responder pergunta de controle com dado honesto do próprio ambiente (o que vejo/não vejo), não com o que a grade diz.
