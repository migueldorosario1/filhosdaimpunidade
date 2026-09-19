# 👷 FÓRUM — OBRA MOKA: CHEFIA ZM + PRINTS 30/30 (30/08/2026)

<!-- 🌙 RONDA MOKA NOITE — ATIVA até 07:00 de 01/09 (ordem do Miguel 31/08 ~22:30) -->
## 🌙 PROTOCOLO DA NOITE (todo despertar do ZM 30/30 executa isto primeiro)
1. Anti-colisão §112: AGY pode estar no repo. Checar `git -C ~/ZCodeProject/moka-app status --short` (2× com 60s) + tail deste fórum. Sem adendo "TERMINADO — ZM pode revisar" → NÃO tocar no repo.
2. Com "TERMINADO": revisar diff → build → publicar ousadia-mirror → provar curl → adendo + ponte.
3. Ping Telegram do Miguel (ponte_cafezinho --send, só positivo/neutro, 1-2 frases).
4. Atualizar linha do monitor.

---


> Tema Duplo: este fórum (decisões) + `Memorias/memoria_obra_moka_chefia_zm_20260830.md` (log técnico).
> Origem: ordem do Miguel via DSC-021 (ponte, 13:24) + prompt DSC-026 (sessão dedicada MOKA PRINTS) + **"vai" direto do Miguel (14:02)**.

## O que aconteceu (30/08)

1. **ZM aceita a CHEFIA DA OBRA MOKA** (DSC-021): missão longa, com calma, ATÉ O FINAL — MEMÓRIA v1 → HARNESS beta → WRITER simplificado; ícones GRANDES com AGY (DSC-019); meta Play Store. Aceite publicado na ponte: **ZM-20260830-008** (commit `48a709fe3`).
2. **Alinhamento direto com o Miguel (14:02)**, dele: prints 30/30 = só a GARANTIA (despertador fotográfico); a obra é o trabalho inteiro até o final, material pronto; rondas podem estourar; transparência e linguagem humana, não técnica.
3. **MOKA PRINTS 30/30 NO AR**: script `cerebro-miguel/scripts/moka_prints_ronda.sh` + automação ZCode `automation-25e54785` (:10/:40 — não colide c/ DSN :00/:30 nem AGY :05/:35). 1ª ronda 13:59 = **12/12 prints** (home/biblioteca/ajuda/writer × cel 375x812 · ipad 768x1024 · pc 1366x768) em `cerebro/Insumos/moka_prints/`, linha por ronda na ponte, commit seletivo (nunca -A), site SÓ LEITURA.

## Decisões

- **"Livro aberto"**: não existe público sem sessão (livros ficam no aparelho do usuário) → captura `/biblioteca` como proxy, limitação declarada na ponte; se o Miguel der URL de livro aberto real, entra no script.
- **Sync × pasta nova**: sync ignora `ponte_laura_completa` (ZL-027) e não deleta nada — prints vivem só no repo `cerebro-miguel` (git), publicados a cada ronda.
- **Risco declarado** (decisão futura do Miguel): ~1,5MB/ronda × 48/dia ≈ 70MB/dia de PNGs no repo. Biblioteca contínua é a ordem; rotação só se o Miguel pedir.

## O que falta (a OBRA)

1. **MEMÓRIA v1** (agora): conversor .md/frontmatter + objeto pesquisável (metadados completos, anti-poluição) + manager (tirar/trocar/importar/criar) + orçamento de tokens SÓ p/ grandes (estimativa→confirmação→custo real) + auto-memória. Specs: DSC-014/017/018/019; arquitetura DSC-021a (memória INDEX.md).
2. **HARNESS beta**: chat web BYOK, entra pelo site, zero install, PWA.
3. **WRITER simplificado**: protótipo mokawriter com visual Moka.
4. **Ícones GRANDES** (cel/iPad/PC): AGY lidera UI usando a biblioteca de prints.
5. **Play Store**: meta final (cadastrar dev account correndo em paralelo — ideia DS-094).

## O que preciso de você (Miguel)

- Nada por enquanto — obra em curso. Testes no celular serão pedidos nos checkpoints de fase (gates CL/CM).
- Opcional: URL de "livro aberto" se quiser essa tela fotografada de verdade.

— ZM · ZCode/GLM-5.3 · 20260830 14:10 BRT

## Adendo 1 — Etapa 1 (MEMÓRIA v1) PRONTA + checkpoint 2 (15:12 BRT)

- **Checkpoint 1 (`2721c15`, ZM-009):** módulo 🧠 completo no espelho — conversor .md/frontmatter, anti-poluição com motivo na tela, busca instantânea (sem acento, título>tags>resumo>corpo), manager (ver/tirar/importar/exportar/drag&drop), multi-memórias (perfis), export portátil 1 .md com Índice (INDEX.md do DSC-021a), orçamento `orcamento.ts` (tokens latim ÷4 / CJK ÷1,5 + custo pelo ranking oficial + recibo com usage real). Branch `obra/memoria` (base `420aad3` = main/ousadia/espelho alinhados). IndexedDB v3 (só ADICIONA stores — estante intacta).
- **Checkpoint 2 (`b4f642d`, ZM-010):** tradução de livro inteiro ponta a ponta — estimativa (25/08) + **confirmação forte** (2 cliques: "Tem certeza? ≈ US$X com a sua chave") + **recibo REAL** (soma usage verdadeiro via evento `moka:usage`, moeda local) + **auto-memória** (livro traduzido entra sozinho, tipo `traducao`, custo no frontmatter; volume único no fim, multi-volume ao integrar — merge agora devolve o livro). 5 strings ×12 idiomas.
- **Espelho:** https://moka-espelho.vercel.app/memoria (HTTP 200 + "Moka Memória" pt-BR servido). Canônico intocado (promoção só c/ aval).
- **Despertador prints:** agora 5 telas × 3 tamanhos = 15/ronda (+/memoria).
- **Estado:** Etapa 1 ✅ aguardando aval do Miguel · **Etapa 2 (HARNESS beta) começando** · Ícones grandes = AGY com os prints.

### O que aconteceu / o que falta / o que preciso do Miguel
- **Aconteceu:** obra aceita e rodando; Memória v1 + orçamento completos no espelho; despertador 30/30 no ar.
- **Falta:** HARNESS beta (chat BYOK que conversa com a memória) → WRITER simplificado → ícones grandes (AGY) → Play Store.
- **Preciso do Miguel:** testar no espelho (celular/iPad) e dar o aval de promoção da Etapa 1 pro canônico; resto eu sigo sozinho.

— ZM · ZCode/GLM-5.3 · 20260830 15:15 BRT

## Adendo 2 — RITO DOS AMBIENTES (ordem do Miguel ~15:50, 30/08)

**Ousadia (experiências) → Espelho 1 (confirmado) → Canônico (certinho).** Corrigido na hora: obra (etapas 1+2) publicada no OUSADIA moka-ousadia.vercel.app (`/memoria`+`/harness` 200 provados); Espelho 1 devolvido ao pré-obra (3 Reverts; `/memoria` 404 provado); canônico intocado. Despertador de prints fotografa /memoria no Ousadia. ⚠️ Lição Vercel: force-push a commit antigo NÃO re-deploya — usar commit de revert. Promoção entre ambientes SEMPRE por confirmação do Miguel. — ZM · ZCode/GLM-5.3 · 20260830 16:05 BRT

## Adendo 3 — Estante→memória, biblioteca, orçamento internacional + fábrica de testes (30/08 ~16h, ZM-015/commit 6039dd2)

Ordens do Miguel ~16h atendidas: botão 🧠 embaixo de cada livro na estante (jogo local grátis); "Importar da biblioteca" na /memoria; OrcamentoModal internacional (modelo BYOK ativo + tokens + tempo + US$ + moeda do usuário via CURRENCIES — zero hardcode; usado no Corrigir do Writer); SectionSwitcher 100% i18n (sec_* ×12). FÁBRICA DE TESTES: moka_teste_ronda.sh roda 1 teste E2E diferente a cada 2h (gancho na 4ª ronda do despertador automation-25e54785 — a sessão da automação não pode criar 2ª automação, learnings), tira print e delega KIT de revisão na ponte pra fila DS-N→AGY→DSC→CL; 1ª ronda: teste memoria ✅ (kit p/ AGY). LOG_TESTES.md na pasta moka_prints. — ZM · ZCode/GLM-5.3 · 30/08/2026 15:33 BRT (carimbo real)

## Adendo 4 — Menu padronizado + Harness valorizado + kinds + NUVEM + PREMIUM (30/08 ~17h, ZM-016, commit 1a3361a)

- **TopNav**: mesma barra grande em todas as páginas da obra; 👁️ esconde o menu (preferência salva); mobile 52px. Pendência AGY: estender às páginas restantes.
- **Moka Harness = nome próprio** (12/12 idiomas); tagline "A IA do Moka"; botão 💬 Moka Harness.
- **Kinds de memória (ordem do Miguel)**: 🎒 bagagem × ⚡ operacional — perfis tipados; Harness consulta ambas (contextos separados).
- **NUVEM da cortesia (pergunta do Miguel: Backblaze ou Cloudflare?)**: parecer ZM = **Cloudflare R2** (10GB grátis + egress ZERO — leitura da memória sem custo de tráfego; S3-API; casa já tem conta/buckets R2 vivos) e **B2 como 2ª opção** (também S3-API; a casa domina). O conector do Moka será **S3-genérico** → suporta os DOIS: a casa oferece a cortesia no R2; quando a pessoa estoura, ela cola o token PRÓPRIO (R2 ou B2) — aviso de limite no dia ~28 (transparência DSC-018). **Aguarda: "vai" do Miguel + credenciais do bucket de cortesia.**
- **MOKA PREMIUM (visão do Miguel ~17h)**: plano que oferece memória na nuvem + AS IAs DA CASA (a pessoa escolhe qual IA pra ler / escrever / vídeo) + escolha de plano; **fase atual = tudo BYOK** (a pessoa usa a própria credencial; o Premium é a evolução comercial). Integrar ao plano de negócios existente (`memoria_moka_plano_de_negocios_20260722.md`) quando virar sprint.

— ZM · ZCode/GLM-5.3 · 30/08/2026 BRT

## Adendo 5 — Bucket R2 de cortesia CRIADO pelo ZM + rito [SEGREDO] (30/08 ~16h)

