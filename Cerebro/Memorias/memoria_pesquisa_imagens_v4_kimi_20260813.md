# Memória técnica — Pesquisa de imagens V4 (11 sem capa + 4 capas IA fracas)

**Data:** 13/08/2026, ~10:04–10:30 BRT
**Sessão:** ZCode (Kimi K3) — workspace ZCodeProject, chat direto
**Gatilho:** carta do Codex no fórum `Foruns/forum_kimi_imagens_pendentes_v4_pos_limpeza_20260813.md` ( Miguel → Kimi, via fórum, ~09:58)
**Escopo:** SOMENTE PESQUISA. Nada publicado/editado/movido no WordPress. Zero escrita em servidores.

## O que foi feito (log)

1. **Protocolo de entrada:** monitor lido (Regra Nº 2) — sem colisões; linha "EM ANDAMENTO" registrada. Fórum do Codex lido integralmente. Recado paralelo do Claude (bug repetidor dedup-lead) lido e registrado no monitor como pendência de decisão (não era desta missão).
2. **Paralelização:** 4 subagentes de pesquisa web (general-purpose), cada um com as regras completas do fórum embutidas no prompt (fontes prioritárias, proibições, formato, verificação de licença na página do arquivo, estrutura de entrega):
   - Agente A — Brasil política/eleitoral: 265465, 265478, 265135, 265378 (19 ops web)
   - Agente B — Brasil infra/economia/saúde/cultura: 265083, 265454, 265471, 265473 (19 ops)
   - Agente C — geopolítica: 265173, 265209, 265376 (22 ops)
   - Agente D — tech/esporte/naval/mineração: 265323, 265439, 265358, 265414 (14 ops)
3. **Complemento próprio (Kimi):** agente C não achou foto horizontal verificada do Trump → busca direta na API do Commons → `File:Donald Trump at the 2026 Salute to America event F20260704AH-1426.jpg` (Andrea Hanks/Casa Branca, PD, 3000×2000, 04/07/2026) — verificada na página do arquivo e adicionada como alternativa do 265209.
4. **Consolidação:** manifesto em `Foruns/manifesto_imagens_v4_kimi_20260813.md` — 15 blocos (7 campos cada: candidata, página, hi-res, dimensões, autor, licença, legenda factual, alternativa, aviso) + notas de licenciamento + estado da missão.

## Resultado (números)

- **15/15 posts com candidata identificada e verificada** (licença+autor+dimensões na página do arquivo — nenhuma presumida de buscador).
- Licenças: 6 PD · 5 CC BY · 4 CC BY-SA · 1 CC0 — todas utilizáveis editorialmente com atribuição (ou sem, nas PD/CC0).
- 13/15 dentro do formato (horizontal ≥1200×675). **2 ressalvas:** 265135 (só vertical — exige recorte) e 265323 (sem foto livre de data center Alibaba — fallback sede corporativa; decisão editorial pendente).
- 0 imagens de agência paga entregues; 0 hotlinks; 0 montagens; 0 fotos de evento errado apresentadas como atuais.

## Arquivos tocados (todos locais, no Cérebro)

- `Foruns/manifesto_imagens_v4_kimi_20260813.md` (NOVO — entrega principal)
- `Foruns/forum_kimi_imagens_pendentes_v4_pos_limpeza_20260813.md` (adendo de entrega)
- `MONITORAMENTO_DE_TRABALHO.md` (linha da sessão + pendência bug repetidor + ✅ final)
- `CEREBRO_NODE_ATUALIZACOES.md` (linha do tempo)

## Lições/aprendizados

1. **Commons API + página do arquivo** é o fluxo confiável: `srnamespace=6` para achar, `wiki/File:...` para confirmar licença/dimensões. Metadados da API conferem com a página.
2. Para fatos de 10–13/08/2026 (72h), **não existe acervo livre do evento** — o padrão honesto é fallback documental/institucional com legenda datada que não finge ser do evento. Funcionou em 15/15.
3. Fontes PD de alto valor para pautas internacionais: **US Navy/DVIDS** (navios — achamos o navio exato KRI I Gusti Ngurah Rai 332), **NASA** (satélite Bayan Obo), **Casa Branca** (Trump 2026 horizontal), **TSE** (urna PD), **IAEA Imagebank** (mina Rössing).
4. Esporte é o pior caso: fotos do jogo são 100% agência paga; fallback correto = estádio com legenda factual (Mineirão, Portal da Copa CC BY 2.0).

## Estado da missão

- **O que aconteceu:** manifesto 15/15 entregue e catalogado.
- **O que falta:** Miguel/Codex decidirem as 2 ressalvas (265135, 265323); aplicação das imagens = etapa seguinte, NÃO autorizada aqui.
- **O que preciso de você (Miguel):** validar o manifesto; se aprovado, autorizar sprint de aplicação (download → biblioteca de mídia → featured image + crédito/legenda).

---

## ADENDO ~11:15 BRT — Fase 2: aplicação autorizada + cartinha ao Claude

**Ordem Miguel (13/08 ~11:00):** "deixa tudo em rascunho; manda cartinha pro Claude auditar e publicar escalonado no loop Vigília".

**Aplicação (canônico `cafezinho-wp`, `/var/www/ocafezinho`, wp-cli `--skip-themes --skip-plugins --allow-root`):**
- Estado inicial real: 9 posts sem capa + 6 com flux-pro (265209/265323/265358/265376/265414/265465 — os 2 últimos estavam na lista "sem capa" do Codex mas já tinham thumb v4-featured; receberam a imagem real do mesmo jeito, flux-pro fica na biblioteca).
- Backup: `/root/backup_kimi_imagens_v4_20260813/thumbs_antes.csv` (+ thumbs_depois.csv). Script: `/root/aplica_imagens_v4.sh` (espelho local `/tmp/aplica_imagens_v4.sh`).
- **15/15 aplicadas** via `wp media import --featured_image` com caption (legenda factual + crédito + licença), alt e desc. Novos attachments: **265483–265499** (mapa na cartinha ao Claude). Posts seguem **pending** ✅. Spot-check de 3 attachments (caption/mime) + arquivos no disco ✅.
- Aprendizado wp-cli canônico: precisa `--allow-root` (roda como root) e `--skip-themes --skip-plugins` — senão o bootstrap do tema cospe código PHP no stdout e contamina parsing.

**Escalonamento proposto** (análise de conteúdo dos 15: título+lead+perecibilidade) — 5 tiers: 🔥 265439→265465→265478→265454→265209 (12:30–16:10) · ⏰ 265173→265358→265376→265414→265323 (17:05–20:45) · 🌙 265083→265378→265471→265473→265135 (21:40–01:20). Tabela completa com raciocínio na cartinha.

**Cartinha ao Claude:** `Foruns/inbox_trindade/claude.md` tag `[KIMI-IMAGENS-V4-15-POSTS-AUDITORIA-E-ESCALONAMENTO-20260813-1115-BRT]` — pede auditoria dos 15 com checklist dele → agenda aprovados em `post_status=future` → reprovados ficam pending + ping em `inbox_trindade/zcode.md`. Issues conhecidos sinalizados (265439 curto; markdown em 265323/265414/265471; cat errada 265358; decisões Miguel 265135/265323 = não reprovar).

**Estado:** imagens aplicadas, zero publicado por mim; bola com o Claude (auditoria+agenda). Próximo check: ver no próximo ciclo do loop dele se começou a agendar.
