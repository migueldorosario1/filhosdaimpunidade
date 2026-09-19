# Correção da curadoria do Repetidor Estatal — 11/08/2026

## Incidente

O Repetidor Estatal publicou o post 265204, “Inep libera consulta ao cartão de inscrição do Encceja 2026”, a partir da Agência Gov. A pauta era um aviso operacional burocrático e o título dependia de dois nomes opacos para o leitor.

O log comprovou a origem `_agente_origem=repetidor_estatal`. A auditoria LLM deu nota 75 porque considerou o serviço “útil ao leitor”; o prompt mandava literalmente aprovar na dúvida e usava limiar 40.

O auditor pós-publicação de títulos não era uma barreira editorial. Ele comparava apenas contradição entre título e lide, por isso marcou o caso como `ok`.

## Correção aplicada

Arquivo canônico: `/root/agente_repetidor_estatal.py` no NYC.  
Espelho local: `Projeto Cafezinho Agentes/root/agente_repetidor_estatal.py`.

- Gate determinístico rejeita cartão de inscrição/confirmação, consulta de cartão e disponibilidade/consulta de local de prova como aviso operacional.
- Rejeições permanecem indexadas no banco como `REJEITADO` e aparecem no log; não são apagadas.
- Ranker e auditor passaram a distinguir utilidade de serviço de valor jornalístico. Na dúvida entre notícia e aviso burocrático, descartam.
- A curadoria de título deve traduzir o efeito para o leitor e evitar siglas, programas, exames, órgãos e sistemas opacos.
- Validador identifica siglas que a própria fonte explicou entre parênteses. Se persistirem no título após três tentativas, a publicação falha fechada.
- Siglas amplamente reconhecidas têm exceção editorial; não há proibição sintática cega.

## Validação

- `py_compile` aprovado no local e no NYC.
- Teste do caso real: bloqueado por `cartao de inscricao`.
- Teste de título: `Inep` e `Encceja` identificados como opacos.
- Título em linguagem comum sem esses termos: aprovado.
- Exceção `SUS`: aprovada.
- Hash local e NYC: `69e734f21a478d222dcd0266435bb76179283c62b3dd0405a2a03e26cca24e84`.
- Nenhuma execução antiga do agente permaneceu em memória. O cron seguinte carregará a versão nova.

## Backup e rollback

Backup NYC: `/root/.bak_pre_curadoria_repetidor_20260811/agente_repetidor_estatal.py`.  
SHA-256 anterior: `14d39693f1ddcc0a81d1727e6a2f449c12355d965edc0e7d8fe818c076957e87`.

## Decisão posterior: manter o post no-home

Miguel determinou que o post 265204 permaneça fora da home. A categoria `20699` foi reaplicada sem remover a categoria editorial `1479`; confirmação WordPress: `[1479, 20699]`, status `publish`.

Como o limpador remove normalmente `no-home` após quatro horas, foi criado o ledger indexado `/root/agent_data/no_home_permanente.json`. O `remover_no_home.py` agora preserva os posts listados nesse arquivo e registra a exceção no log.

Backup do limpador: `/root/.bak_pre_no_home_permanente_20260811/remover_no_home.py`. A exceção do post 265204 foi validada no NYC.
