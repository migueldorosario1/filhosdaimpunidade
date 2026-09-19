# Fórum — Baleia Azul: comando de volta ao ZM + prompt único + fallback Laura (15/09/2026)

Ordem do Miguel (~15h, 15/09/2026): "Faz o Baleia Azul você aqui do ZM. Bota no cérebro e vamos consolidar, centralizar, para botar um prompt único... qualquer um que fizer o Baleia Azul vai seguir o mesmo prompt... Escreve um código de fallback para cair para a Laura... Tem que atualizar o V6 e tem que mandar por Telegram... 400 palavras tá bom, linguagem humanizada, até divertido, com dados de audiência, comparativo, post de sucesso, categorias para orientar."

## O que aconteceu ( diagnóstico )

- O Baleia estava MUDO desde 11/09 07:03 (ed. 46): a editoria passou ao DS-N Chefe em 01/09 (junto com o desligamento dos crons de envio do Dell) e ele morreu no apagão de quota DeepSeek — 4 dias sem edição, sem e-mail e sem Telegram.
- A pergunta "voltou a ser publicado?" na data: NÃO. Última edição boletim_baleia_azul_20260911_manha.md (ed. 46).

## Decisão (resolvida por delegação do Miguel: "resolva isso para mim")

- **Titular: ZM (ZCode Miguel, Dell)** — manhã e tarde. Justificativa: todo o ferramental de dados vive no Dell/alcance do ZM (coletor GA4 via NYC, API dos medidores no Tencent, wp-cli, ponte Telegram) e o ZM carrega o contexto fresco de audiência (obras /v6/audiencia, correlações). **A Laura Claude fica como FALLBACK formal** — acionada por código determinístico, produz pelo mesmo prompt único.
- Formato novo: ~400 palavras (350-450), humanizado/divertido, foco em audiência (comparativo com datas nas duas pontas, post de sucesso, posts/categorias que orientam a pauta, observação de erros, produção em 1 linha). Substitui a carta longa (~1.500 palavras) do DS-N.

## Peças implantadas (15/09, tudo no ar)

1. **PROMPT ÚNICO:** `Foruns/ponte_laura_completa/baleia_azul/PROMPT_UNICO_BALEIA_AZUL.md` (na ponte, propaga a todas as máquinas pelo git; espelho canônico no Cérebro). Formato, fontes de dados com comandos prontos, regras editoriais consolidadas, rede de segurança e numeração (ed. 46 = 11/09 → 47 = retomada 15/09 → 48 = 15/09 tarde).
2. **Automação ZM:** automation-15458117-897c-4d97-b38b-5438dd445f51, cron `5 7,19 * * *` (07:05 e 19:05 BRT), autodetecção de turno por hora; produz, commita, pusha e manda o texto completo no Telegram. Primeira execução: hoje 19:05 (ed. 48).
3. **Fallback Laura (código, sem LLM):** `~/bin/baleia_fallback_laura.sh` no crontab do Dell (07:30 e 19:30) — edição do turno faltando → bloc 🔴 URGENTE BALEIA-FALLBACK-<data>-<turno> na ponte de_dell.md chamando a ZL (produzir em até 45 min pelo prompt único) + push + Telegram ao Miguel. Dedupe por marcador.
4. **Watchdog Tencent (Dell desligado):** `/home/ubuntu/bin/baleia_watchdog_telegram.sh`, crontab 07:45 e 19:45 BRT — sem edição no clone, Telegram direto ao Miguel sugerindo "ponte laura".
5. **Edição de retomada:** ed. 47 (manhã, atrasada, 449 palavras) produzida e entregue — commit 9ab7b262d + ajuste, Telegram ao Miguel ~15:17, painel V6 mostrando "Edição 47" (verificado via curl interno; fonte v6_data atualizada por scp cirúrgico).
6. **Cadeia V6 consertada:** clone cerebro-miguel do Tencent estava 175 commits atrás do mirror NYC com 111 commits locais vivos do workflow DS YouTube (reset proibido) → merge `nyc/main` limpo (61135ee7a), 0 marcadores introduzidos (queue_youtube.md tem marcadores HISTÓRICOS, pré-existentes, do workflow dele — registrados, não mexi).

## O que ficou desligado (por decisão, registrar)

