# Fórum — Painel de comando manual do agente YouTube (/v6/youtube) — 15/09/2026

> Missão: ordem do Miguel 14/09 ~23:0x («vai») + acréscimos («campo opcional para colar prompts» + «ver se o agente youtube do rio carta está modernizado no padrão do agente youtube cafezinho»). Construção concluída 15/09 00:2x BRT.

## O que foi construído

Página /v6/youtube do painel CCTV V6 ganhou o BLOCO «🎯 Comando manual — indique o vídeo e os destinos»:
1. Campo de URL do YouTube (validado: só youtube.com/youtu.be).
2. Textarea OPCIONAL de prompt de produção (direção editorial do Miguel — entra nos prompts de redação de todos os destinos marcados como «DIREÇÃO DO EDITOR-CHEFE (prioridade máxima)», máx 4.000 chars, transportado em base64).
3. Cinco quadradinhos de destino: ☕ Cafezinho (pt, rascunho) · 🌍 GSN (en, direto) · 🏙️ Mapa Rio (pt, direto) · 🤖 Aiatolah (pt, direto) · 📜 Rio Carta (pt, direto).
4. Botão PRODUZIR + tabela de status ao vivo (refresh 12s; por destino: ⏳/✅ com link/🔴 com motivo; custo da transcrição).

## Arquitetura (transporte e segurança)

- POST /youtube/manual (painel, tencent) valida URL/destinos → ssh com CHAVE DEDICADA yt_manual_dispatch (ubuntu@tencent → root@nyc) com command= FORÇADO /root/youtube_manual_dispatch.sh — a chave NÃO executa mais nada (provas: URL de outro domínio rc=65; comando arbitrário cai no uso; regex de b64).
- Dispatcher NYC revalida tudo (URL/destinos/pedido/prompt-b64) e dispara setsid nohup /root/venv/bin/python3 youtube_manual.py (agente em /root/tematicos/agentes_tematicos/v4/).
- Status incremental: /root/agent_data/youtube_manual/pedidos/<id>.json espelhado por scp (porta 38422, mesma rota do transkriptor_detalhe) para v6_data/youtube_manual/ no tencent; GET /youtube/manual/status alimenta a tabela.
- Público: endpoints exigem Basic Auth (401 sem creds provado); porta 8084 fechada ao exterior.

## Padrão sofisticado (resposta ao pedido «riocarta no padrão cafezinho»)

O executor youtube_manual.py aplica a TODOS os destinos (Rio Carta incluso) o padrão da cadeia V2 do Cafezinho:
- Transcrição ÚNICA por vídeo com diarização (classe da casa, modo zizi); reuso da tabela dialogos = custo zero (provado: 62.857 chars reusados, US$ 0).
- corrigir_nomes_personagens (materializador V2) no título e corpo pós-LLM.
- identificar_entrevistado (auditor V2: lista-ouro + meta + regex) — entrevistado identificado TEM que ser citado no texto (regra Nima); reprova se não.
- Gate determinístico de idioma por destino (publicador._versao_no_idioma): corpo PT nos 4 sites pt-BR, EN no GSN — tradução jornalística na redação quando o vídeo cruza idioma.
- Auditoria programática (título ≥15, corpo ≥180 palavras, entrevistado citado, idioma) com 1 retry com feedback; 2 reprovações = NÃO publica (fail-closed).
- Cafezinho: rascunho cat 28 autor Redação 5470, embed no topo, capa sddefault/maxres via REST /media, metas _video_id_youtube + _agente_origem=youtube_manual_painel (§137 — agente nunca publica).
- Temáticos: hero = thumbnail no repo do site, publicador oficial (veto/tribunal/gates); fila ocupada por terceiros → gravação direta via render+commit sem mexer nos outros.
- Gate de vídeo inexistente/privado (oembed 401/403/404) aborta ANTES de qualquer custo.

## Provas (15/09 00:1x-00:2x BRT)

- Auditoria offline 6/6 (PT ok, EN ok, corpo PT em destino EN reprova, corpo EN em destino PT reprova, entrevistado não citado reprova, corpo curto reprova).
- E2E disparado PELO PAINEL (pedido 20260915_002223_6a027d, vídeo t6XtiiIIMBw — Daniel Davis/Deep Dive, já transcrito): DISPATCH_OK → transcrição reusada US$ 0,00 → entrevistado identificado (lista-ouro:daniel davis) → draft 270973 «Conflito no Irã e no Iémen pode escalar e afetar toda a região» (autor 5470, cat Vídeos, capa 270972, embed no topo, meta _agente_origem) — o título REFLETIU o prompt de teste («destaque ao risco de escalada regional»). Limpeza: 270969/270974 (testes) deletados.
- Prints: scratch/print_painel_youtube_comando_form_20260915.png + print_painel_youtube_status_pedidos_20260915.png (formulário completo + tabela com pedido concluído ✅).
- Segurança: 401 público sem creds; chave ssh só executa o dispatcher; regex b64 em estrela (o quantificador {0,8192} MATA o bash 5.2 por OOM — bug achado na pele).

