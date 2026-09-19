# 📱 Fórum — Moka TWA Android → Play Store (07/08/2026)

**Sprint:** empacotar o Moka Reader como app Android (TWA via Bubblewrap) e deixar tudo pronto para a Play Store. Aprovado pelo Miguel ("pode montar sim!"). Sessão: ZCode (chat direto, workspace ZCodeProject).
**Memória-irmã (log técnico completo):** `Memorias/memoria_moka_twa_android_play_store_20260807.md`

## Decisões

1. **Rota TWA confirmada** (doc 16 do Cérebro): o site É o app — sem código nativo. iOS (Capacitor + build em nuvem) fica para depois da conta Apple.
2. **Pacote:** `com.mokareader.app` (nome permanente na Play). Nome no launcher: "Moka". Nome completo: "Moka — Leia qualquer coisa. Entenda tudo."
3. **Versionamento:** `versionCode=1` (1º upload) / `versionName="5.7.1"` (paridade com o site).
4. **Keystore NÃO vai para o GitHub** (`.gitignore` no `apps/twa`). Espelhado nos DOIS cofres (Regra 4/§117): `keystores/moka_twa/android.keystore` + `MOKA_TWA_KEYSTORE_PASSWORD` nos `.env.unificado`.
5. **Ferramentas em userspace** (sem sudo): JDK 17 Temurin `~/java/jdk-17`, SDK `~/Android/Sdk`, bubblewrap 1.25.0 (npm/nvm). Env: `source ~/moka-twa-env.sh`.

## O que está PRONTO (07/08)

- ✅ Projeto TWA gerado em `Moka-Lab/apps/twa` (bubblewrap init 100% automatizado via PTY)
- ✅ **APK assinado** `apps/twa/app-release-signed.apk` (1,4MB) + **AAB de loja** `apps/twa/app-release-bundle.aab` (1,5MB)
- ✅ Certificado: CN=Moka Reader App / O=Cafezinho Media Group / C=BR, **válido até 2081**, SHA256 `9A:BB:E0:F1:…:35:95:44:26`
- ✅ `assetlinks.json` **NO AR**: `https://www.mokareader.com/.well-known/assetlinks.json` HTTP 200, conteúdo verificado (fingerprint bate com o keystore) — commit `8790c9a` pushado → Vercel deployou
- ✅ Backup pré-deploy: `Moka/backups/moka_pre_deploy_twa_20260807_1215.zip`
- ✅ `store_icon.png` (512) gerado para a listagem da loja
- 🔄 Emulador Android 34 (KVM, headless) no ar, APK instalado, app lançou — teste final em curso

## O que FALTA (próximos passos)

1. Terminar a prova no emulador (passar da tela de boas-vindas do Chrome no emulador novo → screenshot do Moka em tela cheia, sem barra de URL = assetlinks validado)
2. Screenshots para a listagem da Play Store (podem sair do próprio emulador)
3. **Ação do Miguel:** criar a conta **Play Console organização (US$25, pagamento único)** — D-U-N-S 943494728 já recebido (04/08) dispensa o teste de 20 testadores/14 dias
4. Com a conta: criar app na Play Console → preencher Data Safety/privacidade (a página `/privacidade` já existe) → upload do `app-release-bundle.aab` → revisão → publicar
5. iOS depois: Apple Developer org (US$99/ano) + Capacitor + build em nuvem (Codemagic/EAS)

## O que preciso de você (Miguel)

- **Criar/pagar a conta Play Console organização (US$25)** — é o único gargalo que resta para o Android. Com ela, o upload do AAB leva minutos.
- (Pendências antigas ainda suas: colar `SMTP_MOKA_*` no Supabase Dashboard; trocar a senha GoDaddy que passeou em chat.)

## 🔄 Atualização 13/08/2026 ~00:42 BRT — App EM ANÁLISE pelo Google (nada pendente p/ Miguel)

**Origem:** Miguel perguntou se foi aprovado; forneceu texto do Console + 10 prints (3 da visão geral em 00:30 + 7 dos formulários individuais em 00:36–39).

**⚠️ Correção ao estado anterior:** a seção "O que FALTA" deste fórum (redigida 07/08) listava os 6 itens de "Conteúdo do app" + categoria como pendentes de preenchimento. **Estava desatualizado / incorreto.** Confirmado nos prints de 13/08 que **TUDO está preenchido**:

