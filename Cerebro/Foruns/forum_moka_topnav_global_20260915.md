# 🌐 Fórum — Moka: menu no alto em TODAS as páginas (TopNav global)

**Data:** 15/09/2026 · **Quem:** ZCode/GLM-5.3 (Dell) · **Ambiente:** ousadia (moka-ousadia.vercel.app), AGUARDA OK do Miguel p/ promover

## 1. O pedido do Miguel (15/09 ~10:0x, voz)

"Conserta no Moka, mas começa pela ousadia. Nas configurações tem que ter o menu, tem que continuar aparecendo no alto. Ou pelo menos o home, pra voltar pra home. Na home tem que colocar o ícone do lado da bandeira das configurações, que tem que aparecer em toda parte. Quando você entra no MokaReader e abre a primeira estante, não tem menu nenhum — tem que ter a configuração na prateleira, na página de estante, o ícone de configuração. Em vídeo também... não tem a bandeirinha de idiomas nem configuração em cima. Em todos: bandeirinha de idiomas e configuração. E home também, pra voltar pra home."

## 2. Diagnóstico (causa tripla)

1. **Menu "CLEAN" nascia ESCONDIDO** — reforma 31/08 deixou o TopNav `hidden=true` por padrão (só o olhinho 👁️ aparece; preferência `moka.navHidden` gravada no aparelho). Para visitante novo, TODAS as páginas TopNav ficavam "sem menu em cima".
2. **A prateleira do livro (book/[id]) era `workspace-no-topbar` por design** — a rota mais usada não tinha menu NENHUM (nem olhinho).
3. **Faltava o botão 🏠 home** no conjunto padrão (bandeira + engrenagem existiam, home não).

## 3. A cura (commit 9e4eb2e + 2207b59, branch ousadia; base = ousadia 4d01f54 + merge do main 5d80145)

1. **TopNav visível por padrão** — `useState(false)` + **chave NOVA `moka.navHidden2`** (zera o "escondido" gravado nos aparelhos pela era CLEAN; quem quiser leitura limpa aperta o olhinho, persiste).
2. **Botão 🏠 home** adicionado em `TopNav` (default) e `TopNavActions` — 🏠 + bandeirinha + ⚙️ juntos, em toda parte.
3. **book/[id] ganha TopNav** (`active="reader"`) no return principal E nos 3 estados antecipados (loading/loadStuck/notFound) — a prateleira nunca mais fica órfã.
4. **Padronização**: tutorial, experimente, auth/confirmado, auth/atualizar-senha e sobre trocaram topbars manuais pelo TopNav padrão (estante/biblioteca/vídeo/configurações/ajuda/writer/harness/telemetria/memória/mural já usavam). Privacidade já tem bandeirinha no PrivacidadeConteudo (2164349). Capa (home) mantém a dela (identidade).
5. **Pré-sync**: merge do main ANTES (fluxo da casa: canônico→…→ousadia para curas) — o ousadia estava sem a cura do dropdown 5d80145 e a do zoom a7f05a3; npm install necessário (undici).

## 4. Provas

- Build local verde (27/27 rotas) ×2.
- Deploy ousadia: `vercel ls moka-ousadia` mostrou que **push NÃO dispara** o projeto (deploys de 39-47s = CLI). Receita usada: backup `.vercel/project.json` → `npx vercel link -p moka-ousadia --yes` → `npx vercel deploy --prod --yes` (Ready 47-60s) → restaurar link moka-v3 + apagar `.env.local` criado pelo link (ruído).
- HTML servido: marcador `Início — voltar para a página central` + 🏠 presentes em `/estante`, `/sobre`, `/tutorial`, `/experimente`, `/video` e `/book/teste-zm` (estado de erro incluído) — curl no ar, 15/09 ~11:3x.

## 5. Estado — o que falta / preciso do Miguel

