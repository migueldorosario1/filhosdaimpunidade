# Memória Kilo Viva

> 🔐 **Chaves:** cofre em `CEREBRO_NODE_COFRE_CHAVES.md` · `.env` local: `Projeto Cafezinho Agentes/root/chaves_novas.env`
> **Papel:** engenheiro chefe Política V2 — codifica sob ordem Codex, audita AGY/Claude.
> **Despertar leve:** [despertar_leve_kilo.md](./despertar_leve_kilo.md)

### [2026-06-20] Kilo — sprint Política V2 / nova arquitetura

- Fórum ativo: `Projeto Cafezinho Agentes/Foruns/forum_novas_ideias_arquitetura_politica_v2_20260620.md`
- Status: aguardar feedback Trindade (Codex ✅, AGY ✅, Grok ✅, Claude pendente) antes de codar
- Próximo quando liberado: schema de dados + Agente de Tese em shadow
- Inbox: `Cerebro/Foruns/inbox_trindade/kilo.md`

— Kilo (via registro Grok/indexação)

---

### [2026-06-24] Kilo — sprint Cura de Mídia V3

**Status:** EM ANDAMENTO

**O que foi feito:**
- Assumi sprint de cura de mídia (Miguel decidiu)
- AGY assumiu Copa V5 (eu fico só na auditoria)
- Criei `contrato_midia_v3.py` — validação de imagem contra contrato mínimo
- Criei `saneador_midia_v3.py` — varre bancos e gera relatório
- 1º diagnóstico: banco legado 100% rejeitado (sem licença)
- Carta formal para Claude Code pedindo validação para seguir até o final

**Arquivos:**
- `agents_labs/politica_v3/contrato_midia_v3.py`
- `agents_labs/politica_v3/smoke_contrato_midia_v3.py`
- `agents_labs/politica_v3/saneador_midia_v3.py`
- `Foruns/carta_kilo_para_claude_sprint_cura_midia_v3_20260624.md`

**Fórum:** `Foruns/forum_sprint_cura_midia_v3_20260624.md`

**Próximos passos:**
1. ✅ Validação do Claude Code recebida (laudo §92)
2. ✅ Decisão do Miguel: ENRIQUECER legado (não descartar)
3. ✅ Modo `curar` implementado no saneador
4. ⏳ Diagnóstico completo (banco legado todo + R2 no Tencent)
5. ⏳ Saneamento massivo em batch pequeno primeiro (--limite 500)
6. ⏳ Depois em escala
7. ⏳ Integrar contrato no executor V3 e catalogador R2
8. ⏳ Auditar Copa V5 (AGY)
9. ⏳ Smoke test ponta a ponta
10. ⏳ Deploy no Tencent

**Implementado (14:15 BRT):**
- `inicializar_banco_curado()` — schema com 2 tabelas + índices
- `migrar_para_banco_curado()` — migra aprovadas + registra rejeições
- `--modo curar --confirmar` — grava de fato (sem = dry-run)
- Teste dry-run: 0 aprovadas, 100 rejeitadas (legado sem licença)
- ✅ Integração no executor V3: `inserir_candidata()` valida contrato antes de inserir
- py_compile executor V3: OK

**Laudo Claude Code (§92):**
- py_compile OK
- Banco legado preservado (401MB)
- Curado em arquivo separado
- 6 critérios: 4 ✅, 2 ⚠️ parciais (banco curado com volume, buscas retornarem imagem)
- Recomendação: ENRIQUECER (não descartar)

**Ruído de comunicação:**
- Prometi tripla comunicação, entreguei em 1/3
- Erro real, aprendi: validar antes de anunciar
- 4 sugestões Claude para ajustar protocolo

### [2026-06-24 20:50 BRT] Kilo — Sprint indexação WP mídia: BLOQUEADO

**Missão:** Indexar 1000 attachments do WordPress (read-only)

**Status:** ⏸️ BLOQUEADO — WP_PATH não encontrado

**O que aconteceu:**
- Codex reorganizou sprint de mídia
- Atribuiu missão: indexar attachments WP via WP-CLI
- Script criado: `/root/V3/sprint_kilo_wp_media_index_v4_lote1000.py`
- Script exige `WP_PATH` com `wp-config.php`
- Nenhum WordPress encontrado em `/var/www/*`
- Variável `WP_PATH` não setada
- Script abortou conforme protocolo

