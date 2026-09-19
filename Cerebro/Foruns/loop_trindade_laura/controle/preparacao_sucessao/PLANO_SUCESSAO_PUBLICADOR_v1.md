# PLANO DE SUCESSÃO — protocolos para o dia em que a Laura assumir a publicação

```yaml
tipo: PLANO_DE_PREPARACAO
autoridade: ORDEM_MIGUEL 20/08/2026 ~20:45 — "se preparar para assumir; protocolos para errar menos e se sentir mais segura"
autor: LAURA-CLAUDE (chefe do Loop Laura, Claude Opus 5)
estado: PRONTO_NAO_ATIVO — ativação é decisão de Miguel, não minha
fonte_de_conhecimento: cerebro/claude_memory/ (sincronizando; último sync 20/08 14:00) + memoria_claude_miguel local (495 arquivos)
```

## 0. O princípio do plano

Publicar não é um ato: é uma **cadeia** — e cada elo já quebrou uma vez nesta
semana, com registro. Estes protocolos existem porque cada um deles nasceu de
um erro real, meu ou do ecossistema. Nenhum é teórico.

## P1 — PROTOCOLO DE ABERTURA DE TURNO (antes de tocar em qualquer post)

1. Gate do relógio: hora externa × local × idade do meu heartbeat (desvio >60s
   ou lacuna acima do limiar ⇒ declarar antes de operar).
2. `git pull` + varredura **por mtime** da árvore (lição 15).
3. Ler as memórias novas do Claude Miguel (`claude_memory/`, por mtime) — as
   diretrizes dele mudam diariamente e **eu herdo as regras, não só a função**.
4. Fila `future` item a item (lição 14): total, datas, cobertura em horas.
5. Conferir HOLDs vivos e autorizações pendentes.
   *Origem: ERRO-1303/1752 (grade abandonada), ERRO-0125 (varredura estreita).*

## P2 — PROTOCOLO DE SELEÇÃO (o que pode ir ao ar)

1. **Frescor** calculado, não opinado: idade do fato × mínimo da vertical
   (PROPOSTA_FRESCOR_v1). Fato sem data descoberta = não publica.
2. **Anacronismo**: ID muito abaixo da faixa corrente ⇒ conferir se o verbo do
   título ainda é verdade (casos 266189, 266751).
3. **Dedup por núcleo factual**, não por assunto (caso 266330/266364/266398:
   três peças, um fato).
4. **Título 7/7** nas regras canônicas + §127 (uma ideia; sem juízo editorial
   na segunda metade).
5. **Camada Brasil presente** quando a vertical exigir (caso 266751).
6. **Fontes**: mínimo 3 nomeadas; "analistas apontam" não conta.

## P3 — PROTOCOLO DO ATO DE PUBLICAR

1. **Reserva no livro** antes (anti-atropelo — 6 mãos no mesmo WP).
2. **Gate de imagem**: `_cafezinho_img_check ok:true` presente **e posterior**
   à última troca de mídia. Sem visão minha ⇒ parecer do Grok, nunca metadado.
3. **Gate de fuso**: `post_date_gmt = post_date + 3h`, sempre — recusar o ato
   se divergir (bug de 18/08: 2 posts publicados 3h antes; 8 presos com GMT
   zerado).
4. **Agendar > publicar**: sempre que possível, criar `future` e deixar o
   WordPress executar — o ato irreversível fica com a máquina, auditável.
5. **Colchão**: nunca encerrar turno com fila cobrindo menos de 2-3h (lição
   14; os silêncios de 1h01 e 56 min).
6. **Trilha**: cada publish/agendamento = linha no ledger com antes/depois.

## P4 — PROTOCOLO DE ERRO (quando eu errar — e eu vou)

1. Publicou errado ⇒ **corrigir é prioridade sobre explicar**; despublicar só
   com registro de motivo.
2. Registrar no diário **no mesmo ciclo**, com gate novo (cultura das 5 fases).
3. Erro que muda sentido do que o leitor já leu ⇒ nota de correção no post,
   não edição silenciosa.
4. **Reconferir correção própria aplicada** na ronda seguinte (lição 12 — a
   repetição do Kushner era minha).

## P5 — PROTOCOLO DE PRESENÇA (a minha fraqueza número 1)

1. Ronda como **tarefa agendada do SO** — pré-condição de ativação, não
   desejo. 6 lacunas em 3 dias provam que despertador de sessão não serve
   para um publicador.
2. Heartbeat com hora externa + `ultima_acao_material` toda ronda.
3. **Vigilância cruzada**: Grok confere meu sinal (45 min), eu o dele (90).
4. Se eu cair no meio de um turno de publicação: o que estiver **agendado
   continua saindo** (é por isso que P3.4 manda agendar) — degradação suave
   em vez de silêncio.

## P6 — PROTOCOLO DE HUMILDADE OPERACIONAL

1. `segunda_opiniao:` declarada em todo veredito (AUSENTE quando for).
2. Mudança de **sentido** (não typo) em post alheio ⇒ comunicar antes.
3. O que eu não consigo medir, eu declaro (`credito: NAO_MENSURAVEL`) — campo
   vazio mente, campo declarado informa.
4. Reprodutibilidade decide, não autoridade — comando público junto de cada
   medição que sustente decisão.

## Condições de ativação (o "quando", que é de Miguel)

1. Ronda do chefe como tarefa agendada ✦ **bloqueante**
2. `schedule` liberado na whitelist (não `publish` — ver P3.4)
3. Gate visual delegado ao Grok por escrito
4. Piloto de janela (madrugada) com auditoria do CM e métrica: zero fora de
   grade · zero correção por erro meu · zero silêncio não declarado
5. Se houver upgrade de modelo (Fable), refazer o piloto do zero — modelo
   novo, prova nova.

— LAURA-CLAUDE, chefe do Loop Laura
