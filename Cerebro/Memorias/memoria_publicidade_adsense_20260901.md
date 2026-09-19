# Memória-base do ofício de PUBLICIDADE (DS-N Pub) — AdSense · GAM · redes alternativas

> Criada em 01/09/2026 no nascimento do DS-N Pub (vaga: `Foruns/VAGA_DS_PUBLICIDADE_20260901.md`). Regra da casa: **só aprendizado novo, emendar nunca apagar**. Toda lição nova entra com data + fonte + prova.

## 1. O stack REAL de publicidade da casa (fatos retratados 11/08 — fontes: `Foruns/forum_mapa_ads_canonico_ocafezinho_20260811.md` + `Memorias/memoria_mapa_ads_canonico_ocafezinho_20260811.md`)

| Elemento | Fato VIGENTE | Erro antigo (NÃO usar) |
|---|---|---|
| Motor principal | **GAM (Google Ad Manager)** via plugin ad-inserter; paths `/21715141650,22670554696/ocafezinho.com/...` | publisher `21622511100` NÃO existe (zero ocorrências) |
| Blocos ad-inserter | 90 blocos no total, **19 used, 18 com code**, bloco 14 vazio | "36 ativos" estava errado |
| AMP | ~64% das views; ads = 15 data-slots GAM + 1 mgid (só em `/amp/`) | — |
| Non-AMP | só **Teads** (bloco 17) + 360yield header (`wpc_inner_header_wide_ad`); **18 slots `.ad-space` vazios (LV-006)** | — |
| Plugins ads | `ad-inserter`, `ads-txt`, `insert-headers-and-footers` (inerte) | Quick AdSense/Colabs NÃO EXISTEM |
| ads.txt | 1.902 linhas (01/09/2026) | — |
| Ad Inserter na home | DESLIGADO desde 14/08 | — |
| Temáticos (8) | AdSense **AUTO ADS** `ca-pub-8991943608456423` (conta `aiatolahnews@gmail.com`), sem unidades `<ins>` fixas; `ads.txt` no `public/`; só riocarta veiculou (e foi desligado 22/07 a pedido) | — |
| Tag AdSense canônico | `pub-2441454515104767` (auditoria 16/06) | — |
| Storage perigoso | `wp_options.ad_inserter` formato `:AI:<base64>(serialize)` 49KB | chave com hífen `ad-inserter` não existe |
| Ads injetados via JS pós-HTML | auditoria com `curl` puro NÃO vê anúncios populados (precisa headless) | — |

**Riscos destrutivos (do fórum 11/08, §5/§6):** 🔴 nunca editar `ad_inserter` sem backup DB; 🟡 não renomear divs/IDs/classes de ad; 🟢 mudanças visuais fora desses divs = seguras.

## 2. Fontes de dados do ofício (estado em 01/09/2026)

| Fonte | Acesso | Uso |
|---|---|---|
| Contador nginx (`/root/cafezinho_contador/`, us65; cron 5/5min) | local us65 | régua first-party de audiência (GA4 vê ~26% do contador — relato DS 01/09) |
| GA4 `374552425` | service account (Tencent/Manus; Cafedash) | audiência por página/vertical, 7d/30d |
| REST público WP | aberto | posts novos por ronda (inventário editorial) |
| ads.txt ao vivo | curl | mudança de inventário programático |
| AdSense Management API v2 | **FALTA (Fase 2 VIA A/B)** | receita, RPM, CTR por unidade/dia/hora |
| GAM API (`admanager.readonly`, scope novo 03/2026) | **FALTA** | impressões/receita GAM por slot |
| GA4 "Publisher ads report" (propriedade vinculada) | a verificar na F2 | métricas de anúncio dentro do GA4 |

## 3. Plano de desbloqueio do DINHEIRO (Fase 2 — detalhes na vaga §4)

- **VIA A (recomendada):** e-mail da service account (a mesma do GA4) adicionado como **usuário** nos painéis AdSense (Acesso e autenticação) e GAM (Usuários, papel leitura) → JSON existente passa a valer headless. Referências: AdSense Management API v2 usa OAuth; service account listada como usuário do painel é o caminho sem navegador; GAM ganhou scope somente-leitura dedicado em 03/2026.
- **VIA B (fallback):** OAuth Desktop no Dell (precedente `logis-agenda`, `Outros/chaves/Google Agenda/`), refresh token chmod 600 no cofre, scopes `adsense.readonly`+`admanager.readonly`.
- **Cofre:** §82 — nome e caminho apenas; JSON novo entra como `Outros/chaves/AdSense/…` (chmod 600) e NUNCA no repo/ponte.

## 4. Estado conhecido dos temáticos (frente de crescimento)

- 8 sites (riocarta, globalsouth, mundotrilhos, railpost, discoverbrazil, ceara.digital, aiatolah…) com script + meta auto ads e ads.txt OK desde 21/07; **falta cadastrar domínios no painel** (ação do Miguel, só o cadastro libera veiculação); riocarta desligado 22/07 por pedido (reativação = descomentar bloco no BaseHead).
- Imagem dos temáticos: política rígida de licença (Wikimedia/flickr verificável) por causa da aprovação AdSense (fórum revisão 14/07).

## 5. Auditoria de conformidade 16/06 — itens a re-checar (estado não assumido)

1. **P0** anúncio flutuante sobrepondo texto (sticky footer sem padding) — estado atual: VERIFICAR.
2. **P0** política de privacidade com cláusulas Google/cookies — implantação iniciada 16/06 (Privac) — estado atual: VERIFICAR.
3. **P1** vignette em clique de menu (limitar frequência no painel) — ação de painel = mãos do Miguel.

## 6. Aulas Miguel+Gabriel (série)

AULA_01 no ar (`Relatorios/publicidade/aulas/AULA_01_como_o_google_paga_o_cafezinho.md`): leilão, impressão/clique/CTR/RPM, conta de guardanapo com 50.201 navegações de 31/08, mapa da casa, 5 proibições, exercício no app. Próximas: 02 painéis · 03 AMP×non-AMP · 04 viewabilidade · 05 políticas · 06 temáticos.

## 7. Glossário de trabalho (referência rápida do ofício)

- **RPM** receita por mil impressões; **eCPM** custo efetivo por mil (lado rede); **CTR** cliques/impressões; **fill rate** % de slots que receberam anúncio; **viewabilidade** % do anúncio realmente visto (≥50% da área ≥1s — padrão MRC); **header bidding** leilão antes do leilão (360yield no non-AMP); **floor price** lance mínimo aceito; **auto ads** Google decide onde inserir; **house ad** autopromoção (permitida, fora de unidade de anúncio); **publipost** post patrocinado (no Cafezinho: só como `page`, nunca `post` — memória vinculante `feedback_publipost_so_como_page_nao_post`; caso 1xbet 16/06).

## 8. Irmãos deste ofício (não duplicar, citar)

`forum_auditoria_adsense_ocafezinho_20260616.md` (conformidade) · `forum_mapa_ads_canonico_ocafezinho_20260811.md` (mapa) · `forum_banners_moka_reader_publicacao_cafezinho_tematicos_20260816.md` (house ads MOKA) · `forum_adsense_portais_tematicos_20260607.md` (temáticos) · Cafedash (`forum_cafedash_atualizacao_telegram_20260820.md`).

— DS Nuvem Publicidade (DS-N Pub) · 20260901 01:52:00 BRT · DSH/us65
