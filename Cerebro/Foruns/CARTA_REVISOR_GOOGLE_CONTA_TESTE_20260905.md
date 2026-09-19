# 📨 CARTA AO REVISOR DO GOOGLE — TEST ACCOUNT COM IA INCLUSA (05/09/2026)

> Para colar no Play Console: **App content → Login details** (e/ou no appeal/contestação em Policy status).
> Conta: zcode.e2e.20260801@gmail.com · senha no cofre MOKA_REVISOR_SENHA (sha8 eab5f63e) · saldo 2.000 pts.
> Origem: ordem do Miguel 05/09 ~11h2x ("escreva já uma carta em inglês para eu pedir para o revisor testar de novo").

---

Subject: Test account with full AI access provided — Moka (com.mokareader.app)

Hello Google Play review team,

Thank you for reviewing Moka. Your previous notice asked for a test account so the app could be fully reviewed. We have now created a dedicated reviewer account with ALL AI features unlocked — no purchase, no subscription, and no API key of your own required.

TEST ACCOUNT (exclusive for the review team):
E-mail: zcode.e2e.20260801@gmail.com
Password: [VALOR SÓ NO COFRE: chave MOKA_REVISOR_SENHA nos .env.unificado, sha8 eab5f63e — regra do Cofre: não gravar valor aqui]

HOW TO USE IT
Open the app (it loads www.mokareader.com) or visit https://www.mokareader.com, then:
1. Tap ⚙️ Settings → "Sign in with your account" (Entrar com sua conta).
2. Enter the e-mail and password above.
3. Import any EPUB/PDF (or open the sample flow) and use everything: tap-to-translate word/page, whole-book translation, page explanation, summaries, Q&A about the text, and neural read-aloud voices (OpenAI).

With this account signed in, every AI feature is real and fully functional — the AI runs on our own server balance, loaded as a courtesy for this review. There is nothing to buy and nothing to subscribe to.

CLARIFICATIONS
- Moka is 100% free: no paywall, no subscription, no in-app purchases. Reading, the library, video summaries and all core features work WITHOUT any login.
- Regular users may optionally connect their own AI API key (BYOK) and pay their AI provider directly, outside the app — Moka never charges anything and stores keys encrypted on the user's device only.
- Only accounts we grant (like this one) can use the courtesy AI balance — the credentials above are exclusive to your team, and usage is capped by the courtesy balance itself.
- If the balance runs low during your review, reply to this submission and we will top it up immediately.

Thank you for your time — we hope this makes the review straightforward.

Best regards,
Miguel Dorosario
Moka — Reader & Video
https://www.mokareader.com

---

## Passo a passo no Play Console (conta Google do Miguel)

1. Acesse **play.google.com/console** (logado na sua conta Google da Play).
2. À esquerda, escolha o app **Moka**.
3. Caminho A (o que o Google pediu — o rápido): **Release → Production** e veja se há banner de erro com link, OU **Policy → App status / Status da política** (mostra o problema "Erro, 19 de ago." da rejeição por paywall).
4. Vá em **Policy → App content → Detalhes de login (Login details)**: marque que o app **não exige login** para funcionar e **adicione as credenciais de teste** (cole a carta acima — e-mail + senha + instruções).
5. Salve. Depois em **Release → Visão geral da publicação (Publishing overview)** → **Enviar para análise / Reenviar para análise**.
6. A contestação de 19/08 consta como enviada; atualizar os Detalhes de login e reenviar é o caminho rápido que o próprio Console indicou na tela de 27/08.

— ZM · ZCode/GLM-5.3 · 05/09/2026

---

## ADENDO 3 — 06/09 07:3x–09:2x: GUIA CLIQUE-A-CLIQUE + CURA URGENTE DO LOGIN NO CANÔNICO

