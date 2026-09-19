# 📜 MANIFESTO DA ESTANTE PRINCIPAL

> **Data:** 2026-07-22 · **Autor:** Kimi k3 (CEO do Cérebro), a pedido de Miguel do Rosário
> **Status:** ⛔ SOMENTE MANIFESTO — **nenhum arquivo foi movido, renomeado ou deletado**
> **Precedentes:** Reforma de arquivos de 22/07 (WS 153G → 30G) já executada e indexada em `CEREBRO_INDEX_REFORMA_ARQUIVOS_20260722.md`. Este manifesto é a **Fase 2**: o emagrecimento fino do que sobrou.

---

## 1. A Visão

O Antigravity (e qualquer IDE/agente) fica leve quando a pasta que ele vigia é leve. Portanto:

> **O workspace `Antigravity Google` passa a ser SÓ produção viva.**
> Tudo que é memória, acervo, backup, cache ou resto de laboratório vai para a **Estante Principal** (atual pasta `~/Dados_Frios/`, que o Miguel renomeará).

A Estante Principal não é lixo nem limbo: é a **biblioteca do ecossistema** — tudo indexado, encontrável, e espelhado no Google Drive conforme a fila já em curso (7 madrugadas, cron 03:00).

## 2. As Três Leis da Limpeza

1. **Produção é intocável.** Nada que um crontab, agente, script ou config referencie sai do lugar. Caminho referenciado = caminho sagrado.
2. **Nada se deleta sem dupla morada.** Item candidato a lixo só é deletado se for (a) regenerável (cache, node_modules, venv) ou (b) já espelhado na Estante/Drive.
3. **Tudo catalogado.** Toda mudança futura entra no índice da reforma + Fórum/Memória (Regra do Tema Duplo).

## 3. Estado Atual do Workspace (medido em 22/07, ~22h)

**Total: 30 GB** — mas só ~6 GB são produção real. O resto é peso morto:

| Bloco | Peso | Natureza |
|---|---:|---|
| `.git_gordo_20260620/` | **18 GB** | ⚰️ Git histórico arquivado em junho — **60% do workspace é um fantasma** |
| `Projeto Cafezinho Agentes/` | 4,9 GB | 🔴 Produção (crons youtube_cafezinho 6/12/18/23h) |
| `.git/` | 2,5 GB | 🔴 Histórico vivo do workspace |
| `Outros/` | 1,8 GB | Misto: produção (jornais, Moka) + restos |
| `Cicero Agentes/` | 965 MB | 🔴 Produção (cron 10h, devolvido na reforma) |
| `aiatolah/` | 258 MB | 🟡 Crons desativados (V4 assumiu) — decidir |
| `Rio Carta Agentes/` | 233 MB | 🟡 Resto leve pós-reforma |
| `Global South News/` | 227 MB | 🟡 Resto leve pós-reforma |
| Demais pastas e arquivos | ~350 MB | Misto: Cérebro, scripts de cron, caches, temps |

---

## 4. Análise Item por Item

### 🔴 FICA — Produção viva (não tocar)

| Item | Peso | Por que fica |
|---|---:|---|
| `Cerebro/` | 35 MB | Memória canônica; AGENTS.md aponta para este caminho |
| `Projeto Cafezinho Agentes/` | 4,9 GB | Crons ativos (`youtube_cafezinho.py` 4×/dia; sites-tematicos com crons 9h15–9h45) |
| `agentes_tematicos/v4/` | 1,3 MB | Coração da produção: `orquestrador.py` com 6 crons ativos |
| `agent_data/` | 3,4 MB | Bancos SQLite vivos + alvo dos logs dos crons |
| `Outros/Jornais do dia/jornaisdodia.sh` | — | Cron 10h30 e 12h00 ⚠️ caminho sagrado |
| `Outros/Aplicativos/` (Moka + MokaVideo) | — | Projetos ativos — Miguel mandou manter |
| `scratch/backup_reforma_local.sh`, `limpa_diario.sh`, `enviar_baleia_azul_v2.sh` | — | 3 scripts com 5 crons ativos ⚠️ a pasta `scratch/` fica por causa deles |
| `Cicero Agentes/` | 965 MB | Cron de produção 10h (devolvido na reforma de hoje) |
| `.git/` | 2,5 GB | Histórico vivo; saneamento é tema da Fase 3, não desta |
| `acorde.sh`, `.env`, `README.md`, scripts `claude-*.sh` | ~15 KB | Rotinas de despertar dos agentes |
| `.agents/`, `.claude/`, `.codex/`, `.kimi/`, `.qwen/`, `.deepseek/`, `.antigravitycli/`, `.vscode/` | ~1 MB | Configs vivas dos CLIs |
| `backups_ceo_cerebro/` | 71 MB | Rede de segurança do Cérebro — pequena e estratégica |
| `Cafezinho Espelho No-Index/` | 8 KB | Ativo editorial |

**Subtotal que fica: ~9,6 GB** (dos quais 2,5 GB são o `.git` vivo).

### 🟡 MOVE — Candidatos à Estante Principal

