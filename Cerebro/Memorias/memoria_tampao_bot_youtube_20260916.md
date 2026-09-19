# Fórum — TAMPÃO (preenchedor de blocos) + Bot Telegram YouTube — 16/09/2026

> Origem: ideia do Miguel 15/09 ~23h («vertical preenchedor de lacunas... investiga, busca nos bancos, se não achar coleta, publica») + ordem de execução 16/09 ~09h/12h (rascunho SEMPRE, assinatura, capa boa, já produzir, avisar ponte) + bot Telegram para disparar o agente YouTube manual de qualquer lugar.

## TAMPÃO v1 (no ar 16/09 ~12:2x BRT)

- **Desenho:** /root/tampao.py (NYC) — quando bloco da home passa da régua (quentes 10h: Nacional/Economia/Tec-IA/Geopolítica · mornos 30h: Cultura/MamB/Esporte/Regional · frios 72h: Saúde), dispara `codigo.v41_ciclo --vertical X` com env TAMPAO_ORIGIN=1. Máx 2 blocos/exec (mais atrasados primeiro) + 2 rodadas/bloco/dia + cooldown 3h. Cron `9 * * * *` NYC (logo após o vigia alerta_blocos 5 * * * * do cafezinho-wp). Vídeos e Regional não cobertos (vídeo=fluxo manual; regional sem vertical no ciclo).
- **RASCUNHO SEMPRE (decisão Miguel):** o ciclo V4.1 já nasce rascunho («jamais publicar» no prompt); quem publica é o publicador externo. O Tampão NÃO tem caminho de publish.
- **Assinatura:** patch no v41_ciclo (.bak_pre_tampao_20260916) — com TAMPAO_ORIGIN, grava metas `_agente_origem=tampao_v1` + `_cafezinho_origem=tampao` no rascunho via REST. É assim que ponte/publicador reconhecem.
- **Capa:** rascunhos V4.1 nascem sem capa → o rodízio/alerta_capa_v41 (cron */30) já captura + publicador externo confere (Miguel: «de qualquer forma o publicador externo também vai verificar»).
- **Diagnóstico de por que as verticais frias pararam:** Cultura/MamB/Esporte/Saúde NÃO TÊM cron do ciclo desde o plano mínimo (só nacional 7/19, economia 13h, ciencia 2/2h, geo horária, digital 3x) — o Tampão vira o gatilho delas.
- **1ª execução real (12:26-12:32 BRT):** Cultura 163h → 2 rodadas sem tese aprovada; Esporte 134h → 2 rodadas sem rascunho; Telegram do Miguel enviado OK com o resultado honesto. Causa: juiz rigoroso (pautas estrangeiras sem gancho BR). O Tampão segue tentando horariamente.
- **🔴 Pendência de decisão Miguel:** juiz em modo Tampão pode ter régua um pouco menor (ex.: corte de aprovação 6,0→5,0 com selo «tampao» p/ revisão humana mais leve?) — hoje NÃO afrouxei (curadoria é editorial). Se os blocos seguirem furados porque o juiz reprova tudo, é essa a válvula.
- Custos: ~centavos/rodada (DeepSeek juiz+redator).

## BOT TELEGRAM YOUTUBE MANUAL (no ar 16/09 ~12:30 BRT)

- `/home/ubuntu/yt_telegram_bot/bot.py` (tencent) + systemd `yt-telegram-bot.service` (Restart=always). Usa o bot @pontecafezinhobot (TELEGRAM_TOKEN_PONTE + MIGUEL_CHAT_ID no .env local 600 — espelhados da Dell, Regra 4).
- **Fluxo:** Miguel manda `/yt` → bot pede o link → valida URL do YouTube → botões inline (☕ Cafezinho · 🌍 GSN · 🏙️ Mapa Rio · 🤖 Aiatolah · 📜 Rio Carta · ✅ TODOS · ❌ Cancelar) → dispara o MESMO dispatcher ssh yt_manual_dispatch do painel → confirma com nº do pedido e avisa que Cafezinho nasce rascunho. Restrito ao chat do Miguel (outros chats ignorados). getUpdates long-polling (coexiste com os senders da ponte — estes não usam getUpdates).
- **v1 = 1 destino ou TODOS**; acumular múltiplos com check = v2 se o Miguel quiser.
- Prova: serviço active, log «bot YouTube no ar», creds carregadas. Teste real: Miguel manda /yt.

## Bug achado no caminho (pedido 20260916_010609 — sabatina Eduardo Paes)

- Transcrição OK (85.918 chars, US$ 3) mas TODOS os 3 destinos reprovaram: «entrevistado identificado mas não citado: Michel Temer» — Temer era CITADO na live, não entrevistado. `identificar_entrevistado` (lista-ouro) marcou errado e a auditoria cega reprovou 2× cada destino. Fail-closed funcionou (não publicou), mas US$ 3 sem entrega.
- **Cura proposta (pendente):** entrevistado = título da live/diarização (quem FALA), não qualquer nome da lista-ouro no texto. Registrado na ponte ZM-20260916-001 item 3.