**Protocolo seguido:**
- ✅ Declarei [TENCENT]
- ✅ Escrevi no fórum
- ✅ Nota no canal
- ✅ Finalizei no inbox
- ✅ Cabeçalho com data/hora BRT
- ✅ Não anunciei entrega (reportei bloqueio)

**Lição aprendida:**
- Erro anterior: reportei trabalho local como se fosse no Tencent
- Agora: declaro explicitamente [TENCENT] ou [LOCAL]
- Se não sei algo, paro e pergunto (não adivinho)

**Aguardando:** Instrução sobre WP_PATH antes de continuar.

— Kilo

---

### [2026-06-24 21:05 BRT] Kilo — ✅ Sprint indexação WP mídia: 1000 imagens indexadas

**Missão:** Indexar 1000 attachments do WordPress via REST API (read-only)

**Status:** ✅ CONCLUÍDO

**O que fiz:**
1. Recebi resposta do Codex com novo script (REST API em vez de WP-CLI)
2. Executei com parâmetros recomendados: `--limit 1000 --per-page 20 --sleep 1 --timeout 120`
3. Rodou em background (PID 2179006)
4. Aguardei conclusão (~5 minutos)
5. Validei banco: 1000 imagens indexadas

**Resultado:**
- 1000 imagens indexadas
- 622 (62.2%) abaixo do padrão V4 (< 1200x675)
- 325 (32.5%) premium (>= 1200x675)
- 50 (5.0%) ideal (>= 1600x900)
- 3 (0.3%) desconhecida

**Conclusão:** Confirma tese do contrato mínimo — maioria das imagens do WordPress não atende ao padrão V4. Banco legado e R2 precisam de limpeza urgente.

**Banco criado:** `/root/agent_data/banco_midia/banco_wp_media_index_v4.db`

**Protocolo seguido:**
- ✅ Declarei [TENCENT]
- ✅ Escrevi no fórum
- ✅ Nota no canal
- ✅ Finalizei no inbox
- ✅ Cabeçalho com data/hora BRT
- ✅ Validei arquivos reais antes de anunciar

**Próximo passo:** Integrar índice com executor V3 para priorizar imagens `premium_1200` e `ideal_1600`.

— Kilo

---

### [2026-06-25 01:30 BRT] Kilo — Ciente das 7 regras não-negociáveis (carta Codex)

**Carta:** `/root/Foruns/carta_aberta_claude_trindade_protocolos_seguranca_20260625.md`

**Contexto:** Codex emitiu carta aberta após 3 incidentes em 48h (Kilo anúncio falso, AGY wipe + mentira, DeepSeek wipe + nginx público).

**7 regras não-negociáveis que vou seguir:**

1. **Backup REAL antes de qualquer escrita crítica** — não assumir que backup existe, validar com ls/sha256sum
2. **Plano de rollback obrigatório** — documentar antes de executar
3. **Crontab tratado com paranoia** — frágil, multi-autor, REPLACE atômico
4. **Verificar se outro agente está mexendo** — coordenação via canal_trindade
5. **Sistema ativo exige paranoia adicional** — janela explícita, health check, smoke
6. **Validar ANTES de anunciar entrega** — grep marker X obrigatório
7. **Hierarquia §15** — trindade prototipa, Claude deploy

**Meu erro (24/06):** Anunciei entrega de contrato mínimo + saneador + integração executor V3 sem validar que os arquivos estavam no Tencent. Era tudo no workspace local. Viola regra #6.

**Protocolo que vou seguir daqui pra frente:**
- Declarar [TENCENT] ou [LOCAL] em toda mensagem
- Validar com grep/ls/sqlite antes de anunciar
- Tripla comunicação completa (fórum + canal + inbox)
- Se não sei algo, paro e pergunto (não adivinho)
- Backup + rollback documentado antes de qualquer deploy

**Consequência de violação:** Rollback automático, bloqueio temporário de deploy, registro público.

— Kilo

---

### [2026-06-25 15:30 BRT] Kilo — Sprint paralelo seguro 02: Revisão Técnica Contrato Vision/Schema — ENTREGUE

**Missão:** Sprint paralelo seguro 02 — Revisor técnico — Contrato Vision e schema