- **PRONTO e NO AR no ousadia**: https://moka-ousadia.vercel.app — Miguel testa (estante, prateleira, vídeo, configurações: 🏠 + bandeirinha + ⚙️ no alto de tudo).
- **AGUARDA OK do Miguel** → promover (fluxo da casa: ousadia→espelho→canônico = www.mokareader.com).
- Aprovada a promoção, o botão 🏠 também passa a valer para o leitor de vídeo em tela cheia (o player continua cobrindo a tela inteira em fullscreen nativo — comportamento do navegador, não do app).


## ✅ PROMOÇÃO CONCLUÍDA — 15/09/2026 11:27 BRT (OK do Miguel: "ficou bom, pode espelhar agora para o espelho 1 e para o canônico")

1. **Repos:** espelho 2 (moka-ousadia) main = 8791f07 · espelho 1 (moka-espelho) main = 9a4d86e (merge, histórico preservado, rito da casa) · canônico (moka.git) main = 8791f07 (FF limpo).
2. **🔴 Incidente no caminho, curado:** o deploy CLI da manhã partiu do branch ousadia do moka.git (4d01f54+merge main), que NÃO continha a7f05a3 (cura do zoom da madrugada, commitada só no repo moka-ousadia) → o ousadia ficou ~1h com o zoom REGREDIDO. Cura: cherry-pick a7f05a3 (7f151f9, globals.css puro, zero conflito) + **merge de reintegração do commit original** (8791f07 — histórico nunca se perde) + redeploy.
3. **Provas no ar (curl, 15/09/2026 11:27):** marcador `Início — voltar para a página central` (🏠 home do TopNav) presente em /estante dos TRÊS domínios (moka-ousadia + moka-espelho + www.mokareader.com) · CSS do zoom `50vw / var(--ui-font-scale` presente no chunk CSS dos TRÊS (grep flexível de minificação — com espaços fixos dá falso negativo).
4. **Lição nova gravada:** antes de deployar em ambiente da casa, conferir a LINHAGEM REAL dele (ls-remote + merge-base) — o main do repo-espelho pode estar À FRENTE do branch homônimo do repo central (foi o caso: a7f05a3 existia só no moka-ousadia).


## 🔧 Adendo — round 2 do QA do Miguel (15/09/2026 19:12, print 19:04) — telemetria/mural padronizadas + Mural vira 6º ícone

1. **O que ele viu na /telemetria:** right próprio degradado — Moka solto linkando à estante + ✕ + label "📊 Suas IAs" escrito, SEM engrenagem; e o acesso ao Mural era um botão ESCRITO no corpo ("era pra ter apenas o ícone").
2. **Cura (commit 0da2584, ousadia):** (a) telemetria e mural-das-ias trocaram o right custom pelo `TopNavActions` padrão (🏠 voltar conta bandeirinha ⚙ telemetria) — Moka-perdido, ✕ e labels escritos FORA; (b) **Mural das IAs entrou na FAMÍLIA como 6º ícone 🏆** no SectionSwitcher (href /mural-das-ias, chave i18n sec_mural criada nos 12 idiomas); (c) botão escrito do mural no corpo da telemetria removido (o ícone no alto de TODAS as páginas cobre).
3. **Provas (curl cache-buster):** telemetria 🏆=1 ⚙️=2 label-degradado=0 · mural 🏆 ⚙️ sem degradado · estante família com 🏆 e 🏠.
4. **Estado:** NO AR no ousadia — Miguel recarrega (Ctrl+F5, a borda cacheia HTML) e confere; com o OK, promoção espelho1+canônico leva topnav+farol juntos.


## 🔧 Adendo — round 3 (16/09/2026 11:39): meio termo do painel de seleção no tablet (print 794px, pasta MOKA marketing/correcoes)

