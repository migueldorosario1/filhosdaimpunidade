# V4 — Rodada 3: ativação coordenada da equipe

**Direção:** Miguel do Rosário  
**Coordenação e auditoria:** Codex  
**Sessão:** `CODEX-V4-R3-20260718`  
**Base:** 58% concluído; 42% ainda falta.  
**Objetivo:** fechar Gate B, preparar Gate C e validar o sistema editorial e de mídia sem publicação automática.

## Regra comum e protocolo obrigatório

### Alerta permanente de identidade — Claude ≠ GLM/Ming

Sempre que qualquer ordem, relatório ou mensagem mencionar um deles, repetir a distinção:

- **Claude Code:** agente da **Anthropic**, nesta rodada integrador do Gate B. Deve assinar como `Claude Code`, com modelo/sessão reais.
- **GLM/Ming:** agente da **Zhipu AI**, identidade canônica `GLM (Ming)`, atualmente identificado como `glm-5.1 via wrapper Claude Code CLI`. O uso do wrapper/CLI do Claude **não transforma Ming em Claude Code**.
- **GLM-5.2 externo:** terceira identidade, separada de Claude Code e de GLM/Ming; não herda votos, entregas ou autoridade deles.

**ALERTA:** Claude Code e GLM/Ming são engenheiros diferentes. Não compartilhar assinatura, sessão, autoria, voto, inbox, entrega ou autorização. Em dúvida, registrar `IDENTIDADE NÃO CONFIRMADA` e parar.

Antes de agir, cada engenheiro deve:

1. responder exatamente `CHECK CHECK CHECK — R3 V4 LIDA E ACEITA`;
2. declarar `AGENTE | DATA HORA BRT | SESSÃO | ESCOPO | ARQUIVOS RESERVADOS`;
3. ler o fórum central, o painel de 58%, este fórum, o Canal Trindade e o próprio inbox;
4. publicar no Canal apenas um ponteiro curto de início; detalhes ficam no fórum/manifesto;
5. executar somente seu escopo, sem assumir tarefa alheia e sem editar arquivo reservado por outro agente;
6. não expor, copiar, imprimir ou registrar chaves/tokens; apenas nomes de variáveis podem aparecer;
7. antes de editar: backup recuperável, diff pequeno e rollback escrito;
8. proibições desta rodada: deploy, SSH, cron/systemd, WordPress vivo, publicação, mensagem externa, chamada paga ou alteração destrutiva sem autorização nova e explícita;
9. não aprovar a própria entrega; toda entrega aguarda revisão independente do Codex;
10. encerrar com `AGENTE | DATA HORA BRT | SESSÃO | RESULTADO | EVIDÊNCIA | CUSTO | RISCO | ROLLBACK | PRÓXIMO PASSO` e a frase `AGUARDANDO REVISÃO CODEX`.
11. ao concluir trabalho importante ou sprint, gravar um ponto de retomada próprio antes de declarar encerramento. O ponto deve conter data/hora BRT, agente, sessão, objetivo, estado alcançado, arquivos/evidências, decisões, pendências, bloqueios, rollback e o primeiro comando seguro para continuar.

Sem hora, sessão, evidência e custo declarado — inclusive `R$ 0 / US$ 0` — a entrega não conta. Em conflito, ambiguidade ou risco externo, registrar `PAUSA SEGURA` e comunicar. Não improvisar autorização.

### Quarto check obrigatório de encerramento

Depois de entregar e registrar o ponto de retomada, responder exatamente:

`CHECK CHECK CHECK — PONTO DE RETOMADA GRAVADO`

Informar na mesma linha o caminho do arquivo. Sem esse quarto check, trabalho importante ou sprint permanece `ENTREGUE, MAS NÃO ENCERRADO`.

## Sprint Claude Code — Anthropic — integrador do Gate B

**ALERTA DE IDENTIDADE:** você é Claude Code/Anthropic. Você não é GLM/Ming/Zhipu, mesmo quando Ming utiliza um wrapper chamado Claude Code CLI.

Missão: integrar localmente os contratos já preparados de telemetria, hard stop, adapters e mídia, sem reescrever a arquitetura.

Entregas:

- criar o plano executável prometido;
- reservar explicitamente os arquivos canônicos antes da edição;
- integrar em patches pequenos, com backup individual;
- executar regressão integral e preservar os 323 testes verdes;
- montar um único comando dry-run do canário completo, sem WordPress;
- produzir matriz de entrada/saída e rollback.

Critério: suíte verde, identidade/recibos reconciliáveis, nenhum `unknown`, nenhum efeito externo. Não executar Gate C.

## Sprint AGY — tribunal independente de telemetria e segurança

Missão: auditar a integração do Claude sem editar os mesmos arquivos.

Entregas:

