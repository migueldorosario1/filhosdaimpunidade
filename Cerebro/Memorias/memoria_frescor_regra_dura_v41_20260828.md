# 🧠 Memória — FRESCOR regra dura no V4.1 (caso-escola 96h) + sabatina Lula JN na capa (28/08/2026)

> Log técnico completo da missão. Fórum-irmão (decisões): `Foruns/forum_frescor_regra_dura_v41_sabatina_lula_jn_20260828.md`.

## Ordem (Miguel, 28/08 ~01:47 BRT)

Matéria fria no bloco Nacional (entrevista do Lula de domingo vista na sexta de madrugada) → endurecer o frescor no loop todo; publicar na capa a sabatina do Lula no JN de 27/08 à noite com foto e transcrição. Adendo (~01:55): o post frio **não** é para tirar — remover prejudica SEO; é para aprender a não ser mais frio e jogar o quente logo.

## Rastreio do caso-escola (post 268033)

- Post frio **268033** ("Lula nega blindagem a familiares em investigação da PF"), `_v4_versao=4.1`, `zizi_job_id=v41_nacional_e88bb07b5659`, publicado 27/08 22:55 — sobre a entrevista do Lula à **Record de domingo 23/08** (~96h).
- Logs `/root/v4_labs/dados/v41_ciclo/20260823_{2226,2326,240026...}.json` → a pauta `e88bb07b5659f8e4` entrou 23/08 22:26 e foi **barrada 3× pelo juiz** (anti_repeticao, "mera expansão da matéria anterior").
- Log `20260827_2126.json` → 96h depois a mesma pauta voltou (status `drafted` no `nacional.sqlite3`, seleção sem filtro de data + dedupe só 24h), tese aprovada, rascunho criado 21:26, publicado 22:55.
- **Raiz:** o juiz media repetição (<48h do último publicado); nenhuma camada media a **idade do fato**.

## Patch V41_FRESCOR_20260828 (`/root/v4_labs/codigo/v41_ciclo.py`, NYC)

Backup `v41_ciclo.py.bak_pre_frescor_20260828`. Duas camadas, alinhadas à doutrina `diretrizes_coleta_curadoria_frescor_v5.md` (hard news = nota 4-5 = ≤24h):

1. **Seleção:** `_FRESCOR_H = {nacional:24, economia:24, geopolitica:24, ciencia:48, saude:48, esporte:48, meio_ambiente:48, digital:48, cultura:72}` → `_fresco_sql = " AND collected_at >= datetime('now','-N hours')"` aplicado às queries de `drafted` E das sobras `new` (antes sem filtro). SELECT agora inclui `collected_at`.
2. **Juiz inter-vertical:** prompt ganhou `COLETADA_EM (UTC)` + `AGORA (UTC)` + **REGRA DO FRESCOR** — idade do FATO CENTRAL > teto da vertical sem fato novo material ⇒ `repetida=true`, motivo `pauta_fria`.

**Provas:** (a) sqlite: pauta `e88bb07b5659` (23/08) BARRADA pela janela 24h; sobras `new` de 27/08 elegíveis; (b) ciclo real 28/08 02:17 (`20260828_0217.json`): pauta "Propaganda no rádio e na TV começa nesta sexta (28)" → rascunho **268079** ("Haddad terá menos da metade do tempo de Tarcísio na propaganda", 4.272 chars, gpt-5.5, FC sonnet ok, coerência calendárica confirmada). Detalhe: `drafted` elegíveis = 0 hoje porque o worker V4 (que marcava drafted) foi desligado em 24/08 — o ciclo nacional vive das sobras `new`, todas frescas.

## Matéria quente (post 268078)

- **Transcrição:** vídeo da íntegra (live Lindbergh Farias, link do Miguel) baixada no Dell com `youtube-transcript-api` (sem bot-check — IP residencial passou): 1.370 segmentos, ~54 min, `/tmp/lula_jn_texto.txt` (blocos de 60s com timestamp). Trechos-chave localizados: "eu sou Fábio" 04:17 · "não conheço essa moça" 07:27 · Marcola/pai 10:35-12:39 · **"Ministério Público aqui" 22:10** · dívida EUA 120%/40tri 23:15-24:21 · "fazer este país crescer" 27:31 · Correios 31:52 · temas ausentes confirmados por grep (trem/ferrovia/solar/mobilidade = 0 ocorrências).
- **Foto:** oficial Stuckert deixada pelo Miguel em `Outros/pautas editoriais o cafezinho/Dia a dia/2026 ago 28/lula/55492848065_9b375e681b_c.jpg` (800×533). MD5 `a9894da3692408950529e8a6800c5211` **livre no manifesto** → mídia **268077** (caption oficial completa).
- **Publicação (canônico cafezinho-wp):** `wp post create` (autor 5470 Redação, cats 22+2403) → **268078**. Armadilhas vencidas: (1) o servidor criou o post com data adiante do fuso do WP (America/Sao_Paulo) → virou `future`; fix via SQL direto (`post_date=UTC_TIMESTAMP()-3h`, status publish); (2) `_thumbnail_id` barrado pela Emenda 7 com carimbo "ok" simples — o formato atual exige **JSON com media_id casado** (`{"ok":true,"ts":...,"agent":...,"media_id":268077,"source":...,"license":...,"alt_text":...,"caption":...}`) gravado ANTES do thumb. Conferido via SQL.
- **Manchete:** `CMH_Manchete_Humana::gravar_manchete(268078)` + `aplicar_trava(268078, 8, "zcode-kimi-k3")` (até ~10:07 BRT) + purge rocket/cache. Provas: HTTP 200, `og:image`=lula-jn-stuckert.jpg, `<h1 class="manchete-titulo">` na home (4 ocorrências do link).
- **Texto:** ~1.100 palavras, **zero dois-pontos** (grep `:` = 0), linha editorial do Miguel integral (ilações, aula de economia, temas ausentes, clichê = programa de Flávio Bolsonaro, obrigação moral do JN na sexta).

## Lições duráveis

1. **Repetição ≠ frescor.** Juiz anti-repetição (janela de publicação) não barra pauta velha nunca escrita. Frescor exige régua própria: idade do fato na seleção E no juiz.
2. **`drafted` sem janela é pauta-zumbi** — qualquer fila sem teto de idade ressuscita matéria fria dias depois (dedupe de 24h não protege: passado o prazo, volta).
3. **Emenda 7 atual exige carimbo JSON com media_id casado** — o "ok" simples de posts antigos não vale mais; gravar o JSON antes do `_thumbnail_id` e conferir por SQL.
4. **Fuso do canônico:** `wp post create` herdou hora adiante do WP → status `future`. Corrigir por SQL (`UTC_TIMESTAMP()-3h`) ou gravar `post_date` explícito no fuso do WP.
5. **YouTube pelo IP residencial do Dell passou** (youtube-transcript-api 1.2.4 direto, sem proxy) — via preferencial para transcrições pontuais quando o bot-check fecha os servidores.

## Pendências

- Ronda seguinte confere logs dos próximos ciclos (cron minuto 25, 2/2h): espera-se `pauta_fria` barrando velhas e zero escrita de pauta >teto.
- Opcional (aguarda "vai"): matéria-espelho pós-sabatina de Flávio Bolsonaro no JN (sexta à noite) cobrando a mesma régua — transcrição pelo mesmo caminho.

— ZCode/Kimi K3, 28/08/2026 ~02:50 BRT
