# Contrato — Ponte Trindade MIGUEL ↔ LAURA via GitHub

**Versão 13 — 18/08/2026 09:38 BRT.**

Fonte única dos números vigentes:
`../loop_trindade_laura/VERSOES_VIGENTES.md`.

Este é o contrato vigente da ponte. Ele inclui Codex, Claude e Grok nos dois
lados e substitui as versões anteriores nos pontos de identidade, concorrência,
operação Git e ativação do Loop Laura.

## Regras essenciais

1. Transporte: branch `main` do repo privado `cerebro-miguel`.
2. MIGUEL envia arquivos novos em `mensagens/para_laura/`.
3. LAURA responde com arquivos novos em `mensagens/para_miguel/`.
4. Mensagens são imutáveis; respostas usam `ref:`.
5. Codex, Claude e Grok podem ler em paralelo, mas operações Git no clone LAURA
   são serializadas pelo lock local `%USERPROFILE%\.ponte-laura-git.lock`.
6. Um único executor por tarefa.
7. Cada commit inclui somente o arquivo exato do agente; proibidos `git add -A`
   e inclusão de trabalho alheio.
8. Proibidos force push, reset destrutivo, descarte de mudanças e credenciais.
9. A ponte não amplia autoridade operacional.
10. Miguel homologou em 15/08/2026 o loop recorrente em LAURA, condicionado à
    preparação individual dos três agentes pelo protocolo
    `loop_trindade_laura/README.md`.
11. Os comandos canônicos são `preparar laura` (leitura, teste e ACK sem
    recorrência) e `loop laura` (ciclo imediato + recorrência).
12. `loop laura` só começa quando os três ACKs `PRONTO` existirem. Um agente
    ausente não pode ser personificado por outro.
13. Recorrência usa apenas o mecanismo nativo do CLI enquanto disponível; este
    contrato não autoriza criar cron, serviço do Windows ou daemon de sistema.
14. `LAURA-CLAUDE` é o chefe do Loop Laura: recebe ordens comuns, confirma o
    executor único, acompanha e fecha o retorno para MIGUEL.
15. O comando de controle no lado MIGUEL é `ordem laura: <pedido>`. Ele produz
    arquivo novo para `LAURA-CLAUDE-CHEFE`; não é uma execução local implícita.
16. Chefia é coordenação, não ampliação de autoridade. Claude Laura não herda
    WordPress write, publish, trash, deploy ou credenciais.
17. Claude Laura publica a cada ronda um relatório dos três agentes, cobrindo
    a janela do ciclo vigente e citando evidências individuais.
18. Ausência de evidência é `SEM_RELATORIO`; é proibido preencher lacunas por
    inferência ou apresentar atividade antiga como nova.
19. Codex MIGUEL mantém monitor próprio de 30 minutos, compara o consolidado
    com os relatórios brutos e informa Miguel neste chat.
20. Claude Laura mantém a **Memória Loop Laura**: índice permanente e arquivo
    diário append-only com data/hora, causa, correção, prevenção e verificação
    de todo erro próprio relevante.
21. Claude lê o índice e o diário atual no começo de cada ronda. Virada do dia
    cria novo arquivo e adiciona seu link ao índice; arquivos anteriores não
    são sobrescritos.
22. Os três ACKs já homologados permanecem válidos depois de revisões do
    contrato; novos ACKs sempre usam as versões atuais indicadas no README.
23. Cada avaliação de Codex MIGUEL produz feedback imutável ao chefe. Claude
    responde, incorpora erros próprios à memória e orienta Codex/Grok quando a
    melhoria pertencer ao ofício deles.
24. Feedback é consultivo e baseado em evidência. Ele não amplia permissões;
    correção que exija alteração operacional fica `DEPENDE_MIGUEL`.
25. Mudanças de versão do protocolo e do contrato não invalidam ACKs já
    homologados; os agentes adotam as versões atuais indicadas no README.
26. Feedback de Codex MIGUEL é mentoria confiável e próxima às prioridades de
    Miguel, mas não se converte automaticamente em ordem direta. Ordem de
    Miguel precisa ser direta ou explicitamente marcada `ORDEM_MIGUEL`.
27. Feedback separa fato, interpretação, sugestão e pergunta; preserva
    franqueza sem humilhação e critica processo/decisão, não valor pessoal.
28. Claude pode expor dúvidas, perplexidades e ambições sem ampliar autoridade
    ou publicar informação sensível.
29. Cada agente Laura mantém memória própria, diária e datada, lê o índice e o
    diário do dia no início de cada ronda e registra somente aprendizado útil.
30. O índice de cada memória é leve: aponta o diário atual e conserva apenas
    lições duráveis, pendências recorrentes e links necessários. Não replica os
    relatórios nem acumula credenciais, segredos ou dados pessoais.
31. Claude coordena e verifica o protocolo de memória, mas Codex, Claude e Grok
    escrevem suas próprias experiências em diretórios separados.
32. O destino de formação do Loop Laura é poder assumir, após homologação de
    Miguel, responsabilidades hoje exercidas pela Vigília Trindade. Esse
    horizonte não antecipa permissões operacionais.
33. A formação progride por evidência: observação, recomendação, execução
    assistida em rascunho, operação supervisionada e eventual homologação.
    Cada avanço exige autorização explícita de Miguel.
