# Fórum — Todos os V4 entram normalmente na home

**Decisão canônica de Miguel — 13/08/2026, 14:22 BRT**

Por decisão editorial direta de Miguel, a categoria WordPress **No Home**
(`term_id=20699`) deixou de ser aplicada a qualquer matéria produzida pelos
V4. A regra vale para todas as verticais do worker central e para os V4
regionais que reutilizam esse worker.

## Regra viva

- Todo post novo do V4 segue com suas categorias editoriais normais e **sem**
  a categoria `20699`.
- Imagem artificial, nota, cota de capa, horário ou vertical não podem voltar
  a acrescentar `No Home` ao V4.
- O fluxo continua **draft-only**: esta mudança de categoria não autoriza
  publicação automática.
- A regra não remove `No Home` de sistemas que não são V4.

## Aplicação técnica

O worker central ativo, `/root/v4_vertical_draft_worker.py`, recebeu a chave
`V4_NO_HOME_ENABLED = False`. Todos os caminhos conhecidos foram fechados:
decisão por nota/cota, composição da taxonomia, imagem artificial, reparo de
imagem e cota de home. O worker regional importa o módulo central, portanto
herda a mesma regra.

Backup do worker:

`/root/v4_vertical_draft_worker.py.bak_pre_no_home_all_v4_20260813_171929`

## Correção retroativa e validação

- 107 posts V4 que continham `No Home` foram corrigidos no WordPress.
- 107/107 foram validados depois da alteração.
- 0 continuaram com a categoria `20699`.
- 0 mudaram de status editorial.
- 0 ficaram sem categoria.
- O post 264853, que só tinha `No Home`, preservou o status `publish` e recebeu
  a categoria editorial Política (`22`).
- 50 conteúdos não-V4 ainda usam `No Home` e foram preservados.

Backup completo e recuperável do estado anterior no servidor WordPress:

`/root/backup_no_home_v4_20260813_141022/posts_pre.clean.json`

Validação:

`/root/backup_no_home_v4_20260813_141022/validation.json`

Nenhum post foi publicado, apagado ou enviado à lixeira durante esta operação.

## Orientações antigas superadas

Ficam superadas, **somente para o V4**, as políticas anteriores de 10%/20% de
home, score mínimo, `No Home` por imagem artificial e permanência temporária ou
definitiva da categoria. Esses registros continuam no Cérebro como histórico,
mas não devem ser usados como regra operacional atual.

