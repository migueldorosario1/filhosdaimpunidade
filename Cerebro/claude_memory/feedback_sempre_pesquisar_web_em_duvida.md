---
name: sempre-pesquisar-web-em-duvida
description: "Sempre que tiver dúvida sobre fato, cargo, pessoa, data, valor, tecnologia recente ou qualquer afirmação que possa ter mudado desde o knowledge cutoff — pesquisar web ANTES de afirmar, não depois de errar"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f333da72-7610-439d-ab22-49569ae85b4a
---

**REGRA INVIOLÁVEL:** Sempre que tiver qualquer dúvida sobre um fato do mundo real — cargo de figura pública, data recente, valor financeiro, versão de software, comando obscuro, quem ganhou eleição, quem morreu, quem assumiu cargo — **pesquisar web ANTES de afirmar**. Nunca proclamar erro factual em produção sem checar fonte externa primeiro.

**Why:** 25/07/2026 02:38 BRT, ciclo Sentinela `20260726_0238`, afirmei com confiança pro Miguel que "Cristiano Zanin é presidente do STF desde set/2025" e chamei o post 262949 de "erro factual grave" — quando na verdade **Edson Fachin É o presidente do STF** (posse 29/09/2025, biênio 2025-2027). Meu knowledge cutoff é jan/2026 mas essa informação escapou. Miguel foi direto: *"edson fachin é o presidente do STF. voce pesquisou na internet para confirmar antes de falar besteira?"* e depois *"sempre que voce tiver dúvidas, pesquise na internet, é tão fácil meu deus."*. WebSearch estava disponível como ferramenta o tempo todo — não usei. Custou credibilidade e podia ter causado dano real se algum ciclo aplicasse `editar_corpo_publicado` automaticamente sobre um post CORRETO.

**How to apply:**
- Antes de acionar `propor_correcao_semantica` ou `editar_corpo_publicado` sobre fato de figura pública com mudança recente de cargo/situação (últimos 12 meses do cutoff) → **WebSearch primeiro**.
- Antes de reportar pro Miguel "post publicado com erro" → verificar externamente que é erro mesmo.
- Antes de dizer "X é Y" quando X é entidade que muda no tempo (presidente, ministro, CEO, técnico de time, versão de software) → WebSearch, mesmo se "acho que sei".
- Se WebSearch confirma → sigo. Se contradiz → corrijo antes de reportar.
- **Vale também pro pipeline Sentinela:** LLMs juízes semânticos (DeepSeek V4, GLM 5.2) têm knowledge cutoff mais velho que o meu — propostas sobre fatos recentes precisam gate de verificação web antes de virar `editar_corpo_publicado` automático. Sugerir isso ao Miguel/Kimi como mitigação estrutural.

**Meta-lição:** LLM como juiz factual sem verificação externa é bomba-relógio em pipeline editorial. Precisão exige fontes vivas, não memória parametrizada.

Regras irmãs: [[nome-proprio-figura-publica-nunca-publish-com-proposta]] (a regra ⛔ que eu MESMO tentei aplicar contra um post correto — a regra é boa, minha aplicação foi ruim porque não verifiquei o "erro" primeiro), [[protocolo-memoria-bugs-ler-antes-agir]].
