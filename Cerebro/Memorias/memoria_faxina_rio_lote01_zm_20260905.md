# Memória — Faxina Rio lote01: execução ZM com gates (05/09/2026)

> Log técnico completo. Decisões resumidas no fórum-irmão: `Foruns/forum_faxina_rio_lote01_zm_20260905.md`.
> ZM (ZCode/GLM-5.3) · ordem do Miguel ~20h de 05/09 · bandeira recebida do Astra (GPT-6), tutor DS-N Chefe.

## 1. Contexto e fontes

- Parecer do tutor (DS-N Chefe) 05/09 09:06 em `Foruns/ponte_laura_completa/telegram_dsc/RESPOSTAS.md`: APROVA retirada dos 17 CONDICIONADA a (a) ZM provar restauração de permissões+conteúdo em cópia isolada antes do corte; (b) acesso durável ao inventário+complemento; (c) não ampliar lista (26 excluídos + system.journal ativo preservados).
- Plano Astra: `Memorias/PLANO_ASTRA_RETIRADA_REVISAO_DSN_ZM_20260905.md` (A01–A17; §5 faltas explícitas; §6 plano de recuperação; §7 critérios de parada).
- Manifesto/backup: `Memorias/MANIFESTO_ASTRA_BACKUP_RIO_20260905.md` (lote01 validado 07:54 BRT; B2 `b2:failover-cafezinho1/faxina/rio-ag/journals/2026-09/astra_20260905_lote01/`).
- Override canônico da faxina (11/08): indexar → backup B2 → verificar → autorização explícita → retirar.

## 2. Gates fechados (provas)

### Gate A — acesso durável às provas
- Inventário local sha256 `de44ac2af0c1f55c15c1bebc196946b67140db674a82a03687718adf8f3d8520` = manifesto ✓
- Complemento local sha256 `f400b74fad8be24b47c5b7ee1e5530a5ba3668c04bece72031e9cf7e55cdac23` = hash final do AST-013 ✓
- GitHub origin/main: inventário + complemento + plano presentes (commits abbe37011 / ecd19767) ✓
- Área privada do Astra preservada no Dell: `Downloads/Antigravity Google/astra_operacoes/state/rio_20260905_hdjufh8i/` (tar 452997120 bytes, gpg, readback, restore) ✓; script sha256 `dd07772bb7fc993e65c1c3c93140f7b392e5002c29a011e2f7f88a3f8eda0495` ✓
- Passphrase do lote presente nos 3 cofres (alias `ASTRA_RIO_JOURNALS_20260905_PASSPHRASE`); valor nunca exibido.

### Gate B — backup B2 reconferido de ambiente independente (Tencent)
- `rclone copy b2:failover-cafezinho1/faxina/rio-ag/journals/2026-09/astra_20260905_lote01/` na Tencent:
  - journals.tar.gpg 94.203.743 bytes sha256 `1d47eb21b0fdc4b8c8f007ac2d777f1f2e929cd9c7c6695afec689d69144e71e` ✓
  - manifest.json `0024e6f4…` ✓ · README.txt `923701f1…` ✓
- Decifração GPG AES256 com passphrase via stdin do ssh (não exposta): tar 452.997.120 bytes sha256 `c2bfce6c75aeb0f5653add1cfa45cf839a874bedd23a86c2e53d811ad52f0e94` ✓

### Gate C — ensaio de restauração em cópia isolada (Tencent, /root/zm_ensaio_rio_20260905/)
Script `zm_ensaio_script.py` (ordem do plano §6.6: conteúdo → dono/grupo/modo → ACL/xattrs → conferir permissões efetivas → tempos ns):
- 17/17 conteúdo SHA256 = inventário ✓
- 17/17 chown 0:999 + modo final 0640 (permissão efetiva conferida pós-ACL) ✓
- 17/17 ACL `system.posix_acl_access` aplicada via `os.setxattr` (bytes base64 do complemento) e re-lida com sha256 idêntico ✓ (método escolhido de propósito: Python puro funciona no Rio, que NÃO tem getfacl/setfacl instalados)
- 17/17 `user.crtime_usec` idêntico ✓
- 17/17 mtime_ns e atime_ns exatos via `os.utime(ns=…)` ✓
- Legibilidade: `journalctl --file=… -n 2 -o json` exit 0, entradas lidas, JSON válido — 3 amostras (primeiro/meio/último) ✓
- Relatório: `Memorias/zm_relatorio_ensaio_rio.json`. Área de ensaio apagada ao final (só relatório+scripts ficaram).

## 3. Revalidação ao vivo (20:10) — ACHADO

- 12 dos 17 (A01–A12, 23/07–10/08) **MISSING**: removidos pelo próprio systemd-journald entre a revalidação do Astra (08:26) e as 20:10 — vacuum com disco 96% e KeepFree violado (defaults, sem overrides no journald.conf). Sem perda (backup lote01 cobre os 17).
- 5 remanescentes (A13–A17): 50.331.648 bytes cada, uid 0 / gid 999 / mode 0640 / nlink 1, **SHA256 5/5 idênticos ao inventário**, `fuser` vazio.
- 26 excluídos: 26 presentes ✓ · `system.journal` ativo presente ✓ · base com 43 arquivos.
- journald active; caddy :80 → 200; cicero_admin :5000 → 302.

## 4. Execução da retirada (20:20)

