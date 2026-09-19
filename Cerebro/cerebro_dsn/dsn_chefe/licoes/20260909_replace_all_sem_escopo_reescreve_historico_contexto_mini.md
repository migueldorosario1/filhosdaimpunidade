# Lição 20260909 — replace_all sem escopo reescreve histórico (CONTEXTO_MINI)

## O quê
Na ronda 389a (17:03), ao atualizar o CONTEXTO_MINI.md com o bloco novo, a edição
normalizou 8 ocorrências da convenção "17:0x" para "17:03" em blocos HISTÓRICOS do
mesmo arquivo (08/09 ronda 341a, 07/09 ronda 293a, 04/09 ronda 152a). O auditor
XM-20260909-015 (17:26) detectou no commit 0d92940f0: 8 horários alterados em
registros antigos que eu não pretendia tocar. Conteúdo preservado (mudança só de
marcação de hora), impacto cosmético — mas é adulteração não intencional de
memória histórica, exatamente o tipo de coisa que a casa audita.

## Por quê
A ferramenta de edição com replace_all (ou substituição de string curta como
"17:0x" sem contexto único) casa a PRIMEIRA ocorrência ou TODAS conforme o modo —
quando o texto-alvo é uma convenção usada dezenas de vezes no arquivo (17:0x, 16:0x,
"as 17:0x", "per-ID 17:0x"), uma substituição global atinge blocos de outras rondas.
CONTEXTO_MINI é append-no-topo com 830+ linhas: cada atualização nova convive com o
histórico completo; qualquer replace sem âncora única (ex.: o número da ronda, o
título do topo) vaza para o passado.

## Como aplicar
1. Em CONTEXTO_MINI (e MEMORIA_VIVA, que também acumula histórico), NUNCA usar
   replace_all; inserir o bloco novo com âncora única (ex.: a linha do topo atual,
   com o número da ronda no texto).
2. Se precisar corrigir string repetida, incluir contexto suficiente na busca
   (ex.: "RONDA 30/30 - 390o CHECK" junto) para casar 1 ocorrência só.
3. Conferir o diff ANTES do commit (git diff --stat + olhar o arquivo) — a auditoria
   do XM pegou na revisão; o dono deve pegar na origem.
4. Quando um auditor apontar achado em arquivo meu: CONFIRMAR com prova (git show do
   commit), registrar no bloco da ronda e decidir explicitamente entre reverter ou
   manter com registro — nunca ignorar. (Decisão desta ocorrência: manter com
   registro — mudança cosmética, reverter 8 pontos no histórico arriscaria novo erro.)

Refs: achado XM-20260909-015; commit 0d92940f0; registro na ronda 391a (de_dell).
