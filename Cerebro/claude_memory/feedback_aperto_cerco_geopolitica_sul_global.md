---
name: feedback-aperto-cerco-geopolitica-sul-global
description: "Matéria sobre líder do Sul Global (Arce, Sheinbaum, Maduro, Castro, Petro, Ortega, Xi, Putin etc.) — verificar cargo/status atual ANTES de aprovar. Dúvida = rebaixar pending, não \"monitorar\"."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c864c422-014f-4122-8468-216a5d32e450
---

🚨 **Aperto de cerco no monitoramento §53 — matérias geopolíticas sobre líderes do Sul Global** (Miguel 2026-06-10 17:50 BRT).

**Why:** Caso #257457 — matéria publicada às 17:33 BRT alegando que "Luis Arce Catacora é presidente da Bolívia" + chamando o governo dele de "extrema direita alinhado a interesses estrangeiros". **Arce não é mais presidente** (Cafezinho linha editorial defenderia ele se fosse). Eu (Claude) auditei e marquei "monitorar" em vez de "rebaixar" por achar o framing "ambíguo". Miguel rebaixou manual. Erro duplo meu: (a) critério frouxo, (b) não verifiquei o fato básico do cargo durante auditoria.

Timing: §53E (Gemini grounding no roteador master) foi deployado às 17:35 BRT — 2 minutos DEPOIS do #257457 publicar. Logo o post saiu pelo gpt-4o **sem web_search** e alucinou cargo desatualizado. Posts pós-17:35 BRT que passem por master_geopolitica/nacional/lula/china/latam/sheinbaum/etc. via roteador master ganham web_search e o Gemini grounding pega cargo errado no Google.

**How to apply:**
- Matéria sobre líder do **Sul Global** (Lula, Sheinbaum, Maduro, Castro/Díaz-Canel, Arce/Morales/sucessor Bolívia, Petro/Colômbia, Ortega/Nicarágua, Xi, Putin, Khamenei/Pezeshkian, Modi, Kim Jong Un, etc.) — auditar com **rigor extra**: cargo atual, partido, posição editorial Cafezinho.
- Dúvida sobre **fato político atual** (cargo, eleição, status de líder) = **rebaixar pending**, NUNCA "monitorar".
- "Monitorar" é pra ambiguidade DE TOM (não factual), não pra dúvida factual.
- Pra ter mais segurança quando houver dúvida, posso buscar via WP API se há OUTROS posts recentes sobre o mesmo líder/país e cruzar referências.
- Se a matéria descreve líder do campo popular como "extrema direita" ou "alinhado a interesses estrangeiros" sem qualificação, presunção de **alucinação** — rebaixar.

**Casos análogos passados a respeitar:**
- Sheinbaum não é presidenta → ERA. (gpt-4o cutoff) — já documentado em [[feedback_linha_editorial_anti_imperialista_russia_inegociavel]] adjacente
- Flávio Bolsonaro não é candidato presidencial → É (2026)
- Trump não é presidente → É (desde jan/2025)

Cura estrutural: §53E (deployada 2026-06-10 17:35 BRT) coloca Gemini grounding como revisor de todos os agentes que chamam o roteador master. A partir desse momento, próximas matérias passam pelo Google Search nativo do Gemini e cargo errado é pego.

Relacionado: [[feedback_auditor_gpt_suaviza_titulos_fortes]] (alucinação reversa gpt-4o), [[feedback_revisor_ler_tudo_rebaixar_so_se_muito_estranho]] (limiar — esse caso É "muito estranho" porque envolve fato político atual de líder Sul Global, NÃO se aplica limiar permissivo aqui), §95 hiperlink fonte obrigatório (ajuda cross-ref).
