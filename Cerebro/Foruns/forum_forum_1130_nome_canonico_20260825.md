# 📺 Fórum 11:30 — nome canônico do programa da TV Fórum (ordem do Miguel 25/08/2026)

**Ref:** ZM-20260825-019 · **Sessão:** ZCode/GLM-5.3 (Dell) · **Data:** 25/08/2026 ~17:00–17:40 BRT
**Par:** `Memorias/memoria_forum_1130_nome_canonico_20260825.md`

## 1. A ordem

Miguel (25/08, chat): **"o nome do programa é Forum 11:30 — corrige lá e ensina ao agente, porque esse é um programa recorrente"** (link do post 267639).

## 2. Verificação na fonte (Regra de Ouro: nome próprio SEMPRE com busca)

- **Playlist oficial do canal TV Fórum:** título **"FÓRUM ONZE E MEIA"** (`PL0M7rdgIk2iifjePO89emPPttp8cELtUg`, 100 episódios, contém o episódio da matéria `_ipojHkU4fA`).
- **oEmbed do vídeo-fonte:** título "Flávio Bolsonaro:100 dias sem explicar milhões de Vorcaro para filme | Janja reage a ataque de Renan", canal **TV Fórum** (@forumrevista).
- **Nome editorial fixado para o site: "Fórum 11:30"** (ordem do Miguel + acentuação da marca TV Fórum; "Onze e Meia" é a forma por extenso da mesma coisa — fica como alias, não como rótulo do site). Conduzido por **Renato Rovai**.

## 3. O que aconteceu (estado)

- **2 posts publicados com o nome errado "Fórum 11.6"** (alucinação do campo `programa` da análise LLM — episódios recentes não trazem o nome no título, e o agente inventou):
  - **267639** (25/08, Flávio/Texas): 3× corpo + 1× subtítulo (excerpt) → corrigido ✅
  - **267498** (24/08, Lula na Record/debate Band): 1× corpo → corrigido ✅
- **Provas no ar:** ambos HTTP 200; 267639 com 7× "Fórum 11:30" (incl. og tags) na produção.
- Backups de segurança: `/root/backups_cafezinho/post_{267498,267639}_{content,excerpt}_pre_forum1130_*.html|txt` no servidor do site.

## 4. 🔴 INCIDENTE-ESCOLA: a edição sumiu com o post do ar (slot de 20min)

`wp post update` num post de **autor-agente** re-dispara o mu-plugin **cafezinho-slot-20min.php** (Emenda 5): como surgiu um vizinho a <20min da data original (267641 às 18:36:47 GMT vs 18:18:18 do post), a máquina empurrou o post para 20:58 GMT e virou **`future`** → origem passou a dar 404 → produção (cache NAT 190.89.239.31/CF) serviu página velha stale. 

**Resolução:** republicado com `post_date`+`post_date_gmt` = **15:15:18 / 18:15:18** (≥20min dos dois vizinhos; mesmo dia, mesmo slug, 3 min antes do original) + `CAFEZINHO_EDITORIAL_HUMAN_OVERRIDE=1` (correção sancionada pelo Miguel, §119/§130).

### ⚠️ LIÇÃO PERMANENTE para TODO agente que corrige post publicado via wp-cli
1. **Sempre** passar `--post_date` **E** `--post_date_gmt` num slot livre (≥20min de qualquer vizinho publish/future) — ou editar como autor humano.
2. **Sempre** conferir `post_status=publish` DEPOIS da edição (`wp post get <id> --field=post_status`).
3. **Sempre** provar no ar (curl externo) — origem 200 não basta se a cadeia de cache (WP Rocket → NAT .31 → Cloudflare) estiver servindo stale; origem saudável atualiza a cadeia sozinha em ~1min.

## 5. Ensino do agente (o pedido central do Miguel)

1. **Banco de nomes canônicos** (`agent_data/personagens_youtube.json`, agora 248 personagens):
   - entrada nova **"Fórum 11:30"** com aliases `Fórum Onze e Meia`, `Forum 11:30`, `Fórum 11 e Meia`, **`Fórum 11.6`** (a grafia alucinada vira alias → na próxima transcrição o casamento já devolve o canônico);
   - stub duvidoso "Renato Rova" (transcrição truncada) → alias de **"Renato Rovai"** (confirmado);
   - backup `personagens_youtube.json.bak_pre_forum1130_20260825`; teste 3/3 ("Fórum 11.6"/"Fórum Onze e Meia"/"Fórum 11:30" → todos resolvem p/ `Fórum 11:30`).
2. **Código do agente YouTube** (`agentes_cafezinho/youtube_cafezinho.py`, backup `.bak_pre_forum1130_20260825`):
   - `PROGRAMAS_DIARIOS["11meia"]`: rótulo → **"Fórum 11:30"**; `match` ganha `fórum 11:30`, `forum 11:30`, `fórum 11.6`, `forum 11.6`;
   - **`_nota_nome_programa(video)` nova** (espelho da `_nota_apresentador`): nota editorial permanente injetada nos prompts de `analisar()` e `redigir()` para TODO vídeo da TV Fórum — "escreva SEMPRE 'Fórum 11:30', NUNCA 'Fórum 11.6'/'Onze e Meia'/variações";
   - sintaxe OK (py_compile) + testes: nota dispara p/ TV Fórum (2 casos) e não dispara p/ outro canal.

## 6. O que falta / o que preciso de você (Miguel)

- **Nada obrigatório** — correção no ar, agente ensinado em 2 camadas (banco + prompt).
- Opcional: se quiser o nome SEM acento ("Forum 11:30") ou a forma por extenso ("Fórum Onze e Meia") como rótulo do site, é 1 minuto — hoje fixei **"Fórum 11:30"** (sua ordem + acento da marca TV Fórum).

## Histórico

- 25/08 ~17:40 — criado por ZCode/GLM-5.3 (sprint completo: fonte verificada, 2 posts corrigidos, incidente slot resolvido, agente ensinado, lição registrada).
