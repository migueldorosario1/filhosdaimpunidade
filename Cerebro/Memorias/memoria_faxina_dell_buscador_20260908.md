# 🧠 MEMÓRIA — Faxina Total do Dell + Buscador Local (08/09/2026) — log técnico

> Tema Duplo do `Foruns/forum_faxina_dell_buscador_20260908.md` (decisões e plano lá). Aqui: comandos, provas, armadilhas. Sessão ZCode Qwen3.8-Max, Dell "novo", 15:0x→.

## 1. Recuperação de contexto (o "e-cons" da transcrição = a faxina do ZCode)

- Memória `faxina-zcode-peso-receita-vacuum-pendente-20260906`: faxina 06/09 deixou `~/.zcode` 4,7→2,1G, backup B2 validado 7/7 em `b2:failover-cafezinho1/faxina/zcode-dell/zm_20260906_faxina_zcode/` (5 pacotes gpg + SHA256SUMS + manifest — relistado hoje 15:1x, íntegro).
- **VACUUM: o Miguel JÁ RODOU** em 06/09 22:24 (prova: `db.sqlite.bak_pre_vacuum_20260906_2224` 1,6G + db atual 738M ≈ previsão ~800M). A pendência da memória antiga está FECHADA. O `.bak_pre_vacuum` foi apagado hoje (B2 verificado) → `~/.zcode` 2,7→1,2G.

## 2. Vilões encontrados (diagnóstico 15:0x-15:2x)

