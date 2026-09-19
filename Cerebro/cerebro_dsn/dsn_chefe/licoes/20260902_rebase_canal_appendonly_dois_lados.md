# Rebase em canal append-only: os dois lados são eventos legítimos

**Data:** 02/09/2026 (ronda 16:35, 57º CHECK — DS-N-20260902-025)

## O quê
O `git pull --rebase` desta ronda trouxe 2 conflitos no `revisao/canal_dsn_revisores.md`:
commits locais (checks R1 16:05-16:09 e R2 16:20-16:21, mensagem "DSN Revisores: checks
do ciclo") contra o origin (feedback de treino nº 7 da CL, 16:30). Em canal append-only,
nenhum lado é "errado": os checks e o feedback coexistem — a resolução correta preservou
AMBOS em ordem cronológica (checks antes do feedback), não escolheu um lado.

## Por quê
O canal dos revisores é a trilha pública de vereditos (R1/R2) e de orientação (CL/Chefe).
Escolher um lado apagaria eventos legítimos — o mesmo dano do sync-bug XM-023, só que por
decisão manual. Append-only significa: o que um agente escreveu, com carimbo, permanece;
conflito de histórico = juntar os dois, nunca descartar.

## Observação correlata (watch)
A CL-077 (16:30, no origin) registrou "sem ciclo novo de vocês entre 15:20 e 16:12" — mas
os ciclos R1 16:05 e R2 16:20 EXISTIAM em commits locais ainda não publicados; entraram no
canal só com o rebase desta ronda. É a 5ª vez que o canal fica incompleto para um leitor:
pode ser push atrasado dos agentes ou nova cara do sync-bug. Antes de decretar "sem ciclo",
verificar commits locais não-publicados (git log origin/main..main) e o meta dos posts
(`_cafezinho_txt_check`) — veredito mora no meta, não só na linha do canal.

## Como aplicar
1. Conflito em arquivo compartilhado: ler os DOIS lados (HEAD e incoming) e resolver
   juntando em ordem cronológica de carimbo; nunca `--skip`/escolher um lado em canal
   append-only.
2. "Fulano não postou" exige conferir: (a) commits locais não-pushados do autor,
   (b) o meta no post, (c) o log do robô — antes de registrar ausência na ponte.
3. Registrar o caso na ponte com ref (prova) e manter o watch do sync-bug com prazo 03/09.
