# Fórum — Fusão dos blocos Tecnologia + IA da home + emergência 401 do site público — 15/09/2026

> Ordem do Miguel (15/09 ~22:4x, transcrições): «as matérias têm que ir pros blocos porque só assim elas vão ficar visíveis; elas não estão indo pros blocos» + «junta os dois, tecnologia e inteligência artificial... qualquer categoria, inteligência artificial, ciência, tecnologia, deixa tudo no mesmo bloco».

## Diagnóstico (por que o bloco Tecnologia parou em 09/09)

- Os posts de tech/IA publicados desde ~10/09 saem só na categoria 5008 (Inteligência Artificial) + 2403 (Redação) — ex.: 271056 «OpenAI compra câmera», 271117 «Golpistas clonam voz», 271216 «Rivais da IA».
- O bloco Tecnologia do front-page.php consultava apenas 19936 (vazia) + 735 (Ciência) + 30 (Tecnologia) → nada novo desde 09/09 (últimos: Navier-Stokes 09/09 00:30, pesquisador Anthropic 09/09 11:30).
- O bloco «Inteligência Artificial» separado (cat 5008, criado 26-27/08) é que recebia tudo — a vertical ciencia_tecnologia_ia do V4.1 marca 5008.

## Fusão executada (no ar)

- front-page.php do tema ocafezinho-portal: h4 «Tecnologia» → «Tecnologia e Inteligência Artificial»; category__in array(19936, 735, 30) → array(19936, 735, 30, 5008) nas 2 queries do bloco; bloco IA separado (separador Digital + section, 2 queries cat 5008) REMOVIDO com comentário de fusão.
- Backup: front-page.php.bak_pre_fusao_tec_ia_20260915. Edição com arquivo baixado na hora (regra anti-sobrescrita), php -l OK (local + servidor), opcache_reset + rocket_clean_home + wp cache flush.
- Prova no canônico www.ocafezinho.com (200): bloco único na posição antiga do Tecnologia; posts de hoje visíveis: «Rivais da IA articulam supervisão que Trump rejeita», «Golpistas clonam voz em 10 segundos», «OpenAI compra câmera de celular»; bloco IA separado sumiu da lista de h4.

## 🔴 Emergência descoberta no caminho: site público trancado

- cafezinho.news e www.cafezinho.news resolvem para **159.65.177.60** (o servidor «espelho» do hack de 13/09) que responde **401 «Restrito - Cafezinho»** (Basic Auth no nginx de lá) — leitores fora.
- Canônico (ocafezinho.com / 190.89.239.65) 200 normal com a fusão.
- Sem registro de quem trancou nem quando (monitor/ponte até 15/09 23:00). Decisão pendente do Miguel: destrancar o 159.65 × apontar DNS para o canônico × manter até a reconstrução limpa (pendência §5 do fórum do hack). Até lá, NADA da home é visível pelo domínio cafezinho.news.
- Aviso na ponte: ZM-20260915-013 (de_dell.md, commit 398c0b908) para @CL @CM @LauraZM @ASTRA @todos — ronda de blocos + reportar contexto do trancamento.

## Estado / o que falta / o que preciso do Miguel

- Aconteceu: fusão no ar com provas; ponte avisada; ingestor DSN do YouTube pausado (55 * * * * — único autônomo de YouTube ainda vivo, agora comentado c/ backup crontab.bak_pre_pause_ingestor_20260915; ordem «nenhum autônomo»).
- Falta: decisão sobre o 401 do cafezinho.news (acima); chefe de publicação publicar rascunho de vídeos (bloco Vídeos/cat 28 só anda com publicado — 271200 na fila).
- Preciso de você: escolher (a) destrancar, (b) apontar DNS pro canônico, ou (c) manter trancado até a reconstrução.

— ZCode/GLM-5.3 · 15/09/2026 23:1x BRT

## ➕ Adendo — Vigia de blocos no ar + redirect 301 + quadro real (15/09 ~23:2x BRT, ordem Miguel)

**Ordem:** «nenhum bloco pode ficar desatualizado muito tempo... os de nacional economia tecnologia geopolítica não podem ficar desatualizados, tem que ter sempre matéria... tem que vigiar os blocos a ponte os monitores o ZM a ronda» + «resolve» (o 401).

**1. Vigia de blocos NO AR:** `/root/alerta_blocos_v1.py` (cafezinho-wp) + cron `5 * * * *` (flock). Régua: quentes 10h (Nacional 22 · Economia 43 · Tecnologia e IA 30+735+5008+19936 · Geopolítica 5003) · mornos 30h (Vídeos 28 · Cultura 79 · Meio Ambiente 582 · Esporte 1271 · Regional) · frios 72h (Saúde 258). Telegram direto no Miguel (TELEGRAM_TOKEN_PONTE/PONTE_CHAT_ID do .env.unificado — mesmo padrão do alerta de capa), cooldown 6h/bloco, silêncio quando tudo ok, estado em /root/agent_data/alerta_blocos_estado.json. 1º alerta REAL enviado 23:17 (OK).

**2. Quadro no 1º diagnóstico (23:17):** OK — Nacional 1h, Tecnologia e IA 2h (fusão funcionando), Regional 1h, Economia 10h (no limite). 🔴 ESTOURADOS — Geopolítica 13h · **Vídeos 66h** (desde 13/09, rascunhos aguardando chefe de publicação) · **Cultura 150h** (09/09) · Meio Ambiente 106h · Esporte 121h · Saúde 109h. Leitura: as verticais frias não estão publicando (juiz rigoroso + plano mínimo), não é bug de categoria.

**3. cafezinho.news resolvido:** o trancamento era DESENHO (ordem Miguel 13/09 «fechar o espelho — sem público, sem canibalizar SEO do canônico»; espelho de teste das verticais). Ação: vhost do 159.65 agora faz **redirect 301 → www.ocafezinho.com** (leitor perdido cai no site oficial; auth mantido como defesa secundária; backup /etc/nginx/backups_pre_edit/cafezinho-news.bak_pre_redirect301_20260915; provado 301→200 seguindo). Site público oficial = www.ocafezinho.com.

**4. Ponte:** ZM-20260915-014 (commit 9408e2031) — casa avisada: @CM @CL avaliar verticais frias (falta de pauta × esteira presa) + chefe de publicação p/ Vídeos.

— ZCode/GLM-5.3 · 15/09/2026 23:2x BRT · adendo vigia
