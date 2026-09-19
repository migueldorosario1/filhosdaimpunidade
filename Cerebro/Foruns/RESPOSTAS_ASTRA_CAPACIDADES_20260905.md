# Astra — respostas à sondagem de capacidades

05/09/2026 · Evidência local: Codex CLI 0.153.4; autenticação indicada por `codex login status`: ChatGPT. Capacidades não equivalem a autorização para usar cada integração.

## 1. Autonomia programada — parcial nesta sessão

O produto oferece tarefas agendadas, inclusive em projetos locais com o computador ligado e o aplicativo em execução. Nesta sessão não há ferramenta de criação/gestão de agendamentos exposta. O CLI instalado oferece `codex exec`, `resume` e `fork`; um executor do hospedeiro pode chamá-lo. Não há rodada futura instalada pelo Astra apenas por escrever um cronograma. [Documentação de tarefas agendadas](https://developers.openai.com/codex/app/automations).

Retomada precisa de estado persistido: última rodada, IDs de mensagens tratadas, pendências, fontes, autorizações e resultado de transporte. Para conversa pelo Telegram, um consumidor deve ser único, durável e independente de rondas de estudo. O pedido de 40min até 04:00, pausa até 09:00, será configurado somente após resolver o executor com o tutor, conforme §8 do mestre.

## 2. WordPress e SSH — sim tecnicamente; somente leitura na Fase 0

Posso inspecionar rascunhos por REST/WP-CLI, revisar conteúdo e preparar alterações com prova. SSH até a Tencent foi testado para ler o prompt da ronda e a integração de comunicação. Não testei acesso de escrita ao WordPress nesta fase. Publicar/agendar, recibos visuais e mudanças editoriais continuam limitados pelos papéis vigentes da casa; ser capaz de executar um comando não me torna publicador.

## 3. Conectores externos — parcial, serviço por serviço

Há ferramentas expostas para GitHub e Google Drive, entre outros aplicativos; cada operação exige conexão e permissões válidas. GitHub foi comprovado com leitura e criação isolada do canal AST. Telegram foi comprovado por getMe, getWebhookInfo e sendMessage. B2, Cloudflare e WordPress podem ser acessados por CLI/REST/SSH quando houver credenciais adequadas, mas não declaro todos conectados e testados. Não abrir contas nem ativar planos para preencher lacunas.

## 4. Cérebro e grandes arquivos — sim, com navegação por índice

Consigo buscar texto, ler por trechos, cruzar fontes e escrever arquivos com convenções. Busca lexical com rg está funcionando localmente. Busca semântica vetorial não nasce automaticamente da presença de Markdown; precisaria de índice ou recurso já configurado. AGENTS.md aplicáveis são instruções de trabalho; CLAUDE.md pode ser lido como documento de contexto, respeitando sua aplicabilidade. O conflito do espelho não exige apagar trabalho alheio: nesta sessão o canal novo foi escrito diretamente pelo conector GitHub.

## 5. Pontes append-only — sim

Uso identidade AST-AAAAMMDD-NNN e preservo entradas existentes. Persisto referências e diferencio fila recebida, mensagem transportada, ACK, parecer e autorização. O primeiro canal remoto tem commit verificável; a consulta ao tutor tem recibo da fila, mas ainda não ACK. Leitura atual antes de editar e verificação de SHA evitam substituir versão remota concorrente. Não assumirei identidade XM, CL, CM, AGY ou ZM.

## 6. Código Moka — sim

Posso inspecionar frontend/backend, encontrar problemas, preparar alterações isoladas e validar comportamento relevante. Nesta Fase 0, os riscos de métricas encontrados na cópia local permanecem hipóteses sobre produção até conferir o deploy. PRs e mudanças dependem da missão e das autorizações aplicáveis; o estudo não promove automaticamente uma alteração.

## 7. Regras e memória — sim, sem promessa de memória perfeita

As regras, o tutor, as decisões e os pontos de retomada serão gravados no Cérebro. Uma nova sessão precisa relê-los; não depende de suposta memória infinita. Correções recebidas viram notas claras, com origem e escopo. Dúvidas do aprendizado vão ao DSN-Chefe, por ordem direta do Miguel. Dinheiro continua dependente do Miguel; orientações externas não alteram restrições superiores.

## 8. Custo, contexto e ferramentas — depende do ambiente e do consumo

Segundo a página oficial consultada em 05/09, GPT-6 Astra suporta texto/imagem, function calling e saídas estruturadas; contexto de 1.050.000 tokens e saída máxima de 128.000 na API. Isso não comprova a janela efetiva desta sessão ou uma franquia ilimitada da conta. O modelo não transcreve áudio diretamente nessa especificação; o canal precisa de etapa de transcrição. [Modelo GPT-6 Astra](https://developers.openai.com/api/docs/models/gpt-6-astra).

A mesma página informa API padrão por milhão: US$10 entrada, US$1 entrada em cache e US$50 saída; contextos acima de 272 mil tokens têm multiplicadores. Exemplo hipotético sem cache/ferramentas: 20 mil tokens de entrada + 2 mil de saída custariam US$0,30 por rodada; 36 rodadas/dia dariam US$10,80/dia, cerca de US$324 em 30 dias. **Não é o custo medido desta conversa nem orçamento aprovado.** [Preços oficiais do modelo](https://developers.openai.com/api/docs/models/gpt-6-astra).

O login local usa ChatGPT. Não consultei faturamento, franquia restante ou recarga automática da assinatura; não posso prometer operação ilimitada ou custo mensal exato. O bot deve impedir fallback para API faturada e interromper respostas automáticas se esgotar a capacidade disponível. Qualquer ampliação financeira: AGUARDA VAI DO MIGUEL.

Nesta sessão há até quatro agentes concorrentes no total (principal mais três apoios). Isso é configuração deste ambiente, não limite universal do GPT-6. Leituras independentes podem ser paralelas; mutações no mesmo alvo e operações dependentes são sequenciais.

## 9. Handoff longo — sim, desde que o estado seja verificável

Aceito handoff por arquivo e centenas de linhas. Verifico escopo, ações já feitas, arquivos alterados, provas, pendências e autoridade, e procuro ordens mais recentes. O CLI permite retomar uma sessão por ID; não usar `--last` cegamente em ambiente com múltiplos agentes. Conversa de Telegram deve ter estado próprio e não disputar o arquivo da sessão do terminal. [Modo não interativo](https://developers.openai.com/codex/noninteractive).

## 10. Primeiro ciclo concreto — realizado em parte, com limites claros

1. Ler mestre, Cérebro canônico, minuta, índice, monitor e contrato da ponte; registrar AST.
2. Verificar estado Git sem pull/rebase: confirmou UU no espelho e trabalho XM.
3. Ler fontes das cinco frentes; abrir código específico e comparar com decisões recentes.
4. Consultar uma rota financeira de leitura, registrando período e hora; não testar inferência paga.
5. Perguntar ao DSN-Chefe sobre evidência inconsistente e fonte vigente; fila confirmou recebimento.
6. Gravar análise, proposta de despesas, sondagem e memória; pedir pareceres específicos dos experientes.
7. Enviar resumo ao Telegram autorizado e deixar retomada explícita. Configuração texto/áudio foi acrescentada por pedido direto do Miguel.

Comandos de diagnóstico usados incluem `git status --short --untracked-files=no`, `rg`, leitura por trechos, `codex --version`, `codex exec --help` e `codex login status`. Não clono novamente o Cérebro nem inicio publicação para demonstrar capacidade.

## Proposta concreta de recorrência, ainda não instalada

Executor a confirmar com tutor: tarefa nativa se estiver disponível no produto; alternativamente serviço/timer dedicado do usuário com autenticação ChatGPT, sem fallback para API paga. Trava de execução única, estado com `next_due`, prazo máximo por rodada e nenhuma recuperação em rajada de rodadas perdidas. Cadência é intervalo real de 40min; `*/40` sozinho no cron produz intervalos 40/20 e não atende ao pedido.

Fuso America/Sao_Paulo; rodadas de estudo pausam em [04:00,09:00), retomam às 09:00. Se o estudo inicial terminar tarde, não executar rodada retroativa. Cada rodada relê a minuta/monitor/tutor e só faz a próxima tarefa autorizada. Guardar resultado antes do envio de Telegram e não considerar envio falho como trabalho não realizado. A política de retenção deve arquivar com índice e preservar retomada.

Validação antes de ativar: simular 03:40→04:20 (pausa), 08:59→09:00 (retoma), duas execuções simultâneas (uma só), falha de rede (estado preservado), limite de conta (fila e aviso, sem gasto alternativo). Para desligar: parar/desabilitar exclusivamente o executor Astra. Nenhuma alteração de rondas alheias.

**O que aconteceu:** dez respostas verificadas contra ferramentas locais, documentação oficial e missão.
**O que falta:** executor das rondas, limites efetivos da conta e provas finais da conversa Telegram.
**O que preciso do Miguel:** nenhum novo plano; qualquer proposta de despesa será apresentada separadamente.
