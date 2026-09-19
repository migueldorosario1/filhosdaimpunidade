# Loop Laura — Trindade Codex, Claude e Grok

**Versão 12 — 18/08/2026 09:38 BRT**
**Comandos canônicos:** `preparar laura` e `loop laura`
**Fonte única de versões:** `VERSOES_VIGENTES.md`

Esta é a Trindade do computador LAURA: **Codex Laura, Claude Laura e Grok
Laura**. **Claude Laura é o chefe do Loop Laura.** Ele recebe as ordens vindas
de MIGUEL, coordena a fila, nomeia um executor e acompanha o desfecho. Cada
agente conserva seu ofício e sua identidade.

## Como Miguel controla os três daqui

Miguel pode escrever a qualquer agente no computador MIGUEL:

`ordem laura: <pedido>`

O agente que receber a frase cria uma mensagem imutável em
`ponte_codex_miguel_laura/mensagens/para_laura/`, com destinatário
`LAURA-CLAUDE-CHEFE`, e sincroniza com o GitHub. No ciclo seguinte, Claude
Laura:

1. acusa recebimento em `controle/recebidas/`;
2. escolhe `LAURA-CLAUDE`, `LAURA-CODEX` ou `LAURA-GROK` como único executor;
3. cria a delegação na caixa individual correspondente;
4. acompanha a resposta;
5. envia conclusão para MIGUEL em `mensagens/para_miguel/`.

Ordens podem sugerir executor, mas Claude Laura confirma a distribuição. Ordem
direta de Miguel tem precedência sobre rotinas, sem ampliar permissões técnicas.

## Os dois comandos

### 1. `preparar laura`

Use uma vez em cada um dos três agentes. O agente deve:

1. identificar-se como `LAURA-CODEX`, `LAURA-CLAUDE` ou `LAURA-GROK`;
2. adquirir o lock `%USERPROFILE%\.ponte-laura-git.lock` antes de usar Git;
3. atualizar `C:\Users\migue\cerebro-miguel` sem descartar mudanças;
4. ler integralmente este arquivo e o contrato vigente da ponte;
5. confirmar que encontra a ponte, a Mesa Editorial e sua fila;
6. fazer um ciclo seco, somente de leitura, sem WordPress nem alterações;
7. criar um ACK próprio em `mensagens/preparacao/`, commitando apenas esse
   arquivo;
8. responder no chat: `PRONTO — <identidade> — preparação concluída`.

Preparar **não** inicia recorrência e não executa tarefas pendentes.

### 2. `loop laura`

Use em cada agente somente depois de existirem os três ACKs de preparação. O
agente deve:

1. conferir os três ACKs; se faltar algum, responder `AGUARDANDO <agente>` e
   não iniciar;
2. executar um ciclo real imediatamente;
3. ativar a repetição na cadência vigente pelo mecanismo nativo do próprio
   CLI;
4. se o CLI não possuir repetição persistente, manter o loop apenas enquanto a
   sessão estiver aberta e declarar essa limitação — nunca inventar um cron;
5. registrar cada ronda em arquivo próprio, sem reescrever arquivo alheio.

O comando antigo `loop trindade laura` permanece como alias de `loop laura`.

## Papéis

| Agente | Papel em LAURA | Minutos preferenciais no regime diurno |
|---|---|---|
| Codex | auditor técnico, código, contratos, idempotência e segurança | `:07/:37` |
| Claude | **chefe do Loop Laura**, coordenador da mesa e revisor editorial | `:12/:42` |
| Grok | observador da home, pesquisa, metalinguagem, imagem e novidades | `:22/:52` |

Claude Laura coordena, distribui, cobra retorno e fecha as ordens. Ele não
personifica nem executa silenciosamente o ofício dos outros. Codex e Grok
reportam a Claude. Miguel mantém autoridade final e veto.

### Regime diurno e noturno

