# 🗂️ CEREBRO_NODE_INDICE_LOCAL — Buscador de arquivos do Dell + Ledger de retiradas (Camada 2)

> Criado em 08/09/2026 (missão Faxina Total do Dell, ordem do Miguel: "cria um buscador... através de um index no próprio Cérebro, pelos metadados dos arquivos"). Nodo catalogado no `CEREBRO_INDEX_MASTER.md`; linha do tempo em `CEREBRO_NODE_ATUALIZACOES.md`.

## O que é

Índice SQLite de TODOS os arquivos/diretórios do Dell (metadados: caminho, nome, extensão, tamanho, mtime, rollup por pasta), com poda de lixo regenerável, + CLI de busca + ledger auditável de tudo que foi retirado do computador para a nuvem.

## Ferramentas (Camada 3 — scripts vivos)

| Recurso | Caminho | Uso |
|---|---|---|
| Indexador | `Cerebro/Ferramentas/buscador_local/indice_local.py` | `python3 indice_local.py [--budget 900]` — rebuild completo (~minutos); roda sozinho nas automações de faxina |
| Buscador | `Cerebro/Ferramentas/buscador_local/buscador.py` | `--nome X`, `--ext pdf --min 50M --antes 2026-07-01`, `--pesados 30`, `--pastas 30`, `--velhos 90 --min 100M`, `--dir --nome jornais`, `--duplicatas --min 50M`, `--resumo` |
| Índice (DB) | `~/.local/share/buscador_local/indice.sqlite` | read-only pelas buscas; FORA do Cérebro de propósito (binário não vai pro sync horário B2/GitHub) |
| **Ledger de retiradas** | `Cerebro/Ferramentas/buscador_local/LEDGER_APAGADOS.md` | **LEIA ANTES de apagar/retirar QUALQUER coisa do Dell** — registro de o que saiu, tamanho, prova de backup, onde está na nuvem; fila noturna N1-N12 vive nele |
| Sweep jornais | `AG/Outros/Jornais do dia/sweep_jornais_verificados.py` | chamado pelo cron `jornaisdodia.sh` (10:30/13:00/18:00) — apaga PDF >3d só com cópia idêntica verificada no GDrive |
| **Gerador da seed /v6/faxina + ÍNDICE DUPLO** | `Cerebro/Ferramentas/buscador_local/gera_seed_faxina.py` | `python3 gera_seed_faxina.py --push [--sem-nuvem]` — df + fila do LEDGER + índice SQLite + curadoria → seed no repo (commit seletivo + prova no origin) + **espelho diário do DB → GDrive+B2 (`espelhar_indice()`, verificação lsf)** + **CATALOGO_NUVEM.md** (commitado junto); roda nas automações (leve passo 7 / pesada passo 8) + **`resolver_faxinas()`** (botões numerados da página: última execução via marcadores/cabeçalho do de_dell, data DD/MM/AAAA) |
| **Catálogo da nuvem** | `Cerebro/Ferramentas/buscador_local/CATALOGO_NUVEM.md` | índice LEGÍVEL do que a faxina guarda nas nuvens (listagens rclone B2/GDrive + Jornais do dia) — regenerado toda passada da leve; no repo = triplicado (D9) |
| Purga ZCode >14d | `Cerebro/Ferramentas/buscador_local/purga_zcode_antigos.sh` | tar+gpg de `~/.zcode/cli/{artifacts,exec}` >14d → GDrive+B2 → **readback sha256 ×2 → só então poda** (fail-closed); passphrase alias `ZM_ZCODE_ANTIGOS_PASSPHRASE` nos cofres; passo 4 da leve 4/4h |
| Rotação de canais | `Cerebro/Ferramentas/buscador_local/rotaciona_canais.sh` | rito QUÁDRUPLO (arquivo datado local + GitHub + GDrive + B2 + aviso nos vivos/inboxes) p/ canais da ponte >8-10M — template: atualizar ref ZM/tamanhos a cada uso; janela entre rondas (§112) |
| Curadoria do mapa | `Cerebro/Ferramentas/buscador_local/faxina_mapa_curadoria.json` | status/obs/GB das linhas do mapa + overrides de GB por lote — **atualizar a cada lote executado/movido** |
| **Página «💾 Backup e Limpeza» (única, 2 abas)** | http://43.156.151.165/v6/backup (= /v6/faxina) | aba Backup DINÂMICA (última coleta c/ data cheia DD/MM/AAAA, cobertura B2/Drive, histórico AGRUPADO POR DIA, «precisam de atenção» só vermelhas — sem tabelão de diretórios) + aba Limpeza (BOTÕES NUMERADOS Faxina 1-6 c/ data via marcadores + barra % da missão + mapa dos diretórios que ficaram) — Tencent: módulo `painel_cctv_v6_backup_limpeza.py` (abas) + `painel_cctv_v6_faxina.py` (corpo barra/mapa) + sync `*/7` SYNC_FAXINA_ZM_20260908; cópias do código no repo `.tencent_v6_oficina/` |

