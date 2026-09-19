# 🗄️ FÓRUM — CENTRAL DE FONTES VIVA (Filhos da Impunidade)

**Data:** 2026-08-06 · **Agente:** ZCode/Kimi K3 · **Commit:** `8c3f335` (AO VIVO em filhosdaimpunidade.vercel.app)
**Pedido do Miguel (06/08, por voz):** "a central de fontes tinha que ter um adicionar fonte... você adiciona para onde ela entra... adicionar também um item... tem que ter um link para apagar fonte... separa: bota Livros, STF Judiciário, Justiça USA, Governo USA, PDF variados, postagem redes sociais... bota uma coisa com mais liberdade para a gente aumentar o número de fontes... e no Estúdio, naquele box da memória de fontes, o item novo já entra automaticamente no checkbox, tanto item quanto fonte individual."

## Decisões resumidas

1. **CRUD total na Central de Fontes** (`index.html`, modal-database):
   - Botão **➕ Adicionar Fonte** no topo do modal: formulário completo (título, autor/veículo, categoria, data, link, resumo, fichamento/transcrição, status, selo).
   - **"Para onde ela entra":** select com todas as categorias + opção **"✨ Criar NOVA categoria..."** (o editor cria a categoria na hora e ela vira aba de filtro automaticamente).
   - **🗑️ Apagar fonte** em todo cartão: fontes embutidas ficam só **ocultas** (restauráveis pelo botão ♻️ que surge nas abas); fontes criadas pelo editor somem de vez. Tudo com confirmação.
   - **➕ Item** em todo cartão: anexar sub-itens (PDF, link, trecho, post) com nota — "acrescentar fonte sobre o item qualquer". Cada item tem seu 🗑️.
2. **Taxonomia nova (pedido explícito):** `livros` (Livros & Bibliografia — separado de PDF), `pdfs` (PDFs Variados & Referência), `stf` (STF & Judiciário), **`justica_usa` (Justiça USA)**, **`governo_usa` (Governo USA)**, `redes` (Postagens Redes Sociais — ex-"X"), mais `yt`, `tarifaco`, `dinheiro`, `outros`. Remap das 44 fontes embutidas aplicado **na leitura** (`BUILTIN_CATEGORY_REMAP`) — o acervo original do código fica intacto.
3. **Integração Estúdio (a parte que o Miguel mais enfatizou):** seção nova **"➕ Suas fontes & itens da Central"** dentro do box "🧠 Consultar memória e banco de fontes canônicas" — cada fonte individual E cada item anexo criado na Central vira **checkbox automaticamente** (marcado por padrão), entra no "Marcar todos", persiste no navegador e é **injetado no prompt da reescrita** (fichamento + notas viram memória factual da IA).
4. **Persistência:** 4 chaves localStorage (`miguel_fontes_custom_v2`, `miguel_fontes_hidden_v1`, `miguel_fontes_items_v1`, `miguel_fontes_custom_cats_v1`) + seleção do Estúdio estendida. Nada se perde ao recarregar.
5. **Qualidade:** IDs únicos anti-colisão (timestamp+random — bug achado no teste: dois itens no mesmo ms colidiam e o checkbox resolvia errado); escape HTML nos campos do editor; link sanitizado (só http/https).
6. **Testes:** suíte Node com DOM-stub (`scratch/teste_central_fontes.js`) — **18/18 fluxos OK** (abas, CRUD fonte/item em fonte sua e embutida, entries do Estúdio, injeção no prompt, apagar/restaurar, persistência). O clique do browser IAB do ambiente estava quebrado (falhou até em botões antigos — limitação do ambiente, não do código).

## Pendências / próximos passos

- [ ] Miguel testar ao vivo no navegador real (adicionar 1 fonte real — ex.: primeiro livro da bibliografia em `livros`, primeiro processo DOJ em `justica_usa`).
- [ ] Se quiser, popular `justica_usa` com USA v. Guo / processos Texas (material existe em `Fontes/Variados/Docs/`).
- [ ] Futuro: exportar/importar as fontes custom em JSON (hoje só localStorage do navegador).

**Memória técnica:** `Memorias/memoria_central_fontes_viva_20260806.md`

## ADENDO 06/08 ~19:00 — UPLOAD DE ARQUIVO DO COMPUTADOR (commit `da37afd`, AO VIVO)

Pedido do Miguel: "bota também a possibilidade de eu subir o arquivo que está no meu computador — fica mais fácil".
- **Input de arquivo** no form Adicionar Fonte **e** em cada mini-form de item anexo (PDF, TXT, MD, CSV, JSON, SRT, RTF, DOC).
- **Onde fica:** IndexedDB do navegador (`fdi_fontes_files`) — localStorage é pequeno demais p/ PDF; sem servidor e sem segredos. Arquivo ganha chip 📁 com botão **Abrir** no cartão.
- **Leitura automática p/ o Estúdio:** TXT/MD/CSV vão direto p/ o fichamento (cap 30 mil chars p/ caber no prompt); **PDF tenta extração automática via pdf.js** (CDN, até 40 págs/30 mil chars) com status ao vivo; falha não impede o anexo.
- Apagar fonte/item remove o blob do IndexedDB; anexo mencionado nas entradas do checkbox do Estúdio.
- Testes Node: **21/21** ✅. Pendente: Miguel testar com um PDF real no navegador dele.

## ADENDO 2 — 06/08 ~19:40 — UX DO FORM + AUDITORIA DE LINKS YOUTUBE (commit `0b80101`, AO VIVO)

Pedidos do Miguel: (1) botão "Adicionar Fonte" tem que mudar quando o form abre ("se clico de novo, volta"); (2) a lista de fontes apertada embaixo do form ("janelinha") não faz sentido; (3) fontes com vídeo indisponível no YouTube ("Turning Point Tampa", "Tucker Carlson") — "está dando link errado, vê isso para consertar".
- **Botão bidirecional:** "➕ Adicionar Fonte" ↔ "⬅️ Voltar ao menu de fontes" (rótulo e cor mudam).
- **Sem janelinha:** com o form aberto, lista e filtros saem da tela — o formulário ocupa o modal inteiro.
- **Auditoria oEmbed dos 23 links YouTube:** 9 OK originais; **3 substituídos por vídeos REAIS verificados** (Tucker Carlson entrevistando Eduardo+Paulo Figueiredo; Fox Business/Lou Dobbs c/ Eduardo legendado; Monark×Eduardo — Cortes do Flow oficial); **13 sem link real localizado** (YouTube/DDG/Bing bloquearam as buscas automatizadas) → marcados `broken:true`, botão vira badge desabilitado **"⚠️ Link indisponível"** (não leva mais à página de erro do YouTube; fichamento/transcrição preservados; tooltip orienta anexar link certo como ➕ Item). **Decisão editorial:** não inventar link (estatuto dos fatos) — quando o Miguel tiver o link certo, entra como item.
- Testes Node: **30/30** ✅. Pendente: links certos dos 13 (Miguel) → trocar ou anexar.
