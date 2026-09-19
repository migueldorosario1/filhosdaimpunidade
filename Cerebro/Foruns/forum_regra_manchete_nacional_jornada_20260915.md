# FÓRUM — Regra permanente: manchete SÓ Nacional/Política/Eleições 2026 das 08h às 22h — 15/09/2026

**Data:** 2026-09-15 ~14:3x→15:0x BRT
**Autor:** ZCode/GLM-5.3 (ZM)
**Status:** ✅ IMPLANTADO E COMPROVADO EM PRODUÇÃO (gate da home v1.1.0)
**Memória-irmã (Tema Duplo):** `Memorias/memoria_regra_manchete_nacional_jornada_20260915.md`
**Relacionados:** `forum_manchete_comentario_soh_nacional_ate_2turno_20260812.md` (tese 12/08 — o filtro no agente seguia pendente; agora virou LEI DE RENDER no gate) · adendos 201b/201c do `forum_ronda_zm_vigia_1h_20260903.md` (sticky e gate da manchete) · `CEREBRO_NODE_MANCHETE.md`

---

## 1. Ordem do Miguel (15/09 ~14:3x, quase literal)

> "Eu quero mudar a regra da manchete. A manchete só pode ser nacional, pelo menos de dia. Até às 10 horas da noite. De 8 da manhã às 10 da noite, a manchete só pode ser nacional. Nacional, política e eleições 2026. Tem que ter alguma dessas tags. Tá? A manchete. Pode mudar a manchete lá agora e bota isso como regra."

**Regra viva nova:** das **08h00 às 22h00** (horário de Brasília), a manchete da home só pode ser post com **Nacional OU Política OU Eleições 2026** (tag OU categoria). Fora da janela (22h–08h) vale a regra anterior (qualquer tema, capa verificada).

## 2. Implementação (mu-plugin `cafezinho-real-image-gate.php` v1.0.0→v1.1.0)

Três funções novas + mudança em `cafezinho_get_real_highlight()`:

| Função | Papel |
|---|---|
| `cafezinho_manchete_janela_nacional_ativa()` | `(int) current_time('H')` em `[8, 22)` — WP timezone = America/Sao_Paulo (conferido) |
| `cafezinho_post_is_nacional_politica_eleicoes($id)` | post tem termo com slug da regra em `category` OU `post_tag` |
| `cafezinho_manchete_nacional_tax_query()` | `(category slugs OR post_tag slugs) AND (category NOT IN 20699 No Home)` |

- **Slugs aceitos** (nas duas taxonomias): `nacional`, `politica`, `politica-2`, `eleicoes-2026`, `eleicoes2026`, `eleicoes`. Termos reais do site: cat 22 «Política» (politica-2, 13.290 posts), cat 21141 «Nacional» (55), cat 5088 «Eleições 2026» (1.178), tag 16 «política» (226), tag 5602 «Eleições 2026» (498). NÃO existe tag «nacional» — nacional é categoria.
- **Manual:** na janela, a escolha manual só vale se ALSO passar na regra (senão é rejeitada em silêncio e cai no fallback — igual ao caso capa sem selo). À noite o manual volta a valer sozinho.
- **Fallback na janela:** 60 recentes + tax_query da regra + capa → filtro verified-real → 1º. **Degrau de segurança:** se NENHUM elegível tiver capa verificada, aceita o mais recente do tema com capa qualquer (regra editorial > selo de capa); se nem isso existir, cai no fluxo antigo para a manchete nunca sumir.
- **Fora da janela:** código idêntico ao anterior (tax_query nem entra).

### 🔴 Bug de core caçado no caminho (registrou-se aqui para nunca mais cair)

**`tax_query` + `category__not_in` juntos = furão.** O core mescla o `category__not_in` como mais uma **cláusula OR** dentro da tax_query — com relation OR no topo, `ID NOT IN (20699)` aprova praticamente TODO post e o filtro de temas vira inócuo (provado: post de IA 271117 eleito às 14:31). **Cura:** exclusão da 20699 DENTRO da tax_query com `relation => 'AND'` no topo e `unset($args['category__not_in'])` na janela. Prova pós-fix: post IA ausente da query bruta (60/60 nacionais).

## 3. Provas (15/09 14:5x–15:0x BRT)

- **Antes:** manchete renderizada = 270489 «Irã e Omã acertam rota de Ormuz fora do comando dos EUA» (geopolítica, manual do agente, sem nenhuma tag da regra) — violava a ordem.
- **Depois (gate):** `cafezinho_get_real_highlight('Manchete')` → **271129 «Ciro Gomes volta a chamar PT de "organização criminosa" e poupa Flávio Bolsonaro»** — cat Política, capa verificada, publicado hoje.
- **Depois (público):** `curl www.ocafezinho.com` → `<h1 class="manchete-titulo">` = Ciro Gomes + link do post (200; CF DYNAMIC p/ HTML + `rocket_clean_home()`).
- Manual 270489 (Irã) rejeitado na janela: `cafezinho_post_is_nacional_politica_eleicoes(270489) === false` ✓.

## 4. Interação com o resto da casa (IMPORTANTE p/ CL/CM/agentes)

1. **`wp_highlights` (manual) NÃO é apagado** — o gate só ignora a escolha de dia. Quem setar manchete manual fora da régua durante 08–22h verá o nacional mais recente no ar; às 22h a escolha manual volta a valer.
2. **Agente_manchete (NYC, score GA4)** segue podendo eleger qualquer tema — o gate protege a renderização sozinho. O patch antigo "só cat 22" do fórum 12/08 segue pendente/opcional (o gate é a lei).
3. **Manchete-humana (trava 2–24h)** também passa pelo mesmo gate: trava de post não-nacional fica invisível de dia.
4. **Espelho cafezinho.news:** mesmo mecanismo, mas site fechado por ordem Miguel/SEO — aplicar quando reabrir.

## 5. Rollback

`cp /var/www/ocafezinho/wp-content/mu-plugins-baks/cafezinho-real-image-gate.php.bak_pre_regra_manchete_nacional_20260915 /var/www/ocafezinho/wp-content/mu-plugins/cafezinho-real-image-gate.php && wp --path=/var/www/ocafezinho --allow-root eval 'rocket_clean_home();'` (v1.0.0 de 12/08, pré-regra). Desligar a regra sem voltar atrás: editar `cafezinho_manchete_janela_nacional_ativa()` para `return false;`.

## 6. Estado / o que falta

- ✅ Regra implantada, manchete trocada na hora (ordem cumprida).
- ✅ Tema Duplo gravado; nodos MANCHETE + ATUALIZACOES + monitor + ponte avisada.
- 🟡 O que precisa do Miguel: nada — se quiser estender a janela (ex.: até 23h) ou adicionar tema à lista de slugs, é 1 linha no mu-plugin.

— **ZCode/GLM-5.3**, 15/09/2026