- **E-mail do Baleia segue OFF** (desde 01/09): o Miguel pediu Telegram + V6; os crons 08:00/19:30 do wrapper continuam comentados. Reativar só com ordem.
- **Coluna_editor separada: fim** (a carta humanizada de 400 palavras absorveu a coluna).
- **DS-N Chefe: aposentado da editoria** mesmo se sua ronda voltar.

## O que falta / próximos passos

- Hoje 19:05: primeira execução automática (ed. 48 tarde) — conferir amanhã de manhã que o ciclo rodou sozinho (ed. 49 manhã às 07:05).
- Prova real do caminho de ESCALONAMENTO do fallback só acontece numa falta real (o caminho OK foi provado hoje; o de escala é por construção + marcador de dedupe).
- Pendência de terceiro: queue_youtube.md (clone Tencent) com marcadores de conflito históricos — dono do workflow DS YouTube pode limpar.

## O que preciso de você (Miguel)

- Nada obrigatório. Se quiser o e-mail de volta (Miguel+Gabriel, 08:00/19:30), um "volta o e-mail do Baleia" basta.
- Se a edição de hoje 19:05 e a de amanhã 07:05 chegarem certinhas no seu Telegram, o sistema fecha o ciclo sozinho.

— ZM · ZCode/GLM-5.3 · 15/09/2026 15:2x BRT

## Adendo 16/09 ~08:45 — E-MAIL REATIVADO (ordem do Miguel: "tem que mandar para mim e para o Gabriel, por e-mail")

O e-mail estava desligado desde 01/09 (migração pro DS-N — crons comentados com BALEIA_DESLIGADA_20260901_ZM; na retomada 15/09 anotei que voltaria só à ordem). Ordem veio 16/09 ~08:4x:

- Crontab Dell religado: `0 8` (manhã) e `30 19` (tarde) → `enviar_baleia_azul_ponte.sh` SEM --telegram (Telegram segue com a automação ZM 07:05/19:05 — sem duplicação).
- Cadeia provada: teste a seco BALEIA_DRY_RUN=1 rc=0 + envio REAL da ed. 49 às 08:43 → /var/log/msmtp.log do Tencent: from=migueldorosario@gmail.com → recipients Miguel, gabrielbarbosa9001@gmail.com, gabrielbarbosa@ocafezinho.com, smtpstatus=250 exitcode=EX_OK.
- E-mail = edição de 400 palavras + blocos de audiência/saúde dos coletores + digests (autoria 5 linhas; audiência-vertices 0 linhas — endpoint lento, fail-soft seguiu).
- Cadeia de horários: 07:05 produção → 07:30 fallback check → 08:00 e-mail manhã; 19:05 produção → 19:30 fallback check + e-mail tarde.
- PROMPT_UNICO §2 e NODO_BALEIA_AZUL retificados.

— ZM · ZCode/GLM-5.3 · 16/09/2026 08:4x BRT

## Adendo 17/09 ~08:0x — NOVO FORMATO EDITORIAL v2 (bronca + ordem do Miguel: "tá muito pobrinho, elabora")

Ordens do Miguel 17/09 manhã: (1) FAROL passa a ser o indicador PRINCIPAL, GA4 secundário; (2) toda visita cita o indicador pelo nome; (3) foco em BOAS NOTÍCIAS; (4) comparar com o MESMO DIA DA SEMANA ANTERIOR (mesma hora); (5) top 10 dos últimos 7 dias COM CATEGORIA e título; (6) os mais lidos PUBLICADOS nos últimos 7 dias; (7) velocidade no CELULAR comparada com semana e mês anteriores; (8) texto MAIS ELABORADO, em forma textual, zero expressão críptica de insiders ("para nunca esquecer" citado como exemplo do que NÃO fazer); (9) sem asterisco; (10) QUEM ESCREVE ASSINA com a LLM.

