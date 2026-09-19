# Fórum — GITHUB_PAT da reportagem multi-IA (05/09/2026)

**Pedido do Miguel (05/09 ~21:2x BRT, chat ZCode):** "estou fazendo uma reportagem usando várias IAs e está juntando tudo no GitHub — confirma se você consegue entrar nesse GitHub pra escrever; guarda isso no Cérebro" + PAT fine-grained entregue no chat.

## Decisões / estado

- ✅ **TOKEN VÁLIDO E COM ESCRITA** — conta `migueldorosario1` (id 63256060), `GET /user` HTTP 200; **31 repositórios visíveis, TODOS com push=True + admin=True** (cafezinho, cafezinho-publicador, globalsouth-v4, moka, moka-ousadia, mundotrilhos-v4, aiatolah, logis, rio-carta, cicero etc.).
- ⏳ **Expira 2026-10-05 23:36 UTC** (token de 30 dias) — renovar até lá.
- 🔐 **Guardado (Regra 4, sem exibir valor):** intake `~/cofre_intake/cofre_intake.env` (nome `GITHUB_PAT_MIGUEL`) + espelho nos 2 cofres locais `.env.unificado` como **`GITHUB_PAT`** (sha8 `5a129c1b`; backups `.bak_pre_github_pat_20260905`; chmod 600; verificação por hash nos 3 destinos).
- **Intocados:** `GITHUB_TOKEN` clássico (`ghp_…esUC`, ecossistema Astro), `GITHUB_TOKEN_AIATOLAH_KIMI` e o OAuth `gho_…` do `gh` CLI (keyring, scopes gist/read:org/repo).
- ⚠️ **O valor trafegou no chat.** Se quiser zerar a exposição: revogar este PAT no GitHub (Settings → Developer settings → Fine-grained tokens) e depositar o substituto via atalho 🔐 Segredo — o rito de rotação é o mesmo da Transkriptor (03/09).

## O que aconteceu / o que falta / o que preciso de você (Miguel)

- **Aconteceu:** acesso confirmado (leitura + escrita + admin nos 31 repos), credencial guardada no intake + 2 cofres, Cérebro registrado (NODO Cofre + ATUALIZACOES + monitor).
- **Falta:** nada bloqueante. Se a reportagem tiver um repo específico, me dizer qual — aí valido um push de verdade nele.
- **Preciso de você:** nada urgente. Opcional: rotação do PAT por ter passado no chat; renovação antes de 05/10/2026.

**Log técnico completo:** `Memorias/memoria_github_pat_reportagem_multiia_20260905.md`.
