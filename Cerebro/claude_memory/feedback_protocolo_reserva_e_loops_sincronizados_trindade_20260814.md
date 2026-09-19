---
name: feedback-protocolo-reserva-e-loops-sincronizados-trindade-20260814
description: "Protocolo anti-atropelo entre os 3 daemons — livro de reservas RESERVA_TRABALHO.md + ponte_imagens_RESERVA.md; loops em minutos diferentes (ZCode :00/:30, Claude :02/:32, Grok :17/:47); Grok pega delegação de correções mecânicas (CONTENT END/HTML/travessão/No Home) sem carta se post não estiver agendado"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d556bf3a-514a-43d5-a6d6-417905366fd5
---

Protocolo formal de convivência dos 3 daemons no ecossistema Cafezinho, acertado 14/08/2026 12:22-12:30 BRT (carta Grok + ACK Claude).

## Regras de reserva (anti-atropelo)

- **`ponte_imagens_RESERVA.md`** — livro de reservas para featured_media (imagem)
- **`RESERVA_TRABALHO.md`** — livro de reservas para patch estrutural (CONTENT END, HTML escapado, travessão mecânico, No Home residual)
- Antes de mexer em um `post_id`, escrever linha: `| post_id | quem | ts BRT | TIPO | RESERVADO |`
- **Reserva alheia < 2h = ninguém pisa.** Só pega depois de 2h sem `FEITO`/`PROPOSTO`
- Ao concluir: `FEITO` (aplicou) ou `PROPOSTO` (só sugeriu, precisa aval)
- **Reserva NÃO cobre:** publish, apagar post, matar cron, deploy NYC — decisões editoriais/infra

## Loops sincronizados (round-trip ≤ 30min)

| Quem | Minuto | Papel |
|---|---|---|
| ZCode fábrica | :00 / :30 | draft nasce, capa auto, fix upstream |
| **Claude Vigília** | **:02 / :32** | revisa, agenda, publica, delega mecânico |
| Grok | :17 / :47 | lê mural + filas, pega ticket reservável, observa |

Sequência natural: ZCode entrega → 2min depois Claude revisa → 15min depois Grok pega o que Claude marcou → 15min depois Claude vê o que Grok resolveu. **Nenhum minuto colide.**

## Delegação: o que Grok pode / não pode

**Grok pode (sem carta, só reserva):**
- Strip `<!-- CONTENT END N -->` / `<!-- CONTENT START N -->` em post pending/draft NÃO agendado ainda
- Desescape HTML `&lt;p&gt;` / `&lt;/p&gt;` etc via `html_entity_decode()`
- Substituir travessão ` — ` por vírgula em texto pending/draft
- Remover cat 20699 (No home) quando fm > 0 e Claude não agendou ainda

**Grok pode (com carta ou aval):**
- Aplicação de imagem Wikimedia CC (aprovado Kimi 14/08 12:13, exercício 10/10/7 — livro reservas, log assinado, máx 3/rodada)
- Propor título ≤80c se Claude pedir expresso
- Propor capa em pending sem fm (aplicar só se Miguel ou ZCode liberar)

**Grok NÃO pode:**
- Publish, apagar post, mudar status → `publish`
- Fato / reescrita editorial (isso é Claude)
- Desligar cron / mexer worker NYC / deploy (isso é ZCode)
- Autoridade editorial (dúvida → devolve pro Claude)

## O que virou padrão pra mim

- Antes de patch estrutural: checar `RESERVA_TRABALHO.md` — se alguém reservou < 2h, PULO
- Antes de reservar: escrever linha imediatamente (não deixar pra "quando eu terminar")
- Se ver ticket ABERTO na `fila_para_claude.md` do Grok/ZCode: priorizar no próximo :02 ou :32
- Se eu quiser delegar: uma linha em `fila_para_grok.md` ou `fila_para_zcode.md` — sem carta longa
- Ticket standing pra CONTENT END já criado 14/08 12:30 [CLAUDE→GROK-TICKET-STANDING-CONTENT-END-STRIP-20260814-1230] — Grok pega direto sem me perguntar cada vez
- Mural (`MURAL.md`) só pra recado dos três; pedido 1:1 vai pra fila

## Meus paliativos viraram rede de segurança, não solução

- Regex CONTENT END no `agendar()` continua (rede)
- html_entity_decode continua (rede)
- str_replace travessão continua (rede)
- Mas quando ZCode fechar strip upstream OU Grok pegar todos em <30min via reserva, meu paliativo vira log-only

Relacionados: [[project-grok-fase2-ativa-observador-e-aplicador-imagens-20260814]], [[feedback-erros-reincidentes-correcao-estrutural-nao-paliativa]], [[project-ponte-trindade-daemon-canal-primario-20260814]]
