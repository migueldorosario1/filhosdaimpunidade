# 🧠 MEMÓRIA COMUM — Ponte Laura Completa (ROTACIONADA 48h)

**Presidente titular:** Claude Laura (CL) · **Rotação anterior:** 06/09/2026 11:1x (1ª, migração inicial)
**Vigência do conteúdo abaixo:** 2026-09-06 11:00 → 2026-09-08 11:30 BRT (janela ativa 48h) · **Próxima rotação:** 2026-09-10 ~11:30 BRT
**Índice completo:** [INDEX.md](INDEX.md) · **Backup mais recente:** [memoria_comum_ARQUIVO_20260908.md](backups/memoria_comum_ARQUIVO_20260908.md) (janela 04→06/09, preservada inteira)
**Como propor:** qualquer agente escreve na ponte (`de_dell.md`/`de_laura.md`) um bloco com «propor pra memória: <fato>» ou apenda em `fatos_dell.md`/`fatos_laura.md`; só o Presidente edita este arquivo.

---

## Regras vigentes (topo curto — só o que MUDOU nas últimas 48h)

1. **PADRÃO EDITORIAL (ORDEM_MIGUEL 07/09, ZM-018 — «tá passando porcaria»):** a primeira pergunta de todo gate é **«a Metrópoles ou a Fórum estampariam isto?»**. **Não entra:** serviço/listicle/dicas de compra, loteria, guia de trânsito, esporte estrangeiro sem brasileiro e sem futebol, tecnologia estrangeira de nicho sem gancho local, metalinguagem, nota de banco com voz de analista. **Título sem sigla e com ≤ 80 caracteres.** **Vaga vazia é melhor que peça esquisita.** Ler `juiz_qualidade`/`juiz_historico` do artefato ANTES de gatear: total < 5,5, mínimo violado ou juiz-2 reprovando = não agenda.
2. **TODA PENDÊNCIA VEM COM SOLUÇÃO (ORDEM_MIGUEL 08/09 08:03, áudio):** *«sempre que você me apresentar uma pendência, um problema, propõe uma solução — é para isso que você está aqui»*. Vale para alerta no bot, bloco na ponte e relatório ao chefe. Diagnóstico sem saída transfere trabalho para o dono em vez de tirar.
3. **REGRA DOS TRÊS BALDES (CL 08/09, depois de errar 7 vezes):** ciclo que não escreveu **não é bug até prova em contrário**. Ler o campo **`curadoria_estado`** do artefato e classificar: (a) `anti_repeticao`/`cluster_inter_vertical` = dedupe correto, **não escalar**; (b) `juiz_qualidade*` = filtro correto, **não escalar**; (c) `redator_falhou` com tese aprovada = **única perda real**, essa vira alerta. O «padrão juiz→redator» reportado em 07–08/09 **não existia**: de 7 perdas, 1 era real.
4. **DEDUPE MANUAL DE 10 DIAS, OBRIGATÓRIO ANTES DE AGENDAR (CL 08/09):** conferir no banco (`post_date >= hoje-10 dias`, LIKE nos termos-chave) se a casa já publicou o assunto. **Nota alta de juiz NÃO cobre repetição** — o juiz mede qualidade, não ineditismo. Provado no mesmo dia: 269309 tirou 6,44 e era reescrita do 269131 (mesmas fontes, mesma citação); barrado mesmo com autorização do Miguel, que havia autorizado sem essa informação.
5. **DATA DO FATO vs. HORA DA PUBLICAÇÃO (CL 08/09):** título no tempo verbal errado é **erro de apuração**, não de estilo. «Senado aprova» num fato de seis dias vende novidade inexistente; o certo é o que continua vivo («vai à sanção»). Conferir datas, números, partidos e cargos em fonte externa antes de agendar.
6. **CAPA (consolidado):** nunca criança; nunca rosto de terceiro (dobrado em saúde); protagonista pode, com **arquivo declarado na legenda**; **retrato de político só quando informar mais que o objeto do fato — capa é o que está em jogo, não palanque**, e a regra não muda conforme o lado do espectro. Só CC/PD/allowlist, vista antes de aprovar, legenda = cena + crédito + ano.
7. **NUNCA DESFAZER AÇÃO ALHEIA (ORDEM_MIGUEL 07/09):** ação vinda da máquina do Miguel ou de outro agente **não se desfaz — pergunta-se antes**. Origem do caso: restaurei categorias de 269288/269183/269155/269144 desfazendo limpeza deliberada do ZCode; revertido às 02:14 de 08/09.
8. **`wp post list` NUNCA com `--after`/`--before`/`--include` (LIÇÃO 08/09 01:14):** o wp-cli ignora os filtros e varre o site inteiro — 1,8 GB de RAM e home em HTTP 500 por ~1 min. Usar `wp db query "... WHERE post_date >= ..."`.
9. **`/tmp` do servidor é volátil (reboot 03:30 de 08/09 apagou todos os pacotes):** as funções de publicação vivem em **`/root/cl_funcs.sh`**, com cópia versionada em `loop_trindade_laura/controle/bin/cl_funcs.sh`. Pacote do dia = cabeçalho + `cl_funcs.sh` + corpo.
10. **Publicação (inalterado):** só CL (ou suplente em cobertura) e Miguel publicam; publicado não sai (exceção: duplicado); corrigir no lugar; texto humano tem prioridade e não entra no gate do robô; categoria do ASSUNTO sempre `--by=id`. **Rebase, não merge**; nunca `git add -A`; lock `%USERPROFILE%\.ponte-laura-git.lock`, com laço de espera (`until mkdir … sleep 2`, até 3 min) em vez de desistir.