## Estado / o que falta / o que preciso do Miguel

- Aconteceu: Tampão no ar (cron+assinatura+Telegram), 1ª execução real (juiz não aprovou — segue horário a hora), bot Telegram no ar, painel /v6/youtube verificado 100% (200 + bloco + PRODUZIR + status + dispatcher), ponte avisada (ZM-20260916-001, 77c2ec479).
- Falta: decisão sobre juiz modo-tampão (régua menor?); cura do identificar_entrevistado; teste real do /yt pelo Miguel.
- Preciso de você: mandar /yt no Telegram pra provar o bot com uso real; e decidir a válvula do juiz.

— ZCode/GLM-5.3 · 16/09/2026 12:4x BRT

## ➕ Adendo — válvula do juiz («vai») + régua 12h (16/09 15:1x BRT)

- **Válvula do juiz NO AR (ordem «vai»)**: patch .bak_pre_valvula_tampao_20260916 — com TAMPAO_ORIGIN, juiz 1 (pauta) usa cortes menores (total 6,0→5,0; interesse_br 5→3,5; encaixe 5→4,0; configurável via juiz_config.json tampao_*); juiz 2 (TEXTO) mantém rigor integral. PROVA: pauta «Evento de arte e tecnologia alfineta...» (Regina Silveira/Sesi Lab) tinha 5,17 REPROVADA às 12:26 e 5,17 APROVADA às 15:10 com a válvula → **rascunho 271411** «Regina Silveira borda crítica à IA no Sesi Lab» (draft, autor 5470, meta _agente_origem=tampao_v1 gravada rc=200).
- **Bug achado e curado no caminho:** o recategorizador de IA do runtime movia posts de verticais alheias para 5008/2403 (o 271411 nasceu IA+Redação e o bloco Cultura seguiria furado) → corrigido na mão (271411 ganhou cat 79) + patch .bak_pre_tampao_cats_20260916 (modo TAMPAO sempre garante a categoria do bloco-alvo além das que o runtime puser; campo tampao_cat_alvo no artefato).
- **Régua reduzida (ordem Miguel «o mínimo não pode paralisar o site»):** Cultura/Meio Ambiente/Esporte/Saúde 30h/72h → **12h** no Tampão E no alerta_blocos_v1 (Telegram). Quentes seguem 10h.
- Dry-run pós-régua (15:13 UTC): MamB 1h, Esporte 2h, Saúde 0h (a casa publicou posts novos — ponte fluindo), Vídeos 15h, único estourado Cultura — cujo rascunho Tampão (271411) já está na fila do publicador.

— ZCode/GLM-5.3 · 16/09/2026 15:1x BRT · adendo válvula+régua

## ➕ Adendo v2 — CONFERÊNCIA da produção de vídeos pela CCTV V6 (17/09 ~16:1x BRT)

Pedido do Miguel «confere aí a produção dos vídeos através da cctv v6» com a tabela do /v6/youtube:

1. **20260917_140152_f9f249 (sabatina Eduardo Paes) — VERIFICADO E APROVADO:** transcrição REUSADA (cache_hit zizi_pt-BR, 85.918 chars, US$ 0 — a mesma paga no pedido 010609 da madrugada); entrevistado identificado CERTO «Eduardo Paes» via titulo_dois_pontos (a regra nome-antes-dos-dois-pontos do auditor — o bug Temer não reincidiu; auditor com mtime de 17/09, casa mexeu); 3 destinos entregues: Cafezinho 271682 «Eduardo Paes diz que tirar crime do Palácio Guanabara é prioridade no Rio» (614 palavras, cat Vídeos, nasceu rascunho e o PUBLICADOR EXTERNO publicou no mesmo dia — fluxo §137 perfeito) + MapaRio no ar (mapario.com.br 200, título no HTML) + RioCarta no ar (riocarta.com 200). **Aspa validada palavra por palavra na transcrição real** (cache youtube_transcript_cache/zizi_pt-BR_QdiOdRlac7Q.json: «a Polícia Federal deveria investigar as relações da política ou com o crime organizado») — zero alucinação.
2. **20260917_135154_b09f2f (Stedile) — ERRO HONESTO + RETRY CONCLUÍDO:** Transkriptor Failed em 135s → fail-closed abortou com 🔴 e US$ 0 (desenho funcionando). Redisparei (20260917_160341_98cfaa): desta vez Completed — 16.726 chars/178 segmentos, US$ 3, entrevistado «João Pedro Stedile» (regex do título), rascunho **271710** «Stedile analisa eleições 2026 e diz que mulheres da periferia vão decidir» (cafezinho, aguardando publicador).
3. 20260916_010609 (mesma sabatina, madrugada 16/09): os 3 🔴 do bug Temer — histórico, sem perda (transcrição foi reaproveitada hoje de graça).
4. 20260915_192035 (Poll FLIP): ✅✅ conhecido (draft 271200 + GSN no ar).

