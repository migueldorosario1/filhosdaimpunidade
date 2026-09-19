# 20260911 — Ranking de tendência não é censo: o instrumento de "o que está quente" não mede volume

**O quê (medido, ronda 456ª do DS-N Chefe, 11/09 07:0x BRT).** O `radar_atual.json` da casa (top-20 GA4 da janela móvel de 24 h) somou **250 leituras às 07:00 de hoje**, contra **3.960 no mesmo ponto de ontem** — queda de 93,7%. O contador do servidor (FAROL), na mesma janela, viu **25.706 navegações contra 31.028** (−17%) e **4.548 pessoas contra 4.731** (−4%). Os dois números não podem estar certos ao mesmo tempo. O detalhe que desempata estava no próprio radar: **de 10/09 10:00 até 20:00 ele devolveu exatamente o mesmo total (3.958), por dez horas**, enquanto a casa publicava 31 matérias — e às 00:00 de hoje resetou para 194 e refez só **+56 leituras em sete horas**, contra **+1.106** no mesmo trecho de ontem.

**Por quê.** Um instrumento que repete o mesmo total por dez horas não está medindo: está servindo o último valor bem-sucedido (cache, coleta falha ou quota). E o efeito não fica no total — fica no **ranking**: com denominador de 250 leituras, **uma leitura move a ordem da lista**; a composição das vinte mudou de 9 entradas leves contra 11 canônicas para 5 contra 15 sem que nada tivesse mudado no site. Ranking construído sobre amostra fina ordena RUÍDO.

**Como aplicar (régua de três linhas).**
1. **Instrumento de ranking responde "qual caso", nunca "quanto".** Volume se lê no contador do servidor (FAROL/SOL); o radar entra só para dizer **qual** assunto está quente.
2. **Sempre que um medidor alimentar decisão editorial, medir também a ESTABILIDADE dele**: valor idêntico por várias horas seguidas, com o mundo mudando em volta, é sintoma — não é firmeza.
3. **Permanência (segundos por leitor) sobrevive à amostra fina** — ela é média por leitor, não soma. Foi o único dado do radar que se sustentou hoje (67,8 s na porta canônica × 3,6 s na porta leve) e é o que a edição usou.

**Família:** BUG-190/191/192 (o instrumento responde com número plausível sem ter medido) + lições `20260910_duas_metricas_no_mesmo_painel.md` e `20260911_o_retry_apaga_o_incidente.md`. **Corolário para quem reporta:** antes de citar um total, perguntar qual é o denominador e há quanto tempo o número não se mexe.
