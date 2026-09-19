# Memória — Moka: checkout R$5 Mercado Pago (log técnico completo, 23/07/2026)

**Par:** `Projeto Cafezinho Agentes/Foruns/forum_moka_checkout_mercadopago_20260723.md`

## Contexto

Checkpoint 12 (pré-lançamento) tinha como pendência crítica nº 1: "Checkout R$5: landing /experimente + Mercado Pago + webhook → 100 pontos". A credencial do MP ainda não existe no ecossistema (mapa de credenciais 06: "AINDA NÃO CONFIGURADOS"). Estratégia: construir 100% do código, testar com MP mockado e deixar a ativação depender apenas de colar o token.

## Implementação (moka/pontos_api/app.py)

### Config (env)
- `MP_ACCESS_TOKEN` — access token MP (produção `APP_USR-...` ou teste `TEST-...`)
- `MP_WEBHOOK_SECRET` — assinatura secreta cadastrada no painel MP (vazio = dev, aceita tudo)
- `MOKA_BASE_URL` — URL pública da API; monta `notification_url` do pagamento
- Placeholders comentados criados no fim de `Projeto Cafezinho Agentes/root/.env.unificado`

### Helpers novos
- `_mp_request(metodo, path, payload, idempotency_key)` — stdlib urllib; 503 se sem token; 502 com corpo do erro do MP
- `_valida_assinatura_mp(data_id, x_signature, x_request_id)` — manifesto `id:{data_id};request-id:{x_request_id};ts:{ts};` HMAC-SHA256 vs `v1` (formato oficial MP)
- `_confirmar_compra(con, compra_id, gateway_ref, status)` — lógica de crédito extraída do webhook interno; idempotente
- `_enviar_email_acesso(email, nome, senha, pontos)` — SSH Tencent (`ssh -p 38422 ubuntu@43.156.151.165 "mail -s ..."`), timeout 25s, nunca derruba o fluxo

### Endpoints novos
| Endpoint | Função |
|---|---|
| `POST /compras/criar` | valida pacote (`PACOTES["r5_100"]` = R$5/100pts), cria usuário se novo (senha `secrets.token_urlsafe(9)`, origem `compra_r5`), insere compra pendente, cria pagamento Pix no MP (`payment_method_id: pix`, `external_reference: compra_id`, `X-Idempotency-Key: moka-compra-{id}`), grava `gateway_ref`, dispara e-mail de acesso se conta nova. Retorna qr_code, qr_code_base64, ticket_url, senha_inicial (só conta nova) |
| `POST /webhooks/mercadopago` | valida assinatura, ignora não-payment, busca `/v1/payments/{id}` no MP (fonte da verdade), mapeia status (approved→pago, rejected/cancelled→cancelado, refunded/charged_back→reembolsado, resto→aguardando) e confirma via `_confirmar_compra` |
| `GET /compras/status` | polling do frontend; exige compra_id+email; **reconcilia**: se pendente e há gateway_ref+token, consulta o MP e confirma se approved |
| `GET /` `/experimente` `/painel` | serve a landing e o painel pela própria API (HTMLResponse) |

### Frontend (moka/marketing/experimente.html)
- Botão R$5 abre seção de checkout inline (e-mail + nome)
- `POST /compras/criar` → mostra QR (img base64) + textarea copia-e-cola + botão copiar
- Polling a cada 4s em `/compras/status` → ao `pago`: tela de sucesso com pontos + senha (se conta nova) + link `/painel`
- Erros voltam o botão ao estado inicial

## Testes (12/12 ✅)

Script: `/tmp/teste_checkout_moka.py` (banco temporário, `_mp_request` mockado, envia assinatura HMAC real). Cobertura: páginas estáticas, regressão do convite (200 pts), criar compra (QR+senha+nova_conta), status pendente, webhook aprovado credita, assinatura errada → 401, retry idempotente, saldo 100 no painel, e-mail errado → 404, recompra não recria conta.

## Pendências para ativação (só com o Miguel)

1. Colar `MP_ACCESS_TOKEN` em `.env.unificado` (painel MP → Suas integrações → Credenciais; usar TEST- primeiro para ensaio com usuário de teste)
2. Definir `MOKA_BASE_URL` (a API precisa de URL pública p/ webhook; ngrok/cloudflared serve no lançamento se não houver domínio)
3. No painel MP: cadastrar webhook `{MOKA_BASE_URL}/webhooks/mercadopago` evento `payment` → gerar `MP_WEBHOOK_SECRET`
4. Ensaio: compra com token de teste → conferir QR, aprovação (cartão de teste/status simulado), crédito de 100 pts e e-mail

## Riscos conhecidos

- Sem `MOKA_BASE_URL` o pagamento é criado sem `notification_url` — a reconciliação por polling cobre, mas em produção o webhook é o caminho principal.
- E-mail depende do SSH local → em deploy na nuvem, rodar a API onde houver a chave SSH da Baleia Azul ou trocar por SMTP.
- `senha_inicial` trafega na resposta do checkout (escopada ao comprador); trocar por link mágico pós-lançamento se quiser endurecer.

## Adendo 23/07 ~11:30 — Ensaio real em sandbox ✅

Access Token de teste do Miguel gravado em `.env.unificado`. Compra real criada via API: Pix sandbox emitido (EMV + QR PNG + ticket_url), reconciliação consultou o MP ao vivo ("pendente"), painel OK com senha automática. Aprovação/crédito cobertos pelo E2E mockado. Próximo: credencial de produção + MOKA_BASE_URL + MP_WEBHOOK_SECRET.
