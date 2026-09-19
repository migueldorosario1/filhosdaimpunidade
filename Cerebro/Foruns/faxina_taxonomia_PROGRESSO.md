# 🧹 Faxina de Taxonomia — PROGRESSO (estado vivo da automação)

> **Arquivo lido/escrito pela automação "🧹 Faxina Taxonomia Cafezinho" a cada sprint noturno (2h e 4h BRT).**
> **Plano completo:** `Foruns/forum_grande_limpeza_taxonomia_cafezinho_20260812.md` (leia §10 mecanismo + §12 análise SEO antes de agir).
> **Alvo:** WordPress O Cafezinho canônico (`ocafezinho.com`, SSH `cafezinho-wp`, `/var/www/ocafezinho`, wp-cli `--allow-root` + `WP_CLI_CACHE_DIR=/root/.wp-cli/cache`).

## 🚦 STATUS: PAUSADO

> ✅ **ONDA 1a CONCLUÍDA (14/08/2026 ~08:20 BRT):** ordem Miguel *"já terminei a reforma do menu, agora pode continuar faxina; só não mexe nos itens do menu — mesmo vazios, ficam (regiões, estados)"*. Executada **manualmente assistida** (Miguel online, fora da janela noturna): backup fresco `/root/backup_taxonomia_20260814_0800.sql` → lotes de 50 com re-confirmação count=0 → **969→0 tags órfãs** (968 removidas; total de tags 19.460→18.492). **Zero categorias tocadas; zero itens do menu mexidos** (menu 21062 mapeado e protegido). Site HTTP 200 ✅.
> ⏭️ **PRÓXIMO GATE HUMANO — Onda 1b:** converter 59 tags com `#` (exige redirect 301) + 1c (dedup slugs) + 1d (redundâncias pequenas). **Nada roda sozinho** sem ordem do Miguel.
> 🤖 **Automação cron `automation-a7be3a1e-...`:** sem função até nova onda ser liberada — os disparos noturnos (2h/4h) vão só **skipar** (STATUS: PAUSADO). Para ZERO disparos: `CronDelete` (a gosto do Miguel).
> Histórico: pausas 12/08 ~23:05 (política de categorias) e 13/08 14:10 (reforma do menu; descoberta SEO das páginas 200 `index,follow`) — ver §9 do `forum_politica_categorias_cafezinho_20260812.md`.

> Valores possíveis: `ATIVO` (automação roda) · `PAUSADO` (Miguel pausou — não faz nada, só avisa) · `PAUSADO_ERRO` (kill switch disparou — não roda até humano resetar p/ `ATIVO`).

## ONDA ATUAL: 1 — Higiene segura (autonomia total)

### Sub-fase 1a — excluir tags órfãs (count=0)  ✅ **CONCLUÍDA 14/08/2026 ~08:20 BRT**
- **Total alvo:** 969 tags · **Concluído: 969 (100%)** · **Restante: 0**
- **Como:** execução manual assistida (Miguel online), lotes de 50 com re-confirmação count=0 por lote
- **SEO:** executada com ciência do risco (páginas serviam 200 `index,follow`, mas fora do sitemap — autorização do Miguel 14/08 após apresentação das opções A/B/C)
- **Provas:** count=0 final = **0** · total de tags 19.460→**18.492** · home HTTP 200 · backups: `/root/backup_taxonomia_20260813_1400.sql` + `/root/backup_taxonomia_20260814_0800.sql`

### Sub-fases pendentes da Onda 1 (NÃO rodam sozinhas — gate humano):
- **1b.** Converter 59 tags com `#` → **REQUER redirect 301** (URLs /tag/X/ indexadas) → sessão assistida
- **1c.** Deduplicar tags com slug conflitante (`niteroi`/`niteroi-rio-de-janeiro`, etc.)
- **1d.** Consolidar redundâncias pequenas (Esportes 1426 → Esporte 1271; Eleições 8→1) → mantém ID-alvo

## ONDAS FUTURAS (NÃO iniciar sem gate humano explícito do Miguel)
- **Onda 2 — Mês 2:** Geografia (Regional▸regiões▸estados + DF; cidades→tag com redirect)
- **Onda 3 — Mês 3:** Autores → tag (~45 categorias, ~13.500 posts, lotes ≤500, redirect 1:1)
- **Onda 4 — Mês 4:** Consolidar temas grandes + decisão "Redação" (37.385)
- **Onda 5 — Mês 5+:** Tags singletons (12.845, revisão assistida)

## 🛑 IDs INTOCÁVEIS (automação NUNCA exclui/funde como origem)
Categorias amarradas a agentes/menu/blocos do tema — ao fundir, estas são sempre o **destino**:
`22` (Política) · `15` (Internacional) · `43` (Economia) · `5003` (Geopolítica) · `30` (Tecnologia) · `735` (Ciência) · `79` (Cultura) · `258` (Saúde) · `582` (Meio Ambiente) · `1271` (Esporte) · `28` (Vídeos) · `5087` (Headline) · `2403` (Redação) · `4986` (Regional) · `21062` (menu) · `21068`–`21090` (regiões + estados)

