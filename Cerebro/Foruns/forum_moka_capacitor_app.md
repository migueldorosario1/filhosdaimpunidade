# 📱 Fórum Moka → Aplicativo (Capacitor) — O Desenho e o Material

> Criado 2026-07-20 a pedido do Miguel: "monta o desenho, junta material,
> preços, condições, o caminho mais fácil".
> Companheiro do estudo: `Moka/manifestos/tematicos/CONVERSAO_APP_MOBILE.md`.

---

## 0. A PERGUNTA-CENTRAL (respondida de vez)

> *"Corrijo no site e adapto pro Capacitor depois? Ou corrijo direto no Capacitor?"*

**Resposta: continua corrigindo NO SITE, tranquilamente.** ✅

No desenho escolhido ("shell vivo"), o aplicativo é uma **janela nativa que
carrega o www.mokareader.com**. Toda correção que sobe no site aparece no app
**sozinha, sem republicar nada**. Você só mexe na camada Capacitor quando for
algo ESPECIFICAMENTE nativo (ícone, splash, "abrir com o Moka", plugin de voz).
Ou seja: 95% do trabalho continua sendo no site, como hoje.

## 1. O DESENHO (arquitetura)

```
┌─────────────────────────────────────────────────┐
│  LOJAS                                          │
│  ┌──────────────┐  ┌──────────────┐             │
│  │ Google Play  │  │ App Store    │             │
│  │ (Android e   │  │ (iPhone e    │             │
│  │  XIAOMI*)    │  │ TODOS iPads) │             │
│  └──────┬───────┘  └──────┬───────┘             │
└─────────┼─────────────────┼─────────────────────┘
          │   1 app (AAB)   │   1 app universal
          ▼                 ▼
┌─────────────────────────────────────────────────┐
│  CAPACITOR (shell nativo — WebView)             │
│  capacitor.config.ts:                           │
│    server.url = "https://www.mokareader.com"    │
│  + plugins nativos: Splash, StatusBar,          │
│    Filesystem, Share, (SpeechRecognition iOS)   │
└──────────────────┬──────────────────────────────┘
                   │ https (mesma origem — /api/proxy, /api/tts funcionam)
                   ▼
┌─────────────────────────────────────────────────┐
│  VERCEL: www.mokareader.com (Moka 1.3+)         │
│  Next.js + IndexedDB + IA (BYOK no aparelho)    │
└─────────────────────────────────────────────────┘

* Xiaomi roda Android (MIUI/HyperOS): o MESMO app da Play Store
  funciona em todo Xiaomi. Extra opcional: publicar na GetApps (grátis).
```

**Fluxo de atualização depois do app publicado:**
`corrige no site → git push → deploy Vercel → app já mostra a novidade`
(sem passar pela loja, sem review, sem espera).

## 2. MATERIAL DE CUSTO E CONDIÇÕES (pesquisado 2026-07-20)

| Item | Preço | Condições | Observação |
|---|---|---|---|
| **Capacitor** | grátis | open source (MIT), Ionic Team | sem custo de licença |
| **Google Play Console** | **US$ 25** | pagamento ÚNICO por conta de dev | publica Android + Xiaomi |
| **Apple Developer** | **US$ 99/ano** | assinatura anual | exigido p/ App Store; review 1-3 dias |
| **Xiaomi GetApps** | grátis | conta Xiaomi Dev | opcional (mesmo APK) |
| **GitHub Actions** | grátis p/ repo público | minutos limitados p/ privado | builda Android no ubuntu e iOS no macos-14 |
| **Codemagic** | free tier ~500 min/mês | pago depois | alternativa de CI mobile |
| **EAS Build (Expo)** | ~US$ 29/mês (plano útil) | — | alternativa; Capacitor não precisa |
| **MacStadium/Mac próprio** | US$ 0 se o Miguel já tem Mac | — | iOS exige Xcode (só macOS) |

**Total mínimo pra começar: US$ 25 (só Android). Com iOS: US$ 25 + US$ 99/ano.**
*(Conferir preços na hora da assinatura — podem mudar.)*

## 3. O CAMINHO MAIS FÁCIL (ordem recomendada)

1. **Android primeiro** — builda em Linux ou CI, sem custo de Mac.
   Resultado: app na Play Store cobrindo Android + Xiaomi.
2. **iOS depois** — quando decidir Mac/CI + assinatura Apple.
   Um app "Universal" cobre iPhone e TODOS os iPads.
3. **Lojas extras por último** — GetApps (Xiaomi), APK no site.

## 4. Passo a passo técnico (Etapa 1 — Android)

```bash
# no apps/web do repo (Moka-Lab):
npm i @capacitor/core @capacitor/cli @capacitor/android
npx cap init "Moka" com.mokareader.app
# capacitor.config.ts → server: { url: "https://www.mokareader.com" }
npx cap add android
npx cap sync
# build: Android Studio OU GitHub Actions (ubuntu-latest)
```

Depois: keystore (backup triplo! P5), ficha da Play, screenshots, data-safety
(ponto forte: "chaves de IA ficam no aparelho do usuário"), enviar pra revisão.

## 5. Cuidados já mapeados (do estudo)

- **Keystore Android**: perder = app morre nas lojas. Backup em `Moka/backups/`
  + cofre + 1 lugar do Miguel. SEM EXCEÇÃO.
- **🎤 voz no iOS**: WKWebView não tem SpeechRecognition — no iPhone/iPad o
  ditado por voz precisa de plugin nativo (ou fica "digite a pergunta").
  No Android funciona (WebView Chromium).
- **Foto da página (📸)**: na WebView, salvar arquivo pede
  `@capacitor/filesystem` — entra na fase fina.
- **Service Worker**: já aprendemos hoje — versão do SW precisa subir a cada
  deploy significativo (moka-v4 agora), senão o app/site velho fica preso
  no aparelho. Adicionar bump do SW ao checklist de deploy (Protocolo P6).

## 6. Decisões pendentes do Miguel

1. ☐ Autoriza Etapa 1 (Android) quando quisermos começar?
2. ☐ iOS: tem Mac disponível? Ou CI (GitHub Actions macos-14)?
3. ☐ Assinaturas: Google US$ 25 agora; Apple US$ 99/ano quando for pro iOS?
4. ☐ Nome do pacote: `com.mokareader.app` — ok?

## 7. Log

- **2026-07-20**: fórum criado. Desenho aprovado em rascunho (shell vivo).
  Pergunta-central respondida: corrige no site, app reflete sozinho.
  Enquanto isso: correções seguem no site normalmente (Moka 1.3.1 = SW v4).
