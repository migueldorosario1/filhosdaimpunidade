# 20260911 — O grep somou dois cabeçalhos: 1.919 posts em 12h que nunca existiram

**O quê (medido na ronda 416ª, 11/09/2026 02:33 BRT).** Na rotina de volume por REST, o comando
`curl -s -D - "...&per_page=1" | grep -i 'x-wp-total' | tr -dc '0-9'` devolveu **3h=33 · 12h=1919 · 24h=3434**.
O site publica 30-50 posts/dia; **1.919 em 12h era impossível**, e esse número ia para o relatório do Miguel.
Ancorando o filtro (`grep -i '^x-wp-total:'`) os valores corretos apareceram: **3h=3 · 6h=5 · 12h=19 · 24h=34**.

**Por quê.** A resposta traz **dois cabeçalhos com o mesmo prefixo**: `x-wp-total: N` e `x-wp-totalpages: N`.
Com `per_page=1` os dois têm o **mesmo número**, e o `grep` sem âncora casou as duas linhas; o `tr -dc '0-9'`
concatenou os dígitos das duas (**3+3=33**, **19+19=1919**, **34+34=3434**). Não houve erro, exit ≠ 0, nem
resposta vazia: **o instrumento respondeu com sucesso à pergunta errada** — 15ª ocorrência da família
(BUG-190/191/198/200/201/202/203/204/205/206) e a 4ª ronda seguida em que a checagem me salva de publicar
alarme falso (a 413ª foi o falso **seca**; esta é o falso **enchente**).

**Como aplicar.**
1. **`grep` de cabeçalho sempre ancorado** no nome completo (`^x-wp-total:`) — prefixo casa com o vizinho.
2. **O número que decide algo sai acompanhado da linha crua que o produziu** (colar o header, não só o total).
3. **Sanidade aritmética antes de escrever:** 3h ≤ 6h ≤ 12h ≤ 24h vale aqui, mas **1.919 > 34 em 24h** já
   denunciava a dupla contagem — comparar as janelas entre si pega o erro que cada janela sozinha esconde.
4. **Quando dois instrumentos discordam, a discordância é o dado** (409ª: `--format=count` × CSV; 413ª: `date -u`;
   414ª: quatro formatos do mesmo comando; 416ª: dois cabeçalhos do mesmo `curl`).

**Fecho:** o mesmo comando que mede pode somar; **a conferência custa 30 segundos e o alarme falso custa a
confiança de quem lê o relatório.**
