---
name: reference-doc-claudia-beatriz-monitoramento
description: "Cláudia Beatriz mantém Google Docs com revisão editorial diária do Cafezinho — bugs por tipo, posts afetados, links pra edição. Top erro = Hiperlink (32%). Fórum dedicado pra cruzamento estrutural."
metadata: 
  node_type: memory
  type: reference
  originSessionId: ad62e53a-7337-4799-84ba-ed7ccefc1122
---

📋 **Cláudia Beatriz (autor WP #5728) mantém um Google Docs vivo com revisão editorial diária do Cafezinho.**

**Link do doc:** https://docs.google.com/document/d/1yZe_bG8hl1_sqxMfuXAiNrMvFczpQu59HrVjK7tI4EY/edit
**File ID (pra leitura via mcp__claude_ai_Google_Drive__read_file_content):** `1yZe_bG8hl1_sqxMfuXAiNrMvFczpQu59HrVjK7tI4EY`

**Conteúdo:** itens numerados por dia (formato `**01- Tipo de erro**` + título do post + descrição + link pro editor WP). Datas começam em 14/05/2026 (15 dias monitorados, ~225 itens registrados).

**Top 7 tipos de erro:**
| Erro | Ocorrências |
|---|---|
| Hiperlink (fonte ausente/quebrada) | 72 (32%) |
| Título IA (clichê LLM) | 50 |
| Imagem Destacada | 24 |
| Título (genérico) | 12 |
| Hiperlink + Imagem destacada | 7 |
| Formatação texto | 6 |
| Subtítulo (Título 2 vs 3) | 2 |

**Comportamento dela (Miguel explicou):** anota E corrige o que dá (manualmente via WP admin). Em geral resolve bugs visuais imediatos (ex: "target=" sangrando como texto). Mas problemas estruturais (hiperlink ausente em escala, Título IA) ficam.

**Meu papel no monitoramento:**
1. Ler doc dela periodicamente (toda rodada de tick ou quando Miguel pedir)
2. Conferir via WP API se ela corrigiu mesmo
3. Registrar status no fórum dedicado: `Foruns/forum_monitoramento_claudia_beatriz_20260607.md`
4. Propor correções estruturais (utils + auditor periódico + snippet PHP)

**Achado da 1ª rodada (07/06 05:25 BRT):** dos 18 itens "Hiperlink" do 06/06, ela corrigiu o "target=" visível em 7 casos mas o hiperlink em si segue ausente em 18/18. Bug é estrutural — não dá pra resolver post-a-post. Proposta `util_hiperlink_fonte.py` no fórum dedicado.

Relacionado: [[project_no_home_opcao_d_descentralizada]] (filosofia utils+auditor que se estende pra hiperlink+título), §93, §94, §86.