- Disco 72% (313G/460G). Home 274G: Downloads 121G (AG=120G), Dados_Frios 52G, .deepseek 28G, .config 9,9G (chrome 8,8G), .gemini 9,5G, .local 8,8G (lib 7,1G), .pyenv 7G, Android 5,9G, .cache 5,6G, .nvm 4,1G, .codex 2,9G, ZCodeProject 2,8G, .zcode 2,7G, .grok 2,4G.
- **AG/.ds_ponte_clone_* = 64 clones × ~1,3G = 59,3G** — clones de `git@github.com:migueldorosario1/cerebro-miguel.git` criados pelas rondas DS-Dell (números 248→309; últimos hoje 05:03/05:34/06:06/12:03/12:32 = 1 por ronda ativa, sem cleanup). Amostra clone_308: `git status --porcelain` = 0 linhas, commits do dia já no origin.
- **AG/.git = 27,38GiB pack**, origin `filhosdaimpunidade` (repo-armadilha, memória 06/09), último commit dc23697c 05/09, `status --porcelain` = 3.196 linhas. Refs locais: deploy-main dc23697c (= origin/main GitHub, ls-remote confere), **master 1222f963 (NÃO existe no remote)**, origin/* velhas, **3+ stashes** (vigilia-cm001-stash, index-html-conflict-push, WIP master "Fix UI contrast..."). → N2: exportar patches/stash diffs (KBs) antes de retirar os 27G.
- **.deepseek/snapshots**: `62842bf2b53f9dcb/62842bf2b53f9dcb/` = só `.git`, pack 20,2GiB, **`fatal: missing object 67a32698... for refs/heads/master`** (corrompido, sem bundle possível) → apagado. `f608...` = pack 5,08GiB, master 9829bd0 "post-turn:2" 22/08 15:20, válido → N1 (bundle→B2→retirar).
- **Jornais do dia**: pasta viva `AG/Outros/Jornais do dia/` 7,0G (PDFs novos ~250MB/dia: NYT 90MB, O Globo HD 60MB...) + arquivo velho `Dados_Frios/Jornais do dia/` 6,1G (230 PDFs até ~25/08, 0 arquivos pós-25/08). Cron do Miguel: `jornaisdodia.sh` 10:30/13:00/18:00 = `rclone copy --ignore-existing` p/ `gdrive:Jornais do dia` — **nunca apagou local** (causa do acúmulo).
- Memórias ZCode = 4,4M (leve). Canais = de_dell.md 9,5M, claude.md 3M, de_laura 2,8M, ponte_cafezinho 896K, MONITORAMENTO 290KB (renovação 48h atrasada desde 31/08 — N8).
- Crons ativos relevantes: jornaisdodia ×3, `backup_reforma_local.sh` :20/h (b2 sync Cerebro+Foruns → bucket Cafezinho-pos-grande-reforma-jun2026 = Cérebro JÁ tem espelho B2 horário), `sync_cerebro_to_github.py` :07/:22/:37/:52, `limpa_diario.sh` 04:00 (rm .cache/google-chrome + mesa + tmp openclaw/transcritor/node), sync_foruns_maestro_b2 :05/:35.

## 3. Retiradas executadas (provas no LEDGER_APAGADOS.md)

1. `rm ~/.zcode/cli/db/db.sqlite.bak_pre_vacuum_20260906_2224` (1,6G) — B2 relistado antes.
2. **Sweeper de clones** (log `/tmp/faxina_clones_20260908.log`): guardou os 2 últimos (`ls -dt | head -2` = 309/308); por clone: exige `.git` + `status --porcelain` vazio + `log --branches --not --remotes` vazio + `stash list` vazio (rc=0 nos 3) → rm; senão mv p/ `Dados_Frios/quarentena_ds_clones_20260908/`. **Resultado: 61 apagados (58.832MB), 1 quarentena (clone_276), 2 mantidos.**
3. `rm -rf ~/.cache/whisper ~/.cache/huggingface` (3,3G, re-baixáveis; chrome NÃO tocado — 50 processos ativos; limpa_diario cuida às 04h).
4. `rm -rf ~/.deepseek/snapshots/62842bf2b53f9dcb` (23G corrompido).
5. `Dados_Frios/Jornais do dia`: `rclone check --size-only --one-way` = **230/230 matching, 0 differences** → `find -name '*.pdf' -delete` (6,1G) + APONTADOR.md (pasta 56K).
6. `AG/Outros/Jornais do dia`: listagem `rclone lsf --files-only --format sp gdrive:Jornais do dia` (1216 entradas) → python3: apaga pdf com (nome,tamanho) idêntico no remoto E mtime>3d. **271 apagados (6,35GiB), 20 mantidos** (12 recentes <3d + FT UK ×3/FT US divergentes de tamanho + NYT etc. recentes).
7. **Fluxo corrigido:** `jornaisdodia.sh` ganhou chamada pós-upload de `sweep_jornais_verificados.py` (mesmo critério, fail-safe sem listagem). Backup: `jornaisdodia.sh.bak_pre_faxina_20260908`.

**df: 313G→219G usados (72%→51%); 94G liberados; 218G livres.**

## 4. Quarentena clone_276 (N1b)

314M em `Dados_Frios/quarentena_ds_clones_20260908/.ds_ponte_clone_276`. Único commit local-only 4e86c333 = "DS-N Chefe ronda 283a 10:30 07/09" — **`git cat-file -e` no repo vivo: JÁ ESTÁ LÁ** (pushed por outro clone). Restam: ` M cerebro/CEREBRO_NODE_BUGS_ATIVOS.md`, ` M cerebro/Foruns/ponte_laura_completa/de_dell.md`, 1 stash → diff × vivo, resgatar o único, retirar.

## 5. Buscador (D4 do fórum)

- `Cerebro/Ferramentas/buscador_local/`: `indice_local.py` (walk scandir do $HOME, poda .git/node_modules/__pycache__ em qualquer nível + prefixos de lixo regenerável [.cache, .pyenv, .nvm, .rustup, .gradle, .local/lib, snap, Android/Sdk, .deepseek/snapshots, perfis de navegador, .vscode/extensions...]; pasta podada vira linha excl; rollup size/nfiles por dir; budget anti-runaway; SQLite WAL) + `buscador.py` (read-only: --nome/--caminho/--ext/--min/--max/--antes/--depois/--dir/--pesados/--pastas/--velhos/--duplicatas/--resumo, saída humana com KB/MB/GB).
- DB: `~/.local/share/buscador_local/indice.sqlite` (FORA do Cérebro: sync horário do Cérebro p/ B2 não carrega binário grande).
- **1ª passada (15:37-15:52): 98.422 arq/17.601 dirs em 902s — PARCIAL.** Causa: `~/GDrive` é **mount rclone FUSE** (`drive: on /home/migueldorosario/GDrive type fuse.rclone`; df = 30T/834G; st_dev 55 ≠ 66307 do home) — o walk entrou e varreu 119G de nuvem pela rede; não chegou em `~/Downloads`.
- **Cura (15:5x):** `escanear()` captura `raiz_dev = os.stat(raiz).st_dev` e registra como `excl` (sem entrar) qualquer dir com `st_dev != raiz_dev` — vale p/ qq mount (gvfs, doc, rede). py_compile OK, DB velho apagado.
- **2ª passada (15:56): COMPLETA em 23s — 265.789 arq / 47.457 dirs / 77,0G rollup / parcial=0.** DB 145MB. Testes: `--resumo` OK; `--pesados 8` OK (topo = itens já nas filas N4/N5); `--pastas 12 --caminho AG` OK (AG 23,1G pós-faxina; Dados_Frios 38,4G; Downloads 23,3G); `--nome MANIFESTO_ZM_BACKUP` OK (60 resultados, incl. dentro da quarentena — prova que dotdirs são varridos).

## 6. Automações (D6)

- **LEVE 4/4h CRIADA:** `automation-dcba2ec0-23d6-493e-8a76-56e7076644d4` (cron `40 */4 * * *`, recurring, próximo disparo 08/09 16:40; fora das âncoras :07/:12/:22/:37/:52 e dos crons 09:30/10:30/13:00/18:00): clones DS + sweep jornais + caches regeneráveis + .bak_fallback ZCode >7d + índice --budget 240 + ledger. Silenciosa se nada.
- **PESADA 03:15 NÃO CRIADA — bloqueio do ZCode:** 2º CronCreate na mesma sessão → "Cannot create a scheduled task inside a session that already belongs to a scheduled task" (a 1ª criação vincula a sessão). **Prompt completo arquivado:** `Foruns/sessoes_zcode/PROMPT_AUTOMACAO_FAXINA_PESADA_20260908.md` (título/cron/ritmo N1-N11/rito fail-closed/casos especiais N2+N1b+N8/N9 congelado) — criar em chat novo e registrar o ID no fórum adendo 1 + aqui.

## 7. Armadilhas novas (lições)

- **Quarentena de dotfiles: `ls` sem `-a` e glob `*` NÃO vêem `.ds_ponte_clone_276`** — pareci "quarentena vazia" por um instante; sempre `ls -la`/glob explícito para dotdirs.
- Monitor foi modificado por sessão paralela ENTRE meu Read e meu Edit (tool recusou; reler e re-Edit com âncora fresca — §112 funcionando como desenhado). A linha Brave das 14:0x registra clobber da escrita 15:14 da ronda: monitor está quente hoje.
- `rclone check` no GDrive reclama "Duplicate object/directory found in destination" (gdrive tem duplicatas de nome — ignorar os NOTICE; o que vale é matching×differences).
- GDrive root listing é LENTO (~90s; timeout de 30s estoura) — sempre timeout ≥120s em `rclone lsd/lsf gdrive:`.
- Snapshot DeepSeek corrompido: `git for-each-ref` dá `fatal: missing object` — não confiar no tamanho do pack como prova de integridade.
- AG/.git: refs locais enganam — `deploy-main` local ≠ `origin/deploy-main` remoto, mas == `origin/main` remoto; comparar sha×sha com `git ls-remote`, não nome×nome.
- `pgrep -f deepseek` não pega o agente DS-Dell (nome do processo varia); evidência de atividade = commits/clones frescos, não ps.
- VACUUM do sqlite só encolhe o arquivo com app FECHADO (auto_vacuum=0) — já sabido de 06/09, reconfirmado (db 738M estável 2 dias).
- 🔴 **`~/GDrive` NÃO é pasta local — é mount rclone FUSE do Google Drive** (30T, st_dev próprio): du/walk/indexador que entrar vai varrer a nuvem pela rede (902s parciais vs 23s locais). Sempre checar `mount`/`df`/st_dev antes de medir ou varrer pasta grande do home. O índice local NUNCA atravessa mount (cura st_dev no `escanear()`).
- 🔴 **ZCode: 1 scheduled task por sessão** — o 1º CronCreate vincula a sessão à tarefa e o 2º é recusado ("Cannot create a scheduled task inside a session that already belongs to a scheduled task"). Precisa de 2+ automações → criar em sessões diferentes (prompt arquivado em `Foruns/sessoes_zcode/`, método da retomada VIGIA).
- Edit de arquivo recém-criado na mesma sessão pode falhar com "File has not been read yet" após o contexto ser resumido — reler (offset/limit basta) e refazer o Edit.

## Adendo — REFORÇO do Miguel 08/09 ~16:5x (executado 17:0x-17:3x, custo R$ 0)

Ordem (voz, quase literal): "não quero pagar nada · quero achar com facilidade qualquer diretório/arquivo, um bom índice · deixar o computador leve · o espaço gigantesco do GDrive é PARA USAR, trabalhava com GDrive, os antigos ficam todos na nuvem · o ZCode era para ser bem levinho · tem que limpar os canais de comunicação, já, tudo com backup e indexado na nuvem, bem levinho, mas não quero perder nada · de preferência com dois backups e o index também, de alguma forma duplo".

**Entregas (provas no LEDGER Lote 3 + fórum adendo 3):**
1. **D9 índice duplo:** `gera_seed_faxina.py` ganhou `espelhar_indice()` (1×/dia, marker `.ultimo_espelho`, rclone copy DB→`gdrive:Backup_Total/dell_faxina/indice/` + `b2:failover-cafezinho1/faxina/indice/`, verificação lsf de tamanho) e `catalogo_nuvem()` (CATALOGO_NUVEM.md — listagens rclone legíveis; commitado junto da seed = triplo via repo). 1ª execução 17:09: "cópia verificada (139MB) nos 2 destinos" + push origin ✅.
2. **D10 GDrive primário:** estrutura `Backup_Total/dell_faxina/{indice,zcode,canais}/` criada; curadoria da página atualizada (caixa da nuvem).
3. **ZCode >14d:** `purga_zcode_antigos.sh` — tar (296 arq, 7,8M) → gpg AES256 (passphrase alias `ZM_ZCODE_ANTIGOS_PASSPHRASE` espelhada nos 2 cofres c/ backups `.bak_pre_zcode14d_20260908`) → upload GDrive+B2 → **readback sha256 ×2** → poda. Rotina no passo 4 da leve (CronUpdate 17:2x). DB vivo 738M intocado → **N12** (snapshot semanal, fila).
4. **Canais:** `rotaciona_canais.sh` — de_dell.md 9,5M + de_laura.md 2,8M → `arquivo/backup_2026-09-08_1714/` QUÁDRUPLO (local+GitHub byte-idêntico 9.919.596 provado no origin+GDrive+B2) + vivos novos (1,5K/716b) + ZM-20260908-005 nos vivos e inboxes. Janela: CL observador até 18:00 (régua CL-025), DS entre rondas; swap atômico (cp→mv em segundos).
5. **Página:** seed 26,7% (4/15) 17:29 push origin ✅; Tencent instala via sync */7.

**🔴 Armadilhas novas (todas fail-closed — nada foi perdido):**
- Bash: `"$DIA_MANIFESTO"` vira UMA variável (underscore é caractere válido) — usar `${DIA}_MANIFESTO`. Matou a 1ª execução no passo 3.
- `rclone copy` aceita NO MÁXIMO 2 args (src, dst) — múltiplos arquivos = loop ou pasta. Matou a 2ª execução no passo 4.
- `rclone lsf --format sp` imprime **"tamanho;nome"** (ponto-e-vírgula, tamanho PRIMEIRO) — grep de verificação tem que ser `^${SZ};nome$`, não `nome SZ$`. Falso-negativo na 3ª execução (abortou sem apagar — fail-closed funcionou).
- `rclone cat "$DEST/arq"` com $DEST terminando em `/` = **barra dupla** → exit 3 silencioso; usar `${DEST%/}/arq`.
- gpg simétrico é NÃO-determinístico (salt+timestamp): sha256 muda a cada execução — readback tem que ser da MESMA execução do upload (o script faz tudo em sequência, ok).
- Rotação de canal quente: o risco real não é o append concorrente (janela cp→mv = segundos) e sim o CLOBBER por reescrita completa de outra sessão com cópia velha em memória (precedente CL hoje) — mitigação: aviso nos inboxes + push imediato (repo = verdade recuperável) + janela entre rondas.

### Nota de incidente — publish 17:3x corrompeu 4 canônicos (rescue-append cego), reparado 17:4x

O passo anti-clobber do publish achou "linhas repo-únicas" em `faxina_mapa_curadoria.json` (42), `gera_seed_faxina.py` (7), `LEDGER_APAGADOS.md` (1) e `CEREBRO_NODE_INDICE_LOCAL.md` (4) e as reanexou no EOF — mas eram as versões VELHAS das linhas que EU MESMO reescrevi na sessão (re-dump JSON indent=2 muda todas as linhas; código novo substitui linhas velhas; N10 riscado substitui o pendente). Resultado: JSON inválido (lixo após `}`), SyntaxError no .py (texto após `sys.exit(main())`), N10 duplicado no LEDGER, rows duplicadas no NODE — e os greps-prova passaram (append não remove marcadores). Cura: truncamento cirúrgico (raw_decode p/ JSON; regex até `__main__` p/ py; corte após última linha esperada p/ MD) → validação `json.loads`+`py_compile`+contagens ANTES do cp → re-publish (push ✅ na 2ª tentativa, non-ff de ronda) → provas 6/6 NO ORIGIN com parse real do blob (`git show origin/main:arq | json.loads`, py_compile do blob, contagens N10=1/N12=1, D1-D10=1/D1-D8=0). Gerador re-rodado limpo 17:42 (seed 26,7% 4/15, catálogo OK); página na Tencent HTTP 200 c/ barra 26.7%. **Regra que fica:** resgate de linhas repo-únicas só é seguro p/ markdown append-only de OUTRAS sessões; arquivo self-rewritten/reformatado nunca recebe append cego — e .json/.py jamais; publish passa a validar parse/compile antes do cp e no blob do origin depois do push (grep de marcador não detecta corrupção de estrutura).

## Adendo — página única «💾 Backup e Limpeza» + ZCode podado (ordem 18:4x + reforço ~19h; no ar 19:1x)

**Tencent (painel):** módulo NOVO `~/cafezinho/v6/painel_cctv_v6_backup_limpeza.py` — `render_backup_limpeza_page()` devolve doc completo; o `chrome()` do painel extrai só o `<body>`, então o `<style>` mora DENTRO do body com seletores escopados `#blwrap` (style no head morreria — lição da /v6/reforma reaplicada). CSS/JS são strings PURAS (não f-string) = zero armadilha de chaves×PEP 701. JS puro: aba por `location.pathname` (`/faxina`→limpeza) ou hash; botões `.blfxbtn` toggam `.blfxdet` via `nextElementSibling`. Painel patcheado por script com 6 asserts (count==1 cada): menu `/v6/faxina` REMOVIDO · menu `/v6/backup` renomeado «💾 Backup e Limpeza» · card home · rotas `/faxina` e `/backup` → lambda do módulo novo com `chrome(..., "backup", ...)` · comentário APOSENTADA na `pagina_backup` (código mantido, sem rota). Backup `.bak_pre_backuplimpeza_20260908`. py_compile 3.12 OK (SyntaxWarning `\w` linha 7248 é pré-existente do `_AOVIVO_HTML`, sem relação). restart cctv-v6 active. Testes: interno `127.0.0.1:8084/backup|/faxina` (SEM /v6 — nginx adiciona) 200×2 40.188b; público UA navegador 200×2.