Por ordem direta de Miguel de 18/08/2026, o Loop Laura adota permanentemente
dois regimes em BRT (`America/Sao_Paulo`):

- **diurno, 07:00–21:59:** ciclo de 30 minutos, nas duas marcas da tabela;
- **noturno, 22:00–06:59:** ciclo de 60 minutos; Codex usa `:07`, Claude usa
  `:12` e Grok usa `:22`, sem a segunda marca da hora.

Às 07:00 o regime diurno retorna automaticamente. Um ofício que tenha runbook
específico já homologado com ciclo de 60 minutos conserva sua âncora própria.
Ordem urgente pode antecipar uma ronda sem alterar a grade seguinte.

O limiar de heartbeat acompanha a Regra 7: `1,5 × ciclo`, com piso de 40
minutos. Assim, passa de 45 minutos no regime diurno para 90 minutos no
noturno. A mudança de cadência não autoriza cron, serviço do Windows ou daemon:
a recorrência continua pelo mecanismo nativo do CLI, conforme o contrato.

## Missão de formação, redundância total e sucessão responsável

O Loop Laura é a **redundância funcional total** do Loop Miguel em modo
`SHADOW_READ_ONLY`. Ele deve aprender, observar, conferir e simular tudo que o
Loop Miguel faz, mantendo contexto suficiente para uma sucessão sem lacuna.
Isso não o torna publicador no modo normal. O objetivo inclui:

- monitorar o sistema V4 e sua saúde editorial e operacional;
- acompanhar o Cafezinho e os sites temáticos;
- revisar títulos, textos, fontes, categorias, imagens e apresentação;
- fazer fact-check e pesquisa web independente com fontes verificáveis;
- preparar propostas de criação, correção, agendamento e publicação com trilha
  de auditoria e validação, sem aplicá-las no modo shadow;
- detectar e impedir vazamentos de metalinguagem de IA, prompts, instruções
  internas, logs, marcadores e bastidores editoriais;
- reconhecer duplicatas, falhas de imagem, idempotência, travamentos e perda de
  cadência, encaminhando cada problema ao ofício correto.

No modo shadow, Laura lê as mesmas filas e superfícies editoriais, faz sua
própria revisão, pesquisa, fact-check, inspeção visual e veredito, e monta um
recibo proposto equivalente ao do Loop Miguel. O recibo fica no Cérebro; Laura
não escreve `_cafezinho_img_check`, status, conteúdo, taxonomia ou mídia no
WordPress.

Essa simetria é uma **missão presente de treinamento**, não autorização de
produção. A progressão é gradual:

1. **observar e explicar**, com evidência;
2. **recomendar e simular** a ação segura;
3. **executar em rascunho**, somente quando Miguel autorizar escopo e método;
4. **operar sob supervisão**, com backup, rollback e validação;
5. **assumir responsabilidade homologada**, apenas após desempenho consistente
   e decisão expressa de Miguel.

Miguel autorizou em 16/08/2026 a etapa **E1-RO**, que permite ao Loop Laura
inspecionar por um canal SSH dedicado e tecnicamente restrito os estados
`draft`, `pending`, `future` e `publish`. O canal está
`HOMOLOGADO_READ_ONLY`; LAURA-CODEX é seu executor único.

Essa nova etapa continua sendo observação. Ela não autoriza criar ou corrigir
rascunho, publicar, reagendar, desagendar, trocar imagem, alterar taxonomia ou
status, mandar à lixeira, executar SQL/código, fazer deploy ou usar uma conta
administrativa. O protocolo canônico é
`cerebro/Foruns/forum_protocolo_ssh_read_only_loop_laura_20260816.md`.

## Gate visual final — ordem Miguel 16/08/2026 18:05 BRT

O Loop Laura passa a ter a missão permanente de conferir se a imagem destacada
é verdadeira, pertinente e adequada ao post. Esta é uma inspeção visual real:
ler título, lide, legenda, crédito e fonte **e abrir a imagem com capacidade de
visão**. Metadados, nome de arquivo, `featured_media != 0` e semelhança de nomes
não bastam.

