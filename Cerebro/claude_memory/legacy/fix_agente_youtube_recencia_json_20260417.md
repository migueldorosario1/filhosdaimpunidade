---
name: Fix Agente YouTube — filtro recência 6h + parser JSON resiliente (2026-04-17)
description: Dois bugs corrigidos: publicava vídeos de semanas atrás (sem filtro de data) e título caía no fallback "Sabatina Exclusiva" quando JSON do Editor Chefe vinha malformado.
type: project
originSessionId: 82c307d7-bd07-4c7a-8ed2-9e86b6fa4e22
---
Em 2026-04-17 o `agente_youtube.py` publicou um post intitulado literalmente "Sabatina Exclusiva" referente a um vídeo ANTIGO do Judging Freedom com o presidente iraniano Pezeshkian. Antigravity diagnosticou os 2 bugs; Claude Code implementou os 2 fixes.

## Bug 1 — Vídeo antigo sendo publicado (filtro de recência)

**Causa:** `monitorar_canais()` (linhas 468-477) só checava se o `video_id` estava no `agent_data/youtube_vistos.json`. O RSS do YouTube entrega os **últimos 15 vídeos** do canal, independente da idade. Quando um canal novo entrava na whitelist ou o robô ficava offline por algumas horas, o vídeo mais recente do RSS (mesmo que de dias/semanas atrás) era tratado como "inédito".

**Fix (linhas 468-495):**
- Importado `datetime, timezone, timedelta` no topo.
- Leitura da tag `atom:published` do RSS Atom.
- Se `idade > timedelta(hours=6)`: descarta + marca como visto + `continue`.
- Cadência de publicação do canal: ~1/dia. Patrulha RSS a cada hora (`25 * * * *`). Janela de 6h dá ~6 oportunidades de captura antes de virar "velho".

**Miguel quis 6h (não 24h):** canais da whitelist postam todo dia → sempre há fresco; janela apertada evita resenhas de vídeos da noite anterior.

## Bug 2 — Título fallback "Sabatina Exclusiva"

**Causa:** try/except (linhas 217-232) abraçava o `json.loads` da resposta do Editor Chefe. Quando o LLM devolvia JSON com markdown (```` ```json ````), aspas curvas ("" ''), ou trailing commas, o parse falhava e caía no fallback hardcoded `titulo_post = "Sabatina Exclusiva"`. Todo o pipeline do Redator (linhas 241-302) funcionava corretamente — só o título saía genérico.

**Fix (linhas 219-285):**
- Função `_sanear_json_bruto(s)`: strip de ```` ```json ```` e ```` ``` ````, troca aspas curvas (`\u201c\u201d\u2018\u2019`) por retas, remove trailing commas com regex `,(\s*[}\]])`.
- Função `_parse_editor(raw)`: tenta `json.loads` após sanear; devolve dict ou None.
- **Retry minimalista** se 1ª tentativa falhar: nova chamada `generate_text` com prompt enxuto pedindo só JSON essencial (texto truncado em 6000 chars, agente `youtube_profundo_editor_retry`).
- Só cai em "Sabatina Exclusiva" + categoria default "Geopolítica" se **ambos** (parse inicial + retry) falharem.
- Loga `editor_out[:400]` no fallback final, pra diagnóstico futuro.

## Regras jornalísticas preservadas

Todas as regras que Miguel e Antigravity construíram na noite de 16→17/04 permanecem intactas:
- Título `[NOME REAL]: "Frase Mais Impactante"` (linha 194)
- NUNCA traduzir nomes de canais (Judging Freedom, linha 195)
- Alerta anti-jabá (linha 197)
- ESTRUTURA JORNALÍSTICA (INVERSÃO DE EXPECTATIVA) — sem chapéus, sem H2/H3, cargo antes do nome, 3º parágrafo com contexto do canal (linhas 296-299)
- Padrão Financial Times: 2 frases por parágrafo (linha 302)
- Memória anti-repetição `memoria_youtube.jsonl` (linha 126)

## Backup no servidor

`/root/agente_youtube.py.bak_20260417_1245`

## How to apply

- **Se voltar a publicar vídeo velho:** conferir `agent_data/youtube_vistos.json` (se o `video_id` já estava lá, o filtro dos 6h não é o problema) e o log da patrulha RSS para ver se `atom:published` está sendo lido.
- **Se voltar "Sabatina Exclusiva":** conferir log do Editor Chefe — agora o except final imprime `editor_out[:400]`. Se for sempre o mesmo padrão de erro, refinar o `_sanear_json_bruto`.
- **Ajustar janela de recência:** trocar `timedelta(hours=6)` no loop de `monitorar_canais`. Máximo seguro é o intervalo da patrulha + folga (patrulha é 1h → filtro mínimo recomendado 2h).
