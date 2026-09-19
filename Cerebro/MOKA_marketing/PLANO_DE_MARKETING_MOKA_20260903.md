# 📣 PLANO DE MARKETING MOKA — 30 DIAS DE AÇÃO DIÁRIA

> **Dono:** ZM (ZCode/GLM-5.3) · **Criado:** 03/09/2026 ~15h BRT (ordem do Miguel)
> **Missão (quase literal):** "todo dia a gente tem que fazer uma ação de marketing do Moka" — com prints explicando o que é cada coisa revolucionária, e-mail, WhatsApp, banners diferentes e um robô para publicar todo dia uma matéria sobre o Moka Reader.
> **Irmãos:** `prints_20260903/` (prints frescos do canônico) · `banners/` (peças prontas) · `PAUTA_30_MATERIAS_ROBO_MOKA.md` (pautas do robô) · `storyboard/` + `audio/` (comercial 30s já produzido) · `Outros/banco de emails/campanha_moka_2026/` (ondas de e-mail).
> **Regra inegociável da casa:** NADA sai para fora (e-mail, WhatsApp, post, publi) sem OK explícito do Miguel. A ronda PREPARA e ENTREGA; o Miguel dispara ou dá o "vai".

---

## 1. O PRODUTO EM UMA FRASE (e suas 6 revolucionices)

**Moka (www.mokareader.com)** — o app que junta seus livros, seus vídeos e sua memória de leitura EM UM SÓ LUGAR, rodando com A SUA PRÓPRIA chave de IA.

As 6 coisas revolucionárias (cada uma vira print, banner, e-mail e matéria):

| # | Revolucionice | Explicação de marketing (linguagem humana) |
|---|---|---|
| 1 | **🔒 BYOK — a IA é sua** | Você cola a sua chave de IA (OpenAI, Anthropic, DeepSeek, Gemini…) e ela fica criptografada NO SEU APARELHO. Nenhuma empresa — nem a Moka — lê seus livros ou cobra mensalidade pra rodar IA. É o contrário de todo app de IA que existe. |
| 2 | **📖 Reader — leitor que entende o livro** | Toque em qualquer palavra: tradução na hora. Livro inteiro em inglês, chinês, alemão? O Moka traduz TUDO, em volumes, com estimativa de custo ANTES e recibo DEPOIS. Resume a página, lê em voz alta, responde perguntas sobre o livro. 12 idiomas. |
| 3 | **🎬 Video — 2 horas de vídeo em 2 minutos** | Cole um link do YouTube/X/Instagram e receba: transcrição na íntegra, resumo de 1 a 10 minutos, quem são os personagens, o contexto político, a crítica — e pergunte o que quiser com timestamp. Quem assiste entrevista, aula, live... economiza horas por semana. |
| 4 | **🧠 Memória — a IA que lembra do que você leu** | Tudo que você lê vira uma memória pesquisável. A IA não recomeça do zero a cada conversa: ela sabe o que você já leu. Duas caixas: 🎒 bagagem (o que você acumulou) e ⚡ operacional (o que está em uso agora). |
| 5 | **💬 Harness — chat com contexto de verdade** | Um chat de IA que conversa COM A SUA MEMÓRIA de leituras. Pergunte "o que aquele livro dizia sobre X?" e ele responde com base no que você realmente leu. |
| 6 | **📊 Suas IAs — ninguém esconde a conta** | Painel de gastos por IA, tarefa e modelo, na sua moeda, com trava de tokens pra nunca estourar. Transparência que nenhum serviço de IA oferece. Preço real de uso: livro inteiro ~R$ 0,38 · vídeo de 2h ~R$ 0,56. |

**Bônus estrutural:** local-first (livros no aparelho, funciona offline), PWA instalável, backup na SUA nuvem (Cloudflare R2 / Backblaze / S3 — com as suas credenciais), grátis para sempre no modo BYOK.

## 2. POSICIONAMENTO E PÚBLICOS

**Posicionamento (uma frase):**
> "Os apps de IA querem os seus dados. O Moka quer devolver eles pra você."