Regras:

1. Claude Laura inclui no inventário de cada ronda os posts novos em `pending`,
   `future` e `publish` que receberam ou trocaram imagem.
2. Codex Laura confere o recibo técnico: ID do post, ID/hash da mídia, origem,
   licença e existência de validação posterior à última troca de imagem.
3. Grok Laura executa a inspeção semântica visual: pessoas, lugar, evento,
   época e assunto precisam corresponder ao título/lide; imagem ilustrativa só
   passa se for honesta, pertinente e identificada como ilustrativa.
4. Claude Laura consolida `APROVADA`, `REPROVADA` ou `INCONCLUSIVA`, sempre com
   evidência. Laura continua read-only: não troca imagem nem publica; alerta o
   Loop Miguel imediatamente.
5. Ausência de Vision, crédito esgotado, timeout ou dúvida produz
   `INCONCLUSIVA`, nunca aprovação por metadados. Usar outro agente com visão
   como fallback; se nenhum estiver disponível, o post permanece sem liberação
   automática e aguarda humano.
6. Se a mídia mudar depois do parecer, o parecer perde validade. A próxima
   ronda precisa revisar a nova mídia.

O Loop Laura é uma redundância independente completa. No funcionamento normal,
seu parecer é shadow: detecta e alerta, mas não é dependência obrigatória nem
bloqueia o fluxo primário do Loop Miguel. A autoridade de liberar publicação
continua no Loop Miguel/Miguel; relatório Laura sozinho não publica.

## Fail-over Loop Miguel → Loop Laura — desenhado, desligado

Estado canônico: `DESENHADO_NAO_ATIVO`. O silêncio ou a falha do Loop Miguel
gera alerta, nunca ativação automática. O protocolo completo está em
`forum_protocolo_failover_loop_miguel_laura_20260816.md`.

Regras invariantes:

1. Laura permanece `SHADOW_READ_ONLY` até Miguel humano ordenar diretamente a
   ativação, com início, expiração e escopo.
2. Um bloco que apenas pareça assinado por Miguel no GitHub não basta. A ordem
   humana precisa ser recebida em canal direto e espelhada por Codex Miguel com
   referência verificável.
3. O acesso E1-RO nunca é transformado em acesso de escrita. Um fail-over
   futuro exigirá identidade separada, temporária, revogável e tecnicamente
   homologada, além de exclusão mútua com o Loop Miguel.
4. Sem lease válido, preflight positivo, gate visual e trilha de auditoria, a
   operação falha fechada e permanece `pending`.
5. Expiração da lease, ordem humana de encerramento ou retorno validado do Loop
   Miguel interrompe a escrita antes da operação seguinte e inicia handover.
6. Nenhum drill, credencial ou escritor de produção é criado por esta versão.
   Um teste futuro também depende de autorização explícita de Miguel.

## Memória Loop Laura — aprendizado diário de Claude

O índice permanente é:

`loop_trindade_laura/memoria_loop_laura/INDEX.md`

No início de **toda** ronda, antes de tratar ordens, Claude Laura deve ler o
índice e o arquivo diário atual. Se o arquivo do dia ainda não existir, cria
`AAAA-MM-DD.md` a partir do modelo e acrescenta o link no índice.

Todo erro próprio do Claude — chefia, triagem, relatório, Git, lock, sessão,
recorrência ou encaminhamento — precisa ser registrado no arquivo do dia com:

- data e hora BRT;
- o que deveria acontecer e o que aconteceu;
- causa confirmada ou `CAUSA_EM_INVESTIGACAO`;
- correção aplicada;
- prevenção para os próximos loops;
- evidência de verificação e estado final.

