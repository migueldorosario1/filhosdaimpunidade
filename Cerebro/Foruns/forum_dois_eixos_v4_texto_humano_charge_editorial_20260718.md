# V4 — dois eixos decisivos: texto humano e imagem destacada

**Direção de Miguel:** 18/07/2026  
**Coordenação:** Codex | `CODEX-V4-DOIS-EIXOS-20260718`  
**Status:** prioridade máxima antes da autonomia.

## Eixo 1 — texto que as pessoas queiram ler

O texto V4 precisa ser fresco, sério, humano e jornalístico. Não basta estar correto. Precisa trazer novidade, explicar por que importa, produzir análise própria e manter ritmo.

### Critérios obrigatórios

1. Abertura com fato novo, conflito ou consequência concreta — nunca introdução genérica.
2. Subtítulo claro, natural e informativo; sem construção burocrática ou semântica torta.
3. Voz humana: variação de ritmo e tamanho de frase, verbos concretos, transições naturais.
4. Análise ligada a fatos: explicar força, interesse, contradição e consequência.
5. Linha de esquerda e anti-imperialista sustentada por dados, relações de poder e contexto; jamais slogan.
6. Evitar bordões de IA, conclusão escolar, repetição do título, enumeração mecânica e excesso de intertítulos.
7. O leitor deve terminar sabendo algo novo e entendendo por que aquilo muda sua vida, o Brasil ou a disputa política.

### Tribunal do texto

Antes de promoção, cada canário recebe notas 0–5 em: novidade, clareza, naturalidade, densidade factual, análise, ritmo, voz do Cafezinho, ausência de clichê, título/subtítulo e poder de retenção. Nota menor que 4 em naturalidade, precisão do subtítulo ou novidade bloqueia.

## Eixo 2 — imagem destacada que tenha identidade

### Faixa contextual do cartum

Todo cartum publicado terá uma faixa inferior padronizada com uma ou duas frases curtas de contexto. A faixa faz parte da identidade visual do V4 e pode acompanhar tanto o cartum destacado quanto o cartum usado ao final da matéria.

O modelo de imagem gera somente a arte e deixa área inferior respirável. Texto, tipografia e faixa são aplicados depois por composição determinística, evitando letras quebradas, erros factuais e variações de estilo. A faixa contextualiza sem repetir o título nem explicar a piada.

A faixa será colada ao desenho e fará parte do arquivo final compartilhado — não será uma legenda do WordPress. Ela incluirá obrigatoriamente a logo oficial do Cafezinho e `ocafezinho.com`. A logo será inserida a partir do ativo oficial; a IA não poderá improvisar ou redesenhar a marca.

### Estratégia híbrida

1. **Fotografia factual licenciada:** primeira escolha quando retrata com precisão pessoa, lugar ou acontecimento.
2. **Charge/ilustração editorial própria:** preferida para análise, geopolítica, economia política e temas abstratos.
3. **Imagem conceitual licenciada:** fallback quando a pauta não exige personagem específico.
4. **Sem imagem:** melhor que imagem errada, enganosa ou sem licença.

### Identidade da charge do Cafezinho

- inteligente antes de engraçada;
- ironia seca, humor político elegante e detalhe visual que recompensa um segundo olhar;
- perspectiva popular, de esquerda e anti-imperialista mostrada pela relação de poder, nunca por cartaz ou palavra de ordem;
- desenho editorial minimalista, composição legível em miniatura e silhuetas fortes;
- paleta curta: preto/grafite, creme de jornal e um acento vermelho queimado;
- sem imitar artista vivo, sem assinatura falsa, sem logotipo de terceiro;
- sem balões, manchetes ou texto gerado dentro da imagem por padrão; título e legenda ficam no CMS;
- se houver pessoa pública, caricatura editorial evidente — nunca falso registro fotográfico;
- disclosure: `Ilustração editorial gerada por IA para O Cafezinho`.

## Prompt-mestre

O prompt canônico fica em `Projeto Cafezinho Agentes/root/v4_labs/labs/sprints_v4_20260718/charge_editorial_cafezinho/PROMPT_MESTRE.md`.

Ele recebe apenas variáveis editoriais estruturadas: fato central, poder dominante, consequência popular, contradição, metáfora visual, personagens permitidos, símbolos proibidos e formato social.

## Benchmark de modelos

Nenhum provedor será declarado vencedor por reputação. Usaremos o mesmo briefing e prompt-mestre em todos os geradores disponíveis, com seeds/versões quando expostas. Avaliação cega, sem nome do modelo, em:

- inteligência/metáfora;
- fidelidade ao briefing;
- legibilidade em thumbnail;
- ausência de clichê;
- qualidade do desenho;
- risco factual/político;
- consistência de estilo;
- custo, latência e taxa de falha.

O campeão vira primário; segundo e terceiro viram fallbacks. A telemetria registra modelo, versão, prompt hash, custo, latência, imagem hash e decisão humana/visual.

## Divisão de trabalho

- **Kimi:** tribunal do texto, sem nova geração enquanto congelada.
- **Kilo:** briefings factuais e metáforas possíveis, sem escrever o prompt final.
- **Grok:** sistema visual, variações e testes em miniatura.
- **DeepSeek:** matriz atual de provedores, custos, termos e capacidades verificadas.
- **AGY:** telemetria das imagens e comparação cega.
- **Claude:** integração no pipeline e regra fotografia/charge/sem imagem.
- **Codex:** prompt-mestre, auditoria, amostra visual e decisão de promoção.

## Gates

### Antes de gerar — exigência alta e barata

- briefing factual completo;
- metáfora escolhida e testada em texto;
- personagens e símbolos permitidos fechados;
- prompt versionado e orçamento aprovado;
- modelo primário/fallback definidos.

### Depois de gerar — auditoria liberal

A charge cara não será descartada porque recebeu nota estética baixa. Só bloqueiam: arquivo quebrado, ilegalidade/risco grave, pessoa errada, fato visual inventado, conteúdo totalmente alheio ou defeito que impeça uso. Fora disso, publicar, medir e aprender.

Uma charge óbvia, pouco engraçada ou visualmente mediana pode entrar e receber nota posterior. Isso vira lição para o próximo prompt/modelo. Não haverá loop automático caro tentando alcançar perfeição.

## Aprendizado e autocura

- toda charge recebe notas posteriores, custo, modelo e prompt hash;
- problemas recorrentes geram proposta de ajuste nas diretrizes externas;
- ajuste é testado em shadow e versionado;
- princípios editoriais não mudam automaticamente por audiência;
- motor técnico não contém estilo hardcoded: lê contratos/diretrizes externas versionadas.

## Feedback 1–5

Arquitetura e regras no fórum `Cerebro/Foruns/forum_feedback_1a5_autocura_editorial_v4_20260718.md`.