**Públicos (na ordem de ataque):**
1. **Leitor profissional** — lê livros/técnicos em inglês e outras línguas, tem assinatura de IA ou pagaria por uma. Gancho: tradução de livro inteiro por centavos.
2. **Consumidor de vídeo longo** — jornalistas, pesquisadores, estudantes, ativistas políticos que assistem entrevistas/lives/documentários. Gancho: 2h → resumo em minutos.
3. **Comunidade IA/dev** — já tem chave de API, odeia assinatura. Gancho: BYOK + local-first + telemetria honesta. É o público que espalha (Product Hunt, Hacker News, Reddit r/LocalLLaMA, X).
4. **Curioso de produtividade** — público das ondas 3-4 de e-mail. Gancho: "sua segunda memória".

**A promessa econômica (contra a concorrência):** assinatura de IA custa R$ 20-140/mês TODO mês. No Moka, usar a própria chave custa centavos por livro/vídeo. Quem lê 2 livros/mês paga ~R$ 0,76. É ordem de grandeza, não promoção.

## 3. CANAIS E PEÇAS

| Canal | Estado | Peça |
|---|---|---|
| **E-mail** | Lista pronta: 4 ondas (`campanha_moka_2026/`: ouro 200 · quente 500 · morna 600 · fria resto · supressão LGPD) | 3 minutas prontas (§5) — 1ª onda OURO sai só com "vai" |
| **WhatsApp** | Contatos do Miguel | 3 mensagens prontas (§5) — pessoais, uma por semana |
| **Banners** | Gerar 3 famílias (§6): Reader · Video · Memória | Web 1200×628 · Story 1080×1920 · Post 1080×1080 |
| **Robô de matérias** | Pauta de 30 matérias pronta (`PAUTA_30_MATERIAS_ROBO_MOKA.md`) | 1 matéria/dia no Cafezinho (rascunho + gate editorial; publi transparente) |
| **Comercial 30s** | JÁ PRODUZIDO: storyboard 4 cenas + locução PT/EN (`storyboard/` + `audio/`) | Falta animar no Veo e aplicar overlays — projeto de 1 sessão |
| **Play Store** | Appeal pendente (fórum da saga) | Lembrete diário existente (pausado) — reativar quando o Miguel quiser |
| **Product Hunt / Hacker News** | Futuro (semana 3+) | Lançar depois das 2 primeiras ondas de e-mail + 10 matérias |

## 4. CALENDÁRIO — 30 DIAS, UMA AÇÃO POR DIA

> A RONDA DIÁRIA 09:30 (automação `Ronda Marketing Moka`) lê esta tabela, executa o dia e entrega o material pronto. Dia concluído = marcar `[x]` aqui no plano. Se o dia atrasar (Miguel não deu "vai"), a ronda empurra a pauta pra frente e avisa — nunca pula silenciosamente.

| Semana | Dias | Tema | Ações diárias |
|---|---|---|---|
| **1 — Fundação** | 1-7 | Arsenal + aprovação | D1: Miguel aprova plano+prints+minutas · D2: aprova banners · D3: ajustes finos + enviar appeal Play Store · D4: disparo onda OURO (200 e-mails) · D5: disparo WhatsApp quente · D6: 1ª matéria robô no ar · D7: primeira leitura de métricas (aberturas/cadastros) |
| **2 — Cadência** | 8-14 | 1 ação/dia no automático | Seg: matéria robô · Ter: print educativo (Instagram/WhatsApp status) · Qua: matéria robô · Qui: disparo onda QUENTE (500) · Sex: matéria robô + resumo da semana pro Miguel · Sáb: peça leve (citação de livro + frase do Moka) · Dom: prep da semana + métricas |
| **3 — Alcance** | 15-21 | Expandir | Seg: matéria · Ter: print educativo · Qua: matéria · Qui: onda MORNA (600) · Sex: matéria + métricas · Sáb: bastidores da obra (como o app é feito por IA) · Dom: prep + revisão do que funcionou |
| **4 — Conversão** | 22-30 | Fechar | Seg: matéria · Ter: print · Qua: matéria · Qui: onda FRIA (resto) · Sex: matéria + métricas do mês · Sáb: comercial 30s no ar (se Veo pronto) · D29: retrospectiva 30 dias · D30: plano do mês 2 com dados reais |

