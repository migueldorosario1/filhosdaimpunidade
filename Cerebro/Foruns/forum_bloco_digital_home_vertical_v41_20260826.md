# Fórum — Bloco DIGITAL criado na home + vertical V4.1 nova (26/08/2026)

**Data:** 26/08/2026 ~20:05 BRT · **Executor:** ZCode/Kimi K3 · **Ordem do Miguel:** 26/08 ~19:35 ("bota um bloco a mais... bota digital. Melhor assim, né? Digital.")

## 1. A ordem

Criar um bloco novo na home: **Digital** (o Miguel chegou a cogitar "Estatística" e decidiu por "Digital" na mesma frase). Como a regra vigente na casa é "bloco parado não tem sentido", o bloco nasceu já com máquina própria de atualização 3x/dia.

## 2. O que foi feito

**Editoria nova de ponta a ponta:**

1. **Categoria WP:** `Digital` criada — **term_id 21189** (slug `digital`, descrição: cultura digital, plataformas, redes sociais, internet e regulação do ambiente digital).
2. **Coletor** (`/root/coletor.py`, backup `.bak_pre_digital_20260826`): seção `digital` (abrev `dig`) com 5 feeds validados ao vivo (Tecnoblog 50 itens, Canaltech 50, Olhar Digital 10, Núcleo 6, Mobile Time 20) + 6 google_queries + classifier_keywords próprias (plataformas, redes sociais, influenciadores, regulação, Anatel/ANPD, golpes digitais). Hard tech fica de fora — continua na vertical Tecnologia.
3. **Intake** (`/root/v4_vertical_intake.py`, backup idem): `DATABASES["digital"]="digital.sqlite3"`, `POLICY["digital"]=48h`.
4. **Redator V4.1:** `v41_ciclo.py` aceita `--vertical digital` (seleção de pauta = `new` frescas 48h, igual às 3 verticais religadas hoje) + patch de categorias no nascimento **[21189, 2403]**; `EDITORIA_ALIASES` do runtime + `mapa_v4_contexto_llm.json` ganharam `v4_digital` (funções luxo irmãs: redação super luxo, revisão, auditoria, fact-check, imagem Gemini); diretriz editorial nova `contratos/v4_digital_v1.md` (escopo: plataformas no cotidiano, cultura de internet, regulação, golpes digitais, soberania digital do cidadão; fora: chips/IA fronteira, gadget puro, e-sports).
5. **Crons** (marca `V41_DIGITAL_20260826`): coleta `15 11,17,23` UTC (08:15/14:15/20:15 BRT) + ciclo `8 12,18,0` UTC (09:08/15:08/21:08 BRT) — 3 chances de post/dia.
6. **Semente da categoria:** 5 posts publicados recentes e on-theme receberam a cat Digital (sem perder as originais): 267615 (multa ECA Digital×TikTok), 266477 (plataforma eleitoral climática), 266291 (Trump×algoritmo do X), 265975 (STF×big techs), 265336 (Discord×crianças).
7. **Bloco na home** (`front-page.php`, backup `.bak_pre_bloco_digital_20260826`): padrão idêntico ao de Esporte (1 destaque grande + 5 em linha), `category__in=[21189]`, posição = logo após Esporte, antes dos banners/Recentes. Cache WP Rocket da home limpo para refletir.

## 3. Provas

- Coleta+intake de estreia: **17/17 candidatas aceitas** no `digital.sqlite3` (22:44 UTC).
- Home ao vivo (pós-cache): separador **Digital** renderizado com 5 posts corretos — destaque "Governo aplica a primeira multa do ECA Digital e escolhe o TikTok".
- Gate de qualidade funcionando: 1º ciclo de redação (19:52) reprovou a pauta B2B "Pontaltech RCS" por **sem-tese** e não escreveu — fail-closed íntegro. Próximo ciclo automático 00:08 UTC (21:08 BRT).

## 4. Estado da missão

- **O que aconteceu:** bloco Digital no ar e populado; vertical V4.1 digital completa (coleta→intake→tese→redator→rascunho [21189,2403]); 3 ciclos/dia programados; publicação segue EXCLUSIVA dos editores CM/AGY.
- **O que falta:** acompanhar a 1ª matéria inédita da vertical (próximos ciclos — pode levar 1-2 rodadas até uma pauta passar na tese); se em 48h o bloco estiver magro, subir coleta para */6h.
- **O que preciso de você (Miguel):** nada agora. Se quiser o bloco em outra posição da home (ex.: logo após Tecnologia, que é o "primo" temático), é um recorte de 5 minutos — me diz.
