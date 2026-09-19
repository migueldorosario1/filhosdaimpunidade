# 🎬 Fórum — AGENTE YOUTUBE CLÁSSICO RESTAURADO no canônico + régua de título EMU-6 em toda a linha (03/09/2026, manhã)

> Ordem do Miguel (~06:5x BRT, chat): a vertical V4.1 YouTube do espelho "está horrível" → **desativar**; o agente YouTube clássico do canônico "estava ótimo" → **reativar draft-only, sem mutilar**, aproveitando o que há de bom (pode usar GPT 5.6 Sol); títulos "estão feios" → achar o prompt errado e consertar **para todos** (título não é resumo: 1 fato, direto, sem ambiguidade). Complemento da ponte: caso-escola 268424 + bolo EMU-6 (`cerebro/Estilo/BLOCO_PRONTO_REGRA_TITULO_EMU6.md`) + ZD-20260903-001 (injetar no v41_ciclo + R2).

## Decisões executadas

1. **Vertical V4.1 YouTube do espelho DESATIVADA** — cron do alimentador comentada no tencent (`# DESATIVADO_20260903_ZM`, backup `crontab.bak_pre_desativa_vertical_espelho_20260903`). A reescrita "ultra-luxo" do materializador (tese/vilão forçados + regra de título restritiva) saiu do ar; está preservada em `.bak_minha_vertical_desativada_20260903`.
2. **Agente YouTube CLÁSSICO restaurado no canônico (draft-only)** — base = `bak_pre_vertical_luxo_nomes` (a versão clássica com Sol, intacta). Prompt clássico neutro preservado; redator = **GPT 5.6 Sol** (escada de luxo já embutida). Enxertos mínimos aprovados: (a) régua de título EMU-1+2+6; (b) NOMES SEM ERRO/personagens (ordens antigas do Miguel 16/08 e 25/08 — "identificava os personagens"). Cron 11h/17h já estava vivo e o publicador posta **draft no canônico** (controle.ocafezinho.com) — ou seja, o clássico volta a produzir rascunhos já na corrida das 11h.
3. **Régua EMU-6 injetada em TODA a linha de título**: redator V4.1 (briefing do `v4_vertical_draft_worker.py`, NYC) · revisor R2 (tencent, regra velha dos "~90 caracteres" substituída) · materializador YouTube clássico · revisores DSN + Loop Laura (já cobertos pela sessão us65 com o bolo verbatim). Diagnóstico do que azedou: a regra de título pedia UMA frase sem dois-pontos e poucos caracteres, e o modelo respondia ESPREMENDO a matéria inteira numa linha — o bolo EMU-6 ataca a causa (título = porta, não resumo; agente concreto + ação com objeto completo + teste "entendi sem ler?").
4. **Espelho = laboratório dos 2 experimentos** (Miguel examina): blocos/categorias **Estatística (id 100005)** e **Investimento (id 100007)** já existem no cafezinho.news — nada a criar. Monitoramento segue pela vigília da casa (Chefe/DSC) + meus relatórios.

## Provas

- `py_compile` OK nos 3 arquivos tocados (materializador restaurado, worker, R2); backups datados em todos.
- SHA materializador restaurado: `c7f2602f91f49efc`; bolo presente (grep positivo) nos 3 prompts.
- Caso-escola injetado em todos: ❌ «EUA barram robôs e drones, mas China mantém escala» → ✅ «Governo Trump barra importação de drones e robôs da China».

## Rollback

- Vertical espelho: descomentar a linha do alimentador (backup crontab no tencent).
- Materializador: `cp .bak_minha_vertical_desativada_20260903` de volta (minha versão) ou `bak_pre_luxo` (clássico puro).
- Worker/R2: `cp .bak_pre_bolo_emu6_20260903` de volta em cada um.

## O que falta

- 1ª corrida do clássico restaurado: hoje 11h BRT — conferir o rascunho (título na régua nova? personagens certos?) e reportar.
- Se o Miguel quiser, o mesmo bolo pode ir ao orquestrador dos temáticos (fora do escopo desta ordem).

— ZCode/Kimi K3 (ZM, Dell) · 03/09/2026 07:4x BRT

---

## Adendo ~07:2x BRT (03/09) — auditoria de títulos pós-publicação + saúde dos coletores (pedido do Miguel)

