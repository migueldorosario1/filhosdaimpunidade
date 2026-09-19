# Carta ao Miguel — diagnóstico e retomada da autocura de imagens V4

Miguel,

Li o fórum e abri o pacote como ele deve ser tratado: um snapshot de laboratório, separado do publicador vigente. Conferi o SHA-256 informado e trabalhei somente nessa cópia. Não tentei upload, não reexecutei os rascunhos contra serviços externos e não autorizei publicação.

A primeira conclusão é favorável ao desenho do V4. O sistema se protegeu quando precisava. A imagem aprovada do 261602 não foi repetida; o 261603 permaneceu fora da operação; candidatas frágeis foram barradas; e a ilustração de vulcão não atravessou o tribunal visual. O defeito não estava na existência do freio. Estava no que acontecia depois dele.

O pipeline sabia dizer “não”, mas registrava esse “não” de forma pobre. O adaptador visual tinha informações por candidata, porém a decisão final reduzia tudo a uma contagem de rejeições. Assim, a autocura não conseguia distinguir entre tema errado, sujeito ausente, composição ruim, elemento obrigatório faltando, elemento proibido aparecendo, identidade incerta ou falha do provedor. Sem essa distinção, tentar outra vez era quase repetir a mesma aposta.

Havia ainda um problema de identidade. O mesmo hash representava o pedido editorial e a execução concreta. Isso funcionava para reproduzir uma decisão boa, mas também podia congelar uma decisão ruim. A nova versão separa pedido, execução e tentativa. Uma imagem segura pode ser reproduzida; uma falha abre uma execução nova; e cada passo recebe seu próprio `attempt_id`.

A terceira mudança é editorial. O prompt de imagem deixa de nascer apenas do título ou de um tema genérico. Ele passa a receber a tese visual da matéria, elementos que precisam aparecer, elementos que não podem aparecer, consultas alternativas e o enquadramento. Na segunda tentativa, recebe também o laudo da primeira rejeição. Se faltaram equipes de resgate, elas entram como obrigatórias. Se apareceu um vulcão onde o assunto era terremoto, o vulcão entra como negativo explícito. Se o sujeito ficou pequeno, muda-se o enquadramento. Se o provedor falhou, registra-se a falha e tenta-se o próximo.

Implementei essa arquitetura no snapshot e deixei o contrato em estado `shadow_patch_review_required`. Os testes locais cobriram o ponto mais delicado — replay versus retry — e confirmaram que o laudo granular alimenta a geração seguinte. Foram cinco testes, todos aprovados, além da compilação dos arquivos Python modificados.

Ainda não considero a correção pronta para produção. O pacote não contém a implementação vigente de todos os módulos importados, especialmente a cascata completa de geração e os coletores externos. Por isso eu consegui testar o contrato e o comportamento do pipeline com adaptadores controlados, mas não provar a rotação real entre FAL, Ideogram e Qwen Image, nem fazer um ensaio ponta a ponta. Essa integração precisa ser o primeiro trabalho da próxima sessão.

Os seis rascunhos continuam exatamente como estavam: sem imagem aprovada. Os laudos granulares antigos não podem ser recuperados porque não foram gravados nas decisões finais. A reexecução em `draft-only` é que produzirá os novos recibos completos. Recomendo fazer isso somente depois de aplicar o patch em uma cópia, conectar o adaptador real ao novo contexto de tentativa e confirmar em mock que uma falha antiga gera uma nova decisão `.run0002.json`.

Deixei três entregas principais: a resposta canônica para o fórum, esta carta e um ZIP incremental com apenas os arquivos que alterei ou criei. O pacote também contém manifesto, diff unificado, testes e hashes, para que a mudança possa ser revisada sem confundir o snapshot com a árvore vigente.

Minha leitura final é simples: o V4 já tinha prudência; faltava memória operacional. A correção transforma a rejeição em dado para a próxima escolha, sem relaxar o tribunal visual e sem transformar autocura em upload forçado. Quando nenhuma alternativa correta existir, deixar o rascunho sem imagem continua sendo uma decisão válida.

— GPT-5.6 Pro
