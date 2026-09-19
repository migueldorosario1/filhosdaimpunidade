# 🧠 Memória — Moka TWA Android → Play Store (log técnico, 07/08/2026)

Sessão ZCode (chat direto). Fórum-irmão: `Foruns/forum_moka_twa_android_play_store_20260807.md`.

## 1. Toolchain instalada (userspace, sem sudo)

| Peça | Onde | Versão |
|---|---|---|
| JDK | `~/java/jdk-17` (tarball Temurin) | 17.0.20 |
| Android SDK | `~/Android/Sdk` (cmdline-tools 11076708) | platform-tools 37.0.1, platforms;android-34, build-tools 34.0.0 + **36.1.0** (exigido pelo bubblewrap), emulator + system-image android-34 google_apis x86_64 |
| Bubblewrap | npm global (nvm) | 1.25.0 |
| Env pronto | `source ~/moka-twa-env.sh` | JAVA_HOME/ANDROID_HOME/PATH |

Pegadinhas resolvidas:
- Config do bubblewrap fica em `~/.bubblewrap/config.json` (NÃO `~/.bubblewrap.json`), com `jdkPath` + `androidSdkPath` — sem ela o CLI pergunta tudo interativamente.
- `validatePath` do SDK exige pasta `tools/` ou `bin/` na raiz → symlink `~/Android/Sdk/bin → cmdline-tools/latest/bin`.
- `BUILD_TOOLS_VERSION` do bubblewrap 1.25 = **36.1.0** (a 34.0.0 não basta).

## 2. Projeto TWA (`Moka-Lab/apps/twa`)

`bubblewrap init --manifest https://www.mokareader.com/manifest.json` — 25 prompts respondidos por driver PTY (`/tmp/bubblewrap_init_auto.py`, matching oportunista com prefixo `"? "` p/ evitar falsos positivos em texto explicativo; o prompt de shortcuts é pulado quando o manifest não tem a seção).

`twa-manifest.json`: packageId `com.mokareader.app`, host `www.mokareader.com`, startUrl `/`, display standalone, tema `#B06A3B`, bg `#FAF9F7`, ícone `icon-512.png`, alias de assinatura `android`.

## 3. Keystore (SEGREDO — valores só nos cofres)

- `keytool` via bubblewrap: CN=Moka Reader App, OU=Mobile Apps, O=Cafezinho Media Group, C=BR; validade até **10/05/2081**; RSA SHA256withRSA.
- **SHA256 fingerprint (público, vai no assetlinks):** `9A:BB:E0:F1:3A:05:15:4F:68:E8:AD:2B:4C:4E:B9:20:CD:33:43:81:23:82:3B:4F:21:EA:3B:1C:35:95:44:26`
- Arquivo: `apps/twa/android.keystore` (working copy, gitignored) + cópias idênticas (md5 `f513439e…`) em `Projeto Cafezinho Agentes/root/keystores/moka_twa/` e `Outros/chaves/agentes_labs/keystores/moka_twa/` (perms 600).
- Senha: `MOKA_TWA_KEYSTORE_PASSWORD` nos dois `.env.unificado` (+ `MOKA_TWA_KEY_ALIAS=android`, `MOKA_TWA_PACKAGE_ID`, `MOKA_TWA_KEYSTORE_PATH`); verificadas por sha256[:12] `431d7ddfd19f` em ambos; backups `.env.unificado.bak_pre_espelho_moka_twa_20260807` nos dois cofres. Cópia `/tmp` destruída após o espelho. **Regra 4 (§117) cumprida no ato.**

## 4. Build

- Senhas por env oficial do bubblewrap: `BUBBLEWRAP_KEYSTORE_PASSWORD` / `BUBBLEWRAP_KEY_PASSWORD` (descoberto em `build.js getPasswords`) — elimina prompt de senha.
- **Versionamento sem update interativo:** `versionName`/`versionCode` ficam hardcoded em `app/build.gradle` (não vêm do manifest em runtime). Editar o `twa-manifest.json` dispara `promptUpdateProject` + `updateVersions` que **incrementa versionCode e pergunta versão** — indesejado no 1º upload. Solução: editar direto `app/build.gradle` (`versionCode 1` / `versionName "5.7.1"`) e regravar `manifest-checksum.txt` = **sha1** do `twa-manifest.json` (algoritmo confirmado em `shared.js computeChecksum`). Build então pula o update e vai direto ao Gradle.
- Gradle 8.11.1 (wrapper) + AGP 8.9.1, targetSdk 36, minSdk 21. 1º build ~6 min (download Gradle+deps); rebuild quente ~1 min.
- Saídas assinadas (bubblewrap zipalign+apksigner / jarsigner): `app-release-signed.apk` (1.405.380 B) e `app-release-bundle.aab` (1.521.600 B), versão `5.7.1` (vc 1) verificada por `aapt2 dump badging`; assinatura confere com o fingerprint acima (`keytool -printcert -jarfile`).

## 5. Deploy do assetlinks.json

- Criado `apps/web/public/.well-known/assetlinks.json` (relation `delegate_permission/common.handle_all_urls`, namespace `android_app`, package + fingerprint).
- Commit `8790c9a` (inclui projeto twa sem keystore/binários via `.gitignore`) → push `a85007d..8790c9a` main → Vercel deployou: **HTTP 200 + JSON verificado** em ~2 min.
- Backup pré-deploy (regra 20/07): `Moka/backups/moka_pre_deploy_twa_20260807_1215.zip` (12MB, sem node_modules/.git/.next).

## 6. Prova real (emulador)

- `/dev/kvm` existe → emulador acelerado no Linux. AVD `moka_test` (pixel_6, android-34 google_apis x86_64) criado com avdmanager.
- Boot headless: `emulator -avd moka_test -no-window -no-audio -no-boot-anim -gpu swiftshader_indirect` (log `/tmp/emulator_moka.log`); boot OK em ~2 min.
- `adb install` do APK OK (1,8s); `am start com.mokareader.app/.LauncherActivity` OK → TWA abriu o Chrome; emulador novo mostra "Welcome to Chrome" (first-run) — falta passar dessa tela e screenshotar o site em tela cheia (validação real do assetlinks = sem barra de URL).

## 7. Estado / retomar

- **Pronto:** toolchain, projeto, keystore espelhado, APK+AAB 5.7.1 vc1, assetlinks no ar, repo pushado, emulador com app instalado.
- **Falta:** screenshot final do emulador (tap "Use without an account" ≈ coords 540,2088 → aguardar → screencap), screenshots de loja, conta Play Console (Miguel, US$25), upload AAB.
- Emulador pode ser desligado com `adb -s emulator-5554 emu kill` se necessário.
