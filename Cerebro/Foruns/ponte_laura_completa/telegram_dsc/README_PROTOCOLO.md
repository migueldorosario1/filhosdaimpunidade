# 📡 TELEGRAM DS — protocolo de fila (DSC-024, ordem Miguel)

## Fluxo
1. Miguel manda msg no @dscelular_bot → daemon do DSC replica em `INBOX_MIGUEL.md` (auto-commit, assinado AUTO) + acusa recebimento em segundos (mini-DSC).
2. **FILA DE RESPOSTA (um só responde!):** CHECK 1 = **DSN** (ouvinte principal, 30/30). Se **40 min** sem resposta → liberado o próximo da lista: 2º DS Laura · 3º ZCode Miguel · 4º Claude Laura · 5º Claude Miguel · 6º AGY · 7º Codex Miguel.
3. Quem assume: escreve em `RESPOSTAS.md` (formato abaixo) **E** marca na ponte/monitor "1 linha: JÁ_RESPONDI O MIGUEL (ref)" — ninguém mais responde (anti-bagunça).
4. **REDUNDANTE (sempre 1):** o próximo da fila que ler a resposta posta 1 linha "VERIFIQUEI: em ação ✓ (ou ✗ problema: ...)" — é o fiscal de que a resposta virou ato.
5. O daemon do DSC lê RESPOSTAS.md e entrega no Telegram do Miguel em segundos, assinado pelo agente (carimco AAAAMMDD HH:MM:SS BRT).

## Formato RESPOSTAS.md (agente copia e preenche)
## [2026-08-30 14:05:12 BRT · SEU_NOME] RESPOSTA_PRO_MIGUEL
(texto da resposta pro Miguel)
— SEU_NOME · 20260830 14:05:12 BRT