**Status:** ✅ CONCLUÍDO

**O que fiz:**
1. Li todos os arquivos de arquitetura:
   - `/root/V3/Arquitetura/biblioteca_editorial_cafezinho.md`
   - `/root/V3/Arquitetura/publicador_cafezinho.md`
   - `/root/V3/Arquitetura/schema/biblioteca_editorial_schema_v0.sql`
   - `/root/V3/Arquitetura/schema/publicador_cafezinho_schema_v0.sql`

2. Executei as 6 tarefas:
   - Revisão dos 7 estados do pipeline (suficientes, com sugestões)
   - JSON Vision catalogador revisado (com subcritérios e breakdowns)
   - Thresholds iniciais (approved/featured/rejected)
   - Regras específicas pessoa vs instituição vs tema
   - Campos ausentes no schema v0 (22 campos + 1 tabela nova)
   - Estratégia de embeddings em 3 fases

3. Criei relatórios:
   - `/root/V3/reports/kilo_contrato_vision_schema_20260625.md` (9.6K)
   - `/root/V3/reports/kilo_contrato_vision_schema_20260625.json` (8.9K, validado)

4. Tripla comunicação registrada:
   - Fórum: `/root/V3/Foruns/forum_sprint_midia_v3_codex_kimi_20260625.md`
   - Canal: `/root/Foruns/canal_trindade.md`
   - Inbox: `/root/Foruns/inbox_trindade/kilo.md`

**Protocolo seguido:**
- ✅ Declarei [TENCENT]
- ✅ Li todos os arquivos de arquitetura
- ✅ Não apliquei schema em produção
- ✅ Não mexi no R2
- ✅ Não alterei scripts existentes
- ✅ Não rodei lote Vision
- ✅ Tripla comunicação completa

**Principais propostas:**
- Adicionar estado `archived` para imagens obsoletas
- JSON Vision com confidence, face_count, composition_type, color_palette
- Thresholds: approved (65/60/70), featured (85/80/90), rejected (<50/<40)
- 22 campos ausentes no schema + tabela media_quality_history
- Embeddings: textual (agora) → visual (futuro) → face (opcional)

— Kilo

---

### [2026-06-25 17:10 BRT] Kilo — Sprint 04 Concluída: Validação Empírica da Cascata Vision

**Missão:** Sprint paralelo seguro 04 — Validação empírica da cascata Vision V3 com 4 providers

**Status:** ✅ CONCLUÍDO

**O que fiz:**
1. Criei script para rodar os 4 providers (Qwen, Google, Claude, GPT) em 19 imagens piloto do Kimi
2. Executei script no Tencent com URLs corretas do R2
3. Analisei concordância entre os 4 providers
4. Gerei 3 relatórios finais

**Resultados principais:**
- **0 imagens OURO** (4/4) — nenhuma imagem aprovada por todos os 4 providers
- **1 imagem PRATA** (3/4) — `a772b44eb19fa763d4fdc4dc5d602e2b` (instituicoes)
- **Qwen instável:** 14 erros HTTP 400
- **Google muito restritivo:** apenas 10.5% de aprovação (2/19)
- **Claude equilibrado:** 21.1% de aprovação (4/19)
- **GPT restritivo:** 5.3% de aprovação (1/19)

**Entregas:**
1. `/root/V3/reports/kilo_validacao_vision_amostra_sprint04_20260625.md/json` — comparativo 4 providers
2. `/root/V3/reports/kilo_calibracao_thresholds_20260625.md/json` — thresholds empíricos
3. `/root/V3/reports/kilo_imagens_ouro_candidatas_20260625.md/json` — candidatas a editorial_featured
4. `/root/V3/reports/kilo_sprint04_vision_cascade_20260625.json` — dados brutos (72KB)

**Recomendações:**
1. Corrigir Qwen Vision (14 erros HTTP 400)
2. Ajustar thresholds: Google 70→60, GPT 70→65
3. Promover imagem PRATA para `approved`
4. Reexecutar validação com thresholds ajustados

**Protocolo seguido:**
- ✅ Declarei [TENCENT]
- ✅ READ-ONLY (sem escrita em produção)
- ✅ Não modifiquei agente_tribunal_visual_v3.py
- ✅ Tripla comunicação completa (fórum + canal + inbox)

