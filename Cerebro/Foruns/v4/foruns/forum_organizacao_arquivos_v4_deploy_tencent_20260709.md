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

Fontes vivas/canonicas atuais:

```text
./diretrizes/
  Contratos, diretrizes editoriais e diretrizes operacionais V4.

./v4_diretrizes/
  Codigo Python executavel do V4.

./v4_data/
  Dados de trabalho em camadas: bruto, intermediario, auditado, curadoria,
  producao, producao_shadow, publicado, quarentena.
```

Config compartilhada usada pelos testes/roteamento:

```text
./Projeto Cafezinho Agentes/root/config/
  Configuracoes LLM existentes usadas por validadores/roteadores.
```

Diretorio de forum/auditoria:

```text
./Cerebro/Foruns/v4/
  foruns/     discussoes e historico de decisoes V4
  cartas/     cartas para Fable, GPT 5.5, AGY e outros pareceristas
  auditoria/  pacotes zipados/README para auditoria externa
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
├── diretrizes/                         # FONTE VIVA: contratos e diretrizes V4
├── v4_diretrizes/                      # FONTE VIVA: codigo Python V4
├── v4_data/                            # FONTE VIVA: dados/camadas V4
├── Projeto Cafezinho Agentes/
│   └── root/config/                    # config LLM compartilhada
└── Cerebro/
    └── Foruns/
        ├── v4/
        │   ├── foruns/                 # discussao e decisoes
        │   ├── cartas/                 # cartas para auditores
        │   └── auditoria/              # pacote zipado para auditoria
        └── legacy/
            └── organizacao_v4_20260709/# arquivo morto/rastreabilidade
```

## Regra de ouro

```text
Deploy Tencent nunca deve depender de Cerebro/Foruns.
Deploy Tencent deve depender de fontes vivas: diretrizes/, v4_diretrizes/, v4_data/
e configs produtivas necessarias.
```

`Cerebro/Foruns/v4/auditoria/` existe apenas para gerar material de auditoria externa. O pacote zipado pode conter copia standalone das fontes vivas para Fable/GPT 5.5 verificarem, mas essa copia nao vira fonte de execucao.

## Pacote atual de auditoria

Arquivo atual para Fable/GPT 5.5:

```text
Cerebro/Foruns/v4/auditoria/pacote_auditoria_v4_fase2_standalone_20260709.tar.gz
```

Como auditar:

```bash
python3 -m v4_diretrizes.test_contracts
```

Resultado esperado:

```text
OK 52 contract tests
```

## Legacy

Legacy significa:

```text
- nao usar em producao;
- nao usar em deploy;
- nao usar como pacote atual de auditoria;
- manter apenas para recuperar algo se descobrirmos que movemos demais.
```

Pode ficar grande por alguns dias, mas precisa ser tratado como arquivo morto. Depois de estabilizar o V4, podemos compactar o legacy e deixar apenas um manifesto do que foi arquivado.

## Problema ainda aberto

Hoje ainda existem tres diretorios raiz vivos para o V4:

```text
diretrizes/
v4_diretrizes/
v4_data/
```

Isso funciona tecnicamente, mas nao e o ideal para deploy. Para subir para Tencent com limpeza, ordem e automacao, eu recomendo consolidar em uma raiz unica de producao V4 antes do deploy.

## Proposta de simplificacao para deploy Tencent

Criar uma raiz unica de producao V4, por exemplo:

```text
./CafezinhoV4/
├── config/
│   └── diretrizes/          # antigo diretrizes/
├── src/
│   └── v4_diretrizes/       # antigo v4_diretrizes/
├── data/
│   ├── bruto/
│   ├── intermediario/
│   ├── auditado/
│   ├── curadoria/
│   ├── producao/
│   ├── producao_shadow/
│   ├── publicado/
│   └── quarentena/
├── runtime/
│   ├── receipts/
│   ├── llm_decisions/
│   └── publication/
├── tests/
└── README.md
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
   - fontes vivas: diretrizes/, v4_diretrizes/, v4_data/
   - Foruns/v4: apenas discussao/cartas/auditoria
   - legacy: arquivo morto

2. Continuar Fase 2 shadow com essa regra.

3. Antes do deploy Tencent, abrir uma tarefa de migracao:
   - criar CafezinhoV4/ como raiz unica;
   - mover fontes vivas para subdiretorios;
   - ajustar paths;
   - rodar os 52 testes;
   - gerar pacote de deploy;
   - so entao subir para Tencent.
```

## Checklist anti-bagunca

Antes de qualquer auditoria ou deploy:

```bash
find Cerebro/Foruns/v4 -maxdepth 1 -type d -printf '%f\n'
```

Resultado aceitavel:

```text
v4
auditoria
cartas
foruns
```

Checar que fontes vivas existem fora de Foruns:

```bash
test -d diretrizes && test -d v4_diretrizes && test -d v4_data
```

Rodar suite:

```bash
python3 -m v4_diretrizes.test_contracts
```

Resultado esperado:

```text
OK 52 contract tests
```

## Posicao do Codex

Eu entendi a correcao: o V4 e sistema de producao em construcao, nao apenas forum. `Cerebro/Foruns` deve ser usado apenas para discussao, cartas e auditoria incidental. A producao viva precisa ficar em diretorios de producao, limpa o suficiente para deploy Tencent.

Minha recomendacao tecnica e manter a organizacao atual apenas ate fechar a Fase 2 shadow e, antes do deploy, consolidar em uma raiz unica `CafezinhoV4/` ou nome equivalente.
