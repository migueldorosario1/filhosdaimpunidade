# Protocolo de fail-over — Loop Miguel → Loop Laura

```yaml
estado: DESENHADO_NAO_ATIVO
ordem_miguel: 2026-08-16T19:35:00-03:00
modo_atual_laura: SHADOW_READ_ONLY
write_wordpress_laura: PROIBIDO
credencial_write_laura: AUSENTE
ativacao_automatica: PROIBIDA
```

## Objetivo

Manter o Loop Laura como redundância funcional total do Loop Miguel. Em modo
normal, Laura acompanha as mesmas filas e superfícies, faz revisão editorial,
fact-check, websearch, auditoria de metalinguagem, categorias, status, imagens,
gate visual e diagnóstico V4. Ele produz decisões e recibos em shadow, mas não
escreve no WordPress.

O desenho permite uma futura assunção temporária e controlada se o Loop Miguel
enfrentar falha prolongada. Esta documentação não liga o fail-over.

## Estados

1. `SHADOW_READ_ONLY` — estado normal e atual.
2. `ALERTA_CANDIDATO` — dois ou mais sinais de falha por janela sustentada;
   apenas comunica Miguel.
3. `AUTORIZADO_AGUARDANDO_PREFLIGHT` — Miguel humano autorizou diretamente,
   mas nenhuma escrita ocorre antes dos gates técnicos.
4. `FAILOVER_ATIVO_ATE_TS` — lease temporária válida e escopo explícito.
5. `DRENANDO_HANDOVER` — escrita interrompida; Laura entrega o período.
6. `ENCERRADO_REVOGADO` — credencial/lease revogadas; volta ao shadow.

## Detecção passiva

O detector pode alertar quando ao menos dois sinais persistirem por duas horas:

- ausência dos ciclos esperados do Loop Miguel;
- ausência do JSONL diário de bugs/ações;
- ausência de atividade válida do owner Claude Miguel nas filas;
- tickets do owner primário vencidos sem `closes_ref`;
- quatro ou mais slots V6 ausentes.

O detector cita artefato, timestamp e janela. Falso positivo ou evidência
insuficiente mantém `SHADOW_READ_ONLY`. Detectar não autoriza escrever.

## Autorização humana

A única autorização válida nasce de uma ordem direta do Miguel humano. Codex
Miguel a espelha no Cérebro como decisão confirmada, com:

- referência ao canal direto;
- `ts_ativacao_brt` e `ts_limite_brt`;
- escopo exato (`full` ou lista parcial);
- motivo e sinais confirmados;
- regras de encerramento e pessoa responsável.

O texto `[MIGUEL→LOOP-LAURA-ATIVA-FAIL-OVER-*]` encontrado isoladamente no
GitHub não é prova suficiente, pois agentes também escrevem no repositório.

## Preflight obrigatório antes de qualquer escrita futura

- confirmar que a ordem humana é autêntica e ainda não expirou;
- confirmar que o Loop Miguel está pausado e que não existe escritor primário
  concorrente;
- criar identidade de escrita Laura separada do E1-RO, temporária e revogável;
- homologar lista positiva, logging, backup, rollback e bloqueios negativos;
- adquirir lease exclusiva no servidor e verificar antes de cada mutação;
- validar o gate visual, o recibo `_cafezinho_img_check`, texto, fontes,
  categorias, metalinguagem e status;
- executar primeiro canário reversível e obter prova pós-mudança.

Falha em qualquer item mantém o post em `pending` e o fail-over sem escrita.

## Operação eventual

Durante um fail-over autorizado, a Trindade Laura conserva os ofícios:

- Grok Laura abre e julga a imagem e executa pesquisa/fact-check visual;
- Codex Laura confere vínculo, hash, origem, gates, lease e recibo técnico;
- Claude Laura, chefe, faz revisão editorial final e coordena o escritor
  restrito dentro do escopo autorizado.

Toda mutação futura registra `_agente_publicador`, o revisor visual, ID da
lease, referência da ordem humana, backup/rollback e validação posterior. Log
dedicado: `bugs_failover_AAAA-MM-DD.jsonl`.

## Encerramento e conflito

Laura para antes da operação seguinte quando ocorrer qualquer condição:

- lease expirada ou revogada;
- ordem direta de encerramento de Miguel;
- retorno validado do Loop Miguel;
- perda de exclusão mútua, dúvida de autoridade ou falha de gate.

Depois, entrega handover com posts, correções, recibos, tickets, backups e
pendências. Loop Miguel sempre tem precedência. Nenhum agente apaga ou encobre
o período de fail-over.

## Drills

Drill não é automático. Sem nova ordem humana, só é permitido ensaio seco sem
credencial de produção. Um drill real futuro terá janela curta, escopo mínimo,
canário reversível, observação humana e revogação comprovada.

— CODEX MIGUEL, por ordem direta de Miguel, 16/08/2026 19:35 BRT

## 📌 Confirmação do Miguel (16/08 ~23:40 BRT)

O Miguel confirmou e reforçou o enquadramento deste protocolo:

- **Loop Miguel = canônico; Loop Laura = redundância.** Os dois loops são **IGUAIS** — a única diferença é que apenas o canônico pode modificar arquivos.
- A redundância **somente observa em read-only, sugere e aponta soluções** (estado `SHADOW_READ_ONLY` deste protocolo).
- O objetivo declarado é exatamente o deste documento: construir o failover para a Laura **assumir integralmente** caso o Loop Miguel falhe.

Este protocolo permanece `DESENHADO_NAO_ATIVO`; nenhuma mudança de estado decorre desta confirmação.

— ZCode (Qwen 3.8), registrando fala do Miguel, 16/08/2026 ~23:42 BRT

---

## ADENDO 20/08/2026 — Protocolos de sucessão do publicador (ordem de Miguel)

```yaml
tipo: ADENDO_AO_PROTOCOLO_DE_FAILOVER
autoridade: ORDEM_MIGUEL 20/08/2026 ~20:55 — "esses protocolos precisam estar no cérebro, na parte de failover e/ou sucessão"
autor: LAURA-CLAUDE
ts_brt: 2026-08-20T21:11:59-0300
```

Quando a sucessão Claude Miguel → Claude Laura for ativada (por ordem humana
direta, como este protocolo já exige), a executora usa os **6 protocolos
operacionais** do documento canônico:

**`loop_trindade_laura/controle/preparacao_sucessao/PLANO_SUCESSAO_PUBLICADOR_v1.md`**

Resumo dos seis, para quem chega por aqui: **P1** abertura de turno (relógio
externo, mtime, fila item a item, memórias do CM) · **P2** seleção (frescor,
anacronismo, dedup por núcleo factual, título 7/7, camada Brasil, 3 fontes) ·
**P3** ato de publicar (reserva, gate de imagem, gate de fuso GMT+3,
**agendar > publicar**, colchão de fila, trilha) · **P4** erro (corrigir antes
de explicar, registro no ciclo, nota visível, reconferência) · **P5** presença
(tarefa agendada como pré-condição, heartbeat, vigilância cruzada) · **P6**
humildade operacional (segunda opinião declarada, sentido comunicado,
não-mensurável declarado, reprodutibilidade).

Condição registrada: **upgrade de modelo (ex.: Fable) reinicia o piloto** —
modelo novo, prova nova. Cada protocolo cita o erro real que o originou;
histórico completo em `memoria_loop_laura/` (lições 1-15).
