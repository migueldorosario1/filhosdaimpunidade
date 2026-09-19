# Forum V4 - Fase 9A curta - Prova de retorno do 007 - 2026-07-10

## Decisao de escopo

Depois do parecer sobre excesso de amplitude do mandato 9A-9E, a execucao foi reduzida a uma prova vertical do `v4_real_007`:

```text
lacuna detectada
-> coleta auditavel
-> reavaliacao
-> candidatas sustentadas ou manutencao da coleta
-> parada para Claude e Miguel
```

Ciencia/IA, internacional/geopolitica e refatoracao de politica/economia nao foram iniciadas.

## Ajustes mecanicos

Os dois apontamentos menores da auditoria da Fase 8 foram implementados:

1. o check passou a se chamar `collection_request_pendencias_por_estagio`;
2. cultura e batch multi-item passaram a ler a mesma lista de 37 fontes em `v4_frozen_sources_v1.json`.

Artefatos historicos permanecem append-only e os contratos antigos mantem compatibilidade.

## Apuracao do 007

O pacote novo usa fontes oficiais do Senado e ANCINE, documentacao da Netflix e sua planilha de engajamento H2 2025. Foram materializados snapshots, hashes, datas de acesso, locators e claims permitidos.

Ficaram documentados:

- o artigo 7 do texto em tramitacao do PL 2331/2022;
- mecanismos propostos de proeminencia, busca e recomendacao;
- a descricao atribuida da personalizacao da interface Netflix;
- circulacao declarada de `Caramelo` e `Os Donos do Jogo`;
- dados agregados de catalogo da ANCINE;
- uma posicao historica da Netflix em audiencia do Senado de 2023.

Nao foi encontrado nexo que demonstre que as duas obras foram afetadas por cota, proeminencia, busca ou recomendacao.

## Auditoria adversarial e regressao

A primeira passagem atribuiu `evidence_role=objeto_ou_criador_afetado` as duas obras e obteve 4/4 requisitos. Esse resultado era um falso positivo semantico: o rotulo transformou audiencia e disponibilidade em prova de efeito.

O erro foi corrigido antes do fechamento:

- as obras agora sao evidencias de `recepcao_ou_circulacao`;
- o requisito de dois afetados voltou a faltar;
- a satisfacao desse requisito passou a exigir relacao `affected_by` com mecanismo resolvido, tipo de efeito controlado e enunciado do efeito;
- claims de regra e status foram tornados atomicos;
- o contrato foi neutralizado para aceitar os resultados A ou B;
- propostas manuais de tese ficam no source e nao atravessam o gate.

O teste adversarial que muda apenas o rótulo das duas obras nao libera mais o caso. O avaliador independente tambem reaplica a relacao e rebaixa uma proposta forjada sem ela. Isso fecha o bypass estrutural por rotulagem, sem fingir que o contrato automatiza a verificacao semantica do locator.

## Resultado final

O 007 permanece em `coleta_obrigatoria`.

```text
3/4 requisitos satisfeitos
missing=[dois_objetos_ou_criadores_afetados]
11 claims, dos quais 10 travaveis
0 candidatas emitidas
0 tese escolhida
0 redacao
0 producao
0 publicacao
human_review_required=true
issues=[]
```

O resultado demonstra a competencia central pretendida: mesmo depois de uma coleta substantiva e de tres rascunhos humanos de tese, o pipeline nao libera curadoria quando a evidencia requerida continua ausente.

## Proxima coleta possivel

Para uma nova tentativa, o pacote precisa trazer dois objetos ou criadores com evidencia verificavel de efeito concreto de destaque, busca, recomendacao, remocao, licenciamento, acesso a dados, remuneracao ou mecanismo equivalente. Views ou presenca em catalogo, sozinhas, nao bastam.

## Gate

Execucao encerrada pelo resultado B. Proximas acoes dependem de:

```text
auditoria Claude do pacote corrigido
avaliacao editorial de Miguel
decisao: coletar novamente, redefinir formalmente o requisito ou encerrar o caso
```

Fases 9B a 9E permanecem proibidas ate nova autorizacao.

## Auditoria externa concluida

Claude auditou o pacote `v4_labs_fase9a_curta_retorno_007_20260710.tar.gz`, confirmou o SHA256 `c7b0cca474ec1c5bd7c708140cd6287e3e36d888e26f960279be7102cd627db0` e aprovou a Fase 9A.

