---
name: Sessão pausada 2026-04-24 ~19:15 BRT — retomar daqui
description: Miguel desligou no meio. Estado: blindagem âncoras universal deployada Tencent. Pendente trocar imagem do #239383 (errada — logo CartaCapital onde devia ser foto Tarcísio+Bolsonaro). Script pronto em /tmp.
type: project
originSessionId: 7b364031-59bc-4cee-8526-b9521b506352
---
## Onde paramos

Miguel disse "vou desligar o computador. grave urgente o que está fazendo" às ~19:15.

## Estado da sessão (Agente Análise — esta tarefa)

### ✅ Concluído nesta sessão

1. **Skeleton completo do Agente Análise** em `Projeto Cafezinho Agentes/root/analise/` (5 camadas + orquestrador + WP publisher).
2. **Atualizador de modelos** (`atualizador_modelos_llm.py`) bate em /v1/models dos 7 providers — JSON em `agent_data/modelos_vivos.json`.
3. **Tabela de preços externalizada** (`agent_data/precos_modelos.json` com 48 modelos + custo por 10k tokens).
4. **2 testes reais do Análise publicados como rascunho:**
   - **#239379** — "Faria Lima e a mídia orgânica" (825 palavras) — auditoria 8/9/6 PUBLICAR_COM_RETOQUES
   - **#239381** — "Militares delatam o golpe e o STF…" (945 palavras) — auditoria 7/8/6 PUBLICAR_COM_RETOQUES
5. **Cross-test do Eleições** (#239383) — auditoria 8/9/7 PUBLICAR_COM_RETOQUES.
6. **Bug "Folha → CartaCapital" do #239383 corrigido manualmente** (texto-âncora trocado).
7. **Blindagem universal `corrigir_ancoras_inconsistentes()` em `util_fonte.py`** + plugada em `motor_publicador.py` e `agente_eleicoes_produtor.py`. **Deployada no Tencent** com backups e MD5 batendo:
   - `7d1d67bf2dd42a3e67c317c5c955dea7  /root/util_fonte.py`
   - `69b2241be36bc71730cad569fb9860db  /root/motor_publicador.py`
   - `d8e416a3b9d093a82dd7b4370d033e9b  /root/agente_eleicoes_produtor.py`
   Backups em `/root/*.bkp-pre-blindagem-20260424_1907`.

### ⚠️ Pendência crítica (Miguel apontou, nem chegou a executar)

**Imagem do #239383 está EDITORIALMENTE ERRADA**: featured_media 239382 = `trend-art-758098c5bb.webp` (1200×1200, sem alt, sem caption) — é arte conceitual da CartaCapital, **não foto de Tarcísio nem de Bolsonaro**. Texto é sobre Centrão articular Tarcísio + isolar Bolsonaro → imagem ideal seria **Tarcísio e Bolsonaro juntos** (preferência explícita do Miguel).

**Script pronto em `/tmp/trocar_imagem_239383.py`** (LOCAL — não rodado ainda). Faz: flickr_live → fallback Flickr API direto → download → upload WP Media → set featured_media. Script já ajustado pra priorizar busca "Tarcísio + Bolsonaro juntos".

### 🛡️ Falha estrutural diagnosticada (anotar no fórum quando voltar)

**Tribunal Visual Gemini não cruzou políticos da pauta com rostos da imagem.** Pauta tinha LULA, TARCÍSIO, EDUARDO BOLSONARO detectados, mas Tribunal aprovou imagem sem rosto reconhecível. Fix proposto: enriquecer prompt do Tribunal com `politicos_esperados` + reprovar se nenhum rosto reconhecível bater.

## Quando retomar

1. **Trocar imagem do #239383** rodando `/tmp/trocar_imagem_239383.py` no Tencent (cuidar com `database is locked` do flickr_live — pode precisar `sudo -u root` ou matar lock antes).
2. **Aplicar lições da §17-§20 do fórum de Eleições no Análise:**
   - Endurecer abertura fisgadora no Pass B (few-shot do padrão "atribuição orgânica no 2º parágrafo").
   - Iterar rewrite de parágrafos longos até 2x (hoje só 1x).
   - Anotar lição "antes de cravar erro factual sobre política recente, cruzar ≥2 fontes do 1º semestre 2026" pro auditor.
3. **Fix estrutural do Tribunal Visual** (cruzar políticos × rostos).
4. **Camada 4.5 imagem** do Análise (flickr_live + Tribunal Visual reforçado + dimensão mínima 1200px + caption obrigatória).

## Pendências antigas que ainda valem

- Tier upgrade da chave Anthropic/OpenAI (Opus 4.7 + GPT-5.5 Pro dão 400/404).
- `MIGUEL_WHATSAPP_ID` no `.env.unificado` pra Mayra notificar.
- Throttle no `coleta_analises_miguel.py` pra evitar WAF.
- Limite de palavras Análise pra 800-1400.
- Camada 5 (distribuição social) ainda não escrita.

## Arquivos importantes a não esquecer

```
LOCAL canônico:
  Projeto Cafezinho Agentes/root/util_fonte.py             (com corrigir_ancoras_inconsistentes)
  Projeto Cafezinho Agentes/root/motor_publicador.py        (blindagem plugada)
  Projeto Cafezinho Agentes/root/agente_eleicoes_produtor.py (blindagem plugada)
  Projeto Cafezinho Agentes/root/analise/                   (Agente Análise completo)
  Projeto Cafezinho Agentes/root/agente_analise.py          (orquestrador)
  Projeto Cafezinho Agentes/root/atualizador_modelos_llm.py
  Projeto Cafezinho Agentes/root/auditar_run_analise.py
  Projeto Cafezinho Agentes/root/auditar_post_eleicoes.py
  Projeto Cafezinho Agentes/root/agent_data_analise/banco_analises_amplo.json (49MB - 7290 análises)

LOCAL temporário (não-deployado):
  /tmp/trocar_imagem_239383.py                              (pendente rodar)
  /tmp/post239383_auditoria.json                            (parecer Grok-4)

TENCENT:
  /root/util_fonte.py                                       (deployado MD5 7d1d67bf...)
  /root/motor_publicador.py                                 (deployado MD5 69b2241b...)
  /root/agente_eleicoes_produtor.py                         (deployado MD5 d8e416a3...)
  /root/*.bkp-pre-blindagem-20260424_1907                   (backups pré-deploy)
```

## Documentação

- `forum_agenteanalise.md` §1-§14 (relatório completo)
- `forum_eleicoes_teste_cruzado_analise_20260424.md` (cross-ref)
- `memory/agente_analise_skeleton_finaflor_20260424.md`
- `memory/agente_analise_1o_teste_real_20260424.md`
- `memory/blindagem_ancoras_universal_20260424.md`
- `memory/sessao_pausada_20260424_1915.md` (este arquivo)
