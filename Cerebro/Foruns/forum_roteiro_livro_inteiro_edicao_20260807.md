# 📝 FÓRUM — ROTEIRO + LIVRO INTEIRO: ANOTAÇÕES CRUD, EDIÇÃO E SEPARAÇÃO LER/COMPILAR (Filhos da Impunidade)

**Data:** 2026-08-07 · **Agente:** ZCode/Kimi K3 · **Commit:** `877f1f0` — AO VIVO (Vercel, verificado via curl: labels novos, modais, `.fdi-ui`, zero "Ler / Compilar")
**Pedido do Miguel (07/08, na página do roteiro `cap=00_frontmatter`):** "coloca também ver anotações... uma listinha das anotações anteriores... ver, editar e apagar. É importante, senão eu não vou poder usar. Tem que editar o roteiro, tem que ter um botãozinho. Tem que estar separado ler o livro inteiro / compilar o livro inteiro... Tem que ter o botão de editar também, o livro inteiro. Esse revisar ficou fora do quadrado, bota ele numa segunda linha... em vez de revisar com IA, um estúdio — você clica, vai para um estúdio igual aqueles dos capítulos, só que o livro inteiro. E esse card aqui está sem contraste, bota essa letra branca."

## Decisões resumidas

1. **Anotações do roteiro viraram LISTA** (`miguel_roteiro_anotacoes_v1`): cada "💾 Salvar Anotação" cria um item novo; lista abaixo da caixa com **👁️ Ver / ✏️ Editar / 🗑️ Apagar** por item. Editar carrega o texto na caixa e o botão vira "💾 Salvar Edição" (atualiza a mesma, não duplica). Apagar = 2 toques no próprio botão (padrão do app — `confirm()` é suprimido em webviews). **Migração automática:** a caixa única antiga (`miguel_roteiro_observacoes`) vira a 1ª anotação com selo `migrada` — nada se perde.
2. **✏️ Editar Roteiro** (header + seção "📜 Texto do Roteiro"): modal com o texto integral do frontmatter; salvar cria override `miguel_roteiro_texto_override_<vol>` (+ ts) — o original embutido NUNCA é tocado; "↩️ Restaurar Original" (2 toques) descarta o override.
3. **Ler separado de Compilar:** o botão da barra de topo "📚 Ler / Compilar Livro Inteiro" virou **"📖 Ler Livro Inteiro"** (só abre a visão compilada). A regeneração mora no **"⚡ Atualizar Compilação"** da capa do compilado. Se houver edição manual ativa, atualizar exige 2 toques (avisa que descarta a edição).
4. **✏️ Editar Livro Inteiro:** modal com o texto exibido; salvar grava `miguel_fullbook_manual_edit_<vol>` (+ ts) **por cima da compilação** — banner âmbar avisa que você está lendo a edição manual; capítulos canônicos e versões R# intactos; "↩️ Voltar à compilação canônica" (2 toques) descarta.
5. **Downloads respeitam a edição ativa:** "📥 Baixar Livro Inteiro" baixa o texto EXIBIDO (sufixo `_editado` no nome quando é edição manual); novo `downloadRoteiro()` — o "Baixar Roteiro (.md)" do header agora baixa o roteiro de fato (antes baixava o livro inteiro compilado).
6. **🎬 Estúdio do Livro Inteiro NUNCA auto-revisa:** o botão roxo abre o Estúdio Editorial apontando para o livro inteiro (mesmo fluxo dos estúdios por capítulo) — modal de aviso reescrito deixando explícito que nada é revisado automaticamente; a reescrita só acontece se o Miguel disparar lá dentro (com confirmação final antes de consumir tokens).
7. **Botões na 2ª linha do card compilado** (como pedido) em fileira `flex-wrap` — nada mais vaza do card.
8. **FIX contraste (causa-raiz):** o título "Livro Inteiro Compilado" renderizava âmbar-escuro `rgb(133,77,14)` apesar do `text-white` — `.prose-book h2` (especificidade 0,1,1) vence a utility do Tailwind (0,1,0) porque os cards UI são renderizados DENTRO de `#reader-content.prose-book`. Correção: classe marcadora **`.fdi-ui`** nos cards de UI + regra `.prose-book .fdi-ui h1..h4/p { color: inherit; margin: 0 }` (sem matar a `font-display`/Cinzel). Confirmado AO VIVO via computed style antes/depois.

## Provas

- Testes Node: **24/24** (`scratch/teste_roteiro_livro_edit.js` — CRUD de anotações, overrides roteiro/livro, 2-toques, downloads, asserts de fonte) + regressões upload-versão **14/14**, drive-sync **9/9**, api-drive **6/6**, central-fontes ok.
- Ao vivo (curl): `fdi-ui` ×9, "📖 Ler Livro Inteiro" ×2, modais `editar-roteiro`/`editar-livro`, `atualizarCompilacao(this)`, "Ler / Compilar" = 0 ocorrências.

## Pendências / próximos passos

- Nenhuma pendência técnica. Opcional futuro: export/backup das anotações do roteiro junto com o pacote de sync (hoje vivem só no localStorage).

**Memória técnica:** `Memorias/memoria_roteiro_livro_inteiro_edicao_20260807.md`
