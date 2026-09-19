# Fórum — Mapa de autoria dos posts do Cafezinho: V4 × V5 × Miguel × Gabriel (21/08/2026)

**Data:** 2026-08-21 ~23:40 BRT · **Executante:** ZCode (GLM-5.3), chat direto · **Ordem:** Miguel ("pode identificar quais posts são do v4, quais são do v5, quais são meus, quais são do Gabriel Barbosa?")

**Resposta curta: SIM, dá para identificar** — auditado direto no banco do canônico (`ssh cafezinho-wp` → `wp db query`). Chave = **author_id + metas de proveniência**.

## 🗺️ Mapa de identificação (canônico www.ocafezinho.com)

| Fluxo | Como identificar no banco | author_id (login) | Publish 15/08→21/08 |
|---|---|---|---|
| **V4 (agentes temáticos)** | meta `zizi_job_id = v4d_<vertical>_<hash>` | **5786** Redacao nova (cafezinhov4@gmail.com) | **299** |
| **V5 (Motor V5 / LAURA-AGY)** | autor 5786 **sem** `zizi_job_id` **e sem** `nomes_check` a partir de 20/08; pool de contas 5786/5742/5785/5470 publicadas em slots de 30 min | 5786, 5742, 5785, 5470 | **10** |
| **Agente YouTube** | meta `cafezinho_nomes_check` (JSON com `video_id`) | 5786 | **6** |
| **Repetidor estatal** | autor 5470 fora dos publicados pelo V5 | **5470** Redator (editordocafezinho@gmail.com, conta de 2018) | **21** |
| **Gabriel Barbosa** | contas próprias | **5780** redator2 (migueldorosario5@gmail.com — confirmado nos fóruns de curadoria de 12/08: "Gabriel=5780 ✅") + **5735** gabrielbarbosa9001 (+5774/5784 ociosas) | **28** (25 + 3) |
| **Miguel (humano)** | conta principal | **2018** James2017 (migueldorosario@gmail.com, 10.359 posts no histórico) | **3** |

## 📌 Posts V5 identificados (20–21/08, todos confirmados no ledger `agy_laura.md`)

266751 (Pacto de Defesa de Meca) · 266791 (Ormuz 92 dólares) · 266806 (Doze dias de juros) · 266824 (Ciro chama Elmano de "anta") · 266826 (Elmano segurança CE) · 266827 (Elmano critica Ciro) · 266828 (Ciro "pacto diabólico") · 266839 (Lula 65% CE Real Time) · 266913 (Margem Equatorial — "Artigo 1 do Motor V5", AL-20260821-024) · 266991 (Datafolha vitória de Lula — AL: "AGY-LAURA pegou o mesmo material 5min depois do draft"; o draft V4 gêmeo 266987 virou canibal CM-057).

## 📌 Posts do Miguel (desde 15/08, autor 2018)

266483 (Ciro defende Mossad p/ Ceará) · 266817 (mitos bolsonaristas/ciristas sobre o Ceará) · 266858 (Liderança espontânea e 57% Elmano).

## 📌 Posts do Gabriel (desde 15/08)

Pela 5780 (25): inclui 266521 (Lula×Putin — a manchete humana de 19/08), séries analíticas Datafolha/Real Time/Ceará. Pela 5735 (3): 266955 (Tarcísio folga 18 pts), 266618 (Unitree 460%), 266607 (FAB plano golpista).

## ⚠️ Nuances importantes

1. **V5 NÃO grava meta própria** no postmeta — a identificação depende de autor+período+ledger. **Recomendação:** o publicador da esteira gravar meta própria (ex. `motor = v5`) nos posts novos.
2. **Híbridos:** a esteira V5 agenda e publica TAMBÉM drafts humanos — 266817 (texto do Miguel) estava no bolo agendado pelo motor (AL-20260821-013). Autoria do TEXTO = conta WP; autoria da PUBLICAÇÃO = motor (ledger).
3. O Motor V5 publica com **pool de contas** (5786/5742/5785/5470) — multiautoria técnica; não confundir contas 5742 ("migueldorosario")/5785 ("miguelpublicador") com o Miguel humano (2018).
4. Não classificado: 266274 (17/08 "Pesquisa Nexus", 5786 sem zizi sem nomes_check, sem embed — anterior ao V5, provável publicação manual do Loop).
5. O fórum de limpeza de taxonomia de 12/08 citava "Gabriel Barbosa (4942)" — 4942 é na verdade `ydb9111999` (login/display sem relação); as contas do Gabriel são 5735/5774/5784 + 5780.

## Queries para reproduzir

```sql
-- classificação por autor + presença de meta V4
SELECT p.post_author, u.user_login, u.display_name,
       SUM(CASE WHEN z.meta_value LIKE 'v4d%' THEN 1 ELSE 0 END) AS v4,
       SUM(CASE WHEN z.meta_value IS NULL THEN 1 ELSE 0 END) AS sem_meta,
       COUNT(*) AS total
FROM wp_posts p JOIN wp_users u ON u.ID=p.post_author
LEFT JOIN (SELECT post_id, meta_value FROM wp_postmeta WHERE meta_key='zizi_job_id') z ON z.post_id=p.ID
WHERE p.post_type='post' AND p.post_status='publish' AND p.post_date>='2026-08-15'
GROUP BY p.post_author ORDER BY total DESC;

-- lista de posts 5786 sem zizi (candidatos V5/YouTube; YouTube = tem nomes_check)
SELECT p.ID, DATE(p.post_date), LEFT(p.post_title,70)
FROM wp_posts p WHERE p.post_type='post' AND p.post_status='publish'
AND p.post_date>='2026-08-15' AND p.post_author=5786
AND NOT EXISTS (SELECT 1 FROM wp_postmeta m WHERE m.post_id=p.ID AND m.meta_key='zizi_job_id')
ORDER BY p.post_date DESC;
```

## O que aconteceu / o que falta / o que preciso de você (Miguel)

- **ACONTECEU:** mapa completo de autoria auditado no banco do canônico; contagens desde 15/08; IDs V5/humanos listados.
- **FALTA:** nada para esta análise. Melhoria sugerida: meta própria `v5` no publicador da esteira.
- **PRECISO DE VOCÊ:** só se quiser adotar a recomendação da meta `v5` (1 linha no publicador).

**Catalogação:** este fórum trata de curadoria/autoria — ligado aos fóruns de manchete/curadoria de 12/08 e à transição V5 de 20/08. Registrado em CEREBRO_NODE_ATUALIZACOES.md (21/08).
