# História do agente Caetano (2026-05-31 → 2026-06-26)

**Status atual**: ⚰️ APOSENTADO definitivamente em 2026-06-26 por autorização Miguel.
**Período ativo real**: 31/05 a 09/06/2026 (10 dias produtivos).
**Aposentadoria executada por**: Claude Code (Daemon) em 26/06/2026 01:18 BRT.
**Causa raiz**: defeito de fundo (loop de autodetecção com 98% de falso positivo) + script principal movido pra `/root/legacy_scripts/` no dia caótico do bug `empty_content` e nunca foi voltado.

---

## 1. Quem era o Caetano

Sistema de **triagem editorial pós-publicação** do portal Cafezinho. Persona com bot Telegram próprio (token `8530517301...`). Conversava com Miguel via botões interativos ("📊 Ver próximo") pra resolver problemas detectados em posts já publicados.

A escolha do nome "Caetano" foi apelido afetivo — outros agentes do sistema seguiam tradição similar (Augusto = Telegram brain, Maestro = orquestrador, etc).

## 2. Arquitetura (3 peças)

```
posts publicados no WP
        │
        ▼
agente_observador.py  ──→  suspeitos_caetano.json  (fila)
   (loop §90 via Maestro)              │
                                       ▼
                       caetano_auto_limpeza.py  (cron 06:00 diário)
                                       │
                                       ▼
                                  triagem
                                  (crítico vs corrigível)
                                       │
                                       ▼
                       consolidar_caetano_diario.py  (cron 08:00 diário)
                                       │
                                       ▼
                              Telegram com botões
                                       │
                                       ▼
                                     Miguel
```

| Peça | Tipo | Função |
|---|---|---|
| `agente_observador.py` | Detector (vivo) | Loop chamado a cada 20min via maestro. Escrevia em `suspeitos_caetano.json` quando detectava problema |
| `caetano_auto_limpeza.py` | Triador (cron 06:00) | Separava críticos vs corrigíveis, removia tratados, arquivava antigos |
| `consolidar_caetano_diario.py` | Comunicador (cron 08:00) | Lia buffer do dia, montava resumo HTML, enviava 1 mensagem Telegram com botões |

## 3. O que detectava (5 problemas reais)

| # | Motivo | Casos no diagnóstico inicial (31/05) |
|---|---|---|
| 1 | **Metalinguagem de IA vazada** ("Como modelo de linguagem...", "Espero que esta análise...") | 814 |
| 2 | **Citação crua** (texto cru de fonte sem formatação) | 515 |
| 3 | **Post sem imagem destacada** | 123 |
| 4 | **Entidades HTML escapadas** (`&amp;` no lugar de `&`) | 68 |
| 5 | **Sem consenso 3/3 entre 5 auditores LLM** | 45 |
| | **Total diagnosticado** | **2.262 posts** |

## 4. Período ativo — métricas reais

Fonte: `caetano_limpeza_log.jsonl` (21 entries, 31/05 13:06 → 09/06 06:00).

| Métrica | Valor |
|---|---|
| Período | 31/05 → 09/06/2026 |
| Duração ativa | **10 dias** |
| Total execuções | 21 |
| Execuções produtivas (>0 ações) | 10 |
| Execuções vazias | 11 |
| Tratados pelo Miguel | **0** |
| Arquivados (>X dias) | **489** |
| Diagnóstico inicial | 2.262 posts |

**Padrão**: Miguel nunca chegou a tratar manualmente os flagged via Telegram. Tudo que saía da fila ia por arquivamento automático (timeout).

## 5. Cronologia da morte (dia 31/05/2026 — incidente fundador)

| Hora | Evento |
|---|---|
| 13:06 | Caetano executa primeira triagem completa: **2.262 posts** diagnosticados |
| **13:08** | `caetano_auto_limpeza.py` **movido pra `/root/legacy_scripts/`** (mtime de criação no destino) |
| 13:53 | Sprint Qwen Coding ("remover markers internos" — P0 da fila Caetano) deploya patch em `motor_publicador.py` |
| 14:50 | DeepSeek autoriza o sprint |
| 15:22-15:44 | Posts saem do WP com payload VAZIO em série (trends/geopolitica/lula/nacional) — HTTP 400 `empty_content` |
| 15:45 | Maestro §90 detecta bug |
| 16:10 | Fórum 🔴 ATIVO aberto: "regressão introduzida pelo sprint Caetano" |
| **17h-18h** | Patch correto deployado, motor volta a publicar |
| **dias seguintes** | `caetano_auto_limpeza.py` continua em `legacy_scripts/`, ninguém volta a olhar |