## 🔒 SALVAGUARDAS (obrigatórias a cada sprint)
1. **Backup < 48h** das tabelas `wp_terms`, `wp_term_taxonomy`, `wp_term_relationships` — se não houver, fazer mysqldump ANTES de escrever. Se backup falhar, **PARE**.
2. **Dry-run sempre** — listar term_ids, confirmar count=0, SÓ ENTÃO excluir.
3. **Kill switch** — qualquer erro (403/timeout/MySQL swap alto/term não count=0): setar `STATUS: PAUSADO_ERRO` e avisar Miguel pela Ponte.
4. **Janela noturna** — só corre entre 01h e 05h BRT; fora disso, abortar.
5. **Sempre pt-BR** nos logs e mensagens.

## 📒 LOG DE SPRINTS (automação anexa 1 linha por sprint executado)

| Sprint | Data/hora BRT | Onda.sub | Ação | Qt | Cumulativo | Resultado |
|---|---|---|---|---|---|---|
| 1 | 13/08/2026 02:01 | — | **SKIP** (STATUS: PAUSADO) | 0 | 0/969 | 1º disparo do cron — **OK** (disparou no horário). Janela 01–05h ✅. Nada feito no banco (Miguel pausou 12/08 23:05). **Ponte silenciada** (noturna + pausado = não acordar o Miguel). Próx. disparo: 04h. |
| 2 | 13/08/2026 04:00 | — | **SKIP** (STATUS: PAUSADO) | 0 | 0/969 | 2º disparo do cron — **OK** (04h no horário). Janela ✅. Nada no banco (STATUS segue PAUSADO). Ponte silenciada. Próx. disparo: amanhã 02h. |
| 3–4 | 14/08/2026 02:02–04:00 | — | **SKIP** ×2 (STATUS: PAUSADO) | 0 | 0/969 | Disparos noturnos OK no horário; pausa da reforma do menu. Nada no banco. Ponte silenciada. *(registros individuais perdidos 2× por escrita concorrente — consolidados aqui)* |
| 5 | 14/08/2026 07:58–08:20 | 1a | **EXECUÇÃO MANUAL ASSISTIDA** ✅ | **968** | **969/969 (100%)** | Miguel liberou ("terminou a reforma do menu; não mexer nos itens do menu — regiões/estados ficam mesmo vazios"). Menu 21062 mapeado e protegido. Backup fresco `/root/backup_taxonomia_20260814_0800.sql` → lotes de 50 c/ re-confirmação count=0 → **969→0 órfãs** (total tags 19.460→18.492). Zero categorias/menu tocados. Site HTTP 200. **ONDA 1a CONCLUÍDA** — 1b (tags `#` c/ redirect)/1c (dedup)/1d (redundâncias) aguardam gate humano. |
| 6 | 14/08/2026 08:50–14:05 | 1b | **EXECUÇÃO MANUAL ASSISTIDA** ✅ | **55 tags** | **0 com `#`** | Miguel: "sim" + "vai". 40 renames (zero redirect) + 15 redirects 301 no Nginx ANTES dos merges + 15/15 merges (77 posts) → **China-EUA unificada (302)**. Total tags 18.477. Redirects 301 ✅ · destinos 200 ✅ · cache flush · home 200. **ONDA 1 COMPLETA.** Próx. gates: 1c/1d. *(linha refeita 15/08 02h — original perdida por escrita concorrente)* |
| 7 | 15/08/2026 02:02 | — | **SKIP** (STATUS: PAUSADO) | 0 | — | 5º disparo noturno — OK (02h no horário). PAUSADO (Onda 1 completa; 1c/1d são gates humanos). Nada no banco. Ponte silenciada. |
| 8 | 15/08/2026 04:00 | — | **SKIP** (STATUS: PAUSADO) | 0 | — | 6º disparo noturno — OK (04h). PAUSADO. Nada no banco. Ponte silenciada. Log estável (sprint 6+7 preservados). |
| 9 | 16/08/2026 02:00 | — | **SKIP** (STATUS: PAUSADO) | 0 | — | 7º disparo — OK (02h). PAUSADO (plano SEO aguarda gate Miguel p/ Onda 2). Nada no banco. **Sem Ponte (regra nova 15/08 — só anomalia)**. |
| 10 | 16/08/2026 04:00 | — | **SKIP** (STATUS: PAUSADO) | 0 | — | 8º disparo — OK (04h). PAUSADO. Nada no banco. Sem Ponte (regra 15/08). |
| 11 | 17/08/2026 (noite) | — | **SKIP** ×2 (STATUS: PAUSADO) | 0 | — | Disparos de 17/08 (02h+04h) não deixaram registro no log (escrita concorrente habitual). STATUS permaneceu PAUSADO — nada no banco. *(consolidado em 18/08 02h)* |
| 12 | 18/08/2026 02:00 | — | **SKIP** (STATUS: PAUSADO) | 0 | — | 9º disparo registrado — OK (02h). PAUSADO (aguarda gate Miguel p/ Onda 2 do plano SEO). Nada no banco. Sem Ponte (regra 15/08). |
| 13 | 18/08/2026 04:00 | — | **SKIP** (STATUS: PAUSADO) | 0 | — | 10º disparo registrado — OK (04h). PAUSADO. Nada no banco. Sem Ponte (regra 15/08). |
