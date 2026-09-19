# CEREBRO_NODE_BUGS_ATIVOS — VERSÃO LIGHT
> Gerado automaticamente por `cerebro_light.py` em 2026-07-09 03:32 BRT
> Original: `CEREBRO_NODE_BUGS_ATIVOS.md` (113KB) — 53 entradas totais
> Este arquivo é READ-ONLY. Edite sempre o original.

---

## CABEÇALHO ORIGINAL (primeiras linhas)

# CEREBRO_NODE_BUGS — Ativos e em Monitoramento
> Gerado por F3 Reforma Cérebro em 2026-05-24 23:25 BRT
> Origem: `CEREBRO_NODE_BUGS.md` (ORIGINAL INTACTO — este arquivo foi gerado por split)
> Descrição: Bugs 🔴 ATIVO e 🟡 OBSERVAR/MITIGADO — requerem atenção
> Busca: `python3 cerebro.py --buscar <termo>`

---

## BUG-20260623-V3-VISION-DEGRADADA-E-FALHA-CODEX-DIAGNOSTICO — P0 ATIVO

**Detectado:** 2026-06-23 por Miguel, apos cobranca direta sobre Qwen Vision e Gemini Vision no Cafezinho/V3.

**Sintoma:** o Vision do V3 ficou quebrado/degradado no caminho real, mas a resposta operacional inicial tratou testes diretos simples como se provassem o funcionamento do pipeline. Miguel nao foi alertado no momento certo de que Qwen Vision e Gemini Vision precisavam ser testados na rota produtiva completa.

**Causa tecnica:** a chave Qwen anterior nao funcionava corretamente para modelos VL; o cliente V3 ainda dependia de endpoint/base URL e envio de URL remota que falhavam em imagens reais por download remoto/`Content-Length`; o fallback Gemini mascarava a degradacao quando o teste nao passava pelo modulo real.

**Falha Codex registrada:** Codex nao diagnosticou com rigor suficiente. O erro foi aceitar smoke direto/toy como evidencia, em vez de validar primeiro `agente_tribunal_visual_v3.py` com URL real representativa, provider/model final e caminho de fallback. Isso gerou conclusao prematura e falta de alerta a Miguel.

**Correcao aplicada em 2026-06-23:** chave Qwen trocada no Cafezinho sem reproduzir segredo em logs; V3 confirmado lendo a chave nova; `qwen-plus` e `qwen-vl-plus` testados; `agente_tribunal_visual_v3.py` passou a usar `QWEN_BASE_URL_2`, baixar a imagem com headers e enviar `data:image/...;base64` ao Qwen; smoke real do V3 retornou `provider=qwen_dashscope`, `model=qwen-vl-plus`.

**Regra permanente:** nenhum agente pode afirmar "Vision funcionando" so por chamada direta ao provider. Validacao obrigatoria: testar o modulo produtivo exato, com imagem real representativa, registrar provider/model/status/fallback, e avisar Miguel se houver queda para fallback, credencial sem permissao ou divergencia entre teste direto e pipeline real.

**Status:** P0 ATIVO / monitorar 48h. Pendente criar healthcheck automatico Vision V3 e alerta explicito para fallback de provider.

---

## Cabeçalho original (índice/sumário)

# 🐛 CÉREBRO CAMADA 2: Nodo de Bugs e Soluções

Este arquivo pertence à Camada 2 do Grande Cérebro. Ele concentra todos os links para os Fóruns e Memórias relacionados à **depuração, falhas, incidentes e bugs de código**.

> **⚠️ A Regra do Histórico Compartilhado (Antigravity, Claude Code, Codex):**
> É VITAL que as resoluções de bugs feitas por *qualquer* agente sejam registradas aqui para evitar conflitos na trindade.
> 
> **Critério de Promoção para o Índice (Responda SIM a pelo menos uma):**
> 1. O erro pode acontecer de novo?
> 2. Alterou código crítico (crons, roteador, publicação, autocura)?
> 3. Um agente precisará saber dessa decisão no futuro?
> 4. Há risco financeiro ou de segurança envolvido?
> 5. O diagnóstico não era óbvio pelo stack trace?
> *(Se TODAS as respostas forem NÃO, não polua este índice. Deixe apenas no log.)*
> 
> **Ficha Canônica de Registro para Autocura:** <!-- exemplo abaixo, não é entrada real -->
> | ID | Sintoma curto | Detector | Causa provável | Fix/Ação | Link |
> |---|---|---|---|---|---|
> | BUG-EXEMPLO | WP 401 | log publicador | env não carregado | load_dotenv() forçado | [Fórum](./Foruns/forum_exemplo.md) <!-- exemplo -->

> **Regra de Indexação da Autocura:** Toda autocura aplicada ou proposta que envolva publicação, rebaixamento para draft, crons, observadores, Caetano, anti-recusa, duplicatas, placeholders, imagens, failover ou custos deve ter uma ficha curta neste node. Logs brutos ficam em Memórias/Fóruns; aqui fica o mapa cirúrgico para o próximo agente resolver rápido.

---

---

## BUG-20260609-UTIL-HIPERLINK-FONTE-GHOST — 🔴 ATIVO

**Detectado:** 2026-06-09 por Kimi Code CLI (auditoria de fóruns).

