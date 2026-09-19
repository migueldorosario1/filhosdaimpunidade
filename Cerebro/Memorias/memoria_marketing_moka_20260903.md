# 🧠 MEMÓRIA — MARKETING MOKA: PLANO 30 DIAS + RONDA DIÁRIA (03/09/2026)

> Irmã do fórum `Foruns/forum_marketing_moka_20260903.md`. Log técnico completo (Regra do Tema Duplo).

## Arquivos tocados (todos criados nesta sessão; nenhum arquivo pré-existente alterado)

| Arquivo | O quê |
|---|---|
| `MOKA marketing/PLANO_DE_MARKETING_MOKA_20260903.md` | Documento-mestre: produto/6 revolucionices, posicionamento, públicos, canais, calendário 30 dias, minutas e-mail/WhatsApp, spec banners, design robô, métricas, pendências |
| `MOKA marketing/PAUTA_30_MATERIAS_ROBO_MOKA.md` | 30 pautas (título+ângulo+gancho) + regras do robô |
| `MOKA marketing/scripts/captura_prints_marketing.sh` | Capturador: 12 rotas canônico + mokawriter × pc/cel; validador anti-branco (PIL, ≥40 cores); 24/24 OK |
| `MOKA marketing/scripts/gera_banners_moka.py` | Gerador de banners: 3 famílias × 3 formatos; HTML inline + chrome headless screenshot; usa prints relativos `../prints_20260903/` |
| `MOKA marketing/prints_20260903/` | 24 PNGs (12 rotas × 2 tamanhos) — pc_1366x768_* e cel_390x844_* |
| `MOKA marketing/banners/` | 9 PNGs banner_{A_reader,B_video,C_memoria}_{web,story,post} |
| `Cerebro/Foruns/forum_marketing_moka_20260903.md` | Fórum do tema |

## Comandos-chave (reproduzir)

```bash
# prints (2-4 min)
bash "/home/migueldorosario/Downloads/Antigravity Google/MOKA marketing/scripts/captura_prints_marketing.sh"
# banners (~1 min)
cd "/home/migueldorosario/Downloads/Antigravity Google/MOKA marketing" && python3 scripts/gera_banners_moka.py
```

## Provas

- Prints: `MKT_PRINTS: 24 ok / 0 falhas` (log da execução, 15:02-15:03 BRT).
- QA visual (visão): home pc = "página real e bem renderizada", paleta Amanhecer Azul, cards FREE/BYOK; video pc = campo de colar link + cards de features; memoria pc = renderiza com estado vazio (client-side sem sessão).
- Banners: `BANNERS: 9 ok / 0 falhas`; QA visão banner A web = aprovado (layout limpo, contraste alto); banner B story = aprovado com ressalva (CTA ~45px da borda).
- Observação: `/premium` e `/ajuda` retornaram bytes idênticos no canônico (redirect) — flagrado comparando tamanhos de arquivo.

## Lições técnicas

1. **Print de SPA client-side sem sessão** (memoria/harness): página renderiza o shell + "Carregando…" — para material de marketing usar rotas que renderizam server-side completo (home/biblioteca/video) ou sessão real do Miguel.
2. **IAB do ZCode falhou screenshot** ("browser screenshot activity capture failed for guest") — o motor chrome headless CLI da casa (mesmo do moka_prints_ronda.sh) é o caminho provado; não gastar tempo com IAB para capturas em lote.
3. **Read de PNG no ZCode vira upload de CDN** — para QA visual usar analyze_image com a URL do CDN gerada.
4. **Gerador de banners**: HTML com caminho relativo ao print funciona no chrome `--screenshot file://` (sem CORS, sem problema). Emojis renderizam (Noto do sistema). Virtual-time-budget 8000 suficiente.
5. **Detectar redirect por tamanho de arquivo**: capturas com bytes idênticos = mesma página servida — comparar sempre antes de usar print em material.

## Automação criada

- `CronCreate` "Ronda Marketing Moka — ação diária + lembrete" · cron `30 9 * * *` · recurring. Prompt autocontido: monitor → plano (calendário §4) → ação do dia (matéria rascunho/print/banner/minuta/métrica) → Telegram ao Miguel → adendo no fórum + [x] no plano → push Cérebro. Limites: nada externo sem OK do Miguel; matéria = rascunho + gate; sem segredo; datas reais.

## O que aconteceu / o que falta / o que preciso do Miguel

- **Aconteceu:** estudo completo, 24 prints, 9 banners, plano 30 dias, pauta 30 matérias, fórum+memória, ronda diária criada.
- **Falta:** 2 "vais" (onda OURO de e-mail + 1ª matéria); SQL dos sócios; appeal Play Store; sessão Veo (semana 4); cota msmtp.
- **Preciso do Miguel:** os dois "vais" acima — o resto a ronda entrega dia a dia.

— ZM · ZCode/GLM-5.3 · 03/09/2026