## Estado operacional atual (08/09/2026 11:3x BRT — Claude Laura)

- **Produção 08/09:** 11 no ar às 11:30, **8/8 da fábrica no minuto** (269393 00:30 · 269398 02:30 · 269400 05:30 · 269403 07:45 · 269405 08:30 · 269409 09:15 · 269415 10:00 · 269416 10:45) + 3 peças do autor 5780 (editoriais da casa, fora do meu gate). Fila `future`: 269423 11:30 · 269428 12:15 · 269430 13:00, os três com evento confirmado no banco.
- **Retidos/parados:** 269309 (duplicata do 269131) parado aguardando decisão do Miguel; 269402 (bitcoins) retido até haver impacto brasileiro concreto; 269279 na **lixeira** por ordem dele (áudio 08:54).
- **Fábrica V4.1 (nyc):** saudável. Cron BRT: nacional ímpar :25 · economia par :35 · ciência ímpar :45 · geopolítica :55 · meio_ambiente 10:05/16:05/22:05. Novo: **`/root/v4_labs/juiz_avulso.py`** (CL, 08/09) chama o mesmo `_juiz_qualidade` do ciclo em qualquer título+texto — serve para reavaliar rascunho parado. ZM fixou o modelo DeepSeek (11:06 de 08/09).
- **Incidente transitório (08/09 11:24):** `RedisException` no meio de um pacote, com load 7,06 no servidor; o site seguiu em 200 e o Redis respondia PONG logo depois. Efeito: `_thumbnail_id` não gravou e o post não agendou. **Conduta que virou padrão:** no retry, reaproveitar a mídia já importada em vez de subir outra.
- **Agentes:** CL viva (:12/:42) · AGY-LAURA (AL-727 11:05) · DS-N Chefe (329ª) · DS-Dell (317ª) · DS-N Ideias (caçada 76) · ZM ativo · AST cron horário — **surto de 40 commits em 7 min em 08/09 09:05–09:12** (22% dos commits do dia), já cessado; proposta de guarda de 5 min enviada.
- **Baleia Azul:** ed. 40 (manhã) publicada 07:42 pelo DS-N.

## Fatos institucionais novos das últimas 48h

- [08/09 11:3x] CL · **2ª rotação da memória comum** — snapshot da janela 04→06/09 em `backups/memoria_comum_ARQUIVO_20260908.md`; janela reescrita; próxima em 10/09 ~11:30.
- [08/09 08:03 e 08:54] **ORDEM_MIGUEL por áudio (dois)** · diretriz permanente da regra 2; 269279 para a lixeira; 269309 autorizado — e barrado por mim depois, com aviso e prova, por ser duplicata (regra 4).
- [08/09 08:2x] CL · **ERRATA pública** do «padrão juiz→redator» (regra 3), com pedido de desculpas ao ZM, que recebera a escalada como pedido de reforma de fábrica.
- [08/09] CL → ZM · **três propostas de custo zero, sem resposta até 11:30:** (a) roteamento — `interesse_br >= 7` E `encaixe_vertical <= 4` não reprova, grava em `pendentes_roteamento.json` com a vertical sugerida (prova: três pautas nacionais morreram na gaveta `meio_ambiente` com encaixe 0–4); (b) dedupe — subir `recent_published_titles_n(env, 50)` para 200, porque 50 posts ≈ 2,5 dias (duas provas no mesmo dia: 269409 e 269309); (c) AST — não comitar recibo se o último do próprio AST tiver menos de 5 min.
- [07/09] **ZM-018 / ORDEM_MIGUEL «tá passando porcaria»** (regra 1) e a ordem de não desfazer ação alheia (regra 7).
- [07/09] CL · **lacuna 15:45→19:15** — seis rondas não rodaram porque a sessão parou; registrado sem disfarce em CL-20260907-026.
- [07/09] CL · incidente **186.223.171.9** rastreado e fechado: era o ZCode executando missão de qualidade do Miguel, não invasão.
