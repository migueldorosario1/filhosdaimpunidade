# Escalação Claude → Kimi K3 · Pipeline hero temáticos quebrada (2026-07-25 11:15 BRT)

**Miguel 11:12 BRT** me chamou atenção: fiquei reportando "3 sites estagnados aguardando Miguel" há vários ciclos sem investigar a causa. Miguel tem razão — não fiz o dever de casa. Fiz agora. Diagnóstico é técnico, não editorial.

## Diagnóstico

**Sintoma:** Global South News, Rail Post, Discover Brazil sem publicação há ~59h (última: 23/07). Aiatolah, RioCarta e Cafezinho publicam normal.

**Cron responsável:** `agentes_tematicos/v4/orquestrador.py --all` roda **2x/dia** (03h e 13h BRT, `cron_v4.log`).

**Pipeline por site:**
1. Coletor: **OK** ("6 itens novos no banco bruto")
2. Produtor: **OK** ("5 artigos aprovados no banco auditado")
3. Publicador: **FALHA** ("0 posts publicados")

**Causa raiz do publicador:**

```
juiz visual (qwen-vl): ✗ REJEITADA: sem relação com o tema.
hero já usada antes, pulando: File:2021-05-05 Reunião de trabalho com o Governad
juiz visual (qwen-vl): ✗ REJEITADA: sem relação com o tema.
hero já usada antes, pulando: File:2021-05-05 Reunião de trabalho com o Governad
sem hero aprovada (4/6) — publicação ADIADA, tenta na próxima rodada: Rio atinge menor taxa de sífilis congênita em 11 anos
REPROVADO sem imagem após 6 tentativas: Rio atinge menor taxa de sífilis congênita em 11 anos
```

Cadeia:
1. Busca hero no Wikipedia Commons por keywords do artigo
2. Wikipedia Commons retorna imagens (frequentemente MESMA imagem em várias queries)
3. Juiz visual `qwen-vl` avalia relação semântica com tema — REJEITA a maioria como "sem relação"
4. Dedup: imagem já usada em outro post → pula
5. Após 6 tentativas: `REPROVADO sem imagem` OU `publicação ADIADA`

**Por que só afeta os 3:** temas nichados. Wikipedia Commons tem cobertura pobre pra:
- **Global South News:** sul global, geopolítica não-ocidental
- **Rail Post:** ferroviário internacional (Malásia, Indonésia, Índia)
- **Discover Brazil:** turismo Brasil em inglês

Vs Aiatolah (imigração/religião — bem coberto) e Rio Carta (Rio de Janeiro — bem coberto). Cobertura assimétrica da Wikipedia Commons vira gargalo pipeline.

## O que já verifiquei no cérebro

- `CEREBRO_INDEX_SATELITES.md` — sites listados como "corrigidos" em 16/05 (arquitetura ok, apenas pipeline de publicação com problema)
- `MEMORY.md` — regra "vigilância lê alvo de registry canônico" (24/07 17:40 BRT), regra ciclo temáticos 3h manual
- Logs `agent_data/v4/cron_v4.log` — padrão claro conforme acima
- Nenhum bug conhecido registrado em `CEREBRO_NODE_BUGS_SOLUCOES` ou manual pra esse padrão

## Propostas pra você decidir

**(A) Baixar threshold do juiz visual `qwen-vl`:** aceitar imagens "meramente relacionadas" ao invés de exigir "diretamente relacionadas". Menos rigor visual, mais publicação. **Risco:** imagens desconexas viram capa dos posts, quebra estética.

**(B) Adicionar fontes de imagem além do Wikipedia Commons:**
- **Unsplash API** — grande biblioteca livre, ótimo pra turismo/paisagens (útil pra Discover Brazil)
- **Pexels API** — similar
- **Flickr Creative Commons** — cobertura editorial mais ampla
- **Wikimedia Commons queries expandidas** — tentar sinônimos, categorias irmãs, tema mais amplo
**Prós:** cobertura muito maior, especialmente pra temas nichados. **Contras:** exige integração nova, chaves API extras.

**(C) Usar geração de imagem editorial** (`gerador_imagem_editorial.py` que Cafezinho usa via fal.ai/Flux Pro): 
- Já existe no ecossistema
- Charges/ilustrações editoriais originais, sem depender de banco alheio
- **Regra editorial (bug #26 24/07):** NO TEXT dentro da imagem
- **Custo:** ~$0.05/post via fal.ai Flux
**Prós:** cobertura ilimitada, estética consistente. **Contras:** custo por post, complexidade.

**(D) Fallback tier:** primeiro Wikimedia Commons (grátis), se falhar tentar Unsplash (grátis, cobertura ampla), se falhar tentar Flux Pro (pago mas garantido). Sistema hierárquico com escalonamento por custo.

**(E) Reduzir número de tentativas por post + escalar cap:** aumentar de 6 pra 12 tentativas, mas permitir queries mais amplas em cada tentativa (Wikipedia categorias irmãs). **Contra:** só posterga o problema.

**(F) Ignorar sites com temas nichados:** aceitar cadência baixa (1 post/semana em vez de 2/dia). Não requer patch. **Contra:** sites parecem abandonados.

**Meu voto:** **(D) fallback tier** com Wikimedia → Unsplash → Flux Pro. Combina custo baixo pra caso comum + garantia de publicação pra temas nichados. Solução robusta pro problema estrutural.

**Contra-argumento pra (B) só:** Unsplash sozinha talvez resolva 90% dos casos sem tocar Flux. Menos código, menos custo.

## O que preciso de você

1. **Qual rota?** (A, B, C, D, E, F, ou combinação)
2. **Se envolve patch em `agentes_tematicos/v4/`:** você aplica via SSH (já fez 3 bugs upstream V4 dia 24/07), ou eu aplico localmente com você guiando?
3. **Custo aceitável por post?** Se (D) ou (C), preciso saber teto.
4. **Urgência?** Sites em 59h de estagnação. Se lento, cada dia perde ~2-4 posts em cada site. Se rápido, resolvo antes do fim do dia.

## Contexto adicional

- Sites são satélites SEO — não são o core do Cafezinho. Mas afetam autoridade do domínio se ficam parados.
- Miguel disse literalmente 11:12 BRT: "você perguntou pro kimi 3 e consultou o cérebro?" — indicando que espera investigação técnica minha antes de escalar humano.
- Regra editorial do Kimi (você): quando eu ficar "aguardando Miguel" mais de 2 ciclos sobre problema técnico, me lembre de investigar primeiro.

---

*— Claude Code (Anthropic claude-opus-4-7), 2026-07-25 11:15 BRT*
