---
name: arquitetura-3-camadas-diretrizes
description: Decisão de arquitetura das diretrizes editoriais do Cafezinho — 3 camadas compiladas em 1 fonte + redundância (defesa em profundidade) no pipeline
metadata: 
  node_type: memory
  type: project
  originSessionId: d7137897-dcad-4847-af64-a409ee24938c
---

# Arquitetura de Diretrizes — 3 CAMADAS + fonte única + defesa em profundidade (Miguel 01/06 23:57 BRT)

Decisão fechada com Miguel após co-design. Substitui a bagunça atual (~30 arquivos, 3 sistemas paralelos, motor que ignora a camada nova).

## As 3 camadas (governança — quem muda o quê, quando)

1. **Diretrizes Políticas** — inegociável, editorial (Categoria B anti-imperialista). Só Miguel escreve. Nunca recebe promoção.
2. **Diretrizes de Forma Permanentes** — consolidado, certo. Miguel autoriza mudança.
3. **Diretrizes Provisórias** — em ajuste. Maturidade é **campo de metadado** dentro da camada (`status: em_estudo | maturando`, `entrou_em: data`), NÃO um 4º arquivo.

Precedência **1 > 2 > 3**: camada inferior nunca contradiz a superior; o compilador descarta conflito e loga.

**Promoção (toda com autorização humana):** 3→2 = **2 meses**; dentro da 3, em_estudo→maturando = **mín. 2 semanas**; →1 nunca por promoção. **Só a camada 3 muda automaticamente** no dia a dia (e mesmo assim não pode contradizer 1/2).

**Histórico:** Miguel começou com 4 camadas (separava "quase-permanente" de "em estudo"). Claude argumentou que a 4ª era frágil (mesma natureza, só maturidade diferente → vira metadado). Miguel concordou: **3 camadas**.

## Por que NÃO é o número de camadas que garante respeito

As N camadas **compilam para 1 bloco** no `diretriz_ativa.json`. O agente NUNCA lê 3 arquivos — lê 1 diretriz efetiva. Logo, reduzir/aumentar camadas-fonte não move o respeito; é só governança de edição.

## O que garante respeito de verdade (a aposta da reforma)

1. **Fonte única.** TODO agente — inclusive o `motor_publicador` — lê o MESMO `diretriz_ativa.json` compilado. Fim do "cada agente lê uma diretriz". (Hoje o motor lê o velho `diretrizes_editoriais.py` + `diretriz_geral.json`, e vários agentes têm regra hardcoded no prompt — esse é o real motivo das diretrizes "não pegarem".)
2. **Defesa em profundidade (redundância no pipeline).** A MESMA fonte compilada injetada em cada etapa — nunca cópias soltas que divergem.
   - **Coleta:** Camada 1 (triagem de pauta).
   - **Redação:** Camada 1 + forma (2/3).
   - **Revisão:** Camada 1 + forma.
   - **Fact-check:** Camada 1 (ponto de MAIOR risco editorial — "desmentir crime russo = reproduzir frame imperial").
   - Camada 1 aparece nas 4 etapas; forma só em redação+revisão.
3. **Política em código, forma em prompt.** Camada 1 = injeção **+ check determinístico** no artefato final antes de publicar (reaproveita `REGRA_VETO_IRAN_ALIADOS`, `REGRA_VETO_RUSSIA_SOBERANIA` já existentes). Garantia **forte**, não depende da boa vontade do LLM. Camadas 2/3 (forma) = prompt + malha revisora §90 no pós → garantia **probabilística**, aceitável porque é estilo. Enforcement respeita [[feedback_soltar_posts_nao_prender]]: detecta → corrige → publica, nunca prende.

**Why:** o respeito às diretrizes vinha falhando por roteamento (3 fontes paralelas, motor órfão), não por estrutura. Ver [[project_baseline_banco_midia_s9]] e o caso "revela" [[feedback_revela_nao_e_proibido_e_desejado]].

**How to apply:** ao implementar a reforma (FASES 0-4), entregar os 2 alicerces — fonte única + (política em código / forma em prompt) com redundância nas etapas certas. Camada 1 = Categoria B [[feedback_linha_editorial_anti_imperialista_russia_inegociavel]] (intocável). Qualquer deploy = §92 [[feedback_deploy_gate_92]]. FASE 0 (destravar publicação com sistema ATUAL) vem ANTES da FASE 2 (religar motor à fonte única).

## 🔎 Parecer externo DeepSeek (2026-06-02 04:00 BRT) — 3 ajustes que ENDURECEM o design (não mudam a estrutura)

Pedido por Miguel ("opinião externa não-contaminada", advogado-do-diabo). Veredito: arquitetura sólida, não quebra em ponto fundamental. 3 ajustes incorporados ao desenho:

1. **Camada 1 deve EXCLUIR citações literais do gate determinístico.** O regex de veto (`REGRA_VETO_IRAN_ALIADOS`/`REGRA_VETO_RUSSIA_SOBERANIA`) só pode operar sobre texto GERADO pelo agente, nunca sobre citação. Senão retém matéria anti-imperialista legítima que cita Biden/Israel dentro de uma crítica (caso real: fact-check Perplexity rejeitou matéria sobre Palestina por confundir menção com endosso). **Regra:** excluir blocos em `<blockquote>`/aspas/prefixados por "segundo"/"disse"/"afirmou"; se o regex casar dentro de citação → logar + pedir revisão humana, **nunca reter** (casa com [[feedback_soltar_posts_nao_prender]]). Citação ≠ endosso.

2. **FASE 2 (religar motor) exige SHADOW MODE 7 dias + rollback de 1 comando.** O perigo real não é erro grosseiro (JSON quebrado se blinda com try/except), é **desvio silencioso de tom** — o JSON compila certo mas regras de forma achatam o estilo gradualmente e em ~3 semanas ninguém percebe que o jornal mudou. Blindagem tripla: (a) shadow mode (motor lê o novo JSON, loga diff, NÃO injeta em produção por 7 dias); (b) amostragem semanal de 5 posts antiga×nova; (c) métrica de engajamento — CTR/tempo de leitura cai >10% → rollback. Rollback tem que ser 1 comando (`cp diretriz_ativa.json.bak ...`), nunca recompilar.

3. **Cláusula de governança bug≠diretriz** (ponto novo do DeepSeek). A arquitetura resolve roteamento mas cria **latência de correção**: bug do motor hoje se corrige em 2 min; pelo ciclo de diretrizes (detectar→provisória→quórum→compilar→shadow→ativar) levaria dias. **Regra explícita:** correções de bug (NameError, empty_content, SQL quebrado) NÃO passam pelo ciclo de diretrizes — vão via §92 normal. Só mudança de regra editorial/forma passa pelo ciclo.

DeepSeek confirmou enfaticamente FASE 0 antes de FASE 2 ("inverter é trocar o pneu com o carro andando"). Parecer completo no fórum `forum_diretrizes_provisorias_permanentes_autocorrecao_20260601.md`.
