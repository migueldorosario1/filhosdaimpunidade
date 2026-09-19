# Cartão de Bolso — Conferir, corrigir e publicar no WordPress canônico do Cafezinho

**Atualizado:** 2026-08-14  
**Para quem:** Grok, Claude, Codex, Kimi, GLM, DeepSeek, Qwen, ZCode e qualquer agente CLI com SSH.  
**Origem:** carta operacional ao Grok, 14/08/2026 (expande a diretriz da Trindade de 13/08).  
**Node-mãe:** `Cerebro/CEREBRO_NODE_PUBLICACAO_WP_CAFEZINHO.md`  
**Acesso SSH (tutorial):** `Cerebro/cartoes_bolso/CARTAO_BOLSO_SSH_SERVIDOR_WP_CAFEZINHO.md`  
**Fórum da diretriz:** `Cerebro/Foruns/forum_diretriz_correcao_posts_ssh_wpcli_trindade_20260813.md`

> **Regra de relatório:** use o alias `cafezinho-wp`. Não exponha IP, porta, chaves, senhas nem Application Passwords em chat, fórum, memória ou Git.

---

## TL;DR

```text
SSH cafezinho-wp → /var/www/ocafezinho → sudo -u www-data wp
→ funções oficiais do WordPress → validar de novo no WP-CLI
```

| Ação | Caminho |
|------|---------|
| Conferir fila / rascunhos / publicados | `wp post list` + `wp post get` + termos + metas |
| Correção pequena | `wp post update` |
| Conteúdo longo, taxonomia, imagem, lote | PHP + `wp eval-file` |
| Publicar | só com autorização editorial explícita |
| REST | fallback (sem SSH, integração externa, criação remota de rascunho) |
| `UPDATE` no MySQL | proibido para corrigir post |

O tema do canônico pode cuspir um `PHP Notice: Undefined index: HTTP_HOST` no stderr do WP-CLI. Ignore o notice; leia a tabela/JSON que vem depois. Não é falha do comando.

---

## 1. Acesso correto

```bash
ssh cafezinho-wp
# WordPress canônico: /var/www/ocafezinho

ssh cafezinho-wp \
  'cd /var/www/ocafezinho && sudo -u www-data wp ...'
```

- Sempre `www-data`. Rodar WP-CLI como `root --allow-root` deixa upload com dono errado.
- Não confundir com NYC, Tencent, GSN ou o espelho `cafezinho.news`.
- Credenciais cruas ficam no cofre (`Outros/chaves/ssh_servidor_wp_cafezinho.md`) — nunca neste cartão.

---

## 2. Conferir os posts mais recentes

Inclui rascunho, pendente, agendado e publicado:

```bash
ssh cafezinho-wp \
  'cd /var/www/ocafezinho && sudo -u www-data wp post list \
    --post_type=post \
    --post_status=draft,pending,future,publish \
    --orderby=date \
    --order=DESC \
    --posts_per_page=20 \
    --fields=ID,post_date,post_status,post_title,post_author \
    --format=table'
```

Publicados nos últimos 20 minutos (útil para vigília / loop):

```bash
ssh cafezinho-wp \
  "cd /var/www/ocafezinho && sudo -u www-data wp post list \
    --post_type=post \
    --post_status=publish \
    --after='$(date -d '20 minutes ago' '+%Y-%m-%d %H:%M:%S')' \
    --orderby=date --order=DESC --posts_per_page=20 \
    --fields=ID,post_date,post_status,post_title \
    --format=table"
```

Um post específico (troque o ID):

```bash
ssh cafezinho-wp \
  'cd /var/www/ocafezinho && sudo -u www-data wp post get 265699 --format=json'
```

Complementos obrigatórios na conferência editorial:

```bash
ID=265699
ssh cafezinho-wp "cd /var/www/ocafezinho && \
  sudo -u www-data wp post term list $ID category && \
  sudo -u www-data wp post term list $ID post_tag && \
  sudo -u www-data wp post meta get $ID _thumbnail_id && \
  sudo -u www-data wp post meta get $ID zizi_job_id && \
  sudo -u www-data wp post meta get $ID _agente_origem && \
  sudo -u www-data wp post meta get $ID _edit_last"
```

### Como ler os marcadores

| Sinal | Leitura |
|-------|---------|
| `zizi_job_id` começa com `v4d_` | post criado pelo V4 |
| `_agente_origem=repetidor_estatal` | Repetidor Estatal |
| `_edit_last` | usuário da última edição |
| Ausência dos marcadores | **não** prova autoria humana. Cruze autor, último editor, revisões e o restante do meta. |

