# Memória — Vigília temáticos 07/08: verificação interna dos 3 sinais do Claude (todos falsos alarmes)

> **Data:** 2026-08-07 10:20–10:55 BRT · **Autor:** Kimi K3 / ZCode · **Fórum (decisões):** `Foruns/forum_vigilia_tematicos_3_sinais_falso_alarme_20260807.md`
> **Contexto:** Claude (Opus 4.7) roda vigília dos 8 sites temáticos 3×/dia (regra Miguel 04:10 BRT). Na rodada deep das 10:04 levantou 3 sinais e pediu verificação via carta (inbox_trindade/kimi.md + carta no chat). Protocolo cumprido: MONITORAMENTO lido antes (sem conflito de escopo), linha registrada no quadro, verificação com acesso interno.

## Ambiente/método

- SSH aliases usados: `china`/`tencent` (43.156.151.165), `nyc` (198.199.121.136), `root@142.93.48.252` (droplet utilitário). BatchMode, sem senha.
- Repos locais espelho: `Projeto Cafezinho Agentes/sites-v4/{aiatolah,ceara,discoverbrazil,globalsouth,mundotrilhos,riocarta,...}` (git fetch feito; HEAD==origin).
- Snapshot analisado: `Cerebro/monitoramento_horario/vigilia_tematicos/snapshot_2026-08-07_10h_deep.json`.

## Sinal 1 — aiatolah.com "parado há 17 dias" → FALSO ALARME

**O que o Claude viu:** `home_dates: []`, amostra = 2 posts de 21/07 (`/en/posts/20260721-china-s-kimi-k3...`, `20260721-kimi-k3-shakes-markets...`).

**O que existe de verdade:**
- Home ao vivo (`curl https://aiatolah.com/`, 26 KB) contém: `/en/posts/20260807-don-t-be-an-ai-middleman-the-value-is-in-understanding` e `/en/posts/20260807-minimax-h3-arrives-in-comfyui...` (07/08!), mais 05-06/08.
- Estrutura da home (headings): seção **"🎥 Frontier Broadcasts"** no topo = posts YouTube antigos (21/07) — seção fixa/pinada; seção **"📡 Latest Reports"** logo abaixo = posts novos (07/08). O scraper amostrou os 2 primeiros links de posts = Broadcasts. Home não renderiza datas nos cards → `home_dates: []` → ilusão de parada.
- Repo `sites-v4/aiatolah` (origin): commits diários "Refatoracao V4 post: ..." — hoje 03:02/03:03, ontem 13:12/13:13, etc. Engine V4 publicando normal.
- Droplet 142.93.48.252 `/root/aiatolah/`: cron `0 */6 * * * ... aiatolah_agente_youtube.py` (tag `AIATOLAH_YT_CENTRAL_20260806`). Log: "Deploy YouTube executado com sucesso! 🚀" + "Já publicados hoje: 1 vídeos do YouTube. Limite de 1/dia atingido" — publicou hoje ~00:01.
- **Nada a reiniciar. Nenhum cron quebrado.**

## Sinal 2 — "bug de template Astro (hero→logo/fallback) em 4 sites" → FALSO ALARME

**O que o Claude afirmou:** hero renderizado = `/_astro/logo.*` (globalsouth/discoverbrazil/mundotrilhos) e `/images/fallback_ceara.png` (ceara); riocarta correto. **Mas o snapshot dele tem `posts_check: []` vazio nos 4** — a afirmação não consta nos dados coletados.

**Verificação ao vivo (post 07/08 de cada site):**

| Site | 1º `<img>` (header) | 2º `<img>` (hero) | Hero HTTP |
|---|---|---|---|
| ceara.digital | `/_image?href=%2F_astro%2Flogo-transparent...` `.logo-img` | `/hero/anvisa-proibe-ozempic...jpg` c/ `onerror`→fallback | 200 · 241.426 B (= repo) |
| discoverbrazil.news | `/_astro/logo.1T5LZRKl_ZmTeoP.webp` `.logo-img` | `/hero/sao-tome-and-principe...jpg` | 200 · 140.315 B |
| globalsouth.news | `/_astro/logo.BkId3aa-.png` `.logo-img` | `/hero/comoros-moroni...jpg` | 200 · 156.716 B |
| mundotrilhos.com | `/_astro/logo.BiQpVRQA_s2JaM.webp` `.logo-img` | `/hero/hitachi-rail-inicia...jpg` | 200 · 123.179 B |
| riocarta.com (controle) | idem (logo header) | `/hero/rio-rotativo-digital...jpg` | — |

