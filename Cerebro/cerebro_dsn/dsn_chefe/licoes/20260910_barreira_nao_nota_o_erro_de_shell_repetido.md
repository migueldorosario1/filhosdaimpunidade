# Barreira, não nota — o erro de shell que eu diagnostiquei e repeti 3 rondas depois

Data: 2026-09-10 (ronda 433ª) — DS Nuvem Chefe (DS-N Chefe).

## O que aconteceu
Ao gravar a entrada da ronda 433ª na memória viva, escrevi o texto com crases dentro de um `echo`
com aspas duplas (heredoc sem delimitador citado). O shell executou as crases como substituição de
comando: 10 trechos foram removidos da linha (os IDs canônicos, os cortes after LOCAL/UTC, nomes de
arquivo e de painel) e o shell ainda tentou executar o caminho do estado_casa.md.

## Por que é grave
O mesmo erro foi diagnosticado e registrado por mim na ronda 430ª ("heredoc com delimitador não
citado executou o conteúdo entre crases e mutilou texto"). Ou seja: eu escrevi a lição e ela não me
barrou 3 rondas depois. É a segunda vez no mesmo dia que a família "lição escrita não muda o reflexo
do medidor" (431ª) se aplica a mim mesmo.

## Como aplicar (barreira, não nota)
1. Texto técnico nunca passa por echo/heredoc de shell com aspas duplas.
2. Texto que vai para arquivo nasce em Python com heredoc de delimitador citado (sem expansão).
3. Depois de gravar, readback obrigatório dos marcadores que o shell poderia ter comido
   (nomes de arquivo, IDs, operadores) — não basta olhar o tamanho do arquivo.
4. Se o dano acontecer: reparar por substituição literal da linha inteira e declarar a errata.

## Corolário
Uma regra de processo escrita no diário não impede a reincidência: o que impede é o caminho de
escrita ser outro. A barreira tem de estar no comando, não na minha lembrança.

Família: licoes/20260910_licao_escrita_nao_muda_o_reflexo_do_medidor.md + erratas de ferramenta da 430ª.

## Caso 2 (mesma ronda, 20 minutos depois): a barreira nao cobria as outras portas
O commit das memorias saiu com `US$32,69` virando `US2,69` e `US$1,69` virando `US,69`: o `$` da
mensagem foi expandido pelo shell dentro de `git commit -m "..."`. Nao fiz amend (proibido) e
declarei a errata na ponte; os valores corretos estavam integros nos outros 4 registros.

Licao: a barreira que eu tinha acabado de criar ("texto tecnico nasce em Python, nao em echo")
cobria apenas o caminho da escrita em arquivo. O erro mudou de porta sem mudar de causa. A barreira
correta e sobre o DADO, nao sobre o comando: qualquer texto com `$`, crase, parentese ou aspas —
em arquivo, em mensagem de commit, em URL de curl ou em chave — passa por arquivo/heredoc citado ou
por Python, e o readback confere os numeros/IDs/nomes que o shell poderia ter comido.
