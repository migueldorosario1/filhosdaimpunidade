---
name: feedback-indexacao-cerebro-e-pedir-decisao-com-contexto
description: "Registro em cada loop + indexação bem-feita no cérebro; quando precisar de decisão do Miguel, escrever pergunta completa/contextualizada porque quem lê é o Kimi via Telegram (não vai adivinhar)"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: cf4e142a-050c-46de-b793-bee2464fc7f7
---

**3 diretrizes complementares:**

## 1. Registro em CADA loop + indexação bem-feita

**Miguel 06/08/2026 04:20 BRT:** *"Não esquece de registrar tudo sempre. Cada loop é uma oportunidade de fazer o seu registro. Sempre registrado. Depois a gente vai juntar todos esses documentos todos. Tudo tem que estar indexado no cérebro. Bem indexado."*

Extensão da regra `feedback-gravacao-datada-por-ciclo-e-ponte-kimi-regular`. Cada loop Vigília DIA/NOITE (inclusive os "zero drafts") deixa registro:

1. `bugs_YYYY-MM-DD.jsonl` — 1 linha JSON por wp_post (já rodando)
2. `Backups/vigilia_v5/YYYY-MM-DD/<pid>_pre_<tag>_...json` (já rodando)
3. `ciclos_vigilia/ciclos_vigilia_YYYY-MM-DD.md` — 1 seção por ciclo, mesmo os vazios (regra 06/08 02:20 BRT)
4. **Ping consolidado 1×/hora** no `canal_trindade.md` (regra 06/08 02:20 BRT — Kimi acompanha)
5. **NOVO — INDEXAÇÃO CANÔNICA:** ao final de cada dia (último ciclo NOITE 06:17), atualizar `Cerebro/monitoramento_horario/INDICE_CICLOS_VIGILIA.md` com 1 linha por dia apontando pros arquivos-chave (ciclos_vigilia_DATA + bugs_DATA + relatorio_revisores_DATA + progresso backup C0X se relevante). Miguel vai juntar tudo depois — o índice tem que dar o mapa.

**Regra da recursão:** todo bug recorrente vira memoria; toda memoria vai pro MEMORY.md; MEMORY.md é o índice-mestre do que aprendi. Não deixa aprendizado no ar, sem ponteiro.

## 2. Pedir decisão do Miguel com contexto completo (Kimi é a ponte Telegram)

**Miguel 06/08 04:20 BRT:** *"O Kimi tem a ponte direta comigo pelo Telegram, mas você tem que explicar melhor. Se você precisa de alguma dúvida, tem um, por exemplo, ele me falou agora que você está com uma dúvida sobre uma editorial aí da Folha... quando você precisa de alguma coisa traz informação, pede porque me dá informações um pouco mais completa para saber."*

**Contexto do que motivou:** publiquei nos ciclos 21:47, 22:47, 23:17 do 05/08 relatos com frases tipo "264428 aguardando decisão editorial sua" sem explicar o que estava em jogo. Kimi levou a dúvida pro Miguel via Telegram sem contexto suficiente — Miguel teve que perguntar do que se tratava.

**A partir de agora, quando precisar de decisão do Miguel via ponte Kimi:**
- Explicar em 3-5 linhas: (a) qual é o post (ID + título curto), (b) qual é a dúvida específica (não "aguardando decisão" genérico), (c) qual é o argumento pró-publicar, (d) qual é o argumento contra-publicar, (e) sugestão minha (recomendo publicar/ignorar/pending, por essa razão).
- Deixar num arquivo específico (não só no chat): `Cerebro/Foruns/inbox_trindade/kimi.md` com tag `[CLAUDE-DECISAO-MIGUEL-<slug>]` — Kimi copia direto pro Telegram do Miguel.
- Se for urgente (draft prestes a expirar), sinalizar com ⏰ + deadline: "expira em X min do cap 8h".

## 3. Regra específica: matérias da Folha sobre "gafes/erros do Lula" → IGNORAR por default

**Miguel 06/08 04:20 BRT:** *"Gafes Lula é, mas isso aí não precisa botar não, tá, matéria da Folha de Gafes de Lula, isso aí pode ignorar."*

**Aplicação:**
- Matérias factuais da Folha (ou outras fontes tradicionais) focadas em ERROS/GAFES/DESCUIDOS do Lula em discurso/entrevista → default = ignorar (deixar expirar do cap 8h sem publicar).
- **Exceção:** se o erro tem consequência política REAL (levou a retratação oficial, mudança de política, comoção pública) → aí sim publicar, mas com título que contextualize a consequência (não "Lula erra" mero).
- Regra irmã editorial não escrita mas coerente com a linha do blog: Cafezinho não amplifica "gafes presidenciais" como pauta autônoma.
- Caso fundador: 264428 (Lula confunde drones, aviões da FAB e custo de presos em fala no PT) — Folha 05/08. Deixado expirar do cap 8h em 04:17 de 06/08. Confirmação Miguel: correto, era pra ignorar mesmo.

**How to apply:** ao ver draft do worker V4 com título tipo "Lula erra sobre X", "Lula confunde Y", "Lula esquece Z", "Lula troca A por B" — checagem editorial rápida: (i) há consequência política real? (ii) é matéria de fonte de esquerda (então há ângulo crítico legítimo) ou de fonte tradicional (Folha/Estadão/Globo) focada só na gafe? Se (i)=não e (ii)=fonte tradicional → pending por padrão editorial + registrar em bugs_YYYY-MM-DD.jsonl com motivo=`gafe_lula_folha_ignorar_padrao_editorial`. Sem pedir decisão do Miguel (default é ignorar).