Ordem do Miguel ("vê se você consegue criar também... quero que você tenha essa autonomia"): a credencial R2 da casa (cafezinho) TEM poder de criar bucket → **`moka-memoria-cortesia` criado via rclone** (30/08 16:02 BRT, escrita+leitura provadas, carimbo no bucket). Registrado nos 2 cofres `.env.unificado` (backups datados) + NODE_COFRE. B2 de backup pendente (chave multi-bucket é restrita a 1 bucket). **RITO DE ENTREGA DE CREDENCIAL (definido com o Miguel ~16h, prático, sem vídeo):** ele cola tudo num bloco só começando com `[SEGREDO]` no chat; ZM grava direto no cofre intake, espelha nos irmãos com backup, registra apenas NOMES+sha8 no NODE_COFRE, nunca repete valores, nada vai pra ponte/fórum. — ZM · ZCode/GLM-5.3 · 30/08/2026 BRT

---

## 🔧 ADENDO 6 — 31/08 ~10:10→10:35: CONCERTOS DO 1º TESTE DO MIGUEL (commit ee8df8b, Ousadia)

**Gatilho:** Miguel viu o Ousadia pela 1ª vez pós-reforma (áudio ~10:10) e listou os defeitos.

**O que ele viu → o que estava → a cura (tudo no commit `ee8df8b`, 17 arquivos, build ✓, push `obra/memoria:main` no moka-ousadia):**

1. **"Um tá bege, outro tá azulzinho"** → biblioteca/ajuda tinham fundo `#fff6ee` fixo (resto usa `var(--bg)`) → `.bib`/`.help` agora acompanham o tema da casa (bônus: dark mode volta a funcionar nelas).
2. **"Dois Mokas no alto, um pouco diferentes"** → página de vídeo aninhava o TopNav DENTRO do header antigo (logo duplo) → wrapper morto; vídeo e vídeo/[id] agora usam TopNav puro.
3. **"Menus em lugares diferentes / sem ícone da estante"** → biblioteca/ajuda usavam header antigo sem o menu de 5 seções → TopNav em TODAS as páginas internas + `TopNavActions` (voltar, conta, idioma, engrenagem, telemetria — MESMO bloco em toda parte).
4. **"PDF pesado ficou parado mudo / não leu"** → parse é leve, mas verificar páginas escaneadas + eleger capa (renderiza até 11 páginas) é o gargalo sem feedback → **barra de progresso com % por etapa** (abrir 8% → verificar páginas 10-40% → capa pág. n/N 45-90% → salvar 96%), na estante vazia e cheia, `pdf-cover.ts` com `onProgress`, 4 strings ×12 idiomas.
5. **"E o token do Cloudflare/Backblaze?"** → **memória na nuvem BYO-bucket NO AR**: `lib/cloud.ts` (cofre AES-GCM igual ao das chaves de IA), `lib/cloud-s3.ts` (cliente S3 SigV4 100% navegador, path-style, R2/B2/S3 genérico), seção "☁️ Memória na nuvem" nas configurações (provedor + credenciais + bucket + **testar conexão** com diagnóstico credencial/bucket/rede-CORS) e botões **☁️ salvar / ⬇️ restaurar** na página Memória (backup = `moka-memoria/memoria-latest.md` + datado). 33 strings ×12 idiomas.
6. **G-Drive** → parecer pro Miguel: NÃO agora (OAuth de app publicado exige verificação Google + refresh token de app "em teste" expira em 7 dias = exatamente a "experiência ruim de travar" que ele teme). R2/B2 com chave estática é o caminho; G-Drive fica como estudo futuro.

**Estado:** consertos 1-5 entregues no Ousadia. **Falta:** Miguel testar de novo (recarregar); CORS do bucket cortesia R2 se quiseremos usar o nosso; B2 app key ainda nasceu sem escopo (pendente Miguel recriar Read&Write).

**O que preciso do Miguel:** testar o Ousadia de novo (cores unificadas, subir o PDF pesado de novo pra VER a barrinha, e se quiser colar um token R2/B2 próprio em ⚙️ → ☁️).

---

## 🔧 ADENDO 7 — 31/08 ~10:40→10:48 (errata: 1ª versão dizia 11:20 chutado; hora real medida): REFORMA DO LEITOR + CONFIG PADRONIZADA (commit 1131cfe)

**Gatilho:** 2ª rodada de teste do Miguel (entrou no EPUB — "o arquivo leve entrou, está na estante"; o PDF pesado segue em observação com a barrinha do adendo 6).

**Pedido → entrega (commit `1131cfe`, build ✓, 5 rotas 200, push Ousadia):**
1. **"Menu do livro: ícones muito pequenos, resume em 3-4 botões GRANDES que abrem submenus"** → `Reader.tsx` reformado: fileira de 14 icon-btns substituída por **3 botões grandes centrais** (`reader-big-btn`, 46px, mobile 52px): **📖 Página** (submenu: 🔊 ler em voz alta c/ estado dinâmico, 📝 resumir/explicar, 🌐 traduzir página incl. fluxo visão p/ scan, 🌍 traduzir livro inteiro se EPUB), **📌 Marcar** (submenu: 🔖 marcar página, 📸 foto, 📓 notas c/ contagem), **🎤 Perguntar** (abre AskModal direto). Logo/➕/📚/⏹ continuam pequenos no canto. Dropdowns com backdrop (padrão stats-hub).
2. **"Menu da direita: ajuda + suas IAs/telemetria + mural + configurações TUDO NUM SÓ"** → 1 botão ☰ (`reader-more-btn`) com dropdown: ❓ Ajuda · 📊 Suas IAs · 🏆 Mural · ⚙️ Configurações (badge se IA não configurada). Bandeirinha e login ficam soltos.
3. **"Configurações com logo dos dois lados, menu desconfigurado"** → right do TopNav da config era `AuthGate+LangSwitcher+✕+brand+label` (brand duplicado!) → agora `<TopNav right={<TopNavActions />} />` padrão da casa. Prova curl: `cfg-topbar-label`/`cfg-close-btn` = 0 no HTML servido.
4. **Prompt de CHECAGEM pro Antigravity Desktop** (bom de visão): `Foruns/PROMPT_AGY_CHECAGEM_MOKA_20260831.md` — papel = olho independente, 9 itens ✅/❌ com print, ANALISA sem editar (regra da casa: parecer antes de executar). SEM credenciais (alvo é site público).

**Estado:** no ar no Ousadia. Leitor (/book/[id]) é client-side — validação visual fica pro Miguel abrir o EPUB da estante + AGY checar.
**Falta:** Miguel testar o leitor novo; AGY devolver o parecer; PDF pesado re-testar c/ barrinha.
**Do Miguel:** rodar o prompt no Antigravity Desktop e trazer o parecer.

---

## 🔧 ADENDO 8 — 31/08 31/08/2026 10:52: AVISO DE PDF GRANDE NO UPLOAD (commit 1d18ebe)

**Pedido do Miguel (quase literal):** "quando for PDF grande que ele vai renderizar pra achar a capa, bota um textinho 'renderizando pra achar a capa', bota a barrinha de percentual… 'livro de tantos megas, PDF, vai demorar um minuto ou dois pra subir tudo renderizando pra encontrar a capa'".

**Entrega (commit `1d18ebe`, build ✓, estante 200):** ao escolher um **PDF ≥10 MB**, a barra abre JÁ DIZENDO: *"Livro de X MB (PDF) — vai demorar um ou dois minutos pra subir tudo, renderizando pra encontrar a capa…"* (acima de 80 MB: "alguns minutos"). A etapa da capa virou *"Renderizando pra achar a capa — página n de N…"*. Megas calculados do tamanho real do arquivo; estimativa por faixa (10-80 MB = "um ou dois minutos"; >80 MB = "alguns minutos"); PDF <10 MB e EPUB mantêm "Abrindo o livro…". `ingest_cover` atualizado ×12 + 3 chaves novas ×12.

**Estado:** no ar no Ousadia. **Falta:** Miguel testar com o PDF pesado dele.

---

## 🔧 ADENDO 9 — 31/08 31/08/2026 11:37: CAPA LIMPA + SUBMENUS DO LEITOR DESTRAVADOS (commit d2c89c3)

**Gatilho:** 1º teste do Miguel no CELULAR + iPad. Diagnóstico dele: "cheio de menu em cima da capa, ficou horroroso — tira tudo"; "menu do leitor não abre no celular… o Marcar não abre submenu no iPad"; "o menu ficou em cima do joguinho vertical (zoom)".

**Causas raiz achadas e curadas (commit `d2c89c3`, build ✓, capa/estante 200):**
1. **Capa:** TopNav REMOVIDO do topo (capa = cartão limpo: kicker, logo MOKA, tagline, 2 caminhos grátis, e a família embaixo). Botões da família REDESENHADOS: ícone grande (34px) em destaque + nome + descrição, TODOS DO MESMO TAMANHO (fim da largura dupla do ⚙️ e da fonte menor), sombra suave + hover elevado; mobile 2×3. Prova no HTML servido: topnav=0, 6×capa-launch-ico, settings-classe-dupla=0.
2. **Submenus "que não abrem" (iPad/celular):** o grupo dos 3 grandes estava DENTRO da `reader-row-scroll` (`overflow-x: auto` → o navegador corta TAMBÉM na vertical → dropdown renderizava cortado/invisível). Movido pra fora; header agora é GRID de 3 áreas (`left | big | right`); no ≤760px quebra em 2 linhas (pequenos+controles em cima, 3 grandes embaixo).
3. **Zoom-rail coberto:** header crescido passava por cima da chave vertical de zoom (top fixo 64px) → no mobile ela desce pra 132px.

**Prompt AGY atualizado** (capa = exceção limpa; submenus exigem teste no celular; zoom-rail visível).
**Estado:** no ar. **Falta:** Miguel re-testar no CELULAR (submenus 📖/📌 têm que abrir agora) + parecer AGY.

---

## 🔧 ADENDO 10 — 31/08 31/08/2026 12:14: chip LLM + ícone duplo morto + ajuda/tutorial (commits 328bce3, fd9d8b2)

**Pedidos do Miguel (~11:4x):** ícone do Harness duplicado na Memória; mostrar qual LLM está ligada (e trocar); confirmar trava de consumo; ajuda/tutorial atualizados com as novidades; auditoria hardcode; e a questão da memória unificada/virtual (respondida por escrito).