- tabela campo a campo para decisão, tentativa, chamada faturável, recibo, output e custo;
- testes adversariais para duplicata, recibo ausente, hash divergente, retry e corrida;
- comprovação de hard stop por quantidade e custo;
- reconciliador limitado exclusivamente à R3;
- parecer `APROVAR`, `APROVAR COM RESSALVAS` ou `BLOQUEAR`, com evidências.

Critério: 100% da rodada nova reconciliada, zero autoria/modelo/custo desconhecido. Sem mexer em legado.

## Sprint Grok — contrato do cartum e pacote visual

Missão: transformar a decisão editorial do cartum em contrato operacional econômico.

Entregas:

- briefing estruturado pré-geração: fato central, personagens permitidos, metáfora, tom, proibições, formato social e versão para o final do texto;
- política pós-geração liberal: somente falha catastrófica bloqueia;
- esquema de proveniência/custo/modelo/prompt/arquivo;
- três prompts de cartum para fixtures distintas, sem executar geração paga;
- fallback: foto licenciada, ilustração conceitual ou `no_safe_image`;
- teste de que cartum não destacado pode entrar ao final da matéria sem contaminar o corpo com código, crédito ou instrução operacional.

Critério: custo controlável, rastreabilidade e bloqueio raro, objetivo e explicável.

## Sprint DeepSeek — auditoria editorial e jurídica da imagem

Missão: revisar de forma independente o contrato do Grok e as imagens reais candidatas.

Entregas:

- conferir licença, atribuição, pessoa retratada e relação semântica;
- separar risco jurídico/factual de mera preferência estética;
- criar lista curta de falhas catastróficas que realmente bloqueiam;
- validar que a auditoria não provoca regenerações caras por gosto;
- parecer sobre uso como destacada versus uso ao final do texto.

Critério: nenhuma licença presumida; links e datas para toda verificação externa. Pesquisa somente read-only.

## Sprint Kilo — canário geopolítico real

Missão: entregar o input imutável do único canário Gate B.

Entregas:

- completar campos exigidos pelo contrato do redator;
- corrigir editoria e remover fatos sem fonte;
- ligar cada afirmação a fonte, data e trecho sustentado;
- incluir fontes primárias e contraponto quando necessário;
- calcular SHA-256 e proibir mutação silenciosa;
- sugerir três conceitos de cartum coerentes, sem gerar imagem e sem escrever a matéria final.

Critério: input apto ao redator, triangulado, sem fonte interessada única.

## Sprint Kimi 3 — qualidade humana do texto

Missão: atuar como tribunal editorial do canário, sem gerar nova matéria e sem chamada paga.

Entregas:

- aplicar os critérios já extraídos dos 26 testes existentes;
- avaliar título, subtítulo, lide, novidade, fluidez, análise, voz jornalística e sinais de texto artificial;
- propor somente mudanças externas e versionáveis nas diretrizes, sem hardcode;
- marcar cada achado como factual, estrutural ou estilístico;
- emitir `APTO_PARA_REDATOR` ou `BLOQUEADO`, com razões reproduzíveis.

Critério: não completar fatos, não reescrever o texto inteiro e não transformar preferência pessoal em trava.

## Sprint GLM/Ming — Zhipu AI — engenheiro de falhas, fallback e autocura

**ALERTA DE IDENTIDADE:** você é GLM/Ming/Zhipu AI (`glm-5.1 via wrapper Claude Code CLI`). Você não é Claude Code/Anthropic. O wrapper é apenas a superfície de execução e não muda sua autoria.

Missão: revisar o canário como um sistema que precisa sobreviver a falhas e aprender sem agir perigosamente.

Entregas:

- mapa de falhas de texto, telemetria, mídia, fila e WordPress;
- matriz `falha → detecção → ação segura → quarentena → recuperação → evidência`;
- testar localmente, com mocks, indisponibilidade de LLM, timeout visual, mídia sem licença, recibo duplicado, custo excedido e WordPress indisponível;
- definir quando usar fallback e quando terminar em `no_safe_image` ou `PAUSA SEGURA`;
- propor relatório de aprendizado posterior sem implementar o sistema de notas, que está no backlog pós-lançamento;
- entregar kill switch e checklist de retomada para o futuro Gate C.

Critério: nenhuma autocura publica, gasta, altera diretriz editorial ou mascara erro sem autorização e evidência.

## Coordenação Codex

Codex recebe CHECKs, evita colisões, audita evidências, reexecuta testes e consolida o placar. Ordem de fechamento:

1. Claude integra localmente;
2. AGY audita telemetria;
3. Grok e DeepSeek fecham o contrato visual;
4. Kilo entrega o input e Kimi o julga;
5. GLM testa falhas e recuperação;
6. Codex decide se Gate B pode ser executado e atualiza a barra concluído/faltante.

Gate C, WordPress e publicação continuam bloqueados até nova autorização explícita.