Executado:
- PROMPT_UNICO §3/§4/§6 reescritos (régua 400-600 palavras com lista; fontes novas; 11 regras; teste final de 3 perguntas).
- 3 ferramentas novas em ~/bin: baleia_farol_serie.py (humanos às 07h por dia + semanas somadas, do SQLite do FAROL), baleia_farol_top7.py (top páginas de 7 dias do histórico de pushes audiencia_red.jsonl) e baleia_velocidade.py (LCP/TTFB mobile CrUX: última boa + 7d + 30d do NYC).
- Edição 51 REFEITA (573 palavras) e reenviada ao Telegram; números-chave: hoje 07h FAROL 7.333 humanos = +25,6% vs quinta passada mesma hora (5.839) e +13% vs ontem; semana 10-16/09 = 127.614 humanos vs 97.395 da anterior (+31%); recorde terça 15/09 com 24.171; top 1 da semana Dark Horse ao PCC (753, Nacional/Política); 8 dos 10 top nasceram na semana; LCP mobile 1,74s (16/09) vs 1,64s (07/09) e 1,63s (17/08), TTFB 0,85s vs 0,98s no mês.
- Observação: medição CrUX de 17/09 falhou (timeout) — usado 16/09 como última boa (recorrente nos últimos dias; collector a revisar). Categorias mapeadas por REST (22=Política, 21141=Nacional, 5088=Eleições 2026, 5003=Geopolítica, 43=Economia).

— ZM · ZCode/GLM-5.3 · 17/09/2026 08:0x BRT

## Adendo 18/09 ~08:5x — MANUAL DE ESTILO PRÓPRIO + bronca "continua vindo ruim" + causa raiz do problema de ontem

Bronca do Miguel 18/09 ~08:3x: "o baleazou continua vindo ruim... tem que usar o manual de estilo... prepara um próprio, parecido com o do cafezinho, mas com diferenças: emoji, mais emoji, tem que ser alegre, procura os dados positivos no farol comparando os dias da semana fechados (quinta com quinta), mais curiosidade sobre os posts nos últimos 7 dias, mais jornalístico... ontem ficou de você fazer a reforma e você não fez, tá tendo algum problema aí".

CAUSA RAIZ do que saiu torto hoje: a automação ZM das 07:05 NÃO disparou (app ZCode fechado na hora — runCount prova 5 rodadas até 17/09 19:05; automação só roda com o app aberto) → o fallback das 07:30 cumpriu o desenho e chamou a Laura, que produziu a ed. 53 sem o novo tom (zero emoji) e com régua de contagem DIFERENTE (1.177 leitores no top 1 vs 753 da série canônica) + um post "sem categoria" exposto na carta. A rede de segurança segurou a EDIÇÃO, mas o CONTEÚDO divergiu do novo formato.

Curas executadas agora:
1. MANUAL_DE_ESTILO_BALEIA_AZUL.md (Cerebro/Estilo/ + repo cerebro/Estilo/) — irmão do manual do Cafezinho, com as diferenças do boletim: emoji bem-vindo e esperado (mapa de uso), alegria honesta (abre e conduz pela boa notícia real), FAROL indicador principal, comparativo de mesmo dia da semana e mesma hora (nunca parcial×fechado), curiosidades jornalísticas dos 7 dias, texto corrido sem jargão de casa, proibida metalinguagem operacional ("o fallback me chamou", "o script mora em outra máquina"), assinatura com a LLM, teste final de 5 perguntas.
2. PROMPT_UNICO apontando o manual como leitura obrigatória antes de qualquer edição — vale para titular E fallback (o arquivo vive no repo, a máquina da Laura também lê).
3. Edição 53 REFEITA pelo ZM (596 palavras, manual aplicado) e reenviada ao Telegram: quinta 17/09 fechada = 23.895 humanos no FAROL (+36,6% vs quinta passada fechada 17.497; +13,8% vs quarta), 2º melhor dia da série; sexta abre +21% vs sexta passada mesma hora; semana fechada 11-17/09 = 134.012 (+30,5%); curiosidades: Folha×Flávio saltou do 8º para o 5º em 24h, Irã entrou oficialmente no top 10, núcleo Vorcaro-Master soma 1.891 em 3 títulos, 7 dos 10 nasceram na semana.

Pendência registrada: o post "A festa que Vorcaro organizou para se aproximar do poder" apareceu na contagem da Laura como "sem categoria no sistema" — arrumar a categoria dele quando couber (checar autor antes: se humano, o gate 423 vale).

— ZM · ZCode/GLM-5.3 · 18/09/2026 08:5x BRT

## Adendo 18/09 ~09:2x — BALEIA ENTREGUE AO DSN CELULAR (ordem do Miguel: "vamos entregar essa baleia para o DeepSeek Lite")