1. **Bug do Miguel:** no iPad, o 2º ícone de tamanho da janelinha de seleção (Perguntar/Traduzir/Explicar) ficava IGUAL ao 1º — "era pra aumentar um pouquinho, tipo metade da página".
2. **Causa raiz:** no mobile (media ≤900px) o overlay até subia o TETO (max-height 40→70vh), mas o card .ai-panel é height:auto do conteúdo — nunca esticava. No desktop funciona porque .ai-panel-overlay .ai-panel { height:100% } (fora do media).
3. **Cura (commit dec68ca, ousadia, CSS puro):** alturas PRÓPRIAS por modo no mobile — meio = 50vh (metade da página, teto 70vh) · tela cheia = calc(100vh-20px) · pequeno segue auto (teto 40vh). Prova: regra height:50vh presente no chunk CSS servido do ousadia (b2772adb).
4. **Estado:** ousadia aguardando Ctrl+F5 do Miguel no iPad; a promoção geral (topnav r1+r2+farol+meio termo) sai junta com o OK dele.


## 🔧 Adendo — round 4 (16/09/2026 11:42): página de telemetria ganha título próprio e subtítulo

1. **Ordem do Miguel (~11:4x, voz):** "essa página de telemetria tem que vir o título lá, telemetria. Aí bota um subtítulo: acompanha aqui o gasto de cada tarefa executada, por modelo, por LLM, por data e por tarefa. Acompanhe cada despesa feita em sua IA."
2. **Cura (commit 67f5dd5, ousadia):** `lib/telemetry-strings.ts` — tele_page_title "Suas IAs"→"Telemetria" e tele_intro → "Acompanhe cada despesa feita em sua IA: o gasto de cada tarefa, por modelo, por LLM e por data." nos 12 idiomas (armadilha: metade dos tele_intro era multiline — segunda passada pegou).
3. **Prova no ar:** curl no /telemetria do ousadia mostra título e subtítulo novos.
4. Pendência geral inalterada: tudo (topnav r1+r2, mural 6º ícone, farol, meio termo, título telemetria) promove junto com o OK do Miguel.


## 🔧 Adendo — round 5 (16/09/2026 11:46): setinha de voltar em primeiro lugar, à esquerda do olhinho

1. **Ordem do Miguel (~11:5x):** "essa setinha de voltar, que está no menu da direita superior, bota em primeiro lugar. Bota ele à esquerda do olho."
2. **Cura (commit d78a191, ousadia):** BackButton migrou do TopNavActions para o TopNav — primeiro filho do grupo da direita, antes do 👁️. Prop `back` do TopNavActions virou no-op (compat com back={false} de video/[id], que agora herda o voltar padrão — voltar da página de vídeo leva à lista, útil).
3. **Prova no HTML servido:** grupo abre com "← 👁️" e segue 🏠 conta bandeira ⚙.


## ✅ PROMOÇÃO FINAL — 16/09/2026 11:52 BRT (OK do Miguel: "ok, pode espelhar com os outros, espelho 1 e canonico")

1. **Repos:** canônico moka.git main = d78a191 (FF) · espelho 1 moka-espelho main = cce3b12 (merge, histórico preservado; 1º push falhou por digitação no nome do branch — refeito) · repo ousadia = d78a191.
2. **Leva promovida (rounds 2-5 + farol):** telemetria/mural padronizadas no TopNav (fim do Moka solto/✕/label, ⚙ de volta) · Mural das IAs = 6º ícone 🏆 da família (i18n 12 idiomas) · meio termo da janelinha de seleção no tablet = 50vh (metade da página) · título Telemetria + subtítulo do Miguel · seta de voltar em 1º lugar, à esquerda do olhinho · pixel FAROL-MOKA no layout (a primeira visita real acende o contador; conferir com GET /api/moka-resumo).
3. **Prova nos 3 domínios (curl cache-buster):** troféu 🏆 · título>Telemetria< · subtítulo · height:50vh no CSS · seta antes do olho · farol-moka no chunk layout — TUDO ✓ em www.mokareader.com, moka-espelho.vercel.app e moka-ousadia.vercel.app.


## 🔧 Adendo — round 6 (16/09/2026 11:57): cards da Telemetria e do Mural das IAs na home (só ousadia, p/ o Miguel ver)

