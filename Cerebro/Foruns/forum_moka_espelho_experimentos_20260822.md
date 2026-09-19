# Fórum — Espelho do Moka Reader (experimentos antes do canônico)

**Data:** 22/08/2026 (~20:30–21:05 BRT) · **Autor:** ZCode/Qwen 3.8 · **Origem:** ordem do Miguel ("vamos criar um site espelho, pra gente primeiro fazer as experiências lá, e só depois passar para o canônico")
**Tema Duplo:** memória técnica em `Memorias/memoria_moka_espelho_experimentos_20260822.md`

## Arquitetura final (NO AR)

| | Canônico | Espelho |
|---|---|---|
| Repo GitHub | `migueldorosario1/moka` | `migueldorosario1/moka-espelho` (NOVO, público) |
| Projeto Vercel | `moka` | `moka-espelho` (NOVO, `prj_Gt8y...`) |
| Branch de produção | `main` | `main` (recebe o conteúdo da branch local `espelho`) |
| URL | www.mokareader.com | **https://moka-espelho.vercel.app** |
| GA4 | ativo (G-43CSQVKW6N) | desativado por guard de domínio |

**Por que repo separado:** a API pública da Vercel não permite mudar a *production branch* de projeto (testado: PATCH em 4 versões, recriar link com campo extra, promote — tudo rejeitado/ignorado). Com repo próprio, `main` do espelho = produção do espelho, e o auto-deploy funciona de verdade (provado com commit de teste).

## Fluxo de trabalho (o combinado)

1. **Experiência nova:** eu trabalho na branch local `espelho` (no repo `moka-app`) e pusho com `git push mirror espelho:main` → o espelho deploya sozinho em ~1 min.
2. **Miguel testa** em https://moka-espelho.vercel.app.
3. **Aprovou:** merge `espelho → main` no repo moka (canônico deploya sozinho) + `git push mirror main:main` pra re-sincronizar a base do espelho.
4. **Não aprovou:** a espelho segue divergindo; nada toca o canônico.

## Decisões adicionais

- **Variáveis de ambiente:** as 10 do canônico espelhadas (produção+preview); `NEXT_PUBLIC_SITE_URL` aponta pra URL do espelho.
- **GA4 protegido:** guard de domínio (commit na espelho) — analytics só injeta em `mokareader.com`. Quando a espelho for aprovada e mergeada, o guard vai pro canônico também (melhoria pros dois: previews do canônico também param de poluir).
- **Domínio:** espelho fica no `*.vercel.app` (sem mexer em DNS); se quiser `espelho.mokareader.com` é só pedir.
- Remote local `mirror` aponta pro repo espelho.

## Estado atual

- ✅ Tudo no ar e provado: push → deploy de produção do espelho (commit 303fa9c, READY, alvo production, repo moka-espelho).
- ✅ Espelho 200 (capa + /telemetria), GA4 ausente; canônico 200 com GA4 intacto.
- ✅ Pasta de trabalho na `main`, link Vercel local = canônico.

## O que falta / próximos passos

- Miguel abrir https://moka-espelho.vercel.app e confirmar.
- Decisão futura (não urgente): desconectar `moka-lab` e `moka-v3` da main (cada push na main dispara 2 builds extras desperdiçados; projetos legado).
- Branch local `espelho` e a branch `espelho` no origin ficam como registro/histórico; o que deploya o espelho é o remote `mirror`.

## Preciso de você, Miguel

- Só confirmar que o espelho abre bem. A partir de agora: experiência → espelho primeiro.

---

# Adendo — incidente da tradução e rollback do canônico (22/08, ~20:45–21:05)

A telemetria que estava no canônico quebrou a tradução de livro (detalhes em `Foruns/forum_moka_telemetria_gastos_ia_20260822.md` §Adendo 3 e `CEREBRO_NODE_BUGS_ATIVOS.md`). Por ordem do Miguel, **tudo que foi feito hoje foi rollbacado do canônico** (reverts na main; produção = estado de 19/08) e **passou a viver exclusivamente no espelho**:

- ✅ Espelho agora contém: telemetria completa (rodadas 1+2) + página "Suas IAs" + guard GA4 + **fix da tradução** (`fcf29e7`: streaming sem `stream_options`).
- ✅ Deploy do espelho verificado: https://moka-espelho.vercel.app 200 (capa e /telemetria), produção alvo `fcf29e73`.
- 🔒 Nova regra do fluxo (valendo): **reforma no canônico, nunca — experiência entra pela espelho e só sobe por merge aprovado.**
- Trocador de modelo por IA (pedido do Miguel): já está na `/telemetria` do espelho — cada card de IA tem botão 🧩 com o modelo atual; 1 clique abre a lista (auto-busca) e 1 clique no modelo salva.


# Adendo 2 — crash client-side do espelho e correção (22/08, ~21:05–21:30)

O Miguel reportou: espelho não abria ("Application error: a client-side exception"). Diagnóstico isolando rotas no navegador: `/privacidade` ok, `/`, `/sobre`, `/telemetria` quebravam → componente das páginas quebradas era o AuthGate (login). Reproduzido localmente com as env vars do espelho: **"Invalid supabaseUrl: Must be a valid HTTP or HTTPS URL"**.

**Causa raiz:** o espelhamento das 10 env vars canônico→espelho copiou os blobs CIFRADOS da API da Vercel (a API não devolve plaintext de vars `sensitive` nem com `decrypt=true`). A `NEXT_PUBLIC_SUPABASE_URL` virou lixo → `createBrowserClient` lançava exceção no boot de toda página com AuthGate.

**Correção executada:**
- As 3 `NEXT_PUBLIC` recriadas com valores reais (Supabase é chave pública por design — extraída do bundle do canônico; SITE_URL = URL do espelho).
- As 6 servidoras (SMTP×4, TRANSKRIPTOR, MOKA_MOTOR_KEY) recriadas a partir dos cofres locais.
- `GITHUB_TOKEN_MOKA`: sem fonte legível → removida do espelho (função que a usa é opcional/try-catch).
- Rebuild via commit vazio (`0615e5f`) → deploy READY → **capa, /sobre e /telemetria verificadas abrindo normalmente**.

**Regra nova (gotcha permanente):** espelhar env vars pela API da Vercel exige conferir o valor, não só o nome — `sensitive` nunca sai em plaintext; usar cofre local ou bundle público como fonte. Detalhes técnicos na memória.


# Adendo 3 — contenção total do espelho + caixa 📖 default (22/08, ~21:40–22:40)

**Reporte do Miguel:** "entrei no espelho, cliquei em configurações e voltei para o canônico. Não pode. O espelho tem que ser total, em todas as páginas."

**Diagnóstico (navegador, rota por rota):** as 9 rotas do espelho (`/`, `/estante`, `/configuracoes`, `/video`, `/sobre`, `/ajuda`, `/tutorial`, `/experimente`, `/biblioteca`, `/telemetria`) carregadas direto **ficam todas no espelho** — não há redirect server-side. O callback de auth do espelho também redireciona corretamente para o espelho (`NEXT_PUBLIC_SITE_URL` certo, provado com `curl /api/auth/callback`). Sobraram exatamente **2 caminhos** que levam ao canônico:

1. **Link absoluto no rodapé do `/video`**: "irmão do Moka Reader" → `https://www.mokareader.com` (target _blank). Único link clicável do código que aponta pro canônico.
2. **Login (Supabase OAuth):** espelho e canônico compartilham o MESMO projeto Supabase (`nsasbuqeeqdwsagpfpcc`). Ao logar no espelho, o Supabase valida o `redirect_to` contra a allowlist do projeto; se a URL do espelho não estiver cadastrada, **cai no Site URL do projeto = produção (mokareader.com)**. É o único mecanismo restante que "devolve" o usuário ao canônico.