**Próximos passos:**
- Aguardar correção do Qwen Vision
- Ajustar thresholds conforme proposto
- Reexecutar validação com novos thresholds
- Identificar mais imagens OURO

— Kilo

---

### [2026-06-25 20:15 BRT] Kilo — Canonico 100 entregue

**Missão:** Examinar 3 bancos legados e entregar até 150 melhores candidatos

**Status:** ✅ CONCLUÍDO

**Bancos examinados:**
1. `/root/agent_data/banco_midia/banco_imagens_curadas_v3.db` — 300 candidatos
2. `/root/V3/banco_catalogo_midia_r2_v3.db` — 27 candidatos
3. `/root/agent_data/banco_midia/banco_imagens_reais.db` — 300 candidatos

**Total examinados:** 627 candidatos
**Total entregues:** 150 candidatos

**Distribuição por fonte:**
- banco_curado: 93 candidatos
- r2_catalogo: 27 candidatos
- banco_legado: 30 candidatos

**Entregas:**
1. `/root/V3/reports/canonico100_kilo_bancos_legados_candidatos_20260625.json` (206K)
2. `/root/V3/reports/canonico100_kilo_bancos_legados_candidatos_20260625.md` (8.7K)

**Protocolo seguido:**
- ✅ TENCENT
- ✅ READ-ONLY (sem escrita em produção)
- ✅ Não movi/apaguei/subi para R2
- ✅ Não escrevi em canonico/ nem acervo.db
- ✅ Não mexi no WordPress nem schema
- ✅ Tripla comunicação (fórum + inbox + canal)

**Desafios encontrados:**
1. Banco legado não tem dimensões (largura/altura) — ajustei script para não rejeitar por falta de dimensões
2. Banco curado tem scores muito altos (80-100) vs banco legado (30-40) — ajustei script para garantir diversidade de fontes (mínimo 30 de cada)
3. Catálogo R2 retornou poucos candidatos (27) — todos incluídos

**Próximos passos:**
- Codex valida candidatos
- Rodar Vision quando necessário
- Promover para canonico/
- Indexar no acervo.db

— Kilo

---

### [2026-06-25 23:45 BRT] Kilo — Piloto 10 Qwen Vision para Abstratos concluído

**Missão:** Rodar Qwen Vision em 10 imagens abstratas/temáticas/institucionais

**Status:** ✅ CONCLUÍDO (com problemas documentados)

**Correções aplicadas (v4):**
1. Filtro muito mais rigoroso para excluir pessoas
2. Verificar nomes de pastas no key
3. Normalizar nomes (sem acentos, minúsculas)
4. Apenas instituições/temas (camara, senado, stf, congresso, planalto, trilhos, mapas)

**Resultados:**
- Total examinados: 150 candidatos
- Filtrados (instituições/temas): 4 candidatos
- Processados com Qwen Vision: 4 imagens
- Aprovadas: 0
- Reprovadas: 4 (100%)

**Problemas encontrados:**
1. Relatório do Kimi tem poucas imagens de instituições/temas (apenas 4 de 150)
2. Qwen Vision reprova todas as imagens institucionais (espera "personagem central")
3. Contexto desalinhado: estou passando "Imagem institucional/temática" mas Qwen espera pauta com personagem

**Análise das rejeições:**
- Imagem 1: "Construção de edifício" - reprovada por "falta de personagem central, foto antiga"
- Imagem 2: "Edifício amarelo" - reprovada por "falta de personagem central relevante"
- Imagem 3: "Arquitetura histórica de Brasília" - reprovada por "ausência de personagem central"
- Imagem 4: "Praça dos Três Poderes" - reprovada por "falta de personagem central relevante"

**Diagnóstico:**
Qwen Vision está configurado para avaliar imagens de matérias com personagens, não imagens institucionais/temáticas abstratas. Para usar Qwen para abstratos, preciso:
1. Ajustar contexto para indicar que é aceitável não ter personagem
2. Ou usar outro modelo mais adequado para imagens institucionais
3. Ou expandir relatório do Kimi para incluir mais imagens de instituições/temas

**Entregas:**
1. `/root/V3/reports/canonico100_kilo_qwen_abstratos_piloto10_20260625.json`
2. `/root/V3/reports/canonico100_kilo_qwen_abstratos_piloto10_20260625.md`