1. **Ordem (~12:0x):** "na home, entre aqueles cards, tinha que ter um card da telemetria e outro do mural das IAs. Faz isso na ousadia para eu ver como fica."
2. **Feito (commit 891c9c6, SÓ no ousadia):** Capa.tsx ganhou 2 cards no mesmo molde da família (capa-launch-btn) — 📊 Telemetria → /telemetria ("Acompanhe cada despesa feita em sua IA") e 🏆 Mural das IAs → /mural-das-ias ("Ranking e calculadora de custo das IAs"), entre o Moka Writer e a ⚙️. Descrições i18n nos 12 idiomas (chaves capa_tele_desc/capa_mural_desc).
3. **Prova:** HTML servido com os 2 cards completos (prerender EN; hidrata troca pro idioma do usuário, igual aos demais cards).
4. **Estado:** AGUARDA o Miguel ver no ousadia (Ctrl+F5) — aprova, promove aos outros 2.


## 🔒 Adendo — round 7 (16/09/2026 12:01): TRANCA DO CÓDIGO (ordem Miguel: "tranca o código para ninguém copiar o código do Moka")

1. **Resposta à pergunta dele (estava trancado?):** NÃO — repos PÚBLICOS + licença MIT (= autorização legal explícita para copiar/usar/vender). Escancarado nas duas camadas.
2. **Tranca dupla executada:** (a) LICENSE MIT → **TODOS OS DIREITOS RESERVADOS** (commit 7a73352, backup LICENSE.bak_pre_tranca_20260916; promovido: canônico main 7a73352 FF, espelho1 db6e4f1 merge, repo ousadia 7a73352); (b) **repos → PRIVATE**: moka, moka-espelho, moka-ousadia, mokawriter (moka-video já era) — provado por gh (todos PRIVATE).
3. **Prova de que chegou limpa:** 0 forks e 0 stars em TODOS os repos (ninguém bifurcou publicamente antes da tranca) · site www 200 no ar com os cards da home já promovidos (round 6: canônico 891c9c6→7a73352, espelho1 da71433→db6e4f1).
4. **Limites honestos registrados:** (a) o SITE serve HTML/JS minificado ao navegador de qualquer visitante — natureza da web, irreversível para qualquer site (o que fica trancado é o FONTE completo: comentários, estrutura, histórico, server-side); (b) quem VISITOU o repo público antes pode ter baixado sem fork — sem rastro mensurável (forks=0 é o melhor sinal disponível); (c) clones privados de terceiros (agentes da casa) não são afetados pois autenticados.


### 📊 Como sabemos se alguém copiou (pergunta do Miguel, 16/09/2026 12:03) — os números reais do GitHub (janela de 14 dias da API de traffic)

- **Visitas à página dos repos: 0 únicos nos 4** (moka, moka-espelho, moka-ousadia, mokawriter) — ninguém abriu o repositório no navegador nos últimos 14 dias.
- **Clones git: dezenas (96/45/57/7 únicos)** — majoritariamente a PRÓPRIA CASA (sessões/robôs que baixam o repo para trabalhar; a API não separa casa×estranho). 0 forks = nenhuma cópia pública mantida.
- **Leitura honesta:** certeza absoluta não existe na internet e a janela da API é 14 dias; mas 0 views + 0 forks + 0 stars + site com ~36 sessões em agosto e 0 em setembro (GA4) = deserto de audiência — não havia gente olhando para existir cópia. A partir da tranca (private + todos os direitos reservados), nem isso é mais possível.


### ⚖️+🔍 Parecer: registro de propriedade + pesquisa de concorrentes (16/09/2026 12:07)

**Registro (pergunta: "como registra a propriedade do site? no Brasil, no mundo? ou não é praxe?"):** Software NÃO se registra para ser protegido — no Brasil (Lei 9.610/98) e no mundo (Convenção de Berna) o direito autoral nasce no ato da criação, automaticamente. Registro é FACULTATIVO e só serve de PROVA de anterioridade: INPI (programa de computador, online, barato) ou Biblioteca Nacional; marca "Moka" no INPI só se decolar (caro, 1-2 anos). Praxe de projeto gratuito indie: NÃO registrar. **O essencial já está feito** (repo private + licença Todos os Direitos Reservados + histórico git datado). Conselho dado: nada agora; INPI opcional no futuro como selo de prova (nota: repo private enfraquece prova pública de anterioridade — INPI ou tag pública de release cobre isso se um dia importar).

