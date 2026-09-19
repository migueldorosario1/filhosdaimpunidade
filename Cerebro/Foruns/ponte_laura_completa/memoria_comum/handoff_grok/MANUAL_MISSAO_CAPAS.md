# Manual — missão de capas V4 (o que eu fazia; agora é seu)

## Escopo autorizado (não alargue)

- **Só** posts `author=5786` (worker V4)
- **Só** `pending` ou `draft` com `_thumbnail_id` 0 / inexistente
- **Não** cria `future` (isso é publicação)
- **Não** muda `post_status`
- **Não** publica, não lixeira, não deleta
- **Não** aplica em outro autor (5470 repetidor, humanos, YouTube)
- Fontes: **Wikimedia Commons** CC BY / BY-SA / CC0 / PD / PD-old **ou** Flickr CC/PD
- Proibido: NC, ND, agência paga, hotlink, IA como foto real
- Flux Pro: só Tec/Geo, ilustração declarada, **nunca Nacional** — e **você não gera Flux**. Se o worker colar Flux como foto real ou em Nacional, **troca**. Em Tec/Geo sem ticket, não pise.
- ≥ **1200 px** no original
- Máx **3** capas por rodada
- Mídia **nova** por post (anti-reuso: grep no log antes)

## Ritual (obrigatório, nesta ordem)

1. Ler `ponte_imagens_RESERVA.md`. Reservado por outro <2h = **pule**.
2. Reservar: `| post_id | LAURA-GROK | ts BRT | RESERVADO |`
3. Banco depurado é **candidato**, não passe livre. Banco original = **congelado**. Prefira pesquisa fresca (3 variantes).
4. Conferir licença **na página** do Commons/Flickr (não só no search).
5. Ver a foto com os próprios olhos nos **5 eixos:** pessoa, lugar, evento, época, assunto. Nome de arquivo mente.
6. Importar pelo WP-CLI como `www-data` (não SQL).
7. `set_post_thumbnail` se o import não colou.
8. Legenda visível = **só fato**. Crédito + licença + URL na **descrição** do anexo (`post_content` da mídia).
9. Log em `ponte_imagens_v4_LOG.md`: ts | post | resultado | crédito | licença | px | media_id | **URL exata** | assinatura `laura-grok`
10. Atualizar reserva para `APLICADO <media_id>`
11. Ping Claude: recibo `_cafezinho_img_check` com `ok:true` — **você não escreve o recibo**
12. Se der problema visual: `_thumbnail_id=0` e loga o motivo

## Como falar com o WordPress

No Dell o alias é `ssh cafezinho-wp` e o path `/var/www/ocafezinho`.  
Na Laura use a identidade do pacote `credenciais_laura/` (PD-1: escrita **whitelist**). Só o necessário: `wp media import`, `wp post update` do anexo, `set_post_thumbnail` / `wp eval` de leitura. Recusa: publish, delete, mudar status.

Stderr do tema com `PHP Notice: HTTP_HOST` é ruído. Ignore.

Pesquise Commons **a partir do servidor** se o DNS da máquina falhar.

```bash
# leitura: fila fm=0
wp eval '... WP_Query author 5786 pending/draft/future + _thumbnail_id 0 ...'

# import (exemplo)
wp media import "$URL" --post_id=$POST --title="..." --caption="fato" --alt="..." --porcelain
```

## Observador (os dois Groks)

Ping na `fila_para_claude.md` só se for **crítico** e o Claude vai colocar no ar:

- `sem_featured_media` em **future**
- metalinguagem de IA no texto público
- título >80c que passou
- `<!-- CONTENT END` residual
- HTML escapado
- dedup lead óbvio
- fato errado gritante (nome/cargo/data)

Não pingue gosto, título com “e”, nem post velho do repetidor.

Título **não se reescreve** daqui. Auditor de Títulos entrega ~10:05 na inbox do Claude. Já vimos sugestões que **pioram** a regra 2 (trocam “para” por “e”).

## Anti-atrito

- Reserva de imagem: `ponte_imagens_RESERVA.md`
- Reserva de texto/patch: `RESERVA_TRABALHO.md`
- Ponte 8 agentes: `Foruns/ponte_laura_completa/` — você escreve em `de_laura.md` (ref `GL-`)
- Ponte GitHub clássica: `ponte_codex_miguel_laura/mensagens/para_miguel/`
- Inbox = 1–3 linhas. Corpo no fórum/ponte.
- Loop Dell Grok agora é **1h ~:51** e **só observa**. Não dispute capa comigo.

## Se `loop_ativo.json` = `miguel`

Failover: o Dell volta a caçar (ZCode +, se o Miguel mandar, eu volto a aplicar). Você volta a shadow até nova ordem.
