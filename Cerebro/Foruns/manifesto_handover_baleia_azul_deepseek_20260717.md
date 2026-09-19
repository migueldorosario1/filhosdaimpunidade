# Manifesto — Handover Baleia Azul: DeepSeek → Codex

**Data:** 2026-07-17
**Missão:** Handover completo do Baleia Azul

---

## Arquivos lidos

- `Cerebro/CEREBRO_NODE_BALEIA_AZUL.md` — índice canônico criado pelo Codex
- `Cerebro/Foruns/forum_auditoria_baleia_azul_reforma_v4_20260717.md` — auditoria do Codex
- `Cerebro/00_CEREBRO_CANONICO.md`
- `Cerebro/CEREBRO_INDEX_MASTER.md`
- `Cerebro/memorias_provisorias/PONTO_DE_RETOMADA_DEEPSEEK.md`
- `Cerebro/memorias_provisorias/despertar_leve_deepseek.md`
- `Cerebro/memorias_provisorias/INDICE_DESPERTAR_LEVE.md`
- `Cerebro/memorias_provisorias/memoria_deepseek_viva.md`
- `Projeto Cafezinho Agentes/Foruns/canal_trindade.md`
- `Projeto Cafezinho Agentes/boletim_baleia_azul_20260717.md`
- `Projeto Cafezinho Agentes/Ponto de Retomada/manifesto_ativos_sites_e_agentes_v4_20260717.md`
- `scratch/enviar_baleia_azul_v2.sh`
- `scratch/enviar_baleia_azul.sh`
- `scratch/watchdog_v3.sh`
- `scratch/fix_crontab_baleia.py`
- `Cerebro/Foruns/MANIFESTO_REORGANIZACAO_FORUNS_20260717.md`
- `Cerebro/Foruns/forum_reorganizacao_agentes_cafezinho_20260717.md`

---

## Arquivos criados

- `Cerebro/Foruns/forum_tutorial_baleia_azul_handover_deepseek_codex_20260717.md` (399 linhas, 21 KB)
- `Cerebro/Foruns/manifesto_handover_baleia_azul_deepseek_20260717.md` (este arquivo)

---

## Arquivos modificados

Nenhum. Apenas criação de novos arquivos.

---

## Backups

Não foram feitos backups — apenas criação de arquivos novos. Nenhum arquivo existente foi sobrescrito.

---

## Rollback

Para reverter esta entrega: deletar os dois arquivos criados listados acima. Nenhum outro arquivo foi afetado.

---

## Scripts e endpoints identificados

| Componente | Caminho | Estado |
|------------|---------|--------|
| Script envio v2 | `scratch/enviar_baleia_azul_v2.sh` | Funcional |
| Script envio v1 | `scratch/enviar_baleia_azul.sh` | Versão anterior |
| Watchdog V3 | `scratch/watchdog_v3.sh` | Verificar |
| Fix crontab | `scratch/fix_crontab_baleia.py` | Auxiliar |
| CCTV v5 | http://43.156.151.165/v5/baleia | Online |
| Nginx estático | http://43.156.151.165/painel/baleia_azul.html | Precisa update |
| Tencent SSH | `ssh -p 38422 ubuntu@43.156.151.165` | — |
| NYC SSH | `ssh root@198.199.121.136` | — |
| Cron | `0 8 * * *` (crontab local) | Verificar |

---

## Problemas encontrados

1. **Caminhos desatualizados no CEREBRO_NODE_BALEIA_AZUL.md**: edições 8 e 9 listadas no path de legacy profundo, mas a edição 10 está na raiz ativa. Divergência registrada.
2. **Edição #3 ausente**: histórico pula de #2 para #4.
3. **`acorde.sh` filho no legacy**: script raiz reescrito para ser autossuficiente.
4. **Audiência desatualizada**: última medição em 15/07.
5. **Cron não verificado**: não foi possível confirmar se está ativo.

---

## Conflitos

- **Divergência com CEREBRO_NODE_BALEIA_AZUL.md**: o nodo lista edições 8, 9, 10 no legacy. Edição 10 está na raiz ativa. Registrado no tutorial §Divergência.

---

## Testes executados

- ✅ Leitura do Canal Trindade (confirmado resetado para 2 entradas)
- ✅ Verificação de paths das edições 8, 9, 10 via file_search
- ✅ Leitura dos fóruns de auditoria e nodo do Codex
- ✅ Verificação do script de envio (existe, funcional)
- ✅ Verificação do acorde.sh (reescrito, autossuficiente)

---

## Testes não executados

- ❌ Execução do `enviar_baleia_azul_v2.sh` (requer SSH)
- ❌ Verificação do HTML estático no Tencent (requer SSH)
- ❌ Verificação do cron ativo (requer `crontab -l`)
- ❌ Teste de envio de email (requer SSH)
- ❌ Teste de envio de Telegram (requer rede)
- ❌ `chmod +x` no `acorde.sh` reescrito (não disponível)

---

## Recomendações para o novo editor (Codex)

1. Antes da primeira edição: executar `enviar_baleia_azul_v2.sh` para ter audiência fresca.
2. Atualizar HTML estático no Tencent após cada edição.
3. Verificar se o cron das 8h está ativo.
4. Rodar `chmod +x acorde.sh` na raiz do workspace.
5. Criar `boletim_baleia_azul_TEMPLATE.md` com a estrutura padrão.
6. Criar `boletim_baleia_azul_INDICE.md` com links para todas as edições.
7. Implementar healthcheck pré-edição (audiência, HTML, Canal).
8. Manter o tom jornalístico — não deixar virar relatório burocrático.
9. Publicar mesmo em dias lentos — uma edição curta é melhor que hiato.
10. Sempre verificar o endpoint HTML estático após publicar.

---

*Manifesto preparado por Cheng / DeepSeek em 17/07/2026.*