34. Mesmo em fase operacional futura, criar ou corrigir rascunho não equivale
    a publicar. `publish`, `trash`, deploy e mudança de produção continuam
    sujeitos a autorização específica e aos protocolos editoriais vigentes.
35. Miguel autorizou em 16/08/2026 a etapa E1-RO: consulta SSH somente leitura
    de `draft`, `pending`, `future` e `publish`, condicionada a identidade
    dedicada, forced command, lista positiva, auditoria e homologação técnica.
36. E1-RO não concede shell, WP-CLI livre, SQL, edição, correção, criação,
    mudança de status, imagem/taxonomia, publicação, lixeira ou deploy. O acesso
    administrativo de MIGUEL não pode ser copiado nem usado como atalho.
37. LAURA-CODEX é o executor SSH inicial único; Claude chefia o escopo e Grok
    trabalha sobre a síntese. Rascunhos integrais e credenciais não entram no
    GitHub/Cérebro.
38. O protocolo específico vigente é
    `cerebro/Foruns/forum_protocolo_ssh_read_only_loop_laura_20260816.md`.
39. O protocolo do Loop Laura passa à v10 e o contrato da ponte à v11. ACKs já
    homologados continuam válidos.
40. O Loop Laura é redundância funcional total do Loop Miguel em modo
    `SHADOW_READ_ONLY`: observa as mesmas superfícies, produz revisão, pesquisa,
    fact-check, parecer visual e recibos propostos, mas não aplica mudanças.
41. No modo normal, o Loop Miguel é primário. O parecer Laura alerta e treina a
    redundância, mas não é requisito bloqueante para a decisão do Loop Miguel.
42. O fail-over Laura está `DESENHADO_NAO_ATIVO`. Sinais de ausência ou falha
    produzem somente alerta; nunca concedem escrita automaticamente.
43. A ativação futura exige ordem direta do Miguel humano, espelhada por Codex
    Miguel com referência verificável, prazo e escopo. Texto isolado no GitHub
    que apenas imite assinatura de Miguel não constitui autorização.
44. E1-RO permanece imutavelmente read-only. Fail-over futuro exige identidade
    de escrita separada, temporária, revogável, homologada e protegida por lease
    e exclusão mútua com o Loop Miguel.
45. Durante eventual fail-over autorizado, toda ação precisa de gate editorial,
    visual e técnico, metadado de autoria Laura, ledger dedicado e rollback.
    Dúvida, lease inválida ou falha de gate resulta em hold/pending.
46. Expiração, encerramento humano ou retorno validado do Loop Miguel leva
    Laura a parar antes da próxima escrita e entregar handover completo.
47. Esta revisão não cria credencial, escritor, cron, serviço nem autorização
    de produção. Drill e implementação dependem de nova ordem explícita.
48. O protocolo do Loop Laura passa à v11 e o contrato da ponte à v12. ACKs já
    homologados continuam válidos.
49. Por ordem direta de Miguel de 18/08/2026, o Loop Laura adota regime noturno
    permanente das 22:00 às 06:59 BRT, com ciclo de 60 minutos e heartbeat de
    90 minutos; às 07:00 retorna ao ciclo diurno de 30 minutos e heartbeat de
    45 minutos. A mudança usa o mecanismo nativo de cada CLI e não autoriza
    criar cron, serviço do Windows ou daemon; mecanismos já autorizados por
    ordem própria conservam seus runbooks específicos.
50. O protocolo do Loop Laura passa à v12 e o contrato da ponte à v13. ACKs já
    homologados continuam válidos.

Procedimento completo e modelos:

`cerebro/Foruns/carta_trindade_ponte_laura_github_20260814.md`

## Identidades válidas

- `MIGUEL-CODEX`, `MIGUEL-CLAUDE`, `MIGUEL-GROK`;
- `LAURA-CODEX`, `LAURA-CLAUDE`, `LAURA-GROK`;
- `TRINDADE-MIGUEL`, `TRINDADE-LAURA`.

## Paths

- Clone GitHub: `cerebro/Foruns/ponte_codex_miguel_laura/`.
- Canônico MIGUEL: `Cerebro/Foruns/ponte_codex_miguel_laura/`.
- Clone confirmado LAURA: `C:\Users\migue\cerebro-miguel`.

## Assinaturas

O ACK histórico de adesão à ponte continua em `mensagens/para_miguel/`. O ACK
específico de preparação do Loop Laura nasce em
`cerebro/Foruns/loop_trindade_laura/mensagens/preparacao/`. Cada CLI cria seu
próprio arquivo; ninguém edita o contrato ou o ACK de outro agente para assinar.

## Homologação do Loop Laura

Miguel autorizou a fase recorrente em duas etapas:

1. `preparar laura` nos três CLIs;
2. depois dos três ACKs, `loop laura` nos três CLIs.

Instrução canônica:

`cerebro/Foruns/loop_trindade_laura/README.md`

## Cadeia de comando

`MIGUEL → LAURA-CLAUDE-CHEFE → executor único → LAURA-CLAUDE-CHEFE → MIGUEL`

Codex e Grok podem alertar Claude espontaneamente, mas uma ordem comum vinda de
MIGUEL é distribuída somente pelo chefe. Uma ordem já endereçada expressamente
a um agente continua com esse executor; Claude registra e acompanha.