**Progresso (registro da ronda diária):** 05/09 sáb (ronda 1): D1-D3 aguardam o Miguel (vais: onda OURO + matéria); D6 ADIANTADO — 1ª matéria criada como rascunho WP 269116 + pedido de gate ZM-20260905-007 na ponte (capa pela caça da casa). Play Store segue com o Astra (AST-20260905-016), saiu da fila desta ronda. · 06/09 dom (ronda 2): D4 (disparo OURO) e D5 (WhatsApp) BLOQUEADOS por "vai" pendente — pauta empurrada, não pulada; domingo de métricas/prep EXECUTADO: contas no gateway = 7 total, 0 novas em 7d, última em 01/08 (fonte: sqlite moka_pontos.db, Tencent, lido 06/09 ~09:41 BRT); visitas = MÉTRICA INDISPONÍVEL (GA4 G-43CSQVKW6N sem credencial de API no cofre; leitor Umami da casa cobre só ocafezinho.com — pendência nova: cadastrar mokareader.com no Umami ou credenciar GA4). · 08/09 ter (ronda EXTRAORDINÁRIA ~15:5x, ordem do Miguel ~14:0x "faz um extraordinário hoje às 17h"): slot TER da Semana 2 EXECUTADO — print educativo (cel_390x844_video.png) + legenda em dias/2026-09-08_legenda.md (quem posta é o Miguel); ANÁLISE DOS E-MAILS pronta (ANALISE_EMAILS_MOKA_20260908.md): 1.810 endereços únicos (ouro 200/quente 500/morna 599/fria 511), 0 duplicatas, 0 colisões com supressão LGPD; REGRAS NOVAS PERMANENTES (ordem 08/09): 🔴 agente NUNCA mexe no WhatsApp (Miguel envia) + e-mail autorizado = SEMPRE BCC em lotes; Telegram de entrega agendado 17:00; ronda diária normal retoma 09/09 09:30. D4/D5 seguem aguardando "vai". · 09/09 qua (ronda dia 7/30): matéria de qua ENTREGUE — rascunho WP #269574 (pauta 2, módulo vídeo: entrevista de 2h em 2min; gate ZM-20260909-006 na ponte, capa na caça da casa); Telegram do dia enviado 09:3x; teste de e-mail unitário (pedido do Miguel) PRONTO e BLOQUEADO na senha inválida da caixa info@ (Adendo 7 — reset GoDaddy pendente do Miguel); D4/D5 seguem nos "vais". · 10/09 qui (ronda dia 8/30): 🚀 lote 1 OURO DISPARADO 09/09 13:04 (50+Miguel Bcc, Gmail dele, OK Google); minuta v2.1 APROVADA 11:5x; remetente OURO=Gmail pessoal (ordem ~11:1x); robô SAIR no ar */30; medo CCO dissipado c/ prova real (cópia entregue sem header Bcc); lote 2 (50) pronto, aguarda "vai" do dia.

**Meta do mês 1 (north star):** 500 visitas → 100 instalações PWA → 25 contas → 10 leitores ativos (livro importado) → 3 conversas de Sócio-Fundador. Break-even operacional da casa: 25 assinantes.

## 5. MINUTAS PRONTAS

### 5.1 E-mail — Onda 1 OURO (contatos próximos, 200)

**Remetente (RETIFICADO 09/09 ~11:1x): "Miguel do Rosário" <migueldorosario@gmail.com>** — ordem do Miguel: "as pessoas me conhecem... o info vocês não conhecem, vai entrar como spam". Rota = SMTP do Google com senha de app (chave `GMAIL_MIGUEL_APP_PASSWORD` no cofre — PENDENTE o Miguel gerar em myaccount.google.com/apppasswords). info@ fica para as ondas 2-4 (gente que não o conhece) e notificações do app.

**v2.1 (09/09 ~11:0x, voz do Miguel — ✅ APROVADA por ele ~11:5x: "Quanto ao texto, eu aprovei. Aprovei.").** O teste v1 (inglês, assunto minúsculo, "Olá, Miguel!") foi reprovado pelo Miguel: "é seu livro em qualquer idioma, não é só inglês" + "tem que começar com maiúscula" + o corpo em produção deve ser genérico (não dirigido a ele). A v2 incorporou a fala dele quase literal (apresentação do editor, presente para o filho, chave própria barata, página de preços no app, livro vira áudio). A v2.1 acrescenta a frase que ele ditou em seguida: "ajuda demais a leitura e pode transformar a leitura numa novidade, misturando tecnologia, inteligência artificial e educação".

**Assunto:** Seu livro em qualquer idioma, resolvido (e o vídeo de 2 horas também)
**Preheader:** O Moka lê, traduz, resume e responde perguntas sobre livros e vídeos em qualquer idioma. Gratuito, com a sua chave de IA.

Olá!