**Correções no código (commit `75e43ff`, branch espelho, deploy READY verificado):**
- `/video`: link "Moka Reader" agora é relativo (`<Link href="/">`) — o espelho nunca vaza pro canônico por link.
- **Badge 🧪 ESPELHO** fixo no canto inferior de TODAS as páginas (layout global), renderizado SÓ quando `NEXT_PUBLIC_SITE_URL` contém "espelho" — no canônico nunca aparece. Acaba a ambiguidade "em qual dos dois sites eu estou?".
- `config.ts` (pedido anterior do Miguel): **nova chave já vem com a caixa 📖 Tradução/Explicação MARCADA** como default (`useForText=true`, se não houver outra entry de texto — a marca é single-select, nova key não "rouba" o lugar). Bônus: editar uma key existente agora PRESERVA as marcas useFor* (antes zerava).

**Verificado ao vivo:** badge aparece em `/`, `/configuracoes`, `/video`; "Moka Reader" do `/video` agora aponta `/` e fica no espelho; lógica do default provada deterministicamente (3 casos). Build limpo.

## O que falta / preciso de você, Miguel

🔴 **Login no espelho (ação sua, ~1 min):** Supabase Dashboard → projeto do Moka → **Authentication → URL Configuration → Redirect URLs** → adicionar `https://moka-espelho.vercel.app/**`. Sem isso, quem tentar entrar com Google/e-mail no espelho cai no canônico (o Site URL de produção). Não há credencial Supabase de gestão em nenhum cofre — essa config é só sua (já constava como pendência sua desde 06/08). Depois de adicionar, testar "Entrar" no espelho: deve voltar ao espelho logado.

---

## Adendo 4 — recado de tradução: maior + nos 12 idiomas (22/08, ~22:50)

**Ordem do Miguel:** adorou o recado "🌐 Traduzindo a página inteira… Tenha paciência" ("está ótimo, parabéns") e pediu: (1) "bota maior, um pouquinho maior só"; (2) perguntou se, com a interface em inglês/francês/etc., o recado aparece no idioma certo.

**Feito (commit `3e0057b` no espelho, deploy READY, verificado nos bundles de produção):**
- **Tamanho:** título 18→20px (no PDF 17→20), subtítulo 13,5→14,5px, caixinha da dica 13→13,5px — caminhos EPUB e PDF.
- **Idiomas:** o recado principal JÁ tinha chave nos 12 idiomas (`reader_translating_page`/`_sub`). Havia 2 furos, corrigidos: (a) a dica "tenha paciência + Mural das IAs" só existia em pt/en/es/fr — os outros 8 idiomas caíam em português; virou i18n de verdade (chaves novas `reader_patience_pre/_wall/_post` nos 12 blocos); (b) no caminho PDF o recado estava hardcoded em português (`PdfPageCanvas`) — agora usa `t()`.

**Resposta ao Miguel:** SIM — o recado inteiro agora aparece nos 12 idiomas da interface (🇧🇷 pt · 🇺🇸 en · 🇪🇸 es · 🇫🇷 fr · 🇩🇪 de · 🇮🇹 it · 🇷🇺 ru · 🇨🇳 zh · 🇯🇵 ja · 🇰🇷 ko · 🇸🇦 ar · 🇮🇳 hi), sempre no idioma da bandeirinha escolhida.

---

## Adendo 5 — LOGIN NO ESPELHO LIBERADO: allowlist do Supabase atualizada pelo Miguel (23/08, ~14:05)

**Contexto:** último vazamento espelho→canônico (bug `BUG-20260822-MOKA-ESPELHO-SUPABASE-ALLOWLIST`). Login Google/e-mail no espelho caía no canônico porque o domínio não estava na allowlist do projeto Supabase compartilhado (validação no `/callback` pós-Google, fallback Site URL = produção).

**Como foi (ação conjunta, ao vivo):** ZCode abriu o Dashboard no navegador do ZCode; login GitHub do Miguel completou no Chrome dele; passo a passo passado no chat (Add URL → colar → Save). Miguel adicionou `https://moka-espelho.vercel.app/api/auth/callback` — **caminho completo, no MESMO padrão das outras 5** (mais restrito que o wildcard sugerido antes; é exatamente o redirect que o app usa). Lista agora: mokareader.com, moka-phi, video.mokareader.com, moka-video, localhost:3100 e **moka-espelho** (Total URLs: 6). Site URL permanece `https://mokareader.com`.

**Estado:** ✅ allowlist corrigida · 🔄 falta o TESTE do Miguel: Entrar no espelho → deve voltar ao espelho logado. Com isso, o espelho fica TOTAL em todas as páginas, incluindo login — objetivo do pedido original.

**Achados úteis:** projeto Supabase interno chama-se **"Igotit"** (plano Free, org migueldorosario1); botão "Add URL" fica NO TOPO da lista (faixa do link "Docs"), pequeno e fácil de não ver.

---

## Adendo 6 — CAPA DO LIVRO NA ESTANTE do espelho (23/08, ~16:15)

**Ordem do Miguel:** "no espelho, você esquece de montar aquele esquema que a capa do livro aparece na estante. isso é importante".

**Causa raiz (provada):** a capa NUNCA ia para a nuvem — os upserts (`saveBook`/`saveToLibrary`) não gravavam capa nenhuma, e a leitura esperava a coluna `cover_image`, que **não existe** no banco (PostgREST: `42703 — column books.cover_image does not exist`). No canônico ninguém notava porque a estante prefere a cópia local (IndexedDB do domínio, que tem a capa gerada no upload). No espelho — domínio novo, IndexedDB vazio — os livros vinham só da nuvem, sem capa (só a capa azul genérica).

**Correção (commit `8b5a7bb`, deploy READY, lógica confirmada no bundle):** capa passa a viajar EMBUTIDA no jsonb `book` (ParsedBook já tem `coverImage`) nos dois upserts; leitura usa `row.cover_image ?? book.coverImage`; no merge, capa local manda e a da nuvem completa se faltar. **Zero mudança de schema** (nada de risco no banco de produção).

**O que o Miguel vê ao recarregar a estante do espelho (Ctrl+F5):** EPUBs com capa embutida → capa real volta JÁ (estava escondida dentro do livro na nuvem). PDFs → capa real volta ao ABRIR o livro (o PDF inteiro fica só no aparelho onde foi enviado, por projeto; ao abrir, o save sobe a capa). Livros sem capa no arquivo → capa elegante azul gerada na hora (igual canônico). Efeito bônus: o canônico também passa a ter capas na nuvem a partir dos próximos saves.

---

## Adendo 7 — CAPA INTELIGENTE: app examina as 10 primeiras páginas e elege a melhor (23/08, ~17:00)

**Ordem do Miguel:** mandou o PDF `2015.166245.Roman-Political-Institutions-From-City-To-State.pdf` ("aqui, a capa é a página 9") e perguntou se o app pode "examinar sempre as 10 páginas e identificar qual é a melhor candidata a capa". Resposta: SIM — feito e calibrado.

**Como foi calibrado (com 6 PDFs reais da pasta dele):** sondas de texto (itens/fonte/cobertura) + pixels (miniaturas 150px: tinta/saturação/cores) + blobs conexos, rodando no navegador do ZCode com o MESMO pdf.js do app. As páginas 2/8/9 do Roman foram VISTAS por IA de visão — p9 = folha de rosto (título grande centrado, Léon Homo, Knopf 1929); p2 = chapa de procedência da U. Washington; p8 = miolo denso.

