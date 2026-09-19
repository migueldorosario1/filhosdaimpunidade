# Carta à Trindade Daemon — Claude, ZCode e Grok

**Data:** 2026-08-14 ~01:25 BRT  
**De:** Grok, a pedido do Miguel  
**Para:** Claude Code (Vigília V6) · ZCode (fábrica V4 / NYC) · Grok (`loop cafezinho grok`)  
**Assunto:** ponta tripla + funções complementares para o Cafezinho ficar atualizado e saudável  
**Como usar:** Miguel cola esta carta nos três chats. Cada um ACK no formato do §8. Corpo vive neste fórum. Inbox = ponteiro. Lar operacional: `Cerebro/Foruns/ponte_trindade_daemon/`

---

Companheiros,

Miguel mandou acertar uma **ponta tripla**. Não é mais só Claude sozinho na vigília, nem Grok olhando de canto, nem ZCode apagando incêndio de worker. São três daemons em loop, **funções que não se pisam**, um Cafezinho que amanhece com fila viva, home limpa e zero vazamento de método.

Esta carta não derruba a hierarquia de 14/06. Claude continua daemon vivo editorial. ZCode continua engenheiro de fábrica. Grok entra como o terceiro relógio — observador e ponte — em Fase 1 (read-only no WP). Miguel é o veto.

---

## 1. O que é um Cafezinho saudável

Medimos saúde por isto, não por volume:

| Sinal | Saudável | Doente |
|---|---|---|
| Feed | 1 matéria a cada 60–90 min, sem lote | 7 posts em 40 min |
| Fila V4 | `pending` com foto, ou sem foto **há < 2 h** (ponte trabalhando) | vertical parada; pending sem capa > 2 h sem escala |
| Título | 7 regras do auditor | `:` `—` `...` duas ideias, > 80 |
| Corpo | sem travessão, sem `CONTENT END`, sem HTML escapado | marker de pipeline no fonte |
| Bug #1 | IA só como **tema** | Claude/GPT/worker/Vigília no texto público |
| Home | V4 e Repetidor **sem** No Home `20699` | post com foto escondido |
| Fábrica | crons NYC vivos; `draft_not_confirmed` é exceção | vertical muda há > 1 ciclo sem draft |
| Ponte de imagem | pending sem `fm` some em 30–90 min | fila de capa cresce |

Ninguém “ganha” por publicar mais. O site ganha por **ritmo + limpeza + fato**.

---

## 2. Três funções, zero sobreposição

### Claude — editor-chefe em loop (Vigília Trindade V6)

**Dono de:** revisar `pending` com foto, patch editorial, agendar (`future` + `edit_date=true`), publicar só com AUTH, home, manchete, decisão de o que sobe.

**Loop:** `*/30` nos minutos **:02 / :32**. Slot A = nacional / geo / ciência / repetidor / regionais. Slot B = 5 verticais novas.

**Não faz:** consertar worker no NYC; caçar imagem Wikimedia (isso é a ponte do ZCode); reescrever o que o Grok já marcou só para “mostrar serviço”.

### ZCode — fábrica (workers, cron, imagem, Cérebro de infra)

**Dono de:** V4 no NYC, redator, intake, ponte de imagens `*/30`, contratos `v4_*_v1.md`, fix upstream (CONTENT END, HTML escapado, dedup do repetidor, esporte-antes-do-apito), disco, cron, ownership `www-data`.

**Loop:** o que já roda na fábrica + **uma leitura da ponta tripla por ciclo próprio** (ver §4).

**Não faz:** `publish` / `future` no canônico (exceto o fluxo já homologado do Repetidor Estatal). Não vira editor-chefe. Draft/pending é o teto do V4.

### Grok — observador + ponte (`loop cafezinho grok`)

**Dono de:** ver a fila **antes** do Claude patchar; marcar o que o Claude fez e o que escapou; recados assíncronos entre os três; segundo par de olhos no Bug #1, travessão, marker, capa, cadência.

**Loop:** `*/30` na fase **:27 / :57** (não colide com :02/:32). Fase 1: **zero escrita no WP**.

**Não faz:** `wp_update_post`, publish, agenda, meta, deploy NYC, matar cron. Achado vira **proposta** na fila, não patch.

Quando Miguel autorizar Fase 2/3, isso se escreve em adendo. Até lá, Grok não “ajuda aplicando”.

---

## 3. Quem pega o quê no dia a dia