**Títulos publicados hoje no canônico (12 últimos, TODOS anteriores à injeção EMU-6 das ~07:0x):** a maioria já boa — ✅ 268731 («Anvisa suspende fabricação de produtos da Unilever em Vinhedo»), 268714 («Governo Trump apoia OpenAI…» — já no padrão agente concreto), 268717, 268723, 268700, 268742, 268740 (cargo+nome correto), 268744 · 🟡 limítrofes: 268739 («…com a assinatura da Índia» ambíguo), 268734 («cautela evitou anular os inquéritos do Master» — "Master" solto), 268730 (duas causas concatenadas), 268727 («hostilização» = escolha de palavra). Nenhum no nível do desastre 268424; a régua nova pega exatamente esses limítrofes.

**Geopolítica ESTÁ publicando** (resposta ao "vamos voltar a publicar geo"): 3 posts no ar só nesta manhã — 268717 (Índia-Rússia, 03:17), 268739 (SCO/Irã, 06:07), 268744 (Kim Jong Un, 07:02) — e a fila segue gorda (1.280 candidatas new; 263 novas nas últimas 24h).

**Coletores (a equipe montada 02/09-03/09): TODOS VIVOS** — cron */15 ativo; os 6 módulos rodaram ~07:0x BRT (estado.json); provas 24h: nacional_direto **319 colhidas** · enriquecedor 6 materiais brutos montados · geo 263 novas (China/BRICS fluindo: Prensa Latina, Al Jazeera, RT) · tec/IA 5 novas (fila 24; vertical mais magra por natureza) · prospector 16 feeds ativos. ⚠️ observado: multilíngue duplicou 1 item Al Jazeera (fonte com e sem prefixo "ingles:") — dedupe entre módulos a observar; sem ação agora (não quebra nada).

---

## Adendo ~07:4x BRT (03/09) — IA/TECNOLOGIA INTERNACIONAL no ar (V41_TEC_MULTIIDIOMA_20260903) + automação do monitor travada no Kimi

**Ordem do Miguel (~07:2x):** "IA não precisa ser português — é até besteira. Vamos usar canais internacionais, em chinês, em inglês, em todas as línguas" + "mantenha o KIMI aqui — voltou o QWEN, droga, você não consegue mexer nisso não?".

1. **Módulo TEC-MULTIIDIOMA no ar** (mesmo robô, mesma física fail-open do multilíngue geo): 19 feeds internacionais de tecnologia/IA — EN (TechCrunch, The Verge, Ars Technica, Wired, MIT Tech Review, VentureBeat AI, The Register, Rest of World, ZDNet) · 中文 (36氪, QbitAI 量子位, 少数派, TechNode, InfoQ中文) · DE (Heise, Golem) · ES (Xataka) · FR (Numerama) · JP (ITmedia) · RU (Habr). Grava na vertical ciencia_tecnologia_ia (`source_type=multi_tec_intl`), régua ≥800 chars, curadoria com nota. Canaltech/fontes PT deixam o papel principal (seguem entrando pelo pipeline antigo, sem exclusão).
2. **Prova da 1ª corrida:** +40 candidatas internacionais (inglês 18 · chinês 7 · alemão 6 · espanhol 3 · francês 3 · russo 3 · japonês 0), só 2 fininhas descartadas, 108s — fila tec 24→64. Amostras: "Flock's AI Search Tool for Cops" (Wired, 16,6k chars, nota 7.5) · "Scaling agentic AI pilots" (MIT TR) · Huawei/5G (TechNode). py_compile OK; backup `.bak_pre_tec_multiidioma_20260903`; rollback no ROLLBACK_INDEX (ligado=false ou 1 cp).
3. **Automação do monitor travada no Kimi:** o prompt da automação horária (automation-d6095d3d) pedia assinatura "ZCode/Qwen 3.8" — atualizado via CronUpdate para "ZCode/Kimi K3" + nota da ordem ("mantenha o KIMI"). O default do app já era kimi-k3 desde ~06:3x (config.json com backup). O que NÃO está ao meu alcance: o seletor de modelo de OUTRAS janelas/sessões abertas (só o Miguel troca na UI de cada uma — sessões velhas em Qwen vão falhar sem crédito até ele trocar o seletor ou fechar).
4. **Resposta "os coletores abastecem os verticais?":** SIM, com números — a fila que os coletores enchem é a MESMA tabela `candidates` que o v41_ciclo consome para escrever: geo 263 novas/24h (3 posts geo publicados nesta manhã: 268717, 268739, 268744) · nacional_direto 319 colhidas/24h · 6 materiais brutos montados pelo enriquecedor · tec 24→64 agora · nacional 651 new · economia 238 new. A guarda anti-fome (autocura da fila, */20) segue ligada vigiando janelas vazias.
