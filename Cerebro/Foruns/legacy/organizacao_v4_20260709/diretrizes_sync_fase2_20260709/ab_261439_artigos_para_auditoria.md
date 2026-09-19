# A/B 261439 — artigos para auditoria externa

Criado em: 2026-07-09  
Origem: fatia fina V4 de curadoria de tese  
Status: dry-run, sem publicacao real, sem WordPress, sem chamada LLM real.

## Escopo

Este arquivo existe para facilitar a leitura de Fable e GPT 5.5 Pro.

Os JSONs correspondentes tambem estao neste diretorio:

```text
v4_real_001.variant_a_original.producao.json
v4_real_001.variant_b.producao.json
ab_261439_curadoria_v4_fase_1.json
v4_real_001.curadoria.json
```

Importante:

```text
A versao A e o rascunho original que gerou o BUG-EDITORIAL-V4-001.
A versao B e uma saida deterministica de smoke test da nova curadoria.
B nao e materia final para publicar; serve para auditar se a curadoria muda a hierarquia editorial.
```

## Variante A — original sem curadoria

**Titulo:** Tarifa dos EUA vira disputa entre Lula e Flávio antes da eleição

A ameaça de novas tarifas dos Estados Unidos contra produtos brasileiros entrou de vez na disputa presidencial de 2026. O episódio colocou Lula e Flávio Bolsonaro em campos opostos, mas obrigou os dois a responder ao mesmo problema: como lidar com a pressão econômica de Washington sem parecer fraco diante do eleitor brasileiro.

Segundo a Associated Press, o governo Trump voltou a discutir uma tarifa de 25% sobre produtos brasileiros, apesar de os Estados Unidos manterem superávit comercial com o Brasil. A medida reacendeu uma tensão que já havia produzido desgaste diplomático no ano anterior, quando tarifas americanas foram associadas ao ambiente político em torno do julgamento de Jair Bolsonaro.

Flávio Bolsonaro, hoje tratado como principal nome da direita para a eleição, tentou transformar o tema em cálculo eleitoral. Em documento enviado ao Escritório do Representante Comercial dos Estados Unidos, o senador argumentou que uma nova rodada de tarifas poderia fortalecer Lula internamente. A lógica é simples: quanto mais a pressão externa parecer uma punição contra o Brasil, mais espaço o governo tem para vestir a defesa da soberania nacional.

Lula reagiu explorando exatamente esse ponto. O presidente classificou a movimentação bolsonarista como mais um gesto de submissão aos interesses americanos e voltou a dizer que não há justificativa para aumento de tarifas agora ou depois. A estratégia do Planalto é enquadrar a disputa como defesa do país, não apenas como divergência comercial.

O El País também registrou a ida de Flávio Bolsonaro a Washington para tentar convencer autoridades americanas a não impor o novo tarifaço. Na audiência, o senador pediu que os EUA não penalizassem o Brasil e sustentou que a medida acabaria beneficiando seu adversário. O jornal destacou ainda que o Pix virou um dos pontos sensíveis da discussão, já que autoridades americanas veem o sistema brasileiro como concorrente dos meios de pagamento privados.

O caso mostra como a eleição de 2026 tende a misturar política externa, soberania econômica e guerra de narrativas. Para Lula, a pressão dos EUA pode reforçar o discurso nacional. Para Flávio, o desafio é criticar o governo sem parecer aliado de uma punição contra o próprio país.

O risco para a direita é conhecido: quando uma disputa doméstica passa a depender da pressão de uma potência estrangeira, o debate muda de terreno. O tema deixa de ser apenas tarifa e passa a ser lealdade nacional.

**Fontes:** Associated Press e El País.

## Variante B — com curadoria V4 dry-run

**Titulo:** Tarifa dos EUA transforma Trump em problema eleitoral para Flávio Bolsonaro

Flávio Bolsonaro foi a Washington tentar conter uma tarifa associada ao campo político que a direita brasileira costuma tratar como aliado. Esse é o ponto que muda a matéria: a pressão de Trump contra produtos brasileiros pode virar custo econômico, reacender a pauta da soberania e entregar a Lula uma bandeira eleitoral que ele sabe usar.

Segundo a Associated Press, a administração Trump voltou a discutir uma tarifa de 25% sobre produtos brasileiros, apesar de os Estados Unidos manterem superávit comercial com o Brasil. Flávio argumentou ao USTR que a pressão tarifária poderia fortalecer Lula. A pergunta editorial, portanto, não é apenas quem venceu a troca de acusações; é por que o próprio bolsonarismo precisou pedir a Washington que não criasse um problema para sua campanha.

A contradição fica mais concreta quando o Pix entra na mesa. O El País registrou que o sistema brasileiro de pagamentos se tornou ponto sensível porque autoridades americanas o veem como concorrente dos meios privados de pagamento. Flávio tenta defender o Pix sem romper com a lógica de acomodação aos EUA, e Lula explora esse flanco como disputa de soberania financeira.

A consequência política é direta: a direita brasileira descobre que alinhamento externo tem custo quando a potência aliada transforma disputa política em tarifa contra o país. Lula tenta ocupar o lugar de defensor do interesse nacional; Flávio tenta impedir que a própria referência internacional da direita entregue esse terreno ao adversário.

**Fontes:** Associated Press e El País.

## Dados de auditoria

```text
curadoria_id: cur_63d2d34a351a7e9c
post_id laboratorio: 261439
item_id: v4_real_001
modo: dry_run_ab_261439
external_publish: false
real_wordpress_draft: false
```

## Pergunta para os auditores

O objetivo nao e escolher qual texto publicar. O objetivo e responder:

```text
1. A curadoria fez a variante B ter tese mais clara que A?
2. O contrato tecnico agora impediria outro texto correto, mas obvio e sem tese?
3. Que ajuste precisa entrar antes de usar redator LLM real/super_luxo?
```