**Entrega:**
1. **Ícone 💬 duplicado na Memória** → era o botão "Conversar" (harness-link) no corpo, redundante com o 💬 do menu de cima — removido.
2. **Chip da LLM ligada** → `components/LlmChip.tsx`: no topo do Harness E do Writer, "🔌 Ligado: {provedor · modelo} — trocar" (um toque abre configurações); sem IA: "⚠️ Nenhuma IA configurada" vermelho. Fonte: `getEntryForText()` + `PRESETS` do ai-providers.
3. **/ajuda** → +3 FAQs (PT e EN): menu do leitor com submenus; Memória na nuvem R2/B2; por que PDF grande demora (barrinha).
4. **/tutorial** → passo 6 NOVO ×12 idiomas: os 3 botões grandes com submenus + memória na nuvem.
5. **Hardcode:** title do logo do leitor virou `reader_home_title` ×12; blocos novos auditados (tudo t()); nomes "Moka Reader/Harness" ficam (marca, não se traduz).
6. **Trava de consumo (pergunta)**: SIM, funciona — avisos e trava nas configurações seguem no ar; transcrição de vídeo só com chave própria (como ele disse).
7. **Deploy engolido**: o 328bce3 não propagou (chunk antigo na CDN); commit vazio `fd9d8b2` redisparou e provou (FAQ novo no HTML+JS). Lição: Ousadia estático + query string NÃO burla cache — provar via chunk JS (`/_next/static/chunks/app/ajuda/page-*.js`).

**Memória unificada (parecer arquitetura, respondido ao Miguel):** o desenho que ele descreveu (credencial própria Cloudflare/B2 → memória disponível em qualquer aparelho) É o que está NO AR desde o adendo 6 (⚙️ → ☁️ + Salvar/Restaurar na página Memória). Próximo degrau quando ele quiser: sincronização automática (pull no abrir + push periódico) e lista de backups datados pra escolher.

---

## 🔧 ADENDO 11 — 31/08 31/08/2026 12:17: bandeirinha de idioma DE VOLTA na capa (commit a83a210)

Correção do adendo 9: ao tirar o TopNav da capa eu tirei junto a bandeirinha de idioma — ordem do Miguel: "a bandeirinha era pra ficar, era importante". Ela voltou SOZINHA no topo direito (`.capa-lang`), sem o resto do menu. Provas: capa-lang=1 no HTML estático, topnav=0, chunk JS confere. Deploy propagou de primeira.

---

## 🔧 ADENDO 12 — 31/08 31/08/2026 12:24: livro da memória → ESTANTE (commit 4eb7882)

**Pergunta do Miguel:** "quando uma coisa está na memória da nuvem, o livro pode aparecer na estante?"

**Entrega:** objetos da memória tipo `livro` ganham botão **"📖 Pra estante"** no card — reconstrói os capítulos do texto do objeto (`## Título` → chapter com paragraph blocks; `sourceFormat: "txt"`), gera capa dinâmica e salva na estante (`saveToLibrary`). Ciclo fechado: **nuvem → Restaurar → memória → 📖 Pra estante → livro navegável**. Nota honesta: volta como TEXTO (capítulos navegam, IA resume/traduz); o arquivo original (PDF escaneado) não é guardado na nuvem — backup da estante com binários fica como próximo passo se o Miguel pedir. Ajuste: "Outro (S3)" → **"Outro — S3 compatível"** ×12 (estava estranho).

**Estado:** no ar (prova no chunk JS page-a5a0f7d8). Miguel testando Cloudflare R2 — CORS do bucket é obrigatório pro teste passar (instrução com JSON colável enviada na resposta).

---

## 🎯 ADENDO 13 — 31/08 31/08/2026 13:00: REGRA DE OURO DA ESTANTE + backup com ORIGINAIS (commit 983ec62)

**Regra do Miguel (quase literal):** "Pra memória, beleza, volta como texto. Pra estante tem que voltar o PDF e o EPUB ORIGINAL. Na estante não pode ter livro convertido pra texto." → REGRA ARQUITETURAL: **memória = texto permitido; estante = só arquivo original.**

**Entrega (commit `983ec62`, build ✓, provas no chunk JS):**
1. Botão texto→estante REMOVIDO da memória (voltou atrás no adendo 12).
2. `Session.epubSource` novo — ingestão agora guarda o original do EPUB também (PDF já guardava `pdfSource`).
3. Estante: **"☁️ Salvar estante na nuvem"** — por livro: `moka-estante/<id>.bin` (arquivo original em BYTES CRUS, sem base64) + `<id>.json` (capa, progresso, metadados). Livros antigos (adicionados antes desta versão, sem original guardado) são pulados com aviso explícito ("reabra o arquivo pra incluí-los"). **"⬇️ Restaurar estante"** — lista o prefixo, baixa bin+json, reparsa o ORIGINAL e reconstrói a Session inteira (capa e progresso de volta) em qualquer aparelho.
4. cloud-s3: `cloudPutBytes`/`cloudGetBytes` (octet-stream) + `cloudList` (ListObjectsV2 por prefixo, regex no XML).
5. 7 chaves ×12; FAQ da ajuda atualizada (memória = texto; estante = original inteiro).

**Estado:** no ar. **Falta:** Miguel testar E2E com o R2 dele (CORS do bucket é pré-requisito — rito já enviado).

---

## 📘 ADENDO 14 — 31/08 31/08/2026 13:09: RITO CLOUDFLARE R2 PRO USUÁRIO (guardar p/ virar /ajuda)

**Ordem do Miguel:** "Guarda essas instruções para instruir o usuário também… espera só dar certo, aí a gente bota para instruir o usuário." → Rito validado parcialmente (Miguel criou o bucket sozinho; editor CORS do Cloudflare vem com placeholder localhost que deve ser SUBSTITUÍDO, não acrescido).

**RITO (formato usuário final):**
1. **Criar a conta/bucket:** dash.cloudflare.com → conta grátis → menu **R2 Object Storage** → **Create bucket** → nome `moka-estante` (ou outro) → região automática. (Plano grátis dá 10 GB — de sobra.)
2. **Liberar acesso (CORS):** entre no bucket → **Settings → CORS Policy** → **APAGUE o exemplo** (o `localhost:3000`) e cole exatamente:
```json
[{"AllowedOrigins":["https://moka-ousadia.vercel.app","https://www.mokareader.com","https://mokareader.com"],"AllowedMethods":["GET","PUT","HEAD"],"AllowedHeaders":["*"],"MaxAgeSeconds":3600}]
```
   (sem CORS o navegador bloqueia com "falha de rede" — é a causa nº 1 de teste falho).
3. **Account ID:** nas Settings do bucket, quadro **S3 API** → o número gigante entre `https://` e `.r2.cloudflarestorage.com` (botão de copiar do lado).
4. **Chaves:** R2 Object Storage → **Manage API Tokens** → **Create API Token** → permissão **Object Read & Write** → escopo só no bucket → criar → copiar **Access Key ID** e **Secret Access Key** NA HORA (a Secret só aparece 1×).
5. **No Moka:** ⚙️ Configurações → ☁️ Memória na nuvem → **Cloudflare R2** → Account ID + chaves + nome do bucket → **🔌 Testar conexão** → "✅ Conexão OK" → 💾 Salvar.
6. **Usar:** página Estante → "☁️ Salvar estante na nuvem" (originais PDF/EPUB inteiros) / "⬇️ Restaurar estante"; página Memória → "☁️ Salvar na nuvem" (texto) / "⬇️ Restaurar".

**Glossário pro usuário (pedido do Miguel "o que é S3?"):** S3 = o "idioma padrão" de armazenamento em nuvem (nasceu na Amazon, virou padrão mundial); R2 e B2 falam S3. No app, Cloudflare/Backblaze são os caminhos guiados — "Outro — S3 compatível" é porta de emergência pra quem já tem outra nuvem.

**Quando o teste do Miguel passar:** transformar este rito em página/FAQ ilustrada no /ajuda (e talvez assistente passo a passo dentro das configurações).

---

## 🔐🔧 ADENDO 15 — 31/08 31/08/2026 13:37: credencial R2 do Miguel testada por ZM (caça ao 403) + fixes UX nuvem (commit 7fdb3b4)

**Contexto:** Miguel colou as credenciais R2 no chat (rito SEGREDO cumprido: gravadas nos 3 cofres c/ backup .bak_pre_moka_r2_miguel_20260831; registro por sha8 — AK 486accc5, SK 0aad5c03, token cfat ddc61e37; valores JAMAIS em fórum/ponte) e pediu: "testa aí você e conserta essas coisas".

