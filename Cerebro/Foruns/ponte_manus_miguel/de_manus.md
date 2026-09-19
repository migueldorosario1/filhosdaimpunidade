# de_manus — Manus Miguel → Loop Miguel (append-only)

Manus: append aqui. Não edite `de_dell.md`. Prefixo `MM-YYYYMMDD-NNN`.

---

## MM-20260822-001 — CHECK inicial

**Data:** 22/08/2026 (BRT)

Li a missão permanente `MISSAO_FDI_MANUS.md` e os documentos-base do repositório canônico `migueldorosario1/filhosdaimpunidade`, na ordem solicitada: `CARTA_AGENTES.md`, `PROJECT_MEMORY.md`, `CONTRATO_DE_TRABALHO.md`, `Kimi K3/MANUAL_DE_ESTILO.md` e `Kimi K3/TESE_CENTRAL.md`.

Fica registrado o entendimento operacional: o GitHub, branch `main`, é o cânone do FdI; o Drive é backup; a publicação na Vercel decorre do fluxo GitHub→Vercel; a ponte é append-only e sem segredos; mudanças na `main` não serão feitas sem autorização explícita do Miguel. Também ficam assumidos o protocolo de prova da não ficção, a regra de um assunto por capítulo, a Constituição/Manual de Estilo como referência de revisão e o fluxo copiar→colar em LLM por assinatura→trazer de volta→gravar versão, com API como exceção.

A leitura da primeira missão está concluída. Prosseguirei com os três documentos do Estúdio, os oito prompts P1–P8 e o capítulo 1, para registrar a primeira entrega nesta mesma ponte.

## MM-20260822-002 — Primeira entrega: Estúdio, capítulo 1 e site

**Data:** 22/08/2026 (BRT)  
**Escopo:** leitura dos três documentos padrão do Estúdio, dos oito Prompts de Estilo P1–P8, da Memória do Projeto e de `Kimi K3/manuscrito/01_estarei_vingado.md`; proposta editorial sem alteração no repositório do FdI.

### 1. Três lapidações concretas nos documentos e prompts

#### 1.1 Constituição — transformar “nada inventado” em protocolo de lacuna

A Constituição já determina que toda afirmação tenha dono e grau e que fato novo só entre com fonte verificada.[7] A lapidação proposta é acrescentar, ao Art. 1º ou ao Art. 10, um pequeno protocolo operacional:

> **Protocolo de lacuna.** Antes de redigir, classifique cada afirmação como documento primário, reportagem atribuída, fala registrada, alegação, defesa ou inferência. Se a fonte não estiver disponível no material de trabalho, não complete pela plausibilidade. Corte a afirmação ou registre `FONTE PENDENTE` exclusivamente no bloco de produção. A marca nunca entra no texto final.

Isso transforma uma proibição abstrata em uma decisão repetível. Também evita que a exigência de produzir entre 800 e 1.000 palavras pressione o redator a preencher o bloco com informação não comprovada.

#### 1.2 Diretriz Editorial — corrigir a tensão entre recorte e contraditório

A seção “O que não entra” diz que críticas fora da linha editorial devem ser ignoradas, mas a Constituição exige contraditório no ponto da acusação.[7] A formulação atual pode ser lida como autorização para omitir uma resposta pertinente. Sugiro substituir o trecho por:

> **O que fica fora é o que é lateral à pergunta-guia. Não fica fora, porém, a contestação relevante à acusação: ela entra no ponto exato da acusação, com verbo de atribuição e fonte correspondente. A linha editorial define o recorte; não autoriza suprimir contraditório pertinente.**

A distinção preserva a tese do livro sem transformar seleção editorial em confirmação automática da tese. Crítica lateral pode ser excluída; resposta que altera o sentido de uma acusação precisa aparecer.

#### 1.3 Cabeçalho comum dos oito prompts — acrescentar um “portão de prova” silencioso

Os oito prompts já determinam estatuto dos fatos, prova sem adjetivo, contraditório, português e extensão de 800–1.000 palavras.[7] Falta uma instrução única para impedir que o modelo trate data, cifra, causalidade e citação como equivalentes. Sugiro acrescentar ao `PROMPTS_ESTILO_PADRAO_CABECALHO`, antes da escolha do ritmo:

> **Portão de prova antes da entrega:** para cada data, número, nome de órgão, citação e relação de causa e efeito, use somente o material-fonte fornecido. Escreva como alegação ou defesa quando essa for a natureza da fonte. Se não houver sustentação, retire a frase e registre a lacuna no bloco de produção. Faça essa checagem silenciosamente e entregue apenas o texto final.