**A eleição (commit `bf3f54d`, deploy READY):** `pdf-cover.ts` reescrito — mede as 10 primeiras páginas e elege em 3 níveis: **A)** capa de arte (≥50% tinta, sat>0.10, ≥40 cores — 5 dos 6 livros, capa na p1); **B)** PDF digital: página de maior fonte com corpo (folha de rosto); **C)** scan P&B: letras grandes (blob de 4–25% da altura) SEM ilustração dominante (>25%) nem miolo (>20% tinta) → **elege a p9 do Roman**. Re-envio de PDF recalcula a capa (estante). Best-effort: qualquer erro → página 1, upload nunca quebra.

**Teste do Miguel:** re-enviar o Roman no espelho → capa da estante vira a página 9. (Essa melhoria vive no espelho; sobe pro canônico só no merge aprovado.)

---

## Adendo 8 — botão 🌐 Traduzir página "mudo" no espelho: caixa de confirmação NÃO foi removida; era PDF sem texto (23/08, ~20:30)

**Reporte do Miguel:** no canônico, "Traduzir a página inteira" mostra a caixa "tem certeza?" antes de traduzir; no espelho, "não tem a caixa" e depois "nem está funcionando — não diz nada, nem traduz nada". A caixa é importante "para evitar erros e gastos desnecessários de IA".

**Diagnóstico:** a caixa (`confirm(t("reader_confirm_translate_page"))`) existe e é idêntica nos dois códigos. O que acontecia: o botão ficava `disabled={translatingPage || !currentPageText}` — sem texto na página (caso do Roman: **scan puro, ZERO itens de texto** — medido na calibração da capa; ou PDF ainda carregando), o clique não disparava NADA: sem caixa, sem erro, sem tradução. Parecia bug, era silêncio.

**Correção (commit `0bc38c0`, deploy READY):** botão só desabilita durante a tradução; clicado sem texto, AVISA (chave nova `reader_scan_no_text` nos 12 idiomas: "Não há texto nesta página para a IA traduzir. Pode ser um livro escaneado (só imagens) ou a página ainda está carregando…") e NÃO chama a IA. Com texto, o fluxo do canônico segue intacto: caixa de confirmação → só traduz após OK.

**Fato importante pro Miguel:** o Roman (escaneado) não tem tradução de página nem no canônico — não existe texto para a IA traduzir; precisaria de OCR (ideia futura). A caixa aparece normalmente em EPUBs e PDFs com texto.

**Verificação completa (23/08 ~20:30, resposta ao "tem certeza?"):** o Roman é 100% imagem do começo ao fim — medi páginas 11/15/20/50/100/200/436 via pdfjs: **0 caracteres de texto em todas** (as 10 primeiras já eram conhecidas: 0 itens). Nenhuma camada de OCR embutida. E o app não tem OCR (grep "ocr|tesseract" só deu falso positivo: "docRef" e "democratizar" contêm as letras o-c-r). Ou seja: Moka (canônico E espelho) traduz PDFs que TÊM texto — inclusive a maioria dos escaneados, que vêm com OCR invisível de fábrica (dokumen.pub, Internet Archive etc.) — mas PDF 100% imagem como o Roman não tem o que traduzir, em nenhum dos dois sites. **Feature futura proposta:** OCR no navegador (tesseract.js, grátis/offline) + tradução em cima do texto lido.

---

## Adendo 10 — TRADUÇÃO DE PÁGINA-IMAGEM POR IA DE VISÃO + transparência total de custo (23/08, ~22:10)

**Ordem do Miguel (literal):** "informa que é uma imagem, que vai custar um pouco mais, e (e aí vamos experimentar no espelho), informa quando deve custar e depois de fazer, diz quanto custou e deixa tudo anotado na página de telemetria." — opção 1 (IA de visão) aprovada.

**Implementado (commit `41387bc`, deploy READY):**
- **Adapter multimodal:** `CompleteOptions.images` (data URLs) → mensagem `[texto + image_url]` no formato OpenAI-compatible (GPT-4o/Gemini/Qwen-VL/GLM-4V...).
- **`translatePageImageStream`:** lê a página-imagem (OCR pela própria visão) e traduz com streaming; tarefa nova **`translate-page-image`** no ledger (rótulo "Tradução de página (imagem)" nos 12 idiomas); trava de tokens respeitada.
- **Antes (estimativa):** `estimateImagePageCostUsd()` = ~1300 tokens de imagem + ~1800 de saída × preço da tabela → o confirm avisa: "Esta página é uma IMAGEM… custa um pouco mais… estimativa de US$ X por página. Continuar?" — **IA só é chamada após OK**.
- **Depois (custo real):** usage real do provedor (ou estimativa) → nota anexada à tradução: "💰 Custo real desta tradução por visão: US$ Y — anotado na sua página de telemetria" (auto-save/notas salvam a tradução limpa, sem a nota).
- **Telemetria:** tudo no ledger de /telemetria, agrupado por tarefa/provedor/modelo, CSV inclusive.

**Limites conscientes:** exige que a CHAVE ativa seja de modelo com visão (se o provedor rejeitar imagem, aparece erro claro); o custo real usa a tabela de preços — modelo fora da tabela → "estimativa indisponível" e custo 0 no ledger. **Teste do Miguel:** Roman no espelho → 🌐 → confirm com estimativa → tradução + nota de custo → /telemetria com a linha "Tradução de página (imagem)".

---

## Adendo 11 — aviso no UPLOAD de PDF 100% imagem (24/08, ~08:15)

**Ordem do Miguel:** "avisar antes de baixar o livro, que PDF em forma de imagem precisam ser baixados com alguns tipos de LLM — um botão de confirmação explicando isso, em todos os idiomas".

**Feito (commit `6840cd4`, deploy verificado no ar):** `isImagePdf()` no pdf-cover (0 itens de texto nas 10 primeiras páginas ⇒ scan puro — mesmo critério da capa inteligente); no upload da estante, ANTES de adicionar: confirm explicando nos 12 idiomas que o livro lê/folheia normal, mas traduzir/explicar páginas exige IA que ENXERGA (GPT-4o/Gemini/Qwen-VL/GLM-4V…) e custa um pouco mais por página; Cancelar = não adiciona. Best-effort: falha de detecção nunca bloqueia upload.

**Bônus do reenvio:** ao reenviar um PDF antigo (como o Roman), o usuário ganha os TRÊS de uma vez: este aviso + a capa inteligente (p9 do Roman) + a tradução por visão.

---

## 🚀 FILA DO MERGE (espelho → canônico) — ATUALIZADA 26/08 ~09:50

**Paridade garantida (Adendo 9):** espelho ⊇ canônico (provado: `git log espelho..main` = apenas os 2 reverts da telemetria, cujo efeito o espelho já contém consertado). Resultado do merge DEVE ser a árvore do espelho.