**A caça ao 403 (crônica de diagnóstico):**
1. rclone no endpoint → **TLS handshake failure**. Suspeitei IPv6 (DNS local resolve só 6) — mas curl -4 também falhou.
2. Remote R2 da CASA funcionava (bookstore-moka etc.) → rede não bloqueia o domínio.
3. Miguel transcreveu a tela do token: endpoint REAL era `...eecd4afd4c0...` — **eu tinha lido errado o ID do print** (usei `...eecd4af4dc0...`, 2 chars invertidos pela visão). ID corrigido nos 3 cofres (Regra 4: errado fora, certo dentro).
4. Com ID certo: conecta! Lista buckets OK — mas **403 no moka-estante**: o token nasceu scoped SÓ pro `bookstore-moka` (a tela dele mostra "Buckets: bookstore-moka"). **Prova: ListObjects no bookstore-moka = 200 (viu capas/*.svg); no moka-estante = 403.**
5. **CORS do bucket moka-estante: PERFEITO** (preflight OPTIONS respondeu Allow-Origin moka-ousadia.vercel.app + GET/PUT/HEAD + headers — o JSON que o Miguel colou está ativo).

**ÚNICO passo restante pro Miguel:** recriar o Account API Token incluindo o bucket moka-estante (ou Apply to all buckets). Respostas às perguntas: NÃO mudar pra admin (Object Read & Write é o certo, admin é poder à toa), NÃO criar usuário novo.

**Fixes no app (commit `7fdb3b4`, provas no chunk page-538ec846):** botão ⬇️ Restaurar aparece na estante VAZIA (caso "novo aparelho" — era a queixa "não aparece o botão"); ☁️ Salvar não fica duro sem livros (avisa o que fazer, i18n ×12); input do Account ID com name próprio anti-autofill (o "já estava gravado" era o Chrome salvando, NÃO hardcode — prova: grep do ID no bundle = 0).

**Observação de conta:** o Miguel está usando a conta R2 DA CASA (a mesma do cafezinho/bookstore) — não uma conta pessoal. Pro Moka de usuário final cada um cria a SUA; pra teste interno, tanto faz. Registrado pra decisão futura (Premium: "quando logado fica na conta da pessoa" — pedido dele anotado).

---

## 🧯 ADENDO 16 — 31/08 31/08/2026 13:45: mistério do "ID colado" RESOLVIDO — era o placeholder (errata parcial do 15)

O "Account ID já gravado no campo" que o Miguel viu NÃO era autofill do navegador (hipótese errada do adendo 15) nem hardcode: era o **placeholder** `a1b2c3d4...c5d6` (fake de 32 hex que EU pus como exemplo de formato) — parecia valor real. 🔴 Lição de UX: placeholder de credencial NUNCA deve parecer valor. Corrigido (commit no ar): Account ID → "copie o Account ID do painel R2 (32 caracteres)"; bucket → "ex.: meu-bucket". Prova: fake sumiu do bundle, dica nova presente.

---

## 🧯 ADENDO 17 — 31/08 31/08/2026 13:52: fim do "onde acho o Account ID?" — cola o endereço Default e o app resolve (commit 2bd66ca)

Queixa do Miguel: a tela do token NÃO mostra Account ID (só Token value/Access Key/Secret + endpoints) — o ID só aparece EMBUTIDO no endereço Default. Corrigido na raiz: `normalizeHost()` aceita o endpoint completo colado (`https://<id>.r2.cloudflarestorage.com` → extrai o id; B2 endpoint/região idem); rótulo e placeholder ×12 convidam a colar o endereço. Nota de operação: o 1º envio deste commit foi cancelado no meio da PROVA (push chegou); o Miguel testou na janela em que o deploy ainda não tinha servido → "❌ Falha de rede" (endpoint colado no app velho = https:// dobrado). Prova do recurso no ar: chunk configuracoes page-1881bde2 contém o matcher do endpoint. Reteste pedido; se vier "credencial recusada" é o escopo do token (falta incluir moka-estante/all buckets).

---

## 🔧 ADENDO 18 — 31/08 31/08/2026 14:00: diagnóstico fechado do "falha de rede" + ✨ COLA MÁGICA (commit 07568ca)

**Fechamento do caso:** o Miguel RODOU (Roll) o token — senha nova (cofre rotacionado, sha8 221a8da3; Access Key ID igual), mas **Roll NÃO muda o escopo**: "Buckets: bookstore-moka" continua. Prova com a senha NOVA: ListObjects bookstore-moka **200** / moka-estante **403 AccessDenied**. 🔴 Descoberta técnica: **403 do R2 vem SEM os headers CORS** → o navegador lança TypeError → o app reportava "falha de rede" enganosa (não era rede nem CORS!). Correções:

1. **✨ Cola mágica** (pedido: "muito campo, simplifica — só a chave!"): textarea onde a pessoa cola a tela do token INTEIRA; o app extrai sozinho endpoint+Account ID, Access Key ID (32hex que não é o account) e Secret (64hex), e detecta o provedor pelo domínio. Campos continuam visíveis (preenchidos) pra conferência. 5 chaves ×12.
2. **Mensagem honesta**: "Falha de rede OU o token não tem acesso a este bucket — confira: CORS / token criado com acesso a ESTE bucket (All buckets resolve) / chaves certas" ×12.

**Como o Miguel termina o teste (2 caminhos):** (a) VITÓRIA IMEDIATA — trocar o nome do bucket no app pra `bookstore-moka` (o token já o acessa; teste passa na hora; não ideal pois mistura com a livraria); (b) O CERTO — Create Account API Token NOVO com **Apply to all buckets** (Roll não resolve) e usar `moka-estante`.

---

## ✅ ADENDO 19 — 31/08 31/08/2026 14:13: ✅ CLOUDFLARE CONECTOU NO CELULAR DO MIGUEL + acabamentos (commit novo)

**MARCO: a memória/estante na nuvem CONECTOU de verdade no teste do Miguel** (token novo com All buckets + moka-estante + cola mágica). Ele segue testando gravação de livros. Pedidos atendidos:
1. **Trocar de provedor LIMPA os campos** (continuavam os números do Cloudflare ao virar a abinha Backblaze — confuso).
2. **✨ Cola mágica Backblaze**: parser estendido — keyID (25 hex, com ou sem label) e applicationKey (K…); endpoint `s3.<região>.backblazeb2.com` já era detectado.

**Resumo do caso-escola (nuvem R2):** Roll não muda escopo · 403-scoped vem sem headers CORS e PARECE falha de rede · placeholder de credencial nunca pode parecer valor real · account id embutido no endpoint Default (agora a cola resolve).

---

## 🔧 ADENDO 20 — 31/08 31/08/2026 14:18: cola mágica preenche o BUCKET também (commit 33b7ab1)

Queixa do Miguel: "na tela do token vem o nome do bucket e você esqueceu do preenchimento automático" — correto: a tela lista "Buckets: <nome>". Parser estendido: extrai o primeiro nome após "Buckets:" (R2) e preenche junto; "All buckets" não tem nome único → continua manual. Prova no bundle servido. Miguel configurou o 2º dispositivo com a cola mágica ("configurei aqui rapidinho") — o fluxo rápido de novo aparelho funciona na prática.

---

## 🔧 ADENDO 21 — 31/08 31/08/2026 14:22: salvar POR LIVRO na nuvem + o mistério do "só veio 1 livro"

**Causa do relato do Miguel** (2 livros, só 1 restaurou): o EPUB antigo foi adicionado ANTES do app guardar o original de EPUB (`epubSource` nasceu no commit 983ec62) → o salvar-estante o pula (com aviso que passou batido). PDF de hoje foi com original inteiro ✓. **Cura pro caso dele:** reabrir o EPUB uma vez (＋ Adicionar livro) — a ingestão nova guarda o original e o próximo backup pega os 2.

**Entregue:** botão **"☁️ Salvar na nuvem" POR LIVRO** no card (ao lado do 🧠; pediu: "bota um botãozinho embaixo do jogar na memória") — manda só AQUELE livro (.bin+.json), vira ✅; livro antigo sem original → aviso explicando o reabrir; aviso do salvar-estante inteira agora vem com ⚠️ na frente dos excluídos. 3 chaves ×12.

---

## 💾 ADENDO 22 — 31/08 31/08/2026 14:27: BACKUP TRIPLICADO + prompt de DESIGN pro Antigravity

**Backup do marco:** tag `ousadia-memoria-nuvem-20260831` (commit `08c7ff5`) + branch `obra/memoria` empurrados pros 3 remotes (origin canônico, mirror espelho, ousadia-mirror) — nada se perde mesmo se o AGY mexer em tudo depois.

**Prompt de design:** `Foruns/PROMPT_AGY_DESIGN_MOKA_20260831.md` (fórum à parte, pedido do Miguel p/ não poluir o chat). Papel do AGY = REVISOR DE DESIGN que PROPOE (kit de botão com CSS, quick wins, nota de elegância) e NÃO executa — regra da casa (parecer antes do "vai"; quem aplica é o ZM no rito Ousadia→Espelho→Canônico). **Sem credenciais**: site público + código local (`~/ZCodeProject/moka-app`); chaves ficam nos cofres.

---

## 🎨 ADENDO 23 — 31/08 31/08/2026 20:13: PARECER DE DESIGN DO ANTIGRAVITY integrado (commit c39f816)

**O que aconteceu:** o AGY Desktop cumpriu o prompt de design (nota **7.2/10** de elegância; auditoria em 10 páginas via Puppeteer, desktop+mobile) mas **foi além do combinado: aplicou direto** no `globals.css` (164 linhas, acréscimo puro — nada apagado, nenhum outro arquivo). Parecer completo: `.gemini/antigravity/brain/eab3533f-902e-4188-8b9e-4d1e3b813d70/artifacts/parecer_design_moka_20260831.md`.

**Revisão ZM (guardião do rito):** kit seguro — refinou só botões existentes (capa/leitor) e criou classes novas (`.moka-btn-primary/secondary/ghost`) **sem uso ainda**. Build ✓, publicado no OUASADIA (laboratório) pro Miguel validar. ⚠️ Pendência de marca: primary do kit veio AZUL; identidade do Moka é quente (accent laranja) — decidir antes de adotar a variante. Registros do AGY: editou `CEREBRO_INDEX_MOKA_LOG.md` (ficha de diretórios lá é do legado Moka-Lab/Producao — obra ativa é `~/ZCodeProject/moka-app` branch `obra/memoria`; nota adicionada no arquivo) e o sub-cérebro dele (território AGY).

**Falta:** Miguel recarregar o Ousadia e opinar (gostou dos botões?); decidir azul×laranja no primary; "vai" do Miguel pra estender o kit às demais páginas (Memória/Config/Estante usam .cloud-btn/.memoria-btn — ainda com estilo antigo).

---

## 🎨 ADENDO 24 — 31/08 31/08/2026 21:12: fluxo de design CLAUDE→AGY + retificação da paleta

**Retificação importante:** a cor principal REAL do site é AZUL COBALTO (`--accent: #1e40af`) com porcelana `#f0f4f9` e dourado `#d97706` — o "laranja da marca" que o ZM citou no adendo 23 era fallback de CSS antigo do próprio ZM. O azul do kit AGY estava ALINHADO. Primary azul CONFIRMADO (decisão pendente anterior resolvida).

**Fluxo do Miguel (prompt em `Foruns/PROMPT_CLAUDE_DESIGN_MOKA_20260831.md`):** 1º CLAUDE como diretor de design (3 direções A/B/C com degradês especificados em hex, recomendação e regras de elegância — resposta 100% textual com paleta real colada no prompt); 2º AGY implementa a opção escolhida (template com placeholder pra resposta do Claude; regras: só apps/web/src, sem deploy — ZM revisa e publica; marco de rollback = tag ousadia-memoria-nuvem-20260831). Sensação-alvo: "sofisticado, sereno, caro — livraria de aeroporto de primeira classe".

---

## 🔑 ADENDO 25 — 31/08 31/08/2026 21:20: prompt AGY com acesso completo (mapa, não valores)

Pedido do Miguel: "prompt com acesso às credenciais do Cérebro e do Moka". Entregue em `Foruns/PROMPT_AGY_MOKA_COMPLETO_20260831.md`: mapa de tudo (repo/branch/remotes/tag de rollback, Cérebro/fóruns/índices, cofres por CAMINHO + nodo do cofre) com as regras inegociáveis da casa embutidas (valores de chave nunca em texto; teste de nuvem via rclone com remotes já configurados; design não precisa de credencial; parar e perguntar na dúvida). AGY continua sem poder de push/deploy — ZM revisa e publica.

---

## 🎨 ADENDO 26 — 31/08 31/08/2026 21:31: SPEC DO CLAUDE anotada + prompt final do AGY pronto

**Spec do Claude (diretor de design) gravada íntegra:** `Foruns/SPEC_CLAUDE_CORES_MOKA_V2_20260831.md` — 3 direções com hex exatos (A "Porcelana e Ouro" · **B "Amanhecer Azul" ⭐ recomendada** · C "Safira e Porcelana"), regras de elegância (Δ≤4% luminosidade, sombras tingidas safira, hierarquia 6 cards>secundários>pílulas), dark mode e notas de migração de emoji→ícones de linha. Claude cravou: "B — nenhnum usuário consegue apontar o que mudou".

**Prompt final do AGY:** `Foruns/PROMPT_AGY_APLICAR_CORES_MOKA_V2_20260831.md` — direção B embutida passo a passo (fundo fixed degradê ambiente, cards pé-azul, caixinha 135°, remoção do opacity 0.72, dark mode), regras do diretor inegociáveis, entrega (build limpo + prints claro/escuro + adendo no fórum), sem push (ZM publica). Fluxo: Miguel cola no AGY → AGY aplica → ZM revisa/publica no Ousadia → Miguel valida.

---

## 🎨 ADENDO 27 — 31/08 31/08/2026 21:52: "AMANHECER AZUL" NO AR (f5292b7) — fluxo Claude→AGY→ZM concluído

**Fluxo completo da casa funcionando:** Claude diretor (spec v2, direção B recomendada) → Miguel aprovou → Antigravity implementou (208 linhas, build exit 0, 4 prints) → **ZM revisou** (auditoria: 27 usos de var(--bg) todos em background shorthand — a troca cor→gradiente não quebra nada; cards/pílulas/caixinha fiéis à spec; !important usado à vontade mas funcional; .ft perdeu o papel-crema pelo amanhecer, coerente) → **olho ZM (4.5V) validou os prints nos 2 temas** → publicado no Ousadia `f5292b7`. Provas no CSS servido: f4f7fb (amanhecer) ✓ f4f8fd (pé azul do card) ✓ eaf1fb (caixinha gelo) ✓ 0b132b (dark noite) ✓. Prints do AGY: `.gemini/antigravity/brain/eab3533f-.../artifacts/screenshot_capa_v2_*.png`.

**Estado:** Amanhecer Azul no ar no Ousadia (claro+escuro, desktop+mobile). **Falta:** Miguel recarregar e dar o veredito; depois, com "vai", estender o refinamento às demais páginas (Biblioteca/Ajuda/Estante usam superfícies próprias) e considerar migração emoji→ícones de linha (cores já previstas na spec).

---

## 🔧 ADENDO 28 — 31/08 31/08/2026 21:57: prompt de ACABAMENTO DO MENU (diagnóstico com números)

Queixa do Miguel: xícara Moka colada no canto em algumas páginas / Writer diferente / menu tem que ficar estável / ícones do menu do mesmo tamanho. **Diagnóstico ZM:** o TopNav mora dentro do `<main>` de cada página e os containers diferem — estante SEM margem (logo a 0px do canto), memória 1080px, writer 880px, harness 820px → menu dança. **Solução especificada no prompt:** `.topnav` full-bleed (`margin-inline: calc(50% - 50vw); width: 100vw`) com padding próprio uniforme (20px/14px mobile) — containers seguem só pro conteúdo; ícones: caixa 46/52px com font-size e line-height iguais + correção óptica por emoji sem mudar a caixa. Prompt: `Foruns/PROMPT_AGY_ACABAMENTO_MENU_20260831.md` (com prints antes/depois de 8 páginas exigidos).

---

## 🔧 ADENDO 29 — 31/08 31/08/2026 22:00: MENU CLEAN no ar + prompt AGY ganha simetria

1. **Menu invisível por padrão NO AR** (commit `7466fe4`, ordem do Miguel "menu invisível como default, mais elegante"): TopNav nasce escondido; 👁 ABRE (era o contrário); preferência antiga respeitada; useState inicial true evita flash.
2. **Prompt do acabamento atualizado** (`PROMPT_AGY_ACABAMENTO_MENU_20260831.md`): contexto novo (não reverter o default escondido; acabamento vale pro menu ABERTO) + pedido novo "primeira e segunda linha, tudo mais simétrico" (grade com caixa/espaçamento iguais nas 2 linhas no mobile).

---

## 🔧 ADENDO 30 — 31/08 31/08/2026 22:10: TopNav FULL-BLEED no ar (fim da logo colada)

Queixa imediata do Miguel (~22h): "falta margem na esquerda, a logo ainda muito colada". Aplicado pelo ZM (sem esperar o AGY — era a solução do adendo 28): `.topnav` com `margin-inline: calc(50% - 50vw)` + padding uniforme (20px/14px mobile) → mesma margem em TODAS as páginas, independente do container de cada uma; `overflow-x: clip` no body pra neutralizar a scrollbar no truque 100vw. Commit publicado + prova no CSS servido (calc no bundle). Prompt do AGY segue valendo pra simetria fina das 2 linhas e tamanho ótico dos ícones.

---

## 🎨 ADENDO 31 — 31/08 31/08/2026 22:13: prompts de PADRONIZAÇÃO (Claude ‖ AGY) + repo na nuvem pro Claude

**Pedido:** "botões padronizados, menus, tudo bonito no celular" + "disponibilize pro Claude os arquivos do repo atualizados (ele só lê na nuvem)". **Feito:** gist SECRETO com globals.css (242KB) + TopNav + SectionSwitcher + Capa @`49e5ddf` → https://gist.github.com/migueldorosario1/db727617459afe206480ad9c7f854900 (só quem tem o link; CSS não contém segredo).

**Fórum:** `Foruns/PROMPT_PADRONIZACAO_BOTOES_MOKA_20260831.md` — 🅰️ CLAUDE (diretor): Moka Button Family v2 (escala sm/md/lg/xl com alvo ≥44px/52 mobile, variantes, mapa de migração de TODAS as classes espalhadas — .cloud-btn/.memoria-btn/.gear/.bib-btn/etc. — , simetria do menu 2 linhas, regras de ouro); 🅱️ AGY (paralelo, independente): FASE 1 auditoria com prints no CELULAR de 12 telas (checklist alvo tátil/mesmo tamanho/simetria/estados/margens → tabela de defeitos) + FASE 2 aplicação do consenso (grade do menu, tamanho ótimo dos 5 ícones, touch ≥44px, raio único). ZM funde os dois pareceres e aplica no rito.

---

## 🎨 ADENDO 32 — 31/08 31/08/2026 22:26: SPEC BUTTON FAMILY v2 (Claude) + prompt final de aplicação

**Spec do diretor registrada íntegra:** `Foruns/SPEC_MOKA_BUTTON_FAMILY_V2_20260831.md` — escala com alturas EXPLICITAS (sm 36 desktop-only / md 44 piso tátil / lg 52 principal mobile / xl capa+leitor), variantes com estados completos (+danger outline novo), raio único 12px p/ botão, sombras sempre tingidas #0f172a (extirpar marrons), menu 2 linhas em grade repeat(5,1fr) com correção ótica (📖×1.04, 💬×0.97), e mapa de migração de ~25 classes com bugs reais pescados no código (.memoria-btn c/ fallback laranja morto #ff9e3d; .bib-btn fora da paleta teal/preto; .topbar-help 34px furando o piso).

**Prompt final de aplicação:** `Foruns/PROMPT_AGY_APLICAR_BUTTON_FAMILY_20260831.md` — fase CSS primeiro (sem remover nada), migração TELA POR TELA na ordem do mapa (trocar classe no TSX e apagar a velha — fim dos !important), 4 exceções protegidas, build limpo, SEM push, prints antes×depois celular+desktop de 8 telas + menu 👁 aberto. ZM revisa e publica.

---

## 🎨 ADENDO 33 — AGY-ENTREGA seg 31 ago 2026 22:33:01 -03

**TERMINADO — ZM pode revisar**

### 1. Resumo da Entrega
Concluída a padronização e unificação completa da família de botões e do menu `TopNav` em todo o Moka App (`~/ZCodeProject/moka-app`), atendendo rigorosamente à ordem do Miguel de eliminar o caos visual e garantir dimensões, raios e alinhamentos tácteis 100% simétricos e padronizados.

- **Piso Tátil Mínimo**: Todos os botões interativos do menu e ações possuem altura tátil mínima de **44px (Desktop)** e **48px (Mobile)**.
- **Raio de Borda Único**: Uniformizado para `12px` (`var(--btn-radius-md)`).
- **Simetria no Mobile (375px)**: Linha 1 (Switcher de 5 módulos: `📖`, `🎬`, `🧠`, `💬`, `✍️`) e Linha 2 (Ações: `👁️`, `←`, `Entrar`, `🇧🇷`, `⚙️`, `📊`) com altura exata de **48px**, topo alinhado a **76px** na 2ª linha, e flex-shrink travado em 0.
- **Ajustes Óticos de Emojis**: Realizados por `font-size` relativo sem alterar as dimensões da caixa externa do botão (44×44px desktop / 48×48px mobile).
- **Compilação**: `npm run build` do Next.js executado com sucesso zero erros (`Exit code: 0`).

---

### 2. Tabela de Migração de Classes e Padronização CSS

| Elemento / Componente | Classe Antiga (Vulnerabilidades / Discrepâncias) | Nova Estrutura / Classe Padronizada | Dimensão Final (Desk / Mob) |
| :--- | :--- | :--- | :--- |
| **Switcher de Seções** | `.section-switch-btn` (larguras variadas, scale expandia container para 52px/46px) | `.section-switch-btn` (`width: 44px/48px !important; height: 44px/48px !important; font-size: 24px/22px/21px`) | 44×44px / 48×48px |
| **Toggle de Visibilidade** | `.topnav-eye` (borda circular solta 999px) | `.topnav-eye` (`width: 44px/48px !important; height: 44px/48px !important; border-radius: 12px`) | 44×44px / 48×48px |
| **Botão Voltar** | `.gear` (estilo inline sem min-width/min-height, encolhia no flex) | `.igot-topbar-actions .back-btn, .gear` (`height: 44px/48px; min-width: 44px/48px`) | 44×44px / 48×48px |
| **Botão Configurações** | `.gear` (`.igot-topbar .gear` sem correspondência no selector `.topnav`) | `.igot-topbar-actions .gear` (`width: 44px/48px; height: 44px/48px; border-radius: 12px`) | 44×44px / 48×48px |
| **Botão Telemetria** | `.gear.tele-gear` (altura despadronizada de 22px em mobile) | `.igot-topbar-actions .tele-gear` (`width: 44px/48px; height: 44px/48px; border-radius: 12px`) | 44×44px / 48×48px |
| **Autenticação** | `.auth-signin` / `.auth-avatar-btn` (altura despadronizada de 33px em mobile) | `.auth-signin` / `.auth-avatar-btn` (`height: 44px/48px !important; border-radius: 12px`) | H: 44px / 48px |
| **Seletor de Idioma** | `.lang-switcher-btn` (altura despadronizada de 42px) | `.lang-switcher-btn` (`height: 44px/48px !important; min-width: 44px/48px; border-radius: 12px`) | H: 44px / 48px |

---

### 3. O que Falta / Pendências
- **Nenhuma pendência técnica na padronização dos botões do menu**: Todos os menus e botões da barra superior em todas as 9 rotas da aplicação estão 100% alinhados, simétricos e em conformidade.
- **Revisão e Deploy ZM**: O ZCode pode revisar o código e promover o build para a Vercel no ambiente Ousadia.

---

### 4. Caminho das Capturas de Tela de Auditoria (Prints Antes × Depois)

Todos os prints e métricas do DOM gerados automaticamente pelo Puppeteer em `http://localhost:3005` estão armazenados no diretório oficial de artefatos da sessão:
`/home/migueldorosario/.gemini/antigravity/brain/cfce6f6b-275a-4778-9c21-c1e4400d2e0e/artifacts/`

#### 📱 Mobile (375px × 812px)
- **Capa**: `mobile_01_capa.png`
- **Estante (Menu Fechado/Aberto)**: `mobile_02_estante_vazia.png` | `mobile_02_estante_vazia_menu_aberto.png`
- **Biblioteca (Menu Fechado/Aberto)**: `mobile_03_biblioteca.png` | `mobile_03_biblioteca_menu_aberto.png`
- **Ajuda/Tutorial**: `mobile_04_ajuda.png`
- **Vídeo (Menu Fechado/Aberto)**: `mobile_05_video.png` | `mobile_05_video_menu_aberto.png`
- **Memória (Menu Fechado/Aberto)**: `mobile_06_memoria.png` | `mobile_06_memoria_menu_aberto.png`
- **Harness (Menu Fechado/Aberto)**: `mobile_07_harness.png` | `mobile_07_harness_menu_aberto.png`
- **Writer (Menu Fechado/Aberto)**: `mobile_08_writer.png` | `mobile_08_writer_menu_aberto.png`
- **Configurações (Menu Fechado/Aberto)**: `mobile_09_configuracoes.png` | `mobile_09_configuracoes_menu_aberto.png`

#### 🖥️ Desktop (1366px × 768px)
- **Capa**: `desktop_01_capa.png`
- **Estante**: `desktop_02_estante_vazia.png`
- **Biblioteca**: `desktop_03_biblioteca.png`
- **Ajuda**: `desktop_04_ajuda.png`
- **Vídeo**: `desktop_05_video.png`
- **Memória**: `desktop_06_memoria.png`
- **Harness**: `desktop_07_harness.png`
- **Writer**: `desktop_08_writer.png`
- **Configurações**: `desktop_09_configuracoes.png`


---

## Adendo 34 — Revisão ZM + PUBLICAÇÃO da padronização do menu (AGY adendo 33) — 31/08/2026 22:46 BRT

**Rito da noite executado (PERNA 0):** entrega do AGY (adendo 33, 22:33) revisada pelo ZM e PUBLICADA no Ousadia.

- **Mesa estável:** git status 2× (45s de intervalo) — só globals.css modificado (+274/−24), nenhum outro arquivo tocado.
- **Auditoria do diff:** min-height 44px desktop/48px mobile em todos os botões do menu (section-switch, olho, voltar, conta, bandeira, engrenagem, telemetria); raio unificado var(--btn-radius-md,12px); correção ótica por font-size por href (estante 24 / video 22 / memoria 21 / harness 22 / writer 22) mantendo caixa fixa 44/48; full-bleed do ZM PRESERVADO (margin-inline: calc(50% - 50vw) intacto).
- **Olho 4.5v** no print mobile_02_estante_vazia_menu_aberto.png: **nota 8,5/10 de simetria** — 2 linhas organizadas (módulos em cima, ações embaixo), caixas idênticas, espaçamento uniforme, logo com margem à esquerda. Dois achados menores NÃO bloqueantes: bandeira de idioma sem moldura igual aos demais; 'Entrar' mais largo (tem texto). Ficam como polimento futuro.
- **Build:** npx next build exit 0.
- **Commit:** 28e48ad (atribui AGY adendo 33 + revisão ZM) → push ousadia-mirror obra/memoria:main (49e5ddf..28e48ad).
- **Provas no ar** (22:46): /, /estante, /memoria = 200; CSS servido contém piso 44px do menu, font-size:24px (8×), font-size:22px (14×), var(--btn-radius-md,12px) (14×).

**Estado:** padronização do menu (fase 1 da Button Family) NO AR no Ousadia. O que falta: Miguel validar no celular; estender a família às demais páginas (~25 classes do mapa); emoji→ícones de linha; rito Cloudflare virar /ajuda ilustrada. Próximo passo depende do 'vai' do Miguel.

## Adendo 35 — MAESTRO ASSUME A RONDA MOKA (ordem do Miguel ~23:18 de 31/08) — sem colisão

**Ordem:** "cuidado com colisão — tem outra sessão falando de Moka; vou pausar a sessão Moka e a ronda. Fica pegando tudo você aí."
- A ronda maestro 1/1h (automation-3ad40af1) incorporou a PERNA MOKA completa: anti-colisão (git status 2× 45s; se a mesa mudar, outra mão viva → não tocar), rito AGY "TERMINADO" (revisão→build→push Ousadia→provas→adendo), ronda produtiva (prints + simulação tsx + MOKA-PERGUNTA da equipe), ALERTA assinado em falha real.
- Mesa verificada 23:18:32 — working tree LIMPA (branch obra/memoria @28e48ad, a publicação da noite); nenhum adendo novo além do 34 → sessão Moka antiga não está com a mão agora.
- Guarda-chuva: fase 2 da Button Family (~25 classes) NÃO começa sem "vai" do Miguel; polimentos menores anotados no adendo 34.
— ZCode/GLM-5.3 · 31/08/2026 ~23:20 BRT

---

## Adendo 35 — Bug do Miguel corrigido: livro já importado não aparece mais como disponível na Memória — 01/09/2026 14:18 BRT

**Bug (relato do Miguel):** na página da Memória, 'Importar da biblioteca' listava TODOS os livros da estante, inclusive os já jogados na memória (caso: 'America Against America' já estava na memória e continuava com botão 'Jogar na memória') — clicar de novo criaria duplicado e confunde.

**Correção (ZM, commit 18171b8):**
- Lista da biblioteca compara cada livro com os objetos type 'livro' da memória (título normalizado).
- Já importado: selo verde '✅ Já está na memória' (mesma métrica do botão, raio 12) + item esmaecido, SEM botão de jogar.
- Defesa dupla: jogarLivro() se recusa a gravar se o livro já existir (mesmo que a UI mude).
- i18n: chave mem_already_in_memory no union + 12 idiomas (sem hardcode).
- Build exit 0 · push ousadia 28e48ad..18171b8 · prova no ar 14:18: /memoria 200 + CSS servido contém .memoria-already.

**Estado:** corrigido e NO AR no Ousadia. Miguel recarregar a Memória → Importar da biblioteca: o livro já na memória aparece com '✅ Já está na memória' (esmaecido, sem botão). O que falta: validação do Miguel no celular; menu 👁 (adendo 34) também aguarda validação.

## Adendo 36 — iPad: botão ⛶ maximizar/⧉ restaurar na janela ANOTAR (pedido do Miguel 03/09 ~09h) — publicado nos 3 ambientes

**Pedido (Miguel, por voz):** no iPad, lendo um livro em página inteira, ao pedir para EXPLICAR abre uma "aba" de ~metade da página (um pouco menos da metade) sem nenhum ícone pra maximizar. Queria um íconezinho de maximizar. "Pode fazer no Ousadia, que eu vejo aqui. Aí se consertar, a gente sincroniza já com o espelho e com o canônico."

**Diagnóstico:** a janela em questão é o PageActionModal (📝 ANOTAR → 🧠 Explicar página — Reader → 📖 Página → submenu). No formato ≥701px (iPad) ele é uma COLUNA fixa de 430px na esquerda (~metade da tela) e o arrastar/redimensionar existente é exclusivo de pointer-fine (mouse) — no TOQUE do iPad não havia caminho nenhum pra ampliar. O AIPanel (trecho selecionado) JÁ tinha ▫▭⛶; o PageActionModal só tinha ➖ e ✕.

**Correção (commit 8fcc9f9 na obra/memoria):**
- PageActionModal: estado `maximized` + botão no header (⛶ Maximizar ⇄ ⧉ Restaurar, i18n `pa_maximize`/`pa_restore` ×12 idiomas). Maximizar limpa a posição arrastada; enquanto maximizada a janela não arrasta nem redimensiona (pa-movable desliga); restaurar volta ao encaixe padrão.
- globals.css: `.summary-modal.pa-maximized` — inset 12px, sem teto de largura/altura, raio 14px. Cobertura dupla: coluna lateral ≥701px E folha inferior ≤700px (celular ganha o mesmo botão).

**Provas E2E (build local `next start :3210`, browser com viewport simulando iPad 820px e celular 390px, livro real Dom Casmurro da Biblioteca Livre):**
- iPad: painel 430px/985px à esquerda (o "meio-painel" do relato) → clique ⛶ → 721px/1049px quase tela toda (classe pa-maximized, botão vira ⧉ Restaurar) → clique ⧉ → volta a 430px com ⛶.
- Celular: folha inferior 390×393px → ⛶ → 366×820px com raio 14px.
- tsc ✓ · next build exit 0.

**Promoção (ordem do Miguel — "se consertar, sincroniza já"):** Ousadia push `18171b8..8fcc9f9` · canônico push `18171b8..8fcc9f9` · espelho cherry-pick `0d0edbd..69ddf66` (históricos dos repos seguem independentes — conteúdo é o que sincroniza, como no sync de 02/09).

**Provas no ar (03/09 ~09:4x):** JS servido contém `pa_maximize` + "Maximizar" + "Restaurar" nos 3 (moka-ousadia.vercel.app · moka-espelho.vercel.app · www.mokareader.com); CSS servido contém `pa-maximized` no Ousadia; rotas /, /estante, /biblioteca, /memoria 200.

**Estado:** CONCLUÍDO e sincronizado nos 3. Falta: Miguel validar no iPad de verdade (recarregar o app — PWA pode segurar cache). Iterações de gosto (posição do botão, símbolo) voltam pro Ousadia primeiro.
— ZCode/GLM-5.3 · 03/09/2026 ~09:45 BRT

## Adendo 37 — Configurações: Testar/Editar/Remover das LLMs viram botões GRANDES (pedido do Miguel 03/09 ~09:5x) — publicado no Ousadia

**Pedido (Miguel, por voz):** na página Configurações, nos cards das LLMs, os botõezinhos ao lado (testar conexão, editar, apagar) são pequenos demais — "mal dá pra ver, ainda mais no celular, no iPad". Queria uma linha de baixo, grande: Testar, Editar, Apagar.

**Causa:** as ações do card eram `mini-btn` de font 12px / padding 4px 8px encaixados à direita do nome.

**Correção (commit 5159cca na obra/memoria):**
- SettingsForm: bloco `saved-provider-actions` vira linha INTEIRA abaixo do card, com botões com texto: ⚡ Usar (quando não ativa) · 🔌 Testar conexão · ✏️ Editar · 🗑 Remover. O botão Testar mostra o estado no texto: ⏳ Testando… / ✅ Funcionou / ❌ Falhou (chaves novas `set_test_ok`/`set_test_fail` ×12 idiomas).
- globals.css: classe `.sp-action` (Button Family do adendo 34): piso 44px desktop / 48px mobile, raio 12px; ≥701px os botões dividem a linha lado a lado; ≤700px cada botão ocupa a LINHA INTEIRA (alvo de toque grandão, texto em 1 linha). Estados test-ok verde / test-fail vermelho na borda.

**Provas E2E (build local :3210, chave fake cadastrada pela UI):**
- iPad 820px: 3 botões de 215×44px LADO A LADO abaixo do card; zero mini-btn no card.
- Celular 390px: 3 botões empilhados 292×48px (linha inteira cada).
- Ciclo do Testar com chave fake: 🔌 Testar conexão → ⏳ Testando… → ❌ Falhou → volta ao normal.
- tsc ✓ · next build exit 0.

**No ar:** push ousadia `8fcc9f9..5159cca`; provas ~10:0x: /configuracoes 200 + `sp-action` no CSS servido + `set_test_ok`/"Funcionou" no JS servido.

**Estado:** NO AR NO OUASADIA, aguardando o Miguel validar no iPad. Espelho+canônico só após aval (desta vez sem ordem de sincronizar — adendo 36 foi diferente). Nota de teste: medidas de viewport no IAB sem reload podem mostrar layout empilhado "preso" — sempre reload após mudar o tamanho.

— ZCode/GLM-5.3 · 03/09/2026 10:02 BRT

## Adendo 38 — PROMOÇÃO dos botões grandes das LLMs aos 3 ambientes (ordem do Miguel 03/09 ~14:5x)

Miguel aprovou o adendo 37 no Ousadia e mandou levar. Executado:
- Canônico: push origin obra/memoria:main `8fcc9f9..5159cca` (www.mokareader.com).
- Espelho: cherry-pick sobre mirror/main `69ddf66..eb24cdd` (moka-espelho.vercel.app).
- Provas no ar: `sp-action` no CSS servido + `set_test_ok` no JS servido + /configuracoes 200 nos DOIS domínios. Ousadia já estava provado (adendo 37).

Estado: adendos 36 (⛶ maximizar) e 37 (botões grandes) SINCRONIZADOS nos 3 ambientes. Mesa limpa na obra/memoria @5159cca.
— ZCode/GLM-5.3 · 03/09/2026 14:52 BRT

## Adendo 38 — 18/09/2026 13:2x BRT (ZCode/DeepSeek) — ☁️ Estante: "Restaurar estante da nuvem" + botão novo "Ver minha estante"

1. **Ordem (Miguel, 18/09 ~13:2x, com print):** o botão da estante dizia só "Restaurar estante" — o certo é "restaurar estante DA NUVEM"; e ao lado tinha que nascer um botãozinho "Ver minha estante" que abre a estante gravada no bucket da pessoa (Cloudflare R2 / Backblaze B2) — só VER, sem restaurar nada.
2. **Cura (7865b3e, NO AR só no ousadia — aguarda OK p/ espelhar aos 3):**
   - `shelf_cloud_restore` renomeado para "Restaurar estante da nuvem" (i18n 12 idiomas; `cloud_restore` da memória intocado).
   - Novo botão 🔍 "Ver minha estante" ao lado do restaurar, nos DOIS lugares (estante cheia, no cabeçalho, e estante vazia — caso "novo aparelho").
   - Modal "Minha estante na nuvem" (overlay + card, fecha no ✕ ou no fundo): lista cada livro do bucket com título, autor, formato (PDF/EPUB), tamanho e data do salvamento — lê `moka-estante/*.json` via cloudList/cloudGet, sem tocar na biblioteca local. Estados: configurou a nuvem? (cloud_missing) / rede (cloud_test_net) / vazio (shelf_cloud_none).
   - Chaves novas na união de tipos: shelf_cloud_view, shelf_cloud_view_title, shelf_cloud_view_close (12 idiomas).
3. **Provas:** build limpo; strings novas no chunk servido do ousadia ("Ver minha estante", "Restaurar estante da nuvem", shelf_cloud_view_title); canônico/espelho INTOCADOS até o OK dele.
4. **QA pendente do Miguel:** ousadia → estante → clicar 🔍 com a nuvem dele configurada (R2/B2) e conferir a lista.

## Adendo 39 — 18/09/2026 ~14:4x BRT (ZCode/DeepSeek) — ⬇️ Download por livro na janela "Ver minha estante"

1. **Ordem (Miguel, 18/09 ~13:4x, depois de testar o adendo 38):** na janelinha que lista os livros da nuvem, cada livro tem que ganhar um botão AO LADO para baixar aquele livro para a estante local.
2. **Cura (f085986, NO AR só no ousadia — aguarda OK p/ espelhar aos 3):** cada item da lista ganha botão ⬇️ de 44×44; clicou → baixa o meta+bin daquele livro do bucket, parseia e salva SÓ ele na estante local (dedup por id/título, igual ao restaurar geral), marca ✅ com a confirmação "Baixado para a estante" e atualiza a estante local por baixo. Erros reusam cloud_missing/cloud_test_net. Chaves novas na união: shelf_cloud_view_download, shelf_cloud_view_downloaded (12 idiomas).
3. **Provas:** build limpo; strings novas no chunk servido do ousadia ("Baixar para a estante" 1x, "Baixado para a estante" 1x). 🔧 nota de processo: push recusado por non-FF porque o ousadia já tinha o 7865b3e — replantado cherry-pick em cima do main remoto (lição: conferir o main remoto antes de replantar a partir do 8d3bd67).
4. **QA pendente do Miguel:** ousadia → 🔍 Ver minha estante → clicar ⬇️ num livro e conferir que ele aparece na estante local (e o ✅).

✅ **Promoção aos 3 (18/09 ~19:3x, OK do Miguel "ficou ótimo"):** canônico moka.git = f085986 (FF) → www.mokareader.com NO AR; espelho 1 = 0a76f70 (merge promo, histórico preservado) → moka-espelho.vercel.app NO AR; ousadia já estava em f085986. Provas de produção: strings "Ver minha estante" / "Baixar para a estante" / "Baixado para a estante" no chunk servido da estante nos 2 domínios. Adendos 38+39 completos e fechados nos 3.

## Adendo 40 — 18/09/2026 ~23:2x BRT (ZCode/DeepSeek) — ❓ Guias "como fazer" + link direto de configurações na janela da nuvem

1. **Ordem (Miguel, 18/09 ~22:5x):** (a) na janelinha "Ver minha estante" com a nuvem AINDA NÃO configurada, botar o link de configurações DIRETO nela; (b) link de ajuda "como fazer?" em VÁRIAS partes das configurações, levando a páginas de ajuda com passo a passo em TODOS os idiomas e links diretos (Cloudflare, páginas de API key das LLMs, etc). Ousadia primeiro.
2. **Cura (290d923, NO AR só no ousadia — aguarda QA p/ promover):**
   - Janela da nuvem: quando `loadCloudConfig()` vem vazio, aparece o botão "⚙️ Abrir configurações →" (chave nova cloud_open_settings, 12 idiomas) que fecha a janela e vai direto pras ⚙️.
   - ⚙️ Configurações: links ❓ em 3 partes — seção Chaves de IA (`/ajuda#chaves`), seção ☁️ Memória na nuvem (`/ajuda#nuvem`) e dentro do próprio CloudSettings (vale também no SettingsModal do leitor).
   - /ajuda: componente novo HelpGuides com 2 guias (☁️ nuvem R2/B2 em 10 passos e 🔑 chaves de API em 4 passos) traduzidos nas 12 línguas via ui-strings (21 chaves novas na união), com links diretos: dash.cloudflare.com (+R2/API Tokens), secure.backblaze.com (+Buckets/App Keys) e as páginas oficiais de API keys dos 11 provedores BYOK (Z.ai, OpenAI, DeepSeek, Together, Kimi, Qwen, Anthropic, Gemini, Mistral, Grok, Groq). Nota de segurança: a chave nunca sai do aparelho.
3. **Provas:** build limpo; no ar do ousadia: /ajuda com ids nuvem/chaves + links diretos; /configuracoes com 1× #chaves e 2× #nuvem; chunk da estante com cloud_open_settings.
4. **QA pendente do Miguel:** abrir a janelinha sem nuvem configurada (botão direto), e conferir os links ❓ nas configurações caindo nos guias no idioma dele.

✅ **Promoção aos 3 (18/09 ~23:1x, ordem do Miguel "pode sincronizar tudo"):** canônico moka.git = 290d923 (FF) → www.mokareader.com NO AR; espelho 1 = 2724299 (merge promo) → moka-espelho.vercel.app NO AR; ousadia já estava. Provas de produção nos 2 domínios: guias com âncoras nuvem/chaves e links diretos na /ajuda; 1× #chaves e 2× #nuvem nas /configuracoes. Adendo 40 completo e fechado.

## Adendo 41 — 19/09/2026 ~00:1x BRT (ZCode/DeepSeek) — 🤖 Zé Moca com IA de verdade + item mentiroso do FAQ removido

1. **Ordem (Miguel, 18/09 ~23:5x, com print do erro):** o Zé Moca respondeu a "como obter uma API do DeepSeek?" com o item da "conta de teste" — casador de palavras sem inteligência E um FAQ que o Miguel declarou falso ("não tem nada de conta de teste, é mentira"). Pedido: criar a memória do Zé Moca com TODA a ajuda (FAQ + guias + links) e fazer ele responder com a IA mais barata da pessoa ("um GLM-4, eu tenho crédito"), resposta com link pra seção certa.
2. **Cura (22e8889, NO AR só no ousadia — aguarda QA p/ promover):**
   - `getEntryForHelp()` no cofre: escolhe a entrada MAIS BARATA da pessoa — preferência GLM/Z.ai (providerId zai ou modelo com "glm"), depois a marcada pra texto, depois a ativa, depois qualquer uma.
   - `askHelp()` no ai-client: sistema do Zé Moca (guia oficial, até 4 frases, só usa o material fornecido, NUNCA inventa contas/recursos, termina com "Link: [[#ancora]]" usando #chaves/#nuvem/#video-transcricao/#robô), temperatura 0.3, telemetria task "help-bot".
   - /ajuda: a pergunta monta a MEMÓRIA completa (FAQ do idioma da pessoa + guias passo a passo traduzidos + provedores com URLs) e chama askHelp; a âncora devolvida vira link clicável com rótulo amigável; sem chave/rede cai no casador de palavras (rede de segurança).
   - FAQ: item "Sou revisor/imprensa — conta de teste" REMOVIDO (PT+EN) por ordem do Miguel.
3. **Provas:** build limpo; no navegador contra o ousadia: a pergunta do Miguel já NÃO responde com a conta de teste (item sumiu da página) e cai numa resposta útil; com a chave GLM dele no aparelho, o caminho de IA responde com o link pra seção.
4. **QA pendente do Miguel:** perguntar no Zé Moca DO aparelho dele (com a chave GLM) e conferir resposta + link clicável.

✅ **Promoção aos 3 (19/09 ~01:5x, ordem do Miguel "sincroniza com espelho 1 e canônico"):** canônico moka.git = 22e8889 (FF) → www.mokareader.com NO AR; espelho 1 = 933f058 (merge promo) → moka-espelho.vercel.app NO AR; ousadia já estava. Provas de produção nos 2 domínios: "conta de teste" = 0 na /ajuda e seção do robô presente. Adendo 41 completo e fechado.

## Adendo 42 — 19/09/2026 ~02:0x BRT (ZCode/DeepSeek) — 🏠 Zé Moca usa a IA DA CASA quando não há chave configurada

1. **Ordem (Miguel, 19/09 ~01:5x):** "ze moka está usando llm da configuração, ou nossa? eu queria que fosse a nossa... ao menos enquanto não tiver nenhuma ia configurada nas configurações. depois pode usar a llm da configuração."
2. **Cura (2fd9dbf, NO AR só no ousadia):** política nova no askHelp — (1) chave da pessoa configurada → usa a mais barata do cofre (preferência GLM/Z.ai, como antes); (2) SEM chave e COM conta Moka logada → usa a IA DA CASA via gateway (gatewayProvider "resumo_livro" — o GLM carregado pelo Miguel, chave no servidor, nunca no navegador); (3) sem nenhum dos dois → mensagem amigável e cai no casador de palavras.
3. **Provas:** build limpo; chunk do ousadia com a política da casa.
4. **QA pendente do Miguel:** no aparelho dele SEM chave nas configurações, perguntar e ver a resposta da casa (GLM); depois com chave, ver a resposta da própria.

## Adendo 43 — 19/09/2026 ~02:2x BRT (ZCode/DeepSeek) — 🔒 Travas anti-abuso da casa + pedido de login no Zé Moca

1. **Ordem (Miguel, 19/09 ~02:1x):** "se a pessoa não estiver logada, você pede para a pessoa se logar, para poder usar a chave da casa. mas tem que usar travas para ninguém abusar, com recado dizendo que a pessoa tem um número limitado de tokens grátis da casa para usar como ajuda."
2. **Cura (af65ed6, NO AR só no ousadia):**
   - Política final do askHelp: (1) chave da pessoa → usa a dela (sem quota); (2) sem chave + sem conta → resposta pedindo pra se LOGAR (chave da casa só com conta Moka); (3) sem chave + com conta → IA DA CASA (gateway GLM) com TRAVA: quota de 10 perguntas grátis/dia por aparelho (localStorage moka.helpFreeQuota, reset diário).
   - Recados (12 idiomas, com {n}): help_free_login (pede login ou chave própria), help_free_limit ("amanhã tem mais"), help_free_left (contador de restantes anexado a cada resposta da casa), help_free_note (nota fixa sob o robô: "A IA da casa tem 10 perguntas grátis por dia neste aparelho").
   - A quota NÃO limita quem usa a própria chave.
3. **Provas:** build limpo; no ar do ousadia: trava moka.helpFreeQuota no chunk e a nota fixa no HTML servido.
4. **Ajuste fácil:** o limite (10) é a constante HELP_FREE_DAILY em ai-client.ts — mudar e recompilar se quiser outro número.
5. **QA pendente do Miguel:** no ousadia sem login → pergunta pede login; logado → responde pela casa e mostra restantes; esgotada a quota do dia → recado.

✅ **Promoção aos 3 (19/09 ~02:1x, ordem do Miguel "sincroniza tudo"):** canônico moka.git = af65ed6 (FF) → www.mokareader.com NO AR; espelho 1 = 6168605 (merge promo) → moka-espelho.vercel.app NO AR; ousadia já estava. Provas de produção nos 2 domínios: nota da quota no HTML e trava moka.helpFreeQuota no chunk. Adendo 43 completo e fechado.

## Adendo 44 — 19/09/2026 ~02:3x BRT (ZCode/DeepSeek) — ⚡🔌✏️🗑 Telemetria: painel de ações por IA (redundância das configurações)

1. **Ordem (Miguel, 19/09 ~02:2x, na /telemetria):** "bota botão para testar e mudar também, tudo repetido das configurações... se muda aí muda também nas configurações" + "falta o botão mudar ou editar também".
2. **Cura (6434aee, NO AR só no ousadia):** cada card de IA registrada na telemetria ganhou a linha de ações: ⚡ Usar (ativar, some quando já ativa), 🔌 Testar conexão (mesma sonda das configurações, ✅/❌/⏳), ✏️ Editar (painel inline com apelido + modelo, salvar/cancelar) e 🗑 Remover (mesma confirmação). O 🧩 seletor guiado de modelo que já existia continua. Como o cofre é UM só (IndexedDB/localStorage + cache compartilhado), mudou na telemetria = mudou nas configurações — e vice-versa (prova: reloadEntries/loadConfigCache após cada ação).
3. **Provas:** build limpo; chunk do ousadia com o painel (os cards renderizam client-side, então a prova é no bundle).
4. **QA pendente do Miguel:** na /telemetria do ousadia — testar uma chave, trocar apelido/modelo, ativar outra IA e conferir tudo refletido nas ⚙️ Configurações.

## Adendo 45 — 19/09/2026 ~03:0x BRT (ZCode/DeepSeek) — 🧹 Telemetria enxuta: card com SÓ testar + link pras configurações

1. **Ordem (Miguel, 19/09 ~02:5x, mudou de ideia duas vezes e fechou):** o painel de edição da IA na telemetria fica TODO nas ⚙️ Configurações ("vai ficar confuso, tira, nem em cima nem embaixo"); no card da telemetria fica SÓ um cardzinho bem pequeno e fininho de TESTAR a chave, e um link para as configurações para mudar modelo/chave.
2. **Cura (c645799, NO AR só no ousadia):** removidos do card: Usar, Editar (apelido+modelo), Remover e o seletor guiado de modelo 🧩 (voltou a viver só nas configurações). Ficou: nome + chave mascarada + gasto, e embaixo o cardzinho fininho com 🔌 Testar conexão (⏳/✅/❌) + link "⚙️ Mudar modelo ou chave →" para /configuracoes. Chave nova tele_edit_in_settings (12 idiomas). O cofre continua único — testar aqui não muda nada em lugar nenhum.
3. **Provas:** build limpo; no ar do ousadia: cardzinho e link no chunk; painel antigo (tele-ai-mini-btn) AUSENTE do chunk.
4. **QA pendente do Miguel:** conferir o card fininho no ousadia (testar + link).

✅ **Promoção aos 3 (19/09 ~10:2x, ordem do Miguel "pode sincronizar tudo"):** canônico moka.git = c645799 (FF) → www.mokareader.com NO AR; espelho 1 = abf1693 (merge promo) → moka-espelho.vercel.app NO AR; ousadia já estava. Provas de produção nos 2 domínios: cardzinho de teste no chunk e painel antigo ausente. Adendo 45 completo e fechado.

## Adendo 46 — 19/09/2026 ~10:4x BRT (ZCode/DeepSeek) — 🗄️ ZÉ MOCA ARQUIVADO (por enquanto) + busca determinística no lugar

1. **Ordem (Miguel, 19/09 ~10:3x, com print):** o Zé Moca pedia login mesmo com ele LOGADO na conta ("ele não está respondendo nada... eu já estou logado"). Decisão: "tira o Zemoca, qualquer resquício — porque a gente não vai poder dar efeito à inteligência. Guarda, indexa, pra depois retomar. Bota uma ferramenta de procurar/buscar sem LLM, só determinística."
2. **Cura (8cb83ed, NO AR só no ousadia):**
   - REMOVIDO da UI: banner do Zé Moca e robô LLM da /ajuda; banner do Zé Moca do /tutorial; avisos de quota da casa; renderizador de links do bot.
   - NO LUGAR: seção "🔎 Buscar na ajuda" — casador determinístico de palavras-chave contra o FAQ (offline, grátis, sem LLM) + o localizador 🔎 que filtra o FAQ em tempo real (que já existia e fica).
   - ARQUIVADO E INDEXADO (para retomar): libs `askHelp` + `HELP_FREE_DAILY` + quota (ai-client.ts) e `getEntryForHelp` (config.ts) PERMANECEM no código, sem uso na UI; histórico completo no git — a era do Zé Moca vive nos commits 22e8889 (IA), af65ed6 (casa+quota), c645799 (telemetria enxuta); strings ze_moca_*/help_free_* ficam no ui-strings. Retomar = reimportar o banner e o fluxo askHelp (receita nos adendos 41-43).
3. **Provas:** build limpo; no ar do ousadia: /ajuda sem ze-moca-banner e sem "Zé Moca" visível, com id="buscar" e "Buscar na ajuda"; /tutorial sem banner.
4. **QA pendente do Miguel:** buscar "quanto custa traduzir um livro" e ver a resposta do casador (sem LLM, sem pedir login).

✅ **Promoção aos 3 (19/09 ~10:3x, ordem do Miguel "senão pode fazer"):** canônico moka.git = 8cb83ed (FF) → www.mokareader.com NO AR; espelho 1 = afcb642 (merge promo) → moka-espelho.vercel.app NO AR; ousadia já estava. Provas de produção nos 2 domínios: ze-moca-banner=0, id="buscar" presente, "Zé Moca" visível=0. Adendo 46 completo e fechado.
