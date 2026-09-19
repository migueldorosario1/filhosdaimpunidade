# 📝 Memória — Ponte de Imagens V4 no Dell: runbook provado + lições + encerramento da operação ativa

**Data:** 27/08/2026 13:45 BRT · **Quem:** ZCode/GLM-5.3 (antes Qwen 3.8, sessão iniciada ~21/08) · **Evento:** ordem do Miguel — caçadora ATIVA desligada no Dell (caçador forte é o do Laura: Zepo de Laura + Clô de Laura reativados + Clô de Miguel); aqui fica só ronda leve de verificação/oferecimento 4/4h (automação `automation-e1b2d648`, antes 1/1h).

## 1. Método provado de aplicação de capa (o coração do runbook — validado ao vivo 26/08)

Ordem inegociável: **reservas → fila → banco depurado/pesquisa → Read da imagem (REGRA-MÃE) → Tribunal Visual → carimbo `_cafezinho_img_check` casado ANTES do `_thumbnail_id` → readback → LOG/reservas**.

```bash
# CANÔNICO (ocafezinho.com)
M=$(ssh cafezinho-wp "sudo -u www-data wp --path=/var/www/ocafezinho media import '<URL>' --post_id=<ID> --title='...' --caption='... — Crédito: <autor> — Licença: <licença>' --porcelain")
ssh cafezinho-wp "sudo -u www-data wp post meta update <ID> _cafezinho_img_check '<JSON com media_id LITERAL>'"
ssh cafezinho-wp "sudo -u www-data wp post meta update <ID> _thumbnail_id <M>"
ssh cafezinho-wp "sudo -u www-data wp eval 'echo get_post_thumbnail_id(<ID>);'"
# ESPELHO: ssh root@159.65.177.60, --allow-root --path=/var/www/cafezinho-news (HÍFEN!)
```

JSON do carimbo: `{"ts":"<ISO>","checker":"tribunal_visual","ok":true,"veredicto":"APROVADA","media_id":<ID literal>,"nota":"..."}`.

Tribunal Visual: `ssh nyc '/root/venv/bin/python3 /root/checar_imagem_vision.py "<url>" "<título>" "<1º parágrafo>" "<crédito>"'` → exit 0 APROVADA / 1 REPROVADA / 2 indisponível (fallback = checagem visual própria, checker `agente_visual`).

## 2. Lições duras (todas pagas com erro real)

1. **JSON por interpolação de shell quebra** (aspas → `media_id:267793,` inválido; gate visao-capa bloqueou o thumb com motivo `capa_sem_visao_casada_emenda7`). Fix: IDs literais no JSON, nunca variável interpolada com aspas tortas.
2. **Carimbo ANTES do `_thumbnail_id`** — o mu-plugin `cafezinho-gate-visao-capa.php` fail-close rejeita thumb sem carimbo casado (mesma media_id).
3. **Emenda 6 trava MD5 repetido**: `cafezinho-manifesto-fotos.php` bloqueou MD5 já usado por OUTRO post de agente (caso 267542: loop reusou foto do 265908 em 23/08 — bug de dedup do loop, não burlar a trava; crop = mesma foto).
4. **URL de thumb do Commons só via API** (`prop=imageinfo&iiprop=url`) — URL adivinhada dá 404/HTML.
5. **Espelho é `cafezinho-news` com HÍFEN** (`/var/www/cafezinho-news`); ponto = scan vazio.
6. **Sync do repo cerebro-miguel pode NÃO pegar arquivos recém-appendados** (caso 17:07 de 26/08: MON subiu, de_dell/LOG não). Prova de subida = `git show origin/main:<path> | grep <marca>`; se faltar, `cp` manual do Cérebro real para `cerebro-miguel/cerebro/` + commit + push.
7. **Tribunal é rigoroso com retrato oficial**: reprovou retrato Senado, foto bandeira-RJ, TSE 161px (pequena demais) e pessoa agachada ao telefone. Emenda 12: pessoa = foto jornalística recente; "foto de arquivo" com legenda honesta passa.
8. **Livro de reservas parado 21/08→26/08** = 5 dias de vacilo sem ninguém notar — a ronda de verificação existe pra isso.
9. **DeepSeek não tem visão**: Read de imagem devolve `[Unsupported Image]` — PASSO visual não roda no fallback (ordem 27/08: sessão no GLM com DeepSeek fallback; parte visual pausa e avisa).
10. Máx 3 canônico + 3 espelho por rodada; Ficção (100002) NUNCA recebe foto da caçadora; BANCO original CONGELADO, depurado (285) é candidato com checagem obrigatória; reservas do GROK <2h = pular.

## 3. Estado da fila no encerramento

- Canônico: 3 aplicados 26/08 16-17h (267589→267792 Leite, 267743→267794 Cleitinho, 267770→267796 Redentor); 267542 (Flávio) pendente foto NOVA (Emenda 6); varredura thumb-sem-meta vazia.
- Espelho: 3 aplicados (267701→400149 Lula chapéu, 267742→400150 Pezeshkian, 267585→400151 Ormuz NASA); **~12 publicados sem capa restantes** — fila para o caçador do Laura ou failover futuro.
- Registros: LOG rodada 26/08 16:55 completa; reservas APLICADO; ZM-20260826-023 na ponte de_dell.

## 4. Nova ronda (backup 4/4h)

Automação `automation-e1b2d648` reescrita: ronda leve 4/4h às :10 — lê pontes/LOG/MONITORAMENTo; se `loop_ativo=laura` e tudo fluindo = SKIP de 1 linha; se failover (`miguel`) = executa ESTE runbook; se alguém precisando = OFERECE ajuda na ponte (não executa sem convite/failover).

**O que aconteceu:** caçadora ativa encerrada no Dell com fila registrada e lições gravadas. **O que falta:** ~12 capas do espelho (dono: Laura) + 267542 canônico. **O que preciso do Miguel:** nada — ronda backup já ativa.
