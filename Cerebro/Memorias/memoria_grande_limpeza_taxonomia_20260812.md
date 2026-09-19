# 🧹 Memória técnica — Grande Limpeza de Taxonomia O Cafezinho (execuções)

> Log auditável das execuções da faxina. Plano: `Foruns/forum_grande_limpeza_taxonomia_cafezinho_20260812.md` · Política: `Foruns/forum_politica_categorias_cafezinho_20260812.md` · Progresso vivo: `Foruns/faxina_taxonomia_PROGRESSO.md`.

## 14/08/2026 07:58–08:20 BRT — Onda 1a/T1: tags órfãs count=0 — ✅ CONCLUÍDA

- **Autorização:** Miguel — *"já terminei reforma do menu. agora pode continuar faxina. só não mexe nos itens que estão no menu. mesmo que vazios, eles ficam. regiões do país, estados, veja lá."*
- **Proteção aplicada (menu 21062 mapeado, 43 itens — NENHUM tocado):** Regional (4986) + 5 regiões (Norte 21068, Nordeste 4984, Centro-Oeste 21069, Sudeste 21070, Sul 21071) + 27 unidades federativas (26 estados + **DF 21139**) + editoriais do menu: Nacional/Política 22 · Economia 43 · Geopolítica 5003 · Tecnologia 30 · Cultura 79 · Meio Ambiente 582 · Esporte 1271 · Saúde 258 · Vídeos 28 · Eleições 47 ▸ Eleições 2026 5088 (+ página "Quem somos" e âncora "Editorias").
- **Execução (SSH `cafezinho-wp`, `/var/www/ocafezinho`, wp-cli `--allow-root`):**
  1. Backup fresco: `wp db export /root/backup_taxonomia_20260814_0800.sql --tables=wp_terms,wp_term_taxonomy,wp_term_relationships,wp_termmeta` (~5 MB, CREATE TABLE confirmado).
  2. Loop em lotes de 50: listar `post_tag` com count=0 (`grep -E '^[0-9]+,0$'` sobre CSV term_id,count) → `wp term delete post_tag <ids> --allow-root` → re-confirmação count=0 a cada lote (re-lista) → sleep 1 entre lotes.
  3. Duração ~22 min (cada wp-cli carrega o WP com eco PHP do tema — lento mas seguro).
- **Resultado:** **tags count=0: 969 → 0** (968 excluídas + 1 flutuação de contagem); total de tags **19.460 → 18.492**; home **HTTP 200** ✅.
- **Contexto SEO:** execução autorizada com ciência de que essas páginas serviam **200 `index,follow`** mas **fora do sitemap** (risco baixo aceito pelo Miguel após apresentação das opções A/B/C em 13/08 — ver §9.3 do fórum da política).
- **NÃO tocado:** nenhuma `category`, nenhum item de menu, nenhum post, nenhum ID intocável.
- **Rollback se algum dia precisar:** restaurar as 4 tabelas de termos de `/root/backup_taxonomia_20260813_1400.sql` ou `/root/backup_taxonomia_20260814_0800.sql`.
- **Próximos passos (GATE HUMANO — não rodam sozinhos):** Onda 1b (59 tags `#` → tag sem `#` c/ redirect 301) · 1c (dedup slugs conflitantes) · 1d (redundâncias pequenas mantendo ID-alvo).

## Histórico de skips (automação 2h/4h — sem escrita no banco)
- 13/08 02:01 · 13/08 04:00 · 14/08 02:02 · 14/08 04:00 — 4 disparos noturnos, todos **SKIP** (STATUS: PAUSADO), Ponte silenciada, janela 01h–05h respeitada.
- Tentativa manual 13/08 ~14:00: **ABORTADA pela validação de segurança** (tags count=0 serviam 200 `index,follow` — premissa de SEO-neutro era falsa; 0 tags apagadas naquele dia). O kill switch funcionou como projetado.