A instrução é comum aos P1–P8, mas não uniformiza a música. O ritmo continua sendo escolhido pelo prompt específico; a prova passa a ser uma camada anterior a todos eles.

### 2. Checagem do capítulo 1 contra a Constituição

**Nota geral: 6,5/10.** O capítulo tem um núcleo narrativo forte: abre com uma pergunta clara, coloca o traidor no centro, usa Silvério e Efialtes como molduras curtas e conduz o leitor até a cena da CNN. A nota cai porque a voz do narrador ainda entrega veredictos, há generalizações sem dono explícito, o contraditório não aparece no ponto de algumas acusações e o arquivo totaliza 623 palavras, abaixo da unidade de 800–1.000 palavras definida para bloco/capítulo.[7] Como o arquivo está identificado como “divisão 1/3”, o número pode ser uma decisão estrutural provisória; ainda assim, precisa ser resolvido antes de tratá-lo como unidade final.

| Artigo | Avaliação | Observação |
|---|---:|---|
| 1 — Estatuto dos fatos | 5/10 | Há cenas e datas precisas, mas “o mais famoso”, “maior traidor” e outras generalizações não têm dono ou grau explícito. |
| 2 — A prova trabalha | 4/10 | “Merece o título de maior traidor”, “tempos muito mais sinistros” e “sua sombra nunca mais saiu da história” entregam juízo antes de a prova concluir. |
| 3 — Contraditório no ponto | 4/10 | A fala de Eduardo aparece, mas não há atribuição/contraponto suficiente quando o narrador transforma a cena em condenação. |
| 4 — Precisão jurídica | 8/10 | O trecho não chama Eduardo de foragido nem afirma trânsito em julgado; convém manter essa disciplina nos blocos seguintes. |
| 5 — Números com fonte | 3/10 | 1789, quatro meses, 18 de julho, oito integrantes, 8h43 e 22 dias aparecem sem referência visível junto ao fato. |
| 6 — Tudo em português | 9/10 | A linguagem está em português; nomes próprios e CNN não constituem uso indevido de língua estrangeira. |
| 7 — Um texto, uma pergunta | 8/10 | A pergunta-guia se mantém, embora a dupla moldura histórica peça vigilância para não abrir dois assuntos. |
| 8 — Os traidores no centro | 10/10 | Silvério, Efialtes e Eduardo são tratados como mecanismo central da narrativa. |
| 9 — Molduras curtas | 9/10 | As molduras de Silvério e Efialtes são breves e funcionam como lente; a transição entre elas pode ser mais econômica. |
| 10 — Nada inventado | 5/10 | Não há como conceder nota plena sem rastrear cada data, citação e caracterização em `Fontes/`; o auditor aponta forma, não prova factual. |

A auditoria automática disponível no repositório confirma oito alertas de forma: repetições de “Silvério”, “Efialtes/persa”, “trilha”, “Brasil”, “Alexandre/Moraes” e “cenário”; dois-pontos avaliável; e uma sequência de três frases em cadência de metrônomo.[9] Esses alertas não substituem a decisão editorial, mas coincidem com os pontos abaixo.

#### As cinco correções mais urgentes

**1. Começar pelo fato, não por uma generalização sobre a memória nacional.** O início atual diz: “A memória nacional registra, infelizmente, uma quantidade enorme de traidores. O mais famoso é Joaquim Silvério dos Reis.” As expressões “infelizmente”, “quantidade enorme” e “o mais famoso” são vagas e avaliativas. Proposta: “Em 1789, Joaquim Silvério dos Reis entregou à Coroa portuguesa os companheiros da conspiração mineira. Entre eles estava o alferes Joaquim José da Silva Xavier, o Tiradentes, que recebeu a pena máxima.” A fonte histórica deve ser anexada ao bloco de produção.

**2. Retirar o veredicto “maior traidor da história do Brasil”.** O período “superou Silvério e merece o título de maior traidor” viola o princípio de que a prova trabalha e o narrador não adjetiva.[5][7] Proposta: “A comparação não terminava em Silvério dos Reis. O autor da frase tinha mandato, sobrenome e acesso ao poder. Ainda assim, passou a buscar no exterior punições contra o próprio país.” A acusação passa a ser construída pelos atos que o capítulo mostra, não por um epíteto antecipado.

**3. Trocar a absolvição/psicologização por estatuto documental.** “Sem querer desculpá-lo, sua situação era realmente vulnerável” comenta a posição do narrador e “apenas para se sentir vingado” afirma uma motivação interna. Proposta: “Silvério devia à Fazenda Real e esperava clemência em troca da delação. Eduardo Bolsonaro não estava nessa posição. Tinha mandato, acesso ao poder e recursos. A frase sobre a ‘terra arrasada’ registra o benefício que ele dizia buscar.” Se a motivação for mantida, deve vir como fala, documento ou inferência marcada, não como fato psicológico.

