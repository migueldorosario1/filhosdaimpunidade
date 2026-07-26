# 🎬 CATÁLOGO DE TRANSCRIÇÕES — Entrevistas de Eduardo Bolsonaro

**Levantamento em 25/07/2026 · ZCode/Kimi.** Pasta de trabalho: `Kimi K3/transcrições/` (pipeline: yt-dlp + faster-whisper local).
Legenda: ✅ transcrito · ⏳ na fila · 📝 fonte escrita (não precisa de vídeo).

---

## ✅ JÁ TEMOS (transcritas e revisáveis)

| # | Entrevista | Data | Duração | Arquivo | Cap. V2 |
|---|---|---|---|---|---|
| 1 | **CNN Brasil — entrevista completa** ("Brasil será mergulhado no caos") | 18/07/2025 | 22m50s | `CNN_18072025_entrevista_completa_TRANSCRICAO.md` | **1** ⭐ (frase canônica aos 08:43) |
| 2 | CNN Arena — corte ("Trump não vai recuar") | 18/07/2025 | 2m51s | `CNN_Arena_18072025_TRANSCRICAO.md` | 1 |
| 3 | **War Room/Bannon** (canal do próprio Eduardo) | 30/04/2025 | 16m | `WarRoom_30042025_TRANSCRICAO.md` (inglês) | 3, 10 |

**Bônus em texto no acervo:** transcrição do podcast sobre a condenação de Guo (`Fontes/Variados/Docs/This_scandal_says_everything...mp3.txt`, inglês, 36k) — cap. 13; transcrição Dal Piva (`Reportagens/DOSSIÊ...mp3.docx`) — Vol. 2.

---

## ⏳ FILA DE TRANSCRIÇÃO (prioridade = municiamento dos capítulos do V2)

### Prioridade A — trava capítulos do V2
| # | Entrevista | Data | Por que | Cap. V2 | Link/status |
|---|---|---|---|---|---|
| A1 | **BBC News Brasil** | 13/08/2025 | É a **conduta nº 8 do acórdão** ("confissão expressa" de Moraes) | 2, 10 | bbc.com/portuguese/articles/c987e8znyg9o |
| A2 | **War Room, 2º episódio** (Battleground EP 753) | 23/04/2025 | Buildup da campanha de pressão | 3, 10 | warroom.org / blog Bannon |
| A3 | **CPAC 2025** (discurso; Bannon o chama "próximo presidente do Brasil") | jan-fev/2025 | O palco da internacionalização | 3, 11 | YouTube CPAC USA / Forbes |
| A4 | **Newsmax** | 28/06/2025 | Pré-tarifaço, pedidos a Trump | 10 | canal Newsmax |
| A5 | **Reuters TV — Washington** | ago/2025 | Advertências sobre sanções (cronologia da AP) | 10 | Reuters vídeo |

### Prioridade B — arco longo (2018–2024)
| # | Entrevista | Data | Cap. V2 | Link/status |
|---|---|---|---|---|
| B1 | **Lou Dobbs, Fox News** (1ª persona anglófona) | nov/2018 | 12 | YouTube Fox |
| B2 | **Palestra "um soldado e um cabo"** (vídeo integral) | 2018 | 13 | a localizar íntegra |
| B3 | **PBS NewsHour** (embaixada, contraponto jornalístico) | 2019 | 12 | PBS |
| B4 | **Epoch Times** ("Purging Brazil of Socialism") | 2019 | 12, 14 | Epoch Times |
| B5 | **Leda Nagle** ("novo AI-5", contexto integral) | out/2019 | 13 | YouTube Leda Nagle |
| B6 | **Tucker Carlson** (2 entrevistas) | 2022 e 2024 | 6, 12 | Fox/TCN |
| B7 | **Jordan Peterson** | 2024 | 6 | YouTube JBP |

### Prioridade C — complementos
- OAN/Matt Gaetz (2025) — cap. 10 · CPAC México (nov/2022) — cap. 11 · lives próprias sobre licença (mar/2025) — cap. 9 · Flow Podcast #312 (2021) — perfil · Epoch Times CPAC 2025 · War Room episódios adicionais de 2025 (lista no inventário GPT Onda 1).

### 📝 Fontes ESCRITAS equivalentes (não precisam de vídeo)
- Gazeta do Povo 15/07/2025 ("tarifa Moraes"; "esposa do Moraes") e 03/06/2026 ("pedi pessoalmente a Trump") — caps. 1, 10
- Reuters 14/08, 15/08, 11/09/2025 e 20/07/2026 (green card) — caps. 9, 10
- FT 11/08/2025 (paywall — obter) — cap. 10

---

## Procedimento (já testado)
1. Localizar URL (yt-dlp busca ou link direto).
2. Baixar formato leve → `Kimi K3/transcrições/`.
3. Transcrever com faster-whisper (small, pt/en) → `NOME_DATA_TRANSCRICAO.md` com cabeçalho (fonte, data, duração, método, citações-chave com timestamps).
4. Registrar no MANIFESTO e, se a citação for usada, na ficha do capítulo correspondente.

**Observação:** legendas do YouTube vêm bloqueadas (429) para nós — a transcrição local resolve. Revisão humana recomendada em nomes próprios (whisper erra fonética).