**Concorrentes (busca real 16/09):** mais próximos em LIVROS+IA+BYOK: BookWith (open source, HN), Lumina Reader (open source, EPUB/PDF+sidebar IA), Readest, ReadAny, Foxycape (local-first). Em VÍDEO+BYOK: extensões Claras, SkipYT, Contextly, LiteScribe (+ free sem key: Glasp, Video Highlight, NoteGPT). **Nenhum achado junta o conjunto do Moka** (livros+vídeo+memória+12 idiomas+PWA local-first num app web único e gratuito); os próximos são leitores de livro open-source com IA. Maioria open source por design — o valor do Moka está na experiência curada, não no segredo do código.


## 🔧 Adendo — round 8 (16/09/2026 12:16): Quem Somos — último card da capa + 👥 no menu + página reescrita (só ousadia)

1. **Ordem (~12:1x, voz):** último cardzinho da home = Quem Somos + no menu também; página explicando quem é ele; data da 1ª subida (achada no git: **bootstrap 13/07/2026** → "desenvolvido a partir de julho de 2026"); e-mail info@mokareader.com; jornalista carioca que vive em Niterói; sites da casa; objetivo difusão do conhecimento, sem fins lucrativos, premium eventual; "quem somos em todas as línguas".
2. **Feito (commit 030b416, ousadia):** (a) Capa: card 👥 Quem Somes (nav_about, 12 idiomas; descrição nova capa_about_desc 12 idiomas) como ÚLTIMO card; (b) TopNav default + TopNavActions ganham 👥 → /sobre (menu em todas as páginas); (c) /sobre reescrito: "jornalista, e agora também desenvolvedor de aplicativos", carioca de Niterói, "desenvolvido a partir de julho de 2026 e no ar desde então", contato info@mokareader.com (troca o e-mail antigo), links O Cafezinho (www.ocafezinho.com, principal PT) + Global South News + Rio Carta + TV Fórum, missão com "não tem fins lucrativos... eventualmente produto premium" (domínios conferidos 200 antes de colar).
3. **Provas no ousadia (curl cache-buster):** card /sobre na home ✓ 👥 ✓ · /sobre: julho de 2026 ✓ info@mokareader ✓ GSN ✓ Rio Carta ✓ fins lucrativos ✓ · menu da estante com 👥 ✓.
4. **Estado:** ousadia aguardando OK do Miguel → promove aos 3 (junto com nada mais pendente — rounds anteriores já promovidos).


## 🔧 Adendo — round 9 (16/09/2026 12:34): QA do Miguel da manhã — dicionário PT + Quem Somos família completa + espelhado aos 3

1. **QA dele:** subtítulo do card em inglês com bandeira PT (bug: minha heurística de idioma não achou o bloco pt-BR no ui-strings → capa_tele/mural/about_desc ficaram EN em todos) + "dois em um" desatualizado (agora são Reader/Video/Memória/Harness/Writer) + link do CMG.
2. **Cura (c2d80a2, PROMOVIDA aos 3 — espelho1 4114c3f):** 36/36 chaves traduzidas nos 12 idiomas de verdade · /sobre com "um ambiente completo de leitura e estudo com IA" e os 5 módulos explicados + telemetria/mural de apoio · Cafezinho Media Group linkado (ocafezinho.com — sem domínio próprio no Cérebro, o portal É o link).


## 🔧 Adendo — round 10 (16/09/2026 12:41): Cafezinho Media Group ganha o endereço PRÓPRIO (Miguel passou)