**4. Reescrever a moldura de Efialtes para eliminar eco e metrônomo.** O trecho “Efialtes não era persa. Era dali. Conhecia o caminho por dentro… Ele conhece a trilha” repete a mesma informação em palavras vizinhas e foi capturado pelo auditor.[9] Proposta: “Efialtes não era persa. Era dali. Mostrou ao exército invasor o caminho que contornava o desfiladeiro. Heródoto registrou o episódio no Livro VII. O invasor entrou pela geografia de um homem da terra.” A sequência preserva o golpe curto, mas troca a repetição por progressão.

**5. Dividir o parágrafo da CNN e limpar o fechamento.** O parágrafo iniciado por “A entrevista estava marcada...” reúne data, local, duração, clima, mandados, restrições e revogação de vistos em um único período longo, o que enfraquece referentes e fontes. Sugestão de abertura: “Em 18 de julho de 2025, Eduardo Bolsonaro participou de uma entrevista à CNN Brasil por videoconferência. Falava dos Estados Unidos, onde vivia havia quatro meses. Horas antes, a Polícia Federal cumprira mandados contra Jair Bolsonaro. Em Washington, Marco Rubio revogara os vistos de Alexandre de Moraes e de seus familiares.” Depois, cada fato deve receber a fonte correspondente. No fecho, trocar “Aos oito minutos e quarenta e três segundos, veio a frase:” por “Às 8h43, Eduardo completou a ideia.” A frase seguinte pode entrar diretamente entre aspas. Em “Terra arrasada. Longe de temer esse cenário...” retirar o eco e a ambiguidade: “Terra arrasada. O próprio Eduardo já celebrara aquele resultado vinte e dois dias antes.”

### 3. Uma melhoria concreta para o site

**Adicionar um selo de proveniência editorial no cabeçalho do leitor.** O site embute os defaults no `index.html`, mas mantém revisões, alterações canônicas locais e operações de capítulos no `localStorage` do navegador.[1][7] Isso cria um risco de o usuário confundir “canônica neste navegador” com “canônica no GitHub/main”.

A melhoria seria um indicador visível, em todos os capítulos, com três estados:

| Estado | Selo sugerido | Significado |
|---|---|---|
| Base publicada | `PUBLICADO · GitHub/main · Vercel` | Texto vindo do conteúdo publicado no repositório. |
| Revisão local | `R# LOCAL · NÃO PUBLICADA` | Existe revisão/alteração no navegador, ainda sem integração no GitHub. |
| Cânone local divergente | `CANÔNICA NO NAVEGADOR · DIVERGENTE DO GITHUB` | O botão “Tornar Canônica” mudou a referência local, não a fonte canônica do projeto. |

O selo deve incluir uma ação simples: **“Ver o que diverge”**, exibindo versão ativa, chave do capítulo, data local e instrução “exportar para a ponte ou abrir branch `manus/<tema>`; não há publicação automática”. A mudança é de UX e transparência, não exige mexer na Vercel nem em credenciais. Ela alinha o comportamento real do `localStorage` à governança declarada: GitHub é a verdade; navegador é estado de trabalho.

### Referências

[1]: https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Foruns/ponte_manus_miguel/MISSAO_FDI_MANUS.md "Missão FDI — Filhos da Impunidade"
[2]: https://github.com/migueldorosario1/filhosdaimpunidade/blob/main/CARTA_AGENTES.md "Carta aos agentes"
[3]: https://github.com/migueldorosario1/filhosdaimpunidade/blob/main/PROJECT_MEMORY.md "Memória e banco de dados canônico"
[4]: https://github.com/migueldorosario1/filhosdaimpunidade/blob/main/CONTRATO_DE_TRABALHO.md "Contrato de trabalho"
[5]: https://github.com/migueldorosario1/filhosdaimpunidade/blob/main/Kimi%20K3/MANUAL_DE_ESTILO.md "Manual de Estilo"
[6]: https://github.com/migueldorosario1/filhosdaimpunidade/blob/main/Kimi%20K3/TESE_CENTRAL.md "Tese Central — O Foragido"
[7]: https://github.com/migueldorosario1/filhosdaimpunidade/blob/main/index.html "Defaults do Estúdio do Estilo dentro do index.html"
[8]: https://github.com/migueldorosario1/filhosdaimpunidade/blob/main/Kimi%20K3/manuscrito/01_estarei_vingado.md "Capítulo 1 — Estarei Vingado"
[9]: https://github.com/migueldorosario1/filhosdaimpunidade/blob/main/Kimi%20K3/verifica_estilo.py "Auditor de estilo"
