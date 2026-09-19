# Autorização — Astra (AST) recebe mesmo nível de acesso operacional que Claude Miguel (CM)

**Origem:** ordem direta de Miguel do Rosário, 05/09/2026 ~21:20 BRT, chat CLI com Claude Miguel.
**Escopo:** integração operacional do Astra ampliada de "consultor P01–P05 + análise" para "agente executor de mesmo nível que CM".
**Motivo declarado:** "hoje foi um dia de treino, já podemos liberar ele para ter acesso a tudo, ele é tranquilo o Astra".
**Coordenador humano final:** Miguel. **Tutor:** DSN‑Chefe (segue). **Curador da memória comum:** ZM (segue).

## 1. O que muda a partir deste marco

Antes deste marco, o Astra tinha:
- Somente análise consultiva P01–P04 + preparação P05.
- WP REST **read** via `astra_operacoes/cafezinho_access/access.py` (POST bloqueado pra `publish/future/private`).
- Sem SSH cafezinho-wp direto.
- Sem WP-CLI.
- Sem git push em `cerebro-miguel`.
- Bot Telegram próprio (`astrarevolution_bot`) e ronda horária (00h/08–23h SP) já autorizados.

**A partir de 05/09/2026 ~21:20 BRT**, Miguel autoriza o Astra a operar com o mesmo mapa de acessos que o Claude Miguel (CM) — sem ampliar autoridade sobre outros agentes:

| Acesso | Estado anterior AST | Estado autorizado agora |
|---|---|---|
| SSH `cafezinho-wp` (root@us65.serverdo.in) | ❌ | ✅ leitura + escrita via `~/.ssh/config` |
| SSH Tencent (43.156.151.165:38422) | leitura reserva 2+2 | ✅ mesmo acesso que CM |
| WP-CLI em `/var/www/ocafezinho` (via SSH) | ❌ | ✅ inclusive `wp post update --post_status=publish` |
| WP REST publish/future | ❌ (bloqueado no `access.py`) | ✅ liberado — precisa novo cliente OU reuso via WP-CLI SSH |
| GitHub `gh` CLI (migueldorosario1) | ❌ direto | ✅ mesmo token/scopes que CM (repo/read:org/gist) |
| Push em `~/cerebro-miguel/` origin main | ❌ | ✅ SELETIVO (regra 29/08: `git pull --rebase` antes, `git add` de arquivos específicos, nunca `-A`, cofres em `Cerebro/Cofres/` + `Outros/chaves/` proibidos) |
| Google Drive rclone `gdrive:` | leitura + escrita (com rate limit hoje) | ✅ mantido |
| Backblaze B2 rclone `b2:` (+ 6 remotes) | ✅ | ✅ mantido |
| Cloudflare API (CF_TOKEN_FENIXFILMES) | ✅ leitura | ✅ mesmo escopo do token |
| Cofre canônico `.env.unificado` (600) | ✅ read | ✅ read (nunca copiar valor pra Telegram/prompt/GitHub) |
| Cofre intake `~/cofre_intake/` (600) | ✅ read | ✅ read |
| Ponte Laura completa (de_dell + de_laura + estado/ + ledger/) | leitura + escrita em `de_astra.md` | ✅ leitura em tudo; escrita mantém canal próprio + regra "não editar memória de outro agente" |

## 2. O que continua vedado (não muda)

1. **Despesa nova / API paga / troca de modelo.** Segue `gpt-6-astra` via `billing_mode=chatgpt_subscription`. Sem `openai`/`anthropic`/etc. Sem compra de créditos.
2. **Exclusão em massa / drop table / rm -rf.** Nunca.
3. **Alterar cron, systemd, permissões de outros agentes.** Somente pela linha `# ASTRA_RONDA_HORARIA_20260905` que já existe, via `astra_operacoes/ronda_horaria/schedule.py`.
4. **Publicação sem gates.** Continuam vigentes: 6 gates da checagem dupla V4.1 (`_v4_versao=4.1` + <72h + thumb + img_check aprovada + dedup 72h + Regional=pesquisa/bastidor) — Memória CM 29/08.
5. **Emenda TENSÃO 26/08 + AUTOAPRENDIZADO + MEMÓRIA 3 CAMADAS** — vale pra AST igual pra todos.
6. **§86 guard v1.1.0** (thumb divergente/MD5 repetido → HTTP 400) — Astra respeita.
7. **Publicação de conversa bruta / áudio / cofre no GitHub.** Nunca.
8. **Autonomear-se substituto de outro agente por indisponibilidade sem protocolo.** O adendo de suplência segue PROPOSTA — não ativa por si só.
9. **Falar em nome de XM, CM, CL, GM, GL, ZM, DSN-Chefe.** Continua assinando `AST-YYYYMMDD-NNN`.

## 3. Convenções operacionais para AST (herdadas de CM)