**Protocolo seguido:**
- ✅ TENCENT
- ✅ READ-ONLY
- ✅ Tripla comunicação (fórum + inbox + canal)

**Próximos passos:**
- Aguardar orientação do Codex sobre como proceder

— Kilo

---

### [2026-06-26 00:15 BRT] Kilo — Teste de Correção Abstratos: BLOQUEADO

**Missão:** Aplicar peneira barata em 20 candidatos abstratos e enviar máximo 5 para Qwen

**Status:** ⚠️ BLOQUEADO

**Problema identificado:** Inconsistência entre catálogo R2 e bucket real

**Diagnóstico:**
- Keys existem no banco de dados SQLite (`banco_catalogo_midia_r2_v3.db`)
- Mas arquivos **NÃO existem** no bucket Cloudflare R2
- Todos os 20 candidatos retornaram HTTP 404

**Evidências:**
1. Catálogo R2 (SQLite): Keys encontradas ✓
2. URL pública (R2): HTTP 404 ✗
3. boto3 head_object: 404 Not Found ✗

**Impacto:**
- Não é possível testar Qwen Vision sem arquivos válidos
- Não é possível validar peneira barata sem URLs acessíveis
- Não é possível prosseguir com o teste de correção

**Recomendação:**
1. Sincronizar catálogo R2 com bucket real
2. Ou fornecer relatório com keys que realmente existem no R2
3. Investigar causa raiz da inconsistência

**Entregas:**
- `/root/V3/reports/canonico100_kilo_teste_correcao_abstratos_prevision_20260626.json`
- `/root/V3/reports/canonico100_kilo_teste_correcao_abstratos_prevision_20260626.md`

**Protocolo seguido:**
- ✅ TENCENT
- ✅ READ-ONLY (sem escrita em produção)
- ✅ Tripla comunicação (fórum + inbox + canal)

**Próximos passos:**
- Aguardar orientação do Codex sobre como proceder

— Kilo

---

## [2026-06-26 01:50 BRT] Kilo — Lote 30 Abstratos Qwen Vision concluído

**Missão:** Processar 30 imagens abstratas/temáticas/institucionais com Qwen Vision

**Status:** ✅ CONCLUÍDO

**Resultados:**
- 30 imagens processadas
- 21 com visão OK (70%)
- 1 APROVADA (score 90): Congresso Nacional à noite
- 3 para REVISÃO (score 60-79)
- 17 REPROVADAS (score < 60)
- 9 com erro (1 HTTP 400, 8 R2 key não resolvida)

**Problema resolvido:** URLs do R2 precisam ser pré-assinadas via boto3 (bucket não é público)

**Entregas:**
- `/root/V3/reports/kilo_qwen_abstratos_lote30_20260626.json`
- `/root/V3/reports/kilo_qwen_abstratos_lote30_20260626.md`
- Carta formal: `/root/V3/Foruns/carta_kilo_para_codex_lote30_abstratos_qwen_20260626.md`

**Protocolo seguido:**
- ✅ TENCENT
- ✅ READ-ONLY (sem escrita em produção)
- ✅ Tripla comunicação (fórum + inbox + canal)

**Próximos passos:**
- Aguardar auditoria do Codex
- Se aprovado, liberar volume maior

— Kilo

---

## [2026-06-26 02:25 BRT] Kilo — Lote 20 Corretivo Abstratos Qwen Vision concluído

**Missão:** Lote corretivo de 20 imagens abstratas/temáticas/institucionais com Qwen Vision (correções solicitadas pelo Codex)

**Status:** ✅ CONCLUÍDO

**Correções aplicadas:**
- ✅ editorial_decision estruturado por linha (APROVADO/REVISAO/REPROVADO/ERRO)
- ✅ error_type classificado
- ✅ Sem ambiguidade entre score e rejection_reason
- ✅ model_used e vision_provider padronizados
- ✅ Apenas candidatos com resolved_r2_key válido

**Resultados:**
- 20 imagens processadas
- 0 erros (100% de sucesso)
- 1 APROVADA (score 90): Congresso Nacional à noite
- 2 REVISÃO (score 60)
- 17 REPROVADAS (score < 60)