## Bugs resolvidos no caminho (registros de caça)

1. WP_URL sem /posts: default meu escrito incompleto (heredoc) — fix: WP_BASE normalizado + sufixo garantido. As sondas campo-a-campo (todas 201) isolaram a causa.
2. Diretório v6_data/youtube_manual inexistente no tencent → scp silencioso falhava (fail-open): mkdir resolvido.
3. Regex {0,8192} no bash = OOM kill (bash 5.2.21): trocada por estrela + [[ ${#var} -gt 8192 ]].
4. ${#VAR:-0} não existe: materializar PROMPT_B64="${PROMPT_B64:-}" antes.
5. Edição do cartão do painel (22:4x) foi SOBRESCRITA pela sessão do gráfico 30d às 23:50 (trabalharam em cima de versão sem meu patch): refeita junto com o bloco novo. Lição: sessões paralelas no painel_cctv_v6.py exigem re-conferência textual pós-restart.

## Estado / o que falta / o que preciso do Miguel

- Aconteceu: painel no ar, end-to-end provado com rascunho real, Rio Carta (e todos os temáticos) nivelados no padrão V2 do Cafezinho, campo de prompt opcional funcionando (provou no título).
- Falta: primeiro uso REAL multi-destino (sites Astro ainda não receberam pedido real — a cadeia temática é o esqueleto em produção há meses, mas o caminho manual+auditoria só rodou para o Cafezinho); fila gsn_fila congelada segue aguardando decisão.
- Preciso de você: nada para operar — é só usar: colar o link, marcar os quadradinhos, opcionalmente escrever o prompt, e clicar PRODUZIR. Os sites Astro sobem direto (padrão da casa); o Cafezinho fica em rascunho para o chefe de publicação.

— ZCode Miguel (ZM) · GLM-5.3 · 15/09/2026 00:3x BRT · painel de comando manual YouTube

## ➕ Adendo v1.1 — RESTAURAÇÃO após perda por sessão paralela (15/09 ~15:1x BRT)

- **O que aconteceu:** pedido do Miguel («recupera aí») revelou que o bloco tinha SUMIDO do painel_cctv_v6.py — a sessão do MM7 (15/09 12:2x-12:52) sobrescreveu o arquivo a partir de versão ANTERIOR à obra (o arquivo voltou a ter o cartão «plano mínimo desde 11/09» e o parágrafo «PAUSADOS por ordem sua (19/08)»). 3º caso de sobrescrita do painel (13/09 noite, 14/09 23:50, 15/09 12:52) — registrado em BUGS_ATIVOS.
- **NYC intacto o tempo todo:** youtube_manual.py + dispatcher + chave yt_manual_dispatch + v6_data/youtube_manual/ (status do pedido 20260915_002223_6a027d ainda lendo) — perda só na camada de apresentação (tencent).
- **Restauração:** patches originais achados intactos em /tmp/patch_ym_painel.py + /tmp/patch_get_ym.py; backup do estado de hoje .bak_pre_ym_restore_20260915_1510 (462.612 bytes, preserva MM7 e demais edições do dia); âncoras todas presentes (6/6); patch + rota GET reaplicados; py_compile OK; restart cctv-v6.
- **Provas pós-restauração (15:1x):** interno /youtube 200 c/ «Comando manual» + «MODO MANUAL desde 14/09 22:40» + PRODUZIR + riocarta; POST URL inválida → 400; POST sem destinos → 400; GET /youtube/manual/status → 200 JSON; público /v6/youtube sem creds → 401, com creds → 200 c/ bloco; chave dispatcher viva (uso rc=64).
- **Efeito colateral menor:** o patch original refez copy2 sobre .bak_pre_ym_painel_20260915 (histórico de 14/09 23:32 substituído pelo estado de hoje) — sem perda real de conhecimento (o conteúdo COM o bloco vivo está no arquivo atual; o pré-obra de hoje está no .bak_pre_ym_restore). Aviso para futuros: nunca deixar BAK fixo em patch reaplicável.

— ZCode/GLM-5.3 · 15/09/2026 15:1x BRT · adendo v1.1

## ➕ Adendo v1.2 — 1º pedido REAL do Miguel expôs fail-open duplo; curido e reexecutado com sucesso (15/09 ~19:2x BRT)

**O pedido:** 20260915_151528_a89dd4 (Poll FLIP/Breaking Points, xzwhoOwCq70, destinos cafezinho+gsn, 15:15 BRT) — o Miguel pediu verificação («verifica se o sistema processou de fato o video, se transcreveu, se fez matéria, se funcionou»).

**Veredito: NÃO tinha funcionado — dois fail-opens:**
1. **Transcrição falhou e o executor seguiu mesmo assim:** Transkriptor submit OK mas status=Failed em 60s; fallback yt-dlp bloqueado («Sign in to confirm you're not a bot», IP NYC); resultado 0 chars, método transkriptor_falhou — e mesmo assim redigiu. Sem base factual, a LLM **ALUCINOU aspas** atribuídas a Krystal Ball e Saagar Enjeti (draft 271151 PT + post GSN EN, 399 palavras). A auditoria da casa NÃO pega isso: checa título/tamanho/idioma/entrevistado — entrevistado não identificado + corpo ≥180 palavras = passou.
2. **Push do GSN rejeitado logado como «publicado»:** remote tinha commit novo (09b1ca1 esteira antiga) não fetchado; `git push` rodava com check=False e o log mentia. Post NUNCA chegou ao ar nessa rodada.

**Curas (15/09 ~19:2x):**
- `youtube_manual.py` patch fail-closed (.bak_pre_failclosed_20260915; py_compile OK): transcrição <500 chars ⇒ ABORTA pedido inteiro com 🔴 por destino («transcrição indisponível — nada produzido; tente de novo mais tarde»); push verificado ⇒ RuntimeError com stderr se rejeitado (destino vira 🔴 honesto).
- Repo GSN realinhado: fetch + `reset --hard origin/main` (commit fabricado 3fca6e7 descartado COM backup em `/root/agent_data/youtube_manual/descartados/`).
- Draft 271151: conteúdo backupado (`/root/descartados_yt_20260915/` no cafezinho-wp) e movido p/ LIXEIRA (aspas inventadas = inutilizável editorialmente).
- **Pedido REDISPARADO (20260915_192035_f7d739, pelo dispatcher oficial):** desta vez Transkriptor completou — 21.551 chars/252 segmentos, US$ 3,0 — draft **271200** «Pesquisa revela que republicanos são vistos como corruptos e extremos» (428 palavras, autor 5470, rascunho, SEM aspas diretas: paráfrase conservadora) + GSN «Poll Reveals Shift: Republicans Viewed as Corrupt and Extreme» pushado (974feca) e NO AR (www.globalsouth.news/blog/20260915-poll-reveals-shift-republicans-viewed-as-corrupt-and-extreme → 200; apex dá 307 p/ www, normal).

**O outro pedido da tabela (20260915_002223_6a027d):** fui EU — E2E de teste da construção do painel (madrugada 00:22, vídeo t6XtiiIIMBw/Deep Dive, prompt de teste, US$ 0 reuso). Rascunho 270973 já está na LIXEIRA.

**Pendências/recomendações:**
- 🔴 **Gate de aspas no executor** (futuro): extrair citações '…'/«…» do corpo e validar substring na transcrição (a receita manual da casa já faz isso no grep) — a auditoria atual não pega aspas alucinadas quando há transcrição parcial/curta. Aguarda «vai».
- Transkriptor é instável em submit (Failed às 15:15, Completed às 19:24 no MESMO vídeo) — retry automático 1× após 5 min valeria a pena; hoje a tabela já ensina «tente de novo».
- 271200 aguarda chefe de publicação (§137) e 271151/270973 estão na lixeira (recuperáveis por 30 dias).

— ZCode/GLM-5.3 · 15/09/2026 19:2x BRT · adendo v1.2

## ➕ Adendo v1.3 — «quem são as LLMs que estão produzindo?» (15/09 ~19:3x BRT)

**Cadeia configurada** (`config/llm_tiers.json` + CADEIA_PADRAO do nucleo_llm, NYC): DeepSeek → Kimi (moonshot-v1-128k) → GLM (glm-4.5-flash) → Qwen (qwen-plus) → OpenAI (**gpt-4o-mini**, temp 0,2) → AssemblyAI (claude-haiku-4-5, coringa pay-gateway). Temperatura tarefa youtube 0,7 (deepseek/gpt forçam 0,2). A API DeepSeek hoje serve deepseek-chat como **deepseek-flash**.

**Quem produzia DE FATO (todos os artigos do painel YM, incluindo os de hoje):** OpenAI **gpt-4o-mini** — último caminho vivo. Prova: cascata ao vivo 1,6s com deepseek 401 + kimi/glm/qwen/assemblyai «Max retries (Proxy 402)» + openai OK.

**Causas (2):**
1. `nucleo_tematico/chaves.py` no import carrega `chaves_novas.env` → `.env.unificado` → … → `.env` com setdefault (primeiro vence); o `/root/chaves_novas.env` (NYC) tinha a chave VELHA morta (****8762, sha8 f2161166) → DeepSeek 401 em toda a casa V4 temática.
2. `chaves.sh` exporta proxy IPRoyal cujo plano VENCEU (túnel devolve **402 Payment Required**) → Kimi/GLM/Qwen/Assemblyai não conectam. OpenAI passava.

**Curas (Regra Nº 4, sem perguntar):** canônica sk-a20c…bef7 (sha8 2fb56976, provada 200 nas duas pontas) espelhada para `/root/chaves.sh`, `/root/.env`, `/root/chaves_novas.env`, `/root/.bashrc` (todos com .bak_pre_ds_20260915; a linha do .bashrc não afeta o dispatcher — está após a guarda interativa — mas saiu por higiene). Chaves truncada (sk-a0c…cbef, 31 chars) e velha aposentadas dos vivos.

**Prova final:** cascata re-testada no ambiente do dispatcher: **provider vencedor deepseek, 1ª tentativa**. Produção volta a sair do DeepSeek (saldo US$ 9,95).

**Pendência Miguel:** renovar o plano IPRoyal OU remover o proxy para os hosts de LLM — até lá, o «nunca depender de um LLM só» está capenga (se DeepSeek cair, cai direto no OpenAI gpt-4o-mini, pagando às cegas — a vigília não lê saldo OpenAI).

— ZCode/GLM-5.3 · 15/09/2026 19:3x BRT · adendo v1.3

## ➕ Adendo v1.4 — proxy IPRoyal + auditoria dos verticais (15/09 ~22:5x BRT, ordem Miguel)

**Proxy IPRoyal:** session nova (uj5JUbPw) instalada no chaves.sh NYC (.bak_pre_iproyal_20260915) — mas o túnel CONTINUA devolvendo **402 Payment Required** mesmo com credenciais novas: a CONTA/plano está vencida, cura = pagar no painel IPRoyal (só o Miguel). Sem drama enquanto isso: `no_proxy` do chaves.sh já isenta api.deepseek.com e api.openai.com (iam direto), então a cascata principal (DeepSeek 1º) não depende do proxy; só os failovers Kimi/GLM/Qwen/AssemblyAI ficam bloqueados até o pagamento.

**Verticais auditados (pergunta «todos os verticais funcionando?») — SIM, todos os religados estão produzindo:**
- Ciclo V4.1 no NYC vivo e rodando HOJE: geral 7h/19h + economia 13h (flag v41_ciclo.pause inexistente) + **ciencia/tecnologia 2em2h** + **digital 3x/dia** + **geopolitica horária** (as 3 religionadas 12/09 por ordem do Miguel, sem flag). Bancos dos coletores quentes (mtimes de hoje).
- Prova ponta a ponta: pauta «Rivais da IA articulam...» aprovada pelo juiz às 21:08 → **post 271216 publicado às 21:31**. Hoje também: «OpenAI compra câmera de celular» (10:01), «Golpistas clonam voz em 10 segundos» (14:31), Milei (13:31, economia), STF/Ciro (nacional).
- Cadência menor que 100/dia de agosto é o JUIZ rigoroso (reprovou hoje: beta Samsung, release institucional de big tech, física quântica sem gancho BR — «sem_tese_ancorada_nao_escreve») — desenhado assim (curadoria), não é defeito.
- **Por que verticais nunca sofreram com a chave errada:** o ciclo V4.1 lê `/root/.env` (que sempre teve a canônica boa); só os temáticos perdiam pela precedência chaves_novas.env no chaves.py (curado no adendo v1.3). Miguel tinha razão: «está pegando chave em algum lugar errado» — nos temáticos, era.

— ZCode/GLM-5.3 · 15/09/2026 22:5x BRT · adendo v1.4
