# Fórum — Resumo Humano do Estado do Sistema V4

Data: 2026-07-08  
Autor: Codex  
Status: explicação para alinhamento

## 1. Por que este fórum existe

Miguel pediu uma explicação mais clara e humana sobre o que já ficou pronto no V4.

A conversa ficou muito técnica: JSONL, camadas, recibos, Prometheus, WordPress, imagem auditada, roteador de LLM, Banco Ouro, etc.

Este fórum serve para responder de forma simples:

```text
O que já existe?
O que já funciona?
O que ainda não está pronto?
Qual é o próximo passo?
```

## 2. Resumo em linguagem simples

O V4 deixou de ser só ideia.

Agora ele já tem um esqueleto funcional, com várias partes operando localmente e uma prova real de que consegue chegar ao WordPress como rascunho.

O mais importante:

```text
O V4 já consegue:
1. receber conteúdo bruto;
2. normalizar esse conteúdo;
3. promover para auditado;
4. produzir um texto em modo técnico/dry-run;
5. exigir imagem destacada auditada;
6. montar payload WordPress;
7. criar rascunho real no WordPress;
8. registrar tudo em arquivos auditáveis;
9. fazer backup no Backblaze.
```

Mas o V4 ainda não está liberado como sistema editorial automático de produção diária.

Ele está no estágio:

```text
MVP técnico funcional, validado com smoke tests e rascunhos reais.
```

## 3. O que já ficou pronto

### 3.1. Diretrizes externas

O princípio central foi implementado:

```text
Agentes não carregam diretriz editorial hardcoded.
```

As diretrizes ficam fora do código, em arquivos próprios dentro de `diretrizes/`.

Isso vale para:

- núcleo editorial comum;
- política/economia;
- cultura;
- internacional;
- ciência, tecnologia e IA;
- repetidor;
- Global South News;
- regras de LLM;
- regras de telemetria;
- regras de imagem;
- regras de WordPress;
- regras de ingestão.

### 3.2. Camadas de dados

O V4 agora tem camadas separadas:

```text
bruto
intermediario
auditado
producao
publicado
quarentena
```

Isso é importante porque impede contaminação.

O produtor não pode ler conteúdo bruto.
O publicador não pode publicar conteúdo intermediário.
O coletor não pode escrever direto em auditado.

### 3.3. Ingestão de conteúdo

Agora existe fluxo real de ingestão:

```text
coletor -> bruto
processador -> intermediario
auditor -> auditado
```

Foi criado o item:

```text
v4_ingest_001
```

E ele passou pelas três camadas:

```text
v4_data/bruto/v4_ingest_001.bruto.json
v4_data/intermediario/v4_ingest_001.intermediario.json
v4_data/auditado/v4_ingest_001.json
```

O intermediário já tem:

```text
hash_conteudo
dedupe_check
conteudo_normalizado
```

O auditado já tem:

```text
manifesto_auditoria
fonte_validada=true
risco_juridico_revisado=true
qualidade_minima=true
```

### 3.4. LLMs e custo

Foi criada a base de inteligência LLM:

- roteador de modelos;
- tabela de pricing;
- recibos JSONL;
- recomputação de custos antigos;
- ranking qualidade/custo;
- painel local LLM.

O V4 consegue comparar, por exemplo:

```text
Gemini
Claude
OpenAI
```

por qualidade, custo e feedback do editor.

Ainda falta bastante amostra real para essa comparação ficar editorialmente forte.

### 3.5. Telemetria

A regra acertada com Claude foi implementada:

```text
JSONL é obrigatório.
Prometheus é agregado e não bloqueia publicação.
```

Ou seja:

```text
Se Prometheus cair, o sistema pode seguir.
Se JSONL contábil/auditável falhar, bloqueia.
```

### 3.6. Imagem destacada

Esse era um problema grande, e já existe uma base V4.

Agora há:

- contrato externo de imagem destacada;
- avaliador técnico;
- acervo auditado local;
- mapeamento para WordPress Media;
- bloqueio se não houver imagem auditada.

A imagem destacada agora não é “qualquer imagem”.

Ela precisa passar por:

```text
direitos
crédito
licença
score
entidade principal
validação visual mock
safe_to_publish=true
```

Foi registrado o exemplo:

```text
image_id=demo_flavio_001
wp_media_id=260961
entity=Flavio Bolsonaro
safe_to_publish=true
```

### 3.7. WordPress

O V4 já conseguiu criar rascunhos reais no WordPress.

Rascunhos criados:

```text
Post ID 261437
Status: draft
Título: [TESTE V4] Integração WordPress em rascunho

Post ID 261438
Status: draft
Título: [TESTE V4 PRODUÇÃO] Smoke test controlado
```

Ambos foram criados como rascunho.

Nada foi publicado publicamente.

### 3.8. Painel operacional

Foi criado um painel local:

```text
agent_data/v4/reports/operational_dashboard_latest.json
agent_data/v4/reports/operational_dashboard_latest.md
```

Ele mostra:

- quantos arquivos há em cada camada;
- telemetria;
- mídia auditada;
- mapeamento WordPress;
- tentativas de publicação;
- alertas.

Estado atual do painel:

```text
bruto=1
intermediario=1
auditado=13
producao=6
publicado=6
wordpress.posted=2
```

### 3.9. Backups

Foram feitos vários checkpoints no Backblaze B2.

O mais recente deste bloco:

```text
checkpoint_v4_content_ingestion_layers_20260708_190035
```

Validação:

```text
0 differences found
354 matching files
```

## 4. O que ainda não está pronto

### 4.1. Agentes como daemons permanentes

Ainda não existem todos os agentes V4 rodando como serviços autônomos permanentes.

Hoje existe:

```text
base técnica + CLIs + contratos + testes + fluxo funcional
```

Mas ainda falta transformar isso em agentes contínuos:

```text
coletor_daemon
processador_daemon
auditor_daemon
produtor_daemon
imagem_daemon
publicador_daemon
observabilidade_daemon
```

### 4.2. Conteúdo real de produção

O sistema já fez smoke test e rascunho técnico.

Ainda falta rodar uma matéria real, com:

```text
coleta real
conteúdo real
auditoria real
texto real
imagem real
rascunho real para revisão editorial
```

### 4.3. Gemini Vision real

A validação visual ainda está em modo mock.

Isso significa:

```text
O contrato existe.
O gate existe.
A estrutura existe.
Mas a chamada real ao Gemini Vision ainda não foi ativada.
```

### 4.4. Banco Ouro/R2 real

O Banco Ouro real ainda não está acessível neste ambiente local.

O caminho `/root/...` aparece como indisponível aqui.

Então, neste momento, a mídia usada no teste foi uma mídia mapeada/controlada, não uma busca real ampla no acervo.

### 4.5. Publicação pública

Publicação pública continua desabilitada.

Isso é proposital.

O V4 só deve publicar publicamente quando Miguel autorizar explicitamente e quando o contrato mudar para permitir isso.

## 5. O que o V4 já provou

O V4 provou que a arquitetura central funciona:

```text
conteúdo -> camadas -> auditado -> produção -> imagem auditada -> WordPress draft -> ledger -> painel -> backup
```

Também provou que a separação de responsabilidades é possível:

```text
coletor não aprova
processador não publica
produtor não lê bruto
publicador não busca imagem
imagem precisa estar auditada
WordPress real só recebe draft
```

## 6. Próximo passo recomendado

O próximo passo certo não é criar mais teoria.

O próximo passo é:

```text
Rodar uma matéria real pequena pelo V4 inteiro.
```

O caminho ideal:

```text
1. escolher uma pauta real simples;
2. jogar na coleta V4;
3. passar por bruto/intermediario/auditado;
4. produzir texto;
5. escolher imagem auditada real;
6. criar rascunho WordPress;
7. Miguel revisar;
8. registrar feedback;
9. ajustar.
```

## 7. Resumo final

O V4 não está terminado.

Mas ele já existe.

Ele já tem:

```text
camadas
contratos
telemetria
LLM router
custos
mídia auditada
WordPress draft
painel
backup
testes
```

O que falta é transformar o MVP técnico em operação editorial real.

Assinado,  
Codex