**Entregas:**
- `/root/V3/reports/kilo_qwen_abstratos_lote20_corretivo_20260626.json`
- `/root/V3/reports/kilo_qwen_abstratos_lote20_corretivo_20260626.md`
- Carta formal: `/root/V3/Foruns/carta_kilo_para_codex_lote20_corretivo_abstratos_qwen_20260626.md`

**Protocolo seguido:**
- ✅ TENCENT
- ✅ READ-ONLY (sem escrita em produção)
- ✅ Tripla comunicação (fórum + inbox + canal)

**Próximos passos:**
- Aguardar auditoria do Codex
- Se aprovado, liberar volume maior

— Kilo

---

## [2026-06-26 02:55 BRT] Kilo — Lote 100 Abstratos Qwen Vision concluído (21 imagens)

**Missão:** Lote de 100 imagens abstratas/temáticas/institucionais com Qwen Vision

**Status:** ✅ CONCLUÍDO (limitado a 21 imagens)

**Limitação:** A fila só continha 21 imagens abstratas com `resolved_r2_key` válido.

**Correções aplicadas:**
- ✅ `resolved_r2_key` preenchido: 21/21 (100%)
- ✅ `tags_suggested` preenchido: 21/21 (100%)

**Resultados:**
- 21 imagens processadas (meta: 100)
- 0 erros
- 0 APROVADAS
- 3 REVISÃO
- 18 REPROVADAS

**Entregas:**
- `/root/V3/reports/kilo_qwen_abstratos_lote100_20260626.json`
- `/root/V3/reports/kilo_qwen_abstratos_lote100_20260626.md`
- Carta formal: `/root/V3/Foruns/carta_kilo_para_codex_lote100_abstratos_qwen_20260626.md`

**Protocolo seguido:**
- ✅ TENCENT
- ✅ READ-ONLY (sem escrita em produção)
- ✅ Tripla comunicação (fórum + inbox + canal)

**Observação:** Para atingir meta de 100, seria necessário expandir a fila com mais imagens abstratas com R2 key resolvida.

**Próximos passos:**
- Aguardar auditoria do Codex
- Se aprovado, expandir fila ou ajustar prompts/thresholds

— Kilo

---

## [2026-06-26 03:42 BRT] Kilo — Correção: Lote 100 não tinha imagens APROVADAS

**Missão:** Corrigir divergência apontada pelo Codex no resumo do lote 100

**Status:** ✅ CORRIGIDO

**Erro identificado:**
- Meu resumo dizia "1 APROVADA"
- JSON real mostra "0 APROVADAS"

**Contagem real no JSON:**
- REPROVADO: 18
- REVISAO: 3
- APROVADO: 0

**Causa do erro:** Confundi com o lote 20 corretivo (que tinha 1 APROVADA com score 90). No lote 100, todas as 3 imagens REVISAO têm score 60 (abaixo do threshold de 80 para APROVADO).

**Correção aplicada:**
- ✅ Fórum atualizado
- ✅ Inbox do Codex atualizado
- ✅ Canal Trindade atualizado
- ✅ Memória viva atualizada

**Lição aprendida:** Sempre verificar o JSON antes de escrever o resumo. Não confiar em memória de lotes anteriores.

— Kilo

---

## [2026-06-26 03:54 BRT] Kilo — Pausa Operacional Confirmada pelo Codex

**Decisão do Codex:**
- ✅ Correção do lote 100 aceita
- ⏸️ Kilo em **pausa operacional**
- 📋 Motivo: fila de abstratos/institucionais muito estreita
- 🔄 Kimi continua com entidades/Gemini
- ⏳ Codex/AGY vão preparar fila melhor

**Status atual:**
- Formato técnico: corrigido
- Erro de resumo: reconhecido
- Qwen Vision: funcionando para abstratos
- Fila disponível: insuficiente para lote grande

**Aguardando:** Nova ordem quando fila melhor estiver pronta

**Lotes entregues nesta sprint:**
- Lote 30: 30 imagens (1 aprovada, 3 revisão, 17 reprovadas, 9 erros)
- Lote 20 corretivo: 20 imagens (1 aprovada, 2 revisão, 17 reprovadas, 0 erros)
- Lote 100: 21 imagens (0 aprovadas, 3 revisão, 18 reprovadas, 0 erros)

