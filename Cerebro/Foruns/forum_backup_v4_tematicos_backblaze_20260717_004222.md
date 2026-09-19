# Fórum — Backup V4 + Temáticos no Backblaze — 2026-07-17 01:02 BRT

**Data:** 2026-07-17 01:02 BRT  
**Responsável:** Codex (continuação da execução de background)  
**Alvo:** Backup rastreável e indexado dos ativos V4 + sites temáticos  
**Status:** Concluído com validação

---

## 1) Objetivo

Gerar backup do conjunto canônico de V4 (operacional) e dos sites temáticos em pacote único por domínio no Backblaze B2, com trilha rastreável de origem→destino, hashes, tamanhos, lista de arquivos e validação `rclone check`.

---

## 2) Destino remoto

- Remote: `b2:failover-cafezinho1`
- Path: `backups/v4_tematicos/20260717_004222`

---

## 3) Snapshot local criado

- **Diretório:** `/home/migueldorosario/Downloads/Antigravity Google/Backups/backblaze_v4_tematics_20260717_004222`
- **Artefatos de controle:**
  - `manifesto.md`
  - `indice_origem_para_destino.tsv`
  - `pack_inventory_counts.tsv`
  - `pack_sizes_human.txt`
  - `pack_temat_create.log`
  - `pack_v4_create.log`
  - `rclone_copy.log`
  - `rclone_check.log`
  - `remote_ls_after_copy.txt`
  - `remote_ls_after_check.txt`
  - `selected_inputs.tsv`
  - `SHA256SUMS_PACKS.txt`

---

## 4) Conteúdo empacotado

- `packs/v4_payload_20260717_004222.tar.gz`
- `packs/tematicos_payload_20260717_004222.tar.gz`

Tamanhos:

- `24M` para `packs/v4_payload_20260717_004222.tar.gz`
- `508M` para `packs/tematicos_payload_20260717_004222.tar.gz`

---

## 5) Índice rastreável origem → destino

| Categoria | Origem local | Destino remoto |
|---|---|---|
| V4 | `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/v4` | `b2:failover-cafezinho1/backups/v4_tematicos/20260717_004222/packs/v4_payload_20260717_004222.tar.gz` |
| V4 | `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/v4_labs` | `b2:failover-cafezinho1/backups/v4_tematicos/20260717_004222/packs/v4_payload_20260717_004222.tar.gz` |
| Temático | `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/sites-tematicos/cafezinho` | `b2:failover-cafezinho1/backups/v4_tematicos/20260717_004222/packs/tematicos_payload_20260717_004222.tar.gz` |
| Temático | `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/sites-tematicos/cafezinhomediagroup` | `b2:failover-cafezinho1/backups/v4_tematicos/20260717_004222/packs/tematicos_payload_20260717_004222.tar.gz` |
| Temático | `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/sites-tematicos/ceara-digital` | `b2:failover-cafezinho1/backups/v4_tematicos/20260717_004222/packs/tematicos_payload_20260717_004222.tar.gz` |
| Temático | `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/sites-tematicos/discover_brazil` | `b2:failover-cafezinho1/backups/v4_tematicos/20260717_004222/packs/tematicos_payload_20260717_004222.tar.gz` |
| Temático | `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/sites-tematicos/discover_brazil_news` | `b2:failover-cafezinho1/backups/v4_tematicos/20260717_004222/packs/tematicos_payload_20260717_004222.tar.gz` |
| Temático | `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/sites-tematicos/global_south_news` | `b2:failover-cafezinho1/backups/v4_tematicos/20260717_004222/packs/tematicos_payload_20260717_004222.tar.gz` |
| Temático | `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/sites-tematicos/mapa_rio` | `b2:failover-cafezinho1/backups/v4_tematicos/20260717_004222/packs/tematicos_payload_20260717_004222.tar.gz` |
| Temático | `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/sites-tematicos/mundo_trilhos` | `b2:failover-cafezinho1/backups/v4_tematicos/20260717_004222/packs/tematicos_payload_20260717_004222.tar.gz` |
| Temático | `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/sites-tematicos/rail_post` | `b2:failover-cafezinho1/backups/v4_tematicos/20260717_004222/packs/tematicos_payload_20260717_004222.tar.gz` |
| Temático | `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/sites-tematicos/rio_carta` | `b2:failover-cafezinho1/backups/v4_tematicos/20260717_004222/packs/tematicos_payload_20260717_004222.tar.gz` |

---

## 6) Exclusões aplicadas nos temáticos

- `node_modules`
- `.git`
- `dist`
- `.astro/cache`
- `.next`
- `.turbo`
- `.svelte-kit`
- `.vercel`
- `.vscode`
- `.env` e `.env.local`
- `.cache`

---

## 7) Hashes (SHA-256)

- `v4_payload_20260717_004222.tar.gz`: `776e1816bf73bc7450d48154dd8e430c4bfa51fd5d0f84c0aa48ae5f690a01ca`
- `tematicos_payload_20260717_004222.tar.gz`: `956a0c24190afbc4d85f2ea90dac5b937fd640b9d35be4a6af82300cd434fd0c`

---

## 8) Verificação

Comandos executados:

```bash
cd "/home/migueldorosario/Downloads/Antigravity Google/Backups/backblaze_v4_tematics_20260717_004222"
rclone check . b2:failover-cafezinho1/backups/v4_tematicos/20260717_004222 --one-way --size-only
```

Resultado final:

- `0 differences found`
- `16 matching files`

---

## 9) Estado final e próximos passos

- Snapshot remoto está íntegro para o escopo definido.
- Arquivos principais para restauração e validação rápida:
  - `b2:failover-cafezinho1/backups/v4_tematicos/20260717_004222/packs/v4_payload_20260717_004222.tar.gz`
  - `b2:failover-cafezinho1/backups/v4_tematicos/20260717_004222/packs/tematicos_payload_20260717_004222.tar.gz`

Observação: houve duas rodadas de `rclone copy` durante a execução por causa de arquivos de log gerados após o primeiro upload; a checagem final já contempla o estado final.
