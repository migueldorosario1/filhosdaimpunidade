# Forum — Organizacao dos arquivos V4 e deploy Tencent

Criado em: 2026-07-09  
Status: forum de organizacao e higiene operacional  
Objetivo: impedir confusao entre fonte viva, forum, auditoria, pacote zipado e legacy antes do deploy para Tencent.

## Entendimento operacional

O V4 nao e apenas uma discussao editorial. Estamos produzindo arquivos reais de trabalho que devem entrar em producao em breve e ser deployados para Tencent.

Portanto:

```text
- arquivos de producao nao devem morar em Cerebro/Foruns;
- Cerebro/Foruns e diretorio de discussao, memoria, cartas e auditoria;
- fonte viva precisa ficar em diretorio de producao vivo;
- pacote para Fable/GPT 5.5 e material de auditoria, nao origem de producao;
- legacy e arquivo morto/rastreabilidade, nao input operacional.
```

## Estado atual corrigido

Fonte ativa de laboratorio:

```text
Projeto Cafezinho Agentes/root/v4_labs/
  Fonte unica de trabalho para Fase 2 shadow/dry-run do V4.
  Inclui contratos/, codigo/, dados/ e config/ de laboratorio.
```

Destino final reservado:

```text
Projeto Cafezinho Agentes/root/v4/
  Somente arquivos finais auditados e prontos para producao.
```

## Decisao atual — v4_labs e v4 dentro do root operacional

Decisao em 2026-07-09:

```text
Projeto Cafezinho Agentes/root/v4_labs/  = laboratorio de testes V4
Projeto Cafezinho Agentes/root/v4/       = destino final para arquivos auditados
```

Motivo:

```text
Projeto Cafezinho Agentes/root/ ja e o centro operacional que contem config/, agent_data/ e scripts vivos.
Colocar v4_labs e v4 dentro dele aproxima o V4 do ambiente que sera deployado para Tencent.
```

Status criado:

```text
Projeto Cafezinho Agentes/root/v4_labs/
  contratos/
  codigo/
  dados/
  config/
  README_V4_LABS.md
  AUDITOR_NOTE_FASE2_20260709.md

Projeto Cafezinho Agentes/root/v4/
  README_V4_FINAL.md
  MANIFESTO_STATUS_V4_FINAL_20260709.md
```

Validacao:

```bash
cd "Projeto Cafezinho Agentes/root/v4_labs"
PYTHONDONTWRITEBYTECODE=1 python3 -m codigo.test_contracts
```

Resultado:

```text
OK 55 contract tests
```

Observacao importante:

```text
v4_labs ainda e copia de laboratorio. A promocao para root/v4 exige auditoria e manifesto.
root/v4 esta reservado e nao recebeu arquivos experimentais.
```

Config compartilhada usada pelos testes/roteamento:

```text
./Projeto Cafezinho Agentes/root/config/
  Configuracoes LLM existentes usadas por validadores/roteadores.
```

Diretorio de forum:

```text
./Cerebro/Foruns/
  forum_*.md  discussoes e historico de decisoes
  carta_*.md  cartas para Fable, GPT 5.5, AGY e outros pareceristas
```

Arquivo morto/legado:

```text
./Cerebro/Foruns/legacy/organizacao_v4_20260709/
  duplicatas antigas, espelhos intermediarios, aliases e pacotes descompactados
  que nao devem ser usados como fonte viva nem como auditoria corrente.
```

## Diagrama atual

```text
Antigravity Google/
├── Projeto Cafezinho Agentes/
│   └── root/
│       ├── config/                     # config LLM compartilhada
│       ├── v4_labs/                    # FONTE ATIVA: laboratorio V4 em teste
│       ├── v4_labs_fase3_preflight_para_fable_20260709.tar.gz
│       └── v4/                         # destino final auditado, ainda reservado
├── Backups/
│   └── v4_root_provisorio_pre_labs_unico_20260709_021707/
│       └── ...                         # raiz V4 antiga, somente rollback
└── Cerebro/
    └── Foruns/
        ├── forum_*.md                  # discussoes
        ├── carta_*.md                  # cartas
        └── legacy/
            └── organizacao_v4_20260709/# arquivo morto/rastreabilidade
```

## Regra de ouro

```text
Deploy Tencent nunca deve depender de Cerebro/Foruns.
Deploy Tencent deve depender do pacote operacional que sair de:
Projeto Cafezinho Agentes/root/v4_labs/  -> testes
Projeto Cafezinho Agentes/root/v4/       -> final auditado
```

Auditoria externa agora deve usar diretamente o laboratorio:

```text
Projeto Cafezinho Agentes/root/v4_labs/
```

Se for preciso subir arquivo compactado para Fable/GPT 5.5, usar:

```text
Projeto Cafezinho Agentes/root/v4_labs_fase3_preflight_para_fable_20260709.tar.gz
```