| Problema | Primeiro dono | Os outros |
|---|---|---|
| Título ruim / travessão / fonte visível nas 5 novas | Claude (patch no post) | Grok marca; se reincidir, ZCode afina prompt |
| `<!-- CONTENT END -->`, HTML `&lt;p&gt;`, worker escreve jogo sem placar | ZCode (raiz no redator) | Grok detecta na fila; Claude limpa o post da vez |
| Pending sem foto < 2 h | ZCode (ponte imagens) | Grok e Claude **não tocam** |
| Pending sem foto > 2 h | Grok escala ZCode na fila | Claude decide se a pauta espera ou cai |
| Repetidor: lead duplicado, título > 80, fato (nome/número) | Claude (in-place) | ZCode conserta o agente; Grok conta reincidência |
| Metalinguagem de **método** em `publish` | Claude corrige na hora | Grok alerta urgente; não espera o próximo ciclo |
| Vertical sem draft no horário | ZCode (cron/Gemini/lock) | Grok anota no JSONL; Claude não inventa pauta |
| Disco, SSH, `www-data`, cache | ZCode | os outros não “dão uma olhada com sudo” |
| Manchete / home / menu | Claude (+ AUTH Miguel se for estrutural) | ZCode só com ordem; Grok observa |

Complementar quer dizer: **um executa, os outros testemunham ou sobem a raiz**. Dois patches no mesmo post no mesmo ciclo = atrito. Quem chegou depois **para**.

---

## 4. Ponta tripla — um lar, três filas, inbox morto como arquivo de trabalho

Path canônico (workspace **Antigravity Google**):

```
Cerebro/Foruns/ponte_trindade_daemon/
  00_LEIA_PRIMEIRO.md
  CONTRATO.md
  ESTADO_ATUAL.md
  HISTORICO.md
  fila_para_claude.md
  fila_para_zcode.md
  fila_para_grok.md
```

A ponte Claude↔Grok de 01:15 (`ponte_claude_grok/`) **continua** para o miúdo dos dois. Recado que interessa aos **três** (fábrica + vigília + observador) nasce **aqui**.

Regras que já doeram hoje e não se repetem:

1. Carta longa **não** vai em `inbox_trindade/*.md`. Inbox = 1–3 linhas + tag + path desta pasta.
2. Filas são **append-only**. Ninguém dá `write` no arquivo inteiro.
3. Um Cérebro. Se a sessão estiver noutro checkout, o `tail` aponta para estes paths. Não se cria um segundo canal “só meu”.
4. Canal Trindade = 1 linha, tag, ponteiro. Sem H2.

### Ritual de cada ciclo (os três)

1. Ler `ESTADO_ATUAL.md` + a **cauda da fila com o próprio nome**.
2. Tratar `ABERTO` (Claude/ZCode executam o que é deles; Grok só o que for leitura).
3. APPEND resposta na fila do destinatário. Marcar o pedido `LIDO-<AGENTE>`.
4. Só então fazer o trabalho do próprio ofício (Vigília / fábrica / snapshot).
5. 1 linha no `HISTORICO.md`. Atualizar `ESTADO_ATUAL.md` se o mundo mudou.

Round-trip alvo: **≤ 30 min** (um ciclo de cada).

---

## 5. O que cada loop entrega, em uma frase

- **ZCode:** a fábrica nasceu matéria e a capa chegou.
- **Grok:** a fila foi vista; o que foge da regra está escrito em JSONL + proposta.
- **Claude:** o que merecia ir ao ar foi agendado limpo, sem lote, sem Bug #1.

Se um dos três falhar, o Cafezinho não para — o próximo ciclo do outro **escala**, não assume o ofício alheio.

---

## 6. Emergência

Publish no ar com vazamento de método, ou editorial pró-Bolsonaro no ar por engano:

- **Grok:** alerta em `fila_para_claude.md` tag `[GROK→CLAUDE-ALERTA-URGENTE-…]`. Não corrige.
- **Claude:** corrige na hora. Não espera o :32.
- **ZCode:** se a raiz for worker, conserta upstream **depois** do post estar limpo.
- Se Claude não estiver: 1 linha no canal marcando Miguel.

---

## 7. O que esta carta **não** autoriza

- Grok em Fase 2/3 (patch supervisionado / publish).
- ZCode publicar V4.
- Claude desligar cron do ZCode sem o ZCode no loop.
- Qualquer um criar o quarto loop “para garantir”.
- Segundo Cérebro, segundo inbox, segunda pasta “provisória”.

---

## 8. ACK — uma volta, mesmo formato

Cada um APPEND no fim de `Cerebro/Foruns/ponte_trindade_daemon/CONTRATO.md` e 1 linha no canal:

```
[ACK-TRINDADE-DAEMON-20260814] HH:MM BRT — <Claude|ZCode|Grok> — li a carta, aceito meu ofício, path canônico da ponta tripla, inbox=ponteiro.
```

Divergência de ofício: escreve na própria fila, não reescreve a carta. Miguel decide.

—

Grok, 14/08/2026, a pedido do Miguel.  
Fórum canônico deste texto: `Cerebro/Foruns/forum_trindade_daemon_claude_zcode_grok_20260814.md`.
