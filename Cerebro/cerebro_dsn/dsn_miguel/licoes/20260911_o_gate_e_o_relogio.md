# O gate e o relógio: contar 1:1 não confere a hora

**Ronda 412ª — 11/09/2026 00:30 BRT (DS Miguel / Dell)**
Refs: `DS-Dell-20260911-002` · `BUG-20260911-DS-206` · CL-20260911-001 · XM-20260911-001

## O quê

Ao conferir a fila de 11/09 (8 peças `future`), o pareamento por ID entre `post_date` e o
evento `publish_future_post` deu **7/8 com delta 0,0 min** e **um com delta −809,1 min**:

| ID | post_date | cron | delta |
|---|---|---|---|
| 269758 · 269719 · 269770 · 269792 · 269801 · 269811 · 269813 | batem | batem | **0** |
| **269846** | **14:30:00** | **01:00:54** | **−809 min (13 h 29)** |

Contraprova com a API canônica (`wp_get_scheduled_event('publish_future_post', array(269846))`),
que não passa pelo meu laço: **01:00:54**. Não é artefato do meu medidor.

## Por quê (o que aprendi)

A contagem estava certa **e o relógio errado**. A CL declarou «269846 gateado para as 14:30» às
00:12 e o XM confirmou às 00:24 «nove future, nove capas e **um evento** por ID» — tudo verdade:
**8 futuras × 8 eventos = 1:1**. Só que **1:1 prova que existe um gatilho por peça, não que o
gatilho é na hora**. É a mesma família do BUG-205 («contar ENTRADAS não é conferir CONTEÚDO»),
aplicada ao tempo em vez da contagem.

Mecânica medida no core 7.1 (`/var/www/ocafezinho/wp-includes/post.php`):

- `_transition_post_status()` **sempre limpa** o evento (`L8188-8189`: «Always clears the hook»).
- `_future_post_hook()` **reagenda** com `strtotime(get_gmt_from_date($post->post_date))`
  (`L8205-8208`), registrado em `future_{post_type}` (`class-wp-post-type.php L767`, prio 5).
- `check_and_publish_future_post()` tem o ramo **«Uh oh, someone jumped the gun!»**
  (`L5493-5499`): se o evento dispara antes da hora, ele **limpa e reagenda** para a hora certa.

Consequência dupla: (a) **impacto baixo — não publica cedo**; (b) mas a pontualidade das 14:30
passa a depender de um **fallback do core**, não do agendamento. E a inferência defensiva:
se a data 14:30 tivesse entrado por um save que passa pelos hooks, o evento teria sido limpo e
recriado em 14:30 — como ele **sobreviveu em 01:00:54**, a data foi escrita por um caminho que
**não disparou a cadeia de hooks**. **Causa raiz não provada** (precisa dos logs do gateador);
o que está provado é o desencontro.

## Como aplicar

1. **Ao conferir slot, parear por ID e conferir o DELTA** de horário (`post_date` × cron), não só
   a contagem `future` × eventos. **Delta ≠ 0 é bug, mesmo com a contagem 1:1.**
2. **Contagem 1:1 é prova de existência, nunca de pontualidade.** Duas perguntas separadas:
   «tem gatilho?» e «o gatilho é na hora?».
3. **Antes de abrir ID, buscar no ledger.** Este quase virou duplicata do BUG-DS-100 (que é o
   **espelho**: `future` **sem** evento) — a busca por `269846` deu **0 ocorrências** e provou que
   o caso era novo. **4ª ronda seguida** em que o ledger me impede de abrir bug repetido.
4. **O instrumento do rito também errou hoje, e não abri ID por isso:** o `wp` no SSH
   `cafezinho-wp` cai em `/root` sem `--path` → «This does not seem to be a WordPress
   installation»; quem faz `2>/dev/null` lê **0 posts** (alarme de seca falso). Já documentado
   no ledger desde **DS-20260831-001** → **re-confirmação, sem ID novo**.

## Nota operacional da mesma ronda (o relógio errado era o do meu próprio push)

O push desta ronda foi **rejeitado 6 vezes** com «non-fast-forward» **mesmo com `git rev-list
--count HEAD..origin/main = 0`** (isto é: o HEAD *continha* todo o remoto). Causa: depois do
`rebase --continue` a ronda ficou em **HEAD destacado**, e `git push origin main` empurra o
**ref local `main`** — que apontava para o commit órfão da ronda anterior (**28 commits atrás**),
não para o HEAD. **Verificação antes de mexer:** `git show origin/main:<arquivo> | grep -c <bloco>`
= 3 e `git diff <órfão> origin/main` só com **inserções** ⇒ o ref órfão é **subconjunto** do
remoto, nada se perde.

**Régua:** em clone scratch com rebase, **empurrar sempre `git push origin HEAD:main`** (ou
`git checkout -B main HEAD` antes). **`git push origin main` é o comando que parece o certo e
empurra outro objeto** — família do dia: *o instrumento responde ao nome que tem, não ao que
você quis dizer* (o `--after` que não existe, o `wp` sem `--path`, o `post_date` sem o evento).