Esse pacote foi testado apos extracao isolada em `/tmp` e retornou:

```text
OK 55 contract tests
```

Como auditar dentro do laboratorio:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m codigo.test_contracts
```

Resultado esperado:

```text
OK 55 contract tests
```

Nao precisamos mais manter pacote pesado nem diretorio `Cerebro/Foruns/v4`. Nos foruns, ficam apenas foruns, cartas e docs leves.

## Legacy

Legacy significa:

```text
- nao usar em producao;
- nao usar em deploy;
- nao usar como pacote atual de auditoria;
- manter apenas para recuperar algo se descobrirmos que movemos demais.
```

Pode ficar grande por alguns dias, mas precisa ser tratado como arquivo morto. Depois de estabilizar o V4, podemos compactar o legacy e deixar apenas um manifesto do que foi arquivado.

## Problema resolvido nesta limpeza

Existiam estes diretorios raiz provisorios fora do Cafezinho Agentes. Sao nomes antigos, arquivados, e nao devem ser usados como fonte ativa:

```text
diretrizes/
v4_diretrizes/
v4_data/
agent_data/v4/
```

Eles foram movidos para:

```text
Backups/v4_root_provisorio_pre_labs_unico_20260709_021707/
```

Regra: nao usar esse backup para auditoria corrente, deploy ou execucao. A fonte ativa agora e `Projeto Cafezinho Agentes/root/v4_labs/`.

## Proposta de simplificacao para deploy Tencent

Promover, quando auditado, de:

```text
Projeto Cafezinho Agentes/root/v4_labs/
```

para:

```text
Projeto Cafezinho Agentes/root/v4/
```

Estrutura final provavel:

```text
Projeto Cafezinho Agentes/root/v4/
├── contratos/
├── codigo/
├── dados/
├── runtime/
├── README_V4_FINAL.md
└── MANIFESTO_PROMOCAO_*.md
```

Vantagens:

```text
- menos diretorios raiz;
- deploy mais simples para Tencent;
- fronteira clara entre producao e forum;
- facilita backup seletivo;
- facilita rsync/scp/docker/systemd;
- reduz chance de agente auditar ou executar arquivo errado.
```

Risco:

```text
- exige ajustar imports, paths de contrato e testes;
- pode quebrar automacoes existentes se feito no meio da Fase 2;
- precisa de migracao controlada e commit/ponto de rollback.
```

## Plano recomendado

Nao mover agora no impulso. Fazer em tres passos:

```text
1. Congelar regra atual:
   - fonte ativa de laboratorio: Projeto Cafezinho Agentes/root/v4_labs/
   - estrutura interna: contratos/, codigo/, dados/, config/
   - Foruns: apenas discussao/cartas/docs leves
   - legacy: arquivo morto

2. Continuar Fase 2 shadow com essa regra.

3. Antes do deploy Tencent, abrir uma tarefa de promocao:
   - validar v4_labs;
   - remover shims temporarios de caminho;
   - promover arquivos auditados para root/v4;
   - rodar os 52 testes dentro de root/v4;
   - gerar pacote de deploy;
   - so entao subir para Tencent.
```

## Checklist anti-bagunca

Antes de qualquer auditoria ou deploy:

```bash
test ! -e Cerebro/Foruns/v4
```

Resultado aceitavel:

```text
sem saida / exit code 0
```

Checar que fontes vivas existem fora de Foruns:

```bash
test -d "Projeto Cafezinho Agentes/root/v4_labs"
test -d "Projeto Cafezinho Agentes/root/v4_labs/contratos"
test -d "Projeto Cafezinho Agentes/root/v4_labs/codigo"
test -d "Projeto Cafezinho Agentes/root/v4_labs/dados"
test -d "Projeto Cafezinho Agentes/root/v4"
```

Rodar suite:

```bash
cd "Projeto Cafezinho Agentes/root/v4_labs"
PYTHONDONTWRITEBYTECODE=1 python3 -m codigo.test_contracts
```

Resultado esperado:

```text
OK 55 contract tests
```

## Posicao do Codex

Eu entendi a correcao: o V4 e sistema de producao em construcao, nao apenas forum. `Cerebro/Foruns` deve ser usado apenas para discussao, cartas e auditoria incidental. A producao viva precisa ficar em diretorios de producao, limpa o suficiente para deploy Tencent.

Minha recomendacao tecnica atual e manter uma unica fonte ativa de laboratorio em `Projeto Cafezinho Agentes/root/v4_labs/`, com nomes semanticos:

```text
contratos/ = JSON/MD, diretrizes externas, contratos operacionais
codigo/    = codigo Python executavel
dados/     = camadas de dados de teste/shadow
config/    = configuracao LLM de laboratorio
```

Depois de auditoria, promover para `Projeto Cafezinho Agentes/root/v4/` com a mesma estrutura.
