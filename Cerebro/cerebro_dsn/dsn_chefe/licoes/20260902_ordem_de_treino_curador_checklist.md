# Lição 2026-09-02 · Executar ordem de treino como curador (DSC-042/043)

## O quê
Ordem do Miguel (DSC-042, retificada pela DSC-043): treinar os revisores R1/R2 com o feedback da CL — semear as MEMORIA_VIVA deles, atualizar a escada de busca desatualizada do R1, garantir a marca FEEDBACK_TREINO no canal, podar/validar e confirmar ao Miguel por Telegram. Execução completa na ronda 14:00 (DS-N-021, msg 120).

## Por quê
O treino precisa "pousar" no mesmo dia, e o aprendiz (robô) não autoregistra sozinho quando a própria escada de leitura dele está degradada (o R1 às 13:05-13:06 logou ok=False ×5 — pode nem ter lido o feedback). Deixar para "ver nos próximos ciclos" arrisca o treino morrer na fila. O DSC-043 corrigiu o próprio erro (memórias JÁ existem em `cerebro_dsn/dsn_revisor1|2/` — não criar duplicata em `cerebro_dsn/` raiz): quem erra, corrige na ponte.

## Como aplicar (checklist do curador)
1. Verificar se o aprendiz autoregistrou (ls licoes/ + grep VIVA por hoje) ANTES de escrever por ele — ordem só autoriza semear se não houver autoregistro em 1-2 ciclos.
2. Semear com lições LAPIDADAS (1-3 linhas, ancoradas na fonte CL-NNNN) na VIVA + arquivo licoes/AAAAMMDD_titulo.md (o quê/por quê/como aplicar) no diretório do aprendiz — nunca em cerebro_dsn/ raiz.
3. Atualizar memória desatualizada que confunde o veredito (escada do R1: GLM+web → qwen3.8-max Token Plan → brave+deepseek → deepseek estático; grok 410 fora) e cadências mortas (:01/:31 → 1x/h :05/:20, grade DSC-039).
4. Marcar no canal oficial (append-only) com a tag da ordem (FEEDBACK_TREINO) apontando onde o feedback completo vive (canal + de_laura.md).
5. Confirmar ao Miguel por Telegram DIRETO com assinatura (msg id na memória) — mesmo que o aprendiz tenha feito a parte dele.
6. Conferir a EVIDÊNCIA do sintoma antes de reportar (o DSC-043 disse "2 posts" no ciclo 13:06; o log mostrava 5 — medir > ecoar o que leram).
7. Poda/validação na ronda do Chefe; loop de curadoria é permanente (ordem DSC-042).
