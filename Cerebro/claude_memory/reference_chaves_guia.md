---
name: Onde estão as chaves
description: Mapa de credenciais — diretório central `chaves/` na raiz + canônico vivo no Tencent.
type: reference
originSessionId: 48473406-5e6a-4ebe-826e-53bfe7292cb4
---
## TL;DR
- **Diretório central:** `/home/migueldorosario/Downloads/Antigravity Google/chaves/` — cópias locais centralizadas + `CHAVES_GUIA.md` com mapa completo.
- **Canônico vivo (fonte de verdade):** `/root/.env.unificado` no Tencent (`ssh -i ~/.ssh/id_rsa -p 38422 ubuntu@43.156.151.165 'sudo cat /root/.env.unificado'`).

## Estrutura `chaves/`
- `CHAVES_GUIA.md` — índice mestre.
- `cafezinho_root/` — espelho de `Projeto Cafezinho Agentes/root/` (chaves_novas.env, chaves.sh, client_secret.json, credenciais_personas_sociais.json, codigo_secreto_pkce.txt).
- `agentes_labs/` — espelho de `Agentes Labs/` (.env.unificado, .env_root, chaves_novas.env, chaves.sh).
- `raiz_dotenv` — `.env` da raiz do projeto.
- `backblaze_b2.env` — chave B2.
- `Mayra Google Console/`, `youtube tvcafezinho/` — credenciais OAuth dedicadas.

## Política
- Atualizar PRIMEIRO no Tencent (`/root/.env.unificado`), depois `cp` manual pras cópias locais.
- Cópias estão `chmod 600`. Nunca rsync com `-a`. Nunca commitar.
- `/root/.env_bot` no Tencent é **LEGADO desde 2026-04-08** — ignorar.
