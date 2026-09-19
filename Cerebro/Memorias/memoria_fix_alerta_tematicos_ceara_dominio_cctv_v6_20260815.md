# Memória — Fix alerta temáticos Telegram: Ceará Digital com domínio errado no painel CCTV V6 (15/08/2026)

**Agente:** ZCode (Kimi K3) · **Workspace:** ZCodeProject · **Janela:** 2026-08-15 ~12:44–13:05 BRT
**Gatilho:** Miguel no chat: "chegou mensagem no telegram cafezinhoantigravitybot sobre problemas em alguns sites temáticos. conserta lá e manda outra mensagem para lá"

## Log técnico completo

### 1. Investigação da origem do alerta

- Log da ponte local (`ponte_cafezinho/logs/ponte.jsonl`) não guarda conteúdo de mensagens; janela 11:35–12:29 cheia de `Name or service not known` (soluço DNS local); boot da ponte 12:30.
- Sentinela Temáticos local (`Projeto Cafezinho Agentes/root/ferramentas/sentinela_tematicos/`) é rascunho NÃO deployado — não foi ele.
- Script do relatório 30min (`cctv_relatorio_30min.py`, automation-e3465bb3) não encontrado no Tencent nem localmente; automação criada pela sessão "PAINEL CCTV V6 Loops" (entregue ~12:50).
- Painel CCTV V6 (Tencent `/home/ubuntu/cafezinho/v6/painel_cctv_v6.py`, porta 8084, serviço `cctv-v6.service`) tem página `/tematicos` com health check (`_saude_tematicos()`, cache 5min em `agent_data/cctv/v6/tem_saude.json`).

### 2. Diagnóstico

Health check do painel (12:52): **6/7 online — Ceará Digital "● falha"**.

Causa raiz: dict `TEMATICOS` do painel (linha 1269) usava `"url": "https://www.cearadigital.news"` — domínio previsto em 22/07 que **nunca foi o real** (canônico desde 05/08: `https://ceara.digital`, vide `CEREBRO_INDEX_SATELITES.md`).

Testes (local + Tencent): `www.cearadigital.news` → HTTP 000 (timeout) de ambos; `ceara.digital` → 200 OK de ambos.

Verificação independente dos 8 temáticos do registry do Sentinela (HTTP + frescor de conteúdo):

| Site | HTTP | Último conteúdo |
|---|---|---|
| riocarta.com | 200 | 15/08 (home) |
| mapario.com.br | 200 | 15/08 (sitemap slug) |
| aiatolah.com | 200 | 15/08 (sitemap slug) |
| globalsouth.news | 200 | 15/08 (home) |
| mundotrilhos.com | 200 | 15/08 (home) |
| railpost.news | 200 | 15/08 (sitemap slug) |
| discoverbrazil.news | 200 | 15/08 (sitemap slug) |
| ceara.digital | 200 | 15/08 (home) |

**Nenhum site realmente fora.** Plural do alerta ("alguns sites") provavelmente veio de falhas transitórias de DNS na janela 11:35–12:29 + o falso positivo permanente do Ceará.

### 3. Fix aplicado (Tencent)

```bash
cd /home/ubuntu/cafezinho/v6
cp -a painel_cctv_v6.py painel_cctv_v6.py.bak_pre_ceara_dominio_20260815   # backup
sed -i 's|"url": "https://www.cearadigital.news"|"url": "https://ceara.digital"|' painel_cctv_v6.py
python3 -c "import ast; ast.parse(...)"                                     # sintaxe OK
sudo systemctl restart cctv-v6                                              # active
rm -f /home/ubuntu/agent_data/cctv/v6/tem_saude.json                        # cache saúde
```

Validação: `curl http://127.0.0.1:8084/tematicos` → **7/7 "● online"** (incluindo 🌵 Ceará Digital).

### 4. Resposta ao Telegram (obrigatória — regra 14/08)

- `ponte_cafezinho.py --send` retornou **exit 0 mas NÃO enviou** (DNS local não resolvia `api.telegram.org`; falha silenciosa, sem `tg_send_erro` no jsonl) — **bug da ponte a endurecer**.
- Envio feito pelo fallback documentado (memória `ponte-telegram-resposta-obrigatoria`): socket direto ao IP **149.154.166.110:443** com `server_hostname="api.telegram.org"` (SNI), POST `/bot<TELEGRAM_TOKEN_PONTE>/sendMessage` para `MIGUEL_CHAT_ID` (credenciais lidas do `.env` da ponte, sem exibição). **Confirmado: HTTP 200, `"ok":true`** (~13:00 BRT).

### 5. Arquivos tocados

- Tencent: `/home/ubuntu/cafezinho/v6/painel_cctv_v6.py` (1 linha, URL do slug `ceara-digital`); backup `.bak_pre_ceara_dominio_20260815`; restart `cctv-v6.service`; cache `tem_saude.json` removido.
- Cérebro: fórum `Foruns/forum_fix_alerta_tematicos_ceara_dominio_cctv_v6_20260815.md` + esta memória; linha no `MONITORAMENTO_DE_TRABALHO.md` (✅); catálogo no `CEREBRO_NODE_OBSERVABILIDADE.md` e `CEREBRO_NODE_ATUALIZACOES.md`.

## O que aconteceu / o que falta / o que preciso de você (Miguel)

- **Aconteceu:** alerta diagnosticado como falso positivo (domínio errado no painel), fix aplicado e validado 7/7, 8/8 sites verificados no ar e frescos, resumo enviado ao seu Telegram.
- **Falta:** (a) endurecer `ponte_cafezinho.py --send` para não falhar silenciosamente sem DNS (logar erro ou usar fallback IP+SNI automático); (b) propagar troca de domínio canônico como checklist (painel/sentinela/relatórios) — lição registrada.
- **Preciso de você:** nada agora. Opcional: homologar `http://43.156.151.165/v6/tematicos` (7/7 online).
