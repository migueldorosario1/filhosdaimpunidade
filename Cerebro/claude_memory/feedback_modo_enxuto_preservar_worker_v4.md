---
name: feedback-modo-enxuto-preservar-worker-v4
description: Worker V4 (superluxo LLM fronteira + WebSearch + revisão) traz texto bom. NÃO reescrever prosa - só corrigir bugs objetivos e ajustar título. Miguel 11/08 05:36 BRT.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ab72ecc4-9deb-4729-9735-80bcceefd907
---

**Worker V4 hoje está em modo "superluxo"** — Miguel investiu em LLMs de fronteira, WebSearch integrado, revisão e curadoria automatizadas. Isso significa que **o texto bruto do worker JÁ ESTÁ BOM**. Minha função na Vigília V5 mudou: não reescrever prosa, apenas emendar bugs objetivos e refinar título quando frio.

**Why:** Miguel 11/08 05:36 BRT: "o worker traz textos, eu mudei o worker pra superluxo. estou desperdiçando bons textos e, sob pretexto de melhorá-los, estar piorando". Caso concreto: post 265158 (Motta apoia Lula) — worker trouxe 6 parágrafos curtos (média 2 frases/parágrafo), sem ponto-e-vírgula, prosa jornalística direta; eu reescrevi 85% do texto virando 3 parágrafos densos com H2, `<strong>`, ponto-e-vírgula, travessões, sub-cláusulas — impondo estilo "artigo de revista" que não é o Cafezinho.

**Regras concretas do "modo enxuto":**

**FAZER:**
1. Corrigir **bugs factuais objetivos** — data errada (ex: "terça (4)" quando era segunda 10), ângulo relacional invertido (ex: "aliado" quando é adversário), número não confirmado no WebSearch, nome próprio errado
2. Ajustar **título** quando estiver frio/oficialesco — regra [[feedback-titulo-forte-simples-ludico-politico]] + [[feedback-titulo-tese-corpo-argumenta]]
3. Adicionar **só o que corrige erro material** (ex: partido/UF omitido em nome citado; data completa quando falta ano)
4. Preservar estrutura de parágrafos do worker

**NÃO FAZER:**
- Reescrever prosa que já está OK
- Adicionar aspas literais que worker parafraseou razoavelmente (só substituir quando paráfrase distorce)
- Adicionar contexto histórico/familiar/ambivalência que worker não trouxe (a menos que crítico pra não induzir leitor a erro)
- Adicionar H2 novos se worker não colocou (worker usa intertítulo simples em `<p>Título</p>`)
- Criar parágrafos longos (padrão: **média 2 frases/parágrafo**, tolerância 3)
- Usar `;` **(ponto-e-vírgula NÃO É padrão Cafezinho)**
- Usar `<strong>` (negrito) no meio do texto corrido — PROIBIDO. Nem nome, nem partido, nem data, nem número, nem sigla, nem aspa. **Única exceção autorizada 11/08 05:54 BRT:** intertítulo claro — texto curto sem ponto final, servindo como subtítulo entre parágrafos. Nesse caso vale UM `<strong>Subtítulo</strong>` isolado em `<p>`.
- Empilhar dois-pontos, travessões, sub-cláusulas — prosa densa "de revista"

**THRESHOLD DE ESCALAÇÃO PRA MIGUEL:**
Se o WebSearch trouxer insight que **muda a TESE do post** (ex: post que era pró vira contra; ângulo político inverte), **avisar Miguel ANTES de publicar** — não decidir sozinho. Mandar 3 linhas: (a) tese original do worker, (b) tese que WS sugere, (c) pergunta simples "aplico ou mantém a do worker?".

**How to apply:** No pipeline Vigília V5, o passo "Claude+WebSearch" era usado como camada de reescrita editorial. Agora vira **camada de checagem factual**. DS+GPT pegam bugs de forma/estilo; meu WebSearch pega bugs factuais/temporais + confirma nomes+números. Nada de estilo. Se DS/GPT recomendam "publicar_com_ajustes" só por estilo, não aplico ajuste — respeitando padrão worker.

**Correção retroativa:** post 265158 deve ser reescrito de volta pra mais perto do worker original (mantendo só as 2 correções factuais: data e ângulo Azevêdo) — feito 11/08 madrugada.

**Padrões estilo Cafezinho vigentes:**
- Sem `;`
- Média 2 frases/parágrafo (tolerância 3)
- Prosa jornalística direta, não densa/acadêmica
- Título tese forte+simples+lúdico+político (regra separada, mantida)
- Nomes com partido/UF na primeira menção (worker já faz)

Regras irmãs: [[feedback-titulo-forte-simples-ludico-politico]] · [[feedback-titulo-tese-corpo-argumenta]] · [[feedback-vigilia-v5-dsgpt-paralelo-websearch]] · [[feedback-liberar-sem-no-home-criterios]] · [[feedback-nada-ruim-nada-estranho-no-cafezinho]]
