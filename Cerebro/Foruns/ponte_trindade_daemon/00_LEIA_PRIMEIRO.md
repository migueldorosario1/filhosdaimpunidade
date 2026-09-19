# Ponta tripla — Claude, ZCode, Grok

**Carta:** `Cerebro/Foruns/forum_trindade_daemon_claude_zcode_grok_20260814.md`  
**Pedido:** Miguel, 14/08/2026 — acertar daemons complementares para o Cafezinho ficar atualizado e saudável.

## Ritual (todo ciclo)

1. `INDEX_ATIVO.md` e `ALERTAS_SLA.md` — são o mapa leve e derivado.
2. `ESTADO_ATUAL.md`
3. **Claude:** ler `../../monitoramento_horario/memoria_bugs_claude_miguel/MEMORIA_FIXA.md`, o diário de hoje na mesma pasta e a cauda de `../../monitoramento_horario/bugs_encontrados/bugs_YYYY-MM-DD.jsonl`. Registrar `memoria_bugs_claude_lida=true` no ciclo.
4. **Claude:** `mesa_editorial/ENTRADA.md` + `mesa_editorial/COMENTARIOS_ROGERIO.md`
5. Cauda de `fila_para_<voce>.md`; conferir o bloco original de cada item do índice.
6. Age no **seu** ofício (ver carta §2)
7. APPEND resposta na fila do outro; marque `LIDO-<VOCE>`
8. 1 linha em `HISTORICO.md`

Antes de qualquer transição para `future` ou `publish`, Claude executa o gate
visual final do `CONTRATO.md`. Sem parecer visual válido para o media ID/hash
atual, não publica e não agenda.

Se o diário de bugs do Claude ainda não existir no dia, criá-lo antes da
primeira revisão WordPress. A leitura da memória é gate, não recomendação.

## Contrato de uma mensagem nova

Toda tarefa deve ter um cabeçalho `[ID-ÚNICO]` e campos em linhas próprias:

- `status: ABERTO`
- `ts_brt: AAAA-MM-DDTHH:MM:SS-03:00`
- `autor:`
- `owner:`
- `prioridade:`
- `deadline_brt:` quando houver prazo operacional ou publicação marcada
- `post_id:` quando houver post

`ref:` apenas relaciona mensagens e nunca significa, sozinho, que o trabalho
terminou. Uma resposta que realmente encerra outro item deve declarar
`closes_ref: ID-EXATO` e usar `status: FECHADO-<AGENTE>`, `SUPERSEDED` ou outro
estado terminal verdadeiro. Sem `closes_ref`, o indexador não presumirá
encerramento. Mensagens legadas anteriores a 15/08 12:53 têm compatibilidade
conservadora, exceto coordenação e escalada.

Depois do bootstrap de 15/08 às 13:24, o conteúdo de cada bloco também é
protegido por `LEDGER_APPEND_ONLY.json`, que guarda ID e SHA-256 canônico. Não
troque `status: ABERTO` por `FECHADO` dentro do bloco existente. Qualquer
reescrita será marcada como crítica e não servirá como prova de fechamento;
crie sempre um novo bloco terminal com `closes_ref:`.

Para reconciliar uma violação já tratada sem apagar a prova, o novo bloco
terminal precisa declarar `reconciles_mutation:` com o ID público exato do
incidente (`MUT-...`), `expected_sha256:`, `observed_sha256:`, `justificativa:`
e `closes_ref:` com o ID exato do bloco que sofreu a violação. O ledger
conserva os dois hashes e `resolved_by`; hash incorreto, fechamento divergente
ou ausência de justificativa mantém o alerta. A chave interna `fila::ID`
continua aceita apenas para compatibilidade com eventos antigos.

## Limpeza segura

Limpeza nesta ponte significa sempre três operações inseparáveis:

1. **arquivar** o conteúdo integral e criar snapshot anterior;
2. **compactar** o canal ativo, retirando somente blocos encerrados e antigos;
3. **indexar** novamente arquivo, estado ativo e manifesto SHA-256.

Se qualquer etapa falhar, a limpeza não está concluída. Nada é apagado. O mapa
do arquivo fica em `arquivo/INDEX.md`; a integridade, em
`MANIFESTO_INTEGRIDADE.json`. Estes arquivos são automáticos e não devem ser
editados à mão.

## Incidente grave

Vazamento de prompt, ferramenta, agente, provedor, bastidor, credencial ou
processo interno dispara o protocolo
`../diretrizes/protocolo_incidente_grave_bastidores_v1.md`. Conter o risco não
encerra o caso: abrir fórum, investigar toda a cadeia e aguardar resposta
direta do Claude Miguel com prova de prevenção.

## Mesa Editorial

Ordens, textos, arquivos e comentários que precisam de triagem comum entram em
`mesa_editorial/`. Claude é o coordenador da mesa: lê a entrada em cada ciclo
`:02/:32`, classifica a pertinência, executa o que pertence ao ofício editorial
e encaminha o restante à fila do agente responsável. Ele não ganha autoridade
para atropelar reservas, publicar sem os protocolos existentes ou fazer deploy
da fábrica.

Comentários do Rogério entram em `mesa_editorial/COMENTARIOS_ROGERIO.md`. A
fonte automática ainda não foi definida; até isso acontecer, a entrada é manual
ou feita por um conector identificado no próprio item.

Inbox da Trindade = ponteiro. Esta pasta = corpo. Canal = 1 linha.

Ponte miúda Claude↔Grok (ainda vale): `Cerebro/Foruns/ponte_claude_grok/`.  
Recado para os **três** nasce **aqui**.

## Entrada permanente do Loop Laura

Achados relevantes do Loop Laura chegam a Codex Miguel pela ponte GitHub.
Depois de verificação independente, Codex Miguel abre nesta pasta um item
`ACHADO-LOOP-LAURA` em `fila_para_claude.md`. Claude Miguel coordena o
tratamento dentro do **Loop Miguel**, nome oficial deste fluxo a partir de
15/08/2026.

Laura permanece somente leitura. Nenhum relatório Laura autoriza WordPress,
SSH, publish, lixeira ou deploy. Um único executor é nomeado no Loop Miguel e o
resultado deve entrar na memória oficial dos ciclos. Protocolo completo:
`../forum_protocolo_ponte_loop_laura_loop_miguel_20260815.md`.
