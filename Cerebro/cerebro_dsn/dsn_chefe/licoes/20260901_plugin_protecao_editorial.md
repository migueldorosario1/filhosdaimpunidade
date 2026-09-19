# Lição 2026-09-01 — Plugin `cafezinho-protecao-editorial` + regra de prova (CL-035/036)

## O quê
Posts do Cafezinho publicados por HUMANO são protegidos por um plugin da casa (`cafezinho-protecao-editorial`): qualquer tentativa de edição por robô (wp-cli/REST) recebe `BLOQUEADO post=XXXX motivo=post_publicado_por_humano canal=wp_cli — Post protegido por decisão editorial humana; use apenas alerta`. Foi a causa-raiz da "falha silenciosa" do item 4 do 268534 (a AGY-L reportou readback de um update que o servidor NUNCA gravou) e do `reader_failed` do canal cafezinho-cl. Simultaneamente, a CL fixou a REGRA DE PROVA: readback = LER DE VOLTA DO SERVIDOR depois do update (`wp post get <ID> --field=post_content | grep <marcador>` ou GET REST novo), nunca ecoar o conteúdo que se PRETENDEU gravar.

## Por quê
A casa decidiu (desenho, não bug): decisão editorial humana não é contornável nem por root. E o falso sucesso é mais caro que a falha: um "executado" que não gravou vira pendência invisível (o 268534 ficou com "segunda-feira (1º)" e Leia Mais errado no ar).

## Como aplicar (na família DS-N)
1. O DS Nuvem Publicador (carteiro) e o DS Nuvem YouTube devem DETECTAR o bloqueio (ler o corpo da resposta do servidor, não só o status) e reportar `BLOQUEADO_PROTECAO` na ponte — nunca sucesso falso nem silêncio.
2. Toda prova de escrita do Publicador = GET pós-update com marcador; se o marcador não aparecer → FALHOU, reportar.
3. Não tentar contornar a proteção; o caminho é pedir exceção pontual ao Miguel ("libera a proteção do X") ou ele mesmo editar no admin (1 min).
4. Na vigília do chefe: post publicado por humano + pedido de correção = rotear para o MIGUEL, não para executor robô.

## Madura
Linha adicionada na MEMORIA_VIVA em 01/09 (ronda DS-N-133).
