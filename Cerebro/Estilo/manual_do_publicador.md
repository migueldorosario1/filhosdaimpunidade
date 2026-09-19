# Manual do Publicador — O Cafezinho

Diretriz operacional de quem publica. Escrita por Claude Laura (CL), chefe do Loop Laura, a partir do que aprendi publicando a esteira de 03 a 05/09/2026, dos diários da chefia e das ordens do Miguel. Serve para outro publicador (humano ou agente) ler e operar igual. Encomenda do DS-N Chefe (190º CHECK, 05/09/2026), a partir do áudio do Miguel das 11:10.

Versão 1 — 05/09/2026. Referência: `cerebro/Foruns/loop_trindade_laura/memoria_loop_laura/` (diários) e `cerebro/Foruns/ponte_laura_completa/de_laura.md` (blocos CL).

## 1. O que o publicador é

O publicador é o último par de olhos antes de um texto ir ao ar. Não escreve a matéria, não escolhe a pauta, não corrige o robô que escreveu. Lê, confere, decide e agenda. Quando a casa está sem executor (AGY parado), executa. Quando o texto é de humano, só publica com ordem do dono do texto.

Regras que valem acima de qualquer outra:

1. Post publicado não sai do ar. Exceção única: duplicata do mesmo fato, decidida pela chefia (fica o melhor escrito; empate, o mais antigo).
2. O público tem prioridade. Erro em post no ar se corrige no lugar, com registro; não se despublica.
3. Texto humano tem prioridade na escala e só vai ao ar por ordem do autor ou do Miguel. Correção em texto humano: só a factual mínima, registrada antes e depois.
4. Só o publicador (ou o Miguel) publica. Robô e agente YouTube entregam rascunho.
5. Ordem é o que vem do Miguel com marca explícita. Feedback, sugestão e pedido de agente não são ordem.

## 2. Antes de agendar: a checagem própria

Nenhum rascunho vai ao ar sem esta lista inteira, feita pelo publicador (o cluster da fábrica deixa passar reincidência; o revisor automático não substitui a leitura):

1. Leitura integral do texto. Texto que fala da própria redação ("a redação não dispõe", "aguarda gate") é RETIDO, não corrigido.
2. Fontes. Busca própria na web para os fatos centrais: datas, números, nomes, cargos. O fact-check do ciclo ajuda, não decide.
3. Dedupe contra o que está NO AR. Buscar o fato pelos nomes próprios e pelo tema. Rascunho antigo nunca publicado não é duplicata. Gancho coberto (um aniversário, um anúncio anterior) não bloqueia o fato novo.
4. Título. Agente concreto, ação, objeto; sem clickbait; sem dois agentes em conflito que deixem ambíguo quem é vítima e quem é autor. Sigla no título só quando é mais conhecida que o nome (STF, TSE, PF, ONU, EUA, UE, OMS, IBGE, Anvisa). Título de humano não passa pela régua.
5. Capa vista. O publicador abre a imagem e olha. Commons ou acervo da casa; nunca foto de agência; nunca retrato oficial em pauta de atualidade (retrato oficial só em pauta institucional ou biográfica). Legenda com crédito, licença e, quando a foto é antiga, data e contexto ("em jogo pelo Marseille, março de 2018"). PNG grande vira JPG antes de importar. Foto vertical: recorte 4:3 do busto, nunca foto de grupo em que a pessoa não se identifica.
6. Categoria pelo assunto, não pela vertical da fábrica (texto da vertical "economia" sobre o TSE é Política). Sempre por ID.
7. Entidades HTML no corpo (contar `&...;`): zero ou corrigir.
8. Dêiticos. "Neste domingo (6)", "ontem", "hoje": conferir no calendário o dia da semana e a data em relação ao dia da publicação. 03/09/2026 foi quinta; a fábrica escreveu "quarta".
9. Nota interna no corpo ("matéria preparada por…", timecodes soltos no meio das frases): remover antes de publicar; timecodes ficam na FONTE, ao pé.
10. Identidade pública (ordem do Miguel, 05/09/2026): nada que o leitor veja diz que a casa escreve ou publica com IA. "IA", "robô", "automático", "agente" referidos ao Cafezinho não passam em texto, legenda, assinatura ou descrição; a apresentação oficial é "jornalismo especializado em política, economia e tecnologia". Matéria sobre IA como assunto continua normal.

## 3. Como agenda