**Sintoma:** Posts publicados pelo motor e por agentes individuais (fantástico, sheinbaum, internacionalista, soberania, latam) saem **sem hyperlink externo de fonte** (§95), apesar das camadas 2101/2253 existentes no motor.


---

## ⏩ 48 entradas antigas omitidas
> Para ver o histórico completo, leia `CEREBRO_NODE_BUGS_ATIVOS.md` diretamente.
> Busca rápida: `python3 cerebro.py --buscar <termo>`

---

## ÚLTIMAS 5 ENTRADAS

### Relatório completo
`Foruns/checkup_lote2_kimi.md`

<!-- /CHECKUP-LOTE2 -->

---

---

## QUALIDADE-REDACAO-20260602-ERR01-05 — 🟡 ATIVO (gargalo de titulação/tradução + acabamento)

> Fórum canônico: `Foruns/registro_erros_qualidade_redacao.md`. Detectado no monitoramento §53 por Claude em 2026-06-02; auditoria Codex 17:15 BRT. Produção não foi tocada por Codex nesta etapa.

**Síntese:** em 6 ticks / 27 posts, 5 erros objetivos foram corrigidos pontualmente no WordPress. Nenhum foi vazamento de prompt ou desvio de linha editorial. O padrão dominante é **camada título/tradução/importação**: ERR-03 placeholder de título, ERR-04 Title Case anglófono + sufixo de fonte, ERR-05 idiom traduzido literalmente. ERR-01/02 são acabamento de corpo/grafia.

| ID | Sintoma curto | Detector | Causa provável | Fix/Ação estrutural | Status |
|---|---|---|---|---|---|
| ERR-20260602-01 | Pontu

> *(... 2498 chars omitidos — ler original)*

---

## QUALIDADE-MONITORAMENTO-20260604-LOOP53 — 🟡 PARCIALMENTE MITIGADO

> Relatórios: `Foruns/relatorio_monitoramento_20260604_0230_loop53_24h.md` e follow-up Codex `Foruns/relatorio_monitoramento_20260604_0242_codex_followup_loop53.md`.

**Sintomas do relatório Claude:** `cat=[] + fm=0`, categoria errada, capitalização recorrente, Rússia ausente no redator, temporal possivelmente mal-injetada, duplicata na raiz, timeouts publisher.

**Patch Codex deployado 2026-06-04 02:42 BRT:** `/root/motor_publicador.py` no Tencent ganhou trava de payload mínimo (`publish` sem categoria válida ou `featured_media` vira `draft`), `REGRA_VETO_RUSSIA_SOBERANIA` no redator/revisor/auditor e `REGRA_TEMPORAL_RIGOROSA` explícita nas camadas críticas. Backup remoto: `/root/motor_publicador.py.bak_pre_monitorament

> *(... 413 chars omitidos — ler original)*

---

## QUALIDADE-FLAVIO-20260604-ALUCINACAO-CRUZAMENTO — 🟡 PARCIALMENTE MITIGADO

> Fórum canônico: `Foruns/forum_alucinacao_cruzamento_multi_tema_20260604.md`. Incidente #256252: título/conteúdo fabricaram leitura literal de vídeo-programa da Revista Fórum como se Daniel Vorcaro tivesse delatado Flávio Bolsonaro diretamente.

**Causa raiz confirmada por Claude:** RSS de `/videos/` entrou como pauta factual; Brave estava com chave inválida, DeepSeek caiu por crédito e Qwen-Max caiu por quota; o agente publicou em modo legado quando o validador ficou indisponível.

**Patch Codex deployado 2026-06-04 12:27 BRT:** `/root/agente_flavio_bolsonaro.py` não publica mais sem selo de integridade aprovado. Quando `status_integridade != APROVADO`, o status WP é rebaixado para `pending` por padrão (`draft`

> *(... 836 chars omitidos — ler original)*

---

## QUALIDADE-DEDUPLICACAO-CROSS-AGENTE-20260611 — 🔴 ATIVO (gargalo arquitetural)

> Fórum/contexto: `Foruns/registro_erros_qualidade_redacao.md` (entrada 11/06 11:08 BRT) + `Foruns/relatorio_monitoramento_20260611_loop53_30min.md` (ticks 09:07 + 09:43→10:07).
> Detectado por Claude (Maestro) durante tick §53 09:43 BRT após Miguel autorizar religar pending Flávio.
> Pedido Miguel 11/06 11:09 BRT: "guarda o bug no cerebro para a gente estudar formas de evitar duplicação. vamos aprendendo com o erro."

**Sintoma:** Dois agentes temáticos distintos pegaram a MESMA pauta factual (Estela Aranha/TSE/Aranha sinaliza pressa na análise da ação do PL contra a pesquisa AtlasIntel sobre Flávio Bolsonaro) em janela de 52min e geraram duas matérias publicadas, ambas com Jaccard de título+corpo ≥0.85:

| 

> *(... 2455 chars omitidos — ler original)*

---

## PONTEIROS
- Original completo: [`CEREBRO_NODE_BUGS_ATIVOS.md`](./CEREBRO_NODE_BUGS_ATIVOS.md)
- Índice geral: [`indice_cerebro.json`](./indice_cerebro.json)
- Busca: `python3 cerebro.py --buscar <termo>`
- Validador: `python3 validar_cerebro.py`