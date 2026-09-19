---
name: Fixes editoriais aplicados 2026-04-17 (parágrafos + militar + turismo)
description: Três fixes deployados de uma vez — parágrafos 2-3 frases no motor_publicador, curadoria militar endurecida, prompt turismo reescrito. Tasnim News desativado.
type: project
originSessionId: b8d23953-06f2-4699-9a68-275c279163e9
---
Deploy 2026-04-17 16:04 BRT resolvendo as 3 pendências editoriais diagnosticadas no dia:

**1. `motor_publicador.py` linha 216 — Regra de parágrafos**
- Antes: "Quebre ou una parágrafos com mais de 2 frases" (ambíguo).
- Depois: "Cada parágrafo DEVE ter exatamente 2 ou 3 frases curtas — padrão Financial Times. PROIBIDO parágrafo de frase única (exceto o lead). PROIBIDO 4+ frases (quebre em dois)."
- Afeta TODA a Trindade Editorial (master_trends, master_nacional, master_geopolitica) e qualquer agente que passe pelo motor_publicador. Foi motivado pelo post 235789 (rio Colorado) que tinha 4 parágrafos de 1 frase.

**2. `robo_coleta_militar.py` — Curadoria endurecida**
- CRITERIOS_SCORE reescrito com "SE O EIXO 1 DER ZERO, NÃO SOME O EIXO 2 — score=0". Lista explícita de temas que recebem ZERO automático: política interna, economia não-bélica, diplomacia sem armamento, imigração, saúde, esporte, cultura, threads de redes sociais, veto UE, celebrações religiosas.
- REGRAS_APROVACAO idem — lista explícita de AUTOMATICAMENTE REPROVADOS alinhada com as do CRITERIOS.
- IMPORTANTE: o cutoff global em `motor_coletor.py` segue `if score < 1.0: return None`. Não subi esse cutoff (o Miguel tem política documentada de "não guilhotinar na coleta, ordenar por score e confiar no fact-check final"). A estratégia é fazer o LLM dar ZERO mesmo em off-topic — o prompt agora rejeita categoricamente.
- Também desativado `Tasnim News (Irã)` em `/root/agent_data/fontes_militar.json` (DNS fail constante do IP Tencent).

**3. `agente_turismo_embratur.py` — Prompt jornalístico puro + capitalização**
- Reescrito `redigir_pt()` removendo "otimista", "chamativa", "cativante", "deslumbrante" do system e user prompt.
- Novo prompt exige: formato `[Sujeito] + [Verbo forte] + [Fato específico]`, sentence case PT-BR, zero adjetivos vagos (lista proibida: deslumbrante, paradisíaco, imperdível, definitivo, maravilhoso, incrível, único, espetacular, mágico, encantador), zero exclamação.
- Inclui exemplos concretos de "bons" (Chapada Diamantina +42% visitação) e "ruins" (os 4 títulos reais publicados em 17/04: Paraíso das Águas, Brasil no Topo do Mundo, Sob a Luz das Estrelas, Padrão Ouro da Hospitalidade).
- Importa `titulo_utils.corrigir_capitalizacao_titulo` e aplica no `title` antes de retornar — garantia de última milha mesmo se o LLM errar.
- Corpo agora exige 2-3 frases por parágrafo (alinhado com o fix do motor_publicador).

**Backups:** `.bak_20260417_1604` para os 3 arquivos no servidor.

**Why:** Miguel autorizou consertar "tudo" depois dos fixes do YouTube+Crime. Os 3 problemas foram diagnosticados durante o dia mas esperando autorização.

**How to apply:** Para verificar o resultado, monitorar próximas execuções: (a) master_trends `0,30 * * * *` — os parágrafos devem ter 2-3 frases; (b) coletor militar `8,38 * * * *` — logs devem mostrar MENOS matérias aprovadas e com score mais alto; (c) agente_turismo rodando periodicamente — títulos devem vir em sentence case PT-BR sem adjetivos vagos.
