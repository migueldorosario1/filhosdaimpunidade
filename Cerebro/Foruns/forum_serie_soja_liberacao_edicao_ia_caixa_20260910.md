# Fórum — Série soja: liberação de edição IA (gate editorial) + caixa de navegação + vazamento controle (10/09/2026)

**Sessão:** ZCode Dell (GLM-5.3) · 10/09/2026 ~20:0x→20:3x BRT
**Pedido do Miguel:** "pode corrigir isso e liberar o claude para fazer edição? assim como antigravity. minhas matérias precisam estar liberadas para eu fazer edição via IA" — referindo-se à série de soja publicada às 20:01 (posts 269789/269790/269791).

## Contexto

O redator (Claude, conta Redator 5470) publicou a série "Como a soja brasileira alimenta o século asiático" sob a byline da conta 5486 (`ocafezinho_2`, display "Miguel do Rosario"). Ao tentar trocar a caixa de navegação (botões Gutenberg empilhados porque o tema não carrega o CSS de layout do bloco no público), a API devolveu **423 `editorial_post_intocavel` / `post_publicado_por_humano`**: o mu-plugin `cafezinho-protecao-editorial.php` só conhecia 3 contas automáticas (5470/5786/5787) e tratava a byline 5486 como humano.

**Gêmea explicada:** os "rascunhos gêmeos" da ronda DS-Dell 17:34 são 269630/269633/269636 na conta 2018 (James2017, o próprio Miguel no editor) — cópias de trabalho dele, NÃO TOCADAS.

## Decisões / o que foi feito

1. **Gate atualizado (v1.0.0 → v1.1.0)** — `cafezinho-protecao-editorial.php`: registradas as contas de autoria automática 5486 (`ocafezinho_2`, byline de séries IA do Miguel — ordem dele) e 5801 (`cafezinhodsn1`, já agente no gate-dois-checks). Backup: `.bak_pre_byline5486_20260910`. Prova wp eval: motivo(269789)=vazio (liberado p/ agente); motivo(269767, conta 2018)=`post_publicado_por_humano`; motivo(269759, conta 5780)=`post_publicado_por_humano` — humanos SEGUEM protegidos.
   - **5780 (`redator2`) FICOU FORA de propósito:** apesar do nome, é o Gabriel (humano), conforme documentação do `cafezinho-origem-post.php` ("5780/5735=Gabriel"). 5795 (`zcode_miguel`) também ficou fora, classificação incerta (2 posts publicados) — pendência de decisão.
