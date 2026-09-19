# 🧠 PLANO DE NEGÓCIOS MOKA — Índice Mestre (cold-start)

> **Comece AQUI.** Este diretório é a casa canônica do plano de negócios do Moka e do resumo da conversa-mãe (20–22/07/2026, ZCode/Kimi + Miguel).

> 🚀 **CHECKPOINT PRÉ-LANÇAMENTO (23/07): o Moka lança neste fim de semana (25–26/07). Leia PRIMEIRO `12_checkpoint_pre_lancamento_20260723.md`.**

> Para continuar o trabalho numa conversa nova: leia este README + `07_proximos_passos.md` e siga os links.

---

## 1. O que este diretório contém

| Arquivo | O que é |
|---|---|
| `documentos/01_plano_negocios_moka.md` | **O plano central**: assinatura R$24,90, capital de 20.000 títulos (0,005%/lucro cada), waterfall, página do investidor (modo real + simulador), arquitetura cripto (títulos contábeis + payout USDC; ⚠️ parecer jurídico antes da 1ª venda) |
| `documentos/02_estudo_sistema_pontos.md` | Custos reais por ação (resumo vídeo $0,17, livro $0,05, tradução $0,20, TTS $0,15), amostra 200 pts = R$4–8/convidado, LLMs escolhidas (DeepSeek/Kimi/GLM/OpenAI-TTS) |
| `documentos/03_schema_pontos_v1.sql` | Banco completo e **validado**: usuarios, convites, carteiras, creditos, consumo, compras, precos_acoes + views (v_saldos, v_margem_usuario, v_custo_diario) |
| `documentos/04_api_pontos_app.py` | **API FastAPI validada 4/4**: resgatar convite, painel/saldo, consumir (com anti-estouro 402), webhook HMAC idempotente. Cópia viva em `Projeto Cafezinho Agentes/moka_pontos/app.py` |
| `documentos/05_apresentacao_ecossistema.html` | Deck de negócios (8 slides, navegável) do ecossistema: 7 portais + Moka |
| `documentos/06_relatorio_email.html` | Versão HTML do plano (já enviada por e-mail ao Miguel em 22/07) |
| `documentos/09_plano_marketing_venda_direta.md` | **PLANO MELHOR (22/07 noite): venda direta** — funil R$5 (100 pts) → assinatura R$24,90, contas de CAC, escada de mídia R$0→R$3.800 até breakeven, arquitetura do checkout Pix. Investidores seguem em paralelo |
| `documentos/10_dossie_marketing_completo.md` | **DOSSIÊ TOTAL**: cards A/B/C com specs, 3 roteiros de vídeo p/ Miguel gravar, copy pronto por canal, landing completa c/ textos, e-mail de acesso, públicos, calendário D1–D15, eventos GA4 |
| `07_proximos_passos.md` | **Backlog priorizado** para a próxima conversa |
| `08_resumo_da_conversa_mae.md` | Tudo que aconteceu na conversa 20–22/07 (refatoração V4, agentes, incidentes, canais) com links para os fóruns |

## 2. Estado do ecossistema (snapshot 22/07 ~19h30)

- **7 portais no ar e atualizados diariamente** (cron 3h/13h + YouTube 2:30/12:30): riocarta.com, globalsouth.news, mundotrilhos.com, railpost.news, discoverbrazil.news, ceara.digital, aiatolah.com. Mapa Rio pausado aguardando conceito.
- **Pipeline V4**: coleta → produção (persona/contrato) → auditoria (valor jornalístico + escopo geográfico) → juiz visual de imagem (Gemini) → dedup/blocklist → publicação git → Vercel → indexação Google.
- **Moka**: schema + API de pontos prontos; plano de capital 20.000 títulos aprovado conceitualmente; próximo: página do investidor.
- **Canais operacionais**: e-mail via SSH Tencent (rota Baleia Azul, testada), 2 bots Telegram sob comando (@cafezinhoantigravitybot, @zizilindav2bot; chat_id 1894890759; ponte `nucleo_telegram.py`).

## 3. Fóruns relacionados (a conversa-mãe completa)

Local: `Projeto Cafezinho Agentes/Foruns/`
- `forum_refatoracao_sistema_sites_tematicos_20260720.md` — fases 0–2 (backup, migração, Vercel, motor V4)
- `forum_sites_um_por_um_aiatolah_riocarta_gsn_20260721.md` — aiatolah/riocarta/GSN um por um
- `forum_sites_tematicos_finalizacao_consolidacao_20260721.md` — consolidação da semana (inclui ERRATA do incidente sites-v4)
- `forum_plano_agente_youtube_cafezinho_v4_20260721.md` — agente YouTube Cafezinho (conceito v2: tese, vilão, momento tenso)
- `carta_para_cloddy_agente_youtube_cafezinho_20260721.md` — esteira: Claude audita e publica os drafts (6h/12h/18h/23h)
- `caderno_erros_teste1_youtube_cafezinho_20260721.md` — 5 erros + 4 regras do 1º teste
- `Cerebro/CEREBRO_INDEX_REFORMA_ARQUIVOS_20260722.md` — reforma 153G→23G + **errata: sites-v4 é dado quente e fica no workspace**

## 4. Regras de ouro deste diretório

1. **Este README é a porta de entrada** — qualquer IA começa por ele.
2. Documentos novos do plano Moka entram em `documentos/` com prefixo numérico e atualizam a tabela acima.
3. O trabalho dos SITES vive nos fóruns (seção 3); aqui mora o NEGÓCIO.
4. Toda mudança de diretriz editorial do Miguel vira regra escrita nos contratos (`agent_data/contratos/`).

## 5. Backup em nuvem
Espelho garantido em **`gdrive:Cerebro_Backups/`** (PLANO_NEGOCIOS_MOKA + ARQUITETURA_MOKA) — sincronizado em 22/07/2026 ~19h40 via rclone. Refazer com:
```
rclone copy "$AG/Cerebro/PLANO_NEGOCIOS_MOKA" gdrive:Cerebro_Backups/PLANO_NEGOCIOS_MOKA
rclone copy "$AG/Cerebro/ARQUITETURA_MOKA" gdrive:Cerebro_Backups/ARQUITETURA_MOKA
```
