# 🗂️ CARTÃO-BOLSO — Política de Categorias do O Cafezinho

> **Referência rápida: ONDE publicar.** Para qualquer agente LLM (Grok/Claude/ChatGPT/Codex/Kimi/Qwen/GLM/Antigravity) ou humano.
> **Canônico desde 12/08/2026** (aprovado pelo Miguel). Detalhes completos: `Cerebro/Foruns/forum_politica_categorias_cafezinho_20260812.md`.
> **Princípio de ouro:** *tudo que não está na whitelist vira TAG — nunca categoria nova.*

---

## ✅ CATEGORIAS OFICIAIS (use SÓ estas)

### 📰 Editoriais (tema) — escolha ≥1 por post
| Categoria | ID | | Categoria | ID |
|---|---|---|---|---|
| Política | 22 | | Saúde | 258 |
| Internacional | 15 | | Meio Ambiente | 582 |
| Economia | 43 | | Energia | 98 |
| Geopolítica | 5003 | | Justiça | 1335 |
| Tecnologia | 30 | | Direitos Humanos | 358 |
| ↳ Ciência (sub) | 735 | | Segurança | 36 |
| ↳ Inteligência Artificial (sub) | 5008 | | Mídia | 23 |
| Cultura | 79 | | Educação | 1479 |
| Esporte | 1271 | | | |

### 🌎 Geografia (opcional — só se o post tem ângulo regional forte)
`Regional (4986)` ▸ **Sudeste / Sul / Nordeste / Norte / Centro-Oeste** ▸ **estado / DF**
- **27 unidades federativas:** 26 estados + **Distrito Federal** (DF é **Centro-Oeste**; cat **DF = 21139**, slug `distrito-federal`, criada 12/08).
- **CIDADE = TAG** (Brasília, Rio de Janeiro, São Paulo, Niterói, BH...) — **nunca** categoria. *A categoria "Brasília" (5710) já existente = arquivo morto (não recebe posts novos).*

### 🔧 Transversais (operacionais)
| Categoria | ID | Uso |
|---|---|---|
| Redação (Geral) | 2403 | safety-net — use se nenhum editorial encaixar |
| Vídeos | 28 | formato (posts com embed de vídeo) |
| Headline / Manchete | 5087 | operacional do agente manchete |

---

## 🚫 NUNCA criar categoria para (use TAG)
- **Pessoa / autor / colunista / político** (Lula, Bolsonaro, Trump, Rhyan de Meira...)
- **Cidade / país / região estrangeira** (Paris, China, EUA, Oriente Médio...)
- **Evento / eleição / escândalo / série** (Eleições 2026, Copa, Lava-Jato...)
- **Qualquer coisa fora da whitelist** → vira **TAG**

> As categorias antigas desses tipos (já existem no site) são **arquivo morto**: posts antigos continuam acessíveis, mas **publicação nova não vai nelas** — vai na editorial da whitelist + tag.

---

## 📝 REGRA DE PUBLICAÇÃO (passo a passo)
1. **≥1 editorial** da whitelist em todo post novo (obrigatório).
2. Se ângulo regional forte → adicionar **Regional ▸ região ▸ estado** (opcional).
3. **Pessoa / lugar / evento** → **TAG** (nunca categoria).
4. Em dúvida → **Redação/Geral (2403)** + tag específica.
5. **Tags sem `#`, sem duplicar slug, sem palavra-de-título.**

---

## 🤖 Para agentes (resumo de 1 linha)
> Publicar em **1 editorial da whitelist** (+ Regional▸estado se aplicar); **pessoa/lugar/evento = tag**; em dúvida, **Redação (2403) + tag**. Tudo fora da whitelist é **tag**, nunca categoria nova.

---

## 📊 Aplicação (em andamento)
- **mu-plugin** `cafezinho-politica-categorias.php` — Fase 1 LOG (observar violações) → WARN → ENFORCE. *(a implementar)*
- **Config agentes:** `CAT_*_ID` já batem com a whitelist (V4: 22/15/43/5003/30/735/79/258/582/1271; youtube→28; manchete→2403+5087).
- **Relatório semanal** de posts fora da whitelist. *(a implementar)*
