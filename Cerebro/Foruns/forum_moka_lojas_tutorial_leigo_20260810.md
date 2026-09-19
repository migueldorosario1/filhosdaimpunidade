# 📱 Fórum — Como colocar o Moka nas Lojas (Play Store + Apple Store)

> **Tutorial em português simples, SEM tecnicismo, pra o Miguel.**
> Criado em 10/08/2026. Atualizado conforme avançamos.
> Irmão: `forum_duns_moka_lojas_20260728.md` (checklist técnico) + `forum_moka_twa_android_play_store_20260807.md` (TWA pronto).

---

## 📖 Primeiro: o que é cada coisa (dicionário do leigo)

### O que é "app de verdade" vs "site"?
- **Site** (mokareader.com): abre no navegador. Qualquer um acessa digitando o endereço.
- **App de verdade**: aparece na **loja** (Play Store / Apple Store). A pessoa clica "Instalar" e o ícone vai pra tela do celular. Mais profissional, mais confiável.

### O que é "Play Console"?
- É o **painel do Google** onde você (desenvolvedor) sobe o aplicativo.
- Site: `play.google.com/console`
- Custa **US$ 25 (uma vez só, pago pra sempre)**.
- É lá que você sobe o arquivo do app, bota a descrição, as screenshots, e o Google aprova e publica.
- O Miguel disse que "já tem um número" — pode ser o número da conta do Play Console (que ele criou pagando os US$25).

### O que é "AAB"?
- É o **arquivo do aplicativo**. Tipo um `.exe` no Windows, mas pra Android.
- A sigla significa "Android App Bundle".
- O Moka já tem esse arquivo **PRONTO**: tá em `Moka-Lab/apps/twa/app-release-signed.aab`
- É esse arquivo que você **faz upload** (sobe) pro Play Console.

### O que é "Play Store"?
- É a **loja de aplicativos do Android**. Onde as pessoas procuram "Moka" e instalam.
- Quando você sobe o AAB no Play Console e o Google aprova, o Moka aparece na Play Store.

### O que é "Apple Store" (App Store)?
- É a **loja de aplicativos do iPhone/iPad**.
- Mais complexa que a Play Store (precisa de Mac, US$99/ano, revisão mais rigorosa).
- O Miguel já tem o D-U-N-S (943494728) que é o primeiro passo.

### O que é "D-U-N-S"?
- É um **número de identificação da empresa** (tipo CNPJ internacional).
- A Apple exige pra criar conta de organização (empresa), não de pessoa física.
- O Miguel JÁ TEM: **943494728** (recebido em 04/08).

### O que é "TWA"?
- Significa "Trusted Web Activity" — é a técnica de **transformar o site em app**.
- O Google abraça o site (mokareader.com) e cria um "casca" que vira app de verdade.
- Não precisa reescrever o app do zero — usa o site que já funciona.

---

## 🟢 PLAY STORE (Android) — Passo a passo

### O que JÁ ESTÁ PRONTO:
1. ✅ **D-U-N-S:** 943494728
2. ✅ **TWA Bubblewrap:** app `com.mokareader.app` versão 5.7.1
3. ✅ **AAB (arquivo do app):** pronto e assinado em `Moka-Lab/apps/twa/app-release-signed.aab`
4. ✅ **Keystore (assinatura digital):** nos cofres
5. ✅ **assetlinks.json:** no ar (faz o Google confiar no app)

### O QUE FALTA (passo a passo):

**Passo 1: Confirmar a conta do Play Console**
- Você precisa ter uma conta em `play.google.com/console`
- Custa US$ 25 (pagamento único)
- O Miguel disse que "já tem um número" — **precisamos confirmar se é a conta do Play Console**
- Se não tem ainda: eu te guio pra criar (leva 5 min)

**Passo 2: Criar o "app" no Play Console**
- Dentro do Play Console, clica em "Criar app"
- Nome: **Moka**
- Tipo: **Aplicativo**
- Gratuito ou pago: **Gratuito**

**Passo 3: Fazer upload do AAB**
- No Play Console, vai em "Versões de produção" → "Criar versão"
- Clica em "Fazer upload" e seleciona o arquivo `app-release-signed.aab`
- O Google processa o arquivo (leva alguns minutos)

**Passo 4: Preencher a ficha do app**
- **Nome:** Moka — Leia qualquer coisa. Entenda tudo.
- **Descrição curta:** Leitor inteligente de livros e vídeos com IA. Traduza, explique, ouça.
- **Descrição longa:** (texto que a gente escreve junto)
- **Categoria:** Education ou Books & Reference
- **Ícone:** 512x512 (já temos)
- **Screenshots:** precisa tirar (do iPad ou emulador)

**Passo 5: Data Safety (segurança dos dados)**
- O Google pergunta que dados o app coleta
- Resposta: o Moka **NÃO coleta dados** (chaves ficam no dispositivo, criptografadas)
- Marcar: "Não coletamos dados"

**Passo 6: Enviar pra revisão**
- Clica em "Enviar pra revisão"
- O Google analisa (1-3 dias)
- Se aprovar: **Moka aparece na Play Store!** 🎉

---

## 🔴 APPLE STORE (iOS) — Passo a passo

### O que JÁ ESTÁ PRONTO:
1. ✅ **D-U-N-S:** 943494728

### O QUE FALTA:
**Passo 1: Apple Developer Program**
- Site: `developer.apple.com/programs`
- Custa **US$ 99/ano**
- Usa o D-U-N-S pra criar como organização (Cafezinho Media Group)

**Passo 2: Build do app pra iOS**
- Precisa de **Mac** (ou serviço de build em nuvem)
- Técnica: Capacitor (transforma o site em app iOS)

**Passo 3: App Store Connect**
- Sobe o app pra revisão da Apple
- A Apple é mais rigorosa que o Google (revisão manual)

**Passo 4: Aprovação e publicação**
- 1-7 dias pra revisão
- Se aprovar: **Moka aparece na App Store!**

---

## 📋 CHECKLIST (o que fazer primeiro)

1. **CONFIRMAR:** Você tem conta no Play Console? Pagou os US$25?
2. Se sim: **qual o número/e-mail** que você usou?
3. Se não: eu te guio pra criar (5 min)
4. Depois: upload do AAB (eu faço por você se tiver acesso SSH)
5. Screenshots: tiramos do iPad

---

## ❓ Perguntas que o Miguel pode ter

**"Preciso de computador?"** → Pra Play Store, não necessariamente (dá pra fazer pelo navegador). Pra Apple Store, sim (precisa de Mac).

**"Quanto custa?"** → Play Store: US$25 (uma vez). Apple Store: US$99/ano.

**"Quanto tempo demora?"** → Play Store: 1-3 dias. Apple Store: 1-7 dias.

**"Aparece como Cafezinho Media Group?"** → Sim, se usar o D-U-N-S da empresa.

**"O app vai funcionar offline?"** → O TWA abre o site (precisa internet pra IA), mas a casca do app funciona sem internet (mostra uma tela de carregamento).
