# ONDA 1 (V2) — Índice de coleta · 22/07/2026 · ZCode/Kimi

Base: `Claude/ESQUEMA_V2_O_FORAGIDO_INVERTIDO.md` (estrutura invertida por importância política, desenhada pelo Miguel).
Regra: tudo que é coleta da Onda 1 fica em `Kimi K3/fontes_baixadas/` (reportagens e documentos) e `Kimi K3/transcrições/` (vídeos + transcrições).

## 1. Fontes do V2 baixadas (10 links)

| Arquivo (fontes_baixadas/) | Status | Cap. |
|---|---|---|
| cap1_leiasemprebrasil_cnn_frase_20072025.html/.md | ✅ | 1 |
| cap1_forum_terra_arrasada.html/.md | ✅ | 1 |
| cap1_bbc_carta_trump_09072025 | ❌ 404 (link de feed, artigo não localizado na busca BBC) — conteúdo da carta coberto por aosfatos/apublica/migalhas + EO 14323 | 1 |
| cap1_aosfatos_nota_conjunta.html/.md | ✅ | 1 |
| cap1_apublica_agu_vazamento_21072025.html/.md | ✅ | 1 |
| cap1_extraclasse_figueiredo_fraude_06082025.html/.md | ✅ | 1, 4 |
| cap1_bdf_magnitsky_30072025.html/.md | ✅ | 1 |
| cap1_migalhas_ofac_30072025.html/.md | ✅ | 1 |
| cap4_forum_figueiredo_ustr.html/.md | ✅ | 4 |
| cap17_metropoles_tarifaco_vigor_22072026.html/.md | ✅ | 17 |
| BÔNUS: 4 artigos BBC jul/2026 (tarifaço 2) | ⚠️ curl bloqueado pela BBC (000) — URLs anotadas para nova tentativa | 17 |

## 2. Fontes primárias obtidas (além da lista do V2)

| Documento | Onde | Destaque |
|---|---|---|
| **EO 14323** "Addressing Threats to the US by the Government of Brazil" (assinada 30/07/2025, FR 05/08/2025) | `cap1_EO14323_Brasil_30072025.txt` + `.pdf` (govinfo oficial) | Fonte primária do tarifaço de 50% |
| OFAC 30/07/2025 — entrada SDN de Alexandre de Moraes [GLOMAG] | `ofac_recent_20250730.html` | Texto oficial da designação |
| Press release Tesouro sb0211 (30/07/2025) | `ofac_pr_sb0211.html/.md` | Bessent: "oppressive campaign of censorship... witch hunt" |
| OFAC 22/09/2025 — Viviane Barci de Moraes + LEX-Instituto [GLOMAG] | `ofac_recent_20250922.html` | Mesmo dia da denúncia da PGR |
| Press release Tesouro sb0257 (22/09/2025) | `ofac_pr_sb0257.html/.md` | "Support Network of Brazilian Supreme Court Justice" |
| OFAC 12/12/2025 — **Removals** (Moraes, Viviane, Lex fora da lista) | `ofac_recent_20251212.html` | A "vitória tóxica desfeita" (cap. 1, fecho) |
| **Acórdão AP 2782** (196 p.) + decisão RTF + andamentos | raiz do `Kimi K3/` | Caps. 2, 10, 18 |

## 3. Vídeos localizados e transcritos (transcrições/)

| Vídeo | Arquivo | Transcrição |
|---|---|---|
| CNN Arena 18/07/2025 (2min51s) — "Trump não vai recuar" | cnn_arena_18072025.mp4 | CNN_Arena_18072025_TRANSCRICAO.md |
| **CNN 18/07/2025 — entrevista completa (22min50s)** ⭐ | cnn_brasil_caos.mp4 | CNN_18072025_entrevista_completa_TRANSCRICAO.md — **citação canônica aos 08:43–08:53**: "O Trump não vai recuar diante de Alexandre de Moraes. Perfeito, se houver o cenário de terra arrasada, pelo menos eu estarei vingado desses ditadores de toga." Fecho (22:46): "nós restaremos vingados." |
| War Room 30/04/2025 (16min, canal do próprio Eduardo) | warroom_30042025.mp4 | warroom_30042025_TRANSCRICAO.md (em processamento) |

Método: yt-dlp (formato leve) + faster-whisper small CPU, idioma pt/en. Legendas do YouTube bloqueadas (429) — transcrição local foi a solução. Revisão humana recomendada nos nomes próprios (whisper erra fonética: "Morais", "tarifarço", "terra rasada").

## 4. Pendências da Onda 1 (para retomada)

1. **Docket USTR-2026-0331** (petição Figueiredo 01/07/2026) — regulations.gov bloqueia robô (403). Tentar portal de comentários do USTR ou acesso manual do Miguel.
2. **Petição PGR 86163** (02/07/2026, AP 2782) — petições de partes não têm link público no portal STF (só documentos judiciais). Alternativa: pedido à assessoria do MPF ou cobertura ConJur/JOTA.
3. **Artigo BBC de 09–10/07/2025** (carta de Trump) — link do V2 morto; usar EO 14323 + Aos Fatos como base; opcional: Wayback Machine.
4. **TSE 2018** — 1.843.735 votos (Pública/Ondas); confirmar no resultados.tse.jus.br na fase de checagem.
5. Vídeos complementares dos caps. 3–6 (War Room 23/04/2025, CPAC 2025, Tucker/Peterson 2024) — transcrever sob demanda na escrita de cada capítulo (pipeline pronta).
6. Revogação de vistos de 18/07/2025 (Rubio/Depto. de Estado) — comunicado oficial a localizar.
