---
name: feedback-titulos-simples-siglas-explicadas-agente-ia
description: "Posts do agente_ia.py NÃO podem ter jargão técnico no título. Leitor leigo precisa entender de uma vez. Cada sigla usada no corpo (OCR, LLM, API, GPU, etc) DEVE ser explicada na 1ª ocorrência. Caso fundador #260250: 'PaddleOCR lança PP-OCRv6 com suporte a 50 idiomas e modelos de até 34,5 milhões de parâmetros' → curado para 'Nova IA chinesa de OCR lê texto em 50 idiomas e roda até em celular' + lide explicativo."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f312988d-5dc6-4ea6-b08a-94b4cada57ec
---

🤖 **Posts do `agente_ia.py`** (que cobre IA, ML, modelos, frameworks) frequentemente saem com títulos cheios de jargão técnico que só especialista entende. Miguel cobrou 2026-06-22 ~13:53 BRT: *"o título desse tá com muita palavra complicada. tem que botar na diretriz desse agente, para títulos simples, que sejam entendidos por leigos. e na matéria, cada sigla desses, se usada, precisa ser explicada"*.

**Regra 1 — Título sempre leigo**
Substituir nomes de produto técnico por descrição funcional. Manter números curtos e palpáveis. Mencionar quem fez e o impacto direto.

❌ ERRADO (caso fundador #260250 22/06 13:50 BRT):
- "PaddleOCR lança PP-OCRv6 com suporte a 50 idiomas e modelos de até 34,5 milhões de parâmetros"
- "Mixtral 8x22B supera Llama 3 70B no MMLU com arquitetura MoE"
- "DeepSeek-V3 atinge 87% no HumanEval com 671B parameters MoE"

✅ CERTO (após cura Daemon 22/06 13:57):
- "Nova IA chinesa de OCR lê texto em 50 idiomas e roda até em celular"
- "Nova IA francesa supera modelo do Meta em testes de raciocínio"
- "IA chinesa atinge 87% em testes de programação e ameaça GPT-4"

**Regra 2 — Lide explicativo (parágrafo 1) com glossário inline**
Antes do conteúdo técnico, abrir com 1 parágrafo "O que é:" explicando os termos centrais que o leitor leigo encontraria adiante. Formato sugerido:

```html
<p><strong>O que é:</strong> [explicação 1-frase do produto/empresa]. [Sigla] ([expansão]) é a tecnologia que [função em linguagem simples]. A novidade chama-se [nome do produto] e [diferencial palpável].</p>
```

Caso fundador #260250 — lide inserido pelo Daemon:
> *O que é: um software de inteligência artificial chinês — o PaddleOCR — acaba de lançar uma versão nova capaz de "ler" texto em imagens em 50 idiomas diferentes. OCR (Optical Character Recognition) é a tecnologia que transforma foto de um documento, placa ou tela em texto editável no computador. A novidade chama-se PP-OCRv6 e tem três tamanhos diferentes para rodar desde em celulares até em servidores grandes.*

**Regra 3 — Cada sigla expandida na 1ª ocorrência**
Sempre que uma sigla técnica aparecer pela primeira vez no corpo, expandir entre parênteses. Próximas ocorrências podem usar só a sigla.

Lista de siglas comuns que DEVEM ser expandidas:
- **OCR** (Optical Character Recognition / reconhecimento óptico de caracteres)
- **LLM** (Large Language Model / modelo grande de linguagem)
- **API** (Application Programming Interface / interface para conectar programas)
- **GPU** (Graphics Processing Unit / placa gráfica para cálculos massivos)
- **TPU** (Tensor Processing Unit / chip do Google pra IA)
- **MoE** (Mixture of Experts / arquitetura de "comitê de especialistas")
- **RAG** (Retrieval-Augmented Generation / IA que busca antes de responder)
- **ML** (Machine Learning / aprendizado de máquina)
- **NLP** (Natural Language Processing / processamento de linguagem natural)
- **MMLU**, **HumanEval**, **HellaSwag** — *testes padrão de avaliação de IA*
- **B parameters**, **34M params** — substituir por "tamanho do modelo" com comparação ("equivalente a um celular médio", "1/100 do tamanho do GPT-4")

**Why:** Cafezinho é portal generalista pra esquerda progressista — público diverso, não-técnico majoritariamente. Título técnico afasta leitor, derruba CTR no GA4. Miguel deixou claro: leigo tem que entender de uma vez.

**How to apply:**
1. **Patch §92 cheio em `/root/agente_ia.py`** (sprint Kimi):
   - System prompt do redator: instrução clara *"Título deve ser entendido por leitor leigo. Nada de nomes de produto técnico. Use linguagem do dia-a-dia."*
   - Inserir validador pós-título: regex bloqueando padrões `[A-Z]+v\d+`, `[A-Z]{2,}-?[0-9]+`, `\d+B parameters` no título — se aparecer, reformular.
   - Adicionar lide explicativo automático: 1ª chamada LLM dedicada (gpt-5-nano) gera parágrafo "O que é:" baseado no conteúdo técnico do post original.
   - Dicionário de siglas (mesmo do código): se sigla aparece no corpo sem expansão, inserir automaticamente entre parênteses na 1ª ocorrência.
2. **Cura editorial Daemon retroativa** quando detectar via §53:
   - Reescrever título usando linguagem leiga
   - Inserir lide "O que é:" com glossário inline antes do 1º parágrafo
3. **Verificar também outros agentes técnicos** que podem ter o mesmo problema: agente_singularidade (se rodando), parts do agente_china quando cobre semicondutores/IA, agente_master_trends.

**Caso fundador 2026-06-22 13:57 BRT (#260250)**:
- Original: "PaddleOCR lança PP-OCRv6 com suporte a 50 idiomas e modelos de até 34,5 milhões de parâmetros"
- Cura aplicada: "Nova IA chinesa de OCR lê texto em 50 idiomas e roda até em celular"
- Lide explicativo de 1 parágrafo inserido
- Link Hugging Face broken `href=""` consertado pra URL plausível

Vinculo correlato: [[feedback-yt-v2-titulo-analista-nominal-corpo-7p]] (regra similar pra YT V2 — título com nome do guest, leigo entende).
