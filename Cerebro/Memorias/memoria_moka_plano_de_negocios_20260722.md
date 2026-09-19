# 🧠 MEMÓRIA — Plano de Negócios Moka v1 (2026-07-22)

> Pedido do Miguel: custos calibrados por uso (vídeo/livro), preço da assinatura, metas do fundador, trial, proposta pra investidores, página de simulação, estratégia financeira (custódia/moeda) e estudo da Cripto Moca.
> Base: preços oficiais (pesquisa 22/07 em `memoria_moka_pesquisa_ia_fornecedores_20260722.md`). Câmbio ref.: R$ 5,30/US$.

## 1. Custos unitários (calibrados)

### Vídeo de 1,5–2h (pacote completo: transcrição + 5 análises)
| Item | Custo |
|---|---|
| Transcrição 120 min (Groq whisper-turbo $0,0007/min) | US$ 0,084 |
| LLM 5 análises (deepseek-v4-flash, ~140k in + 6k out) | US$ 0,021 |
| **Total** | **US$ 0,105 ≈ R$ 0,56** |
| (se OpenAI gpt-4o-transcribe) | US$ 0,74 ≈ R$ 3,93 |
| **Alavanca:** vídeos COM legenda = transcrição grátis. Custo misto realista ≈ **R$ 0,35/vídeo** | |

### Livro (~350 págs, 500k chars)
| Item | Custo |
|---|---|
| Tradução integral (140k in + 140k out, DeepSeek) | US$ 0,059 |
| Análises/resumos/perguntas (~50k+20k) | US$ 0,012 |
| **Sem voz** | **US$ 0,071 ≈ R$ 0,38** |
| + Voz integral (Google WaveNet $4/1M chars) | +US$ 2,00 → **R$ 10,98** |

## 2. Cenários mensais (custo por assinante)

| Uso | Custo/mês |
|---|---|
| 5 vídeos/dia + 1 livro/semana (sem voz) | US$ 16,10 ≈ **R$ 85** |
| 10 vídeos/dia + 5 livros/semana (sem voz) | US$ 33,12 ≈ **R$ 176** |
| 20 vídeos/dia + 5 livros/semana (sem voz) | US$ 64,70 ≈ **R$ 343** |
| 5 vídeos/dia + 1 livro/semana COM voz integral | US$ 24,70 ≈ **R$ 131** |
| 10 vídeos/dia + 10 livros/semana COM voz integral | US$ 120,65 ≈ **R$ 639** |

**Lição:** os dois motorzinhos de custo são MINUTOS DE TRANSCRIÇÃO (vídeo) e VOZ INTEGRAL (livro). Os tiers limitam exatamente esses dois.

## 3. Trial (custo por usuário de teste)
- **24h** (3 vídeos + 1 livro): **R$ 2,05** — recomendado no lançamento.
- 7 dias (10 vídeos + 2 livros): R$ 6,34 — fase 2, com cartão pré-cadastrado.

## 4. Proposta de tiers (custo ≤ ~45% do preço; margem antes de taxas/gateway ~10%)

| Tier | Preço | Limites | Custo est. | Margem |
|---|---|---|---|---|
| ☕ **Cafezinho** | **R$ 19,90** | 20 vídeos + 3 livros (sem voz integral) | ~R$ 9 | ~55% |
| ☕☕ **Capuccino** | **R$ 44,90** | 50 vídeos + 10 livros + resumo em ÁUDIO dos vídeos | ~R$ 21 | ~53% |
| ☕☕☕ **Família** | **R$ 89,90** | 120 vídeos + 20 livros + 2 livros falados/mês + 3 usuários | ~R$ 55 | ~39% |

Alavancas pra margem: legendas grátis quando há (30-50% dos vídeos), free tier Google TTS (4M chars/mês = 8 livros falados grátis), Batch API 50% off em traduções de livros, créditos startup (Google/Microsoft — 1-2 anos quase grátis).
BYOK continua grátis pra sempre (modo avançado).

## 5. Metas do fundador (break-even e marcos)