**Dell (cadeia das datas):** curadoria `faxina_mapa_curadoria.json` + chave `faxinas_regulares` (6 itens: n/nome/cadencia/o_que/backups/ultima/resultado/marcador). Gerador `gera_seed_faxina.py` + `resolver_faxinas(curadoria)` → seed ganha `"faxinas"`: marcador `auto:cabecalho_de_dell` = regex «ROTACIONADO em (\d{2}/\d{2}/\d{4} \d{2}:\d{2})» no topo do `de_dell.md` (🔴 o cabeçalho real NÃO é ISO — regex dupla); marcador de arquivo = 1ª linha ISO (`^\d{4}-\d{2}-\d{2}`) senão mtime; saída `ultima_fmt` DD/MM/AAAA[ HH:MM] + `ultima_iso`. `purga_zcode_antigos.sh` grava `.marcadores/purga_zcode` SÓ no fim real (o `exit N` da linha 32 não grava — marcador = última poda de verdade; backup `.bak_pre_marcador_20260908`). Seed 19:02 `--push` com prova no origin (6 faxinas; F3 18:54 do db_snapshot, F4 17:14 do cabeçalho).

**Coletor (`scratch/coletor_backup_dashboard.py`, backup `.bak_pre_pagina_backup_limpeza_20260908`):** `rclone_size` das nuvens timeout 300→600s; `resultado["parciais"]` = nº de pontas de nuvem que retornaram (None,None) — a página exibe ⚠️ «coleta parcial» (causa visível da oscilação de cobertura 303%↔88%); histórico compacto += `parciais`/`duracao_seg`; cap 5→100 coletas. A página tolera JSONs VELHOS sem esses campos (`.get` com default) — testado ao vivo com o histórico antigo.