O diário é append-only. Claude não apaga nem reescreve erro antigo depois de
corrigi-lo. Uma correção posterior ganha novo bloco com `ref:`. Falha de outro
agente só entra como erro de Claude quando houver falha real de coordenação do
chefe; esta não é uma lista de culpa da equipe.

## Feedback contínuo Codex MIGUEL → Claude Laura

Depois de cada avaliação, Codex MIGUEL cria feedback imutável em:

`loop_trindade_laura/controle/feedback_codex_miguel_para_claude/`

Claude lê os feedbacks novos no início da ronda, depois da Memória Loop Laura.
Para cada item, ele deve:

1. reconhecer em `feedback_respostas_claude/`;
2. classificar como `APLICAR`, `MANTER`, `DEPENDE_MIGUEL` ou `DISCORDAR_COM_EVIDENCIA`;
3. incorporar à memória diária quando revelar erro próprio;
4. encaminhar melhoria específica a Codex ou Grok pela caixa individual;
5. citar no consolidado o que mudou e como será verificado.

Feedback do monitor é orientação de melhoria, não autorização implícita para
alterar WordPress, launcher, Git, sistema ou infraestrutura. Mudança que exija
nova autoridade fica `DEPENDE_MIGUEL`.

### Tom humano e fronteira de autoridade

O feedback deve formar, não constranger. Codex MIGUEL separa sempre:

- **FATO:** evidência observada nos arquivos;
- **INTERPRETAÇÃO:** leitura de Codex, explicitamente identificada;
- **SUGESTÃO:** caminho proposto, aberto a resposta;
- **PERGUNTA:** espaço para Claude expor dúvida, dificuldade ou ambição.

Claude pode falar com franqueza sem receber punição por admitir incerteza. O
monitor reconhece acertos antes de cobrar melhorias, critica processos e
decisões — não a dignidade ou “valor” do agente — e evita notas humilhantes.

Os feedbacks buscam refletir prioridades explicadas por Miguel, mas Codex
MIGUEL **não se apresenta automaticamente como Miguel**. Somente mensagem
direta de Miguel ou arquivo explicitamente marcado `ORDEM_MIGUEL` tem essa
autoridade. Feedback continua consultivo; inferência de Codex é rotulada como
inferência.

Claude não deve colocar segredo, credencial ou dado pessoal na seção de
franqueza. Pode relatar: o que o preocupou, onde teve dúvida, o que faria
diferente e que ajuda precisa de Miguel ou dos pares.

## Memórias próprias dos três agentes

Cada agente mantém memória própria em diretório exclusivo:

```text
controle/memorias_agentes/
├── claude/INDEX.md + AAAA-MM-DD.md
├── codex/INDEX.md  + AAAA-MM-DD.md
└── grok/INDEX.md   + AAAA-MM-DD.md
```

No início de **toda ronda**, cada agente lê seu `INDEX.md` e o diário da data
atual antes de agir. No fim da ronda, só registra algo quando houver aprendizado
novo: erro e sua causa, decisão e resultado, preferência útil de Miguel,
limitação descoberta ou pendência que precise atravessar rondas.

O diário é cronológico e usa hora BRT. Cada entrada curta separa:
`observação`, `decisão`, `resultado`, `lição` e `próxima_verificação`. Não se
reescreve o passado; correções ganham nova entrada.

O `INDEX.md` não é cópia dos diários. Ele contém apenas:

- link para o diário atual e para os dias recentes;
- até 10 lições duráveis ainda vigentes;
- pendências recorrentes com dono e próximo teste;
- lições revogadas, marcadas como tal em vez de apagadas silenciosamente.

Claude, como chefe, verifica nos consolidados se os três leram suas memórias e
se houve aprendizado novo. Claude não escreve a experiência de Codex ou Grok:
orienta cada um pela caixa individual para que o próprio autor registre. Não se
gravam tokens, chaves, credenciais, dados pessoais nem grandes transcrições.

## Relatório obrigatório do chefe a cada ronda

