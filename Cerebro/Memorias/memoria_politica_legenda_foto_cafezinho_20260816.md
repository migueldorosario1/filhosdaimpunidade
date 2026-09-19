# Memória — Política de legenda de foto Cafezinho: log técnico (16/08/2026)

Fórum correspondente: `Foruns/forum_politica_legenda_foto_cafezinho_20260816.md`. Executor: ZCode/Kimi K3.

## Incidente detonador

- Post **265953** (`video-de-mal-estar-de-flavio-bolsonaro-em-debate-volta-a-circular`, publish 16/08 03:00) com figcaption quebrada: `O senador Fl\u00e1vio Bolsonaro \u2014 Cr\u00e9dito: Ag\u00eancia Senado \u2014 Licen\u00e7a: CC BY 2.0` (escapes unicode LITERAIS no banco).
- Causa: a rodada da **Caçadora ZCode de 15/08 14:38** (livro de reservas: `| 265953 | ZCODE | 2026-08-15 14:38 BRT | APLICADO |`, media 265955/265956) escreveu o `--caption` com escapes JSON não-decodificados. O prompt antigo da automação pedia `--caption="<legenda factual> — Crédito: <autor> — Licença: <licença>"` (crédito visível — política revogada hoje pelo Miguel).
- O ícone 📷 era do tema (span `manchete-caption-icon`), não do banco.

## Correções executadas (ordem cronológica)

1. **Anexo 265955** (thumbnail do 265953): backup `/root/backup_legenda_265955_pre_fix_20260816.json` → `wp post update 265955 --post_excerpt="O senador Flávio Bolsonaro (Republicanos-RJ)" --post_content="Crédito: Agência Senado — Licença: CC BY 2.0 — Fonte: Wikimedia Commons"` + `wp post meta update 265955 _wp_attachment_image_alt "O senador Flávio Bolsonaro (Republicanos-RJ)"`. (Imagem = Commons "Entrevistas - Senador Flávio Bolsonaro (Republicanos-RJ) e advogado Frederick Wassef".)
2. **Redis:** `wp cache flush` falhava (wp-cli sem conexão Redis — web ok). Solução: `redis-cli DEL wp:posts:265955 wp:post_meta:265955` (chaves com prefixo `wp:`, DB 0, ~9,6k chaves só de object cache).
3. **Tema V2.9:** bloco `manchete-caption` (front-page.php linhas 35-43, `wp_get_attachment_caption` + figcaption + span 📷) substituído por comentário de rollback. Fluxo: scp p/ local → Edit → scp `/tmp/front-page.php.new` → `php -l` verde → cp. Backup `/root/backup_legenda_home_20260816/front-page.php`. Single (`single.php:37-38`, `get_post(thumbnail)->post_excerpt`) intacto.
4. **Prompt da Caçadora** (`automation-e1b2d648-1ae6-4109-bb4c-177cd3d18729`): CronUpdate ~17:53 — PASSO 4 reescrito (4a import com legenda SÓ factual; 4b crédito/licença/fonte na descrição do anexo + ALT) + REGRAS com anti-escape `\uXXXX`.
5. **Diretriz aos loops:** `Projeto Cafezinho Agentes/Foruns/canal_trindade.md` (tag `[ZCODE-KIMIK3-DIRETRIZ-LEGENDA-FOTO-NOVA-POLITICA]`) + `Cerebro/Foruns/inbox_trindade/claude.md` + `grok.md`.
6. **Passivo (116 anexos):** varredura `post_type=attachment AND post_excerpt LIKE '%Crédito:%' AND post_date > 2026-08-01` → 114; +2 encontrados depois (265633 só com "Licença:"; 266127 reescrito por rodada em curso às 17:49). Backup TSV `/root/backup_legendas_passivo_20260816.tsv`. Script `/tmp/fix_legendas.php` (eval-file, 1 boot WP, regex 3 variantes de split em "Crédito:", `wp_update_post`): dry-run 113 ok/0 vazios/1 sem-regra → apply → 113 migrados. Manuais: **265105** (caption era só "Crédito: @rafael.fonteles" → "Rafael Fonteles (PT), governador do Piauí"; post-pai 265063 publish), **265633**, **266127** (Lula Vila Euclides — Crédito Ricardo Stuckert/Lula Oficial CC BY-SA 4.0).
7. **Caches finais:** `redis-cli DEL` das chaves `wp:posts:*`/`wp:post_meta:*` dos 115 anexos c/ descrição "Crédito:%"; `rm -rf` do cache Rocket das 71 URLs publish afetadas (`/var/www/ocafezinho/wp-content/cache/wp-rocket/www.ocafezinho.com/AAAA/MM/DD/slug[-amp]`).

## Provas ao vivo (18:20-18:25)

- 265953: `<figcaption>O senador Flávio Bolsonaro (Republicanos-RJ)</figcaption>` ✅
- 265959 (Ceará×Cuiabá, thumb 265962): `<figcaption>O Estádio Presidente Vargas, em Fortaleza, casa do Ceará</figcaption>` ✅
- Home `ocafezinho.com`: `grep -c figcaption` = **0** ✅
- Banco: 0 anexos pós-01/08 com Crédito/Licença em post_excerpt ✅

## Gotchas desta sprint

- `wp post list`/`wp cache flush` via CLI quebram quando o Redis soluça (RedisException); `wp db query` NÃO carrega WP (só-leitura ok) e o `redis-cli` direto resolve cache stale (chaves `wp:posts:<id>`).
- Página "ainda velha" pós-fix = object cache Redis (não só Rocket): DEL da chave do anexo resolve; arquivo Rocket de URL específica some com `rm -rf` direto (nunca `find` na árvore de cache — timeout).
- Migração em lote de anexos: eval-file com `wp_update_post` em 1 boot (rápido); mas rodada da Caçadora EM CURSO pode reescrever caption no formato velho (caso 266127) — re-checar o count DEPOIS do apply.
- Janela de corrida no monitor: Edit falhou 1× (outra sessão escreveu junto); reler+reaplicar.
- Outra sessão ativa no mesmo horário (V4 agendamento, NYC+WP) — sem colisão de arquivos (ela em worker/agendamento; eu em tema+anexos).

## Em aberto

- ACK Claude/Grok da diretriz (canal Trindade).
- Espelho: captions novas chegam via sync de posts; bloco manchete-caption do tema do espelho ainda existe (replicar se o Miguel pedir).

---

## Atualização 17/08 ~08:25 BRT (ordem Miguel)

Legenda visível (`post_excerpt`) = texto jornalístico até o crédito do fotógrafo (`— Crédito: X`), **sem licença**. Licença → `_wp_attachment_image_alt` e descrição do anexo. Bug associado: legends com escapes `\u00XX` crus (JSON) exibidos com caracteres estourados — corrigidos em massa (49 anexos, backup `legendas_reparadas_20260817_backup.json` no canônico), mu-plugin `cafezinho-legenda-limpa.php` (unescape + strip no save/render) e worker V4 corrigido (alt_text leva licença).