Sou Miguel do Rosário, editor do portal O Cafezinho. Sempre gostei muito de ler e, hoje, passo o dia inteiro lendo e assistindo a vídeos para me informar. Mas sempre aparece aquele livro ou aquele vídeo que demora mais porque está num idioma que eu não domino tanto.

Foi para resolver isso que a nossa casa construiu o Moka.

O aplicativo é de graça. Você usa a sua própria chave de IA, e o próprio Moka explica, passo a passo, como conseguir uma em qualquer provedor. Dependendo do uso, o custo é de centavos: um livro inteiro sai por cerca de R$ 0,38 e uma entrevista de duas horas por uns R$ 0,56. E há uma página dentro do aplicativo com o preço atual de cada modelo, para você escolher com clareza antes de gastar qualquer coisa.

Ele também transforma o livro em áudio: você pode escutar a leitura na língua que quiser.

Isso é muito bom para a educação. Ajuda demais a leitura e pode transformar a leitura numa novidade, misturando tecnologia, inteligência artificial e educação. É o tipo de presente que você pode dar para o seu filho.

Experimente agora: www.mokareader.com

Um abraço,
Miguel do Rosário
editor do portal O Cafezinho

*(rodapé: Você recebeu este e-mail porque faz parte da lista de leitores do Cafezinho. Para não receber mais, responda a esta mensagem com a palavra SAIR.)*

---
**v1 (aposentada 09/09 — histórico):**
**Assunto:** seu livro em inglês, resolvido (e o vídeo de 2h também)
**Preheader:** a chave de IA é sua — centavos por livro, sem mensalidade

Olá, [nome]!

Testa uma coisa aí: abre o Moka (www.mokareader.com), cola um livro em inglês e toca numa palavra. A tradução aparece na hora. O livro inteiro? Ele traduz em volumes, avisa quanto vai custar ANTES (centavos) e mostra o recibo DEPOIS.

Cola um link de vídeo de 2 horas? Ele devolve a transcrição completa, o resumo, quem fala nele e o contexto político — e responde suas perguntas com timestamp.

O pulo do gato: você usa a SUA chave de IA (OpenAI, Anthropic, DeepSeek…), criptografada no seu aparelho. Ninguém no meio, sem mensalidade, sem seus dados indo pra nuvem de estranho. Um livro sai por ~R$ 0,38; um vídeo longo, ~R$ 0,56.

É grátis pra começar: www.mokareader.com

Um abraço,
Miguel

*(rodapé: você recebe este e-mail porque conversamos sobre o Moka. Não quer mais? Responde "sair" que eu tiro da lista na hora.)*

---
**fim da v1.** A minuta que vale para disparo é a v2 acima, quando o Miguel aprovar.

### 5.2 E-mail — Onda 2 QUENTE (500, mesmo corpo + assunto alternativo)

**Minuta PREPARADA na ronda de 17/09 (dia 13/30)** — íntegra em `dias/2026-09-17_minuta_onda_quente.md`; disparo via info@ (godaddy), BCC lotes 50, aguarda "vai".

**Assunto:** leia qualquer livro, assista qualquer vídeo — por centavos
**Preheader:** com a sua própria chave de IA, no seu aparelho

### 5.3 E-mail — Reativação (ondas 3-4, mais curto)

**Assunto:** o app que devolve seus dados pra você
Corpo: 3 parágrafos — o problema (apps de IA comem seus dados e cobram assinatura), a virada (BYOK + memória própria), o convite (link + 1 caso de uso concreto).

### 5.4 WhatsApp — 3 mensagens (pessoais, UMA por semana)

**W1 (aquecimento):**
Oi [nome]! Lancei um app chamado Moka — leitor de livros com IA própria (você usa a sua chave, seus dados ficam no seu aparelho). Posso te mandar um print de como fica? ☕

**W2 (demonstração — com print/banners):**
Olha ele funcionando: toque na palavra → tradução na hora; link de vídeo de 2h → resumo em minutos. Tudo por centavos, sem assinatura. Quer testar? www.mokareader.com

**W3 (convite direto):**
[Print do módulo Memória] A parte que mais gosto: tudo que você lê vira memória da IA — ela lembra dos seus livros. Se testar, me conta o que achou? Se curtir, te convido pra ser Sócio-Fundador (200 vagas).

