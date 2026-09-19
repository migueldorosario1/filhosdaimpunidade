# Fórum — Reforma do agente Kimi busca-imagem (crise "imagem não encontrada" V4)

> **Data:** 2026-08-09 ~03:40–04:20 BRT · **Quem:** ZCode (Qwen 3.8 Token Plan, conversa Vigília) a pedido do Miguel (2 mensagens de voz, ~03:40)
> **Tema duplo:** memória `Memorias/memoria_reforma_agente_kimi_busca_imagem_20260809.md`
> **Status:** ✅ REFORMA APLICADA E TESTADA · backlog em queima via cron (6 itens/30 min)

## O problema (chamado do Miguel)

Miguel recebendo enxurrada de e-mails "🖼️ Kimi: imagem não encontrada" (remetente
info@mokareader.com — só o mensageiro). Correção do Miguel (voz 2): **não é Moka, é O
Cafezinho V4** — postagens sem imagem; alguém já tentou Flickr 6× sem sucesso. Pedidos:
(1) achar as imagens; (2) ampliar catálogo Flickr; (3) ver se o V4 já tem imagens
usáveis; (4) se houver rascunho acumulado, publicar **de forma paulatina**; (5)
**ensinar o sistema a achar imagem pra não repetir**.

## Diagnóstico (raiz)

1. **Guarda fatal (raiz das 64 pendências):** o fallback de `termos_de_busca` devolvia o
   TÍTULO CRU (70 chars) e a guarda anti-INPA (`_match_pessoa`) exigia essa string nos
   metadados → impossível → 100% de falha em manchetes sem nome próprio composto.
2. **Scrape fino:** agente raspava HTML do Flickr SEM API key → metadados ralos (a chave
   oficial `FLICKR_API_KEY` existe nos 2 cofres e nunca era usada).
3. **Apelidos threshold ≥5** excluía nomes de 4 chars (Lira, Cptm) da busca — mas a
   guarda os exigia → impasse.
4. **`flickr_live.py` nunca plugado** — o módulo de contas oficiais (Planos A–D, 18 contas
   NSID) existia no root e o agente não chamava.
5. **MAX_POR_RODADA=3** lento demais pro backlog de 64.

## Decisões / o que foi feito

| # | Mudança | Por quê |
|---|---------|---------|
| D1 | `_termos_pessoa`: guarda só exige nomes próprios reais (sequências de maiúsculas OU tokens isolados ≥4), nunca título inteiro | mata a exigência impossível |
| D2 | Flickr via **API oficial** (`flickr.photos.search`, licença 4,5,7-10, extras description/owner/tags/url_c/z/l) quando há chave; scrape HTML vira fallback | metadados ricos = guarda passa |
| D3 | `buscar_oficiais()` plugando `flickr_live.buscar_foto_oficial` (contas oficiais, Planos A–D, bypass Jaccard p/ contas dedicadas) | catálogo oficial direto da fonte |
| D4 | Expansão EN via Gemini 2.5-flash (fail-silent) quando não há nome composto | casos "China/cães robôs" |
| D5 | Apelidos threshold 5→4; cap de termos 4→5 | Lira/Cptm entram na busca |
| D6 | **Fallback por-token único** após a guarda: se nada sobreviveu, busca tokens isolados ("Lira", "Cptm") em cada fonte | consultas combinadas morrem no AND implícito das fontes |
| D7 | MAX_POR_RODADA 3→6 | queima do backlog (64 pendentes) |
| D8 | `_carregar_env()` lê `.env.unificado` direto (cron não carrega env) | já existia p/ SMTP, generalizado |

## Provas (testes ao vivo 09/08 ~04:00)

| Manchete | Antes | Depois |
|----------|-------|--------|
| Friedrich Merz anuncia pacote de defesa na Alemanha | 0 | 2–5 candidatas |
| China planeja usar cães robôs… | 0 | 2 candidatas (via expansão EN) |
| Tarcísio libera R$ 14 bi para Cptm após greve | 0 | **7 candidatas** (fallback por-token) |
| PF acha Lira, Ramagem e aliados em rancho… | 0 | **12 candidatas** (fallback por-token) |

