# 🗺️ FÓRUM — Mapa geral das missões ZCode + auditoria de backup pré-limpeza

**Data:** 25/08/2026 ~19:30 · **Agente:** ZCode/Kimi K3 (1ª missão após reintegração) · **Status:** mapeamento concluído; limpeza NÃO iniciada

## 1. Inventário da memória do ZCode

`~/.zcode/cli/memories/.../memory/`: **286 arquivos** (~1,4 MiB), cobrindo 13/08→25/08.

- **Concluídas:** dezenas — destaques: V4 OFF + V4.1 exclusivo, Painel CCTV V6, Rio Carta retomado, Ponte Café bidirecional, Ponte Laura Completa 8/8, Contrato Geral homologado, Moka espelho no ar, decisão de modelos 25/08, aliança Fênix×Cafezinho planejada.
- **Pendentes do Miguel (26):** recarga DeepSeek / não renovar Kimi, ACK publicadores, Mapa Rio OK produção, Moka Drive (4 passos), cofre SSH "selar", cross-promo banners, campanha Moka, V4 R1b/R4, saúde servidores, Instituto ILS sede, etc.
- **Pendentes técnicas (26):** mapa arquitetura + ronda loops (em curso), DeepSeek NYC 401, Transkriptor 47 falhas, plano autoria F0.2-F3, GA4 realtime, faxina taxonomia ondas 1c/1d, migração Dell→Laura, etc.
- **Obsoletas (15):** enxame manchete (revogada), ronda V4 30/30, ponte simples, "sombra/termômetro", agente Instagram noturno, ordens "Kimi sempre", banco de links congelado, etc.
- **Recorrentes (32):** rondas V4.1, §118, Baleia Azul, Tribunal Diário, trilho git 15min, backup diário, acervo 100%, gate de estoque, etc.

## 2. Veredito do backup — NÃO está 100% (não limpar ainda)

| Destino | Status | Última prova |
|---|---|---|
| GitHub cerebro-miguel (push+pull 15min) | ✅ | 25/08 19:22 |
| Backblaze B2 (diário + loops 30min) | ✅ | 25/08 03:40 / 19:16 |
| Google Drive (diário + loops) | ✅ | 25/08 03:41 / 19:17 |
| **Alibaba (rsync)** | ❌ **falha desde 22/08** (host key mudou) | última falha 25/08 03:42 |
| **~/.zcode (3,8 GB: config, hooks, memórias)** | ❌ **SEM backup** | — |
| **6 arquivos sensíveis do Cerebro** (bloqueados do sync) | ❌ só no disco local | — |

**Conclusão:** o pedido "confirma que fez backup de tudo" tem resposta honesta: **não**. Cérebro está em 3 lugares (GitHub/B2/Drive), mas a pasta `~/.zcode` — que é exatamente o que o Miguel quer limpar — **não tem backup nenhum**. E o 3º destino do backup diário (Alibaba) está quebrado há 4 dias.

### Fechar antes de limpar (obrigatório)

1. **Backup one-shot de `~/.zcode`** (tar/rclone → B2 + Drive, excluindo caches grandes regeneráveis, com manifesto). ~1 minuto de comando.
2. **Reparar Alibaba** (host key) ou aceitar oficialmente 2 destinos remotos.
3. Guardar os 6 arquivos sensíveis em destino cifrado fora do disco local.

Só depois disso: limpeza.

## 3. Auditoria de indexação — boa, com 3 gaps de 25/08

Tudo de 25/08 está nos nodos, **exceto**:

1. `forum_moka_ousadia_20260825.md` — órfão (vai em CEREBRO_INDEX_MOKA_MASTER).
2. `memoria_moka_gdrive_arquivado_20260825.md` — órfã (encerramento Drive Moka sem registro).
3. `forum_proposta_fontes_ciencia_ia_saude_20260825.md` — órfão (vai em NODE_DIRETRIZES_COLETORES).
4. Parcial: memória do Fórum 11:30 sem link nominal (Tema Duplo incompleto).

Mais ~15 órfãos de 20-24/08 (cartas, emendas, duplicatas NOME-X/NOME_X) — candidatos a varredura de compactação.

## 4. Plano de limpeza (após backup confirmado)

**Fase 0 — backup:** item 2 acima (one-shot ~/.zcode + Alibaba + sensíveis).
**Fase 1 — catalogar:** fechar os 3 gaps de nodos + índice semanal.
**Fase 2 — limpar ZCode leve:** `~/.zcode` pesado = `cli/exec` (snapshots de sessão), `rollout` (model-io), `artifacts`, caches de update, `v2/sessions` antigas — apagar só o regenerável, preservar config/hooks/memórias (já em backup).
**Fase 3 — memória ZCode:** compactar MEMORY.md (99KB > limite), mover detalhe de missões concluídas para o Cérebro, manter só regras vivas + pendentes.
**Fase 4 — Cérebro:** varredura duplicatas + órfãos, sem apagar histórico (tudo vira arquivo morto linkado).

## 5. O que aconteceu / o que falta / o que preciso do Miguel

**O que aconteceu:** mapa completo (286 memórias, 32 rotinas, 52 pendências), auditoria de backup (3 destinos OK, 2 falhando), auditoria de nodos (3 gaps).

**O que falta:** backup de ~/.zcode + reparo Alibaba — **sem isso, não limpar**.

**O que preciso do Miguel:** autorizar a Fase 0 (backup one-shot ~/.zcode agora) e dizer se aceita 2 destinos remotos (dispensando Alibaba) ou se quer o reparo.


## ADENDO — divulgação executada 25/08 22:39 (automação 22:30)

1. **Telegram:** resumo humanizado enviado ao Miguel (mapa 286 memórias + veredito backup + 2 pendências).
2. **Baleia Azul:** novo digest `~/bin/baleia_mapa_zcode_digest.py` anexado ao emissor (bloco 3.6, fail-soft; rollback `.bak_pre_mapa_zcode_20260825_2230`; prova visual 7 linhas).
3. **CCTV:** página **Mural Geral** no ar em `http://43.156.151.165/v6/mural-geral` (HTTP 200 interno e público; backup `.bak_mural_geral_20260825_2230`; regressão 5/5).
