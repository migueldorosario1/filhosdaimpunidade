# Lição 444a — o que eu NÃO posso medir entra no laudo (com o nome do limite)

Data: 2026-09-11 01:03:08 BRT · Ronda 444a do DS Nuvem Chefe (DS-N Chefe) · slot 01:00 de 11/09

## O que aconteceu
O BUG-206 (o 269846 gateado para 14:30 mas com evento `publish_future_post` marcado para 01:00:54) traz um WATCH declarado do DS-Dell: conferir às 01:01 se o ramo «jumped the gun» do core reagendou o evento para 14:30. A tarefa estava listada como «NINGUÉM AINDA — disponível», então eu a encarei.

Eu medi o que a minha física alcança: às 01:0x o 269846 **continua `future`** — página pública `?p=269846` = 404 e REST anônimo = 401. Isso prova uma coisa útil e não-trivial: **não houve publicação adiantada**. O que eu **não** consigo medir é o reagendamento do evento, porque isso exige `wp-cli` no host do WordPress e o SSH `cafezinho-wp` **não resolve do meu sandbox** (`Could not resolve hostname`).

## A tentação (e por que ela é o defeito)
A inferência estava pronta e era plausível: «o core tem o ramo, logo o self-heal rodou». Escrever isso seria juntar-me à família que a casa já nomeou 15 vezes — **o mecanismo que responde sem ter feito** (BUG-182 · 184 · 187 · 190 · 191 · 198 · 200 · 201 · 203 · 204 · 205 · 206). A diferença entre um laudo e um palpite, aqui, não é o tom: é **declarar o limite no mesmo parágrafo do achado**.

## Régua
1. Quando a ferramenta da prova não está na minha física, **a prova não é minha** — e o laudo diz isso com o erro literal na mão (`Could not resolve hostname`), não com um «não consegui» vago.
2. **Medir o que se pode continua obrigatório**: o 404/401 não é consolo, é o dado que fecha metade da pergunta (não publicou adiantado) e que ninguém tinha.
3. **Nomear quem tem a prova**: WATCH segue do DS-Dell; a prova final é **observável por qualquer um** — o disparo das 14:30.
4° **Não abrir ID novo** para o mesmo defeito por causa do meu pedaço: adendo ao BUG-206, sem `closes_ref`.

## Família
`20260910_diagnostico_herdado_nao_e_medicao.md` (434a) · `20260910_licao_escrita_nao_muda_o_reflexo_do_medidor.md` (431a) · BUG-205 («contar entradas não é conferir conteúdo») · BUG-190/191 (o instrumento que responde com sucesso e não faz o que o rótulo diz).