Ordens do Miguel 18/09 ~08:5x: reanimar o DS celular (estava travado: patch com GLM sem crédito + chave DeepSeek velha 401), configurar DeepSeek Flash como motor com DeepSeek V4 Pro de opção, e ENCARREGAR o DSN celular do Baleia 2×/dia (07:00 e 19:00), produzindo pelo prompt com o manual de estilo, atualizando o V6, mandando Telegram com a revisão/opinião dele no padrão Cafezinho. A edição de 18/09 ficou com o ZM.

Executado:
1. **Reanimação:** chave da API do serviço (sk-...) nos 2 cofres com backup .bak_pre_dsn_celular (nunca exibida); DEEPSEEK_API_KEY viva instalada no /root/.dsh/deepseek_env (a velha dava 401) com backup; patch cordis.patch.yml reescrito (provider deepseek: deepseek-flash default + deepseek-v4-pro opção; GLM mantido listado) + copiado ao perfil headless; restart dsh-web ativo; prova de vida headless: "Sou o deepseek-v4-flash, e mando um olá ao Miguel!".
2. **Painel:** GET /api/baleia-dados (pack: FAROL humanos/dia fechado, 07h e 19h, semanas somadas, top 7 dias, instantâneos — provado 21 dias + 11 top) e POST /api/baleia-edicao (grava a edição direto no V6 na hora, token do contador). Backup painel .bak_pre_baleia_dsn_20260918.
3. **Missão + ciclo:** /root/dsh_workspace/baleia_mission.md (lê prompt único + manual do repo, coleta o pack, escreve seguindo o manual) + /root/bin/baleia_dsn_ciclo.sh (produz headless → valida 300-700w/sem asterisco/sem trama/sem CJK/com cabeçalho → parecer do DSN → commit+push no clone /root/Cerebro → POST V6 → Telegram completo com parecer). Bug pego no teste: source sem set -a (chave não herdada) — corrigido; alerta de falha no Telegram provado (200).
4. **Agenda:** cron do servidor 0 7 / 0 19 com TRAVA de ativação a partir de 19/09 (a edição de 18/09 ficou com o ZM; a automação ZM 07:05/19:05 é pausada após a edição da tarde de 18/09).
5. **Prova DRY (09:18):** edição completa de 589 palavras produzida pelo DSN seguindo o manual — FAROL em primeiro, emoji, sexta×sexta, top 10, curiosidades, assinatura "DSN celular · DeepSeek V4 Flash". Artefato de teste removido.
6. **Fallback:** o script do Dell (07:30/19:30) e o watchdog do Tencent (07:45/19:45) vigiam o repo — cobrem o DSN automaticamente (falha dele → chamada URGENTE para a Laura).

Pendências honestas: o pacote de dados v1 não inclui GA4 diário nem velocidade CrUX (ficam no NYC; o DSN marca "não confirmado" nesses blocos — incluir na v2 do pack); a credencial do serviço DSH na URL é basic auth nginx separada da chave sk- (a sk- ficou nos cofres).

— ZM · ZCode/Kimi K3 · 18/09/2026 09:2x BRT

## Adendo 18/09 ~09:4x — DSN celular com DOIS motores: Kimi K3 + DeepSeek Flash (ordem do Miguel "deixa o dsn celular com os dois")

Ordem do Miguel 18/09 ~09:3x: "óótimo, deixa o dsn celular com os dois, kimi k3 e deepseek flash."

Executado:
- Provider kimi adicionado aos patches web+headless: apiKeyEnv KIMI_API_KEY (a chave KIMI_CODE_API_KEY_ZCODE dos cofres — as outras três chaves Kimi dos cofres estavam expiradas/401; env do DSH atualizado com backup .bak_pre_kimi_20260918), api: openai-completions, baseURL https://api.kimi.com/coding/v1, modelos k3 e k3-256k (a API lista kimi-for-coding, kimi-for-coding-highspeed, k3 e k3-256k).
- Default segue deepseek-flash (opção deepseek-v4-pro); Kimi fica disponível como 2º motor (seleção no Models da web UI ou por patch overlay).
- Rota de erros até o boot limpo (documentada p/ futuros providers desconhecidos do catálogo do harness): precisa de api declarada (openai-completions, não "openai"), baseURL (maiúsculo) e models listados à mão quando o catálogo não descreve a rota. Crash-loop transitório observado por restart no meio da escrita do arquivo — curado com stop/start limpo.
- Provas: web ativo escutando 3080 com a config final; headless com overlay kimi responde tarefa objetiva correta (21×3=63); API Kimi 200 com a chave de coding.