**O que sobe (28 commits, `2facdf1`…`f61fade`):**
1. `2facdf1`/`303fa9c` — base do espelho (teste de conexão, auto-deploy)
2. `1032b21` — GA4 com guard de domínio (analytics só no canônico)
3. `fcf29e7` — fix da tradução (stream_options fora do streaming) + telemetria via estimativa quando provedor não informa
4. `0615e5f` — env vars do espelho com valores reais (rebuild)
5. `75e43ff` — contenção total (link relativo) + badge 🧪 ESPELHO (env-gated, invisível no canônico) + caixa 📖 default + preservar marcas ao editar chave
6. `3e0057b` — recado de tradução maior + dica de paciência nos 12 idiomas (PDF sem PT hardcoded)
7. `8b5a7bb` — capa do livro viaja na nuvem (embutida no jsonb book) — estante completa em qualquer domínio/aparelho
8. `bf3f54d` — capa inteligente (elege a melhor página entre as 10 primeiras; Roman→p9; reenvio recalcula)
9. `0bc38c0` — botão 🌐 com voz: página sem texto avisa nos 12 idiomas e não gasta IA
10. `41387bc` — tradução de página-IMAGEM por IA de visão (estimativa antes, custo real depois, tudo na telemetria)
11. `6840cd4` — aviso no upload de PDF 100% imagem (12 idiomas, confirm)
12. `11478fc` — tradução de livro PAUSA sozinha em segundo plano (nunca mais gasta às cenas)
13. `92b24f4` — toda ação do livro no ledger (nota vol X/Y · pág Z na telemetria)
14. `a584b12`+`91782b6`+`93771d9`+`5eae68c`+`d5227f2`+`c118db5`+`3d8d6fc` — Google Drive: construído, e **REMOVIDO por decisão do Miguel** (o que fica do merge é o estado LIMPO, sem Drive; conhecimento arquivado no Cérebro p/ eventual retorno por Picker verificado)
15. `41387bc`+`8b5a7bb` — (incluídos acima)
16. `8b5a7bb` — (capa na nuvem, acima)
17. `bf3f54d` — (capa inteligente, acima)
18. `0bc38c0` — (botão com voz, acima)
19. `c55f7aa` — clicar em USAR uma LLM acende a caixinha 📖 nela (single-select)
20. `b1b4108` — recado de espera turbinado (LLM+modelo, "alguns minutos", barra de progresso %) + custo só no pop-up
21. `e16f82c`+`0177222` — header: nav quebra linha na classe certa + ⛶/👁 na chave de zoom + hub 📊 (2 submenus) + cura do menu ampliada (Anotações) + 👁 destravador universal
22. `6508f40` — erro de chave → CONFIGURAÇÕES primeiro (botão ⚙️ no erro; links de causa → /configuracoes)
23. `006aaa2` — 🏆 Mural das IAs página própria + botões nas Suas IAs/configurações + ícone 🏆 na capa + TeleCharts (2 gráficos custo/tokens com filtro por LLM)
24. `650cc33`+`6b7a98f` — telemetria: 3 linhas de gasto (início/7d/30d ×12) + 🧮 calculadora migrada pro Mural
25. `b6477d0`+`3d8d6fc` — Drive REMOVIDO por completo + faxina total (zero sujeira)
26. `1f0d5d7` — cura do menu ao voltar da página do livro (fullscreen órfão; verdade do DOM)
27. `297315e` — pacote UX: ícones na chave de zoom + hub 📊 + nota 💰 (agora só pop-up) + travão do 🌍 com estimativa
28. `f61fade` — 🌍 Biblioteca 100% internacional (kicker ×12 + sinopses {pt,en} ×8 + CTA ×12) + título das causas + PDF carregando ×12

**Passo a passo do merge (quando o Miguel aprovar):**
```
cd ~/ZCodeProject/moka-app
git checkout main && git pull origin main
git merge -X theirs espelho        # conflitos → lado espelho (paridade)
cd apps/web && npm run build       # verde antes de subir
git push origin main               # canônico deploya (Vercel)
git push mirror main:main          # re-sync da base do mirror
```
**Pós-merge:** checar deploy canônico READY + 5 rotas 200 + login + caixa de confirmação + capa + /telemetria + GA4 só no canônico. Badge 🧪 NÃO pode aparecer no canônico (env-gated). **Nada de env var a fazer** (cada projeto Vercel tem as suas). Env órfã `NEXT_PUBLIC_GDRIVE` no espelho: inofensiva (limpar quando der).

**Pré-teste do Miguel (valida 8/10 itens de uma vez):** reenviar o Roman no espelho → aviso de PDF-imagem + capa p9 + tradução por visão com custos. 

---

## Adendo 12 — 📂 subir livro direto do GOOGLE DRIVE, sem baixar pro PC (24/08, ~22:35)

**Ordem do Miguel:** "O Moka espelho poderia ler um livro no meu Google Drive, subindo para a estante? Pode subir para a estante mesmo sem precisar baixar. Aí ficaria a opção de baixar ou ler direto no Gdrive." → "faz o drive".

**Feito (commit `a584b12`, verificado NO AR na /estante):** botão **"📂 Do Google Drive"** na estante → modal lista seus PDFs/EPUBs do Drive (mais recentes, com MB e data, busca por nome) → clique → os bytes vêm do Google DIRETO pro navegador (nada no disco) → mesma pipeline de sempre (dedup → parse → aviso de PDF-imagem → capa inteligente → estante). Sem OAuth client próprio do Google: usa o **mesmo login Google do Moka** — o token do Google fica na sessão Supabase (`provider_token`), com escopo `drive.readonly` (ver abaixo). Sem token/expirado (~1h) ou acesso recusado → tela "Reconectar com o Google" (re-login renova). 8 chaves novas × 12 idiomas; modal com CSS próprio; best-effort total (erro nunca quebra a estante). `handleFile` foi refatorado em `ingestBook(data, fileName, fileSize)` — arquivo local e Drive compartilham a mesma pipeline.

**🔴 PASSO DO MIGUEL (~1 min, Supabase Dashboard — mesma área do allowlist):** Authentication → Sign In / Providers → **Google** → campo **Authorized scopes** (ou "Escopos autorizados") → adicionar `https://www.googleapis.com/auth/drive.readonly` → Save. Depois: **sair e entrar de novo no espelho** — o Google mostra a tela de consentimento do Drive ("ver seus arquivos do Drive") → aceitar. Aí o 📂 lista e sobe os livros. (Sem esse passo, o botão funciona mas o Google recusa com a mensagem de reconexão/escopo.)

**🔴 Correção DEFINITIVA do 403 (24/08 ~22:57, commit `93771d9`):** a tela de diagnóstico provou o 403 `insufficient authentication scopes` (login feito sem o escopo do Drive). Descoberta que simplifica tudo: o supabase-js aceita **`scopes` direto nas options do signInWithOAuth** — o `reconnectGoogle` agora pede `drive.readonly` + `access_type=offline` NO PRÓPRIO FLUXO OAUTH: o Google mostra o consentimento "ver seus arquivos do Drive", o usuário ACEITA e o token da sessão passa a valer pro Drive — **sem depender de campo nenhum no painel Supabase** (a instrução anterior de Authorized scopes ficou obsoleta). Tela 🔒 agora tem o botão Reconectar + instrução de aceitar o consentimento (12 idiomas). Teste: Ctrl+F5 → 📂 → 🔒 → Reconectar → aceitar no Google → 📂 de novo → lista.

**➡️ DECISÃO DE PRODUTO FINAL (24/08 ~23:15, ordem/pergunta do Miguel "não podemos dar nenhuma experiência negativa ao usuário... basta desistir?"):** confirmado que TODOS os usuários bateriam na mesma parede do Google (app em Testing + escopo restrito = só testadores). Resposta do ZCode aceita pelo desenho: **NÃO desistir — virar BETA PRIVADO do dono** (commits `d5227f2`+`c118db5`): botão 📂 só renderiza com `NEXT_PUBLIC_GDRIVE=1` (criada SÓ no projeto espelho; canônico sem a env = botão invisível = merge 100% seguro, zero experiência negativa).

