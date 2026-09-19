# Fórum — D-U-N-S do CNPJ para as lojas do Moka (documento de trabalho)

**Aberto em:** 2026-07-28 | **Por:** ZCode/Kimi + Miguel | **Estado:** EM ANDAMENTO
**Tema duplo:** doc-mãe `Cerebro/PLANO_NEGOCIOS_MOKA/documentos/16_lojas_play_store_app_store.md`

## Por que isso existe

Google Play (organização) e Apple (organização) exigem D-U-N-S para as contas de empresa. Com ele: Play pula o teste de 20 testadores/14 dias; Apple publica como "Cafezinho Media Group". É o gargalo de tempo do plano de lojas (doc 16).

## O plano de ação (passo a passo do chat de 28/07)

1. **Consultar se já existe:** https://developer.apple.com/enroll/duns-lookup (ou dnb.com.br)
2. **Pedir (rota rápida Apple, grátis):** https://developer.apple.com/duns → "Request a D-U-N-S Number"
   - Alternativas: dnb.com.br ("Solicite seu D-U-N-S®") · boavistadados.com.br (BvD)
3. **Dados EXATOS do cartão CNPJ** (regra de ouro: sem divergência — é o motivo nº 1 de rejeição):
   - Razão social, CNPJ, endereço completo, telefone, e-mail, CNAE, nº funcionários, faturamento aproximado, nome+cargo do sócio
4. **Espera:** Apple 5–15 dias úteis · D&B/BvD 2–4 semanas · chega por e-mail (9 dígitos)
5. **Ao receber:** registrar aqui + engatilhar Play Console org (US$25) e Apple Developer org (US$99/ano)

## Checklist vivo (marcamos juntos)

- [x] Consulta inicial — FEITA 04/08 (portal Apple, por Miguel com guia do ZCode)
- [⏳] Pedido/informação enviada — 04/08 via **Apple** (resposta: 'We've received your information. Your organization's D-U-N-S Number has been sent to the email address you provided.') → aguardando e-mail em `comercial@ocafezinho.com` (checar SPAM!)
- [x] **Número recebido: 2026-08-04** — guardado no COFRE (`Outros/chaves/agentes_labs/.env.unificado` → `MOKA_DUNS_NUMBER`), NÃO neste fórum
- [ ] Play Console organização verificada
- [ ] Apple Developer organização verificada

## Notas de trabalho

- **2026-07-28 (ZCode):** fórum criado; passo a passo entregue no chat; Miguel juntando dados do CNPJ. Doc de estratégia: doc 16 do PLANO_NEGOCIOS_MOKA.
- Preencher abaixo a cada avanço (quem, o quê, quando).
- **2026-08-04 (ZCode):** fórum COPIADO do local errado (`Projeto Cafezinho Agentes/Foruns/`) pra sede canônica (`Cerebro/Foruns/`) — atualizar daqui pra frente SÓ nesta cópia. Miguel retomou o plano; checklist segue em aberto (pedido ainda não feito).


## Dossiê cadastral (referência pública — cartão CNPJ, usado no pedido)

| Campo | Valor canônico (USAR SEMPRE ASSIM) |
|---|---|
| Razão social | MIGUEL G B DO ROSARIO SERVICOS DE INFORMACOES |
| Nome fantasia | O CAFEZINHO |
| CNPJ | 22.193.457/0001-00 (matriz) |
| Natureza jurídica | 213-5 — Empresário (Individual) |
| CNAE principal | 63.19-4-00 — Portais, provedores de conteúdo e serviços de informação na internet |
| Porte | ME |
| Abertura | 06/04/2015 |
| Endereço | Rua do Resende, 99 — Apto 806, Centro, Rio de Janeiro/RJ, CEP 20.231-091 |
| Telefone | +55 21 2223-2279 |
| E-mail do pedido DUNS | comercial@ocafezinho.com (escolha registrada: domínio do grupo, não do produto) |
| Situação | ATIVA (desde 02/07/2019) |

## Notas de trabalho (continuação)

- **2026-08-04 (ZCode + Miguel):** D-U-N-S **943494728 recebido** via rota rápida Apple (mesmo dia do pedido!). Checklist: consulta ✅ · pedido ✅ · número ✅ (no cofre). **Desbloqueado:** Play Console organização (US$ 25) e Apple Developer organização (US$ 99/ano) — próximos passos do doc 16 (assetlinks.json, ícone 512, screenshots, Data Safety; iOS via Capacitor + build nuvem).
