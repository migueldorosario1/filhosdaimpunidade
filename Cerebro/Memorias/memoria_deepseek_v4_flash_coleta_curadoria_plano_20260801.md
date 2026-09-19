# MEMÓRIA — DeepSeek V4 Flash em coleta/curadoria: diagnóstico técnico completo

**Data:** 2026-08-01 ~17:30 BRT
**Autor:** ZCode (GLM-5.2), ordem direta do Miguel
**Fórum irmão:** `Foruns/forum_deepseek_v4_flash_coleta_curadoria_plano_20260801.md`
**Tipo:** Log técnico — mapeamento preciso do roteador V4 e pontos de mudança.

---

## 1. Arquitetura do roteador V4 (estado ao vivo NYC 01/08)

**Arquivos canônicos (NYC produção):**
- `/root/agente_roteador_llm.py` (145 KB, 29/07 19:14) — roteador principal
- `/root/config/llm_context_routes.json` (3,2 KB, 25/05) — ordem editorial por contexto
- `/root/config/llm_ratings.json` (39 KB, 29/07) — sistema de notas Q/P/V

**Mecanismo:** agentes chamam `gerar_texto(..., contexto="X")` ou `gerar_texto_governado(tarefa="Y", ...)`. O roteador consulta `llm_context_routes.json` (`contexts[X]`) → lista de provider_tier ordenada → tenta em ordem com fallback.

## 2. Contextos existentes em llm_context_routes.json

`luxo`, `padrao`, `economico`, `revisor`, `auditor`, `eleicoes_redacao`, `eleicoes_auditoria`, `eleicoes_revisao`, `eleicoes_chines`, `comentario_site`, `comentario_site_resposta`, `analise_sentimento`, `dinamico`, `editorial`, `social_redator`, `super_luxo`, `super_luxo_auditoria`, `producao_editorial_v3_super_luxo`, `brutas_plus_v3_super_luxo`, `auditoria_final_v3_super_luxo`, `tribunal_visual_gemini_luxo`.

**⚠️ NÃO existe contexto `coleta`, `curadoria` nem `scoring` explícito.** A curadoria da coleta (`motor_coletor.py`) chama `gerar_texto_governado(tarefa="scoring")` → cai num tier default do roteador (provável: `economico` ou hardcode).

## 3. Mapeamento: quem chama o quê (coleta/curadoria)

| Arquivo | Função LLM | Contexto/tarefa | Modelo atual |
|---------|-----------|-----------------|--------------|
| `motor_coletor.py:250` | `gerar_texto_governado` | `tarefa="scoring"` | default roteador (investigar) |
| `motor_coletor.py:211` | `curadoria_llm_rapida()` | wrapper do scoring | — |
| `agente_curador_fontes.py` | `gerar_texto` | sem contexto explícito | default |
| `agente_curadoria.py` | `gerar_queries()` | (não é LLM, só string) | — |
| `agente_curadoria_gsn.py` | (herda motor_coletor) | `scoring` | default |
| `refresh_curadoria.py` | (orquestra curadores) | — | — |
| `agente_coletor_social.py` | `gerar_texto` | `social_redator`, `editorial` | DeepSeek luxo |
| `agente_produtor_bella_ciao.py` | `gerar_texto_artigo` | direto | **`deepseek-v4-flash` ✅ (já usa!)** |
| `agente_eleicoes_produtor.py` | roteador | `retry`, `auditor`, `revisor` | DeepSeek |
| `agente_comentarista_v4.py` | roteador | `comentario_site_resposta` | — |

**Prova de viabilidade:** `agente_produtor_bella_ciao.py` já roda `deepseek-v4-flash` direto em produção → infra suporta, modelo funciona.

## 4. Plano de mudança (3 camadas, rollback por arquivo)