- Ops fixa (Vercel/Supabase acima do free + domínio + ferramentas): ~R$ 300-500/mês → **~25 assinantes Cafezinho cobrem**.
- **Marco 1:** 100 assinantes ≈ R$ 2.500 MRR (prova de tração p/ sócios)
- **Marco 2:** 1.000 assinantes ≈ R$ 30.000 MRR (contrata app de loja + voz premium)
- **Marco 3:** 10.000 assinantes ≈ R$ 300.000 MRR (empresa)
- Métrica guia no /socios: MRR estimado = assinantes × preço médio ponderado.

## 6. Proposta aos investidores (estrutura da oferta)

- **Tese:** "Netflix da compreensão" — vídeo de 3h em 1 minuto, livro de 400 págs em áudio/tradução. Dois produtos, um app (Moka 2.0 ✅).
- **Margem de software:** custo R$ 9-55 vs preço R$ 19,90-89,90.
- **Moat técnico:** leitura pelo IP do usuário (contorna bloqueio do YouTube — ninguém mais tem), BYOK privado, 12 idiomas.
- **Oferta:** pré-venda "Sócio-Fundador" (200 vagas, selo + painel /socios com transparência total). Retorno simbólico de comunidade; participação real SÓ via estrutura jurídica (ver §8).
- **Página de simulação (/socios/simulacao — a construir):** sócio informa posição e vê cenários (100/1.000/10.000 assinantes) com MRR, custo, pool e retorno estimado/mês — com disclaimer "projeção, não promessa de rentabilidade".

## 7. Estratégia financeira (custódia e moeda)

- **Brasil:** Mercado Pago (PIX) → liquida em BRL na conta PJ. Separar conta da empresa da pessoal (MEI/CNPJ).
- **Internacional:** Paddle (Merchant of Record) → payout em USD (Payoneer/banco). Moeda de operação: **BRL** (custos são em USD mas pequenos; hedge natural: preço em BRL, custo em USD cai quando o dólar sobe? não — sobe; manter 30% de reserva dos repasses em conta).
- **Reserva:** 30% de todo repasse → conta "custos + impostos" (gateway ~5%, impostos, IA, chargebacks).
- **Chargeback/consumidor:** reembolso 7 dias (CDC) sem burocracia — política clara no /privacidade.

## 8. 🪙 Cripto Moca — estudo de viabilidade (pedido do Miguel)

**Tecnicamente fácil:** token ERC-20/BEP-20/SPL sai em dias (<R$ 2.500 com auditoria básica). **O problema é 100% jurídico:**

- **Valor acoplado a assinantes/investidores = security token.** No Brasil: Lei 6.385/76 + CVM (oferta pública precisa de registro ou plataforma autorizada de equity crowdfunding). Lei 14.478/22 + regras do Banco Central (2024-25): custódia/exchange de cripto exige **autorização de instituição pagadora** — operar sem licença = risco de autuação, bloqueio e crime.
- **EUA/internacional:** SEC (teste de Howey) — vender pra americanos sem registro é pedir problema.
- **Fiscal:** IR sobre ganhos de capital em cripto (15%+), declaração obrigatória (IN 1888).
- **Reputação:** associar o Moka a "token que promete valorização" atrai o público errado e o regulador certo.

**Veredito: NÃO fazer cripto agora.** Custo jurídico real: R$ 50-200 mil + meses + licenças.

**Alternativa que entrega 90% do efeito (legal e simples):**
1. **Pontos Moka** (programa de fidelidade, não-transferíveis): assinante/sócio ganha pontos por mensalidade paga, indicação e marcos; pontos trocam por meses grátis, tiers e brindes. NÃO é dinheiro, NÃO é valor mobiliário (modelo Smiles/loyalty — juridicamente tranquilo com termos claros).
2. Manter painel /socios transparente (já existe ✅) + pré-venda Sócio-Fundador (recompensa, não investimento).
3. Se um dia fizer cripto: via parceiro licenciado, fora do varejo, com advogado especializado — depois da tração.

## 9. Decisões pendentes do Miguel

- [ ] OK nos tiers/preços (§4) ou calibrar diferente?
- [ ] Trial de 24h grátis no lançamento? (recomendo sim, custo R$ 2)
- [ ] Pré-venda Sócio-Fundador: preço (sugestão R$ 299/ano) e brindes?
- [ ] Advogado pra estrutura de retorno dos sócios (equity crowdfunding CVM 88 quando tração).
- [ ] Construir /socios/simulacao depois dos números aprovados.

— ZCode/Kimi, 2026-07-22
