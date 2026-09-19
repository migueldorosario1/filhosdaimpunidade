# 20260910 — O `.maintenance` que sobrevive à janela de 10 min NÃO é removido: a casa fica com o gatilho armado

**Data:** 10/09/2026 (ronda 393ª DS-Dell)
**Contexto:** incidente de manutenção do WordPress em produção (cafezinho), 503 no dinâmico de ~11:02 a ~11:12, fechado «sozinho». Pedido de verificação feito pelo DS-N-20260910-023-ADENDO-2 §4 (o DS-N não tem SSH da nuvem; eu tenho a torneira WP-CLI read-only no host).

## O quê (fato, com prova)

1. O `.maintenance` **não foi removido**: às 12:03, ~1 h depois do incidente, `ls -la /var/www/ocafezinho/.maintenance` = **33 B, `www-data:www-data`, mtime `2026-09-10 11:02:18.641`**, conteúdo `<?php $upgrading = 1789048938; ?>`.
2. No mesmo instante o **dinâmico respondia 200** com cache-bust (`?p=269725&x=<rand>`, `/wp-json/`, `/wp-json/wp/v2/posts?per_page=1&x=<rand>`) — ou seja, **arquivo presente e site servindo**.
3. O updater **continua rodando** no host depois do incidente: `wp-content/upgrade-temp-backup/plugins/` (criado 11:02, vazio) e `wp-content/upgrade/wordpress-7.1-es-es/` (**criado 11:56** = novo download de pacote de idioma do core). Nenhum processo de updater vivo às 12:02; `core_updater.lock` e `auto_updater.lock` **inexistentes**.

## Por quê (causa-raiz)

O `wp_maintenance()` do core **só mata a requisição enquanto `time() - $upgrading < 600 s`**. Passados os 10 minutos, ele **retorna sem bloquear e NÃO apaga o arquivo**. Consequência direta: **a janela de 503 fecha pelo cronômetro, não pelo fim do update** — e o resíduo fica em disco indefinidamente. Como o efeito do arquivo depende **só do mtime**, o **próprio upgrader** (que grava `<?php $upgrading = time(); ?>` antes de instalar) **rearma o gatilho** na próxima atualização; um `touch`/rewrite acidental faz o mesmo.

O agravante é de instrumentação, e é a razão de este bug valer registro: **o health check da casa bate na home (cacheada) e reporta «online 200» enquanto o layer dinâmico está 503** — foi exatamente o que o DS-N provou no ADENDO-2 §3b. Nesta classe, **não existe alarme na casa**.

## Como aplicar (régua)

- **Fechar o incidente com o arquivo na mão, não com o 200 de volta.** «O site voltou» ≠ «o `.maintenance` saiu». A verificação é `ls -la` + `stat` no arquivo, não uma requisição bem-sucedida.
- **Remover o `.maintenance` no `finally`/`trap` de todo processo de update** — não só no caminho de sucesso; e limpar `upgrade-temp-backup` órfão.
- **Sonda dupla de health check:** uma URL na home (aceita cache) **e** uma com **cache-bust de 1 caractere** ou no **`/wp-json/`** — a segunda é a única que vê o 503 do dinâmico.
- **Alarme de resíduo (custo ~um `stat`):** `.maintenance` com **mtime > 15 min** = achado de vigilância, mesmo com o site servindo 200.
- **Ação de produção não é alça de vigia:** remover arquivo do host é do dono (us65/ZM); o vigia **registra com prova** e pede.

## Ligação com a família

É a **2ª camada** de duas lições irmãs do mesmo dia: `20260910_health_check_so_ve_cache_nao_ve_503_do_dinamico.md` (DS-N) e `20260910_data_declarada_nao_e_a_hora_do_ar.md` (minha, BUG-192). Todas as três respondem à mesma pergunta de fundo, que é a que eu venho errando: **não «este instrumento está certo?», mas «o que este instrumento NÃO está medindo?»**.
