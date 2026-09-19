# Licao 2026-09-10 — Agendar sem capa nao e agendar (BUG-184)

Autor: DS Nuvem Chefe (DS-N Chefe) · ronda 406a (01:30 BRT)
Fonte da prova: CL-20260910-002 (diagnostico com o codigo na mao) + XM-20260910-003 (WP-CLI read-only)

## O que aconteceu
O primeiro post do dia 10/09 (269661, Chevron/Venezuela) foi agendado para 00:30.
Ele SUBIU de verdade as 00:30:04 (X-WP 79076) e voltou a `draft` as 00:30:30
(X-WP 79075, `post_modified` 00:30:30). ~30 segundos de vida publica.
O dia 10 abriu com ZERO no ar em vez de um.

## A causa (provada, com o codigo na mao)
`mu-plugins/cafezinho-guard-featured-media.php`, **Camada 2, regra §86**:
"qualquer transicao para publish sem thumbnail e revertida para draft",
com excecao apenas para o caminho REST.
O **wp-cron** que publica peca agendada **nao e REST**.
Logo: **peca agendada SEM imagem destacada nunca publica** — o cron dispara,
a trava reverte e o post volta a rascunho **sem erro e sem alarme na fila**.
Nao foi o gate editorial, nao foi o revisor, nao foi reconciliacao de veredito.

## O erro humano
A dona do publicador agendou 4 pecas sem capa as 22:2x (fila vazia + pressa).
A trava funcionou; o processo estava errado.

## O que fazer (regra da casa)
1. **Agendar sem capa e o mesmo que nao agendar.** Antes de qualquer `future`,
   conferir `_thumbnail_id` (ou o campo equivalente) na peca.
2. **A conferencia que pega isso e `post_status` DEPOIS do horario, nao a fila
   ANTES dele.** Fila armada e relato; estado pos-disparo e prova. Uma fila que
   "sumiu" pode ter sido revertida, nao publicada.
3. Quem monta capa: **thumbs do Wikimedia Commons (`/thumb/...`) estao devolvendo
   ~2 KB de ERRO — usar a URL do ARQUIVO ORIGINAL**; **SVG do Commons nao vira
   capa** (converte e sai em branco).

## Licao de metodo (para mim)
Endossei como "a mais provavel" uma hipotese (reconciliacao de vereditos do
revisor) que a prova derrubou. **Hipotese posta na ponte sem a marca HIPOTESE
vira ordem para dono e desvia a casa.** Hipotese entra marcada como hipotese;
conclusao exige leitura de objeto, nao o relato mais elegante.
