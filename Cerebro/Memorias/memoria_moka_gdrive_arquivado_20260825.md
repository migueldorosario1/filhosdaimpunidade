# 🗄️ ARQUIVO: integração Google Drive do Moka (encerrada 25/08 — ordem do Miguel)

> **Decisão final (Miguel, 25/08 ~11:00):** "esquece o google drive. Não vamos mexer nisso. Tira o google drive da estante. O usuário vai usar apenas arquivos em seus dispositivos. Essa experiência de bloqueio é muito ruim." → código REMOVIDO por completo (faxina total, `3d8d6fc`). Este arquivo guarda TODO o conhecimento para um eventual retorno (só por Picker verificado, regra de lançamento abaixo). **Não propor o retorno ao Miguel — decisão encerrada.**

## O que foi construído (funcionava tecnicamente)

- **Fluxo legado** (`lib/gdrive.ts`, commit `a584b12`): token Google da sessão Supabase (`provider_token`) + `listDriveBooks` (Drive API v3 `files.list`, PDF/EPUB) + `fetchDriveFile` (`?alt=media`) + `reconnectGoogle` com `scopes: drive.readonly` + `access_type=offline` no signInWithOAuth.
- **Fluxo Picker** (`lib/gdrive-picker.ts`, commit `5eae68c`): Google Identity Services (`initTokenClient`) + Google Picker (janelinha oficial) com escopo LEVE `drive.file` — app só enxerga o arquivo ESCOLHIDO. Ativava com `NEXT_PUBLIC_GOOGLE_CLIENT_ID` (nunca recebeu valor).
- **UI:** botão 📂 na estante (flag privada `NEXT_PUBLIC_GDRIVE`), modal lista/busca/MB/data, tela 🔒 com resposta do Google (diagnóstico 403 visível), crachá 📂 Drive + `sourceOrigin` viajando no jsonb `book` (commits `650cc33`→`3d8d6fc`).
- **Recuperar o código:** `git show a584b12:apps/web/src/lib/gdrive.ts`, `git show 5eae68c:apps/web/src/lib/gdrive-picker.ts`, e a UI na estante em `650cc33`/`b6477d0~1`. As 10 chaves i18n `shelf_gdrive_*` estão em commits ≤ `b6477d0`.

## Por que travou (as 3 paredes, na ordem)

1. **403 insufficient scopes** — login feito sem pedir `drive.readonly` (cura: `scopes` direto no `signInWithOAuth` — supabase-js aceita; campo do dashboard Supabase NÃO é necessário).
2. **403 access_denied "app em fase de testes, só testadores aprovados"** — client OAuth em modo Testing + escopo RESTRITO (`drive.readonly`): só test users liberados pelo dono. Para o próprio Miguel: console Google → tela de permissão → usuários de teste (+ ativar Drive API + origem JS autorizada). Para o PÚBLICO: verificação formal.
3. **Decisão de produto (a parede final):** o público JAMAIS pode ver tela de bloqueio (regra de ouro do Miguel) → beta privado flag → desistência total.

## Se um dia voltar (regra de lançamento do Miguel, 24/08)

1. Via **Picker + `drive.file`** (verificação GRATUITA do Google — `drive.readonly` restrito exige avaliação cara e está descartado);
2. Publicar o app no console Google;
3. Testar com o Miguel no espelho;
4. SÓ ENTÃO expor ao internauta ("primeiro oferecemos a integração oficializada; só depois de confirmada, o usuário integra").
5. Ambiente certo: **Espelho Ousadia** (espelho 2) — nunca no espelho canônico.
