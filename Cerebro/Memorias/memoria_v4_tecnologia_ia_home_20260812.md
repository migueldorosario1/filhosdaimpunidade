# V4 Tecnologia — IA tolerada e bloco próprio na home

**Data:** 12/08/2026  
**Autoridade:** decisão direta de Miguel  
**Status:** aplicado e validado em produção

## Diagnóstico

O cron de Ciência, Tecnologia e IA estava ativo a cada 30 minutos, mas a
produção de rascunhos confirmados parou em 11/08. Havia duas causas:

1. `CONFIG["ciencia"]["category_ids"]` ainda continha a categoria WordPress
   `19936`, já inexistente. Todas as tentativas falhavam com
   `wordpress_draft_taxonomy_not_confirmed` e viravam `pending` órfãs.
2. A permissão de IA comparava `cfg["section"]` com `"ciencia"`, embora a seção
   interna dessa vertical seja `"tecnologia"`. Por isso ela caía por engano em
   `image_pending:vertical_sem_ia:tecnologia`.

## Política aplicada

- foto real continua sendo procurada primeiro: Banco Ouro, biblioteca WP,
  fonte original, Flickr e busca ativa;
- se não houver foto real satisfatória, Tecnologia pode gerar imagem por IA;
- posts da vertical Tecnologia não recebem `No Home`, inclusive com IA, para
  alimentar o bloco visual dedicado;
- imagens de IA de Tecnologia continuam identificadas por
  `cafezinho_image_kind=artificial` e com crédito editorial;
- a Manchete principal continua exigindo foto real verificada;
- Cultura continua com proibição absoluta de IA.

## Arquivos e backups

- NYC `/root/v4_vertical_draft_worker.py`;
- backup `/root/v4_vertical_draft_worker.py.bak_pre_tech_tolerant_20260812`;
- WordPress MU plugin
  `/var/www/ocafezinho/wp-content/mu-plugins/cafezinho-real-image-gate.php`;
- backup no servidor WordPress
  `/root/cafezinho-real-image-gate.php.bak_pre_tech_tolerant_20260812`.

## Validação

- `py_compile` e `php -l`: aprovados;
- categorias canônicas confirmadas: Ciência `735`, Tecnologia `30`, IA `5008`;
- teste do gate: post tecnológico com IA não consta na lista global bloqueada;
  post de outra editoria com IA continua bloqueado;
- rodada supervisionada recuperou o post `265389`, anexou a mídia `265403`
  via Flux Pro, preservou `pending`, aplicou categorias `[735, 5008, 30]` e
  não aplicou `20699` (No Home).

## Pendência editorial observada

O coletor de Tecnologia está aceitando excesso de geopolítica geral do feed do
SCMP. O encanamento voltou a funcionar, mas a curadoria temática merece revisão
separada para concentrar o bloco em ciência, tecnologia e IA de fato.
