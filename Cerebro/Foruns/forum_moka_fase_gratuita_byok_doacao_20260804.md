# Fórum — Pivô pra FASE GRATUITA (Moka 5.0): tudo BYOK + doação

> Data: 2026-08-04 · Autor: ZCode · Status: ✅ EM PRODUÇÃO (commit `1076c67`, "Moka 5.0")
> Decisão do Miguel (verbatim): "a gente não vai poder começar com esse pago — fase experimental com tudo gratuito; numa segunda etapa a gente cobra só o valor para poder usar o aplicativo, uma taxa para poder usar."

## 1. O que foi decidido

- **Tudo gratuito**, só **BYOK** (a IA roda com a chave do próprio usuário — privacidade BYOK enfatizada: a chave fica criptografada no dispositivo, nunca passa por servidores).
- **Fora toda cobrança:** preços, planos, pontos, checkout Pix, licença de modo avançado, seletor de modelo da casa, gates 401/402 na UI.
- **Rodapé em todas as páginas (12 idiomas):** doação (PayPal pro mundo, Pix pro Brasil) + e-mail `info@mokareader.com` + **Quem Somos**.
- **Help caprichado (12 idiomas):** como pegar a chave de IA (1 min), custo estimado pro usuário, e o aviso de que **vídeo sem legenda precisa de API de transcrição de áudio** (Whisper/OpenAI) — nem toda API de texto serve.
- **Botão esquerdo do topo sempre volta pra capa** (já estava assim — conferido).
- **Fase 2 (futuro):** cobrança de taxa de uso — restaurar da versão paga preservada.

## 2. Backup PRÉ-PIVÔ (segurança primeiro — feito ANTES de mexer)

| Item | Onde |
|---|---|
| Código app (V 4.3, `8be6d63`) | Tag git **`pre-pivot-pago-v4.3`** + zip 9 MB |
| API de pontos + .env + SQLite | `pontos_api_pre_pivot_20260804.tar.gz` (⚠️ contém segredos vivos) |
| Banco ao vivo | backups no próprio servidor (`*.bak_pre_pivot_gratuito_20260804`) |
| **Manifesto completo** | `Moka/backups/MANIFESTO_PRE_PIVOT_PAGO_V4.3_20260804.md` |

## 3. O que foi implementado (Moka 5.0)

- **SettingsForm:** abre direto no BYOK (chave sempre aberta) + bloco da fase gratuita; fora planos/pontos/licença/seletor de modelo da casa.
- **ai-client (livro + vídeo):** sem fallback pro gateway — sem chave, o erro guia pra ⚙️ com o passo de 1 minuto.
- **Transcrição da casa (Transkriptor): DESLIGADA** com flag `MOKA_CASA_TRANSCRICAO=1` pra religar na Fase 2 (código, cache e fila intactos). Vídeo sem legenda → mensagem honesta da fase.
- **ContaButton 🪙:** removido de todas as páginas.
- **Capa + /experimente:** reescritos pra fase gratuita (BYOK + doação). Checkout Pix antigo salvo em `/tmp/experimente_checkout_backup.tsx` + no backup/tag.
- **SiteFooter (novo) + `lib/donate.ts`:** PayPal ativo; **botão Pix ESCONDIDO até o Miguel definir a chave** (`PIX_KEY = ""` — pendência dele).
- **i18n:** 7 chaves novas × 12 idiomas (`free_*`, `byok_*`, `footer_*`).

## 4. O que NÃO foi tocado (de propósito)

- **Gateway da Tencent (pontos_api):** continua rodando intacto (pontos, `/ia/completar`, `/transcricao/job`) — a UI é que parou de chamar. Na Fase 2 é só religar. Conta de teste `zcode.e2e.20260801@gmail.com` (65 pts) preservada.
- **moka-conta.ts / gatewayProvider / MODELOS_CASA:** código dormente no repo (Fase 2).

## 5. Pendências da fase gratuita

