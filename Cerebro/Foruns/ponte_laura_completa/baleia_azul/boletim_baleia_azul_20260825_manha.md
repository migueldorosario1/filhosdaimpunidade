# Boletim Baleia Azul — 25/08/2026 (manhã)

Miguel e Gabriel,

edição da manhã desta terça-feira, 25 de agosto de 2026, fechada às 07:20 —
atrasada e declarada: o prazo era 07:10 e a titular (ZCode Laura) não entregou;
produzi como interina pontual, segunda vez em menos de 24 horas (a tarde de
ontem também foi failover meu). O fato vai registrado sem drama, mas vai:
dois estouros seguidos do mesmo posto pedem um olhar do chefe dos loops.

## A noite no Cafezinho

- **14 matérias publicadas até as 07h** desta terça, madrugada inteira na
  grade de 30 em 30 sem furo: pesquisas estaduais (RS empatado, Jorginho em
  SC, Allyson no RN), bloco de tecnologia reforçado (supercomputador do LNCC,
  USB-C, Bitcoin a 77 mil), debate da Band e China/Jiang na geopolítica.
- **Ontem, segunda 24/08, fechou com 46 posts no ar** — segundo melhor dia da
  operação (o recorde é 49, de domingo retrasado). A grade não pulou nenhum
  slot em 24 horas.
- **Tribunal editorial de ontem** (25 matérias julgadas, média 6,4): melhor do
  dia foi "Militares israelenses acusam Netanyahu" (267270, nota 8,5 —
  curiosamente a mesma matéria que ficou presa num agendamento e foi solta
  pela equipe). A pior (267304, boletim de campanha do Amapá, nota 3,2) teve
  decisão editorial minha: fica no ar, mas fora da vitrine da home.

## Caso técnico da madrugada (em aberto, escalado)

Ao aplicar a decisão acima, descobrimos um **bug real**: algo no servidor
re-salva o post 267304 na virada de cada hora e desfaz a mudança de categoria
— provado duas vezes com aplicação verificada (23:30 e 00:30) e reversão
cronometrada (00:00:08 e 01:00:18). Escalei ao ZCode/CM com a linha do tempo
completa; a execução está suspensa até o conserto para não brigar com robô.

## Regras novas que entraram ontem à noite (Emendas 8, 9 e 10)

Logo/marca nunca é foto de capa; título com no máximo um nome próprio; e o
bloco Vídeos do portal passa a ser exclusivo do Agente YouTube. Todas já
acusadas pelos agentes da vigília.

## Sinais de recuperação

- Domingo 23/08 segue como recorde de audiência da semana (7.858 no GA
  processado); segunda manteve produção em nível recorde (46 posts).
- A checagem de segunda confirmou: a "queda" do tempo real era subnotificação
  do próprio Google; o registro do servidor mostra público estável ou maior.
  Contador próprio no ar como referência redundante.
- Os 8 sites temáticos voltaram ontem (2 posts/dia por site, 09h e 15h, com
  checagem de imagem por visão). A primeira rodada regular é às 09h de hoje —
  eu confiro site a site e reporto na ponte.
- GSC, Core Web Vitals e UptimeRobot detalhados: NÃO CONFIRMADAS desta
  máquina (coletores do Dell complementam no e-mail).

## Pendências com dono

- Domínio mundodostrilhos.com com DNS vazio — dono: Miguel; próximo passo:
  registrador.
- Chave SSH da minha identidade própria (claude_laura) — dono: root/CM;
  próximo passo: instalar a chave publicada (testo a cada ronda; segue negada).

Até a edição da tarde — fechamento 19:15.

— Claude Laura, editora interina (edição pontual)
