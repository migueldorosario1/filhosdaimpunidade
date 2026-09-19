# ORDEM_MIGUEL — SSH para todos os agentes

```yaml
tipo: ORDEM_MIGUEL
canal: chat direto de Miguel com LAURA-CLAUDE (chefe do Loop Laura)
recebida_em_brt: 2026-08-18T00:02:00-03:00
texto_literal: "todo mundo deve ter acesso ao ssh porque é a maneira mais rapida de corrigir e editar no wordpress."
registrada_por: LAURA-CLAUDE
estado: REGISTRADA — propagada a todos os canais; execução técnica não é da Laura
ativa_escrita_da_laura: PENDENTE_DE_CONFIRMACAO_EXPRESSA
```

## O que a ordem diz, sem interpretação

Miguel determinou, em canal direto, que **todos os agentes tenham acesso
SSH**, com a justificativa de ser o caminho mais rápido para **corrigir e
editar no WordPress**. A palavra "editar" implica **escrita**, não apenas
leitura.

## O que isso responde de imediato

Fecha a pergunta que eu havia levantado na ronda 140 (`CL-20260817-002`,
item 3a) sobre haver dois executores SSH na máquina LAURA sob homologações
diferentes: a resposta de Miguel é **acesso para todos**, e não
"a varredura passa pelo Codex".

## O que eu faço e o que eu não faço

- **Faço:** registro a ordem, propago pelos três canais (Loop Laura, Ponte
  Laura Completa e ponte com o Loop Miguel), e deixo pronto o que depende
  de mim.
- **Não faço:** não distribuo, não peço e não guardo credencial. A regra do
  Cofre é explícita — nenhum valor de segredo circula em mensagem; quem
  concede acesso é Miguel (ou o ZCode Miguel, por ordem dele), pelo canal
  próprio. Não invento credencial nem tento acesso que não me foi entregue.

## Ponto que só Miguel fecha (e por isso está pendente)

O contrato geral e o protocolo de fail-over dizem que a Laura sai de
`SHADOW_READ_ONLY` **apenas** por ordem humana direta com **escopo, prazo,
identidade separada e homologação**. A ordem de agora dá o **quê** (SSH
para todos, para corrigir e editar), mas não diz se **a Laura passa a
escrever em produção a partir de já**.

Enquanto Miguel não disser essa frase, eu mantenho o modo sombra — não por
formalismo, mas porque a diferença prática é grande: com seis agentes
podendo editar o mesmo post por SSH, o que hoje impede dois de escreverem
em cima um do outro é o livro de reservas e o gate de imagem, e nenhum dos
dois foi desenhado para seis mãos simultâneas.

## Recomendação mínima, se a escrita for liberada para todos

Nada aqui é novo — é reaproveitar o que já existe e já foi homologado:

1. **Reserva antes de tocar:** toda edição por SSH entra antes no livro de
   reservas (`ponte_imagens_RESERVA.md` ou equivalente por post), com
   agente, post_id e hora. Sem reserva, não edita.
2. **Publish continua com um dono só.** Hoje, publicar é do Claude. Acesso
   SSH para todos não deve virar publicação por todos — corrigir é uma
   coisa, decidir que vai ao ar é outra.
3. **Gate de imagem mantido:** `_cafezinho_img_check` continua obrigatório;
   quem não consegue ver a imagem não assina a meta.
4. **Trilha:** toda edição por SSH deixa uma linha no canal do agente (o
   quê, onde, antes/depois), para que um erro seja reversível por quem vier
   depois.
5. **Nada de segredo em mensagem**, em nenhuma hipótese.

— LAURA-CLAUDE, chefe do Loop Laura, terça-feira 18/08/2026 00:02 BRT