## Números da auditoria WP (04:05, API controle.ocafezinho.com)

- **590 rascunhos** no total · **388 com imagem** · **202 sem imagem**.
- Dos 202, boa parte é refugo antigo (maio/junho): títulos vazios, "RASCUNHO TESTE
  Codex", "Pauta vetada por violação da linha editorial" — esses não são alvo do agente.
- **Fila ativa do agente: 64 pendentes** (estado.json; 41 já em 6ª tentativa = origem do
  enxurrada de e-mails; alerta dispara na 6ª e a cada 12).

## Publicação paulatina (pedido do Miguel) — JÁ É NATIVA ✅

- Worker NYC `v4_vertical_draft_worker.py`: **"Cria no máximo um draft/hora por
  vertical"** (docstring, design Miguel 27/07) + crons escalonados por vertical.
- §86: post só publica com `featured_media > 0` → rascunho sem imagem NÃO sai; quando o
  agente resolve, o worker publica no ritmo de 1/h/vertical. Não há risco de "entrar tudo
  de uma vez".

## Esclarecimento do Miguel (~04:16, voz): SÓ recentes — rascunho antigo NÃO publica

"Não é pra publicar rascunho antigo, não. Verificar acumulado só das últimas 24 horas."

- **Auditoria 24h (corte 08/08 04:16 BRT):** 49 publicados, **todos com imagem** ✅;
  acúmulo real = **7 posts `pending` sem imagem** (264881 PF/Lira 03:22, 264878 Irã/Ormuz
  03:04, 264874 Lula/TSE 01:53, 264868 Israel/Líbano 00:04, 264846 Mailza/Acre 19:08,
  264812 Cleitinho/MG 13:25, 264785 Fundação FHC 06:54). Drafts 24h = 0; future = 0.
- **Rascunhos antigos (202, mais novo = 31/07) ficam PARADOS:** não entram no pipeline —
  worker NYC `select_candidate` só pega `status='new'` com **frescor máximo**
  (`freshness_hours`, regra do próprio Miguel 28/07, incidente 263234) e o intake já barra
  item velho na entrada. §86 ainda exige imagem p/ publicar.
- Israel/Líbano (264868) já foi RESOLVIDO pela reforma às 04:00 (ouro_97b2bcb30ea2c010);
  PF/Lira (264881) tem 12 candidatas achadas no teste — cron 04:30+ processa.

## Estado da missão

- **Pronto:** reforma completa + testada; cron `*/30` já roda o código novo (python lê o
  arquivo a cada execução); backups `.bak_pre_reforma_20260809` (agente + estado.json).
- **Em curso:** queima do backlog de 64 (6/30 min ≈ 12/h → ~5-6h para zerar; itens que
  continuam impossíveis seguem o desenho: alerta pede dica ao Miguel na 6ª/18ª/…).
- **O que falta:** acompanhar 2-3 rodadas do cron (~04:30, ~05:00) e confirmar RESOLVIDOs
  reais (ingestão Banco Ouro NYC/Tencent/local).
- **O que preciso de você (Miguel):** nada por ora — se algum item específico chegar no
  6º alerta de novo, me diga uma fonte/dica que eu adiciono ao catálogo.

## Registro cruzado

- Bug: `BUG-20260809-KIMI-GUARDA-FALLBACK-FATAL` em `CEREBRO_NODE_BUGS_RESOLVIDOS.md`.
- Linha do tempo: `CEREBRO_NODE_ATUALIZACOES.md`.
- Relacionados: fórum §86 (`forum_sec86_guarda_imagem_obrigatoria_20260730.md`),
  `forum_bug_imagem_v4_orfaos_20260801.md`, `flickr_live.py` (root, não alterado).