- ⚠️ **Chave Pix da doação** — Miguel decide (e-mail/CNPJ/aleatória) → preencher `PIX_KEY` em `apps/web/src/lib/donate.ts` (o botão aparece sozinho).
- Help completo em 12 idiomas (o /ajuda segue em PT no corpo; o bloco BYOK essencial já está em 12).
- **Fase 2:** reativar cobrança (taxa de uso) a partir do backup + tag; decidir destino do Transkriptor grátis×pago e do BYOK (grátis? licença?).
- PWA: usuários presos em versão antiga se recuperam via fix do SW (Moka 4.2) — a versão gratuita chega sozinha em ~24h.

## Registros relacionados

- Backup/manifesto: `Moka/backups/MANIFESTO_PRE_PIVOT_PAGO_V4.3_20260804.md`
- Moka 4.0 (transcrição da casa): `Foruns/forum_moka_video_transcricao_transkriptor_plano_v2_20260801.md`
- Moka 4.1 (modelo da casa): `Foruns/forum_moka_modelo_casa_deepseek_v4_flash_20260801.md`
- D-U-N-S recebido (lojas desbloqueadas): `Foruns/forum_duns_moka_lojas_20260728.md` — ⚠️ nota: a estratégia de lojas pressupunha app pago; a capa TWA agora mostrará a versão gratuita.

## Acréscimo 05/08 — Login Google em destaque (Moka 5.0.1, `f927d66`)

Decisão do Miguel: "deixa o login do Google — é importante, porque aí a pessoa guarda a sua biblioteca… a gente tem acesso ao e-mail pra mandar e-mail depois". **Verdade do sync (verificada em `lib/repository.ts`):**
- **EPUB:** synca TUDO — o livro parseado (texto!) vai no jsonb da tabela `books` → abre em outro aparelho **sem precisar do arquivo** ✅
- **PDF:** synca metadados/progresso/anotações/traduções — o **binário não vai** (re-adiciona o arquivo no outro aparelho, o resto está lá) ⚠️
- **Videoteca:** segue **local** (IndexedDB `moka-video`, sem sync) ⚠️
- **Chaves BYOK:** ficam só no dispositivo (por design, privacidade) ✅
Implementado: `AuthButton` no topbar da capa + linha do benefício em 12 idiomas ("sua biblioteca fica guardada na nuvem e abre em qualquer aparelho").
**E-mail marketing:** todo registro Google cai em `auth.users` (Supabase) com e-mail — exportável pelo dashboard pra campanha. ⚠️ LGPD: incluir linha de consentimento (e-mail pra novidades do Moka) na `/privacidade` ou no primeiro login antes de usar a lista pra marketing.

## Roadmap oficial das fases (registrado 05/08 por Miguel, verbatim)

> "Esse pago a gente vai voltar ele depois — passar por uma fase experimental de teste, que todo mundo conseguir funcionar, que não tiver muita reclamação, que estiver sólido. Aí a gente vai introduzindo pouco a pouco um prêmio. Vai ser a segunda etapa. E depois a gente tem que converter isso tudo pra aquele sistema pra transformar em aplicativo."

- **FASE 1 (AGORA):** experimental GRATUITA total (BYOK) + doação. Objetivo: funcionar pra todo mundo, ficar SÓLIDO, pouca reclamação. Métricas a olhar: usuários ativos, falhas reportadas, custo zero nosso.
- **FASE 2 (depois, quando sólido):** introduzir **prêmio POUCO A POUCO** (a taxa de uso) — restaurando da versão paga preservada (tag `pre-pivot-pago-v4.3` + `MANIFESTO_PRE_PIVOT_PAGO_V4.3_20260804.md` + gateway intacto na Tencent). Introdução gradual: decidir na hora o que é cobrado primeiro (transcrição da casa? IA da casa?).
- **FASE 3 (depois):** **converter pra aplicativo** (TWA/Bubblewrap → Play Store com D-U-N-S ✅ 943494728 no cofre; iOS via Capacitor + build nuvem). O pacote carrega a versão do site da fase vigente.

## Estado dos backups (conferido 05/08)

- Tag git no GitHub: `pre-pivot-pago-v4.3` ✅ (8be6d63)
- Zips locais: V4.3 paga completa, V5.0, V5.1, V5.2 ✅
- Gateway + .env + SQLite: `pontos_api_pre_pivot_20260804.tar.gz` ✅ (⚠️ sensível)
- Manifesto: `MANIFESTO_PRE_PIVOT_PAGO_V4.3_20260804.md` ✅
