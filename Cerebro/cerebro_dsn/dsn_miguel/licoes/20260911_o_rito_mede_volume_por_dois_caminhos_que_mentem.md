# O rito mede volume por dois caminhos — e os dois mentem em silêncio

**Data:** 11/09/2026 · ronda 418ª do DS Miguel (Dell) · BUG-20260911-DS-209
**O quê:** o ritual do DS pede a contagem de posts em 3 h, 12 h e 24 h e oferece **duas** vias: REST
(header `X-WP-Total` de `/wp-json/wp/v2/posts?after=…`) e WP-CLI
(`wp post list --post_status=publish --after="3 hours ago" --format=count`). Nesta madrugada **as duas
falharam no mesmo uso** — e nenhuma das duas avisou.

**As duas faces, medidas:**

1. **REST sem segundos ⇒ HTTP 400 lido como VAZIO.**
   `after=2026-09-11T00:31` (formato `%Y-%m-%dT%H:%M`, sem `:SS`) devolve
   `HTTP 400 {"code":"rest_invalid_date","message":"Data inválida."}`.
   O pipeline usado no rito (`curl -s -D - -o /dev/null … | grep -i '^x-wp-total:' | awk '{print $2}'`)
   **não tem header para ler** ⇒ devolve **string vazia**, que na leitura humana vira «0 posts» / «sem dado».
   Com `after=2026-09-11T00:32:51` (local, com segundos) ⇒ `http=200`, `x-wp-total: 1`.

2. **WP-CLI `--after` é IGNORADO em silêncio ⇒ devolve o TOTAL histórico.**
   WP-CLI **2.11.0**: `wp help post list` **não menciona `after`** (0 ocorrências) — o argumento é aceito
   sem erro e **não filtra nada**. Provas: `--after="2026-09-11 00:00:00"` → **79111**;
   `--after="3 hours ago"` → **79111**; `--after="2030-01-01 00:00:00"` (data impossível) → **79111**.
   E **79111 é exatamente o `X-WP-Total`** de todos os publicados = **total histórico**, não janela.

**Por quê isso machuca:** quem responde à pergunta errada **erra barato e erra feio**. Um `0` falso vira
alarme de «esteira seca»; um `79111` falso vira «tudo normal». Nas duas pontas o operador humano confia
porque o número **existe** — só não é o número da janela pedida.

**Como aplicar (régua que fica):**

- **Capture o status junto do dado:** `curl -w "http=%{http_code}"` (ou `-D -` **e** o código). Valor
  ausente é **erro**, nunca zero. Se o header não vier, o `http_code` diz por quê.
- **Nunca `2>/dev/null` em comando de medição:** foi o stderr suprimido que escondeu o `--after` ignorado.
- **Sanidade aritmética antes de publicar:** o número da janela **nunca** pode ser igual (nem maior) ao
  total; e `3h ≤ 6h ≤ 12h ≤ 24h ≤ hoje+ontem`. Se a razão entre janelas for ~1,00, a janela não foi aplicada.
- **Data no REST:** `YYYY-MM-DDTHH:MM:SS` em **hora local** (a lição de 03/09 continua valendo: `date -u`
  faz a janela sair de `date`, não de `date -u`).
- **Duas vias só valem se discordarem em voz alta:** comparar os dois caminhos e tratar divergência como
  **falha de instrumento**, não como dado.

**Família:** 17ª ocorrência da família «o instrumento responde à pergunta errada» — e a 3ª em 6 rondas em que
**a minha própria medição** devolveu zero falso (413ª `date -u` no `after`; 416ª `grep` somando
`x-wp-total` + `x-wp-totalpages`; esta).

**Refs:** `DS-Dell-20260911-008` · memória viva (Ronda 418ª) · `CEREBRO_NODE_BUGS_ATIVOS.md` BUG-20260911-DS-209.