**Miguel (~12:4x):** "https://cafezinhomediagroup.vercel.app/ — aqui o endereço do Cafezinho Media Group. Pode linkar no cérebro e botar lá." · Site confirmido no ar (200, título 'Cafezinho Media Group | Central de Portais de Mídia Independente').
**Feito (335e0d1, PROMOVIDO aos 3 — espelho1 d4d5cf9):** /sobre do Moka linka o grupo ao endereço próprio (antes apontava ao portal ocafezinho.com pela falta de registro do domínio do grupo no Cérebro). **📌 REGISTRO CANÔNICO PARA A CASA: o site do Cafezinho Media Group é https://cafezinhomediagroup.vercel.app/ (central de portais de mídia independente).**


## 🔧 Adendo — round 11 (16/09/2026 14:08): Quem Somos BILÍNGUE (QA do Miguel: bandeirinha em inglês não mudava a página)

1. **QA dele (~12:5x):** "estou no Quem Somos, mudei a bandeirinha para o inglês e a página continua a mesma."
2. **Causa:** a página era server component com texto FIXO em PT — não escutava o i18n (a bandeirinha só trocava rótulos da interface).
3. **Cura (b52519a, PROMOVIDO aos 3 — espelho1 d3a85a6):** conteúdo extraído para `SobreConteudo.tsx` (client, `useI18n`) no MESMO padrão da Privacidade (`lang.startsWith('pt')` → bloco PT senão EN — demais idiomas caem no EN). Page vira wrapper server (metadados SEO preservados). Tradução EN completa e fiel (família de módulos, criador, sites, CMG, missão sem fins lucrativos).
4. **Prova:** /sobre dos 3 domínios contém ambos os blocos (Who We Are + Quem Somos — o render escolhe no cliente pelo idioma da bandeirinha).


## 🔧 Adendo — round 12 (16/09/2026 15:22): olho do leitor reconfigurado (bug do Miguel: "não está escondendo nada")

1. **QA dele (~15:1x, print 15:06):** o 👁 da chave de zoom (ao lado do Aa) "não tem função — clico e não muda nada. A gente mudou o menu de cima e ele perdeu a razão de ser. O olho de cima esconde o menu de cima; o de baixo deveria esconder o de baixo — tem um bug, reconfigura."
2. **Causa:** o botão era o "destravador universal" de 25/08 (fora de fullscreen SÓ trazia o menu; com o menu já visível, clique = nada visível). Pós-reforma do menu, virou botão morto na prática.
3. **Cura (5d941ed, PROMOVIDO aos 3 — espelho1 d1eea46):** handler agora é SEMPRE `setMenuVisible(v => !v)` — alternância honesta dentro e fora da tela cheia; o antigo destravador continua funcionando como efeito natural (estado preso, um clique traz). De volta: a xicrinha ☕ flutuante (desenho original) reaparece quando o menu está oculto.
4. **Prova:** código do olho confirmado no bundle servido do canônico.


## 🔧 Adendo — round 13 (16/09/2026 16:00): o MOKA do menu vira identidade — caixa alta, fonte da capa, azul-safira da xicrinha

1. **Ordem (~15:3x, voz):** "deixa a xicrinha só... o ideal: xicrinha + MOKA juntos, caixa alta, mesma fonte da capa, nesse azulzinho igual o da xicrinha. Não mexe na xicrinha, depois a gente mexe ela."
2. **Cura (debf632, PROMOVIDO aos 3 — espelho1 625c11e):** `<span class="brand-word">MOKA</span>` no TopNav + CSS: fonte var(--font-brand) weight 600 (a da capa), cor #1e3a8a (o azul-safira do PRÓPRIO gradiente da xícara — coeso por construção), dark-mode #93c5fd; o antigo era gradiente laranja destoando. Xicrinha intocada por ordem expressa (nota: o Miguel sinalizou mexer nela depois — "xicrinha não está com uma cor bonita... depois a gente mexe").
3. **Prova:** brand-word no HTML e no CSS servido dos 3 domínios.

