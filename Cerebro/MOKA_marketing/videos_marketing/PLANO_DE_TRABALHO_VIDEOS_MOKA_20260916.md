# 🎬 PLANO DE TRABALHO — SÉRIE DE VÍDEOS MOKA (YouTube + rede)

**Origem:** ordem do Miguel 16/09 ~14:5x — "fiz um vídeo explicando como usar o Moka; vou tentar fazer um vídeo todo dia ou toda semana. Transcreve, faz descrição do YouTube, capa bonita, texto pro Twitter, Instagram, Cafezinho (matéria com vídeo embebado), Facebook, TikTok, e-mail pros leitores. Prepara o plano, reúne as credenciais, prepara os textos — NÃO DISPARA NADA, deixa tudo pronto."

## 1. O formato (série)
- **Episódio 01:** "Como usar o Moka" — vídeo de 20min do próprio Miguel (1280×720), pasta `videos marketing/2026-09-16_01-como-usar-o-moka/`.
- Cadência alvo: 1 vídeo/dia ou 1/semana (o Miguel decide o ritmo; o pipeline abaixo serve para ambos).
- Cada episódio gera UM KIT com 9 peças (ver §3), sempre na mesma estrutura de pasta — replicável por qualquer agente.

## 2. Credenciais (levantadas no cofre unificado — NUNCA exibir valores)
| Canal | Chave no cofre | Estado |
|---|---|---|
| X / Twitter | X_BEARER_TOKEN, X_API_KEY, X_API_KEY_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET | ✅ COMPLETO (OAuth 1.0a + v2) |
| Facebook (página) | FB_PAGE_ID, FB_PAGE_ACCESS_TOKEN | ✅ COMPLETO (Graph API, aceita upload de vídeo) |
| YouTube (canal Moka) | ZCODE_MOKA_YOUTUBE | ✅ existe (é a chave do agente YouTube p/ o canal) — conferir escopo de UPLOAD na hora do 1º disparo |
| Instagram | INSTAGRAM_MAKE_WEBHOOK (+ CREATOMATE_TEMPLATE_ID_INSTAGRAM) | ✅ via webhook Make (postagem) — vídeo vertical renderiza no Criatomate |
| TikTok | — | 🔴 SEM credencial no cofre (criar conta/token ou publicar via Make quando o Miguel quiser) |
| E-mail (leitores Cafezinho) | SMTP GoDaddy (SMTP_MOKA_*) + disparador dispara_onda_moka.py | ✅ pronto (BCC, supressão, trava --vai) |
| Cafezinho (matéria c/ vídeo) | wp-cli cafezinho-wp | ✅ pronto (rascunho + gate editorial) |

## 3. O kit de cada episódio (9 peças — pasta por episódio)
1. `transcricao.md` — transcrição com timestamps (faster-whisper small/pt, CPU, custo zero)
2. `youtube.md` — título (≤70 chars), descrição (com capítulos da transcrição + links), tags, capa
3. `capa_youtube.png` — 1280×720 (frame do app + título grande, paleta da casa)
4. `twitter.md` — fio ou post único (≤280)
5. `instagram.md` — legenda + orientação de corte vertical (Criatomate)
6. `facebook.md` — texto médio p/ página (o vídeo sobe direto, não link)
7. `tiktok.md` — legenda curta + corte vertical
8. `cafezinho.md` — matéria completa (texto maior, vídeo embebado, selo publi Moka, RASCUNHO + gate)
9. `email.md` — minuta curta p/ leitores (padrão BCC da casa)

## 4. Pipeline (ordem de preparo)
áudio (ffmpeg) → transcrição (faster-whisper) → textos (todos de uma vez, da transcrição) → capa (frame+PIL) → kit conferido → AGUARDA "vai" do Miguel (canal a canal ou tudo).

## 5. Rito de disparo (SÓ com "vai" explícito, por canal)
YouTube (upload + capa + descrição) → Cafezinho (rascunho WP + gate editorial, publicação é da esteira) → Facebook (vídeo nativo na página) → X (texto + link do YouTube) → Instagram (Make/vertical) → TikTok (quando houver credencial) → E-mail (dispara_onda, BCC, supressão).

## 6. Regras da casa aplicadas
- NADA dispara sem "vai" (por canal). WhatsApp segue exclusividade do Miguel. E-mail = sempre BCC. Matéria Cafezinho = rascunho + 2 checks. Selo: "Conteúdo produzido pelo Cafezinho para apresentar o Moka, projeto da casa." (quando for publi no portal).

## 7. Estado do episódio 01 (16/09)
- [x] Vídeo recebido (20,2 min) · [x] Áudio extraído · [~] Transcrição rodando (faster-whisper) · [ ] 9 peças · [ ] capa · [ ] conferência do Miguel