| Item | Peso | Justificativa | Destino proposto na Estante |
|---|---:|---|---|
| `.git_gordo_20260620/` | **18 GB** | Git arquivado em 20/06; já é "morto" por definição. Único item que muda o jogo | `Estante/git_gordo_20260620/` |
| `aiatolah/` | 258 MB | Crons V4-desativados em 20/07; portal já migrado pro orquestrador. ⚠️ **precisa de OK do Miguel** (ecossistema ativo?) | `Estante/aiatolah/` |
| `Rio Carta Agentes/` (resto) | 233 MB | Pesado já saiu na reforma; resto são coadjuvantes. ⚠️ confirmar que nada referencia | `Estante/Rio Carta Agentes/` |
| `Global South News/` (resto) | 227 MB | Idem; cron local comentado. `server doin/` interno está **vazio** | `Estante/Global South News/` |
| `artifacts/` | 47 MB | Artefatos de sessões passadas | `Estante/artifacts/` |
| `banco_midia/` | 50 MB | ⚠️ verificar se algum site puxa mídia daqui antes | `Estante/banco_midia/` |
| `github_work/` | 1,4 MB | Área de trabalho pontual | `Estante/github_work/` |
| `tmp_v3_docs/`, `tmp_v3_remote/` | 1,1 MB | Temporários do V3, sucedido pelo V4 | `Estante/tmp_v3/` |
| `comunicacao_externa/`, `brain/`, `memory/`, `v4_memoria/`, `v4_telemetry/`, `passo2e_taxonomia_seo/`, `AGY/` | ~330 KB | Micropastas de fases antigas | `Estante/micropastas_historicas/` |
| `reportagens_casa_da_moeda.md` | 132 KB | Documento de acervo | `Estante/Outros_docs/` |
| Zips soltos na raiz (`agentes_tematicos.zip`, `files_claude_autocura_*.zip`, `imagens_autocura_*.zip`, `Para_mostrar_ao_Claude_*.zip`) | ~12 MB | Pacotes já extraídos/enviados | `Estante/zips_raiz/` |
| `Outros/` (o que não for produção — ~90 subpastas de acervo, fotos, finanças, pesquisas) | ~1,7 GB | Acervo pessoal e editorial frio | `Estante/Outros/` (fundindo com o que já lá está) |

**Subtotal que move: ~20,4 GB** (18 GB dos quais são o `.git_gordo`).

### 🟢 LIMPA — Lixo técnico (deletável, sem mudar de pasta)

| Item | Peso | Por que pode ir |
|---|---:|---|
| `.aider.tags.cache.v4/` | 91 MB | Cache do aider; regenera sozinho |
| `claude-desktop_amd64.deb` | 166 MB | Instalador; após o upgrade do Ubuntu (sexta) perde a função — e sempre se baixa de novo |
| `node_modules/` | 19 MB | `npm install` recria em segundos |
| `__pycache__/`, `.pytest_cache/` | 590 KB | Caches Python |
| `tmp/` | 8,3 MB | ⚠️ revisar conteúdo antes, mas por definição é temporário |
| `.transcribe_venv/` | — | Venv recriável com requirements |

**Subtotal que limpa: ~285 MB.**

### ⚪ DIRETÓRIOS VAZIOS encontrados (candidatos a remoção)

```
Outros/passagem/                    Outros/videos teste/
Outros/twitter_media_harvest/       Global South News/server doin/
contratos/                          agent_data/agent_mundotrilhos/
agent_data/agent_railpost/          Projeto Cafezinho Agentes/.git/  ← ⚠️ .git VAZIO: investigar (repo quebrado?)
```

---

## 5. Resultado Projetado

| Cenário | Workspace | Leitura |
|---|---:|---|
| Hoje | 30 GB | Pós-reforma bruta |
| Após mover 🟡 | **~9,6 GB** | Produção + histórico vivo |
| Após limpar 🟢 e ⚪ | **~9,3 GB** | Workspace enxuto |
| Fase 3 futura (sanear `.git` internos dos portais) | ~4–5 GB | Workspace de competição |

**O passo único mais valioso:** mover `.git_gordo_20260620/` → Estante. Um comando, −60% do workspace.

## 6. Protocolo de Execução (quando o Miguel autorizar)

1. Miguel renomeia `~/Dados_Frios/` → `~/Estante Principal/` (ou eu executo, se autorizado — **atenção:** atualizar a fila de upload pro Drive e o índice da reforma, que citam o nome antigo).
2. Migração via `rsync` com verificação, começando pelo `.git_gordo` (janela sem crons: fora de 3h–13h).
3. Antes de mover qualquer 🟡: `grep -r "nome_da_pasta"` nos crontabs, `~/.zcode/AGENTS.md` e scripts ativos — prova negativa obrigatória.
4. Cada leva registrada no `CEREBRO_INDEX_REFORMA_ARQUIVOS_20260722.md` + Fórum/Memória.
5. Limpeza 🟢 por último, só depois da Estante validada.
6. Script de reversão gerado junto com cada leva (rollback de 1 comando).

## 7. O que este manifesto NÃO autoriza

- ❌ Mover, renomear ou deletar qualquer arquivo agora
- ❌ Tocar em caminhos de produção (Seção 4, 🔴)
- ❌ Renomear `Dados_Frios` sem atualizar os índices que o referenciam

---

*Escrito por Kimi k3 em 22/07/2026, ~23h. Mapeamento empírico via `du`, `crontab -l`, `find`. Nada foi alterado no disco durante a elaboração deste documento.*
