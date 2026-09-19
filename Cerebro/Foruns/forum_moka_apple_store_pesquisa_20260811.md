# 🍎 Fórum — Como lançar o Moka na Apple Store (pesquisa profunda, 11/08/2026)

> Pesquisa completa sobre o processo de publicação do Moka Reader na Apple App Store.
> Criado por ZCode (GLM-5.2) a pedido do Miguel.
> Irmão: `forum_moka_lojas_tutorial_leigo_20260810.md` (Play Store) + `forum_duns_moka_lojas_20260728.md`.

---

## ⚠️ REALIDADE: Apple ≠ Google

Diferente da Play Store (que aceita TWA = embrulho direto do site), a Apple **NÃO aceita TWA**. Precisa embrulhar o site num app nativo iOS usando **Capacitor** (ferramenta que cria uma casca nativa com WKWebView).

A Apple tem a regra **Guideline 4.2 (Minimum Functionality)**: se o app parece só um "site embrulhado" sem funcionalidade nativa, **é rejeitado**. Precisa adicionar valor nativo (notificações, offline, navegação nativa, biometria).

---

## 📋 PASSO A PASSO COMPLETO (8 etapas)

### Etapa 1: Apple Developer Program (US$99/ano)
- Site: `developer.apple.com/programs`
- Miguel JÁ TEM o D-U-N-S: **943494728**
- Cria como **organização** (Cafezinho Media Group)
- Usa o mesmo e-mail que registrou no D-U-NDS
- **Aprovação demora 24-48h** (Apple verifica a empresa)

### Etapa 2: Gerar certificados e provisionamento
- No portal Apple Developer → **Certificates, Identifiers & Profiles**
- Criar:
  - **App ID** (Bundle Identifier: `com.mokareader.app` — mesmo do Android)
  - **Signing Certificate** (Distribution)
  - **Provisioning Profile** (App Store)
- **PREISA DE UM MAC** pra gerar via Xcode (ou usar serviço cloud)

### Etapa 3: Instalar Capacitor no projeto
```bash
npm install @capacitor/core @capacitor/cli
npx cap init "Moka" "com.mokareader.app" --web-dir=apps/web/out
npm install @capacitor/ios
npx cap add ios
npx cap sync
```

### Etapa 4: Abrir no Xcode
```bash
npx cap open ios
```
No Xcode:
- Configurar **Signing & Capabilities** (Team = Cafezinho Media Group)
- Adicionar **App Icons** (já temos 512×512)
- **Launch Screen** (tela de abertura)
- Adicionar plugins nativos (pra passar na 4.2):
  - Push notifications
  - Haptic feedback
  - Status bar config
  - Splash screen

### Etapa 5: Testar num iPhone real
- Conecta iPhone no Mac
- Roda do Xcode pro dispositivo
- Testa offline, login, leitura

### Etapa 6: App Store Connect
- Site: `appstoreconnect.apple.com`
- Criar novo App: **Moka**
- Bundle ID: `com.mokareader.app`
- SKU: `moka2026`
- Idioma principal: **Português (Brasil)**

### Etapa 7: Archive e Upload
- No Xcode: **Product → Archive**
- **Distribute App → App Store Connect → Upload**
- O Xcode empacota e envia pra Apple

### Etapa 8: Preencher metadados na App Store Connect
- **Nome:** Moka
- **Descrição:** (mesma da Play Store)
- **Categoria:** Education
- **Screenshots:** precisa de iPhone (6.7") + iPad (12.9")
- **Política de Privacidade:** `https://www.mokareader.com/privacidade`
- **App Privacy:** "Não coletamos dados"
- **Keywords:** leitor, livros, IA, tradutor, epub, pdf
- **Support URL:** `https://www.mokareader.com/ajuda`
- Enviar pra **Review**

---

## 🚨 RISCO: Guideline 4.2 (Minimum Functionality)

A Apple **rejeita** apps que são "só um site embrulhado". Pra passar:

| O que o Moka JÁ TEM (ajuda) | O que PRECISA adicionar |
|---|---|
| ✅ Offline (service worker + cache) | Push notifications (nativas) |
| ✅ Login (Google/e-mail) | Haptic feedback |
| ✅ Funcionalidade real (não é só conteúdo) | Status bar nativa |
| ✅ Não usa chrome/browser UI | Splash screen nativa |
| ✅ Funciona independente do site (PWA completo) | Talvez: Share extension |

**Estratégia:** o Moka já tem funcionalidade real (leitor, IA, tradução, voz). Não é "só um site" — é uma ferramenta. Com Capacitor + plugins nativos, **deve passar na revisão**.

---

## 💻 PROBLEMA: Precisa de Mac

O Xcode SÓ roda em macOS. Opções:

### Opção A: Comprar/alugar um Mac
- Mac Mini M2: ~US$600 (mais barato)
- Aluguel cloud: MacStadium / MacInCloud (~US$30-50/mês)

### Opção B: Serviço cloud de build
- **GitHub Actions** com runner macOS (grátis até 2000 min/mês)
- **Bitrise** (CI/CD pra mobile)
- **Codemagic** (CI/CD pra Flutter/Capacitor)

### Opção C: PWABuilder (Microsoft)
- Site: `pwabuilder.com`
- Cola a URL `mokareader.com`
- Ele gera o pacote iOS automaticamente (Capacitor)
- Baixa, abre no Xcode (ainda precisa Mac) ou usa cloud build

---

## 📊 COMPARAÇÃO: Play Store vs Apple Store

| Aspecto | Play Store ✅ | Apple Store ⏳ |
|---|---|---|
| Tecnologia | TWA (Bubblewrap) | Capacitor (WKWebView) |
| Custo | US$25 (uma vez) | US$99/ano |
| Mac necessário? | ❌ Não | ✅ Sim |
| Aprovação | 1-3 dias | 24-48h |
| Revisão | Automatizada | Manual (humano) |
| Rigor | Médio | Alto (4.2 Minimum Functionality) |
| D-U-N-S | Opcional | Obrigatório (já temos) |
| Status | **ENVIADO** | Não começado |

---

## 🗓️ CRONOGRAMA SUGERIDO

1. **Hoje:** Play Store em análise ✅
2. **Esta semana:** Esperar aprovação Google
3. **Próxima semana:** Decidir Mac (comprar/alugar/cloud)
4. **Semana 3:** Apple Developer Program (US$99)
5. **Semana 3-4:** Capacitor setup + plugins nativos
6. **Semana 4:** Build + upload
7. **Semana 5:** Revisão Apple
8. **Semana 6:** Moka na App Store! 🎉

---

## 📚 FONTES

- [Capacitor — Deploying to App Store](https://capacitorjs.com/docs/ios/deploying-to-app-store)
- [PWABuilder — Publish to iOS](https://blog.pwabuilder.com/posts/publish-your-pwa-to-the-ios-app-store/)
- [Apple — Submitting Apps](https://developer.apple.com/app-store/submitting/)
- [Capgo — PWA to Native](https://capgo.app/blog/transform-pwa-to-native-app-with-capacitor/)
- [Reddit — How I put my PWA on App Store](https://www.reddit.com/r/PWA/comments/1ptb14t/)
- [MobiLoud — Publishing PWA](https://www.mobiloud.com/blog/publishing-pwa-app-store)

---

## 📋 DECISÃO DO MIGUEL (11/08 ~02:40)

**Apple Store FICA PARA DEPOIS** — Miguel decidiu adiar porque é caro (US$99/ano + esforço de Capacitor).

**Quando retomar:**
- Miguel tem Mac da esposa + iPhone disponíveis (não precisa comprar)
- O processo tá completo no Cérebro (este fórum)
- Prioridade: Play Store primeiro (já em análise), Apple depois

**Lembrete:** quando o Miguel disser "vamos fazer a Apple", seguir o passo a passo deste fórum. O Mac da esposa resolve o maior obstáculo.