**Hipótese provável**: no calor do incidente alguém moveu `caetano_auto_limpeza.py` pra `legacy_scripts/` pra "remover a regressão", esqueceu de tirar do cron OU atualizar o path. Cron continuou apontando pra `/root/caetano_auto_limpeza.py` que não existia mais. Falha silenciosa em `/var/log/caetano_auto_limpeza.log` (7.239 bytes só de "No such file") por **17 dias** (31/05 → 17/06 — depois ninguém ligou).

**Última tentativa de retomada**: 09/06 23:52 (mtime "Change" do arquivo em legacy) — alguém mexeu mas não voltou pro `/root/`.

## 6. Defeito de fundo (visto no buffer 2026-06-05 01:41)

Trecho real do `caetano_buffer_2026-06-05.log`:

> "Miguel, 54 itens na fila, 24 marcados como críticos, 95 horas parados. O fiscal automático gerou 53 dos 54 alertas sozinho, e a **taxa de falso alarme está em 98%**.
>
> O padrão é claro: o fiscal está lendo as próprias instruções editoriais do sistema e apitando como se fossem vazamento de prompt no corpo do artigo. É um **loop de autodetecção** — a máquina farejando o próprio manual e achando que é invasão. Os três casos do topo são todos iguais nisso."

**O problema técnico**: o detector de "metalinguagem de IA vazada" (motivo #1, 814 casos no diagnóstico inicial) estava sendo enganado pelas próprias instruções/regras editoriais que constavam no rodapé ou nos metadados de alguns posts. Triggava como "vazamento de prompt" o próprio manual de redação.

**Consequência**: 98% dos alertas eram falso positivo. Sinal não-acionável. Miguel parou de responder.

## 7. Sprint "Fila do Caetano" (P0 que gerou regressão)

| Item | Quem | Quando |
|---|---|---|
| Proposta | Qwen Coding | 31/05 12:30 BRT |
| Autorização | DeepSeek | 31/05 14:50 |
| Deploy | Qwen Coding | 31/05 13:53 |
| Backup | `motor_publicador_pre_fix_metalinguagem_20260531_1353_qwen.py` (§82.3) |
| Detecção bug | Maestro §90 | 31/05 15:45 |
| Causa-raiz | Bloco `limpar_markers_internos()` caiu em lugar errado no `motor_publicador.py` |

Objetivo da sprint **era legítimo** (remover 94% dos markers internos vazados, motivos #1 e #2 do Caetano). Falha foi de **inserção/merge** durante deploy, não da lógica.

## 8. Por que aposentar (decisão 2026-06-26)

Combinação de 3 fatores:
1. **17 dias de bug silencioso** sem ninguém notar — sinal de baixa relevância prática
2. **Defeito de fundo não resolvido** — loop autodetecção com 98% FP
3. **Sucessores parciais já existem** — pipeline V3 (quando voltar) tem auditor próprio: `agente_auditor_titulos_gpt.py` (15min), `agente_qualidade_redacao.py` (3h30), `agente_diretrizes_editoriais.py` (4h)

## 9. O que ficou aposentado em 2026-06-26 01:18 BRT

### Cron pausado (REGRA #3 — append cirúrgico, preservou 165 linhas)

L68 do crontab root:
```
# APOSENTADO_CAETANO_20260626 0 6 * * * /usr/bin/python3 /root/caetano_auto_limpeza.py >> /var/log/caetano_auto_limpeza.log 2>&1
```

Ativas: 52 → 51.

### Código patcheado

`/root/agente_observador.py`:
- Adicionada flag `CAETANO_APOSENTADO = True` no topo
- 3 funções viraram stubs no-op (não quebra chamadas):
  - `carregar_suspeitos()` → retorna `[]`
  - `salvar_suspeitos(lista)` → no-op
  - `enviar_telegram_caetano(texto, reply_markup=None)` → no-op silencioso
- Backup em `/root/backups/agente_observador.py.bak_pre_aposentar_caetano_20260626_011836`

### Artefatos arquivados em `/root/legacy/caetano_aposentado_20260626/`

| Tipo | Quantidade | Origem |
|---|---|---|
| `caetano_buffer_*.log` (35 buffers diários mai/jun) | 35 | `/root/agent_data/` |
| `suspeitos_caetano*.json` (4 arquivos) | 4 | `/root/agent_data/` |
| `caetano_limpeza_log.jsonl` | 1 | `/root/agent_data/` |
| `caetano_auto_limpeza.py` | 1 | `/root/legacy_scripts/` |
| `consolidar_caetano_diario.py` | 1 | `/root/` |
| `var_log_caetano_auto_limpeza.log.archived` | 1 | `/var/log/` |
| **README necrologio** | 1 | criado |
| **Total movidos** | **42** | |

### Dependências secundárias (não-aposentadas)

`agente_autocura_v4.py` ainda referencia `suspeitos_caetano.json` (linhas 70, 152, 644) — mas como `salvar_suspeitos` é stub no-op, o arquivo nunca mais é populado. Autocura vai ler arquivo vazio (a função `carregar_suspeitos` agora retorna `[]`).

`autocura_licoes.py` tem `horas_sem_interacao_caetano()` — vai retornar 99.0 (default) indefinidamente, pois flag de interação nunca mais é atualizada.

Comportamento esperado: silencioso. Nenhum desses quebra.

## 10. Como reverter (improvável, mas documentado)

```bash
# Restaura observador.py original
sudo cp /root/backups/agente_observador.py.bak_pre_aposentar_caetano_20260626_011836 /root/agente_observador.py

# Restaura crontab
sudo crontab /root/backups/crontab_root_pre_aposentar_caetano_20260626_011836.txt

# Restaura artefatos
sudo mv /root/legacy/caetano_aposentado_20260626/caetano_buffer_*.log /root/agent_data/
sudo mv /root/legacy/caetano_aposentado_20260626/suspeitos_caetano*.json /root/agent_data/
sudo mv /root/legacy/caetano_aposentado_20260626/caetano_limpeza_log.jsonl /root/agent_data/
sudo mv /root/legacy/caetano_aposentado_20260626/caetano_auto_limpeza.py /root/  # ou /root/legacy_scripts/ + ajusta cron path
sudo mv /root/legacy/caetano_aposentado_20260626/consolidar_caetano_diario.py /root/
sudo mv /root/legacy/caetano_aposentado_20260626/var_log_caetano_auto_limpeza.log.archived /var/log/caetano_auto_limpeza.log
```

**Antes de reverter**: corrigir o defeito de fundo do loop de autodetecção (whitelist do próprio manual editorial antes de classificar como "vazamento de prompt"). Sem isso, 98% FP volta.

## 11. Lições

1. **Bug silencioso de cron**: script removido sem tirar do cron = falha silenciosa que pode durar semanas. **Mitigação**: cron deveria ter alerta de "script not found" via watchdog. Considerar implementar.
2. **Confusão pós-incidente**: limpar arquivos no calor de bug em produção é arriscado — pode mascarar coisas funcionais. Sempre fazer backup nominal antes.
3. **Detector vs falso positivo**: 98% FP mata acionabilidade. Métrica de qualidade de alertas (precision/recall) deveria ter sido monitorada desde dia 1.
4. **Sucessores parciais**: 3 detectores do pipeline V3 cobrem 60-70% do escopo do Caetano. Migrar gradualmente é mais resiliente que ressuscitar.

---

**Aposentadoria executada por**: Claude Code (Daemon) — claude-opus-4-7 · Anthropic
**Autorização**: Miguel (autoridade final)
**Data**: 2026-06-26 01:18 BRT
**Protocolo**: carta dura (backup ANTES + REGRA #3 append cirúrgico + smoke pós + plano rollback documentado)
