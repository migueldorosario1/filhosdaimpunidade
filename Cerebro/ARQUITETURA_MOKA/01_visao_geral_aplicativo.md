# 01 — Visão Geral do Aplicativo Moka

## O que o Moka é

**Um leitor com superpoderes**: agrega o conteúdo dos 7 portais temáticos + oferece 2 serviços pagos por pontos, com amostra grátis por convite e plano premium por assinatura.

## Os 2 serviços centrais (o motor de receita)

### 🎬 Serviço de VÍDEO
| Capacidade | Como funciona | Custo/pontos |
|---|---|---|
| Resumir vídeo (YouTube) | Transcrição (Transkriptor) → resumo DeepSeek | 30 pts (~$0,17) |
| Áudio do resumo | TTS OpenAI (premium: ElevenLabs) | 20 pts (~$0,15) |
| *(futuro)* Resumo de live completa | pipeline já existe nos agentes YouTube | — |

### 📚 Serviço de LIVRO
| Capacidade | Como funciona | Custo/pontos |
|---|---|---|
| Resumir livro | Kimi K2 (1M ctx, livro inteiro) ou DeepSeek | 40 pts (~$0,05) |
| Traduzir livro inteiro | DeepSeek temp 0.3, fiel | 80 pts (~$0,20) |
| Áudio (TTS) | OpenAI TTS / ElevenLabs premium | 20–150 pts |

## As camadas do produto

1. **Leitor de notícias** (grátis): feed unificado dos 7 portais + leitura confortável
2. **Amostra grátis**: convite `MOKA-XXXXX` → 200 pontos (cobre 3 vídeos + 2 livros + 1 áudio)
3. **Pontos avulsos**: pacotes R$19,90/500 · R$49,90/1.500 · R$99,90/4.000
4. **Premium (assinatura)**: R$24,90/mês ilimitado (âncora Kindle) + TTS ElevenLabs
5. **Funil**: os 7 portais carregam o banner central do Moka

## Os 7 portais que alimentam o app

riocarta.com (PT) · globalsouth.news (EN) · mundotrilhos.com (PT) · railpost.news (EN) · discoverbrazil.news (EN) · ceara.digital (PT) · aiatolah.com (PT+EN) — todos com GA4 próprio, AdSense, cron 4×/dia.