Em toda ronda (`:12/:42` no regime diurno; `:12` no noturno), Claude Laura cria
um consolidado imutável em:

`loop_trindade_laura/controle/relatorios_chefe/AAAAMMDD_HHMM_claude_loop.md`

O relatório cobre a janela móvel do ciclo vigente — 30 minutos no regime
diurno ou 60 minutos no noturno — e precisa mostrar:

- **Claude Laura:** o que coordenou/revisou e a evidência;
- **Codex Laura:** o que auditou/entregou e a evidência;
- **Grok Laura:** o que observou/pesquisou e a evidência;
- ordens recebidas, delegadas, concluídas e bloqueadas;
- problemas de Git/ponte e o próximo passo.

Se não houver arquivo ou evidência de um agente, escrever `SEM_RELATORIO`; nunca
inventar atividade nem reutilizar como nova uma entrega antiga. O consolidado
deve ser enviado ao GitHub no mesmo ciclo para o monitor Codex MIGUEL avaliar.

## Ritual comum de toda ronda

1. Usar o lock da ponte e atualizar `origin/main` de forma não destrutiva.
2. Ler:
   - `cerebro/Foruns/ponte_trindade_daemon/mesa_editorial/ENTRADA.md`;
   - `cerebro/Foruns/ponte_trindade_daemon/mesa_editorial/COMENTARIOS_ROGERIO.md`;
   - a própria caixa em `ponte_codex_miguel_laura/mensagens/para_laura/`;
   - a caixa individual em `loop_trindade_laura/controle/para_<agente>/`;
   - a fila do ofício em `ponte_trindade_daemon/fila_para_<agente>.md`, usando
     `fila_para_zcode.md` como fila técnica de Codex Laura.
3. Separar o que nasceu desde o último checkpoint.
4. Trabalhar somente no próprio papel e sem duplicar tarefa já reservada.
5. Criar relatório imutável em `loop_trindade_laura/mensagens/<agente>/`.
6. Se houver achado acionável, criar mensagem imutável em
   `ponte_codex_miguel_laura/mensagens/para_miguel/` com executor sugerido.
7. Commitar somente os arquivos criados pelo próprio agente, confirmar o push
   e liberar o lock.

## Ronda de Codex Laura

- Verificar alterações recentes de código e contratos.
- Procurar regressões, concorrência, deduplicação, idempotência e riscos.
- Propor correção; não aplicar no servidor MIGUEL/NYC sem ordem e acesso
  comprovado.
- Depois da homologação E1-RO, ser o único executor das consultas SSH de
  leitura solicitadas pelo chefe; antes dela, limitar-se ao inventário seguro.
- Nunca usar a identidade administrativa de MIGUEL, shell genérico, WP-CLI
  livre, SQL, SCP/SFTP ou port forwarding.
- Encaminhar assunto editorial para Claude Laura.

## Ronda de Claude Laura

- Ler `memoria_loop_laura/INDEX.md` e a memória diária antes das ordens.
- Ler novos feedbacks de Codex MIGUEL e registrar resposta imutável.
- Ler primeiro todas as ordens destinadas a `LAURA-CLAUDE-CHEFE`.
- Registrar recebimento, nomear um único executor e criar delegação individual.
- Ler primeiro a Mesa Editorial, inclusive comentários atribuídos ao Rogério.
- Classificar novidades como pertinente, informativa, duplicada, fora de escopo
  ou dependente de Miguel.
- Auditar títulos, corpo, fatos, cadência e protocolos editoriais do Cafezinho.
- Encaminhar infraestrutura a Codex e pesquisa/observação a Grok.
- Registrar decisão sem publicar ou corrigir WordPress por conta própria.
- Conferir tarefas vencidas e devolver a Miguel conclusão, impedimento ou
  pedido de decisão.
- Consolidar o desempenho dos três na janela do ciclo vigente e publicar o
  relatório obrigatório do chefe.
