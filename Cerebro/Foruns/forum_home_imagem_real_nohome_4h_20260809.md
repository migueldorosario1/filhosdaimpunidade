# Home com imagem real e No Home temporário de 4h

> [!WARNING]
> **POLÍTICA SUPERADA PARA OS V4 em 13/08/2026.** Por ordem de Miguel, nenhum
> V4 usa mais `No Home`, inclusive quando a imagem é artificial. Consulte
> `forum_v4_sem_no_home_20260813.md`. O restante deste arquivo é histórico.

**Data:** 9 de agosto de 2026  
**Autoridade:** decisão direta de Miguel  
**Executor:** Codex  
**Status:** aplicado em produção com backups e testes sem publicação

## Regra editorial

1. Imagem artificial recebe a categoria `No Home` (`20699`) no momento em que o V4 anexa a mídia.
2. O removedor volta a retirar `No Home` depois de quatro horas. Como o cron roda a cada duas horas, a retirada efetiva ocorre entre quatro e seis horas.
3. A home recusa posts marcados com imagem artificial. A cota de capa por pontuação continua ativa.
4. A Manchete possui bloqueio rígido contra imagem artificial, tanto na escolha manual quanto na renderização da capa.
5. Fontes classificadas como reais pelo V4: Banco Ouro, fonte original, Flickr oficial, biblioteca V4, busca ativa de foto real e biblioteca WordPress auditada.

## Implementação

### NYC

- `/root/v4_vertical_draft_worker.py`: persiste `cafezinho_image_kind=real|artificial` e o gerador no post e no attachment; força `No Home` quando o resultado é artificial; registra `image_kind` no evento.
- `/root/agent_data/no_home_score_policy.json`: versão `v2-home-real` com a regra declarada.
- cron `0 */2 * * * ... remover_no_home.py` reativado; `NO_HOME_TEMPO_ESPERA` permanece com default 4.
- backup do worker: `/root/v4_vertical_draft_worker.py.bak_pre_home_real_20260809_170303`.
- backup do crontab: `/root/crontab.pre_home_real_20260809_170303.txt`.
- backup da política: `/root/agent_data/no_home_score_policy.json.bak_pre_home_real_20260809_170303`.

### WordPress canônico

- novo MU plugin: `/var/www/ocafezinho/wp-content/mu-plugins/cafezinho-real-image-gate.php`.
- registra os metadados REST do post e attachment;
- exclui imagens artificiais das consultas da front page;
- intercepta a ação manual `highlight_process` e devolve HTTP 403 para Manchete artificial;
- possui heurística de compatibilidade para imagens antigas ainda sem metadado estruturado.

## Testes

- Python `py_compile`: OK.
- classificação de nove geradores reais/artificiais: OK.
- PHP `-l` no servidor: OK.
- metadados REST de post e attachment registrados: OK.
- detector legado reconheceu `Ilustração editorial / Flux Pro`: OK.
- cron ativo e limiar lido como 4 horas: OK; 33 posts `No Home` observados em leitura, sem execução manual do removedor.
- home HTTP 200 após purge do WP Rocket.
- nenhuma matéria foi publicada ou editada para o teste.

## Caso real encontrado pelo gate

A Manchete configurada no banco era o post `264832`, com attachment `264841`. A legenda e descrição dizem `Ilustração: Cafezinho / Flux Pro`; o detector classificou `artificial`. Depois do purge, o post deixou de ser renderizado na Manchete, conforme a nova regra. Nenhuma substituição automática foi feita: uma nova Manchete real deve ser escolhida pelo fluxo editorial.

## Rollback

1. Restaurar worker, política e crontab pelos backups acima.
2. Remover o MU plugin `cafezinho-real-image-gate.php`.
3. Purgar WP Rocket e object cache.

— Codex · imagem artificial pode publicar, mas não governa a capa

## Adendo — foto real liberada após 1 hora (12/08/2026)

Por decisão direta de Miguel, o `No Home` foi relaxado para posts com foto
real verificada:

- foto real confirmada pelo gate da Manchete: espera mínima de **1 hora**;
- imagem artificial, desconhecida ou sem confirmação positiva: mantém **4 horas**;
- ledger de `no-home` permanente continua prevalecendo;
- cron do NYC passou de `0 */2` para `0 *`, reduzindo a liberação efetiva de
  1–3 horas para aproximadamente 1–2 horas após a publicação.

O MU plugin canônico agora expõe o booleano REST
`cafezinho_verified_real_image`, calculado pelo mesmo verificador positivo da
Manchete. O removedor não tenta inferir `unknown` como foto real.

Deploy e validação:

- NYC: `/root/remover_no_home.py`; backup
  `/root/remover_no_home.py.bak_pre_real_1h_20260812`;
- crontab NYC: backup `/root/crontab.bak_pre_nohome_real_1h_20260812.txt`;
- WordPress: MU plugin `cafezinho-real-image-gate.php`; backup
  `/root/cafezinho-real-image-gate.php.bak_pre_nohome_real_1h_20260812`;
- `py_compile`, `php -l`, teste positivo/negativo do campo REST e teste dos
  limiares 1h/4h aprovados;
- primeira execução liberou os posts 265391, 265381 e 265367; preservou o
  permanente 265204. O legado 264853 permaneceu protegido porque só possui a
  categoria 20699 e o removedor não deixa posts sem categoria.