- Script `/tmp/zm_rm_5.sh`: revalida SHA256+abertura de cada um dos 5 ANTES (FAIL=1 aborta) → `rm -f --` caminhos literais gerados do inventário (sem glob) → medição pós.
- Resultado: REVAL_OK → PRE df 23.081.092 KB usados / 1.202.492 KB livres (96%) → POS 22.855.600 / 1.427.984 (95%) → **225.492 KB liberados (~215 MiB)**; base 43→38; ativo+26 intactos; caddy 200 / cicero 302; journald active (uso 1.4G).

## 5. Mapa estrutural do Rio (du -x, hoje)

- `/root` 10,7G: riocarta_remote 3,9G + cicero_remote 3,6G + gsn_remote 1,7G (git packs com imagens) + agentes 0,7G + .npm 0,2G
- `/var/log/journal` 1,77G (voraz; 1,4G após limpeza); /var 3,1G; /usr 2,9G
- Recomendações (aguardam "vai"): lote02 backup dos 26 (URGENTE — o journald vai comê-los), journald.conf SystemMaxUse=400M+MaxFileSec=30d, git gc nos 3 repos, purge .npm.

## 6. Medições dos demais servidores (20h, vigia central :42 + SSH)

- Rio 95% (pós) · NYC-failover 70% · Tencent 68% (moka na Tencent: 64M) · ServerDo Cafezinho 42% · Espelho 29% (/var/www 13G) · Central alertas 41%. Detalhes e plano por servidor no fórum §5.

## 7. Lições/armadilhas (para a próxima faxina)

- **journald em disco cheio é consumidor E concorrente da faxina**: 12 candidatos sumiram sozinhos entre a indexação e a execução. Em qualquer servidor 🟠, o lote de journals precisa de backup ANTES de qualquer deliberação — o sistema não espera.
- O Rio não tem getfacl/setfacl/getfattr: restauração de ACL/xattr por lá = Python puro (`os.setxattr` com bytes base64 do complemento) — método validado no ensaio.
- Tar USTAR traz uid/gid/mode mas NÃO ACL/xattrs/ns — o complemento do Astra é obrigatório na recuperação (e fica só no Cérebro/GitHub, não no B2).
- Comparador de hashes: sha256sum imprime "hash caminho" e meu arquivo esperado era "caminho hash" — falso 0/5; sempre normalizar a ordem antes de concluir divergência (critério de parada merece prova real).
- df --output=used,avail em KB: o ganho real (225.492 KB) < nominal alocado (240 MiB) — df é a régua do resultado, o nominal é estimativa.
- Custo real da operação: egress B2 ~94MB ≈ US$0,01 (registrado; sem outras despesas).

## 8. Rollback / como recuperar os arquivos removidos

1. Baixar `b2:failover-cafezinho1/faxina/rio-ag/journals/2026-09/astra_20260905_lote01/journals.tar.gpg` (sha256 1d47eb21…).
2. Decifrar com a passphrase do alias `ASTRA_RIO_JOURNALS_20260905_PASSPHRASE` (cofres) → tar sha256 c2bfce6c….
3. Extrair em diretório novo; conferir 17 membros contra `Memorias/INVENTARIO_ASTRA_BACKUP_RIO_20260905.json`.
4. Aplicar metadados de `Memorias/COMPLEMENTO_ASTRA_METADADOS_JOURNALS_RIO_20260905.json` na ordem: chown 0:999 → chmod 0640 → setxattr dos 2 xattrs → tempos ns (script pronto: `/root/zm_ensaio_rio_20260905/zm_ensaio_script.py` na Tencent; receita Python pura roda em qualquer host).
5. Só devolver ao caminho original se autorizado no fluxo DS-N→ZM (plano Astra §6.8).

## ADENDO — Fase 2 da noite (21:1x): lote02 + teto journald + gc/npm — 96% → 88%

- Ordem do Miguel: hoje SÓ Rio; Cafezinho canônico vetado; Tencent condicionada a análise de segurança profunda prévia.
- Lote02: inventário no próprio Rio via Python puro (/tmp/zm_lote02_inventario.py — dupla leitura SHA256, xattrs base64, /proc p/ abertos): 36 membros/1.520 MB, 1 aberto pulado, ativo fora. Transferência tar-stream ssh (-T lista) → 36/36 íntegros no Dell. Tar USTAR --owner=0 --group=999 --mode=0640 com inventário+manifesto DENTRO (1.593.907.200 B, sha 0cb56c41…) → GPG AES256/ZLIB (407.591.584 B, sha 48fb5422…; passphrase nova alias ZM_RIO_JOURNALS_LOTE02_20260905_PASSPHRASE nos 3 cofres c/ .bak_pre_lote02_20260905, hash 3/3) → B2 zm_20260905_lote02 → readback Tencent: gpg/tar shas ✓, 38 membros, 36/36, journalctl ✓.
- Armadilha gpg: no PATH do sudo na Tencent o gpg rejeitou --pinentry-mode (versão 1.x); --batch --passphrase-fd 0 sem a opção resolveu.
- journald: drop-in /etc/systemd/journald.d/90-faxina-zm.conf (400M/30d) + restart + vacuum-size=400M → 1,1 G liberados, base 38→16, serviços OK.
- git gc: repos reais em /root/*_remote/<nome>/.git (não na raiz!) — riocarta 2402→2402, cicero 2325→2299, gsn 1365→1365 MB: packs já compactados; causa = imagens versionadas (≈6,1 G) → recomendação LFS/mídia fora do git, decisão do Miguel. .npm/_npx 202→1 MB.
- Números da noite: 96%→88% (1,20 GB→2,9 GB livres) = lote01 220 KB-mil (225.492 KB) + vacuum 1,1 G + npm 201 MB + gc 26 MB.