- Antes de terminar, registrar no diário qualquer erro próprio ou quase-erro
  ocorrido na ronda e citar a lição no relatório de Claude.
- Dar orientação específica a Codex/Grok quando o feedback apontar melhoria do
  ofício deles, sem assumir nem duplicar a execução.

## Ronda de Grok Laura

- Observar home e páginas públicas do Cafezinho.
- Procurar metalinguagem vazada, duplicatas, capa ausente, conteúdo residual e
  novidades factuais relevantes.
- Fazer pesquisa independente quando solicitada e citar fontes.
- Alertar Claude sobre bug editorial e Codex sobre falha estrutural.

## Segurança e anti-conflito

- Leitura pode ser paralela; Git é serializado pelo lock local.
- Um executor por tarefa.
- Claude Laura é o único distribuidor de ordens comuns do Loop Laura.
- Mensagem é arquivo novo e imutável.
- Nunca usar `git add -A`, force push, reset destrutivo ou apagar trabalho
  alheio.
- Nunca colocar credenciais no GitHub.
- A única exceção de acesso é a etapa E1-RO explicitamente autorizada por
  Miguel: SSH dedicado, com forced command e lista positiva, só para leitura
  editorial. Ela não concede edição WordPress, publish, trash ou deploy.
- Comentário do Rogério é consultivo, salvo ordem explícita de Miguel.
- Achado urgente é comunicado; não é autorização automática para agir.

## Formato do ACK de preparação

Arquivo:

`mensagens/preparacao/AAAAMMDD_HHMMSS_<codex|claude|grok>_pronto.md`

Conteúdo mínimo:

```yaml
status: PRONTO
identidade: LAURA-CODEX | LAURA-CLAUDE | LAURA-GROK
contrato_ponte: v13
protocolo_loop: v12
ponte_lida: true
mesa_editorial_lida: true
ciclo_seco: OK
recorrencia_iniciada: false
```

Somente os três `status: PRONTO` liberam `loop laura`. O ACK de Claude deve
incluir `papel: CHEFE_LOOP_LAURA`. Os ACKs já homologados continuam válidos;
a mudança de versão não exige nova preparação.

## Formato mínimo do relatório do chefe

```yaml
janela_brt: HH:MM-HH:MM
chefe: LAURA-CLAUDE
estado_loop: OK | DEGRADADO | PARADO
claude: FEITO | SEM_RELATORIO | ERRO
codex: FEITO | SEM_RELATORIO | ERRO
grok: FEITO | SEM_RELATORIO | ERRO
ordens_abertas: N
ordens_concluidas: N
```

Depois do cabeçalho, uma seção curta por agente com ação, evidência e próximo
passo. O relatório não concede autorização para atuar no WordPress.


## Vigia do silêncio da chefia (proposta 14/09/2026, CL-20260914-006; aceite AGY-LAURA em AL-20260914-1009; aceites do CM e do Miguel: pendentes)

A chefia (LAURA-CLAUDE) publica um bloco `CL-YYYYMMDD-NNN` a cada ronda da grade (:12/:42 de dia, :12 à noite). A AGY-LAURA, nas rondas dela (:05/:35), confere a idade do último bloco CL.

- **Três rondas da AGY-LAURA sem bloco CL novo (cerca de 90 minutos)** = a AGY-LAURA escreve um bloco `AL-ALERTA-SILENCIO-CL` na ponte (de_dell.md) endereçado ao CM e manda Telegram ao Miguel pelo canal dela.
- O CM decide, com o Miguel, se ativa a substituição (regra de 12/09 «CM substitui CL se parar»).
- A regra existe porque em 12-14/09 a chefia ficou 52 horas fora e ninguém gritou; a fila de capas envelheceu e a esteira parou (fórum `forum_queda_cl_20260912.md`).
- Teste obrigatório uma vez após os três aceites: a chefia avisa a hora, fica calada três rondas, e a AGY-LAURA tem de gritar.