— ZM · ZCode/Kimi K3 · 18/09/2026 09:4x BRT

## Adendo 18/09 ~09:5x — Rondas do dia no KIMI K3 (mudança de ideia do Miguel: "deixa no kimi k3 para fazer as duas rondas")

Mudança de ideia do Miguel 18/09 ~09:4x: as duas rondas diárias do Baleia (07:00 e 19:00) rodam no **Kimi K3** — DeepSeek V4 Pro e DeepSeek Flash seguem como opções disponíveis.

Executado e CAUSA RAIZ documentada: o patch com provider/model em agent-default-model NÃO bastava — existe uma **settings store** (/root/.dsh/settings.yaml) com seleção salva (deepseek-official/deepseek-v4-flash + reasoningEffort high) que SOBREPÕE a config estática do patch (o plugin dsh-agent-default-model lê primeiro a store). Por isso os testes saiam em deepseek-flash mesmo com patch em kimi. Cura: settings.yaml editado para provider kimi / model k3 (backup .bak_pre_kimi_default_20260918) + patches nos dois perfis alinhados + assinatura da missão ajustada para "DSN celular · Kimi K3". Prova objetiva: sessão nova no registro com provider kimi (6×); serviço ativo na 3080.

Estado final dos motores: default kimi/k3 (rondas); opções deepseek-flash, deepseek-v4-pro, kimi k3-256k (seleção na web UI ou overlay).

— ZM · ZCode/Kimi K3 · 18/09/2026 09:5x BRT

## Adendo 18/09 ~19:5x — E-MAIL NO FORMATO VELHO CURADO NA RAIZ + ed. 54 tarde no manual v1.1

Bronca do Miguel 18/09 ~19:37: "quem está fazendo o baleia azul? recebi esse email agora de tarde. nenhum dos problemas que identifiquei foram sanados... vai". CAUSA RAIZ provada: a automação ZM das 19:05 não produziu a edição da tarde (app fechado na hora) → o wrapper de e-mail das 19:30 caiu no caminho LEGADO (arquivo local + emissor velho) e despachou o corpo antigo — GA4 como régua, "temáticos pra nunca esquecer", asteriscos — exatamente os vícios banidos. O fallback das 19:30 já tinha escalado para a Laura (marcador), mas a edição não existia quando o e-mail saiu.

Curas executadas:
1. Edição 54 tarde produzida pelo ZM no manual v1.1 (597 palavras; FAROL primeiro — sexta +33,8% vs sexta passada mesma hora; GA4 DEPOIS com descompasso como parágrafo-ouro — FAROL semana recorde 135.103 vs GA4 −30%; duas AtlasIntel de ontem furando o top da semana num dia; Telegram + V6 instantâneo + e-mail).
2. Wrapper de e-mail REESCRITO ESTRITO (enviar_baleia_azul_ponte.sh v2, backup .bak_pre_estrito_20260918): envia SÓ a edição nova do repo (formato do manual); sem edição = e-mail RETIDO + aviso Telegram ("não mando mais o formato velho"). Emissor legado fora da cadeia — o formato antigo JAMAIS volta a sair.
3. Bug de aspas do envio curado (corpo via arquivo/scp para o Tencent) — prova msmtp 19:44:22, 250 OK, 3 destinatários, mailsize 3.636 (a edição nova).
4. Automação ZM (automation-15458117) DELETADA às 19:45 — handoff completo: o DSN celular é o titular a partir de amanhã 07:00; fallback Dell (07:30/19:30) e watchdog Tencent (07:45/19:45) seguem vigiando o repo e cobrem o DSN.
5. Token do V6: o AUDIENCIA_RED_TOKEN do cofre Dell está DEFASADO (403 no /api/baleia-edicao) — o válido é o push_token do contador no cafezinho-wp; REGRA 4: rotacionar/espelhar na próxima faxina do cofre.

— ZM · ZCode/Kimi K3 · 18/09/2026 19:5x BRT
