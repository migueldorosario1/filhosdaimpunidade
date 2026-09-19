# 🐤 CEREBRO NODE — Canário Pós-Reforma

> **Data:** 14 de junho de 2026  
> **Status:** Ativo  
> **Local:** Tencent VPS (Cingapura) — `/root/cafezinho/`  

---

## 📍 O que é este nó

Este nó documenta o estado atual do canário pós-reforma em paralelo com o legado.

---

## 🔗 Links

- **Diário de Bordo:** `Projeto Cafezinho Agentes/Foruns/forum_diario_bordo_canario_20260614.md`
- **Fórum geral da Reforma:** `Cerebro/Foruns/forum_grande_reforma_balanco_geral_e_consolidacao_20260613.md`
- **Inbox Kimi:** `Cerebro/Foruns/inbox_trindade/kimi.md`

---

## 📊 Estado Atual (última atualização: 21:30 BRT)

| Métrica | Valor |
|---------|-------|
| **Status do canário** | 🟢 Ativo (primeiro ciclo em andamento) |
| **Temas ativos** | 9 (geopolitica, nacional, lula, eleicoes, crime, militar, sheinbaum, flavio_bolsonaro, china) |
| **Frequência** | A cada 15 minutos (primeiras 2h) |
| **Posts gerados hoje** | 0 (ciclo em andamento) |
| **Notícias auditadas total** | 15 (14 de ontem + 1 hoje) |
| **Fact-check** | 100% aprovado |
| **Publicação** | Draft (protegido) |
| **Processos ativos** | 7 |
| **Erros críticos** | 0 |

---

## 🗂️ Arquivos de Monitoramento

| Arquivo | Caminho no Tencent |
|---------|-------------------|
| Log do canário | `/root/cafezinho/Dados/logs/canario.log` |
| Banco SQLite | `/root/cafezinho/Dados/bancos/pipeline_editorial_local.db` |
| Anti-repetição | `/root/cafezinho/Dados/logs/anti_repeticao.log` |
| Scripts | `/root/cafezinho/scripts/` |

---

## 👥 Responsáveis

- **Kimi:** Métricas, volume, latência, erros
- **Claude:** Comparação editorial
- **Codex:** Operação e correções
- **GLM:** Qualidade de redação
- **Qwen:** Fact-check e viés
- **AGY:** Arquitetura e integridade
- **Antigravity:** Segurança e isolamento

---

## 📝 Notas

- Canário ligado em: 2026-06-14 21:10 BRT
- Primeiro relatório: 2026-06-14 21:30 BRT (Kimi)
- Plano: 7 dias de canário paralelo
- Meta: 30 posts/dia
- Comando K adotado pela Trindade: comparação rápida legado vs pós-reforma. Histórico em `Projeto Cafezinho Agentes/Foruns/forum_comparativo_legado_vs_pos_reforma_20260614.md`.
- Regra Codex para K: sempre declarar janela temporal usada, porque "hoje", "últimas 24h" e "desde o início do canário" dão números diferentes.
- 2026-06-14 21:40 BRT — Codex validou `Cerebro/scripts/comparativo_k.py` e `scratch/comparativo_k.py`: removida credencial embutida, endpoint público sem autenticação, banco preferencial do canário ajustado para `portal_cafezinho`, `py_compile` OK.
- 2026-06-14 21:50 BRT — Padrão K Unificado aplicado por Codex: script canônico agora roda em uma única conexão SSH, inclui métricas obrigatórias ampliadas, mantém WordPress público sem credencial embutida e conta também `Falha`/`❌` como erro operacional.
- 2026-06-14 — Parecer Codex sobre estratégia de transição: 4 camadas fazem sentido no canário, mas precisam de estados fechados (`draft_gerado`, `qualidade_pronto`, `qualidade_revisar`, `guardiao_liberado`, `guardiao_bloqueado`, `revisao_humana`, `publish_liberado`) e plano de simplificação após 48h estáveis.
- 2026-06-14 22:14 BRT — Codex implementou no publicador do canário o custom field invisível `meta.origem_transicao=canario`. Validado local e remoto em dry-run; subido para Tencent via rsync canário. Legado precisa de implementação própria `origem_transicao=legado` pela frente responsável.

---

> Atualizado por: Kimi (Maestro Diagnóstico)  
> Última atualização: 2026-06-14 21:30 BRT

| 2026-06-14 21:45 | Reset comparativo | Backup: `historico_comparativos/forum_comparativo_20260614_2145.md` |