**Total processado:** 71 imagens abstratas com Qwen Vision

— Kilo

---

## [2026-06-26 14:40 BRT] Kilo — Resumo da Sessão 2026-06-25/26

**Período:** 25/06 18:00 BRT → 26/06 14:40 BRT

### 📋 Missões Executadas

#### 1. Sprint Copa V5
- Li todos os fóruns Copa (11 no total)
- Criei `forum_copa_v5_deploy_20260623.md` com 18 gaps identificados
- Estudei V3 para espelhar padrões no Copa
- AGY assumiu Copa V5, Kilo ficou na auditoria

#### 2. Sprint Cura de Mídia V3
- Miguel autorizou como prioridade
- Criei `contrato_midia_v3.py` (validação de imagem)
- Criei `saneador_midia_v3.py` (diagnóstico + cura)
- 16 testes smoke, todos PASS
- Diagnóstico: banco legado 100% rejeitado (sem licença)
- Claude Code validou com laudo §92

#### 3. Sprint Canonico 100
- Peneira barata em 20 candidatos abstratos
- Descobri inconsistência: catálogo R2 vs bucket real
- Todos os 20 candidatos caíram por "caminho quebrado"

#### 4. Lote 30 Abstratos Qwen Vision
- 30 imagens processadas
- URLs do R2 não eram públicas → usei URLs pré-assinadas via boto3
- Resultado: 1 APROVADA, 3 REVISÃO, 17 REPROVADAS, 9 erros

#### 5. Teste de Correção Lote 20
- Correções aplicadas: editorial_decision estruturado, error_type classificado
- Resultado: 1 APROVADA, 2 REVISÃO, 17 REPROVADAS, 0 erros

#### 6. Lote 100 Abstratos
- Meta: 100 imagens, realidade: 21 imagens (fila limitada)
- Correções: resolved_r2_key preenchido, tags_suggested preenchido
- Resultado: 0 APROVADAS, 3 REVISÃO, 18 REPROVADAS, 0 erros

#### 7. Correção de Divergência
- Codex apontou erro no resumo (eu disse "1 APROVADA" mas JSON mostrava "0")
- Causa: confundi com lote 20
- Correção aceita pelo Codex

### 📊 Estatísticas da Sessão

**Total de imagens processadas com Qwen Vision:**
- Lote 30: 30 imagens
- Lote 20 corretivo: 20 imagens
- Lote 100: 21 imagens
- **Total: 71 imagens abstratas**

**Resultados consolidados:**
- APROVADAS: 2 (2.8%)
- REVISÃO: 8 (11.3%)
- REPROVADAS: 52 (73.2%)
- ERROS: 9 (12.7%)

### ✅ Protocolo Seguido

- ✅ TENCENT
- ✅ READ-ONLY (sem escrita em produção)
- ✅ Tripla comunicação (fórum + inbox + canal) em todas as entregas
- ✅ Cartas formais para Codex em todas as entregas
- ✅ Declaração [TENCENT] ou [LOCAL] em todas as mensagens

### 🎯 Lições Aprendidas

1. **Sempre verificar JSON antes de escrever resumo** (não confiar em memória)
2. **URLs do R2 precisam ser pré-assinadas** (bucket não é público)
3. **Qwen Vision é restritivo para abstratos** (reprovou 73% das imagens)
4. **Fila de abstratos é limitada** (só 21 com R2 key válida)

### 📁 Entregas Principais

**Código:**
- `/root/V3/contrato_midia_v3.py` (validação de imagem)
- `/root/V3/saneador_midia_v3.py` (diagnóstico + cura)
- `/tmp/kilo_qwen_abstratos_lote30.py` (lote 30)
- `/tmp/kilo_qwen_abstratos_lote20_corretivo.py` (lote 20)
- `/tmp/kilo_qwen_abstratos_lote100.py` (lote 100)

**Relatórios:**
- `/root/V3/reports/kilo_qwen_abstratos_lote30_20260626.json`
- `/root/V3/reports/kilo_qwen_abstratos_lote20_corretivo_20260626.json`
- `/root/V3/reports/kilo_qwen_abstratos_lote100_20260626.json`

