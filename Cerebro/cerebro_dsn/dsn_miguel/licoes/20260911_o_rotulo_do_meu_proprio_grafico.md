# 20260911 — O rótulo do meu próprio gráfico

**O quê.** Na ronda 420ª (11/09 04:40 BRT) eu montei o histograma de exceções do incidente (BUG-208) com o comando `grep -o "^2026/09/11 0[34]:[0-9][0-9]" /var/log/nginx/error.log | sort | uniq -c` e **rotulei o resultado como «RedisException por minuto»** — mas aquele filtro **não filtrava `RedisException`**: contava **todas** as linhas de erro (FastCGI, warnings, avisos de plugin). Lido assim, o gráfico mostrava **7 exceções às 04:01, 5 às 04:02, 2 às 04:03, 7 às 04:04, 4 às 04:05** e «provava» que o meu próprio **ADENDO-2** («zero RedisException entre 03:48 e 04:05») estava errado — eu estava a um passo de publicar uma **errata falsa contra um acerto meu**. O filtro correto (`grep RedisException | grep -o "hora:minuto"`) confirma o ADENDO-2 (**0** naquela janela) e revela a série verdadeira (193 no total, batendo com o `grep -c`).

**Por quê.** É a **16ª ocorrência da família «o instrumento responde à pergunta errada»** (182·184·187·190·191·198·200·201·203·204·205·206·207·209·210). A diferença das anteriores: nas outras a ferramenta era de terceiros ou do rito; **esta era minha, feita na hora, e o erro foi de etiqueta** — o comando mediu uma coisa e o rótulo afirmou outra. Bug de instrumento com boa-fé: o número não estava errado, **estava respondendo a outra pergunta**.

**Como aplicar.**
1. **O filtro que produz o número tem de ser o filtro que assina o rótulo.** Se o cabeçalho diz «RedisException», o comando tem de conter `RedisException`.
2. **Teste de controle embutido:** rodar o mesmo comando **sem** o filtro e conferir que o total cai — se o número não muda, o filtro não está a filtrar.
3. **Antes de publicar uma errata contra um achado meu, refazer a medição com o filtro explícito.** Errata errada é pior que erro: destrói a confiança no acerto e no corretor.
4. **Desconfiar de histograma bonito demais:** um gráfico que «prova» exatamente o que eu temia merece uma segunda medição antes de virar relatório.
