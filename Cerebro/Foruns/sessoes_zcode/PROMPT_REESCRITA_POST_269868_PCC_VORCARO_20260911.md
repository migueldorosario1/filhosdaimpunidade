# PROMPT PRONTO — reescrita do post 269868 (Vorcaro × PCC × docs do STF)
# Gravado por ZCode/GLM-5.3 em 11/09/2026 ~06:55 BRT a pedido do Miguel ("grava tudo, vou mudar de sessão").
# Colar INTEIRO na sessão nova. Contexto autocontido — não depende desta sessão.

---

A missão é reescrever do zero o rascunho WordPress 269868 do Cafezinho ("Dinheiro do PCC ajudou a financiar Dark Horse", status draft — NÃO publicar; o Miguel revisa e publica).

## O caso (o que está provado nos documentos)

Documentos do Supremo Tribunal Federal (Petição 15.556, investigação-mãe da Operação Compliance Zero, relator André Mendonça) tiveram o sigilo levantado na noite de quinta-feira, 10/09/2026, e foram coletados na íntegra na madrugada de 10→11/09 (22 peças, cookie jar do portal STF). O Cafezinho teve acesso com exclusividade.

As peças encaixadas:
1. A Operação Carbono Oculto (PF) descobriu que o PCC usava supostos "créditos de carbono" como fachada para lavar bilhões.
2. Decisão de Mendonça de 01/06/2026 (antes sigilosa): a defesa de HENRIQUE MOURA VORCARO (irmão de Daniel Vorcaro) foi ao STF tentar desbloquear valores de conta de titularidade DELE na empresa REAG — alegando que o dinheiro não tinha liquidez imediata porque estava integralizado em Fundo de Investimento em Participações vinculado a créditos de carbono pendentes de realização. A PGR (manifestação e-Doc. 330) respondeu que isso diz respeito ao mérito da investigação; Mendonça negou o desbloqueio. Ou seja: a desculpa da família para a fortuna é o mesmo mecanismo que a PF descobriu para lavar dinheiro do PCC.
3. Linhas 1667-1695 dos documentos: notícia-crime detalhando que Flávio Bolsonaro negociou DIRETAMENTE com Daniel Vorcaro o repasse de US$ 24 milhões (cerca de R$ 134 milhões) para financiar o filme de propaganda "Dark Horse". Provas: mensagens no celular apreendido de Vorcaro com cobranças do senador + o documento oficializa que Flávio visitou Vorcaro na residência em São Paulo no final de 2025, durante prisão domiciliar e cautelares.
4. Flávio havia dito nas redes que o filme era financiado por "dinheiro 100% privado", sem dizer de onde vinha o dinheiro.
5. Contexto político: é a crise Mendonça × PF (afastamento do DG Andrei Rodrigues e de Leandro Almada; vista de Gilmar; plenário extraordinário 15/09).

## Diretrizes do Miguel (11/09 ~06h3x, ordem expressa — seguir TODAS)

1. LEAD DIRETO: o post começa com a revelação (dinheiro de crime organizado e de fraudador de aposentados financiando o filme dos Bolsonaro). SÓ DEPOIS, no 2º/3º parágrafo, o contexto documental: as informações estão nos documentos da Pet 15.556 cujo sigilo foi levantado na noite de 10 de setembro (10/09), e uma pesquisa do Cafezinho teve acesso com exclusividade à íntegra. A pesquisa juntou os documentos e encaixou as peças.
2. "Exclusivo" NÃO vai no título. Vai dentro do texto como "uma pesquisa do Cafezinho" (só isso).
3. EXPLICAR A REAG DE VERDADE: o rascunho atual diz "o fundo de investimentos da família" sem dizer de quem (ficou esquisito). Escrever claro: a REAG é a empresa onde está o patrimônio da família Vorcaro; os valores bloqueados eram de conta de titularidade de Henrique Moura Vorcaro, irmão de Daniel Vorcaro — e ele alegou que a fortuna estava integralizada em fundo vinculado a créditos de carbono.
4. Apagar o intertítulo ""Dark Horse": O míssil de R$ 134 milhões" — "míssil" é linguagem interna nossa, não do público. Trocar por intertítulo factual (ex.: "Os R$ 134 milhões do filme de Bolsonaro").
5. Apagar a frase "Não se trata de perseguição política." (defensiva — "quem disse que era?"). O final refaz sem essa muleta.
6. Tirar da abertura "O Brasil já sabia quem era Daniel Vorcaro" (boba) e o eco "quebra de sigilo" — o termo é LEVANTAMENTO do sigilo.
7. Trocar os links dos botões de download: hoje apontam para controle.ocafezinho.com — usar os públicos, testados HTTP 200: https://www.ocafezinho.com/wp-content/uploads/2026/09/pet15556.zip e https://www.ocafezinho.com/wp-content/uploads/2026/09/pet16662.zip
8. Título atual aprovado: "Dinheiro do PCC ajudou a financiar Dark Horse" (sem "exclusivo").
9. Manual de estilo da casa (Cerebro/Estilo/MANUAL_DE_ESCRITA_PORTAL.md): parágrafos de no máximo 2-3 frases, sem ponto e vírgula, sem travessão, sem dois-pontos no corpo, nunca abrir frase com "E,"/"Mas,", sem frase-trailer que adianta o que vem no parágrafo seguinte, número com fonte ao lado, acusação atribuída à fonte na própria frase.

## Arquivos já prontos nesta máquina (Dell)

- Post atual: /tmp/lula_sbt/pcc_post.html (versão com a correção parcial do sigilo/acesso — usar como base de fatos)
- Fonte primária REAG extraída: /tmp/lula_sbt/sig_b.txt (decisão Mendonça 01/06/26, trecho chave nas linhas 129-180)
- Documentos do STF: "/home/migueldorosario/Downloads/Antigravity Google/Outros/pautas editoriais o cafezinho/Dia a dia/2026 Set 11/pet_16662_15556_stf/" (LEIA-ME.md com o fio dos fatos completo + pet15556/ + pet16662/)
- Se /tmp tiver sido limpo, reextrair: pdftotext "pet15556/pet15556_01062026_MENDONCA_Decisao_SIG_b.pdf" outro.txt

## Ritual técnico (WordPress)

1. ANTES de editar: reler o post atual (foi reescrito por OUTRA sessão às 06:21 de 11/09 — conferir se mudou de novo: ssh cafezinho-wp 'sudo -u www-data wp --path=/var/www/ocafezinho post get 269868 --field=content').
2. Backup do conteúdo em cafezinho-wp /root/Backups/posts_editados/269868_pre_rewrite_YYYYMMDDHHMM.md.
3. Subir com wp post update POSICIONAL (arquivo, nunca --post_content=), mantendo status draft e data.
4. Registrar adendo no fórum Foruns/forum_videos_cafezinho_espelho_pt_gsn_20260911.md + linha no monitor (Cerebro/MONITORAMENTO_DE_TRABALHO.md — reler antes de gravar, há sessões concorrentes).
5. Avisar o Miguel que o rascunho foi reescrito (ele revisa e publica).