A API pública (`controle.ocafezinho.com/wp-json`) só enxerga `publish`. Rascunho, `pending` e `future` exigem este SSH.

---

## 3. Backup antes de qualquer correção

Antes de mudar, registre no mínimo:

- ID, título, conteúdo, resumo (`post_excerpt`)
- status, autor
- categorias, tags
- imagem destacada
- metadados relevantes (`zizi_job_id`, `_agente_origem`, `_edit_last`, `_thumbnail_id`)

Lotes com **5 ou mais** posts: JSON completo **antes** da alteração, com data e hora no nome.

Locais habituais:

| Onde | Caminho |
|------|---------|
| Workspace | `Cerebro/backups_pre_edit/YYYY-MM-DD_HHMM_<motivo>.json` |
| Servidor | `/root/backup_<motivo>_YYYYMMDD_HHMMSS/` |

As revisões nativas do WordPress ajudam no rollback de um post. **Não substituem** o snapshot JSON em lote.

Nunca use `UPDATE` direto no MySQL para corrigir posts.

---

## 4. Método preferencial para correções

### Correção pequena — WP-CLI direto

```bash
ssh cafezinho-wp \
  'cd /var/www/ocafezinho && sudo -u www-data wp post update 265699 \
    --post_title="Título corrigido"'
```

### Conteúdo longo, categorias, imagem ou lote — `wp eval-file`

```php
<?php

$post_id = 265699;

$result = wp_update_post([
    'ID'         => $post_id,
    'post_title' => 'Título corrigido',
], true);

if (is_wp_error($result)) {
    throw new RuntimeException($result->get_error_message());
}

clean_post_cache($post_id);

echo wp_json_encode([
    'ok'     => true,
    'ID'     => $post_id,
    'status' => get_post_status($post_id),
    'title'  => get_the_title($post_id),
]);
```

```bash
scp patch_post.php cafezinho-wp:/tmp/patch_post.php

ssh cafezinho-wp \
  'cd /var/www/ocafezinho && sudo -u www-data wp eval-file /tmp/patch_post.php'
```

Antes do `scp`: `php -l patch_post.php`. Depois da execução: validar (§9). Não deixe PHP de patch permanente no servidor; `/tmp` é o lugar certo.

---

## 5. Funções oficiais recomendadas

Use sempre as funções do WordPress — elas preservam hooks, revisões, cache e consistência.

| Função | Uso |
|--------|-----|
| `wp_update_post()` | título, texto, resumo, status, autor |
| `wp_set_post_categories()` | categorias (substitui o conjunto) |
| `wp_set_post_tags()` | tags |
| `set_post_thumbnail()` | imagem destacada |
| `delete_post_thumbnail()` | remover imagem destacada |
| `wp_remove_object_terms()` | tirar **uma** categoria ou tag sem tocar nas outras |
| `update_post_meta()` / `delete_post_meta()` | metadados |
| `clean_post_cache()` | invalidar cache do post |
| `get_post()` / `get_post_status()` | conferir depois |
| `wp_get_post_categories()` | conferir categorias |
| `get_post_thumbnail_id()` | conferir imagem destacada |

Não troque título, texto, autoria, imagem e status no mesmo lote sem necessidade.

---

## 6. Retirar “No Home”

Categoria **No Home** = ID **20699**.

Regra editorial vigente (13/08/2026):

- V4 **não** usa No Home.
- Repetidor Estatal **não** usa No Home, inclusive em Previsão do Tempo.
- Registros antigos que dizem o contrário são históricos e estão superados.

Remover sem afetar as demais categorias e sem mudar o status:

```php
<?php

$post_id = 265699;
$status_before = get_post_status($post_id);

$result = wp_remove_object_terms($post_id, 20699, 'category');

if (is_wp_error($result)) {
    throw new RuntimeException($result->get_error_message());
}

clean_post_cache($post_id);

$categories = array_map('intval', wp_get_post_categories($post_id));

if (in_array(20699, $categories, true)) {
    throw new RuntimeException('No Home ainda está presente.');
}

if (get_post_status($post_id) !== $status_before) {
    throw new RuntimeException('O status foi alterado inesperadamente.');
}

echo wp_json_encode([
    'ok'         => true,
    'ID'         => $post_id,
    'status'     => get_post_status($post_id),
    'categories' => $categories,
]);
```

---

