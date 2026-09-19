# 💰 Fórum — Estratégia de Monetização + Unificação Moka (2026-07-22)

> Tema novo: modelo de negócio da família Moka (Reader + Video).
> Memória técnica: `MEMORIA/memoria_moka_monetizacao_unificacao_20260722.md`.
> Nodos: `CEREBRO_INDEX_MOKA_LOG.md`, `CEREBRO_INDEX_LEITOR_VIDEO.md`.

## O problema (diagnóstico do Miguel)

BYOK (usuário cola a própria chave de API) é inegociável pra adoção em massa:
gente normal não tem chave, não confia em colar ("vão entregar minha chave
pra um site desconhecido?"), e DUAS chaves (LLM + Whisper no Video) é demais.
A mensagem "fica no seu aparelho" existe, mas convencer é batalha perdida.

## DECISÕES DO MIGUEL (2026-07-22, via AskUserQuestion)

| Pergunta | Decisão |
|---|---|
| Como receber? | **PIX Mercado Pago (Brasil) + Paddle/LemonSqueezy (internacional, merchant of record cuida de imposto/nota)** |
| O que fica grátis? | **Só BYOK grátis** ("modo avançado" — sem degustação com nossas chaves) |
| Juntar Reader+Video? | **Federar agora (uma assinatura, dois sites), fundir num app só na fase da Play Store/iPhone** |
| O que construir primeiro? | **Preparar terreno**: i18n automático + mensagem de confiança BYOK + página de assinatura com 3 níveis (sem cobrar ainda) |

## Arquitetura aprovada ("Moka Clube")

- **Grátis:** BYOK — a chave da pessoa, no aparelho dela (como hoje).
- **Assinatura (3 níveis ☕/☕☕/☕☕☕):** login Google → usa as NOSSAS chaves no servidor, cota mensal por nível. Transcrição (Whisper) INCLUSA — usuário nunca ouve falar em segunda chave.
- **i18n:** automático por país (x-vercel-ip-country, padrão Aiatolah) + bandeirinhas grandes pra trocar; Reader já tem 12 idiomas, Video ganha o mesmo.
- **Jurídico:** Paddle/LemonSqueezy como MoR resolve a maior parte fiscal global; Brasil via Mercado Pago (avaliar CNPJ/MEI, política de reembolso 7 dias, LGPD).

## Pedidos menores registrados

- Botão "fechar app": PWA não pode se fechar (limitação real); fazer botão "voltar pro início" + dica de gesto do sistema. No app de loja, botão Fechar real.
- Reader no celular: bug do menu de seleção cortando → corrigido V 1.6.3 (quebra em 2 linhas).
- Bug regressão V 1.5 (timer disparando com livro aberto) → corrigido V 1.6.3.

## Próximos passos (ordem aprovada)

1. i18n automático + bandeiras (Video; checar auto no Reader).
2. Mensagem de confiança BYOK em destaque ("sua chave nunca sai do aparelho").
3. Página de assinatura (3 níveis, preços, sem cobrança ainda) nos dois apps.
4. Sprint de pagamento: gateway + cotas no Supabase (sprint separada, com CNPJ/gateway decididos).
5. Fase loja: app único (shell) Reader+Video, botão Fechar real.

— ZCode/Kimi com Miguel, 2026-07-22