**➡️ VIA OFICIAL IMPLEMENTADA (24/08 ~23:25, commit `5eae68c`, ordem "ok, pode fazer então"):** `gdrive-picker.ts` — Google Picker (janelinha oficial do Google) + escopo LEVE `drive.file` via Google Identity Services: o app só enxerga o livro ESCOLHIDO (não lista o Drive), token direto no navegador (fim da dependência do provider_token do Supabase). Ativa com `NEXT_PUBLIC_GOOGLE_CLIENT_ID` (ainda SEM valor — pendente); sem a env usa o fluxo legado. **Passos pendentes do Miguel:** (1) colar o Client ID (Supabase → Providers → Google — valor público) pro ZCode setar na env do espelho; (2) console Google → Biblioteca → **API do Google Drive → Ativar**; (3) Credenciais → OAuth Client → **Origens JavaScript autorizadas** → `https://moka-espelho.vercel.app`; (4) Tela de permissão → **Usuários de teste** → migueldorosario@gmail.com (enquanto "em testes"). Teste: 📂 → janelinha do Google → escolher livro → estante.

---

## Adendo 13 — erro de chave → CONFIGURAÇÕES primeiro, ajuda depois (24/08, ~23:40)

**Ordem do Miguel:** "deu um erro na chave e entrou o recado, com link de possíveis causas, mas aí entra na ajuda, ao invés de entrar primeiro direto nas configurações para eu botar minha chave."

**Feito (commit `6508f40`, deploy READY, botão provado no bundle):** quando o erro é de CHAVE/autenticação (`isKeyOrConfigError()`: 401/403, chave inválida, nada configurado), o bloco de erro abre com botão grande **"⚙️ Abrir configurações e corrigir minha chave"** como PRIMEIRO caminho (usa o `onOpenSettings` do Reader, que navega pra /configuracoes; fallback link). Os links de causa de chave/modelo/sem-config agora apontam pra `/configuracoes`; `/ajuda` fica só para crédito/limite, rede e genérico. Regra de UX consolidada: **erro se resolve na tela que corrige o problema.**

---

## Adendo 14 — 🏆 Mural página própria + 📈 DOIS gráficos na telemetria (24/08, ~23:55)

**Ordens do Miguel:** (1) "bota o mural das IAs numa página separada... botão Mural das IAs nas Suas IAs e nas configurações... ícone na primeira página. Não vamos misturar a página de telemetria com mural das IAs"; (2) "na página de telemetria... terminar com um gráfico dos gastos — ou melhor dois, um de custos, outro de tokens — com botões para marcar: gráfico de todas as LLMs ou apenas de algumas".

**Feito (commit `006aaa2`, deploy READY, provas: /mural-das-ias 200 + TeleCharts no chunk app/telemetria):**

- **Mural separado:** página nova `/mural-das-ias` (LlmPriceRanking com casa própria, topbar padrão); botão "🏆 Mural das IAs" nas Suas IAs (/telemetria) e nas Configurações; ícone **🏆 na primeira página** (MuralIconButton ao lado do 📊); /ajuda: seção vira link; recado de paciência do leitor aponta pra `/mural-das-ias`. Telemetria não renderiza mais o ranking (fim da mistura).
- **Gráficos (TeleCharts, fim da /telemetria):** DOIS gráficos de barras empilhadas por dia (14 dias) — **custo US$** e **tokens** — somando TODAS as tarefas/idiomas cadastrados; **legenda clicável por LLM** (bolinha colorida + gasto total: liga/desliga cada uma) + botão "Todas". SVG puro (sem lib — bundle leve). 7 strings × 12 idiomas em telemetry-strings + `mural_link` × 12 na ui-strings.
- **Gotcha:** chunks de página do App Router moram em `/chunks/app/<rota>/page-<hash>.js` — regex de chunk `chunks/[0-9]*-[a-z0-9]*` NÃO os pega (falso "não está no ar"); usar `--compressed` + padrão amplo.

---

## Adendo 15 — nav quebra linha (ícone atrás da bandeira) + ⚙️ em TODO erro de IA + tradução a diagnosticar (25/08, ~00:55)

**Reportes do Miguel:** (1) ícone ao lado do 🌍 escondido ATRÁS da bandeira; (2) "Moka não está funcionando: chave funciona nas configurações mas NÃO traduz página inteira NEM trecho"; (3) "o aviso entra mas não dá link pra configurações".

**Feitos (commit `e16f82c`, verificado NO AR):**
- `.reader-nav { flex-wrap: wrap }` — em tela estreita os ícones caem pra segunda linha em vez de ficarem sob a bandeira do idioma.
- Botão do bloco de erro agora aparece pra **QUALQUER falha de IA** ("⚙️ Abrir configurações e trocar de IA") — antes só para erro classificado como chave; trocar chave/modelo/provedor resolve chave, modelo, crédito e rate na maioria dos casos.

**Tradução (investigação aberta):** revisados os diffs suspeitos da cadeia (commit 92b24f4 da outra sessão = só nota no ledger, inofensivo; adapter multimodal sem imagens = string idêntica ao antes; runStreamWithCap/handler intactos) — nada quebra o fluxo no código. **Hipótese principal: 402/429 do provedor** — o teste de conexão gasta ~1 token (passa mesmo no fim do crédito) e a página inteira gasta milhares (falha). Pendente: o Miguel colar o TEXTO do aviso (⚠️ + frase) ou print da próxima ocorrência → causa exata na hora; enquanto isso o ⚙️ novo destrava trocando de IA.

---

## Adendo 16 — caixinha 📖 ligada por default: autorreparação pra chaves ANTIGAS (25/08, ~00:59)

**Ordem do Miguel:** "deixa a caixa de tradução/explicação ligada por default". O default pra chave NOVA já existia (75e43ff, 22/08) — mas o caso dele era chave CADASTRADA ANTES do fix, que ficava desmarcada pra sempre. **Feito (commit `ab4f8cc`, deploy READY):** na carga do cofre, se NENHUMA chave tem a marca de texto, a ATIVA (ou a 1ª) ganha a caixinha 📖 marcada sozinha — uma única vez, sem tocar em escolhas já feitas; vale pros dois formatos do cofre (v2 e migração v1). Teste do Miguel: Ctrl+F5 → configurações → caixinha da chave ativa ✓.

**✅ REGRA DE LANÇAMENTO da integração (ordem do Miguel, 24/08 ~23:25 — confirmada por ele):** "primeiro temos que oferecer a integração [oficializá-la com o Google], e depois, SÓ DEPOIS DE CONFIRMADA, oferecer a possibilidade do internauta integrar a sua estante." Checklist prático: (1) refazer via Google Picker + escopo `drive.file` (verificação GRATUITA do Google — a rota `drive.readonly` restrita exige avaliação cara e está descartada); (2) publicar o app no console Google; (3) testar com o Miguel no espelho; (4) SÓ ENTÃO criar `NEXT_PUBLIC_GDRIVE=1` no projeto canônico (o botão nasce pro público). Até lá: público nunca vê o 📂.

O Miguel usa no espelho após os 2 passos de testador no Google Cloud Console (projeto do client do Moka): (1) APIs e Serviços → Biblioteca → **API do Google Drive → Ativar**; (2) APIs e Serviços → **Tela de permissão OAuth → Usuários de teste → + Adicionar** `migueldorosario@gmail.com`; (3) espelho → 📂 → Reconectar → Aceitar. Nota: em Testing o Google expira a autorização em ~7 dias (re-login semanal, aceitável no beta privado).

**Decisão consciente:** NÃO implementei "ler direto do Drive sem estante" (streaming por página) — lento, quebra offline, e a estante perde a função de biblioteca; o upload transparente resolve o pedido real (não baixar pro PC). Detalhe: tokens de outra sessão no meio (92b24f4/11478fc, telemetria de ações + pausa de tradução) — paridade conferida, sem conflito.

---

## Adendo 9 — REGRA: o espelho é IGUAL ao canônico EM TUDO (ordem do Miguel, 23/08 ~20:20)

