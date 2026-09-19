# 🎬 FÓRUM — FdI: Reforma do menu + Estúdio do Estilo + fluxo copiar/colar (assinatura-first)

**Data:** 19/08/2026 (criado ~11:25 BRT como CHECKPOINT da vigília 🟠 — Kimi 105%)
**Agente:** ZCode/Kimi K3 (sessão interativa, ZCodeProject)
**Repo:** `/home/migueldorosario/ZCodeProject/filhosdaimpunidade` (GitHub: migueldorosario1/filhosdaimpunidade → Vercel filhosdaimpunidade.vercel.app)
**Arquivo principal:** `index.html` (663 KB, SPA — livro inteiro embutido em JS)

## O pedido do Miguel (consolidado, 2 rodadas)

1. **Menu enxuto:** poucos itens fixos no topo; o resto abre em **submenus** (dropdowns). Hoje há ~15 botões soltos no header.
2. **Assinatura-first, API é exceção:** produção via copiar/colar para ChatGPT/Claude/Grok/Gemini **por assinatura**. As 6 APIs do Estúdio (Gemini/GPT/Claude/DeepSeek/Kimi/GLM) ficam, mas recuadas como "modo exceção".
3. **Estúdio do Estilo = coração do site**, com:
   - **📜 Constituição** (regras maiores, imutáveis)
   - **📰 Diretriz Editorial** (rumo do conteúdo)
   - **🎵 Diretriz de Estilo** (ritmo/tamanho de frase, cadência)
   - **🎼 Prompts de Estilo — 8 (OITO), no plural** (refinamento 2ª rodada): 8 ritmos/cadências diferentes para REVEZAR por capítulo. **CRUD livre:** criar mais, apagar, editar. Começar com 8.
4. **Textos de 800–1000 palavras** como unidade de trabalho — vale para post do Cafezinho E para bloco de capítulo de livro.
5. **Memória indexada num arquivo só** (memória do projeto FdI organizada).
6. **Botão Copiar com checkboxes:** `[x] Prompts de estilo` (marca → abre seletor Prompt 1–8 para escolher QUAL vai junto) + `[x] Memória` → copia **um bloco único**: prompt de estilo na frente + memória + texto. Desmarcado = texto puro.
7. **DEPOIS (fase futura, NÃO nesta entrega):** FdI vira **gerador de livros** — botão no alto "🧹 Limpar / Iniciar novo projeto", "Usar estilo antigo" (copiar diretrizes de outro projeto), "Filhos da Impunidade" vira o NOME DO PROJETO. **Preparar o terreno, mas implementar depois.** Ordem textual: "Primeiro você prepara e termina de configurar o Filhos da Impunidade".

## Plano de execução (aprovado no entendimento — Miguel: "ficou ótimo aí")