**Lições:** Transkriptor segue intermitente no mesmo vídeo (Failed→OK com 2h de diferença) — retry manual resolve; o reuso de transcrição já poupou US$ 3 hoje; pipeline YouTube manual íntegro de ponta a ponta (transcreve→identifica→redige→rascunho→publicador publica).

— ZCode/GLM-5.3 · 17/09/2026 16:1x BRT · adendo v2 conferência CCTV

## ➕ Adendo v3 — PARECER do texto do Paes (271682) + 5 correções STT (17/09 ~16:3x BRT)

Pergunta do Miguel «o texto do Paes ficou bom?». Parecer ZM: **estrutura e fidelidade BOAS** (lead certo com quem conduziu a sabatina, sequência fiel — ADPF/Castro, Palácio Guanabara, unificação, presídios com números, força-tarefa/Coaf, fecho com bio; aspas ancoradas na transcrição real) — **mas NÃO estava pronto para público: 5 erros do robô de transcrição publicados crus**, herança do STT citado literal: «Amigo Escuro e Nação» (= amicus curiae), «Brazipina» (= Braz de Pina), «operação do Me Lembro Qual» (= fala "não me lembro qual" virou nome próprio!), «recadação» (= arrecadação), «William Ciri» (= William Siri, candidato real do PSOL confirmado em busca). CORRIGIDOS no ar com colchetes jornalísticos (backup /root/backup_271682_pre_fix_stt_20260917.html no cafezinho-wp; override + rocket_clean; provado no público: 0 ocorrências dos erros).

**Lição sistêmica:** o corretor de nomes da casa (corrigir_nomes_personagens) cobre PESSOAS; lugares, termos jurídicos e nomes de candidatos estropiados passam. «Me Lembro Qual» é quase metalinguagem publicada. Proposta (aguarda «vai»): (a) varredura pós-transcrição de suspeitos (palavras capitalizadas no meio de fala + lista de termos mal-ouvidos típicos + nomes de bairros/cargos conferidos) e/ou (b) instruir o publicador externo (ponte) a conferir nomes próprios em rascunhos de VÍDEO antes de publicar — hoje o post foi ao ar com os 5 erros.

— ZCode/GLM-5.3 · 17/09/2026 16:3x BRT · adendo v3 parecer Paes

## ➕ Adendo v4 — LINKS PÚBLICOS na tabela do /v6/youtube (17/09 ~16:4x BRT, ordem Miguel)

Bronca: os ✅ do Cafezinho apontavam p/ controle.ocafezinho.com/?p=ID (endereço interno do REST). CURAS: (1) patch youtube_manual.py (.bak_pre_links_publicos_20260917) — draft_cafezinho monta o permalink público www.ocafezinho.com/ano/mes/dia/slug a partir do JSON do create (permalink_structure /%year%/%monthnum%/%day%/%postname%/) e o destino temático monta a URL do post (/blog/arquivo/) quando a gravação é direta (antes: só a home do site); (2) retro-fix dos pedidos existentes (script /tmp/retrofix_links.py no NYC): consulta REST pública, PUBLICADO ganha permalink bonito (f9f249→Paes e 192035→Poll FLIP corrigidos), RASCUNHO mantém o interno (Stedile 271710 — é o que existe p/ conferir rascunho) + réplica scp p/ o tencent (a tabela lê v6_data/youtube_manual). Provas: endpoint /v6/youtube/manual/status mostrando o permalink novo + 200 no endereço público.

— ZCode/GLM-5.3 · 17/09/2026 16:4x BRT · adendo v4 links públicos

## ➕ Adendo v5 — FOTO REAL do André Marinho NO AR (17/09 ~17:5x BRT, após falha do turno anterior)

O turno anterior sofreu defeito de renderização (loop) e a troca NUNCA tinha sido aplicada (hero ainda IA 52729 bytes + crédito Ideogram + zero commits — Miguel confirmou vendo o site). EXECUTADO AGORA de verdade: crop real 853x479 (foto Elder Ibanhez/Wikimedia Commons CC BY-SA 4.0) → public/hero do repo riocarta (backup /tmp/hero_andre_IA_backup.jpg) + hero_credit corrigido + commit ee0105b + push. Deploy Vercel demorou ~5min (HTML e hero atualizados, provado: HTML com Elder Ibanhez 1× e hero pública 56780 bytes). 🔴 Lições: (1) loop de renderização NÃO significa execução — sempre re-verificar estado real do alvo após turno com defeito; (2) deploy riocarta ~5min, não 90s.

— ZCode/GLM-5.3 · 17/09/2026 17:5x BRT · adendo v5