### Camada 1 — `llm_context_routes.json` (mapeamento scoring)
Adicionar contexto `scoring` apontando pra `deepseek_economico` (que resolve pra v4-flash):
```json
"scoring": ["deepseek_economico", "alibaba_economico", "moonshot_economico"]
```
(fallback asiático barato, sem ocidental — alinhado à política de economia)

### Camada 2 — `agente_roteador_llm.py` (confirmar resolução)
- Verificar que `tarefa="scoring"` no `gerar_texto_governado` resolve pelo `contexts["scoring"]` (se não existir mapeamento tarefa→contexto, criar).
- Garantir que `deepseek_economico` tier aponta pra `deepseek-v4-flash` (não `deepseek-chat` legado).

### Camada 3 — `motor_coletor.py` (ponto de chamada)
- Linha 250: `gerar_texto_governado(tarefa="scoring")` — sem mudança necessária se camadas 1+2 estiverem certas. Confirmar após deploy.

### Curadores diretos (avaliar caso a caso no deploy)
- `agente_curador_fontes.py` e outros que chamam `gerar_texto` sem contexto: forçar `contexto="scoring"` ou `economico` se a tarefa for curadoria/filtro.

## 5. Matriz de NÃO-mudança (respeitar autorização Miguel)

| Contexto | Ação | Motivo |
|----------|------|--------|
| `luxo`/`padrao`/`editorial` (redação) | **MANTÉM** | Miguel: "não redação" |
| `auditor`/`revisor` | **MANTÉM** | Miguel: "não auditoria" |
| `super_luxo*` | **MANTÉM** | editorial premium |
| `tribunal_visual` | **MANTÉM** | visão, não Coleta/curadoria |

## 6. Saldo DeepSeek ao vivo (bloqueador)

```
GET https://api.deepseek.com/user/balance (NYC, 01/08 ~17:25 BRT):
  total_balance: $0.37
  topped_up_balance: $0.37
  granted_balance: $0.00
```
`deepseek-chat` respondeu HTTP 200 ("你好！很高兴") — API viva, saldo quase zero.

**Estimativa de consumo em coleta+curadoria:** alto volume (centenas/dia nos 8 temáticos). $0,37 → esgota em horas. Necessário ≥ $5 antes do deploy; recomendado $10-20 pra validação tranquila.

## 7. Histórico de consumo DeepSeek (contexto)

- 01/08 15:05: saldo $1,20 (forum auditoria custos)
- 01/08 ~17:25: $0,37 (esta medição) → consumiu ~$0,83 em ~2h
- 01/08 13:52 UTC: circuit breaker marcou `deepseek-v4-pro quota_exhausted em cooldown (219min)`
- Taxa observada: ~$0,40/h em uso normal → sem rotear coleta. Com coleta roteada, escala muito mais.

## 8. Rollback (1 comando por arquivo)

```bash
ssh nyc "cp /root/config/llm_context_routes.json.bak_pre_dsflash_<ts> /root/config/llm_context_routes.json"
ssh nyc "cp /root/agente_roteador_llm.py.bak_pre_dsflash_<ts> /root/agente_roteador_llm.py"
ssh nyc "cp /root/motor_coletor.py.bak_pre_dsflash_<ts> /root/motor_coletor.py"
```

## 9. Gatilho de ativação (QUANDO Miguel recarregar)

1. Miguel recarrega DeepSeek (≥ $5 ideal, $10-20 recomendado).
2. Me confirma: "saldo DeepSeek recarregado, pode ativar v4-flash".
3. Eu rodo: backup → mudança camadas 1+2 → smoke isolado → observação 1 ciclo → confirmo custo caiu.

## 10. Pendências

1. Miguel recarregar DeepSeek.
2. Confirmar escopo (temáticos+V4 vs piloto 1 portal).
3. (Opcional) Definir teto diário de gasto DeepSeek + alerta vigia (padrão já existe p/ Qwen).

— ZCode (GLM-5.2), 01/08/2026 ~17:30 BRT