- **Fase A — Menu:** header passa a 5 itens: `📖 Livro` ▸ (Vol.1/Vol.2/Roteiro/Livro Inteiro/Gerenciar capítulos) · `🎬 Estúdio` ▸ (do Capítulo/⭐ do Estilo) · `🧠 Memória` ▸ (do Projeto/Central de Fontes/Banco de Dados) · `☁️ Sincronia` ▸ (GitHub/Drive) · `⚙️` (tema, modos, download). Ficam fora: ◀ ▶ + seletor de capítulo (uso diário). Mesmos onclick existentes — só reagrupar HTML + JS de dropdown.
- **Fase B — Estúdio do Estilo:** página full-screen (padrão `page-manual-estilo`), 4 seções: Constituição, Diretriz Editorial, Diretriz de Estilo, Prompts de Estilo (cards P1–P8 c/ Ver/Editar/Copiar/Apagar 2-toques + ➕ Novo + Restaurar originais). Persistência: padrão `getActiveManualMarkdown()` (defaults embutidos + override localStorage). Conteúdo inicial destilado de `Kimi K3/MANUAL_DE_ESTILO.md` (#1–#34), `REFERENCIA_LITERARIA.md`, `CONTRATO_DE_TRABALHO.md`, `TESE_CENTRAL.md`. Os 8 ritmos: cadências distintas (Machado longa/sinuosa · Thompson curta/pancada · César documental/fria · Perfil de cena/íntima · Geopolítica panorâmica · Maquiavel fato→mecanismo→máxima · Crônica fluida · Editorial afiado), cada um com regra das 800–1000 palavras.
- **Fase C — Memória do Projeto:** página própria, documento único indexado (aponta BANCO_DE_LINKS, MAPA_ENTREVISTAS, NOTAS, IDEIAS_E_REFLEXOES, blocos de produção por capítulo, Central de Fontes).
- **Fase D — Copiar c/ checkboxes:** junto ao `📋 Copiar Texto` (linha ~796, `copyEntireChapterText()` ~7557). Checkboxes persistem em localStorage. Seletor de prompt aparece ao marcar.
- **Fase E — API recuada:** dropdown de modelos + botão revisar → seção colapsável "⚡ Modo API (exceção)". Ciclo principal documentado na UI: instrução → copiar → colar no chat → colar resposta no textarea → Gravar revisão (saveDeepSeekRevision já existe).
- **Fase F — FUTURO (não agora):** gerador de livros.

## Estado da missão (atualizar a cada fase)

- ✅ Estudo do site + nodo do Cérebro
- ✅ Entendimento confirmado pelo Miguel + refinamentos (8 prompts, 800–1000 palavras, gerador depois)
- ✅ Checkpoint vigília: git limpo (HEAD c4bd69d), este fórum criado, monitor atualizado
- ✅ Fase A (menu 5 dropdowns; IDs legados ocultos preservados)
- ✅ Fase B (Estúdio do Estilo: 3 documentos + 8 prompts c/ CRUD)
- ✅ Fase C (Memória do Projeto num arquivo só)
- ✅ Fase D (📋 Copiar c/ caixinhas [🎼 prompts + seletor P1–P8][🧠 memória] → bloco único; estado persiste)
- ✅ Fase E (card do ciclo copiar→colar→gravar; reescrita recuada p/ "⚡ Modo API (exceção)")
- ✅ Testes Node **41/41** + commit `1cf8684` + push HEAD==origin + **AO VIVO na Vercel (200, marcadores verificados ~11:50)**
- ✅ Memória técnica `Memorias/memoria_fdi_reforma_menu_estudio_estilo_20260819.md`

## ADENDO FINAL — o que está no ar (19/08 ~11:50)

**Entregue e verificado ao vivo:**
1. **Menu enxuto:** header tinha ~15 botões → agora ◀▶ capítulo + 5 menus (📖 Livro / 🎬 Estúdio / 🧠 Memória / 👁️ Exibição / ☁️ Sincronia). Botões antigos preservados ocultos (JS intacto).
2. **⭐ Estúdio do Estilo** (menu 🎬): Constituição (10 artigos), Diretriz Editorial (tese + unidade 800–1.000 palavras + o que entra/não entra), Diretriz de Estilo (matemática da prosa) — cada uma com Editar/Copiar/Baixar/Restaurar + "📥 Baixar tudo". Conteúdo v1 destilado de MANUAL_DE_ESTILO + REFERENCIA_LITERARIA + TESE_CENTRAL — **Miguel revisa e edita na própria tela**.
3. **🎼 8 Prompts de Estilo** (aba da mesma página): Machado, Thompson, César, Cena c/ Endereço, Panorama e Facções, Maquiavel, Crônica Fluida, Editorial Afiado. CRUD livre (➕ novo, ✏️ editar, 🗑️ apagar 2-toques, ↺ restaurar os 8).
4. **📇 Memória do Projeto** (menu 🧠): acervo inteiro indexado num arquivo só, editável.
5. **Cópia com caixinhas:** no Estúdio do Capítulo, ao lado do 📋 Copiar Texto: `[🎼 Prompts de estilo]` (abre seletor Prompt 1–8) + `[🧠 Memória do projeto]` → bloco único (prompt → memória → texto) pronto p/ colar no chat.
6. **API recuada:** card do ciclo de 5 passos (instruir → copiar → colar no chat → colar resposta → gravar R#) como fluxo principal; botão de reescrita dentro de "⚡ Modo API (exceção)".

**O que falta / próximos passos:**
- ⏳ **Miguel revisar o CONTEÚDO** dos 3 documentos e dos 8 prompts (edição direta na tela; nada é fixo).
- ⏳ **Fase futura (pedido registrado):** FdI virar **gerador de livros** — botão "🧹 Limpar / Iniciar novo projeto", "usar estilo antigo" (copiar diretrizes de outro projeto), nome do projeto variável ("Filhos da Impunidade" vira o nome do 1º projeto). Terreno preparado: dados novos namespacados (`fdi_*` no localStorage).
- ⏳ Validação visual do Miguel no ar (menu, páginas, ciclo de cópia).

**Preciso de você (Miguel):** testar no ar e lapidar os textos dos documentos/prompts pela própria tela (✏️ Editar). Se quiser mudar nomes de menu ou a ordem dos ritmos, é fala direta minha.