## 7. Trocar a imagem destacada

Confirme primeiro que o ID é mídia (`attachment`), não outro post.

```php
<?php

$post_id  = 265699;
$media_id = 265698;

if (get_post_type($media_id) !== 'attachment') {
    throw new RuntimeException('O media_id não é um attachment.');
}

$result = set_post_thumbnail($post_id, $media_id);

if (!$result) {
    throw new RuntimeException('Não foi possível definir a imagem destacada.');
}

clean_post_cache($post_id);

echo wp_json_encode([
    'ok'             => true,
    'ID'             => $post_id,
    'featured_media' => get_post_thumbnail_id($post_id),
]);
```

Não basta anexar. Confira também:

- correspondência com a notícia
- licença e procedência
- crédito e legenda
- resolução
- ausência de texto artificial ou marcas indevidas
- se a destacada **aparece de fato** na URL pública

Não reutilize uma imagem só porque “parece relacionada”.

---

## 8. Publicar

Publicação é ação editorial sensível. Só publique com **autorização explícita** e revisão final.

```php
<?php

$post_id = 265699;

$result = wp_update_post([
    'ID'          => $post_id,
    'post_status' => 'publish',
], true);

if (is_wp_error($result)) {
    throw new RuntimeException($result->get_error_message());
}

clean_post_cache($post_id);

echo wp_json_encode([
    'ok'        => true,
    'ID'        => $post_id,
    'status'    => get_post_status($post_id),
    'permalink' => get_permalink($post_id),
]);
```

Checklist antes de publicar:

- [ ] título revisado
- [ ] texto completo e factual
- [ ] fontes e atribuições
- [ ] categorias corretas (whitelist: `CARTAO_BOLSO_POLITICA_CATEGORIAS.md`)
- [ ] imagem destacada adequada + crédito
- [ ] sem duplicata
- [ ] status autorizado pelo responsável editorial

**V4** continua criando só `draft` / `pending` para revisão humana. Não converta automaticamente a fila V4 em publicação.

**Repetidor Estatal** tem fluxo próprio já homologado para publicação direta.

---

## 9. Validação obrigatória depois da mudança

O comando ter saído sem erro **não** encerra o trabalho. Leia de novo:

```bash
ssh cafezinho-wp \
  'cd /var/www/ocafezinho && sudo -u www-data wp post get 265699 \
    --fields=ID,post_title,post_status,post_modified \
    --format=json'

ssh cafezinho-wp \
  'cd /var/www/ocafezinho && \
    sudo -u www-data wp post term list 265699 category && \
    sudo -u www-data wp post meta get 265699 _thumbnail_id'
```

Se a mudança afetar apresentação, abra a URL pública (`https://www.ocafezinho.com/...`). Se houver cache (WP Rocket), valide depois da invalidação.

---

## 10. Regras de segurança

1. Não alterar diretamente as tabelas do MySQL.
2. Não apagar definitivamente um post; prefira a lixeira.
3. Não publicar sem autorização editorial.
4. Não trocar título, texto, autoria, imagem e status no mesmo lote sem necessidade.
5. Não reutilizar imagem só porque “parece relacionada”.
6. Não interromper um worker no meio da execução.
7. Não instalar patch sem backup, `php -l` e validação posterior.
8. Lote com 5+ posts: manifesto dos IDs + snapshot JSON completo.
9. Mudança estrutural: registrar no Cérebro o backup e o rollback.
10. Relatórios: alias apenas — sem IP, porta, chave ou senha.

Em resumo: SSH para chegar, WP-CLI para carregar o WordPress, funções oficiais para consultar ou modificar. É o mesmo ambiente em que o site opera.

---

## 11. Mapa rápido de documentos

| Preciso de | Documento |
|------------|-----------|
| Este playbook (conferir / corrigir / publicar) | este arquivo |
| Acesso SSH, chave, hardening | `CARTAO_BOLSO_SSH_SERVIDOR_WP_CAFEZINHO.md` |
| REST, cofre, script `publicar_cafezinho_wp.py` | `CEREBRO_NODE_PUBLICACAO_WP_CAFEZINHO.md` |
| Onde categorizar | `CARTAO_BOLSO_POLITICA_CATEGORIAS.md` |
| Menu do site | `CARTAO_BOLSO_MENU_WP_CAFEZINHO.md` |
| Alinhamento da Trindade (13/08) | `Foruns/forum_diretriz_correcao_posts_ssh_wpcli_trindade_20260813.md` |
