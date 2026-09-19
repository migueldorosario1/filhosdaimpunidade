# Home somente-leitura e /tmp por-comando: quando a jaula muda, o caminho de 1ª classe da ronda muda junto

**Data:** 10/09/2026 (ronda 410ª DS-Dell) · **Família:** infraestrutura do agente — «o caminho que funcionava ontem não é o caminho de hoje».

## O quê
Na abertura da ronda 410ª, os dois endereços onde a ronda trabalha estavam mortos:
- `touch ~/.ds_write_test` → **EROFS** (somente leitura). O clone scratch `~/.ds_ponte_clone_409`, usado na ronda anterior, **não existe mais** — não foi apagado pela casa: o `~` inteiro está read-only para esta física.
- `/tmp` continua **gravável**, mas é **por-comando**: o arquivo `/tmp/ds_med_410.php` criado num comando **desapareceu no comando seguinte**. Cada `bash` recebe um `/tmp` próprio.
- A política corrente da jaula é **workspace-write**: só o workspace da sessão persiste.

## Por quê
O sintoma não parece infraestrutura: parece erro bobo. O medidor rodou `ssh … "wp eval-file -" < /tmp/ds_med_410.php` → `bash: /tmp/ds_med_410.php: Arquivo ou diretório inexistente`; o clone em `~` falhou por EROFS. É a mesma família que a casa passou o dia medindo — **o passo que responde com sucesso é o passo, não a obra** (182/184/187/190/191/198/200/201/203/204/205) — agora aplicada à **física onde a ronda roda**, não ao dado que ela mede.

## Como aplicar (régua)
1. **Primeiro ato da ronda: testar a física, não assumi-la** — `test -w ~ && echo ok || echo EROFS` + `hostname`. Custa um segundo e evita duas falhas.
2. **Temp e consumo no MESMO comando**: criar, usar e remover na mesma chamada (`cat > f <<'PH' … PH; ssh … < f`). Medição multi-passo **não pode depender de /tmp**.
3. **Clone da ronda mora no workspace** (único persistente): `…/Antigravity Google/.ds_ponte_410`, com `origin` no GitHub (`git@github.com:migueldorosario1/cerebro-miguel.git`), porque o canônico local é read-only (BUG-194). Sempre `fetch` + `rebase origin/main` antes do push.
4. **Escrita é append**: o canônico segue fonte de verdade da leitura; o clone é o braço de escrita.

## Nota
Registrado como **observação de infraestrutura**, não como bug de produção — nada no site depende disso. Mas é a **2ª vez em 2 dias** que o caminho de 1ª classe da ronda muda de física sem aviso: na 409ª o canônico já era EROFS (BUG-194); na 410ª o `~` e o `/tmp` caíram junto. Quem tiver rito salvo em caminho fixo falha no mesmo ponto.
