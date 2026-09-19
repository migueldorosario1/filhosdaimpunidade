# Fórum — Moka 6.7: app sem cadastro obrigatório (fix rejeição Google Play "paywall") (19/08/2026)

> Data: 2026-08-19 ~09:25 · Autor: ZCode/Kimi K3 · Status: ✅ **NO AR E VERIFICADO** (commit `cc5f236`)
> Ordem do Miguel (19/08, voz): consertar o app ANTES de apelar ao Google, "fazer a mudança mais segura possível pro Google", recado no site traduzível pelas bandeiras, resposta ao Google preparada em EN + PT para aprovação.
> Contexto: rejeição do Play 19/08 00:54 — "App content is restricted by a paywall" (o revisor bateu no muro de login e leu como paywall).

## Causa-raiz confirmada

O login estava **OBRIGATÓRIO** desde 13/08 (commit `b5cd786`, decisão do Miguel da época): o componente `RequireAuth` envolvia `/estante` e `/book/[id]` — sem login, só aviso "mas você precisa estar logado". O FAQ da ajuda dizia "Sim, é de graça — você só precisa entrar com Google ou e-mail". Para o revisor do Google = conteúdo restrito.

## O que foi feito (tudo à prova de rejeição)

1. **Muro de login REMOVIDO** de `/estante` e `/book/[id]` — o app abre e funciona sem cadastro; login fica **opcional** (só sync nuvem e /socios). `RequireAuth.tsx` mantido no repo mas marcado **OBSOLETO** (rollback fácil, sem uso).
2. **Recado no site (i18n, bandeiras funcionam):** nova 1ª pergunta do FAQ /ajuda — **"O Moka tem paywall ou cobrança?"** → "100% gratuito: sem paywall, sem assinatura, sem compra no app, sem cadastro obrigatório; a IA usa a chave do próprio usuário" (pt) / versão "100% free..." (en, fallback das outras 10 línguas). Pergunta "Preciso criar conta?" corrigida para **Não** (pt+en).
3. **Qualidade:** backup `Moka/backups/moka_lab_pre_sem_login_20260819.zip`, `tsc`+`next build` verdes (22/22), commit `cc5f236` push main → Vercel.
4. **Verificação ao vivo:** chunk do /estante com **0** ocorrências da string da trava ("precisa estar logado"); /ajuda com o recado novo em pt e en.
- Nota: o commit levou junto `backups/moka_pre_seo_gsc_redirects_20260816/` (pasta de backup antiga que estava untracked no repo — código-fonte público, sem segredos; sem impacto).

## Resposta ao Google + App access (rascunhos — AGUARDANDO APROVAÇÃO DO MIGUEL)

**Reply (EN — idioma que o Google exige) e versão PT** foram preparadas no chat 19/08 ~09:30 junto com o texto do campo **App access** (Play Console → Policy → App content → App access: "No login required — all content is freely accessible without an account."). Sequência: app já consertado e no ar → Miguel aprova os textos → ele cola o App access no Play Console → envia a resposta.

## Estado da missão

- **Aconteceu:** app consertado e no ar (sem cadastro); recado no site; rascunhos EN+PT prontos; App access text pronto.
- **Falta:** Miguel aprovar os textos → colar App access no Play Console → mandar a resposta. Play Store segue rejeitada até então.
- **Preciso de você (Miguel):** aprovação dos 3 textos (estão no chat). Para o `socios-schema.sql` (painel /socios): explicado simples — só você pode rodar no SQL Editor do Supabase (2 min); sem credencial de escrita nos cofres, eu não consigo executar. Se preferir, te colo o SQL aqui pronto.

---
— ZCode/Kimi K3, 2026-08-19


## ✅ ADENDO 19/08 ~09:45 — Banco de sócios REMOVIDO da fase 1 (ordem do Miguel)

- **Ordem:** "não quero ter banco de sócios por enquanto; tira qualquer referência a banco de sócios lá no Moka; tudo gratuito; segunda fase depois."
- **Feito (commit `fc84138`):** rota `/socios` REMOVIDA (404 em produção; código preservado no git p/ fase 2) · links comentados de sócios limpos de `/sobre` e `/video` · comentários internos atualizados (VisitPing, sitemap) · `socios-schema.sql` mantido fora do app (fase 2) · backup `moka_lab_pre_sem_socios_20260819.zip` · tsc+build verdes (21/21).
- **Prova ao vivo:** `/socios` 404; home/sobre/video 200 com **0** ocorrências de "sócios".
- **Supabase:** com isso o `socios-schema.sql` fica SEM urgência (é infra da fase 2) — pendência retirada da fila quente.


## ✅ ADENDO 19/08 ~09:50 — Resposta ao Google gravada como RASCUNHO (ordem do Miguel)

- **Ordem:** "pode responder por mim ao google. assina como Miguel do Rosário, responsável pelo aplicativo Moka Reader. Mas não envia — deixa em rascunho que eu vou lá e clico em enviar."
- **Feito:** rascunho criado na pasta **Drafts** do mailbox `info@mokareader.com` (GoDaddy/Titan) via IMAP APPEND — NADA foi enviado. Assunto `Re: Action Required: Your app is not compliant with Google Play Policies (Moka)`, In-Reply-To/References da mensagem original (Message-ID do Google de 19/08 00:54), corpo = minuta EN aprovada, assinatura Miguel do Rosário (Founder — responsável pelo Moka Reader).
- **Onde o Miguel envia:** webmail GoDaddy (email.secureserver.net) ou Titan → pasta Drafts/Rascunhos → abrir → Enviar.
- **Aviso registrado:** o remetente do Google é `no-reply-googleplay-developer@google.com` — resposta por e-mail pode não chegar a humano; o canal efetivo da apelação é o Play Console (App access + apelação). Textos prontos no chat para colar lá.
