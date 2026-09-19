# Estudo — Sistema de Pontos do Moka (amostra grátis + pacotes)

**Data:** 2026-07-22 | **Para:** decisão do Miguel | **Status:** proposta com custos calculados

---

## 1. O modelo

- **Sem assinatura**: o usuário compra PONTOS e consome por ação
- **Amostra grátis**: convidado recebe código único + senha e **200 pontos**
- **Painel**: saldo + histórico de consumo + compra de pacotes

## 2. Custos reais por ação (APIs, jul/2026)

| Ação | Detalhe técnico | Custo unitário | Preço em pontos |
|---|---|---|---|
| Resumir vídeo 10 min | Transkriptor ~$0,15 + DeepSeek ~$0,002 | ~$0,17 | 30 pts |
| Resumir 1 livro | ~120k tok in + ~2k tok out (DeepSeek/Kimi) | ~$0,05 | 40 pts |
| Traduzir livro inteiro | ~120k in + ~130k out (DeepSeek) | ~$0,20 | 80 pts |
| TTS 10 min de áudio | OpenAI TTS ~10k chars | ~$0,15 | 20 pts |
| TTS premium (ElevenLabs) | ~$3/10min — SÓ no plano pago alto | ~$3,00 | 150 pts |

**Margem por ponto:** se 1 pt = R$ 0,04 ao usuário, custo médio real ≈ R$ 0,008–0,012 → margem 3-5×.

## 3. Amostra grátis (200 pontos)

Uso esperado: 3 vídeos (90) + 2 livros (80) + 1 áudio (20) = 190 pts.
**Custo por convidado: ~$0,75–1,50 (R$ 4–8)** — aceitável como verba de marketing.

Anti-abuso: 1 código por e-mail; opcional CPF/device fingerprint se houver farm de contas.

## 4. LLMs por tarefa

| Tarefa | 1ª escolha | Fallback | Observação |
|---|---|---|---|
| Resumos | DeepSeek V3 | GLM-4.5-flash | melhor custo×qualidade em PT-BR |
| Livro inteiro | Kimi K2 (ctx 1M) | DeepSeek chunked | Kimi lê sem cortar |
| Tradução | DeepSeek V3 (temp 0.3) | Qwen-plus | fiel, não literário demais |
| TTS | OpenAI TTS-1 | Edge-TTS (grátis, qualidade menor) | ElevenLabs só premium |
| Visão (capas) | Gemini 2.5 flash | GPT-4o-mini | já em uso no pipeline |

## 5. Pacotes pagos (sugestão)

| Pacote | Preço | Pontos | Equivale a |
|---|---|---|---|
| Amostra | grátis | 200 | 3 vídeos + 2 livros + 1 áudio |
| Starter | R$ 19,90 | 500 | ~16 vídeos ou 6 livros traduzidos |
| Leitor | R$ 49,90 | 1.500 | ~50 vídeos ou 18 livros traduzidos |
| Premium | R$ 99,90 | 4.000 | + TTS ElevenLabs liberado |

## 6. Componentes a construir

1. **Cadastro/convite**: código único (`MOKA-XXXXX`) + senha; ativação grava 200 pts
2. **Ledger de pontos**: tabela `creditos(user, acao, custo_pts, custo_usd, ts)` — toda ação registra custo real em USD para auditoria de margem
3. **Painel**: saldo grande no topo, histórico, botão comprar (Mercado Pago/Stripe)
4. **Metering no app**: antes de executar, checa saldo; depois, debita e loga
5. **Admin**: relatório de custo real × receita por usuário (para calibrar o preço do ponto)

## 7. Riscos

1. **TTS é o ralo de dinheiro** — limitar no plano grátis (1 áudio) e usar Edge-TTS se estourar
2. **Abuso da amostra** — farms de e-mail descartável; mitigar com device fingerprint
3. **Livro inteiro traduzido é o item mais caro** — capar tamanho (até ~500 páginas) no grátis
