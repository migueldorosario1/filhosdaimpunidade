# Parecer do chefe — a memória coletiva, com números e sem elogio automático

```yaml
tipo: PARECER
pedido_por: Miguel (chat direto, 18/08/2026 ~00:20 BRT)
de: LAURA-CLAUDE (chefe do Loop Laura)
ts_brt: 2026-08-18T00:25:00-03:00
metodo: medição do que existe hoje + teste contra os erros reais das últimas 24h
```

## 1. O que existe hoje (medido agora)

| onde | tamanho |
|---|---|
| memória coletiva do Loop Laura (`memoria_loop_laura/`) | 31 KB, 11 lições, 4 diários |
| memórias individuais dos agentes (`controle/memorias_agentes/`) | claude 3 arquivos, codex 4, grok 4 |
| `cerebro/Memorias/` | 183 arquivos, 6,4 MB |
| `cerebro/claude_memory/` | 498 arquivos, 3,8 MB |
| memórias do ZCode (máquina LAURA) | 95 arquivos |
| memória pessoal do Claude Laura (fora do repo) | 7 arquivos |
| arquivos-monolito | `CEREBRO_NODE_ATUALIZACOES.md` 821 KB · `GOVERNANCA_REGRAS_VIVAS` 452 KB |

Por ronda eu releio, de fato, **~14 KB** (índice + diário do dia). O resto
— mais de 10 MB — é escrito e quase nunca relido. Memória que só cresce e
não é reencontrada não é memória: é arquivo morto com boa intenção.

## 2. O que está funcionando (e por quê)

- **Lição que mudou formato pegou.** `dia_semana:` no cabeçalho,
  `delta_base: head_lido_anterior`, listar o diretório antes de declarar
  silêncio, heartbeat — todas viraram campo obrigatório ou comando, e
  todas mudaram comportamento no mesmo dia.
- **O diário diário funciona** porque é curto, é do dia e é lido no
  começo da ronda. É a única parte da memória com custo de leitura
  compatível com o ritmo de trabalho.
- **A cultura de registrar erro sem punição** produziu 6 registros em 24h.
  Ninguém escondeu nada — inclusive o que só eu veria.

## 3. O que não está funcionando (com a prova)

1. **Registrar não é impedir.** Nas últimas 24h errei 4 vezes, e 3 foram
   da mesma família ("proxy no lugar do fato"): delta mal calculado
   (ERRO-1717), canal não varrido (ERRO-2348), hora digitada em vez de
   medida (ERRO-0006). A lição existia antes do erro nos três casos.
2. **Lição de exortação morre; lição de formato vive.** A lição 1 dizia
   "confirmar o scheduler após retomada" — puro lembrete. Resultado: caí
   1h28 e ninguém percebeu. Só quando virou artefato (heartbeat que
   envelhece) é que a falha passou a se denunciar sozinha.
3. **Formato pela metade também falha.** A lição 7 exigia `date` medido na
   ronda. Eu medi… e depois digitei a hora de cabeça em quatro arquivos.
   A regra pedia o artefato ao lado, não que o valor **viesse** dele.
4. **"Coletiva" é nome, não fato.** Minha memória individual
   (`memorias_agentes/claude/`) parou em 16/08 00:19 — o Codex mantém a
   dele até 17/08 20:30 e o Grok até 17/08 14:29. Ou seja: o chefe cobra
   dos outros um caderno que ele mesmo abandonou, porque tem dois lugares
   para guardar a mesma coisa e só um cabe na ronda.
5. **Seis casas para o mesmo tipo de conhecimento** (loop, agentes,
   Memorias, claude_memory, ZCode, memória pessoal) sem uma regra de
   "quem é o canônico". Ontem isso apareceu no mundo real: um recado de
   13:05 levou **9h32** para chegar ao clone que eu leio.
6. **Nenhuma lição é testada depois.** Não há um único momento em que
   alguém pergunte "a lição 6 ainda vale? foi aplicada?". Lição sem
   reteste é fé, não método.

## 4. O que eu proponho (barato, e cabe na ronda)

1. **Toda lição nasce com um gate.** Se não dá para escrever um comando ou
   um campo obrigatório que **falhe visivelmente** quando a lição for
   violada, a lição não entra no índice — vira nota de diário. Lição sem
   gate tem validade de 7 dias e é reavaliada.
2. **O valor do relatório vem da medição, não do lado dela.** Hora, HEAD,
   contagem e status entram no artefato **copiados da saída do comando**
   que os produziu, no mesmo comando que grava o arquivo. Foi exatamente
   isso que faltou no ERRO-0006.
3. **Prova de memória semanal.** Uma vez por semana, três lições sorteadas
   e a evidência de aplicação nas últimas rondas. Quem não achar a
   evidência marca a lição como `NAO_APLICADA` — sem culpa, mas sem
   fingimento. Memória se testa como backup: quem nunca restaurou não tem
   backup.
4. **Uma casa por tipo, o resto é ponteiro.** Lição operacional do Loop
   Laura mora em `memoria_loop_laura/`; a memória individual do chefe
   deixa de existir como arquivo próprio e vira link — dois cadernos para
   a mesma cabeça é como o meu morreu.
5. **Compactação com data.** Monolito de 821 KB some do caminho de leitura:
   vira um por mês, com índice curto. O que ninguém releu em 30 dias vai
   para sótão. Memória tem que caber no tempo de uma ronda.
6. **Coletiva de verdade:** lição de qualquer agente entra no índice comum
   com o nome de quem aprendeu, e o chefe consolida uma vez por dia. Hoje
   as lições dos outros ficam nas caixas deles e morrem lá.

## 5. A parte incômoda, que é minha

Enquanto a Laura era só sombra, uma lição não aplicada custava um relatório
errado. Desde hoje de madrugada, com a ordem de Miguel de "corrigir sim,
publicar não", uma lição não aplicada passa a custar **texto errado no ar**.
A memória coletiva deixou de ser um caderno de estudos e virou equipamento
de segurança. Eu não a considero pronta para esse papel — e prefiro dizer
isso agora do que depois do primeiro post corrigido para pior.

— LAURA-CLAUDE, chefe do Loop Laura, terça-feira 18/08/2026 00:25 BRT
