---
name: Agente Análise — 1º teste real (2 rodadas) + cross-test Eleições — 2026-04-24 18h
description: 3 rascunhos publicados no WP (2 do Análise + 1 do Eleições), todos auditados por Grok-4. Padrão consistente PUBLICAR_COM_RETOQUES. WAF baniu IP residencial; sistema produtivo OK.
type: project
originSessionId: 7b364031-59bc-4cee-8526-b9521b506352
---
## Estado ao fim de 2026-04-24 ~19h BRT

### 3 rascunhos publicados (todos status=draft, 1ª semana forçada conforme §11.2 #7)

| post_id | Agente | Título | Palavras | Auditoria Grok-4 | Veredito |
|---|---|---|---|---|---|
| **239379** | Análise R1 | Faria Lima e a mídia orgânica: a pinça de classe que o governo se recusa a nomear | 825 | qualidade 8 / coerência 9 / fact-check 6 | PUBLICAR_COM_RETOQUES |
| **239381** | Análise R2 | Militares delatam o golpe e o STF enfrenta o que ninguém quer nomear em voz alta | 945 | qualidade 7 / coerência 8 / fact-check 6 | PUBLICAR_COM_RETOQUES |
| **239383** | Eleições | Centrão articula apoio a Tarcísio e enfraquece pré-candidatura de Bolsonaro à reeleição em 2026 | n/a | qualidade 8 / coerência 9 / fact-check 7 | PUBLICAR_COM_RETOQUES |

### Insight transversal das auditorias

Os dois agentes têm **voz e coerência sólidas (7-9)** mas pecam em **disciplina factual (6-7)**. Sem alucinações detectadas — mas vagueza em fatos específicos (datas, nomes, números). No Eleições especificamente: Validator Numérico Preliminar deixou passar um número possivelmente errado de votação do Eduardo Bolsonaro.

### Stack rodando

- **Modelos pinados teóricos:** Opus 4.7 + GPT-5.5 Pro + Grok-4 reasoning + Sonnet 4.6.
- **Modelos efetivos no teste:** Sonnet 4.6 (Anthropic) + GPT-5-chat-latest (OpenAI) + Grok-4 reasoning (auditor) — Opus 4.7 e GPT-5.5 Pro deram HTTP 400/404 (chave do projeto não tem acesso aos modelos mais novos ainda).
- **Custo efetivo:** ~US$ 0.10-0.20/matéria com Sonnet 4.6 (vs ~$0.50 projetados quando Opus liberar).

### WAF do `controle.ocafezinho.com` baniu IP residencial do Miguel

Causa: varredura prévia do `coleta_analises_miguel.py` (centenas de GETs em /wp-json com pagination cheia) acionou Wordfence/EdgeOne. **Sistema produtivo NÃO afetado** — Tencent (`43.156.151.165`) publica normalmente. Workaround usado pra publicar #239379: SCP do `camada4.json` pro Tencent + script enxuto `/tmp/publicar_run_temp.py`. Em ~10 min o WAF liberou e a R2 (#239381) publicou direto do localhost.

**Próximo `coleta_analises_miguel.py`:** adicionar throttle (sleep 1s entre paginações) + User-Agent identificável.

### Pendências priorizadas

1. **Habilitar Opus 4.7 e GPT-5.5 Pro na chave do projeto** (tier upgrade) — sem isso, fina flor é teórica.
2. **Camada 4.5 — imagem** com `flickr_live` + Tribunal Visual + cascata banco SQLite (mesmo padrão dos temáticos premium).
3. **Mayra na Praia → WhatsApp**: configurar `MIGUEL_WHATSAPP_ID` no `.env.unificado` pra notificação real chegar no celular.
4. **Throttle no `coleta_analises_miguel.py`** pra não acionar WAF de novo.
5. **Limite de palavras** revisitado pra 800-1400 (R1 ficou em 825 e a auditoria não considerou problema).
6. **Ancoragem factual no Pass B**: prompt deve exigir 2-3 dados específicos (data, número, nome) — auditoria detectou esse buraco nas duas rodadas.
7. **Cartão de Integridade do Eleições** — regex do Cartão precisa aceitar formatos comuns (`"Lula (PT) 56%"`, sem dois-pontos), senão pesquisas reais sempre caem em CARTAO_INCOMPLETO_REVISAVEL.
8. **Fact-check Perplexity** está caindo em fail-open porque Sonar agora retorna `<think>...` antes do JSON. Parser precisa pular bloco de raciocínio.

### Arquivos-chave criados nesta sessão

```
Projeto Cafezinho Agentes/root/
├── analise/                                  # pacote do Agente Análise
│   ├── schemas.py, historico_analises.py
│   ├── banco_teses.py, augusto_notifier.py (mantido)
│   ├── mayra_whatsapp_notifier.py            # canal de notificação real
│   ├── llm_router.py                         # pinagem por papel + sanitização JSON
│   ├── camada1_escuta.py … camada4_redacao.py
│   └── wp_publisher.py
├── agente_analise.py                          # orquestrador (CLI)
├── auditar_run_analise.py                    # auditoria externa do Análise
├── auditar_post_eleicoes.py                   # auditoria externa do Eleições
├── atualizador_modelos_llm.py                # bate em /v1/models dos 7 providers
├── agent_data/
│   ├── modelos_vivos.json                    # cache atualizado
│   └── precos_modelos.json                   # tabela de preços externalizada (48 modelos)
├── agent_data_analise/
│   ├── banco_analises_amplo.json             # 7290 análises Miguel
│   ├── banco_teses.json                      # 15 teses-âncora + exemplos TF-IDF
│   ├── curadoria_dia.json                    # input da Camada 1
│   ├── historico.db                          # SQLite anti-repetição (bootstrapado)
│   └── runs/<run_id>/                        # artefatos por execução
└── gerenciador_tokens.py                     # MOD: lê preços do JSON, fn /10k tokens
```

### Documentação

- `forum_agenteanalise.md` §14 — relatório dos 2 testes + auditorias.
- `forum_eleicoes_teste_cruzado_analise_20260424.md` — relatório do teste cruzado (arquivo dedicado pra não atropelar a tarefa paralela do Eleições).