## Documentos do tema (Camada 3)

- **Fórum:** `Foruns/forum_faxina_dell_buscador_20260908.md` — decisões D1-D10, estrutura-alvo de diretórios (D5), índice duplo (D9), GDrive primário (D10), fila noturna, estado da missão.
- **Memória:** `Memorias/memoria_faxina_dell_buscador_20260908.md` — log técnico, provas, armadilhas.
- **Antecessora:** faxina ZCode 06/09 (`forum/memoria_faxina_zcode_dell_20260906` + `MANIFESTO_ZM_BACKUP_ZCODE_20260906.md`) — VACUUM confirmado FEITO pelo Miguel em 06/09 22:24.

## Automações ativas

- 🧹 **Faxina LEVE 4/4h** (:40) — clones DS-Dell velhos (limpos+pushed), sweep jornais, caches regeneráveis, `.bak_fallback_*` ZCode >7d, **ZCode >14d → nuvem dupla via `purga_zcode_antigos.sh` (passo 4, readback ×2 antes de podar)**, atualização do índice, ledger; **passo 7: gera a seed da página /v6/faxina, ESPELHA o índice 1×/dia p/ GDrive+B2 (D9 índice duplo), regenera o CATALOGO_NUVEM.md e pusha tudo (toda passada — é o ritmo da barra/série)**. Silenciosa quando não há o que retirar.
- 🌙 **Faxina PESADA 03:15** — UM lote da fila N por noite; rito: monitor (§112) → backup B2+GDrive (gpg p/ sensível; mídia não-sensível pode ir crua) → verificação (readback/rclone check) → retirada → APONTADOR.md → LEDGER → **passo 8: atualizar curadoria do mapa + gerador da página** → 1 Telegram 🟢 de manhã. Fail-closed: sem verificação, não retira. (Prompt arquivado: `Foruns/sessoes_zcode/PROMPT_AUTOMACAO_FAXINA_PESADA_20260908.md` — criação em chat novo, pendência do Miguel.)
- 📊 **Página /v6/faxina** (painel CCTV v6, ideia do Miguel 08/09 ~16:1x) — cadeia: `gera_seed_faxina.py --push` (Dell) → seed `.tencent_v6_oficina/faxina_dell_status_SEED.json` (repo) → cron `*/7` `sync_faxina_status.py` (Tencent, tag SYNC_FAXINA_ZM_20260908) → `v6_data/faxina_dell_status.json` → página única «💾 Backup e Limpeza» (08/09 19:1x): `painel_cctv_v6_backup_limpeza.py` (2 abas; corpo da faxina vem do `painel_cctv_v6_faxina.py`, STALE 13h; padrão us65 da /v6/reforma) — a chave `faxinas` da seed alimenta os botões numerados (`resolver_faxinas()` no gerador, datas DD/MM/AAAA de marcadores reais).

## Regras permanentes do tema

1. **Nunca apagar nada do Dell sem backup verificado** (B2 e/ou GDrive/GitHub/fonte pública) + registro no LEDGER.
2. **Diretórios de trabalho são intocados** (lista D3 no fórum) e **pastas vivas NÃO se movem** (crons referenciam caminhos absolutos).
3. Pasta esvaziada ganha **APONTADOR.md** (para onde foi, como buscar).
4. Antes de mover qualquer item do topo do AG (209 itens → consolidação N11): grep crontab/systemd/scripts por referências.
5. Clones `.ds_ponte_clone_*`: sweeper guarda sempre os 2 últimos + só apaga com `status` limpo + 0 commits local-only + 0 stash; resto = quarentena.
