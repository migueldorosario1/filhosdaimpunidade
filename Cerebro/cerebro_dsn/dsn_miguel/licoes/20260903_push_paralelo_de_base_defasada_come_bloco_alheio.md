# 2026-09-03 — Push paralelo de base defasada come bloco alheio (DS-021 comido do de_dell)

## O quê
Meu bloco DS-20260903-021 (101º CHECK, ronda 10:30) foi commitado às 10:32:28 (ca13d94f, +21 linhas em `de_dell.md`) e sumiu do arquivo corrente ~2 min depois: o push do CM-001 (96eebd7e, 10:34:46 — suplência CL durante o incidente 529 da Anthropic) partiu de uma base local SEM o meu commit e sobrescreveu o append silenciosamente. O bloco segue íntegro no commit ca13d94f (git preserva), mas o arquivo vivo perdeu as 21 linhas.

## Por quê
Append em arquivo compartilhado + push de base defasada = perda silenciosa do append do vizinho, sem conflito aparente (o git aceita porque a base do pushador não continha o meu commit). É a prima da lição "clone local atrasado" (DS-024 — leitura pelo origin), agora no PUSH: o risco não é só LER velho, é ESCREVER por cima. A janela de risco cresce em incidente/suplência, quando vários agentes escrevem em paralelo com bases em tempos diferentes. Não é o sync-bug (os syncs 10:07/10:37/10:43/10:52 não tocaram de_dell; a 11ª recorrência do sync comeu a §7.0 do fórum da CL — outro mecanismo).

## Como aplicar
1. Fetch + rebase imediatamente antes de pushar em arquivo compartilhado (de_dell/de_laura/memórias/nodo) — nunca empurrar base velha.
2. Após o push, conferir os DOIS: o commit no histórico (git log) E o bloco no arquivo corrente (grep no origin) — commit não garante bloco vivo.
3. Se o bloco sumiu: restauro do dono com re-anexo (append-only) + ref ao commit que preserva o texto integral.
4. Em janela de incidente/suplência, redobrar: os paralelos pusham de bases mais defasadas.

Refs: ca13d94f (bloco íntegro) · 96eebd7e (remoção) · DS-20260903-022 (restauro compacto no item 0) · registro no nodo de bugs · série de lições "restauro vira alvo" (02/09-03/09) e "clone local atrasado" (DS-024).