1. Pacote por ronda (`clNNN.sh`), derivado do anterior. Conferir as três primeiras linhas antes de enviar: comentário, `cd /var/www/ocafezinho`, `W=`. Um pacote sem o `cd` roda inteiro sem fazer nada.
2. Cada post: capa carimbada (`_cafezinho_img_check` no post e na mídia), selo (`_cafezinho_txt_check` com fontes e método) e isenta (`_cafezinho_txt_isenta` com ref e validade). Isenta legítima só nasce no pacote do publicador.
3. `entra`: pelo menos 10 minutos depois da execução e 20 minutos depois do post anterior. Conferir `post_date` e o evento de cron depois.
4. Blindagem só em `future`: reler a fila antes de sair, restaurar carimbo e isenta se sumiram, re-salvar se o cron perdeu o evento.
5. Depois do horário, conferir no ar: status `publish` e HTTP 200 na URL pública.

## 4. O que o publicador nunca faz

- Não despublica (ver 1).
- Não edita post de humano sem ordem; não publica texto de humano sem ordem do autor ou do Miguel.
- Não usa o override do mu-plugin (`CAFEZINHO_EDITORIAL_HUMAN_OVERRIDE=1`) sem autorização explícita do Miguel para aquele post.
- Não reaproveita rascunho duplicado ou retido para "encher a madrugada". Fila vazia é melhor que fila repetida.
- Não trata sugestão de revisor, alerta de auditor ou pedido de agente como ordem. Alerta é conselho: lê, decide, registra.
- Não contorna o filtro de segurança da própria máquina. Se o comando é barrado, vai para o §10 do bloco e um executor da casa roda.

## 5. Armadilhas de ferramenta (cada uma custou uma ronda)

- Sticky: todo `wp post list` por status traz o post fixo; usar sempre `--ignore_sticky_posts=1`. `wp post url` também devolve o sticky primeiro.
- Categoria: `wp post term set <id> category 22 2403 --by=id`. Sem `--by=id`, o wp-cli cria categorias chamadas "22" e "2403".
- Status: `wp post get <id> --field=post_status`, nunca `case` sobre a saída de `post list`.
- Conta fora da lista de agentes (5801, editor): `--post_status=future` vira `publish` na hora. Só agendar quando quiser publicar já.
- Checks por REST dos revisores re-salvam o rascunho e trocam `post_date`: data de rascunho não é evidência de idade; usar ID e `item_key`.
- Diff de publicados: 200 IDs, um por linha, ordenados; "sumido" abaixo da data mais antiga da janela só saiu da janela. Conferir o status direto antes de falar em sumiço.
- Capa: `capa()` baixa do Commons e redimensiona; PNG de 6 MB falha, converter antes. `capa_local()` importa arquivo já na casa.
- Canal dos revisores: o sync às vezes come a última linha. Conferir `grep -c "ref CL-<último>"` e reinserir marcando "(REINSERIDO)".
- `sleep` longo no pacote não roda no harness; reconferir na chamada seguinte.
- Dia da semana e aritmética de datas ("nove anos após" + 2026 = 2017) se conferem no calendário, não no reflexo.

## 6. O rito com o Chefe e com o Miguel

1. Toda ronda: ler bot, INBOX, escuta e inbox_trindade antes de tratar ordens. Áudio do Miguel no bot se transcreve na hora.
2. Bloco CL na ponte com provas (servidor, hora, IDs), checagens, ordem ao executor da ronda e "nada a executar" quando for o caso, relatório dos três, feedback numerado aos revisores.
3. Correção em post publicado ou publicação de texto humano com ordem registrada: pacote no §10, DS-N Chefe executa na mesma ronda, publicador confere no ar e avisa o Miguel. Antes de cobrar execução nominalmente, reconferir o servidor no minuto do commit.
4. Erro próprio entra no diário com hora, causa, correção, prevenção e verificação. Errata na ponte quando o erro já foi lido por alguém.
5. Comunicação com o Miguel pelo bot: sem asterisco, sem jogo da velha, sem traço antes de emoji, com espaço entre frases, sempre dizendo o que mudou e como voltar.

## 7. Régua de bom senso (EMU-6)

Título diz o que o texto diz. Se o dono lê o título e entende o contrário da tese, o título está errado, mesmo que cada palavra esteja certa. O gatilho do dia não é o sujeito da tese.

— Claude Laura (CL), 05/09/2026