**A regra:** o espelho contém SEMPRE 100% do canônico — nunca pode faltar nada nem regredir comportamento. O espelho = canônico + melhorias testáveis, nunca canônico menos algo.

**Prova (git, 23/08 20:15):** o ramo do espelho contém todo o estado de produção do canônico (19/08). Os únicos 2 commits da main ausentes são os REVERTS da telemetria (96f0713/335e18c) — e o estado que eles produzem (site sem a telemetria quebrada) já está no espelho por construção: lá a telemetria foi CONSERTADA (fcf29e7 + guard GA4 1032b21) em vez de revertida. Comportamentalmente: **nada do canônico falta no espelho**.

**O espelho tem A MAIS (aguardando OK do Miguel p/ merge):** telemetria consertada + "Suas IAs" + guard de analytics · fix da tradução (stream_options) · contenção total (link relativo + badge) · caixa 📖 default · recado de tradução maior e nos 12 idiomas · capa viajando na nuvem · capa inteligente (eleição da melhor página) · botão 🌐 com voz (aviso em vez de silêncio).

**Verificação da paridade (ritual a cada mudança):** `git log --oneline espelho..main` — se aparecer commit que NÃO seja revert já refletido, paridade quebrou.

---

## Adendo 17 — "uso das LLMs dá erro": provas E2E e hipóteses refinadas (25/08, ~01:00)

**Feito pra diagnosticar:** (1) testei o CAMINHO do app com uma chave REAL válida do cofre (DeepSeek payg, saldo ok): **200 no modo não-stream (o do teste de conexão) E no streaming SEM stream_options (o da tradução)** — provedor+formato sãos; (2) SW auditado: blindado desde 03/08 (HTML network-first, API nunca cacheada) — não é cache do PWA; (3) diffs da cadeia revisados (nada quebra); (4) E2E no IAB bloqueado (cliques instáveis — gotcha conhecido).

**Hipóteses restantes, em ordem:** (a) **chave EM USO (ativa/marcada 📖) ≠ chave testada no form** — testa a boa, o app usa outra (velha/morta) → 401 constante; (b) crédito/limite (402/429) só nas chamadas grandes; (c) navegador/cache pontual. **Plano com o Miguel:** Ctrl+F5×2 (deploy do ⚙️-em-todo-erro saiu 00:54; testes dele foram antes) → conferir chave ATIVA nas configurações (marcar 📖 na boa) → se persistir, COLAR o texto ⚠️ do bloco (agora sempre com ⚙️ "trocar de IA"). Bônus descoberto: DeepSeek já tem modelo de VISÃO (`deepseek-v4-flash-vision-exp`) — futuro candidato pra tradução de página-imagem.

**📲 Pendência (ordem do Miguel 25/08 ~01:05):** depois que o erro das LLMs for CORRIGIDO/fechado, enviar mensagem ao Telegram dele via ponte_cafezinho (`--send`) com o resultado.

---

## Adendo 18 — 🎯 CAUSA RAIZ do "não traduz nada": streamFn solto perdia o `this` (25/08, ~09:30)

**Fechamento da investigação do Adendo 17:** teste de chave passava, toda tradução falhava ("talvez sem crédito" era a causa SUGERIDA pelo bloco de erro — o erro real: "Cannot read properties of undefined (reading 'stream')", 2 LLMs com crédito falhavam igual). Metodologia: curl ponta-a-ponta (provedor ok em 3 modos) → /api/proxy-stream ao vivo (200 SSE) → **E2E Chrome+Playwright com chave DeepSeek real do cofre + livro da Biblioteca Livre** (reproduziu o erro na tela; capturado com patch de debug no dev local, revertido) → stack: `openaiCompatible.stream` com `this.transport` undefined.

**Causa raiz:** telemetria de 22/08 (`fc63cb7`) passava `streamFn: provider.stream` (generator method por referência) → perde `this` → explode antes da rede. Só no espelho (canônico rollbacou a telemetria — por isso lá traduzia). **Cura (commit `c463406`, deploy READY):** `.bind(provider)` nos 7 pontos + CSS da nav na classe certa (`.reader-row-scroll` wrap — o de 24/08 fora em seletor morto `.reader-nav`; ícone-atrás-da-bandeira resolvido de verdade). **Prova:** E2E dev local E produção espelho — 🌐 → confirm → tradução de Dom Casmurro fluindo em português, proxy-stream 200. **Telegram enviado ao Miguel (pendência cumprida).** Ficha completa: BUG-20260825-MOKA-TRADUCAO-STREAMFN-THIS em BUGS_RESOLVIDOS.

**Nota:** a dica de boas-vindas (tip-overlay 3 passos, 1× por livro) cobre a tela na primeira abertura — clique fora do balão fecha; nos testes E2E precisou dispensar antes do 🌐 (não é bug).

---

## Adendo 19 — pacote UX do leitor: ícones na chave de zoom + hub 📊 + nota 💰 universal + travão do 🌍 (25/08, ~10:12)

**Ordens do Miguel (turno das ~10h):** confirmar que 🌐 traduz SÓ a página (sim — livro inteiro é o 🌍 separado) · custo na hora (tokens + US$ + moeda do usuário) + telemetria · Kimi K3 demorou >1min (normal: modelos com raciocínio pensam antes; o aviso de paciência cobre) · "chave de zoom sumiu + janelinha de telemetria apareceu" (era o header de 2 linhas cobrindo o rail) · travão do livro inteiro com estimativa prévia (tokens/reais/tempo) · menu com itens demais → mover ⛶/👁 pra chave de zoom · 1 ícone com 2 submenus (telemetria + mural).

**Feito (commit `297315e`, deploy READY, hub 📊 confirmado no chunk do livro):**
- **Header emagrece:** ⛶ e 👁 migraram pra CHAVE DE ZOOM (abaixo dos +/−; 👁 mantém a regra de só agir em fullscreen).
- **📊 hub:** 1 ícone no leitor abre dropdown com "Suas IAs" (/telemetria) e "🏆 Mural das IAs" (/mural-das-ias) — labels nos 12 idiomas (tt).
- **💰 nota universal:** toda tradução de página (texto E imagem) termina com "—\n💰 US$ X (≈ R$ Y) · N tokens" (custo/usage reais do provedor, fallback estimativa; auto-save/histórico gravam o texto limpo). `translatePageStream`/`explainPageStream` passaram a devolver `usage` + `costUsd` no `AIActionResult`.
- **🧮 travão do 🌍:** na tela de confirmação, antes de começar: ≈ tokens do livro inteiro, ≈ US$ + moeda do usuário, ≈ tempo (~75s/volume) — best-effort, nunca bloqueia.

---

## Adendo 20 — crachá 📂 Drive: livro do Google Drive diferencia do baixado (25/08, ~10:16)

**Ordem do Miguel:** "o livro que estiver gravado como link do gdrive tem que estar diferenciado do livro que estiver baixado no dispositivo."

**Feito (commit `650cc33`, deploy READY, badge confirmado no chunk da estante):** `Session`/`ParsedBook` ganham `sourceOrigin` ("gdrive"); as duas vias do Drive (Picker e legada) marcam no `ingestBook(origin)`; a marca **viaja na nuvem dentro do jsonb `book`** (técnica da capa — sem coluna nova) e volta na leitura (nuvem pura + merge); badge azul **📂 Drive** no card ao lado do formato (EPUB/PDF). Upload local segue sem badge.

---

## Adendo 21 — telemetria: 3 linhas de gasto + 🧮 calculadora muda pro Mural (25/08, ~10:40)