**ZCode (pergunta do Miguel respondida com números):** `~/.zcode` 1,2G. DB 786M: hot backup (sqlite backup API, integrity ok, 521 sessões/124.182 parts, 750M) → gpg AES256 253.707.154b sha256 9b61caef… → GDrive `Backup_Total/dell_faxina/zcode/db/` + B2 `failover-cafezinho1/faxina/zcode-dell/db/` verificados (lsf "tamanho;nome" + `rclone cat|sha256sum` nos 2) → poda WAL-safe 384/521 sessões >14d em lotes de 15 (busy_timeout 60s, foreign_keys=0; 66.415 linhas: part 18.844 · tool_usage 16.489 · model_usage 14.742 · session_entry 5.363 · message 4.914 · session_input 2.948 · turn_usage 1.803 · todo 1.312; linhas de session preservadas) → freelist 130MB (VACUUM só com app FECHADO — `~/faxina_zcode_vacuum.sh` do Miguel) → marcador `db_snapshot` (= 1ª instância manual da faxina 3/N12). `MEMORY.md` 58,1→34,2KB (hooks inteiros preservados nos arquivos-tópico).

**Estado:** aconteceu = página única no ar (2 abas, datas cheias, botões dinâmicos) + coletor curado + ZCode podado com backup duplo verificado. Falta = VACUUM com app fechado (Miguel) · automação pesada 03:15 em chat novo · 5 PDFs FT · N9. Preciso do Miguel = rodar o VACUUM quando puder fechar o app + chat novo para a automação pesada.