- ✅ Política de Privacidade: `https://www.mokareader.com/privacidade`
- ✅ Segurança dos dados (questionário respondido)
- ✅ Declaração de anúncios: **app SEM anúncios** (freemium com pontos)
- ✅ Público-alvo e conteúdo: **18+**
- ✅ Classificação do conteúdo (questionário IARC)
- ✅ Apps de saúde (não se aplica)
- ✅ Categoria selecionada

**Estado REAL (13/08):** `Alterações em análise` — o Google está revisando as **declarações de política** que o Miguel preencheu (ID de publicidade, apps governamentais, recursos financeiros, login com recursos restritos). A "Visão geral da publicação" mostra os itens com verbos "atualizar/preencher" **enquanto estão em análise** (enganoso — não significa vazio). O botão **"Iniciar o lançamento completo"** (Produção 1.0, 176 países) só ativa **depois** de o Google concluir esta análise.

**A bola está 100% com o Google.** Nada pendente para o Miguel agora.

**Linha do tempo:** AAB v5.7.1 (827 KB) subido ~08/08 · declarações em análise desde então · 13/08 = dentro do prazo normal (1–3 dias úteis p/ análise de declarações). Próximos marcos: (1) análise das declarações conclui → (2) Miguel clica "Iniciar o lançamento completo" → (3) revisão do app em si (1–7 dias úteis; conta org nova pode ser mais lenta) → publicado.

**Ação Miguel:** nenhuma por ora. Monitorar Console/e-mail. Se o Google pedir algo → responder (eu ajudo). Atualizar este adendo quando sair o resultado.

---

**Relacionados:** `CEREBRO_INDEX_MOKA_LOG.md` (timeline) · fórum D-U-N-S · doc 16 (rotas de loja) · `forum_moka_sprint_pos_pivot_552_57_20260805.md`.

---

## Adendo — 27/08/2026 15:45: checagem do e-mail a pedido do Miguel ("vê se o Play Store respondeu o pedido de revisão")

**VEREDITO: NÃO respondeu — e o appeal por e-mail NUNCA chegou ao Google.**
- INBOX do info@mokareader.com conferida inteira (IMAP GoDaddy): nada novo desde 22/08; Spam/Archive/Trash vazios de Google.
- Único e-mail "do Google" pós-notificação segue sendo o auto-reply de 19/08 13:04 UTC: "*** YOUR EMAIL MESSAGE WAS NOT RECEIVED BY GOOGLE PLAY SUPPORT *** — só respondemos pedidos via formulários de contato".
- E-mail original (19/08 00:54 -0700): app **Rejected** — "Violation of Play Console Requirements… We could not review your app" (login/demo, conforme diagnóstico 26/08). Sem link-token de appeal no corpo; o caminho é o **Play Console** (ou "Contact us" do Help Center: support.google.com/googleplay/android-developer).

**Próximo passo (Miguel, quando quiser):** Play Console → Política/App status → resolver o item de login (conta de teste OU fluxo sem login — ver [[moka-play-store-appeal-google-resposta-20260826]]) → submeter o appeal pelo FORMULÁRIO do Console (não por e-mail).

### Complemento 27/08/2026 15:58 — o "recado no fórum do Play Store" localizado

Era o E-MAIL de appeal enviado em 19/08 13:04 UTC (pasta Sent do info@mokareader.com) respondendo à notificação, texto excelente: Moka 100% grátis, sem paywall/assinatura/compras, login opcional (só sync de biblioteca), IA = chave do próprio usuário (BYOK, paga direto ao provedor), app acess information atualizada no Console. Destinatário: no-reply-googleplay-developer@google.com — **endereço que NÃO recebe**. O auto-reply de rejeição chegou 37 segundos depois. Desde então, zero resposta (INBOX/Spam/Archive/Trash conferidos 27/08 15:45).

**Conclusão prática:** o texto do appeal está PRONTO e BOM — só precisa ser entregue pelo canal certo (formulário do Play Console → Policy/appeal, com conta de teste anotada). É clique do Miguel (conta Google dele); qualquer sessão guia passo a passo.

### 27/08/2026 18:34 — ⏰ RONDA DIÁRIA 11h CRIADA (ordem do Miguel "me lembra disso uma vez por dia, todo dia às 11h")

