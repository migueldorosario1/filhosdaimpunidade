# 17 — PLANO DE TRABALHO TÉCNICO: Campanha de e-mail + canais do Moka

> Pedido do Miguel (28/07): "recupera o plano de marketing do Cérebro, e faz o plano técnico de como mandar os e-mails — eu uso minhas mãos, mas automatiza tudo que puder." Par: `Foruns/forum_campanha_email_moka_20260728.md`.

---

## 1. O que já existe (não reinventar)

| Ativo | Onde |
|---|---|
| Banco auditado: **1.811 contatáveis** em 4 ondas | `Outros/banco de emails/campanha_moka_2026/onda1_ouro_200.csv` · onda2_quente_500 · onda3_morna_600 · onda4_fria_resto |
| **Lista de supressão** (NUNCA contatar) | `.../supressao_NAO_CONTATAR.csv` |
| Plano de venda direta (funil, contas de CAC) | doc 09 |
| Dossiê de marketing (cards, roteiros, copy) | doc 10 |
| **Fábrica de cupons** (gera MOKA-XXXXX com pontos e lote) | `moka/pontos_api/gerar_convites.py` + endpoint /admin/cupons/gerar |
| SMTP GoDaddy funcionando (info@mokareader.com) | já envia o e-mail de acesso das compras ✅ |
| Loja no ar: /experimente (R$5 teste + R$40 pontos) | mokareader.com |

---

## 2. A OFERTA da campanha (decisão do Miguel)

**Amostra grátis: 50 pontos** (≈ R$ 5 de valor, custo ~R$ 1 pra nós) — dá pra **resumir 1 livro (40 pts) + 1 vídeo (30 pts)** sobrando. E a escada natural:
```
50 pts grátis (cupom)  →  gostou? Teste R$5 = 200 pts  →  pontos a partir de R$40  →  licença R$50/6m
```
Cada onda recebe **um cupom coletivo próprio** (ex.: `MOKA-ONDA1` com 200 usos de 50 pts) — atribuição limpa de conversão por onda no /admin.

---

## 3. COMO MANDAR OS E-MAILS (a parte técnica — realista)

### Limites reais (pesquisa do Miguel respondida)
| Canal | Limite | Nota |
|---|---|---|
| Gmail pessoal (web) | ~500 destinatários/dia | lotes de 200 em BCC de uma vez = risco de spam/bloqueio |
| Google Workspace | ~2.000/dia | idem cuidado com cold list |
| **info@mokareader.com (Titan/GoDaddy)** | ~250–500/dia | SPF/DKIM já verificados ✅ — reputação boa, mas não é ferramenta de bulk |
| Amazon SES / Brevo | milhares/dia | caminho de escala (fase 2) |

### Estratégia recomendada (fase 1 — essa semana)
**Eu automatizo tudo; o Miguel aperta o botão de cada onda.**

1. **Eu preparo** por onda: lista limpa (menos supressão), cupom coletivo da onda (fábrica), texto com nome da pessoa (`Olá, {nome}!`), link com UTM (`mokareader.com/experimente?utm=onda1`).
2. **Envio via SMTP da info@** (a mesma rota que já funciona): **lotes de 40–50 e-mails/hora**, em BCC + 1 cópia visível. Script novo `moka/pontos_api/campanha.py` com: leitura do CSV, filtro de supressão, personalização, envio com intervalo (60–90s entre lotes), log de enviados/erros, e **relatório no Telegram** ao fim de cada lote.
3. **Miguel revisa** o texto e dispara a onda 1 (ouro, 200) no dia escolhido. Primeira onda = teste de fogo de entregabilidade.
4. Métricas em tempo real: cupons resgatados por lote (admin), compras com UTM, bounces.

### Estratégia fase 2 (escala >1.000/semana)
Migrar pra **Amazon SES** (~R$ 0,50/mil e-mails) ou **Brevo** (300/dia grátis): reputação dedicada, unsubscribe automático (obrigatório), webhooks de bounce. Eu preparo a conta; o Miguel só confirma no painel.

---

## 4. A MENSAGEM (minuta base — Miguel edita à vontade)

> **Assunto:** um presente do Moka: resuma um livro inteiro em 2 minutos ☕
>
> Olá, {nome}!
>
> Sou o Miguel, do Cafezinho. Acabamos de abrir o **Moka** — o app que resume vídeos e livros com IA, no seu idioma.
>
> Quero te dar uma amostra de graça: **50 pontos** — dá pra resumir um livro inteiro e um vídeo, sem pagar nada, sem cartão.
>
> 👉 Seu cupom: **{CUPOM}**
> Resgate aqui: mokareader.com/experimente?utm={onda}
>
> Se gostar, o teste de R$ 5 dá mais 200 pontos. Sem pegadinha: os pontos não expiram.
>
> Abraço, e me conta o que achou (é só responder este e-mail),
> Miguel
>
> *(Não quer mais receber? Responde "sai" que eu te tiro da lista.)*

---

## 5. OUTROS CANAIS (a campanha completa)

| Canal | Ação |
|---|---|
| **X/Twitter** | 3 posts com corte 60s do anúncio (R2) + link UTM |
| **Facebook** (grande) | post no perfil + página do Cafezinho; público dos leitores |
| **7 portais** | banner próprio (mídia grátis — doc 09) |
| **YouTube Cafezinho** | vídeo do anúncio (4min07) no canal + comunidade; a esteira de drafts (Claude) inclui o Moka nas pautas |
| **WhatsApp/Telegram** | comunidade mokacomunidade + listas do Miguel |
| **E-mail** | este plano (ondas 1–4) |

---

## 6. MÉTRICAS (o funil medido)

1. Cupom resgatado por onda (/admin, lote)
2. Primeira ação com pontos (consumo no admin por origem)
3. Teste R$5 comprado (UTM ondaX)
4. Pacote R$40+ / licença R$50
5. GA4 events: `cupom_resgatado → primeira_acao → compra_r5 → compra_pontos`

Meta semana 1: onda1 (200) → ≥30 resgates (15%) → ≥5 testes R$5.

---

## 7. PROTEÇÕES

- **Supressão sempre aplicada** (supressao_NAO_CONTATAR.csv em todo envio, sem exceção)
- Linha de descadastro em toda mensagem (verdadeira — quem pedir sai na hora)
- Sem compra de listas, sem anexo, links só mokareader.com
- Bounce alto (>5%) = pausa e revisão da copy antes da próxima onda

## 8. BACKLOG TÉCNICO (ordem)

1. `campanha.py` (ler onda, filtrar supressão, personalizar, enviar lotes via Titan SMTP, log, Telegram)
2. Cupons das ondas: MOKA-ONDA1 (200×50pts), ONDA2 (500), ONDA3 (600), ONDA4 (511)
3. UTM no /experimente (registrar origem na compra)
4. Relatório automático pós-onda no Telegram
5. Fase 2: SES/Brevo quando escalar
