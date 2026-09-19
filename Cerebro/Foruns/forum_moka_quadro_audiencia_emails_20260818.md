# Fórum — Moka Reader: quadro da audiência + caixa info@mokareader.com (snapshot)

> Data: 2026-08-18 (tarde) · Autor: ZCode/DeepSeek (sessão "quadro da audiência do moka reader", pedido do Miguel) · Status: ✅ **RELATÓRIO ENTREGUE — snapshot, nenhum código alterado**
> Fontes consultadas: HTML/bundles de mokareader.com, REST Supabase (projeto `nsasbuqeeqdwsagpfpcc`, chave pública do bundle), IMAP GoDaddy (info@mokareader.com), Tencent 43.156.151.165 (`pontos_api`, moka_pontos.db, nginx), Cérebro.

## 1. Quadro da audiência (o que existe de medição hoje)

| Fonte | Estado em 18/08/2026 |
|---|---|
| **GA4 / Plausible / Vercel Analytics no site** | ❌ **NENHUM instalado** — verificado no HTML e nos bundles de mokareader.com (zero tags gtag/plausible/_vercel/insights). |
| **Painel de Sócios (/socios + /api/metrics/summary + ping)** | ⚠️ Código pronto e no ar, MAS as tabelas do Supabase (`metrics_events`, `partners`, `subscriptions` + view `subscriber_count`) **NUNCA foram criadas** — PGRST205 confirmado na REST. O `socios-schema.sql` segue PENDENTE do Miguel desde 01/08 (item 1 do `CEREBRO_INDEX_MOKA_MASTER.md`). Consequência: os pings de visita/instalação (1x/dia por aparelho, via POST /api/metrics/ping) **falham em silêncio** desde sempre → **nenhum número de audiência está sendo registrado no Supabase**. |
| **pontos_api (Tencent :8420, moka_pontos.db)** | 7 usuários cadastrados — **TODOS contas de teste** (migueldorosario, teste.pacotes, gateway.teste, gateway.teste2, tvcafezinho, teste.r10, zcode.e2e; 6 via "compra_r5", 1 convite). 0 logins nos últimos 7 dias. 2 transcrições (01/08, testes). 10 consumos/295 pts. DB parado desde o pivot gratuito (04/08). |
| **Nginx Tencent (rotas /painel e /api/pontos via sslip.io)** | Sem tráfego real do Moka — só scanners (visionheight.com, bots de .env). |
| **Play Store (app TWA)** | App enviado 11/08 (AAB v5.7.1, em análise). Números de instalação/audiência só no Play Console (não acessível daqui). |
| **Contas Google (Supabase auth)** | Quantidade não verificável sem service role key (não está em nenhum cofre). |

**Conclusão do quadro:** a audiência real do Moka Reader **ainda não está sendo medida em nenhum lugar**. Para destravar: (1) rodar `socios-schema.sql` no Supabase (2 min, pendente do Miguel) — liga visitas/instalações do painel; (2) opcional: instalar GA4/Plausible no site para o quadro completo.

## 2. Caixa info@mokareader.com (GoDaddy/Titan — lida via IMAP hoje)

- **INBOX: 21 e-mails · Sent: 1 · Spam/Trash/Archive/Drafts: 0.** Última mensagem: 13/08/2026.
- **Nenhum e-mail de usuário real até agora.** Composição do INBOX:
  - **7 e-mails de sistema:** GoDaddy "novo login" (22/07, 06/08), Titan setup (22/07), GoDaddy "adicione aos dispositivos" (23/07), Gmail confirmação de "enviar como info@" (23/07), **Nubank — finalize o cadastro da chave Pix** (06/08 — chave Pix do info@; status de finalização não verificável daqui), Google Play Console código de verificação (10/08).
  - **3 testes do Miguel** (23/07, teste 2/3/4 — envio/relay SMTP).
  - **8 bounces:** 2 falhas de entrega 28/07 + **6 falhas de entrega em 12/07** — todas do mesmo caso: envio via relay do Moka como `gabrielbarbosa@ocafezinho.com` → `habresult@aol.com` (AOL rejeitou; duplicado em 2 remetentes de bounce: br195.ser... e secureserver).
  - **3 "Moka Diagnóstico" (13/08, todos testes do Kimi):** `teste-envio` ✅ (rota /api/report-error funcionando), `erro` (app v6.6, URL de livro, "nenhum erro capturado nesta sessão"), `teste-painel` (teste de criação de issue no GitHub).

## 3. Estado da missão

- **O que aconteceu:** levantamento completo feito e entregue (este fórum). Fontes: site, Supabase, IMAP, Tencent.
- **O que falta:** (a) rodar o SQL do Supabase — ação do Miguel; (b) decidir se instala GA4/Plausible no Moka; (c) conferir o cadastro da chave Pix no Nubank (e-mail de 06/08 pedia "finalize").
- **O que preciso de você (Miguel):** nada urgente — é um quadro de status. Se quiser medição de audiência funcionando, o passo 1 é o SQL do Supabase (item pendente desde 01/08).


## 🔴 ADENDO 18/08 ~18:30 — GA4 no Moka = PENDÊNCIA URGENTE (ordem do Miguel)

"A gente tem que instalar o ga4 no moka! coloca isso como pendência urgente!" → registrado como urgência máxima em: `CEREBRO_INDEX_MOKA_MASTER.md` §5 (aviso vermelho), `CEREBRO_NODE_SPRINTS_ATIVOS.md` (bloco próprio 🔴), `CEREBRO_INDEX_MOKA_LOG.md` e `CEREBRO_NODE_ATUALIZACOES.md`. Caminho pronto: (1) Miguel cria a propriedade GA4 no console (~2 min) ou autoriza a service account; (2) tag gtag no layout.tsx do Moka-Lab + `NEXT_PUBLIC_GA_MEASUREMENT_ID`; (3) push main → deploy Vercel; (4) validar no Realtime.

**Status 18/08 ~18:50:** tentativa do ZCode de criar a propriedade via Admin API com a service account do Tencent (`google-analytics-admin` instalado) falhou com `UNAUTHENTICATED` na listagem de contas — a SA só tem escopo da Data API do Cafezinho; habilitar o escopo admin exigiria mexer no projeto GCP (não autorizado). **Caminho confirmado: criação manual no console pelo Miguel (~2 min) → colar o G-… no chat → ZCode executa o resto.**

**Status 18/08 ~18:35:** instruções passo a passo com links entregues ao Miguel no chat (criar propriedade 'Moka Reader' na conta do Cafezinho, fuso GMT-3, moeda BRL, fluxo Web `https://www.mokareader.com`). **Aguardando o G-… (ID de medição)** — ao receber, o ZCode executa os passos 2–4.

---
— ZCode/DeepSeek, 2026-08-18
