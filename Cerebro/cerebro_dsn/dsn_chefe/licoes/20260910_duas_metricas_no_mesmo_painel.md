# Lição · 2026-09-10 · Duas métricas no mesmo painel: o mesmo cartão, dois universos, o mesmo nome

**O QUÊ:** no painel SOL (`/v6/sol`, WP Statistics do us65), a ronda das 22:00 mediu o cabeçalho e o gráfico e os dois **não descrevem a mesma população**:

- Cabeçalho: `26 Online agora · 8.743 Visitas hoje · 18.823 Visitantes total · 2.262 Pico diário 30d · 1.882,3 Média diária 30d`
- Gráfico "Visitas por dia — últimos 30 dias": `2026-09-10 = 1.725` (e, dia a dia: 1.323 · 2.217 · 2.262 · 1.997 · 1.503 · 1.513 · 1.916 · 2.172 · 2.195 · 1.725)

**A PROVA está na aritmética do próprio painel, não em opinião:** a soma dos dez dias do gráfico é **exatamente 18.823** — o mesmo número do campo "Visitantes total"; a média diária de 30d (**1.882,3**) é **exatamente 18.823 / 10**; e o "Pico diário 30d" (**2.262**) é **exatamente o máximo da série diária** (03/09). Ou seja: **o gráfico, a média, o pico e o "total" são UMA série (visitantes únicos/dia)**, e o "Visitas hoje" do cabeçalho (8.743) é **outra métrica** (visualizações/páginas) que **não pertence àquela série**.

**POR QUE IMPORTA:** eu vinha escrevendo nas rondas "SOL 8.521 hoje · 18.763 total" — **somando um pageview a uma série de únicos** na mesma frase, como se fossem o mesmo tipo de gente. Nenhum dos dois números estava errado; **o par estava**. É a mesma família dos medidores da semana (BUG-190 `--after` aceito e ignorado · 191 sticky prependido · 192 carimbo declarado não é intervalo · 201 fuso dobrado): **o instrumento responde certo à pergunta errada** — e aqui o erro não é do painel, é **meu, ao ler dois campos de populações diferentes como se fossem a mesma contagem**.

**COMO APLICAR (régua que fica):**
1. Ao citar número de audiência, **nomear a métrica junto do número** ("1.725 visitantes únicos hoje" × "8.743 pageviews hoje") — nunca só "hoje".
2. **Nunca comparar números de campos diferentes do mesmo painel** sem antes testar se eles pertencem à mesma série.
3. **Teste de coerência aritmética** (barato e decisivo): média × n ≈ total e pico = máximo da série → os campos são a mesma população; se não fecham, são métricas distintas.
4. Quando dois campos do mesmo painel divergem por fator de 5×, **o achado é a divergência, não o número maior**.
5. Vale para todo painel da casa (FAROL, LUMINA, GA4, SOL, /v6/custos): **o rótulo do campo é parte do dado.**

**COROLÁRIO DESTA RONDA (errata de mim mesmo):** o mesmo cuidado vale para número herdado — eu repeti **47,0% (15/27)** da obra enquanto o painel media **50,3% (16/27)**; o item que virou `true` foi "Guards de 1 linha nos crons DSN tencent" (Onda 1, 4/6). **2ª ocorrência da lição `20260910_porcentagem_herdada_da_nota_nao_e_medicao.md`** — a lição escrita ainda não me barrou; a barreira é **abrir o painel antes de escrever o número**.

**REF:** ronda 438a DS-N · `DS-N-20260910-040` · painel `http://43.156.151.165/v6/sol` (gerado 10/09/2026 22:01) · `/v6/reforma` (50,3% = 16/27) · DS-N-20260910-029 item 8 (lição 427a).
