# 🎨 PROMPT — CHECAGEM VISUAL do MOKA OUASADIA (Antigravity Desktop, você é bom de visão!)

> Colar este prompt inteiro numa conversa NOVA do Antigravity Desktop.
> Papel do AGY aqui: **OLHO INDEPENDENTE** — ANALISAR e dar parecer, NÃO editar código.
> Nenhuma credencial é necessária nem deve ser usada: o alvo é um site público.

---

PROMPT (cole a partir daqui):

Você é o revisor visual independente do Moka (app de leitura da casa). O ZCode/GLM-5.3 acabou de fazer uma reforma no ambiente de testes (**Ousadia**) e o Miguel quer um parecer VISUAL seu, item por item, antes de aprovar. **Sua missão é SÓ ANALISAR — não mexa em código, não corrija nada.** Se achar defeito, DESCREVA o que viu e sugira o conserto; quem decide é o Miguel.

**Alvo:** https://moka-ousadia.vercel.app (se aparecer versão velha, aguarde 1 min e recarregue — deploy novo de 31/08 ~11h)

**Como analisar:** abra no navegador (janela estreita de celular ~375px E janela larga de desktop ~1366px) e tire print de cada página. Compare TODAS estas páginas entre si: `/` (capa), `/estante`, `/biblioteca`, `/ajuda`, `/video`, `/memoria`, `/harness`, `/writer`, `/configuracoes`.

**CHECKLIST — dê ✅ ou ❌ por item, com print de prova e 1 frase do que viu:**

1. **Menu lá de cima IGUAL em todas as páginas — EXCETO a capa, que agora é LIMPA (sem menu no topo, ordem do Miguel)** — mesma barra, mesma posição, mesmos 5 ícones (📖 🎬 🧠 💬 ✍️), mesmas ações à direita (voltar, conta, bandeirinha de idioma, engrenagem, telemetria). Antes: cada página tinha um menu diferente. Ainda está diferente em alguma?
2. **UMA cor de fundo só** — antes a Biblioteca e a Ajuda eram beges e o resto azulzinho. Ainda existe página com cor destoante?
3. **UM logo só por página** — antes o Vídeo tinha DOIS Mokas no alto (um pouco diferentes entre si) e as Configurações tinham logo na esquerda E na direita. Ainda sobra logo duplicado em qualquer página?
4. **Dentro do leitor** (teste no CELULAR e no desktop!) (suba um EPUB leve em `/estante` — botão de adicionar livro — e abra o livro): a fileira de cima agora deve ter **3 BOTÕES GRANDES no centro**: **📖 Página** (abre submenu: ler em voz alta, resumir/explicar, traduzir a página, traduzir o livro), **📌 Marcar** (abre submenu: marcar página, tirar foto, notas) e **🎤 Perguntar** (abre direto a janelinha de pergunta). Eles estão GRANDES e bem visíveis? Os submenus 📖 e 📌 ABREM certinho (inclusive no celular/iPad — antes eram cortados pela fileira rolável) e fecham ao clicar fora? No celular os 3 ficam numa linha própria embaixo? A chave de zoom vertical (canto direito) continua visível, SEM o menu por cima dela?
5. **Lado direito do leitor**: agora é **UM botão só (☰)** que abre um menu com: Ajuda, Suas IAs/telemetria, Mural das IAs e Configurações — a bandeirinha de idioma e o login ficam soltos ao lado. Está assim? Ainda tem fileira de ícones pequenos sobrando?
6. **Configurações** (`/configuracoes`): menu padrão igual às outras páginas, sem logo repetida? Deve existir uma seção **"☁️ Memória na nuvem"** com provedor (Cloudflare R2 / Backblaze B2 / Outro S3), campos de chave, bucket e botões "Testar conexão" e "Salvar".
7. **Barra de progresso de upload**: em `/estante`, suba um PDF GRANDE (de centenas de páginas). Deve aparecer uma **barrinha com percentual subindo** e a etapa escrita ("Abrindo o livro…", "Verificando as páginas…", "Preparando a capa — página X de Y…", "Salvando na estante…"). Ele aparece? Para mudo em alguma etapa?
8. **Capa** (`/`): SEM menu no topo (limpa!), e com 6 botões GRANDES TODOS DO MESMO TAMANHO e bonitos (Reader, Vídeo, Memória, Harness, Writer + Configurações, cada um com ícone grande em cima), SEM foto ilustrativa. Está assim?
9. **Página Memória** (`/memoria`): devem existir 2 botões de nuvem no topo ("☁️ Salvar na nuvem" e "⬇️ Restaurar da nuvem") e, sem configuração de nuvem, um link "Configurar nuvem →".

**Formato do seu parecer** (devolva EXATAMENTE assim):
- Tabela: item 1-9 → ✅/❌ → o que você viu (1 frase) → print anexado
- No fim: lista de defeitos encontrados (se houver) ordenados por gravidade, cada um com sugestão de conserto VISUAL (não mexa no código)
- Nota geral de 0 a 10 do visual da família Moka pós-reforma

**Contexto da casa:** o Moka tem 5 módulos com a MESMA importância (Reader, Vídeo, Memória, Harness, Writer); o rito é Ousadia (testes) → Espelho → Canônico (mokareader.com); tudo 100% local no aparelho do usuário (livros, chaves IA, nuvem BYO-bucket). Se quiser contexto completo: `Downloads/Antigravity Google/Cerebro/Foruns/forum_obra_moka_chefia_zm_20260830.md` (adendos 6 e 7).

---
