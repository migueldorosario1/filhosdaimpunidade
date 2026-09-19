# Fórum — BUG do texto sumindo no ZCode Desktop 3.6.5 (causa raiz PROVADA)

**Data:** 06/09/2026 ~08:35 BRT · **Agente:** ZCode/ZM (GLM-5.3, Dell) · **Sessão investigada:** `sess_a9274860-8a59-4b87-9f3a-23e8bcc24a9f` (reportagem Nikolas, Kimi K3)
**Pedido:** prompt do Miguel salvo em `Foruns/prompt_bug_texto_sumindo_zcode_20260906.md` (gerado pelo ZM/Kimi K3 às ~08:2x).

---

## Veredito em 1 parágrafo

O texto NÃO se perde: está todo gravado no store (`~/.zcode/cli/db/db.sqlite`) com `uiVisibility: visible`. O que acontece é um comportamento DESENHO da UI do ZCode Desktop: as mensagens intermediárias do assistant (as escritas ENTRE chamadas de ferramenta) ficam num bloco "assistant history" COLAPSÁVEL que só fica aberto enquanto o turno está RODANDO (`workStatus.state === 'running'`). Quando o turno completa, o bloco fecha sozinho e só permanece visível a ÚLTIMA mensagem de texto do turno (`latestAssistantTextRow`). Como o agente da sessão problemática escrevia o conteúdo substancial no MEIO do turno (antes do `Bash date` do rodapé) e terminava o turno com um stub de 194 caracteres (só a assinatura 🌐·🕐·📁), o Miguel via o texto completo streamando, o turno fechava, o histórico colapsava e sobrava só o rodapé — a percepção exata de "apagou o que você escreveu".

## Cadeia completa da prova (3 camadas)

1. **Store (db.sqlite, tabela `message`/`part`):** todos os textos presentes. Ex. do turno das 08:15-08:16: seq=224 `text[4332c]` e seq=225 `text[1187c]` ("Prints A no repo... PRINT B... PRINT C...") gravados, `semantics.uiVisibility=visible` em TODAS as 187 mensagens assistant da sessão. Nada apagado.
2. **Rollout do modelo (`~/.zcode/cli/rollout/model-io-sess_a927...jsonl`):** às 08:16:45 o modelo respondeu `text`[1187c] + `toolCalls`[Bash `date '+%d/%m/%Y %H:%M'`] com `finishReason: "tool-calls"` — ou seja, o conteúdo saiu do modelo JUNTO com a chamada de ferramenta do rodapé (meio do turno). A rodada seguinte (5,5s) produziu o stub final de 194c com `finish: stop`.
3. **Bundle do app (`/opt/ZCode/resources/app.asar`, extraído em `~/tmp_zcode_asar/out/renderer/assets/styles-DyAcaLKy.js`):** `assistantHistoryDefaultOpen: !timelineOnly && (forceOpenHistory || isLastTurn && workStatus.state==='running' || ...)` — o histórico do turno abre por default SÓ rodando; ao completar, colapsa. Componente com chevron (`rotate-90`) e Collapsible confirmam o "sumiço" visual pós-turno.

## Correlação queixa×turno (janela 06/09 07:47-08:23)

| Turno completa em | Última msg do turno | Conteúdo no meio | Queixa do Miguel |
|---|---|---|---|
| 07:50:38 | text[524c] (CONTEÚDO) | — | nenhuma ✓ |
| 07:52:42 | stub 194c | 320c+137c | (ocupado c/ captcha) |
| 07:58:34 | stub 194c | 645c | — |
| 08:03:35 | stub 194c | 1434c | **08:04:12 "ué. apagou o que você escreveu. é aquele bug de novo"** |
| 08:04:34 | stub 194c | 665c | **08:09:03 "...de novo apaga..."** |
| 08:11:17 | stub 194c | 56+82+596c | — |
| 08:16:51 | stub 194c | 4332c+1187c | **08:18:05 "já sumiu de novo"** |

Regra observada: TODA vez que o turno terminou com stub-final houve (ou haveria) percepção de perda; o único turno que terminou com conteúdo-final (07:50) não gerou queixa.

## Hipóteses do prompt — placar

- **(a) Texto entre ferramentas não exibido de forma estável — CONFIRMADA (com nuance):** fica visível streamando, colapsa quando o turno completa. É desenho da UI, não perda.
- (b) Bloco do navegador embutido força re-render — DESCARTADA como causa: `browser-use turnEnded` dispara no fim do turno como parte normal do fluxo; as injeções ambiente (943c, lembrete TodoWrite) não alteram visibilidade.
- (c) Limite/buffer do markdown — DESCARTADA: turnos sem erro, `context_exceeded=0`, textos grandes persistidos; compactação só 1× (05/09 23:10, fora da janela).
- (d) `browser_turn_end` terminando turno antes da hora — DESCARTADA como anomalia: todos os turnos `status=completed` no `turn_usage`; os 2 cancelados (08:12) foram input novo do usuário.
- Extra: 19 erros `proto.staleRevision` no log às 08:21:31/08:24:50 são avisos de re-sincronia da projecção de file-changes — posteriores às queixas, não são a causa.

## Workaround + cura

1. **AGENTE (imediato, sem mexer no app):** o conteúdo essencial SÓ na MENSAGEM FINAL do turno, com NENHUMA chamada de ferramenta depois dela. Ritual do rodapé invertido: chamar `Bash date` ANTES de escrever a resposta (data pode ser buscada no início do turno), e a última mensagem carrega conteúdo completo + assinatura. Foi exatamente o que a sessão Kimi violou: conteúdo → `date` → stub.
2. **MIGUEL (recuperação):** nada se perdeu — clicar no bloco colapsado do turno (chevron/section "history") re-expande e mostra os textos intermediários; o store também pode ser lido direto (receita na memória-irmã).
3. **APP (mais longo):** bug/sugestão à Z.ai: manter histórico aberto ao completar, ou exibir digest dos textos intermediários, ou setting `forceOpenHistory`.

**Como confirmar a cura:** sessão nova, pedir tarefa com ferramentas + rodapé da casa, verificar que a ÚLTIMA mensagem visível contém a resposta completa + assinatura (não stub) e que o texto permanece na tela ≥1 min após o turno completar. Repetir 3×.

## Estado

- o que aconteceu: causa raiz provada em 3 camadas (acima).
- o que falta: propagar a regra "conteúdo só na mensagem final" aos prompts dos agentes (Kimi/GLM/GPT) que usam o rodapé da casa; opcional abrir chamado com a Z.ai.
- o que preciso do Miguel: nenhum para o workaround; "vai" se quiser que eu propague a regra para os prompts dos robôs/agentes.

**Memória-irmã:** `Memorias/memoria_bug_texto_sumindo_zcode_20260906.md` (receita técnica: queries SQL no store, decodificação do bundle, comandos).
