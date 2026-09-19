# Memória — Rotina de organização do Antigravity Google — ZM-20260910-002

10/09/2026 ~11:2x-12:0x BRT · ZCode/GLM 5.3 × ASTRA (gpt-6-astra direto via codex exec, sandbox read-only, cwd AG, 11:3x→11:5x rc=0 16.329b).

## Executado nesta rodada (SÓ isto moveu/apagou)

- 6 vazios removidos no AG (ordem direta do Miguel, com checagem 0 consumidores): dirs Google/.ds_r286 e Google/ (vazia após), 4 arq .ds_tmp/{serie_completa,notas_final,notas_mem2,notas_ponte2}.txt. Manifesto: /tmp/vazios_removidos_20260910_*.tsv + ~/.local/share/buscador_local/.reorg_vazios_*.tsv. LEDGER Lote 9. 33 vazios MANTIDOS com motivo (locks, ledgers de robôs, .git/branches, node_modules/.astro, intocáveis, ronda_385 com pendente de HOJE).

## Dados-chave (ZM + Astra confirmou/varreu)

- AG top-level: 298 itens (86 dirs + 211 arquivos + 1 symlink), ~62 GiB.
- 24/53 crons vivos do Dell apontam pro AG (Astra não ratificou a contagem exata — dele confirmados: jornais 3×/dia, sync 5min, ronda DSH 30min, ronda ASTRA, MOKA, loops Cérebro).
- 🔴 .git raiz 28G NÃO dormente: reflog até 07/09 06:35 (reset origin/main), HEAD dc23697c de 05/09 ("Refatoração V4"), deploy-main rastreia Cérebro. ZM errou com mtime de .git/HEAD — SEMPRE reflog > mtime. Auditoria de 7 pontos exigida antes de qualquer arquivamento.
- Candidatos nuvem-first numerados 1-11 no parecer (só o .git 28G supera 500MiB sem "aguardar idade": novo livro 2,5G, mapa rio videos 2,2G, Aplicativos 1,8G...).
- Caminho do repo vivo do filhos hoje: ~/ZCodeProject/filhosdaimpunidade (projetos/ é árvore-ALVO da Fase 3, ainda não criada — Astra flagou a divergência do prompt).

## Rotina formulada (ver fórum p/ detalhe)

10 guarda-chuvas + exceções explícitas; D3/crons não movem (subdiretórios internos para novas saídas); cadência 4/4h leve (≤50 itens/1GiB, fail-closed, sem mensagem se nada) + diária (produtor de entrada indevida) + semanal (lotes) + mensal (restauração ×2); nuvem-first 6 critérios + rito readback integral ×2; fases 1 reconciliar→2 reduzir raiz→3 offload→4 sustentar; regra de entrada: missão nova = dono+destino+prazo ANTES de gerar arquivo.

## O que aconteceu / o que falta / o que preciso do Miguel

- Aconteceu: rotina formulada em dupla, vazios seguros removidos, tudo registrado (fórum+memória+parecer+LEDGER).
- Falta: "vai" p/ Fase 1 AG (reconciliar+congelar); auditoria .git (7 pontos); Fase 3 ZCodeProject ainda pendente do "vai" anterior.
- Preciso do Miguel: aprovar Fase 1 AG (e se quer auditoria do .git já na Fase 1).
