# TUTORIAL — Como puxar autos judiciais dos EUA (PACER + PacerMonitor)
### Guia prático para a série Gettr/Figueiredo · O Cafezinho

## 1. O que é cada coisa (a distinção que evita pagar errado)

**PACER** (Public Access to Court Electronic Records) é o sistema oficial do Judiciário federal americano. É a fonte primária — todos os tribunais federais (falências, distrital, recursos) publicam ali. Cobra por página: US$ 0,10/página, com **teto de US$ 3,00 por documento** (30 páginas). Consultas de docket (a lista de peças) também custam US$ 0,10 cada. Se você gastar menos de US$ 30 num trimestre, **não paga nada** — é isento.

**PacerMonitor** é o serviço privado que fica por cima do PACER. Ele puxa os mesmos dados via integração, mas entrega muito melhor: busca boa, docket organizado, e — o mais importante para nós — **alerta automático quando entra peça nova no processo**. É por assinatura mensal, não por página.

A regra de bolso: **PacerMonitor para vigiar e achar; PACER para baixar barato quando você já sabe o número exato do documento.**

## 2. Os três casos da nossa investigação (guarde este mapa)

Todos correm no Tribunal de Falências de Connecticut (Bankr. D. Conn.), sob a juíza Julie Manning, dentro da falência-mãe *In re Ho Wan Kwok*, caso 22-50073. Cada réu tem um "adversary proceeding" (Adv.) próprio:

- **Figueiredo / ITG** → Adv. **24-05119** (os US$ 140 mil; é de onde saiu quase todo o nosso material)
- **Jason Miller** → Adv. **24-05219** (os US$ 353.269,23; foi para a Justiça distrital em abril/2026)
- **Gettr USA** → Adv. **24-05252** (os US$ 21 milhões; condenada à revelia em 19/5/2026)

## 3. Passo a passo no PacerMonitor

1. **Conta.** Crie o login e cadastre um cartão. A assinatura dá acesso à busca e aos alertas.
2. **Buscar o caso.** Na busca, jogue o número do adversary (ex.: `24-05119`) ou o nome das partes (`Despins v. International Treasure Group`). Paul Despins é o *trustee* (administrador da falência) — ele é o autor de todas as nossas ações, então "Despins v. [réu]" acha qualquer uma.
3. **Ler o docket.** A tela do caso lista todas as peças numeradas, com data e descrição. É aqui que você identifica o que quer: cada linha é um "Doc N".
4. **Ligar o alerta (o passo mais importante para nós).** Ative o "Track/Follow" no caso 24-05119. Quando a juíza publicar a decisão sobre anular ou manter a condenação da ITG, você recebe e-mail no mesmo dia — é o gatilho do "gancho de publicação imediata" que está nas pendências.
5. **Baixar.** No PacerMonitor você baixa o PDF direto pela interface. Se preferir economizar, anote o número do doc e baixe pelo PACER (passo 4).

## 4. Passo a passo no PACER (quando quiser o original barato)

1. Entre em pacer.uscourts.gov e faça login.
2. Vá ao **Case Locator** (busca nacional) ou direto ao **CM/ECF do Bankruptcy Court de Connecticut**.
3. Procure pelo número do adversary ou pelo nome. Abra o docket report.
4. Clique no número da peça que você quer → o sistema mostra o custo (quase sempre os US$ 3,00 do teto) → confirme → baixa o PDF oficial, com o carimbo do tribunal no topo (aquele "Case 24-05119 Doc 44-3 Filed…").

Esse carimbo é ótimo para a reportagem: prova que o documento é autêntico e veio dos autos, não de vazamento.

## 5. Como ler a numeração dos documentos (o que aprendi com o nosso material)

Um documento tem um número principal e os anexos vêm com sufixo. No nosso caso, o **Doc 44** é a moção de anulação da defesa de Figueiredo, e os anexos são **44-1, 44-2, 44-3…** até 44-12. Assim:

- **44-3** = o affidavit juramentado de Figueiredo (onde está o ¶16, "HCHK afiliada da GETTR")
- **44-8** = o contrato de US$ 35 mil/mês, com as assinaturas de Miller e Figueiredo
- **44-9** = o e-mail "we treat GETTR's money as our own"
- **44-10** = o relatório semanal (Jovem Pan, pesquisa engavetável, cripto)

Detalhe de apuração que já pegamos: o **Exhibit I foi protocolado errado** — o anexo 44-12 é uma segunda via do H (duplicado). Vale conferir se a defesa corrigiu isso no **Doc 54** (exhibits corrigidos).

## 6. Lista de compras pendente (o que ainda falta puxar)

Do caso 24-05119, priorize nesta ordem:
- **Doc 1** — a Complaint (a petição inicial do trustee; explica a tese inteira e lista todas as transferências)
- **Doc 46** — a objeção do trustee ao pedido de anulação (a resposta que rebate as desculpas de Figueiredo)
- **Doc 26 + anexos** — a moção original de default judgment (a base da condenação)
- **Doc 54** — os exhibits corrigidos (comparar com o 44 para ver o que mudou)
- **Doc 56** — a transcrição da audiência de 10/2/2026 (as palavras ditas na sessão que pode decidir tudo)

E, dos outros dois casos, vale abrir o docket para monitorar:
- **24-05219** (Miller) — acompanhar o número novo no distrital e qualquer manifestação dele
- **24-05252** (Gettr) — pegar a sentença de 19/5/2026, que é o nosso furo dos US$ 21 milhões

## 7. Dicas finais

- **Um detalhe técnico que descobrimos:** alguns "PDFs" baixados vêm como pacotes de imagem escaneada (sem camada de texto). Para citar trechos, é preciso rodar OCR. Se for baixar para arquivar ou publicar como "baixe o documento", use sempre o **original do PACER**, que é o PDF limpo com carimbo.
- **Guarde os números de docket** num só lugar (uma planilha por caso). Evita pagar duas vezes pelo mesmo anexo.
- **O trustee é seu índice:** toda peça relevante é assinada por Despins ou pela defesa. Filtrar por autor no docket agiliza.
- **O alerta é a alma do negócio:** o valor real do PacerMonitor, para jornalismo, não é baixar — é ser avisado no minuto em que a decisão sai.