`automation-3631380a` — todo dia 11:00: (1) checa IMAP info@mokareader.com por resposta do Google (INBOX+Spam+Archive+Trash); (2) sem resposta e appeal não enviado → Telegram diário cobrando (link Console + texto pronto neste fórum); (3) com resposta → Telegram imediato + adendo; (4) appeal enviado → vira vigilância silenciosa (sem spam). **1ª execução: 28/08 11:00 (nextRunAt conferido).**

### 27/08/2026 18:43 — 🔍 MIGUEL ACESSOU O CONSOLE (tela colada) — causa-raiz da rejeição CONFIRMADA + fix já promovido aos 3

**Tela (Policy status → Detalhes do problema):** rejeição = "app restrito por paywall; forneça conta de teste com assinatura/waypoints ou bypass de pagamento nos Detalhes de login". Status: "Erro, 19 de ago." + **"Contestação enviada"** (a de 19/08 está no sistema). Google diz: caminho rápido = atualizar **Detalhes de login** → reenviar pra análise.

**CAUSA-RAIZ (evidência na tela):** o card do app "🔑 Como conseguir sua chave — **Custo pra você: centavos por uso**, pagos direto ao seu provedor (resumo US$ 0,01–0,05…)" foi lido pelo revisor como paywall. Como o app é TWA (espelha o site), **fix no site = fix no que o revisor vê**: string `byok_cost` reformulada nos 12 idiomas (commit `420aad3`, PROMOVIDO aos 3 ambientes) — agora abre com "O Moka é 100% gratuito — sem assinatura, sem compras e sem paywall. Se quiser usar as IAs, o custo (OPCIONAL) é pago direto ao provedor da sua chave, FORA do app… O Moka nunca cobra nada."

**PASSO A PASSO entregue ao Miguel (Console, ~10 min):** Conteúdo do app → Detalhes de login → marcar que NÃO exige login → colar instruções pro revisor (texto pronto no chat) → Visão geral da publicação → Enviar pra análise. Contestação de 19/08 segue em análise; ronda 11h vigia a caixa.

### ⏰ Ronda diária 11h — 29/08/2026 11:02 (última checagem da caixa)

Caixa info@mokareader.com checada (INBOX/Spam/Archive/Trash): **nenhum e-mail do Google desde 27/08** — sem resposta à contestação de 19/08. "APPEAL ENVIADO" (reenvio c/ Detalhes de login) ainda não confirmado pelo Miguel → lembrete diário enviado ao Telegram (texto atualizado ao estado real: contestação consta, falta Detalhes de login + reenvio; card de paywall já corrigido no site 27/08 18:43).

### ⏰ Ronda diária 11h — 30/08/2026 11:02 (última checagem da caixa)

Caixa checada (4 pastas): **nenhum e-mail novo desde 29/08 11:02** — Google mudo. ATENÇÃO futura: a menção "APPEAL ENVIADO" na linha da ronda 29/08 é da própria ronda ("ainda não confirmado"), NÃO é o marco. **Marco oficial a partir de agora: adendo contendo "MILESTONE: APPEAL ENVIADO ✅"** (gravado só quando o Miguel confirmar o envio). Hoje: reenvio ainda pendente → 2º lembrete diário enviado ao Telegram.

### ⏰ Ronda diária 11h — 31/08/2026 11:02 (última checagem da caixa)

Caixa (4 pastas): **nenhum e-mail novo desde 30/08 11:01**. DETECTOR AFUNDO: o grep de "MILESTONE" dava falso positivo porque a ronda 30/08 citou a string na própria definição — **marco real = adendo cujo TÍTULO começa com "MILESTONE: APPEAL ENVIADO"** (grep: '^#\+.*MILESTONE: APPEAL ENVIADO'; hoje = 0). Reenvio segue pendente → 3º lembrete diário enviado ao Telegram.

### ⏰ Ronda diária 11h — 01/09/2026 11:02 (caixa INACESSÍVEL — auth failed)

IMAP imap.secureserver.net recusou login com AS DUAS credenciais do cofre (SMTP_MOKA_PASSWORD e MOKA_SMTP_PASS — ontem 31/08 a mesma chamada funcionava). Hipóteses: senha trocada (cofres desatualizados — Regra 4) ou lock temporário GoDaddy. Não houve martelada (2 tentativas only). **Amanhã re-tenta; se persistir, cobrar o Miguel sobre troca de senha do info@mokareader.com.** Marco do reenvio segue 0 → 4º lembrete diário enviado ao Telegram (SEM afirmar checagem de caixa; incluí a pergunta sobre troca de senha).
