---
name: Fix parser Fantástico + blacklist Analytics — 2026-04-20
description: Fantástico rejeitava 100% dos candidatos silenciosamente porque LLM respondia tudo numa linha e o parser não pegava. Analytics travava no mesmo artigo Grandes Lagos — agora tem blacklist por falhas consecutivas.
type: project
originSessionId: c4ce2046-925d-4cef-9df8-6970e904a43e
---
**Deployado 2026-04-20 ~11:50 BRT em Cingapura.**

## Bug A — Fantástico rejeita 100% silenciosamente

**Sintoma:** Desde ~07h UTC o `agente_fantastico.py` começou a não publicar nada. Log dizia `❌ Nenhum candidato aprovado pela auditoria LLM` sem nenhum `DESCARTADO` individual.

**Causa raiz:** gpt-4o-mini (usado como Fantástico Auditor) começou a responder as 14 avaliações **tudo numa linha única**, sem quebras `\n` entre elas. Exemplo real capturado:

```
NOTA: 60 | VEREDITO: PUBLICAR | MOTIVO: ... NOTA: 30 | VEREDITO: DESCARTAR | MOTIVO: ... NOTA: 70 | ...
```

O parser fazia `resultado.strip().split('\n')` → 1 linha única. Aí `line.split('NOTA')[0]` era string vazia → `idx_str = '0'` (fallback) → `idx = -1`. Como `if 0 <= idx < len(candidatos)` falha pra -1, caía no else silencioso. **8 PUBLICAR eram perdidos por rodada.**

**Fix em `agente_fantastico.py` linha ~220:**
1. Parser robusto: se só vier 1 linha com múltiplos `NOTA:`, parte por regex `re.split(r'(?=NOTA:\s*\d)', resultado)` mantendo cada bloco como "linha lógica".
2. Índice: tenta extrair `[N]` explícito; senão usa posição sequencial.
3. Regex isolada pra NOTA, VEREDITO e MOTIVO — tolerante a espaços e case.
4. Prompt reforçado com regras explícitas de formato: "Cada avaliação em NOVA LINHA", "SEMPRE inclua [número] em colchetes", "NUNCA cole duas na mesma linha".

**Validação empírica:** 10 candidatos → 4 aprovados (40% taxa), logs de APROVADO/DESCARTADO detalhados por item.

## Bug B — Analytics trava no artigo Grandes Lagos

**Sintoma:** Agente tentava há muitas horas gerar spin-off do mesmo artigo ("Arqueólogos desvendam estruturas submersas de 9 000 anos nos Grandes Lagos", 9056 views). Brave Search trazia apenas 1 candidato fraco e auditoria sempre rejeitava. Loop infinito.

**Causa raiz:** o `_filtrar_cooldown` só removia artigos que **já tinham gerado spin-off publicado**. Se o artigo falhava na auditoria, o cooldown não o bloqueava, e como ele tem views atípicas (outlier), o `random.choices(weights=views)` quase sempre cai nele.

**Fix em `agente_analytics_v9.py`:**
1. Novo arquivo de estado: `/root/agent_data/analytics_tentativas_falhadas.json`
2. Helpers: `_carregar_tentativas`, `_esta_bloqueado`, `_registrar_falha`, `_limpar_falhas_do_titulo`, `_chave_titulo` (normaliza com `unicodedata.NFKD` pra remover acentos antes do regex).
3. Constantes: `MAX_TENTATIVAS_ANTES_BLOQUEIO = 3`, `DURACAO_BLOQUEIO_HORAS = 24`.
4. Integração:
   - `_filtrar_cooldown` agora pula títulos bloqueados (log `⏳ Pulando (bloqueado por falhas)`).
   - `run_analytics` chama `_registrar_falha(titulo_campeao)` quando Brave retorna vazio OU quando auditoria rejeita tudo.
   - Após `_registrar_falha` acumular 3 tentativas, seta `bloqueado_ate = now + 24h` e loga `🚫 Artigo bloqueado`.
   - Após publicação bem-sucedida, chama `_limpar_falhas_do_titulo` — resetta contador.

**Estado inicial aplicado:** o artigo Grandes Lagos foi seedado com `bloqueado_ate = 2026-04-21T14:47Z` pra pular imediatamente (sem esperar 3 ciclos reincidirem). Próximo cron do Analytics (`:45 * * * *`) escolherá outro.

**Validação:** função `_esta_bloqueado` retorna True pro Grandes Lagos; retorna False pros outros 28 posts do pool.

## Arquivos modificados
- `root/agente_fantastico.py` — parser robusto + prompt reforçado (+50 linhas)
- `root/agente_analytics_v9.py` — blacklist completa + integração nos 3 pontos (+80 linhas)

## Comportamento esperado nas próximas horas
- Fantástico: próximo cron (`:05 * * * *` ou `9,15,21h` conforme crontab) deve voltar a publicar 1x/dia quando achar tema forte.
- Analytics: cron `:45 * * * *` da próxima hora escolherá artigo diferente (o mais votado sem blacklist). Se a nova escolha também falhar 3x, também é bloqueada. Progressivamente o sistema vai rotacionar entre artigos até achar um que gere spin-off.