### O caminho no Play Console (guiado ao vivo com prints do Miguel)
1. app-list → "Ver app →" na linha do Moka (status "App rejeitado").
2. Painel do app → "Acessar 'Status da política'".
3. Status da política: ficha "App rejeitado — Recusado 19 de ago. de 2026" + ficha "Contestações — Resposta enviada à contestação (envio 20/08)". **Houve contestação em 20/08 com resposta do Google que nunca tínhamos lido.**
4. "Mais detalhes" da rejeição = texto OFICIAL do Google: paywall; pede conta de teste com créditos suficientes OU bypass, na seção Detalhes de login; e "Envie as mudanças para análise... Acesse Visão geral da publicação". Confirma 100% o nosso preparo (conta com 2.000 pts + carta).
5. Conteúdo do app → Detalhes do login (URL .../app-content/testing-credentials): "Sim" já marcado; entrada antiga "Test account" (do envio de agosto) com lápis/lixeira; toggle "Permita que o Google use..." LIGADO; botões Descartar/Salvar no rodapé.
6. PRÓXIMO CLIQUE (pendente): lápis da linha "Test account" → colar e-mail + senha + instruções EN → Salvar → Visão geral da publicação → refazer envio.
- IDs certos: conta 8941059687461753914 · app 4974547187552827561 (os prints antigos do Astra traziam outro ID de conta — links antigos descartados).

### O teste de login que falhou (e por quê)
Miguel testou a credencial do revisor NO APP e levou "E-mail ou senha errados". Causa: o app tem DUAS portas de login — AuthModal (conta cloud Supabase, sync de biblioteca) e ContaButton/gateway de pontos (Tencent). A conta do revisor só existe no gateway; a porta cloud a recusa. Prova: GET /api/pontos/painel/saldo com a credencial = 200 (saldo 2000); senha errada = 401. Ou seja: credencial VIVA; a porta é que era a errada.
Dois bugs de UI relatados junto: (a) botão "Entrar" da topbar com a palavra estourando da caixa; (b) caixas de login fechando sozinhas no meio da digitação.

### Cura (ordem do Miguel: direto no canônico, urgência)
Commit **babea59** no origin/main (tag backup_pre_fix_login_20260906), 3 arquivos:
- globals.css: guerra de especificidade — ".igot-topbar-actions button" (0,1,1) vencia o override ".auth-signin" (0,1,0) mesmo com !important (herdava fonte 20px + caixa 44x44 de ícone). Novo seletor ".igot-topbar-actions button.auth-signin, button.auth-signin" (0,2,1 / 0,1,1 posterior) vence; botão vira pílula accent visível; idem no media mobile.
- AuthModal.tsx: overlay NÃO fecha mais por clique fora (fecha ✕/Esc); PORTA DUPLA — se o Supabase recusar, tenta a mesma credencial no gateway (verificarConta) e, se valer, setConta + evento "moka-conta-mudou" + fecha. Revisor entra por qualquer porta.
- ContaButton.tsx: pop NÃO fecha mais por clique fora (✕ novo nos dois estados); escuta "moka-conta-mudou" e refaz verificação sem reload.
Deploy verificado no ar: marcador "moka-conta-mudou" no chunk 7714-0165... servido + regra "button.auth-signin" no CSS fd885143... servido. Push no mirror RECUSADO (espelho divergido antes do fix) — sync ritual do espelho fica pendente, sem urgência.
Rito Ousadia→Espelho→Canônico PULADO por ordem explícita do Miguel (urgência do reenvio ao Google).

### Estado da missão
- Aconteceu: guia até a tela Detalhes do login; causa da falha de login achada e curada no canônico; credencial re-provada na API.
- Falta: Miguel retestar o login no navegador (Ctrl+Shift+R); preencher o lápis "Test account" (e-mail + senha + instruções EN); Salvar; Visão geral da publicação → refazer envio; milestone "APPEAL/REENVIO ENVIADO" aqui e no fórum da saga Play.
- Preciso de você (Miguel): reteste do login + prints da janelinha de edição preenchida e da tela de refazer envio.

— ZM · ZCode/GLM-5.3 · 06/09/2026 09:2x

## ADENDO 4 — 06/09 ~09:5x: ENTRAR VOLTA À PÁGINA INICIAL (ordem do Miguel) + MARKETING PAUSADO