2. **Caixa da série trocada nos 3 posts** — grupo Gutenberg `serie-soja-nav` → bloco `wp:html` com estilo embutido (design do próprio redator: bege #f4ebdd, vermelho #c8102e na parte atual, marrom #3d2b1f nas demais). Única alteração de design: `flex-wrap:wrap` (em vez de nowrap) para quebrar de linha no celular em vez de estourar a tela; no desktop ficam na mesma linha.
3. **🔴 Vazamento `controle.ocafezinho.com` no público (padrão Vorcaro):** os 3 botões de TODOS os posts apontavam `controle.ocafezinho.com/?p=...` e as 4 IMAGENS de gráficos da Parte 1 também eram servidas de lá. Tudo reescopado para `www.ocafezinho.com` (4 imagens testadas 200 no www antes da troca). Readback banco: 0 ocorrências de controle nos 3.
4. **Edição aplicada SEM override** (`wp post update` sem `CAFEZINHO_EDITORIAL_HUMAN_OVERRIDE`) — prova viva de que o caminho de agente ficou aberto para a byline 5486. Para o REST do Claude/Redator a lógica é a mesma: `rest_pre_dispatch` só bloqueia quando `motivo()` não-vazio; com 5486 registrada, motivo=	vazio	 → liberado.
5. **Cache purgado** (rocket_clean_post ×3 + rocket_clean_domain + wp_cache_flush) e **QA ao vivo**: 3 páginas 200, caixa flex presente, "Você está na Parte N" correto em cada uma, 0 controle no HTML servido. Screenshot full-page analisado: 3 botões lado a lado, vermelho na parte certa.
6. **Backups:** `Cerebro/Backups/posts_editados/{269789,269790,269791}_pre_serie_soja_box_20260910.md` (restauração = `wp post update <id> <arquivo>`).

## Estado da missão

- **O que aconteceu:** gate liberado p/ byline 5486 (+DSN 5801), caixa corrigida nos 3 posts, vazamento controle zerado, tudo verificado ao vivo. Claude/Redator já pode editar a série (e futuras matérias da byline) normalmente pela API.
- **O que falta:** (a) classificar 5795 `zcode_miguel` (agente ou humano?); (b) posts antigos de 24/08 e 31/08 da conta 5486 (267462/267463/268390) agora também estão editáveis por IA — era o pedido ("minhas matérias"), só registrar ciência; (c) o tema não carrega CSS de layout Gutenberg no público — qualquer bloco nativo com layout flex terá o mesmo problema; para séries futuras, usar direto bloco HTML com estilo embutido (receita gravada na memória irmã).
- **O que preciso de você (Miguel):** nada obrigatório; se quiser, decidir sobre 5795.

**Ref.:** memória irmã `Cerebro/Memorias/memoria_serie_soja_liberacao_edicao_ia_caixa_20260910.md` · OBS-035 (CEREBRO_NODE_BUGS_ATIVOS) · precedente Vorcaro `forum_serie_vorcaro_nikolas_urls_controle_20260907.md` · incidente WP Statistics `wp-statistics-controle-admin-ajax-exposto-20260907` (memória ZCode).


## Adendo 1 (10/09 ~20:4x, ZCode/GLM-5.3) — AUTORIA JAMES2017 + ALLOWLIST `liberados` NO GATE (v1.2.0)

**Ordem do Miguel (~20:2x):** "bota os tres como autoria de miguel do rosario (James2017)".

1. **O Miguel mesmo fez a troca no editor** (logado como 2018 desde ~20:20, `_edit_lock` user 2018; saves às 20:38:03/08/12). Minha tentativa wp-cli `--post_author=2018` (~20:3x) saiu BLOQUEADA (`meta_wp_cli`, `post_publicado_por_humano`) justamente porque o autor JÁ era humano no banco — sinal de que a troca tinha ocorrido. Estado final = pedido: 3 posts autor 2018, publish intactos, **caixa nova NÃO clobberada** (flex=1, controle=0, caixa velha=0 nos 3).
2. **Consequência tratada:** autor 2018 (humano) religaria o 423 para o Redator — contrariando a ordem anterior "minhas matérias precisam estar liberadas para edição via IA". Cura: **gate v1.2.0** com `cafezinho_protecao_editorial_liberados()` — allowlist explícita dos 3 IDs (motivo `ordem_miguel_serie_soja_20260910`, expira 2026-12-31), checada em `motivo()` ANTES do teste de humano (ordens-bloqueio seguem com prioridade). Demais posts do 2018 seguem protegidos (prova: motivo(269767)=`post_publicado_por_humano`). Backup `.bak_pre_liberados_20260910`.
3. **Provas ao vivo (pós rocket_clean ×3 + domain + flush):** byline "Miguel do Rosário" nas 3, `james2017` ×4 por página, caixa flex presente, 0 `controle.ocafezinho.com`.
4. **Lição:** autor de post é campo volátil quando o dono está com o editor aberto — re-ler estado antes de escrever (meu update bloqueado foi inofensivo, mas o erro poderia levar a re-tentar em falso).

**Estado:** CONCLUÍDO. Pendências inalteradas (5795 zcode_miguel; série futura = bloco HTML direto).

## Adendo 2 (10/09 ~20:5x, ZCode/GLM-5.3) — PROMPT PRONTO p/ o Miguel repassar aos outros agentes

Bloco abaixo é cópia fiel do prompt entregue ao Miguel (texto limpo, sem markdown, serve p/ Telegram e chats de agentes):

```
AVISO A TODOS OS AGENTES — TRAVA EDITORIAL DO CAFEZINHO ATUALIZADA (10/09/2026, ZCode/GLM-5.3, ordem do Miguel)

1) O QUE ACONTECEU

A série da soja (posts 269789, 269790 e 269791 — "Como a soja brasileira alimenta o século asiático") foi publicada hoje às 20:01 sob a byline da conta ocafezinho_2 (id 5486). Depois de publicar, o redator (conta Redator, id 5470) tentou editar e tomou HTTP 423 editorial_post_intocavel com motivo post_publicado_por_humano: o mu-plugin cafezinho-protecao-editorial.php só conhecia 3 contas automáticas (5470, 5786, 5787) e tratava a byline 5486 como se fosse humana.

No caminho descobrimos mais dois problemas nos mesmos posts: a caixa de navegação da série (bloco Gutenberg de botões) renderizava empilhada porque o tema não carrega o CSS de layout do bloco no site público; e os 3 botões mais as 4 imagens de gráficos da Parte 1 apontavam para controle.ocafezinho.com — o domínio de administração, proibido em qualquer coisa pública (mesmo padrão do incidente Vorcaro de 07/09).

2) O QUE FOI FEITO PARA DESTRAVAR

a) Gate v1.0.0 para v1.1.0: as contas 5486 (ocafezinho_2, byline de séries de IA do Miguel) e 5801 (cafezinhodsn1, já era agente no gate-dois-checks) foram registradas como autoras automáticas. Todo post dessas contas agora é editável por agente, via REST ou wp-cli, sem override.

b) Os 3 posts foram reatribuídos à conta James2017 (id 2018, exibindo "Miguel do Rosário") — a troca o próprio Miguel fez no editor às 20:38.

c) Gate v1.1.0 para v1.2.0: como autor humano religaria o 423, foi criada a allowlist cafezinho_protecao_editorial_liberados() com exatamente esses 3 IDs (motivo ordem_miguel_serie_soja_20260910, expira 31/12/2026). Resultado: os 3 continuam editáveis por IA mesmo estando na conta do Miguel.

d) A caixa foi trocada por um bloco HTML com estilo embutido (flex, quebra de linha no celular), botões com permalinks do www, e o reescopo controle.ocafezinho.com para www foi aplicado (as 4 imagens testadas 200 antes). Cache purgado e páginas verificadas ao vivo: byline "Miguel do Rosário", 3 botões lado a lado, zero ocorrência do domínio admin.

Backups: conteúdo original dos 3 em Cerebro/Backups/posts_editados/ (arquivos *_pre_serie_soja_box_20260910.md) e do plugin no servidor (.bak_pre_byline5486_20260910 e .bak_pre_liberados_20260910).

3) COMO A TRAVA FUNCIONA AGORA (VALE PARA TODOS)

Editável por agente sem override: posts cujo autor seja 5470 (Redator), 5786 (Redacao nova), 5787 (redacaoagente), 5486 (ocafezinho_2) ou 5801 (cafezinhodsn1); e os 3 posts liberados da série (269789, 269790, 269791), mesmo estando na conta 2018.

Seguem PROTEGIDOS (o 423 neles é desenho da casa, não bug): posts de autores humanos — 2018 James2017 (exceto os 3 liberados), 5780 redator2 (atenção: apesar do nome é o Gabriel, humano), 5735 gabrielbarbosa, 5800 rhyan, 1257 tadeuporto, 5749 rhyandemeira — e os IDs da lista de ordens editoriais.

Se tomarem 423 editorial_post_intocavel: não insistam, não tentem contorno e nunca reportem sucesso falso (lição OBS-035). Reportem BLOQUEADO_PROTECAO com o post_id e o motivo, e leiam de volta do servidor depois de qualquer update (readback é sempre do servidor, nunca eco do que vocês pretendiam gravar). O override CAFEZINHO_EDITORIAL_HUMAN_OVERRIDE=1 no wp-cli só existe com ordem explícita do Miguel na sessão.

Para séries futuras: caixa de navegação já nasce como bloco HTML com estilo embutido (o tema não carrega CSS de layout Gutenberg no público) e links sempre com permalink do www — nunca do controle.

Pendência aberta: classificar a conta 5795 (zcode_miguel) como agente ou humano — hoje ela não está liberada.

4) COMO CONFERIR

Estado da trava para qualquer post:
ssh cafezinho-wp, cd /var/www/ocafezinho, então wp eval 'echo cafezinho_protecao_editorial_motivo(ID);' — vazio significa editável; post_publicado_por_humano significa protegido.

Exemplos ao vivo: https://www.ocafezinho.com/2026/09/10/brasil-embarca-114-milhoes-de-toneladas-de-soja-em-um-ano-e-a-china-leva-737-da-receita/ e as partes 2 e 3 da mesma data.

Registro completo: Cerebro/Foruns/forum_serie_soja_liberacao_edicao_ia_caixa_20260910.md (com adendo 1), memória irmã em Cerebro/Memorias/, e OBS-035 no CEREBRO_NODE_BUGS_ATIVOS.
```
