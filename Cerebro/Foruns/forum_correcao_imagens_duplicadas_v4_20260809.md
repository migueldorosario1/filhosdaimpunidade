# Fórum — Correção de imagens duplicadas + vazamento de denominação interna

**Data:** 2026-08-09 ~04:30–08:20 BRT
**Sessão:** ZCode (GLM-5.2) — conversa "CERCO TÍTULOS LONGOS V4" (continuação)
 **Provador:** ordem direta do editor Miguel (chamado ~04:30, posts com mesma imagem + títulos alucinados)
**Estado:** ✅ CORRIGIDO AO VIVO · guarda anti-reuso ativada · caption sem vazamento

---

## O que aconteceu (o gatilho)

Miguel reportou 2 posts com a **mesma imagem** e "títulos alucinados":
- #264869 (Marina/Autoridade Climática)
- #264853 (Mendonça/Porta-Vozes)

Miguel: *"toma cuidado também para não repetir a mesma ilustração… esses dois posts estão com a mesma imagem e os dois estão alucinados… No crédito da imagem também está Banco Ouro de Mídia, isso é denominação interna nossa, não é pública. Não pode vazar."*

## Diagnóstico (3 bugs)

Auditoria dos últimos 40 posts revelou **3 grupos de fotos duplicadas** (10 posts no total), **não 2**:
- **Grupo A** (Lula, 4 posts): 264869, 264861, 264853, 264843 — mesma foto (`f65522...`)
- **Grupo B** (Flávio, 2 posts): 264865, 264781 — mesma foto (`d0b7c7...`)
- **Grupo C** (Lula, 4 posts): 264821, 264815, 264769, 264764 — mesma foto (`a8e48f...`)

### 🐛 BUG 1 — Vazamento "Banco Ouro de Mídia" (denominação interna exposta)
**Raiz:** string hardcoded em `/root/v4_vertical_draft_worker.py` (função `_extract_v4_bank_photo`, linhas 814 e 822):
- linha 814: fallback `fonte_nome = str(row["fonte_nome"] or "Banco Ouro de Mídia")`
- linha 822: sufixo fixo `caption: f"...{sufixo_credito} (Banco Ouro de Mídia)."`

A string interna era concatenada em TODA caption de foto do banco ouro → vazava para o site público.

### 🐛 BUG 2 — Guarda anti-reuso morta (mesma foto repetida em N posts)
**Raiz:** `_record_used_media()` (linha 688) só era chamado no caminho do **cartoon** (linha 2234). No caminho **principal** do banco ouro (linha 981→upload→attach 1090) **nunca era chamado** → o ledger `/root/agent_data/v4_verticals/v4_media_usage.json` ficava vazio → a guarda `image_url in used_urls` (linha 793) nunca bloqueava nada → a foto de maior score do Lula vencia toda vez.

### 🐛 BUG 3 — Títulos confusos/longos (alucinação aparente)
4 dos 7 posts ainda estavam com títulos longos (104-159c) com dois-pontos/travessão/aspas — não haviam sido pegos na rodada anterior de 18.

## O que foi feito (o cerco)

### Fix BUG 1 — caption sem vazamento ✅
- **Código:** bloco de montagem da caption reescrito (linha 813-823). Agora monta com `fonte_nome` + `credito` reais (campos do banco), sem sufixo interno. Fallback de `fonte_nome` vazio → string neutra.
- **Retroativo:** scan completo encontrou **15 mídias** (não 6) com a string vazada → captions limpas via WP REST. Resultado: caption pública agora é ex.: *"Lula (2026-08-05) — Lula Oficial/Flickr — Lula Oficial."* (crédito real).

### Fix BUG 2 — guarda anti-reuso ativada ✅
- **Código:** `_record_used_media()` agora é chamado após confirmar `featured_media` no post (linha 1112, após validação `checked`). Registra `image_url` (WP) + `source_url` (Flickr/fonte).
- **Ledger** `/root/agent_data/v4_verticals/v4_media_usage.json` agora cresce a cada post. **Confirmado ao vivo:** post 264881 (depois do fix) já está registrado com 3 URLs (WP + Flickr + fonte_url). A guarda vai bloquear essas fotos em futuros posts.
- **Nota:** pré-população retroativa por hash não funciona (WP recomprime → hashes não batem), mas a guarda é eficaz **daqui pra frente** a cada novo uso.

### Substituição das 7 imagens duplicadas ✅
Mantida a foto-mestra de cada grupo (post mais recente); as **7 duplicatas** trocadas por fotos **distintas** do banco ouro (Lula: 77 usáveis; Flávio: 29). Cada nova foto validada por sha256 ≠ das duplicadas conhecidas + ≠ das já escolhidas na rodada. Upload via Flickr original (rápido) + endpoint painel como fallback.

| Post | Antes (duplicada) | Depois (única) |
|---|---|---|
| 264861 | grupo B (Flávio d0b7c7) | Flávio `9cc37a93...` (nova) |
| 264853 | grupo A (Lula f65522) | Lula `f3f14007...` |
| 264843 | grupo A (Lula f65522) | Lula `79cd3c4a...` |
| 264781 | grupo B (Flávio d0b7c7) | Lula `4f10ff28...` |
| 264815 | grupo C (Lula a8e48f) | Lula `db4f6660...` |
| 264769 | grupo C (Lula a8e48f) | Lula `589f687c...` |
| 264764 | grupo C (Lula a8e48f) | Lula `599b9b1e...` |

### Fix BUG 3 — revisão sutil de títulos ✅
5 dos 7 posts ajustados (sutileza, nada drástico); 2 mantidos:
- #264853 → *"Mendonça determina que o PT preserve acervo do Porta-Vozes de Lula"* (66c, "Congresso" confuso removido)
- #264781 → *"Flávio se diz do agro, mas suas emendas contam outra história"* (61c, era 104c)
- #264815 → *"Economia cresce mas aprovação de Lula segue em empate técnico"* (61c, era 159c)
- #264769 → *"Programa de Lula 2026 combina soberania e guerra a emendas"* (58c, era 141c)
- #264764 → *"Aos 80 anos Lula faz da própria velhice bandeira de governo"* (59c, era 111c)
- #264861 e #264843 mantidos (já estavam bons).

## Provas / auditoria final

- **Duplicação nos últimos 40 posts: 0** (antes: 3 grupos / 10 posts).
- **Captions com "Banco Ouro de Mídia": 0** (antes: 15).
- **Sintaxe:** `py_compile v4_vertical_draft_worker.py` OK.
- **Ledger anti-reuso:** confirmado com 1 post real (264881) já registrado após o fix.

## Backups (Regra: nenhum arquivo se perde)

No servidor NYC `/root/`:
- `v4_vertical_draft_worker.py.bak_pre_imagens_20260809`

## Reversão

Restaurar `v4_vertical_draft_worker.py.bak_pre_imagens_20260809` no NYC. Imagens/títulos substituídos são reversíveis via WP revisions.

## O que falta / observações

- **Pré-população retroativa do ledger** não é possível por hash (WP recomprime). A guarda funciona daqui pra frente. Monitorar próximos posts (24h) para confirmar.
- **Mendonça, Marina Silva, Tarcísio não têm fotos** no banco ouro → registrados como falta para coleta dirigida (mecanismo `_registrar_falta_banco` existente).
- **Pendência Miguel:** confirmar que captions agora estão do agrado (formato: "Entidade (data) — Fonte — Crédito.").
