# 🎨 PROMPTS — DESIGN MOKA: primeiro CLAUDE (direção), depois ANTIGRAVITY (aplicação)

> Fluxo do Miguel (31/08): 1º colar o PROMPT 1 no Claude → resposta em TEXTO volta →
> Miguel escolhe a opção → colar PROMPT 2 no Antigravity Desktop (com a resposta dentro).
> Feito pelo ZCode/GLM-5.3. Paleta extraída do código real (globals.css).

---

## 📝 PROMPT 1 — pro CLAUDE (copie daqui pra lá)

Você é o **diretor de design** do Moka (app de leitura com IA, da casa O Cafezinho). Sua entrega é **100% em texto** — uma especificação de design tão precisa que outro agente (o Antigravity) consegue implementar sem te ver. Não escreva código; escreva DIREÇÃO com números.

**O produto:** leitor de livros (EPUB/PDF) com IA que traduz, explica e resume. 5 módulos com a MESMA importância: Reader 📖, Vídeo 🎬, Memória 🧠, Harness 💬, Writer ✍️, + ⚙️ Configurações. Público: pessoas comuns lendo no celular e no PC. Sensação desejada: **sofisticado, sereno, caro** — como uma livraria de aeroporto de primeira classe, não como um app de entrega de comida.

**A tela principal (capa), de cima pra baixo:** palavra "MOKA" + frase de efeito; dois cartões discretos ("gratuito" e "como pegar sua chave de IA"); e **a estrela da tela: 6 CARDS-BOTÃO em grade (3×2 no PC, 2×3 no celular)** — cada card: um ÍCOME dentro de uma caixinha 48px arredondada, o nome do módulo em negrito, e uma linha de descrição. Hoje: fundo branco puro, borda quase invisível, sombra levinha; no hover levanta 3px.

**A paleta REAL do site hoje (use-a como base, pode refinar):**
- Fundo geral: porcelana azulada `#f0f4f9` · Superfícies: branco `#ffffff` · Secundária: `#e2ebf6`
- Cor principal: **azul cobalto `#1e40af`** (hover `#dbeafe` gelo, press `#172554` safira)
- Texto: `#0f172a` (noite) / `#475569` (ardósia) · Detalhe dourado envelhecido: `#d97706`
- Dentro do leitor: 3 BOTÕES-PÍLULA grandes (Página/Marcar/Perguntar) e menu ☰.

**O PEDIDO (do Miguel): "mudanças sutis nas CORES, com DEGRADÊ, pra ficar mais SOFISTICADO"** — foco nos cards/botões da capa.

**Responda EXATAMENTE assim:**
1. **3 direções (A, B, C)**, cada uma com nome e personalidade (ex.: "Porcelana e Ouro", "Amanhecer Azul", "Biblioteca Noturna"). Para CADA uma, especifique em TEXTO PRECISSO:
   - O degradê EXATO do card em repouso (hex inicial → hex final, direção: vertical/diagonal 135°) e no hover;
   - Cor da borda, sombra em repouso e hover (RGB com alfa);
   - Fundo da caixinha do ícone (degradê ou sólido, hex) e se o ícone muda de cor;
   - Tipografia dos cards (peso/tamanho do nome e da descrição);
   - Como o FUNDO GERAL da página muda (ou não) pra acompanhar;
   - Tratamento dos 2 cartões secundários e dos 3 botões-pílula do leitor (mais discreto que os cards);
   - Como fica no MODO ESCURO.
2. **Qual das 3 você recomenda** pro "sofisticado, sereno, caro" e por quê (2 frases).
3. **3 regras de elegância** que o time deve respeitar ao implementar (ex.: contraste mínimo, um degradê por elemento só, etc.).

**Restrições fixas:** os 5 módulos permanecem visualmente IDÊNTICOS em importância (nada de destacar um); nada de foto/ilustração decorativa; emojis continuam como ícones por ora; mudanças SUTIS — quem já usa o site deve achar "ficou mais bonito", não "troquei de app".

---

## 📝 PROMPT 2 — pro ANTIGRAVITY (depois da resposta do Claude; cole a resposta dele onde marcado)

Você é o implementador de design do Moka (repo local `/home/migueldorosario/ZCodeProject/moka-app`, branch `obra/memoria`, app em `apps/web/src`; site-laboratório https://moka-ousadia.vercel.app). O diretor de design (Claude) definiu a direção abaixo; o Miguel escolheu a **OPÇÃO ___**. Sua missão: **implementar essa opção nos CARDS da capa (`/`, classe `.capa-launch-btn`/`.capa-launch-ico`) e nos botões-pílula do leitor (`.reader-big-btn`)**, respeitando o que já existe (kit v1.0 em `globals.css` com tokens `--btn-*` — estenda os tokens, não brigue com eles).

**ESPÉCIFICAÇÃO DO CLAUDE (cole a resposta dele aqui):**
```
[COLE A RESPOSTA COMPLETA DO CLAUDE AQUI]
```

Regras: (1) mudanças SUTIS e sofisticadas — degradês conforme a especificação, sem exagero; (2) os 6 cards permanecem IDÊNTICOS entre si; (3) nada de texto hardcoded em português nos componentes (i18n 12 idiomas); (4) **edite apenas `apps/web/src`** e NÃO publique/FAÇA deploy — quem revisa e publica no Ousadia é o ZCode (rito da casa: Ousadia → Espelho → Canônico); (5) ao terminar, entregue: lista do que mudou + prints desktop/celular + como voltar atrás (o marco anterior é a tag `ousadia-memoria-nuvem-20260831`).

---