**Ordens do Miguel:** (1) "na página de telemetria tem que ter datas e horas das tarefas e o total de gastos em 3 linhas: desde o início do uso do app naquele dispositivo, últimos 7 dias, últimos 30 dias"; (2) "o ícone calculadora no início da página de telemetria está em lugar estranho — até gostei, bota na página Mural das IAs".

**Feito (commit `6b7a98f`, deploy READY, provas no ar):** datas/horas já existiam no histórico (fmtDate dia+hora por tarefa — confirmado); **3 linhas de gasto** no topo da seção (US$ + moeda do usuário com marcador ativo; `tele_total_all/_7/_30` ×12 idiomas); **calculadora virou componente próprio (`CostCalculator`) e mudou pro Mural** — junto do ranking, onde se ESCOLHE IA (mostra US$ + ≈ moeda local sempre); telemetria volta a ser só o bolso.

---

## Adendo 22 — ⛔ FIM do Google Drive: removido da estante por completo (25/08, ~11:00)

**Ordem do Miguel:** "tentei entrar no google drive, bloqueou aqui. Esquece o google drive. Não vamos mexer nisso. Tira o google drive da estante. O usuário vai usar apenas arquivos em seus dispositivos. Essa experiência de bloqueio é muito ruim."

**Feito (commit `b6477d0`, deploy READY, botão confirmado REMOVIDO do ar):** botão 📂, modal, handlers e as duas libs (gdrive.ts, gdrive-picker.ts) deletados — upload só por arquivo local, definitivo. Pendência cosmética: env `NEXT_PUBLIC_GDRIVE` órfã no projeto espelho (token da API caiu no delete; inofensiva — limpar). Código inerte que ficou de propósito: badge 📂 Drive + `sourceOrigin` (documentado — se um dia voltar por Picker verificado, reaproveita; NÃO propor isso ao Miguel: a decisão foi definitiva, baseada na regra de ouro "nenhuma experiência negativa").

---

## Adendo 23 — faxina TOTAL + NOVA ARQUITETURA: espelho canônico × espelho ousadia (25/08, ~11:15)

**Ordem do Miguel:** "não deixa sujeira nenhuma — pode tirar tudo (crachá etc), mas deixa tudo guardado no Cérebro pra testar de novo noutra oportunidade. Acho que vamos precisar de um segundo espelho pros testes mais ousados. O espelho final tem que ficar igual ao canônico. Vamos fazer aos poucos. Prepara uma tarefa de 24 horas pra gente ir já fazendo o espelho ousadia, que é o espelho 2. O espelho 1 pode se chamar espelho canônico."

**Feito:**
- **Faxina total (commit `3d8d6fc`, estante 100% limpa no ar):** sourceOrigin saiu de Session/ParsedBook/repository/estante; badge 📂 e CSS removidos; 10 chaves i18n órfãs (`shelf_gdrive_*`) removidas dos 12 idiomas; classe gdrive-hint → tele-hint. Única sobra: env `NEXT_PUBLIC_GDRIVE` órfã no projeto Vercel do espelho (token da API caiu; inofensiva — pendência de limpeza).
- **Conhecimento arquivado:** `Memorias/memoria_moka_gdrive_arquivado_20260825.md` (fluxos, 3 paredes do Google, regra de lançamento, shas do git pra recuperar o código) — retorno só por Picker verificado, nunca propor.
- **NOVA NOMENCLATURA OFICIAL:** espelho 1 = **ESPELHO CANÔNICO** (moka-espelho.vercel.app — fica igual ao canônico + melhorias aprováveis; paridade ⊇ sempre); espelho 2 = **ESPELHO OUSADIA** (testes ousados; ainda não existe — nasce por plano).
- **Tarefa de 24h CRIADA (automação `automation-514072e4`, diária 09:10):** 1 passo por dia do plano F0–F5 — fórum-mestre `Foruns/forum_moka_ousadia_20260825.md` (repo GitHub moka-ousadia → projeto Vercel → envs → badge própria → provas; regras: nunca tocar espelho canônico/main; Telegram diário; desligamento proposto ao Miguel no F5).

---

## Adendo 24 — caixinha 📖 acende ao USAR LLM + recado turbinado + fim da nota colada (25/08, ~11:40)

**Ordens do Miguel:** (0) "o espelho 1 continua nosso laboratório até o ousadia ficar completo — registrado; (1) ao clicar em usar uma LLM nas configurações, a caixinha default de tradução/explicação tem que ACENDER nela; (2) o recado 'Traduzindo a página inteira' tem que dizer a LLM X e modelo Y, e que pode levar ALGUNS minutos (tradução OU explicação), com o texto aparecendo ali; (3) barra de tempo com % do trabalho; (4) o custo NÃO cola na página — só na caixinha pop."

**Feito (commits `c55f7aa` + `b1b4108`, deploy READY, barra confirmada no chunk do livro):**
- `setActiveEntry`: marcar `useForText` na entry ativada e apagar nas demais (single-select) — USAR acende a 📖.
- Recado de espera (EPUB e PDF): linha **"🤖 {LLM} · {modelo}"** + texto "pode levar alguns minutos" (12 idiomas; era "até 1 minuto") + **barra de progresso com %** (estimada pelo streaming: 95% teto até concluir, 100% no fim) + texto continua aparecendo na página.
- Nota 💰 REMOVIDA da página (tradução volta limpa; custo só no pop-up UsageToast). `usage/costUsd` continuam no `AIActionResult` (infra p/ futuro).

---

## Adendo 25 — recaída do menu ao fechar ANOTAÇÕES + 👁 destravador universal (25/08, ~11:50)

**Relato do Miguel:** "fui entrar em anotações, fechei, o menu sumiu de novo. Esse bug sempre volta de um jeito ou outro. Tinha que ter um jeito alternativo de desbugar na hora — tipo o olhinho. Porque cliquei em maximizar e voltar, e desbugou."

**Feito (commit `0177222`, deploy no ar — chunk do livro com hash novo):**
- **Cura estrutural ampliada:** o efeito que reexibe o menu agora também observa `notesOpen`/`bookmarksOpen`/`statsHubOpen` — o painel de Anotações era a porta aberta desta recaída (não estava nas deps). TODOS os painéis do leitor agora reexibem o menu ao fechar.
- **👁 destravador universal (ideia do Miguel):** o olhinho (agora na chave de zoom) fica SEMPRE clicável — fora de fullscreen, clicar **SEMPRE TRAZ o menu de volta** (destrava qualquer estado preso; nunca esconde); em fullscreen alterna como antes. O ⛶ maximizar→voltar também desbuga (constatação do próprio Miguel — toggleFullscreen reseta menuVisible nos dois caminhos).
- **Lição da hidra:** cada recaída do menu foi um mecanismo novo (overlay inline 01/08 → pop-up settings 09/08 → fullscreen órfão no voltar 25/08 madrugada → painel fora das deps 25/08 manhã). Com o destravador, o usuário NUNCA fica preso mesmo se uma quinta cabeça nascer.

---

## Adendo 26 — 🌍 Biblioteca 100% internacional + varredura PT hardcoded (26/08, ~09:45)

**Ordem do Miguel:** "coloquei em inglês na biblioteca e tá tudo em português ainda. O Moka tem que ser totalmente internacional — faz uma investigação, vê se tem muita coisa hardcoded."

**Investigação (2 scanners):** literais PT em JSX e em props (title/placeholder/alt) em todo app. **Feito (commit `f61fade`, biblioteca EN provada no ar):**
- **Biblioteca (a queixa central):** kicker "Biblioteca Livre" hardcoded → `bib_kicker` ×12; as 8 sinopses PT → **`sinopses: {pt, en}`** por livro (EN editorial escrito na mesma voz; pt-BR → pt, demais idiomas → en); CTA "Baixe direto pra sua estante" → `shelf_bib_cta` ×12.
- **Uso real:** título do bloco de causas no erro → `diag_causes_title` ×12; "Carregando página…" do PDF → `pdf_loading` ×12.