## Adendo — Coluna Solução + prompt circular (Missão 5, ordem ~19:3x; no ar 19:3x-19:4x)

**Arquivos tocados:**
- `tencent:~/cafezinho/v6/painel_cctv_v6_backup_limpeza.py` (21.536b, v2) — NOVOS: CSS `.blcopy`/`.blcopy:hover`; JS `blFallbackCopy(txt,ok)` (textarea fixed opacity 0 + execCommand) e `blCopiar(btn)` (clipboard API → fallback; feedback "✅ Copiado!" 1,6s); helper `_pontas_faltando(o)` (varre local/b2/drive com bytes None → "local/B2/Drive" ou "nuvem"); `_prompt_solucao(o, ts_fmt)` (f-string multi-linha: título c/ origem+ts da coleta, CONTEXTO c/ origem_local/b2_dst/drive_dst + human/obj por ponta, SITUAÇÃO 🔴/⚪ + diag, cadeia, regras da casa, TAREFAS 1-5 c/ item 4 🔁 CIRCULAR obrigatório, fecho "vai"); tabela de atenção c/ 6ª coluna `<th>Solução</th>` + botão + `<div class="blprompt" style="display:none">` c/ `html.escape(prompt)`; nota muted menciona o prompt circular. Backup da v1 no `.bak` da Tencent; cópia no repo `.tencent_v6_oficina/painel_cctv_v6_backup_limpeza.py`.
- `scratch/coletor_backup_dashboard.py` (Dell) — origens agora gravam `"b2_dst"`/`"drive_dst"` (caminhos reais dos destinos; a página usa no prompt). py_compile OK. 1ª coleta c/ dst = 19:30.
- `~/cerebro-miguel/.tencent_v6_oficina/reforma_v3_status_SEED.json` — P6/P9: instrução 🔁 CIRCULAR inserida antes do " vai" final (script python c/ asserts: endswith("vai"), "CIRCULAR" not in, n==2, json.loads antes/depois; só o campo prompt muda). Commit `2197d261f` + push. Sync: `python3 /home/ubuntu/bin/sync_reforma_status.py` manual (SYNC_OK) + cron */5 (SYNC_REFORMA_BARRA_us65_20260902).