## 🔧 Adendo — round 14 (18/09/2026 13:0x): UMA barra de menu só dentro do leitor (PRONTO da ponte, DSH-us65)

1. **Ordem (Miguel, 18/09 ~10:3x, via DSH-us65 → PRONTO_MENU_MOKA_LEITOR_20260918.md):** com o livro aberto ficavam DUAS linhas de menu empilhadas (TopNav de trabalho + barra simplificada de 3 itens do leitor) — "quando abre o livro era bom não ter mais essa barra: ficar uma barra só".
2. **Cura (8d3bd67, NO AR só no ousadia — aguarda QA do Miguel p/ promover):** TopNav removido da rota `book/[id]` nos 4 estados (leitura/carregando/travado/não-encontrado); a barra do leitor fica sozinha e já tem 🏠 (logo → home central) idioma ⚙️ (no ☰) e olhinho. Olhinho do leitor agora GRAVA a preferência (chave nova `moka.readerNavHidden2`) — escondeu, fecha e reabre limpo (teste 4 do PRONTO). Curas preservadas: BUG-20260801 (interação reexibe o menu — só não no mount/troca de livro), fontes 15/09 (o leitor nem usa .topnav), `moka.navHidden2` segue valendo nas demais páginas.
3. **Prova:** build limpo; SSR servido do ousadia: /book/xyz sem topnav (0), /estante com topnav (1); chave nova achada no chunk do livro; canônico www.mokareader.com INTOCADO até o OK dele.
4. **QA pendente do Miguel:** Ctrl+F5 no ousadia + os 6 testes de aceitação do PRONTO (contar barras, fonte 140%/85%, 2 toques p/ 🏠/idioma/⚙️/submenu, preferência do olhinho, sair p/ estante, estados de exceção).

✅ **Promoção aos 3 (18/09 ~13:1x, OK do Miguel "ficou ótimo"):** canônico moka.git main = 8d3bd67 (FF) → www.mokareader.com NO AR; espelho 1 = e1c3d06 (merge promo, histórico preservado) → moka-espelho.vercel.app NO AR; ousadia já estava em 8d3bd67. Provas de produção: /book sem topnav (0) e /estante com topnav (1) nos 3 domínios; chave moka.readerNavHidden2 presente no chunk do livro do canônico.

## 🔧 Adendo — round 15 (18/09/2026 ~20:1x): TopNav só onde precisa — páginas de conteúdo ganham a barrinha mínima

1. **Ordem (Miguel, 18/09 ~20:0x):** "assim como você tirou o top nav do menu de leitura, tira de outras páginas onde não precisa do top nav."
2. **Cura (49639f6, NO AR só no ousadia — aguarda QA p/ promover):** componente novo `InfoTopbar` (← Moka + bandeirinha, padrão da Privacidade) substitui o TopNav em: /sobre, /ajuda, /tutorial, /experimente, /auth/confirmado e /auth/atualizar-senha. Continuam com TopNav (as 6 seções + ferramentas): estante, video, video/[id] (tem ações próprias: ＋ novo vídeo e 📤 compartilhar), memoria, harness, writer, mural-das-ias, telemetria, configuracoes e biblioteca. Capa e privacidade já tinham o padrão mínimo.
3. **Provas:** build limpo; SSR no ousadia: as 6 páginas com topnav=0 e info-topbar presente; estante e configuracoes com topnav=1 (intactas).
4. **QA pendente do Miguel:** conferir se alguma página que ficou SEM o menu deveria ter (ou vice-versa) — a lista de cima é a minha leitura do "onde não precisa".

✅ **Promoção aos 3 (18/09 ~20:2x, ordem do Miguel "vai jogando tudo pro espelho e canônico logo"):** canônico moka.git = 49639f6 (FF) → www.mokareader.com NO AR; espelho 1 = 7010748 (merge promo) → moka-espelho.vercel.app NO AR; ousadia já estava. Provas de produção: /sobre topnav=0 com info-topbar e /estante topnav=1 nos 2 domínios. Round 15 completo e fechado.
