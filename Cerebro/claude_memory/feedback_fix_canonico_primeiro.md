---
name: Fix sempre no canônico local PRIMEIRO, depois propaga com MD5 check
description: Fix aplicado só no servidor (Tencent) é efêmero — qualquer sync/deploy reverso sobrescreve. Sempre editar `Projeto Cafezinho Agentes/root/` primeiro.
type: feedback
originSessionId: d12bd15a-b1a1-490f-b582-882687c3c015
---
**Toda mudança de código de produção deve ser aplicada PRIMEIRO no canônico local (`Projeto Cafezinho Agentes/root/`), depois propagada ao servidor, com MD5 check antes e depois.**

**Why:** Em 2026-04-22, o bug `UnboundLocalError: html` do Repetidor **reapareceu** — tinha sido corrigido em 21/04 10:23 DIRETO NO SERVIDOR, mas a cópia local ficou com bug. Entre 21/04 e 22/04, algum sync/deploy de cima pra baixo sobrescreveu o fix. O código ficou quebrado 66 vezes no dia seguinte até detectarmos. Manual de bugs tinha o bug documentado mas o fix tinha ressuscitado.

**How to apply:**
- Antes de editar: `md5sum` local vs servidor. Se divergir sem motivo conhecido, PARAR e investigar (alguém editou paralelamente).
- Aplicar Edit no arquivo local em `Projeto Cafezinho Agentes/root/`.
- `scp` pra `/tmp/` no Tencent (não direto pra `/root/` — ownership quebra).
- `md5sum` local == MD5 de `/tmp/` no servidor antes de mover.
- Backup pré-fix (`sudo cp file file.bak_pre_<motivo>_<stamp>`) + `sudo mv` + `chown root:root` + `chmod`.
- MD5 final do arquivo em `/root/` bate com local.
- **NUNCA** rodar `sed -i` direto no servidor sem sincronizar com local.
- **NUNCA** aplicar fix via `ssh ... 'cat > file'` — viola §3 do CLAUDE.md e cria drift.

**Auditoria recomendada:** cron diário comparando `md5sum` dos .py principais local vs servidor; alertar se divergir sem deploy correspondente. Sem isso, fixes ressuscitam silenciosamente.