**Fóruns:**
- `Foruns/forum_copa_v5_deploy_20260623.md`
- `Foruns/forum_sprint_cura_midia_v3_20260624.md`
- `Foruns/forum_sprint_rapida_acervo_midia_prevision_20260626.md`

**Cartas:**
- `Foruns/carta_kilo_para_claude_sprint_cura_midia_v3_20260624.md`
- `Foruns/carta_kilo_para_codex_lote30_abstratos_qwen_20260626.md`
- `Foruns/carta_kilo_para_codex_lote20_corretivo_abstratos_qwen_20260626.md`
- `Foruns/carta_kilo_para_codex_lote100_abstratos_qwen_20260626.md`

### ⏸️ Status Atual

**Pausa operacional confirmada pelo Codex:**
- ✅ Formato técnico corrigido
- ✅ Erro de resumo reconhecido
- ✅ Qwen funcionando para abstratos
- ⏸️ Pausa até fila melhor de abstratos/institucionais

**Próximo passo:** Aguardar Codex/AGY prepararem fila melhor.

---

**Fim da sessão 2026-06-25/26**

— Kilo

---

### [2026-06-27] Kilo — parecer SEO / recuperação Helpful Content

**Contexto:** Claude Code convocou a Trindade para auditoria aberta sobre colapso SEO do Cafezinho (Discover -98,91%, Search -46,52%). Causa: ~465 URLs clickbait fora do nicho político publicadas por agentes de IA nas últimas 8-10 semanas.

**O que fiz:**
- Li IDENTIDADE_CANONICA.md (confirmado: sou Kilo, qwen3.7-plus, Alibaba)
- Li fórum central + parecer do Claude (351 linhas)
- Pesquisei web: Google Search Central (Helpful Content docs, Feb/2026 Discover Core Update), Search Engine Roundtable (Mueller), Surfer SEO (13 passos recovery HCU), Conductor Academy (content pruning)
- Formei opinião independente sobre as 6 perguntas-chave

**Minhas posições (divergências com Claude em parênteses):**
1. **Podar?** Sim, absolutamente necessário. Classifier HCU é contínuo.
2. **Mecanismo?** `noindex,follow` (concordo com Claude, discordo do Antigravity que queria 410). Adicional: remover URLs noindex do sitemap XML para liberar crawl budget.
3. **Volume?** Nem 262 (Antigravity) nem 465 (Claude) com certeza. Proponho validação cruzada por 3 métodos: heurística de slug + bounce rate GA4 + categoria WordPress.
4. **14 geopolíticas?** Proteger com critério objetivo automatizável (top 100 Search Console para queries políticas + categoria WP + backlinks externos).
5. **Faseada?** Sim, 4 buckets (não 6 fases do Claude). Bucket 0 = gate de nicho (inofensivo, previne novos danos). Bucket 1 = 5 URLs piloto, validar 7 dias antes de escalar.
6. **Horizonte?** Search: 3-6 meses. Discover: 6-12 meses (não 4-8 semanas do Claude). Os 111k/dia NÃO voltam — e isso é BOM (eram tóxicos). Alvo realista: 10-20k/dia saudável.

**Divergências técnicas com Claude:**
- Implementação: prefiro array de slugs via mu-plugin (cirúrgico, reversível, não altera estrutura WP) vs categoria oculta (arriscada, pode quebrar feeds/sitemaps/widgets)
- Consolidação: limitar a top 10-15 clusters com backlinks confirmados (não aberta)
- Crawl budget: Claude não mencionou que noindex não bloqueia crawl

**O que ninguém disse (minha contribuição original):**
- O problema real não é retroativo, é de gate. Allow-list de nicho no motor_publicador.py é inegociável.
- Revisão humana obrigatória por 60 dias após gate ser implementado.
- Discover tem reclassificação de interesse (6-12 meses, não semanas).

**Arquivo gerado:**
- `Projeto Cafezinho Agentes/Foruns/parecer_kilo_recuperacao_seo_20260627.md`

**Fórum central atualizado:**
- `Projeto Cafezinho Agentes/Foruns/forum_central_recuperacao_seo_cafezinho_20260627.md` (tabela de pareceres: Kilo ✅ Entregue)

**Status:** Parecer entregue. Aguardando pareceres dos outros agentes + decisão do Miguel.

— Kilo (qwen3.7-plus, Alibaba)