- **Mecânica do erro:** o "logo" é o `<img>` do header (navbar), presente em toda página. Scraper/render que pega o 1º `<img>` reporta "hero = logo". No ceará, o hero tem `onerror="this.src='/images/fallback_ceara.png'"` (rede de segurança); num render com glitch de rede o onerror dispara e o DOM mostra o fallback — mas o arquivo existe (200, 241 KB, byte-idêntico ao repo `public/hero/`, 81 heroes versionados).
- **Layouts `BlogPost.astro` dos 5 repos lidos:** todos com `{heroImage && <img width="1020" height="510" src={heroImage} ...>}` + figcaption `hero_legenda`/`hero_credit`. RioCarta não difere em nada relevante. **Nenhum patch aplicado — nada a copiar do riocarta.**

**Achado real lateral (não é o sinal reportado):** o post ceará da Anvisa (07/08) usa foto de estação de hidratação da Berlin Marathon 2021 (alt em alemão). É erro de SELEÇÃO de imagem do juiz V4 (mesma classe dos casos 06/08 "PF mandados"/"cães vacinação"), não de template. Segue na fila de trocas manuais que aguardam confirmação do Miguel.

## Sinal 3 — railpost.news + mapario.com.br "offline" (2 rodadas) → FALSO ALARME

**Matriz de testes:**

| Origem | railpost.news | mapario.com.br |
|---|---|---|
| Local (PC Miguel) | 1º try: TLS hang no ClientHello → 2º try: handshake OK | 1º try (porta 80, IP .193): sem resposta → depois OK |
| Tencent | 308 → `www.railpost.news` → **200** (0,09s) | 308 → `https://mapario.com.br` → **200** (0,01s) |
| NYC | 308 → 200 (0,08s) | 308 → 200 (0,10s) |
| Droplet 142.93.48.252 | 308 (0,08s) | 200 (0,11s) |

- **DNS mapario:** A = `216.150.16.65` / `216.150.16.193` (authoritative `ns1.vercel-dns.com`, TTL 1800). Parece parking (Voodoo) mas **é range legado da Vercel**: `server: Vercel` no header HTTP; HTTPS no IP direto retorna 200 com cert válido do domínio e cache Vercel (`age:`). 7/7 IPs do pool testados = 200. RDAP registro.br: status active, expiração 2027-03-01, NS = vercel-dns (correto).
- **DNS railpost:** NS GoDaddy (`domaincontrol.com`), A = 76.76.21.21 (Vercel anycast), www → CNAME `cname.vercel-dns.com`. Tudo nominal.
- **Veredito:** servidores/CDN 100% vivos; o timeout intermitente é da **rota local brasileira** (ISP/anycast POP — afeta o observador, não o site). Kuma (droplet, 13 monitores, container saudável 20h up) não apitou.

## Resposta enviada + metodologia proposta

Resposta completa em `Foruns/inbox_trindade/claude.md` (`[KIMI-VIGILIA-TEMATICOS-RESPOSTA-3-SINAIS-RODADA-10H]`, 10:55), incluindo 4 fixes de metodologia p/ a vigília: (1) amostrar ≥3 links de posts, nunca só o topo (seções pinadas); (2) hero check ignorando `.logo-img` e casando src com og:image; (3) timeout/308 → retry `-L` + 2ª rota (SSH/Kuma) antes de alarmar; (4) fallback `onerror` → checar HTTP do `/hero/*.jpg` antes de declarar bug. Recibos v0.1.1: orientado a NÃO emitir (falso positivo de monitoramento ≠ evento de pipeline).

## Estado final

**8/8 sites temáticos VIVOS e publicando às ~10:55 BRT.** Zero ações em produção. Zero patches. Verificação registrada na vigilia do dia (`vigilia_tematicos_2026-08-07.md`) + monitor ✅.
