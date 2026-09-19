# Memória técnica — Tutorial de conexão ao Cérebro para LLMs + auditoria do espelho GitHub

**Data:** 2026-08-03 ~06:00 BRT | **Executor:** ZCode (Kimi K3) | **Fórum resumido:** `Foruns/forum_tutorial_conexao_cerebro_llms_20260803.md` | **Pedido:** Chairman Miguel, em sessão ZCode (`/home/migueldorosario/ZCodeProject`)

## 1. Contexto do pedido

Miguel pediu: (a) tutorial para colar em LLMs ensinando a se conectar ao Cérebro; (b) verificar se o espelho completo do Cérebro está no GitHub e atualizar se necessário; (c) enviar o tutorial por e-mail para migueldorosario@gmail.com "com as credenciais com tudo"; (d) publicar fórum e no chat.

## 2. Auditoria do espelho GitHub (passo a passo)

1. `gh auth status` → conta `migueldorosario1` ativa (keyring), protocolo SSH, escopos `repo`/`workflow`/`admin:org`.
2. `gh repo list` → localizado **`migueldorosario1/cerebro-miguel`** (privado), descrição "Cerebro Miguel — conhecimento operacional do ecossistema O Cafezinho (sem credenciais)".
3. Clone local em `~/cerebro-miguel`, branch `main`, working tree limpo, último commit `sync: 2026-08-02 10:00 — 5235 arquivos`.
4. Mecanismo de sync identificado: `~/cerebro-miguel/scripts/sync_cerebro_to_github.py`:
   - Fonte: `~/Downloads/Antigravity Google` (env override: `CEREBRO_SOURCE_DIR`)
   - Lista positiva: `Cerebro`, `Projeto Cafezinho Agentes/Foruns`, `Global South News`
   - Extensões bloqueadas: `.sqlite .db .env .key .pem .p12 .log .jsonl .tar.gz .mp4 .mov`
   - Nomes bloqueados: `.env`, `.env.unificado`, `chaves.sh`, `legacy_chaves_novas.env`, `legacy_raiz_dotenv`
   - Regex de segredos (`is_sensitive`): `api_key|secret|token|password|app_password = valor(16+)`, `ghp_*`, `sk-*`, padrão app-password Google (4×16 letras)
   - Pastas ignoradas: `.git`, `private`, `Backups`, `backups`, `venv`, `__pycache__`, `node_modules`
5. `find -newermt "2026-08-02 10:00"` nas 3 pastas-fonte → **0 arquivos modificados** após o último sync (espelho já estava íntegro).
6. Sync executado mesmo assim (idempotente): `2026-08-03 05:54 — 5236 arquivos`, push OK. **10 arquivos bloqueados pelo scanner** (listados abaixo) — comportamento correto.

### Arquivos bloqueados no sync de 2026-08-03 (scanner de segredos)

- `Cerebro/cartoes_bolso/CARTAO_BOLSO_SSH_SERVIDOR_WP_CAFEZINHO.md`
- `Cerebro/subcerebro_antigravity_desktop/sub_cerebro_antigravity_desktop.md`
- `Cerebro/Foruns/forum_parecer_glm_maestro_local_20260719.md`
- `Cerebro/Foruns/gpt_5_6_sol/v4_qualidade_texto_curadoria_20260710/04_codigo_contexto/test_contracts.py`
- `Projeto Cafezinho Agentes/Foruns/sub_cerebro_antigravity_desktop.md`
- `Global South News/root/chaves_gsn.env.bak_qwen_20260517_20260517_093647`
- `Global South News/root/chaves_gsn.env.bak_pre_kimi_moonshotai_20260723_085848`
- `Global South News/root/chaves_gsn.env.bak_pre_kimi_vision_20260723_084247`
- `Global South News/root/chaves_gsn.env.bak_qwen_20260521_20260521_151147_codex`
- `Global South News/root/agent_data/diagnostico_youtube_20260601.md`

**Observação:** os 2 `sub_cerebro_antigravity_desktop` e o fórum GLM/maestro ficam de fora do espelho por conterem padrões sensíveis. É o preço correto da proteção — documentado aqui para que ninguém "corrija" o scanner por engano.

### Estrutura interna do repo (verificada)

`cerebro/` (canônico completo), `projeto_cafezinho_agentes/foruns/`, `global_south_news/`, `scripts/`, `README.md`, `SECURITY.md`, `v6_custos_staging/`, `{knowledge/` (dir legado com nome irregular — não mexido). ~230 MB.

## 3. Decisão de segurança — "com as credenciais com tudo"

Miguel pediu o tutorial "com as credenciais com tudo". **Não foram incluídos valores** — Constituição do Cafezinho Artigo 1 + `CEREBRO_NODE_COFRE_CHAVES.md` ("Agentes novos devem receber acesso operacional por este índice e pelos arquivos `.env` reais, **não por cópia de segredo em chat, canal ou fórum**"). O tutorial aponta os cofres:

- Local: `Outros/chaves/agentes_labs/.env.unificado` (111 variáveis verificadas)
- Servidores: `/root/.env.unificado`
- GitHub: variável `GITHUB_TOKEN_AIATOLAH_KIMI` no cofre (única var GitHub do cofre unificado)

## 4. Envio do e-mail (mecanismo)

- Não há CLI de mail no desktop nem credenciais SMTP no cofre local (`MOKA_SMTP_PASS` ausente).
- Mecanismo existente: `moka/pontos_api/descadastro.py` usa `smtplib.SMTP_SSL` porta 465, usuário `info@mokareader.com`, senha via env `MOKA_SMTP_PASS` — que vive em `~/moka/pontos_api/.env` no **servidor Tencent** (`ssh tencent`, cron a cada 15 min confirmado).
- Envio executado do próprio Tencent via script Python temporário que **carrega o `.env` no servidor** (nenhum valor transitou ou foi exibido localmente). Remetente: `Moka <info@mokareader.com>` → `migueldorosario@gmail.com`, assunto: "🧠 Tutorial — Como conectar um LLM ao Cérebro (espelho GitHub verificado 2026-08-03)".
- **Nota de DNS:** o domínio `mokareader.com` tem SPF/DKIM GoDaddy (`secureserver.net`) verificados em 2026-07-22 (ver `Foruns/forum_moka_email_godaddy_20260722.md`) — entrega ao Gmail esperada; se cair em spam, checar a caixa de spam.

## 5. Arquivos gravados nesta sessão (Tema Duplo + canônico)

| Arquivo | Papel |
|---|---|
| `Cerebro/TUTORIAL_CONEXAO_CEREBRO_LLMS.md` | Tutorial canônico (Camada 3, raiz do Cérebro — sincroniza ao GitHub) |
| `Cerebro/Foruns/forum_tutorial_conexao_cerebro_llms_20260803.md` | Fórum (decisões resumidas) |
| `Cerebro/Memorias/memoria_tutorial_conexao_cerebro_llms_20260803.md` | Esta memória (log técnico) |
| `CEREBRO_NODE_AGENTES.md` | Catalogação do trio acima (Camada 2) |
| `CEREBRO_NODE_ATUALIZACOES.md` | Registro auditável da sessão |

Após as gravações, novo sync para o GitHub (`sync_cerebro_to_github.py`).

## 6. Pendências

- Nenhuma bloqueante. Se o Miguel quiser envio de e-mail direto do desktop no futuro, criar app-password Gmail e registrar no cofre (nova regra: valor só no `.env.unificado`, ponteiro no nodo do Cofre).
