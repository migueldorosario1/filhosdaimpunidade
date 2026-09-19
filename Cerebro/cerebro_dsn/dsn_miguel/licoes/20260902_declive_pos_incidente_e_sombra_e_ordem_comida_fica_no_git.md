# 2026-09-02 — Declive pós-incidente é sombra, não tendência · e ordem comida pelo sync não se perde (o git preserva)

## O quê
Duas correções/descobertas da ronda DS-20260902-029 (68º, 18:10):

1. **Declive de 1 leitura pós-incidente é SOMBRA do incidente, não tendência.** Na DS-028 (17:31) eu registrei "declive suave do fim de tarde INICIADO" porque o FAROL tinha caído 642 (👤313 + 🤖329) contra 855/381 da leitura anterior — 30 min depois (18:00) o FAROL voltou a 843 (👤398 + 🤖445), dentro da faixa do platô da tarde (372-447). O "declive" era o aftermath do 503 das 17:12: a proteção if-carga cortou crawler (bots caíram mais: 474→329) e, passado o susto, bots e humanos voltaram. A leitura do DS-N Chefe às 17:30 ("queda pós-503") estava certa; a minha ("declive iniciado") estava apressada.

2. **Ordem comida pelo sync NÃO se perde — o git preserva.** A DSC-048 (ordem do Miguel ao DS-N Chefe: vigiar o 1º artigo ultra-luxo no ar + crítica real no Telegram) foi acrescentada ao `MONITORAMENTO_DE_TRABALHO.md` pelo commit 2af8b2ca4 (17:49:16) e REMOVIDA pelo sync 245e479a2 (17:52:16) — 8ª recorrência do sync-bug (XM-024). O conteúdo continua vivo no commit: `git show 2af8b2ca4`. Li a ordem pelo git, registrei com ref de commit e NÃO restaurei o arquivo (protocolo: recuperação = novo evento do dono).

## Por quê
1. Queda que coincide com incidente de infra recente tem explicação mais provável no incidente do que no comportamento do leitor. Anunciar tendência (declive) com uma leitura contaminada por um 503 é o mesmo erro de anunciar degrau com leitura única (lição DS-012/DS-N de 05:00 e 15:07) — só que no sentido oposto: lá era pico que não se confirmava, aqui era vale que não se confirmava. A régua é a mesma: a SÉRIE é o veredito, não o dígito.

2. O sync-bug apaga LINHAS do arquivo vivo, não do histórico. Para o vigia, o git é o cursor (3ª confirmação do dia: DSC-047 carimbo 18:05 × commit 17:44:41) e também o cofre: se a ordem existe em commit, ela não foi perdida — foi escondida do arquivo. Restaurar por conta própria = 2ª mutação = violação de append-only. O correto é: ler pelo git, registrar com ref, avisar o dono para a recuperação entrar como novo evento.

## Como aplicar
1. **Antes de anunciar declive (ou degrau):** olhar o histórico recente de infra (503/load/if-carga) na janela da leitura. Se houve incidente ≤30-40 min antes, trate a leitura como potencial sombra dele e escreva "vale pós-incidente — confirmação na próxima", não "declive iniciado". Veredito = série de 2-3 leituras na mesma direção, com o incidente já fora da janela.
2. **Sempre que um bloco de ordem (DSC-*) ou feedback sumir de um arquivo vivo:** procurar no `git log`/`git show` pelo commit que o acrescentou; registrar no relatório com a ref de commit (ex.: DSC-048 em 2af8b2ca4); NÃO editar o arquivo alheio; deixar a recuperação para o dono como novo evento append-only.
3. **Nos relatórios de audiência:** quando eu errar uma leitura (anunciei declive que não se confirmou), corrigir na ronda seguinte com a série completa — registro honesto vale mais que previsão certa.

**Ref.:** DS-20260902-028 (17:31, leitura do "declive") · DS-20260902-029 (18:10, correção) · DS-N Chefe (59º, 17:30, leitura "pós-503") · XM-20260902-024 (8ª recorrência do sync, 17:53) · commit 2af8b2ca4 (DSC-048) · CL-20260902-080.