O auditor reproduziu 118/118 testes, 11 agentes, batch 3/3, Resultado B do 007 e preflight fechado apenas pela coleta. Tambem verificou a coleta contra a materia oficial viva do Senado e submeteu o guard `affected_by` a quatro ataques adversariais, todos bloqueados.

Carta formal:

```text
Cerebro/Foruns/carta_claude_auditoria_fase9a_retorno_007_20260710.md
```

A auditoria esta fechada. A decisao editorial permanece com Miguel:

```text
A = buscar evidencia individual com produtores/criadores
B = redefinir formalmente o requisito para exposicao documentada de menor confianca
C = estacionar a pauta ate novo ato concreto do PL
```

Nenhuma opcao foi escolhida neste registro. O 007 continua em `coleta_obrigatoria`, e 9B-9E continuam sem autorizacao.

## Decisao editorial provisoria de Miguel

**Registrada em:** 2026-07-10 20:00 BRT  
**Autor:** Miguel

> ok, pode ser A. Mas cuidado para não fazer nada muito definitivo que dependa de minha decisão, porque eu posso mudar de opinião.

Interpretacao operacional conservadora:

- opcao A autorizada apenas como apuracao preparatoria, reversivel e com escopo curto;
- localizar interlocutores e fontes publicas;
- preparar perguntas, matriz probatoria e minutas de contato;
- nao enviar mensagens externas sem nova confirmacao;
- nao alterar contrato, threshold, claim, `affected_by`, `collection_request` ou `estado_editorial`;
- nao reexecutar o 007 como caso suficiente antes de receber evidencia auditavel;
- Miguel pode substituir A por B, C ou outra instrucao sem exigir rollback de codigo ou dados.

O caso permanece em `coleta_obrigatoria`. Esta decisao nao autoriza 9B-9E.

## Preparacao reversivel da opcao A

Foi criada apenas a camada preparatoria, sem contato externo e sem tocar no laboratorio:

```text
Cerebro/Foruns/plano_apuracao_f9a_opcao_a_provisoria_007_20260710.md
```

A prospeccao encontrou pistas publicas atribuidas para os dois objetos:

- `Caramelo`: declaracao de Iafa Britz sobre plataforma global e campanha, mais releases oficiais da campanha;
- `Os Donos do Jogo`: declaracao de Heitor Dhalia sobre influencia da distribuicao nas escolhas da obra, mais renovacao e segunda temporada documentadas pela Netflix.

Essas pistas nao foram convertidas em claims nem em `affected_by`. O plano preserva as diferencas entre campanha, distribuicao, influencia criativa, renovacao, audiencia e causalidade algoritmica.

Estado da frente:

```text
plano=pronto
minuta=pronta_nao_enviada
outreach_enviado=false
timebox_iniciado=false
claims_alterados=false
estado_editorial=coleta_obrigatoria
```

O proximo ato externo exige nova confirmacao de Miguel.

## Envio autorizado, aguardando reautenticacao

Miguel respondeu `pode seguir`, autorizando o envio da rodada curta. O conector Gmail exigiu reautenticacao antes de revelar a conta remetente.

Nenhum contato saiu. Foram preservados:

```text
mensagens_enviadas=0
rascunhos_remotos=0
conta_alternativa_usada=false
formulario_usado=false
telefone_usado=false
timebox_iniciado=false
```

As tres mensagens finais e os destinatarios estao registrados no plano de apuracao. Apos a reconexao, a identidade do remetente deve ser conferida antes do envio. A autorizacao pode ser revogada enquanto isso sem qualquer contato externo para desfazer.

### Retry de 2026-07-11

Nova reconexao foi tentada. `gmail.get_profile` e uma verificacao neutra de labels retornaram erro interno do conector. Permanecem `mensagens_enviadas=0` e `timebox_iniciado=false`. Nao houve fallback por outra conta ou canal.

## Regra definitiva de comunicacao externa - 2026-07-11

Miguel determinou:

> emails só podem ser manuais.

Aplicacao imediata:

- V4, Codex e agentes nao enviam emails;
- nao criam drafts remotos em Gmail;
- nao autenticam nem operam caixa de email para outreach;
- podem apenas preparar minutas locais e listas de destinatarios;
- envio, follow-up e decisao de remetente pertencem exclusivamente ao humano;
- as tentativas anteriores resultaram em zero mensagens e zero drafts.

A autorizacao anterior `pode seguir` fica reinterpretada e substituida por esta regra. O plano A permanece preparatorio; seu timebox nao comeca automaticamente.