**Testes/provas:** interno `127.0.0.1:8084/backup` 200 — marcadores: `Solução</th>`=1, `blCopiar`=10, `Copiar prompt`=9, `PROMPT DE SOLUÇÃO`=10, `CIRCULAR`=9, `SEM LEITURA de`=10, "5 ⚪ sem leitura de local"; público `http://43.156.151.165/v6/backup` 200 (UA navegador — WAF barra python) c/ 9 linhas de atenção incl. Recordings. Página /reforma interna 200 (54.133b): P6/P9 True p/ CIRCULAR literal; auditoria fraseado: 10/10 prompts mencionam atualizar página/seed/painel (8 já mencionavam antes, sem a palavra CIRCULAR).

**Armadilhas/lições:** (1) rótulo estático mente — "sem dados de nuvem" era falso p/ Recordings (nuvem OK, LOCAL=None): rótulo tem que nascer dos dados (`_pontas_faltando`); (2) `grep -c` conta LINHAS não ocorrências — usar `grep -o | wc -l` p/ contagem de marcador em HTML; (3) clipboard em HTTP puro exige fallback execCommand (navigator.clipboard só em secure context); (4) textContent de div oculta preserva as quebras de linha do prompt — não usar innerHTML; (5) seed da reforma é compartilhada c/ o Chefe — edição ADITIVA só no campo prompt, nunca reescrever o arquivo inteiro sem diff.

**Estado:** aconteceu = coluna Solução + prompts circulares nos 2 painéis + coleta 19:30 CONFIRMADA (aterrissou 19:51:53, duração 1.311s, parciais=3; prompts renderizados com destinos reais — 9× `gdrive-backup-b2:`, 7× `drive:Backup_Total`; página interno/público 200 67.234b mostrando coleta «08/09/2026 19:51» + aviso ⚠️ parcial). Falta = nada. Preciso do Miguel = nada; pendências antigas seguem (VACUUM c/ app fechado, automação pesada 03:15 em chat novo).