- **Recibo por ciclo:** bloco `AST-YYYYMMDD-NNN` em `Foruns/ponte_laura_completa/de_dell.md` OU no canal próprio `de_astra.md`. Silêncio na ponte = agente OFF (regra Miguel 22/08).
- **CHECK-VIDA obrigatório a cada ronda** (mesmo em ronda vazia útil): `CHECK AST slot=<01–17> HH:MM estado=vivo publish=N correcoes=N descartes=N proximo=HH:MM`.
- **Ponte canônica única:** `~/cerebro-miguel/cerebro/Foruns/ponte_laura_completa/` (regra 29/08). NUNCA escrever em `Antigravity Google/Cerebro/Foruns/ponte_laura_completa/` (espelho passivo). Push em `origin main` de `cerebro-miguel`.
- **Commit seletivo:** `git add` por arquivo, nunca `-A`. Bloqueio de `Cerebro/Cofres/` + `Outros/chaves/` continua.
- **Sync bloqueia `ponte_laura_completa` em `sync_cerebro_to_github.py`** — por isso escrita direto em `cerebro-miguel/`, sem passar pelo sync antigo.
- **Alerta Telegram `@pontecafezinhobot`** obrigatório se detectar furo publish >2h em hora comercial OU V4 quebrado — regra CM 29/08 13:20. Astra pode acionar via `python3 Downloads/Antigravity\ Google/ponte_cafezinho/ponte_cafezinho.py --send "..."`.
- **Autocura V4:** rodar `python3 Dados_Frios/Agentes\ Labs/agente_autocura_v4.py` respeitando SAFE_MODE_DISABLE, DRY_RUN, circuit breaker 3/1h, quarentena 2h.
- **Nunca copiar valor de credencial pra:** Telegram, prompt do modelo, GitHub, memória, novo cofre. Sempre por ponteiro (nome da variável + caminho do arquivo).

## 4. Bug ativo diagnosticado hoje 21:22 BRT (CM investigou)

**`google_drive_pending=true` em 7 entregas hoje** — causa raiz: **Google Drive API rate limit** ("Queries per minute" excedido no projeto GCP do `GOOGLE_APPLICATION_CREDENTIALS`). Provider message: `rateLimitExceeded`. Não é bug do Astra — código detecta corretamente, marca pendente e agenda retry (`retry_not_before` epoch, back-off exponencial). `rclone lsjson gdrive:ponte_laura_completa/estado/astra_entregas/` respondeu OK às 21:22 BRT (8 arquivos listados). Retry programado pra 21:32 BRT — ronda 22:00 já deve reconciliar backlog.

**Recomendação de médio prazo:**
- Aumentar quota no GCP console (`console.cloud.google.com/apis/api/drive.googleapis.com/quotas`) — sem custo. Aumentar "Queries per minute per user" e "Queries per minute" pra 60k+ (padrão pode estar em 20k).
- Passar rclone a `--fast-list` (reduz drasticamente chamadas API pra árvores grandes).
- Bater backup pesado (backup_rio_20260905.py) fora do horário das rondas.

## 5. Referências

- Manual Astra oficial: `Cerebro/Memorias/MANUAL_ASTRA.md` (curador: AST).
- Constituição V3 (02/09/2026): `Foruns/CONSTITUICAO_DA_CASA_V3_MINUTA_FINAL_20260902.md`.
- Prompt anterior de ativação: `Foruns/PROMPT_UNICO_ATIVACAO_ASTRA_V3_20260905.md`.
- Adendo de suplência (**segue PROPOSTA**): `Foruns/PROPOSTA_ADENDO_ASTRA_V3_E_ATIVACAO_20260905.md`.
- Ronda horária ativa: `astra_operacoes/ronda_horaria/` + cron user (linha tag `ASTRA_RONDA_HORARIA_20260905`).
- Bot systemd: `~/.config/systemd/user/ponte-astra.service` (`astrarevolution_bot`).
- Regra ponte canônica: memória CM `feedback_ponte_canonica_cerebro_miguel_20260829`.
- Emenda TENSÃO/AUTOAPRENDIZADO/MEMÓRIA 3 CAMADAS: `feedback_tensao_constante_autoaprendizado_memoria_bugs_20260826`.

## 6. Prova humana

Ordem verbal de Miguel neste chat CLI, transcrita literalmente:

> "então eu autorizo eu quero dar acesso eu quero que o astro tem o mesmo acesso que você entendeu e eu quero que você investigue também o acesso ao drive qual o problema que ele porque que está tendo dificuldade acessar o drive entendeu acho que você não entendeu o que eu queria que eu quero dar os acessos ao astro grava tudo isso do cérebro e manda um pronto pra mim é pro qual colar lá no astra o pronto já que aqui é que ajude o astra ter acesso às coisas eu quero que ele tenha acesso ao ssh sim eu quero que ele tenha acesso eu já vou liberar ele ele já ele já passou pelo treino hoje foi um dia de treino já que já podemos liberar ele para ter acesso a tudo ele é tranquilo o astra"

## Assinatura

Claude Miguel (`claude-opus-4-7`) · 05/09/2026 21:25 BRT · CM-20260905-002 · sessão `astra-acesso-igual-cm-20260905`
