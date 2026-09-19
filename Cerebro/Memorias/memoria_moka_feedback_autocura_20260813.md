# 🧠 Memória — Moka: sistema FEEDBACK + AUTOCURA de erros (13/08/2026)

**Fórum-irmão:** `Foruns/forum_moka_feedback_autocura_20260813.md`
**Sessão:** ZCode (Kimi K3). Proposta do Miguel.

## Ideia (registrada pra análise, NÃO implementada ainda)

Evoluir o diagnóstico 6.5.1 (botão "copiar", já no ar) pra um recado profissional com:
- Botão **"Enviar diagnóstico"** → e-mail automático pra `info@mokareader.com`.
- **Causas auto-corrigíveis** listadas (com links p/ tutorial).
- **Resposta automática** por e-mail na língua do usuário.
- Especialista com nome localizado ("Zé da Moca" pt-BR, etc.).

## Fatos técnicos relevantes (pra implementação)

- **SMTP GoDaddy já existe e foi testado** (06/08): `SMTP_MOKA_HOST=smtpout.secureserver.net`, `SMTP_MOKA_PORT=465` (SSL), `SMTP_MOKA_USER=info@mokareader.com`, `SMTP_MOKA_PASSWORD` no cofre. E-mail real enviado ao Gmail do Miguel com sucesso. → C1 (enviar diagnóstico) é viável AGORA via rota `/api/report-error` que usa esse SMTP.
- **IMAP GoDaddy** pra ler respostas/inbox: `imap.secureserver.net:993` (mesma senha). → base do C3 (resposta automática).
- Diagnóstico já captura: kind, message, status HTTP, providerDetail, providerId, model, livro, página, textLen, stack, UA, ts, targetLang (`lib/diagnostics.ts`). Falta só: enviar (não só copiar) + mapear status→causa + idioma do recado.
- i18n já existe (`lib/i18n.ts`, `lib/ui-strings.ts`) — o recado e o nome localizado entram lá.
- O app está no ar em **176 países** → o tom/nome precisam funcionar internacionalmente (por isso o C4 importa).

## Decisões pendentes (Miguel)
1. Tom do recado OK?
2. Aprova Fase 1 (C1+C2+C4)?
3. E-mail destino = `info@mokareader.com`?
4. Diagnóstico também pro Supabase (histórico) além do e-mail?
