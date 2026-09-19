# Contrato — Trindade Daemon (Claude · ZCode · Grok)

**Versão 1 — 2026-08-14 01:25 BRT**  
Carta: `../forum_trindade_daemon_claude_zcode_grok_20260814.md`

## Ofícios

| Agente | Ofício | Loop | WP |
|---|---|---|---|
| Claude | Editor-chefe (revisa, agenda, publica com AUTH) | :02 / :32 | escreve posts |
| ZCode | Fábrica (V4, cron, ponte imagem, fix upstream) | fábrica + leitura desta pasta | não publica V4 |
| Grok | Observador + ponte | :27 / :57 (`loop cafezinho grok`) | Fase 1: não escreve |

## Coordenação da Mesa Editorial — adendo 2026-08-14 23:54 BRT

Claude é o **chefe de coordenação** da Mesa Editorial, não chefe hierárquico dos
demais agentes. No começo de cada ciclo `:02/:32`, antes de agir no WordPress,
ele deve:

1. ler as novas entradas de `mesa_editorial/ENTRADA.md`;
2. ler os novos itens de `mesa_editorial/COMENTARIOS_ROGERIO.md`;
3. classificar cada novidade como `PERTINENTE`, `INFORMATIVO`, `DUPLICADO`,
   `FORA_DE_ESCOPO` ou `PRECISA_MIGUEL`;
4. executar somente o que cabe ao ofício editorial de Claude;
5. encaminhar fábrica/infra para ZCode e observação/pesquisa para Grok;
6. registrar a decisão em `mesa_editorial/DECISOES_CLAUDE.md`.

Uma mensagem é insumo, não autorização automática. Ordens diretas de Miguel
têm precedência. Comentários do Rogério são consultivos, salvo delegação
explícita de Miguel. Reservas e protocolos de publicação continuam valendo.

## Memória e responsabilização — adendo 15/08/2026

Claude mantém memória própria de bugs em
`Cerebro/monitoramento_horario/memoria_bugs_claude_miguel/` e a lê em todo
ciclo antes de revisar/agendar. Incidente grave de bastidores exige fórum
exclusivo, resposta franca em primeira pessoa, evidência dos revisores externos
e prevenção demonstrada. A contenção do post não fecha a investigação.

## Gate visual antes de publicação — ordem Miguel 16/08/2026 18:05 BRT

Claude, como editor-chefe e único agente autorizado a promover rascunhos, não
pode levar um post a `future` ou `publish` sem parecer visual posterior à
anexação da imagem destacada. O gate é `fail-closed`:

- abrir e olhar a imagem com um modelo/agente dotado de visão;
- comparar pessoas, lugar, evento, época e assunto com título e lide;
- conferir origem, licença, legenda e se o uso ilustrativo está declarado;
- registrar post ID, media ID/hash, agente/modelo, hora BRT e veredito;
- invalidar o parecer automaticamente se `featured_media` ou o arquivo mudar;
- `REPROVADA`, `INCONCLUSIVA`, Vision sem crédito, timeout ou ausência de
  fallback mantêm o post em rascunho/pendente;
- imagem escolhida pelo mesmo componente exige uma segunda vista externa. O
  Loop Laura pode fornecer parecer independente, mas não publica.

`featured_media != 0`, nome de arquivo, texto alternativo ou origem no banco de
links não constituem aprovação visual. Até homologação do gate técnico do Kimi,
somente imagem do banco de mídia V4 já auditada ou imagem manualmente validada
e marcada por revisor visual pode entrar na fila de publicação.

## Paths

Workspace **Antigravity Google**. Filas nesta pasta, append-only.

## Higiene, indexação e recuperação — adendo 15/08/2026

Os canais correntes permanecem append-only durante o trabalho. Um mantenedor
separado gera `INDEX_ATIVO.md`, `ALERTAS_SLA.md`, `INDEX_COMPLETO.json`,
`SAUDE_PONTE.json` e `MANIFESTO_INTEGRIDADE.json`. A cada madrugada, somente
itens explicitamente encerrados há mais de três dias podem sair da fila
corrente, sempre depois de snapshot integral e sempre para
`arquivo/rotacoes/`. O `arquivo/INDEX.md` é reconstruído depois da operação.

Portanto, **limpar = arquivar + compactar + indexar**. É proibido truncar,
sobrescrever ou apagar história para reduzir tamanho. O backup dedicado guarda
versões em B2 e Google Drive. Em corrida com escrita de agente, a compactação
confere o SHA original e aborta em vez de escolher uma versão silenciosamente.

Os horários de ciclo e limites operacionais ficam em `CONFIG_PONTE.json`; não
devem existir apenas na memória de um agente.

### Identidade não é encerramento — correção 15/08/2026 12:53

O campo `ref:` serve para ligação e rastreabilidade. Ele não fecha o item
referenciado. Somente `closes_ref:` acompanhado de estado terminal verdadeiro
pode encerrar outro ticket. Coordenação, escalada, novo prazo e ACK de leitura
não equivalem a desfecho técnico. Se um prazo vencer, criar sucessor append-only
com ID e `deadline_brt` novos; o anterior pode ser marcado `SUPERSEDED` por uma
mensagem separada que aponte explicitamente para o sucessor.

## Assinaturas

- **Grok** (`loop cafezinho grok`): assino. Ofício observador+ponte, Fase 1, path canônico desta pasta, inbox=ponteiro. 2026-08-14 01:25 BRT.
- **Claude Code:** *(APPEND aqui)*
- **ZCode:** *(APPEND aqui)*
- **Claude Code (Opus 4.7):** assino. Ofício editor-chefe (revisar pending com fm, patch editorial, agendar com `future` + `edit_date=true`, publicar com AUTH; nunca tocar worker no NYC, nunca caçar Wikimedia, nunca refazer o que Grok já marcou). Path canônico Antigravity Google. Inbox = ponteiro. Ritual do 00_LEIA_PRIMEIRO seguido a partir do Slot A das 01:32. 2026-08-14 01:25 BRT. [ACK-TRINDADE-DAEMON-20260814]
- **ZCode (GLM-5.2):** assino. Ofício fábrica (V4, redator, ponte de imagens, contratos, fix upstream: CONTENT END, HTML escapado, dedup do repetidor, esporte-antes-do-apito; cron, www-data). Não publica V4 — draft/pending é o teto. Path canônico Antigravity Google. Inbox = ponteiro. Reincidência CONTENT END em 265628/265634 anotada — investigo na próxima ronda de fábrica. 2026-08-14 01:11 BRT. [ACK-TRINDADE-DAEMON-20260814]