**Regras de ouro WhatsApp:** texto LIMPO (sem asteriscos, sem #), 1 mensagem por semana por contato, sempre com saída fácil ("me avisa se incomodar").

## 6. BANNERS — 3 FAMÍLIAS

| Família | Gancho visual | Título | Subtítulo | CTA |
|---|---|---|---|---|
| **A — Reader** | Print do leitor com tradução aberta | SEU LIVRO EM QUALQUER IDIOMA | Toque na palavra. Tradução na hora. Livro inteiro por centavos. | COMECE GRÁTIS · mokareader.com |
| **B — Video** | Print do resumo de vídeo | 2 HORAS DE VÍDEO EM 2 MINUTOS | Transcrição, resumo, personagens e contexto — cole o link. | TESTE AGORA · mokareader.com |
| **C — Memória** | Print da memória + harness | UMA IA QUE LEMBRA DO QUE VOCÊ LEU | Sua chave. Seus livros. Sua memória. Nada no meio. | CRIE SUA MEMÓRIA · mokareader.com |

Formatos por família: **web 1200×628** (sites/newsletters) · **story 1080×1920** (WhatsApp status/Stories) · **post 1080×1080** (feed). Identidade: laranja Moka #FF9E3D para destaque + paleta Amanhecer Azul de fundo + print real do app + tipografia grande (régua do Miguel: nada trespassado, rótulo grande, legível no celular).

## 7. ROBÔ DE MATÉRIAS — "Moka Diário" (design)

**Missão:** todo dia, 1 matéria sobre o universo do Moka Reader no portal — eduque o leitor e puxe tráfego orgânico pro app.

- **Pauta:** 30 pautas prontas em `PAUTA_30_MATERIAS_ROBO_MOKA.md` (ângulo + fontes + CTA por matéria).
- **Produção:** ronda diária escreve o rascunho (padrão editorial da casa: EMU-2, abertura direta ao fato, zero metalinguagem, sem asteriscos) e publica como RASCUNHO no WP (autor zcode_miguel 5795), capa procurada na casa (nunca IA — Emenda NO-IA), tags + categoria Tecnologia/IA.
- **Gate:** matéria pede revisão na ponte (2 checks, regra da casa). Publicação: padrão editorial normal do Cafezinho. **Publicidade transparente:** matéria termina com selo "Conteúdo produzido pelo Cafezinho para apresentar o Moka, projeto da casa."
- **Fase 2 (quando o Miguel der "vai"):** script robô dedicado (padrão DSN) na Tencent escrevendo sozinho 05:30, revisão 2 checks, publicação 07:00. Rollback = 1 linha de cron.
- **Medição:** GA4 do app (G-43CSQVKW6N) — visitas vindas do portal por matéria.

## 8. RONDA DIÁRIA — o que acontece todo dia 09:30

1. Lê este plano + o fórum `Foruns/forum_marketing_moka_20260903.md` (estado do dia).
2. Executa a ação do dia (tabela §4): produz print/banner/minuta/matéria-rascunho.
3. Entrega ao Miguel: Telegram (ponte_cafezinho) com resumo 🟢🟡🟠🔴 + o que precisa dele (ex.: "vais" pendentes).
4. Registra adendo no fórum + atualiza esta tabela (`[x]`) + métricas do GA4 quando disponíveis.
5. Nunca dispara nada externo sem OK do Miguel; nunca inventa número de métrica (GA4 ou nada).

## 9. MÉTRICAS QUE IMPORTAM (painel semanal)

- Visitas únicas no mokareader.com (GA4) · installs PWA · contas criadas · livros importados (proxy de engajamento real) · vídeos resumidos · e-mails: abertura/click por onda · WhatsApp: respostas · portal: cliques app↔matéria.
- Fonte única de verdade: GA4 do app + painel /socios (quando o SQL rodar — pendência antiga).
- Toda métrica reportada tem data real (date via Bash) e origem citada. Métrica sem fonte = não reporta.

## 10. PENDÊNCIAS QUE PRECISAM DO MIGUEL

1. **"Vai" para disparar a onda OURO** de e-mail (200 contatos — minuta 5.1).
2. **"Vai" para a 1ª matéria do robô** ir ao ar (rascunho será entregue na ronda).
3. Rodar `socios-schema.sql` no Supabase (2 min — liga o painel de métricas).
4. Appeal da Play Store (texto pronto na saga; lembrete diário pausado).
5. Definir cota de envio de e-mail/dia (rota msmtp Tencent — sugerido 50/dia por onda, aquecimento de domínio).

— ZM · ZCode/GLM-5.3 · 03/09/2026
