# ESPELHO-SYNC — Sync canônico→espelho NÃO propaga lixeira/rascunho (posts órfãos publicados)

**Tag:** ESPELHO-SYNC (sentinel do Claude: `sync_from_cafezinho.sh`)
**Achado por:** ZCode (DeepSeek via failover) — aviso Miguel 17/08 02:5x ("post em inglês no espelho")
**Status:** 🟡 CONTIDO (17 órfãos removidos do espelho com backup) — patch de reconciliação pendente no script do sync

## Sintoma

Post **265600** ("Tidebound Grotto on Mythic..." — guia de WoW em inglês, lixo de SEO de 13/08)
continuava **PUBLICADO no espelho** cafezinho.news depois de ir para a **lixeira no canônico**
(14/08 20:14). Miguel: "ta aqui no espelho. não está no canonico. menos mal. mas porque isso?"

## Causa

`sync_from_cafezinho.sh` (espelho, cron horário :17, autor Claude 03/07) sincroniza só
**NOVOS + EDITADOS** com `post_status IN ('publish','inherit')`. Mudança de status para
trash/draft/pending **nunca sai no delta** → o espelho mantém a cópia publicada para sempre.
Diff completo espelho×canônico (IDs publicados) achou **17 órfãos**: 4 recentes
(264355 draft, 264869/265816/265920 trash), 13 antigos (jul/ago; 4 trash, 6 pending, 3 draft
— inclui "TESTE WP-CLI PUBLISH — remover" 261951).

## O que JÁ foi feito (ZCode, 17/08 ~03:20)

Todos os 17 movidos para a lixeira do espelho, cada um com backup JSON em
`ZCodeProject/handoff_gsn/limpeza_espelho_20260817/` (também ficam na lixeira do próprio espelho).
O post cassino (265611, lixo da MESMA leva de 13/08) está **publicado no canônico com proteção
editorial** (`post_publicado_por_humano`, autor 5780 não-automático) — NÃO mexi no canônico;
no espelho ficou `pending` (gate de imagem reverteu o restore) = invisível. **Aguardando decisão
do Miguel** (se não for intencional, ele libera e eu jogo fora).

## Pendente (Claude — dono do sentinel)

1. **Reconciliação no sync:** passo diário (ou por execução) que compara IDs publicados
   espelho×canônico e joga na lixeira do espelho os que deixaram de ser publish no canônico.
   Sugestão barata: no fim do sync, `SELECT ID FROM wp_posts WHERE post_type='post' AND
   post_status='publish'` dos 2 lados (mysql direto, como o script já faz), diff via arquivos,
   `wp post delete` local para cada órfão. Custo: ~2 queries simples.
2. Ou (alternativa) incluir status mudados no delta: adicionar `post_status IN ('draft','pending','trash')`
   ao where do dump de wp_posts quando `post_modified > cutoff` — o REPLACE INTO então rebaixa a
   cópia do espelho naturalmente. (Cuidado: passaria a sincronizar rascunhos, o que muda a
   semântica do espelho — a opção 1 é mais segura.)
3. Os 400077/400079 (publicados direto no espelho pelo V4 TENDÊNCIAS) são esperados — NÃO são
   órfãos; a reconciliação precisa ignorar o range 400000+ (conteúdo nativo do espelho).

## Lição

Espelho = cópia de segurança pública: manter lá publicado o que o canônico despublicou é pior
que não ter espelho (conteúdo rejeitado segue no ar sob a marca). Sync unidirecional precisa de
reconciliação de status, não só de conteúdo.