- Ordem: "voltar o login à página inicial... o botãozinho de entrar ao lado da bandeira de idioma. Tem que ficar sempre lá, toda página tem que ter isso."
- Commit 61bbd86 no origin/main: Capa (home) ganhou AuthGate ao lado do LangSwitcher (+ CSS .capa-lang com gap/align); /experimente idem (era a única outra página pública sem o botão — sobre, tutorial e todas as páginas de módulo já tinham via TopNav/info-topbar; páginas de fluxo auth/* ficam de fora por serem parte do próprio login).
- Provas: home agora carrega o chunk 7714 (código de login com o fallback) + screenshot canto sup. direito mostra pílula laranja "Entrar" à esquerda da bandeira BR (arquivo /tmp/moka_home_com_entrar.png).
- Marketing Moka PAUSADO por ordem do mesmo recado até concluir a missão Play Store: automação diária removida + prompt arquivado (ver Adendo 3 do fórum de marketing).
— ZM · ZCode/GLM-5.3 · 06/09/2026 09:53:31 BRT

## ADENDO 5 — 06/09 ~10:0x: BOTÃO ENTRAR AGORA REFLETIR AS DUAS CONTAS (6a256ff)

- Bug do Miguel: entrou pela porta de PONTOS e o botão da home continuou "Entrar" (AuthButton só olhava o Supabase).
- Cura: AuthGate compõe o estado (user Supabase OU conta de pontos via getConta/evento moka-conta-mudou) — logado em qualquer porta = avatar 👤 com inicial do e-mail; Sair limpa as duas; sem loading eterno quando a conta de pontos já existe.
— ZM · ZCode/GLM-5.3 · 06/09/2026 11:05:51 BRT

## ADENDO 6 — 06/09 ~11:4x: MILESTONE — REENVIO AO GOOGLE EM ANÁLISE

- Miguel colou credenciais + instruções EN (versão 482 chars, limite 500 do campo) na entrada "Test account" dos Detalhes do login e chegou à Visão geral da publicação: "Alterações em análise — as mudanças serão enviadas para revisão assim que as verificações forem concluídas (até 14 min)" e "O que você nos informou: Conteúdo do app: atualização das instruções de detalhes de login (todos ou alguns recursos são restritos)".
- OU SEJA: a resposta à rejeição de 19/08 (paywall → conta de teste com créditos) FOI ENVIADA. Missão principal cumprida; agora aguardar o veredito do revisor.
- Pendências de LOJA que apareceram na Visão geral (lançamento completo, não são rejeição): países (adicionar resto do mundo), Classificação do conteúdo (questionário IARC), Público-alvo (18+), Política de Privacidade (URL https://www.mokareader.com/privacidade), Declaração de anúncios (não temos anúncios), Segurança dos dados (questionário), Apps de saúde (não é), Categoria (Livros e referências ou Educação). Respostas-base verificadas no código: sem anúncios; telemetria própria mínima (/api/metrics/ping de visita); conta cloud = e-mail (Supabase); conta pontos = e-mail+senha (gateway); chaves de IA ficam no dispositivo.
- Próximo: guiar o Miguel nesses formulários um a um (prints pergunta-resposta); depois vigiar a resposta do Google.
— ZM · ZCode/GLM-5.3 · 06/09/2026 11:48:28 BRT

## ADENDO 7 — 06/09 ~11:55: PRIVACIDADE COM BANDEIRINHA+ENTRAR E BILÍNGUE (2164349)

- Ordem do Miguel: toda página tem que ter a bandeirinha e o Entrar em cima — /privacidade era a faltante (texto fixo pt, sem topo).
- Feito: PrivacidadeConteudo.tsx (client, PT p/ português · EN p/ todos os outros idiomas — revisor lê inglês) + wrapper server mantém canonical; topo padrão info-topbar (← Moka · Entrar laranja · bandeira). Deploy provado: info-topbar servido + screenshot.
- URL para o Console: https://www.mokareader.com/privacidade
— ZM · ZCode/GLM-5.3 · 06/09/2026 11:55:29 BRT