**Lote 2 registrado (fazer aos poucos, prioridade crescente):** textos das causas no `getSuggestedCauses()` (diagnostics — PT hardcoded), /privacidade e /sobre (editorial longo — precisa de decisão: traduzir ou manter PT), /tutorial, /video e /video/[id], ContaButton, InstallPrompt, VideoAskModal, SectionSwitcher ("Seções do Moka"), páginas /auth/*. Não-strings mas relevante: "Moka — Ir para página central" (title) e "Voltar à estante" (vários topbars).

---

## Adendo 27 — pop-up de gastos FIXO + Copiar + recado telemetria (26/08, ~10:15)

**Ordem do Miguel:** "o pop aparece e some muito rápido. Tem que ficar fixo e apenas ser fechado manualmente, clicando no X no canto, ou num botão Ok. Pode botar um botão também Copiar nesse pop. E um recado nele: os gastos serão guardados na sua página de telemetria."

**Feito (commit `4b1feca`, deploy READY, pop fixo provado no chunk):** `UsageToast` sem auto-close (era 15s — ficava "rápido demais"): agora fica FIXO até o ✕ ou o novo **botão Ok** destacado; **botão 📋 Copiar** (resumo tarefa/LLM/tokens/US$ + moeda local numa linha, feedback "Copiado ✓" 2s); recado novo "📊 Os gastos serão guardados na sua página de telemetria" (usage_telemetry_note ×12). Link "📊 ver" e "não quero mais ver" preservados.

**Nota do caso da tradução (resolvido pelo Miguel):** só o DeepSeek estava marcado 📖 — o Kimi não; funcionou normal depois. App sadio confirmado (E2E passando de novo hoje).

---

## Adendo 28 — barra de progresso ficava em 0% (não enche nunca) (26/08, ~10:26)

**Relato do Miguel:** "a barra com percentual fica apenas no 0%, ela não está mexendo — tinha que ir enchendo pra dar noção do andamento".

**Causa:** a barra existia SÓ dentro do recado de espera (waiting). O código troca a espera pelo texto assim que o PRIMEIRO chunk chega — ou seja, a barra morria junto com o recado antes de ter tempo de encher. **Cura (commit `d9a1100`, provada no chunk do livro):** a barra agora vive no TOPO (sticky) do texto que vai fluindo — EPUB e PDF — durante TODA a `translatingPage` (enchendo de verdade conforme o streaming), e continua no recado de espera antes do 1º chunk. Progresso calculado pelo texto recebido (95% teto, 100% no fim).

---

## Adendo 28b — barra da ESPERA (antes do texto) anda por TEMPO (26/08, ~10:44)

**Esclarecimento do Miguel:** "a barra só depois que aparece o texto é que anda — mas a PRIMEIRA barra (do recado de espera, onde demora mais) fica presa em 0%. Era legal ter o percentual aí."

**Causa:** o % vinha só do texto recebido; antes do 1º chunk (IA "pensando"/thinking) nada chega e a barra morria em 0% — exatamente a parte que mais demora. **Cura (commit `b0fe07f`, provada no chunk):** na espera inicial a barra sobe por TEMPO até 35% (rápido no início, desacelerando perto do teto, `+max(0.4, (35-prev)*0.06)/1.2s`); ao chegar o texto, o % real assume com piso 35 (nunca volta); barra do topo segue até 95% e fecha em 100%. Timer limpo no 1º chunk, no fim e no erro.

---

## Adendo 29 — 🧩 galeria de ícones na ajuda + Zé Moca i18n ("John Moca" EN) + anotações (26/08, ~11:23)

**Ordens do Miguel:** (1) no começo da ajuda, explicação dos ícones (repete o ícone grande + para que serve) — simpático; (2) "Pergunte ao Zé Moca" aparece em PT com bandeirinha americana — traduzir; (3) em inglês o nome dele é **John Moca**; (4) vê se o Zé Moca funciona/responde; (5) ver se a gente consegue um bot GRATUITO ligado ao banco de dados do Moka (avaliação); (6) slugs de página em inglês (anotar, aos poucos); (7) tirar o resto do hardcode (anotar, aos poucos).

**Feito (commit `fed449e`, deploy READY, galeria+John Moca provados no ar):** galeria com os 12 ícones do leitor em tamanho grande + explicação {pt, en} antes de "Como o Moka funciona"; título do robô `help_zemoca_title` ×12 (EN = "Ask John Moca").

**Sobre o Zé Moca (resposta ao "da onde veio / funciona?"):** ele é um robô de **busca local na FAQ** (palavras-chave em PT/EN, offline, sem gastar IA) — criado na página de ajuda com o Miguel (símbolo 🧑‍🌾 roceiro com enxada). Responde de graça e já funciona (FAQ_PT e FAQ_EN por idioma). **Não é LLM** — então o "bot gratuito ligado ao banco do Moka" já existe por design (ele explica o app sem custo); se um dia quisermos IA conversando, avalio modelo grátis (OpenRouter free/Gemini free) sem chave do usuário — anotado como avaliação futura, sem promessa.

**Anotado (aos poucos, sem quebrar):** slugs de página em inglês (/, /biblioteca→/library etc., com redirect) e o resto do PT hardcoded (lote 2 do adendo 26).
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/tmp/zcode-a7281bd1-3f33-4b37-9906-0b758dded36e-cwd'; fi
exit "$__zcode_status"


---

## Adendo 30 — 🚀 MERGE EXECUTADO (canônico reformado) + ESPELHO 2 (OUSADIA) NO AR (26/08, ~11:50)

**Ordem do Miguel:** "leva tudo já para o canônico, o espelho 1 está certinho. E cria o espelho 2 — as experiências doravante vão ser no espelho 2; quando tudo certo, sobe pro espelho 1 (camada de confirmação), e depois pro canônico (público)."

**Executado e PROVADO:**
- **MERGE:** `main ← espelho` (commit `363a6e0`, merge -X theirs; 21 arquivos, +1443/−177 — Mural página própria, calculadora no Mural, TeleCharts, hub 📊, galeria de ícones, i18n biblioteca, Drive removido/limpo, e TODOS os fixes do sprint). Canônico (www.mokareader.com) deploy READY. **Provas: 7 rotas 200** (/, /configuracoes, /telemetria, /mural-das-ias, /estante, /ajuda, /biblioteca) + **badge 🧪 AUSENTE no canônico** (env-gated ok). GA4 guard confirmado (não vaza pro espelho).
- **ESPELHO 2 (OUSADIA) criado e NO AR:** https://moka-ousadia.vercel.app (200) — repo `migueldorosario1/moka-ousadia`, projeto Vercel `prj_cAXX3GT1pVZTz6Efvs5qUqbB1D3Z`, branch local `ousadia`, remote `ousadia-mirror`, 9 envs criadas (públicas + servidoras dos cofres, sem exibição), badge **🎢 OUSADIA** em todas as páginas (commit `99f07b4`, provado no bundle). F1–F4 do plano da automação CONCLUÍDOS por esta sessão (a ronda diária deve assumir o F5/fechamento no fórum do ousadia).
- **Fluxo oficial (Miguel):** experiências no ESPELHO 2 → certo → ESPELHO 1 (camada de confirmação) → certo de novo → CANÔNICO (público). Espelho 1 = estável.
- **Telegram de confirmação enviado ao Miguel.**
