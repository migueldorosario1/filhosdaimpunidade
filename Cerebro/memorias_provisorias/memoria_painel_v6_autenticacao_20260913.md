# Memória — Painel CCTV V6: Basic Auth — 13/09/2026 (ZCode/GLM-5.3)

Log técnico completo. Decisões: `Foruns/forum_painel_v6_autenticacao_20260913.md`.

## Arquivos tocados

| Arquivo | Ação |
|---|---|
| tencent `/home/ubuntu/cafezinho/v6/painel_cctv_v6.py` | bloco de auth antes do V6Handler + gates em do_GET/do_POST |
| tencent idem `.bak_pre_auth_20260913` | backup (rollback 1 comando) |
| tencent `/home/ubuntu/cafezinho/v6/.painel_auth` | NOVO, 600, USER=/PASS= (creds do Miguel; sem valor aqui) |
| Dell `Projeto Cafezinho Agentes/root/.env.unificado` | + `PAINEL_V6_USER`/`PAINEL_V6_PASS` (após `PAINEL_V6_TOKEN`), `.bak_pre_painelv6auth_20260913` |
| Dell `Outros/chaves/agentes_labs/.env.unificado` | idem espelhado (sha8 dos valores conferido igual nos 2) |
| Cérebro | fórum + esta memória + nodos OBSERVABILIDADE/COFRE_CHAVES/ATUALIZACOES + monitor + ponte de_dell ZM-20260913-002 |

## Código (essência)

```python
PAINEL_AUTH_ARQ = Path(__file__).resolve().parent / ".painel_auth"
def _painel_auth_creds():  # lê USER=/PASS= do arquivo; fallback env PAINEL_V6_USER/PASS
def _checar_basic_auth(handler) -> bool:
    # isentos: path in ("/api/audiencia-receber","/v6/api/audiencia-receber")
    #          local direto: client 127.0.0.1/::1 E sem X-Real-IP
    # comparação: hmac.compare_digest("Basic "+b64(user:pass), header Authorization)
    # falha: 401 + WWW-Authenticate: Basic realm="Painel CCTV V6"
```
Chamado no topo de `do_GET` e `do_POST`: `if not _checar_basic_auth(self): return None`.

## Descobertas de infraestrutura (para futuras sessões)

- **nginx**: `location /v6/` fica em `/etc/nginx/conf.d/painel.conf` (linha ~150), com `X-Real-IP $remote_addr` SEMPRE — é isso que permite distinguir "local direto" de "público via proxy" dentro do serviço. `sites-enabled/cctv` serve outros apps (8091/8082/8083/18081) e NÃO tem o /v6.
- **UFW**: 8084 fechada de fora (só 22/80/8080/38422/5555…) — acesso externo só via nginx :80; a auth no serviço cobre ambos os caminhos de todo jeito.
- **Crons locais que dependem de isenção**: WARM_CACHE (`*/25` → GET /audiencia,/,/baleia) e FAROL_COLETOR (`*/30` → GET /api/farol-coletar, endpoint que já era localhost-only). Ambos provados 200 pós-deploy.
- **Consumidores externos**: só o pusher `/api/audiencia-receber` (token próprio, NYC) — isento e provado (403 do token, não 401 Basic). Demais APIs externas de agentes agora exigem creds (aviso na ponte).

## Provas executadas

- Unitário isolado (exec do bloco extraído): 10/10 cenários.
- Servidor interno: local 200 · X-Real-IP sem creds 401 + WWW-Authenticate · com creds 200 · senha errada 401 · POST pusher 403-token · FAROL cron 200.
- Público: /v6/audiencia sem creds 401 · com creds 200 · senha errada 401 · 8084 direto bloqueado (timeout/000).
- `ast.parse` 3.12 OK antes do cp (padrão: py_compile local 3.10 não serve, PEP 701).

## Lições

- **Proxy nginx + isenção localhost**: NUNCA isentar por `client_address == 127.0.0.1` puro em serviço atrás de proxy local — todo o tráfego público pareceria local. Sempre casar com ausência de `X-Real-IP` (que o nginx injeta) ou equivalente.
- **sync_cerebro_to_github RECUSA worktree sujo** (não-rastreados de outros agentes) — resposta certa é commit cirúrgico dos próprios arquivos + `pull --rebase` + push, nunca limpar/commitar trabalho alheio.
- Pusher com token próprio não precisa de isenção de senha — mas ISOLAR a isenção por rota exata evita brawl de autenticação dupla.

## Estado

- No ar. Falta: agentes externos adotarem as creds (avisados). Troca de senha: editar `.painel_auth` (Tencent) + 2 chaves nos cofres, mesma ação.
