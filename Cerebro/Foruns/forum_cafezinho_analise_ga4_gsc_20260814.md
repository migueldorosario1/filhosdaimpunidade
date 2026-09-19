# 📊 FÓRUM — Análise GA4 + Search Console + Vitals do Cafezinho (14/08/2026)

**Tema:** Auditoria de audiência e performance Google (30d + comparativos 7d/30d)
**Autor:** ZCode (GLM-5.3), sessão ZCodeProject
**Status:** ✅ CONCLUÍDA — relatório entregue ao Miguel
**Memória técnica:** `Memorias/memoria_cafezinho_analise_ga4_gsc_20260814.md`
**Dados brutos + relatório:** `Outros/google search/google search/analise_cafezinho_20260814/`

---

## Decisões/resumos (o que importa)

1. **SIM, estamos melhorando no Google** — 30d×30d: cliques web +27,6% (54.518→69.549), impressões +31,6%, posição média 4,55→3,35 (jun 4,19 → ago 3,08). Discover +755% (4.055→34.677 cliques).
2. **GA4 real (sem bots):** usuários +34% (91,6k→122,5k); com bots aparece +64,6%. Sessões +45%, views +50%, engajamento 30,5%→36,2%. Brasil +49%.
3. **FÓRMULA DE AUDIÊNCIA (achado central):** título com **verbo de ação no presente** = 9× mais resultado (score 11.884 vs 1.346); comprimento ideal **55–75 chars**; sweet spot **450–800 palavras** (score 7.575, 69s de leitura); **Economia** tem o melhor score/post (15.838 — viral Moreira/ICL), **Geopolítica** é o motor de volume (10 dos 20 maiores), Eleições 2026 puxa impressões massivas, **Regional (Ceará) estreou bem**.
4. **CWV:** desktop **100% "Bom"** (7.919 URLs, zero problemas em 12/08 — antes 15k melhorias); mobile 58% Bom (9.044) vs <1k em maio; Ruins 1.594→638. CrUX campo da home: LCP 1,6s / CLS 0,002 / INP 161ms — tudo FAST, só TTFB 992ms amarelo.
5. **Discover concentrado:** 90% dos cliques do mês vieram de 3 posts (Moreira 19.458 + China-míssil 6.260 + China-Rússia-Japão 5.402). Semana 07–13/08 caiu −31,5% vs anterior (pico 02/08 no comparativo + delay GSC 12–13/08).

## Problemas achados (com solução proposta — detalhes no relatório)

| # | Problema | Gravidade | Solução proposta |
|---|---|---|---|
| P1 | Bots China inflam GA4 (~28k "usuários", Urumqi+"not set", 6s na home, headless Chrome) | 🔴 | Filtro GA4 country=China + edge rate-limit ASN CN; monitorar share China >2% |
| P2 | Discover dependente de virais (90% em 3 posts) | 🟠 | Cadência diária 2–3 posts formato Discover (China/militar/ciência, imagem ≥1200px, 250–450 pal) |
| P3 | CTR cai (3,27→3,17%) com posição melhorando — queries broad mal convertidas ("bolsa família" 0,8%, "dolar" 0,2%, "pix" 1,3%) | 🟠 | Reescrever título/meta com query literal; landing pages atualizáveis |
| P4 | TTFB ~992ms (único amarelo CrUX home) | 🟡 | Cache edge do HTML; lazy ads (lab TBT 5,4s) |
| P5 | CWV mobile: 5.836 URLs CLS>0,1 + 638 LCP ruim | 🟡 | aspect-ratio nas imagens; fetchpriority na capa; Otimizador SEO no backlog |
| P6 | AMP sem pesquisa aprimorada (CTR 1,79% pos 10 vs 3,29% pos 2,5) + 404s subindo (2.788→3.426) | 🟡 | Validar structured data AMP; redirects 301 das top 404 |

## O que aconteceu / o que falta / o que preciso do Miguel

- **O que aconteceu:** análise completa entregue (GA4 API + GSC API + exports CSV + WP REST + PSI/CrUX), relatório salvo, dados brutos arquivados.
- **O que falta (próximos passos sugeridos):** (1) aplicar filtro GA4 anti-bot China; (2) disparar cadência Discover-friendly no V4/redatores; (3) campanha de otimização CTR para queries broad; (4) continuar faxina CWV mobile.
- **O que preciso do Miguel:** decidir se aplica P1 (filtro China no GA4 — muda o histórico dos relatórios daqui pra frente) e priorizar P2–P3.


---

## 🔬 ADENDO (15/08 ~00:40 BRT) — IDENTIFICAÇÃO DEFINITIVA DO "TRÁFEGO CHINA" = BOT (fingerprint de cliente, sem mexer em nada)

Miguel pediu identificação (não quer filtro). Provas novas:

**GA4 fingerprint do cliente (15/07–13/08, country=China):**
- Dispositivo: desktop 26.937 (95%) · OS: Windows 26.931 (95%)
- **Resolução de tela: 1600×1600 = 26.535 usuários (94%)** — resolução quadrada, default de headless Chrome; inexistente em humanos em massa
- **Versão do browser: Chrome 99.0.4844.51 = 26.027 (92%)** — Chrome 99 é de mar/2022 (4+ anos); nenhuma população real usa versão pinada de 2022
- Duração média 5,9s · engajamento inflado por auto-dismiss
- Contraste Brasil (real): 84% mobile (Android+iOS), duração 68–200s, resoluções diversas de aparelho real

**Nível servidor (access log origin `cafezinho-wp` 190.89.239.65):**
- Site atrás de proxy ServerDo (190.89.239.31/.244, HTTP/1.0) que **descarta X-Forwarded-For** (probe controlado com XFF 203.0.113.99 chegou limpo) e vhost loga formato combined sem IP real
- **Home é cacheada na borda** (probe `/?probe=` não chegou ao origin; `/wp-json/` e 404 chegam) → os hits dos bots na home nem chegam ao origin, logo IP deles só é visível na borda (Cloudflare/proxy) ou no cliente (GA4)
- Sem token Cloudflare no cofre (só R2) → sem acesso a firewall events/bot score da borda

**Conclusão:** bot farm com fingerprint fixo (Windows+Chrome 99+1600×1600), executando JS, concentrado na home. Diagnóstico forense fechado por 2 lados independentes (cliente GA4 + comportamento). Nenhum filtro aplicado (ordem do Miguel).
