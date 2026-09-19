# Fórum — Vazamento de scaffolding de LLM em post publicado (caso 269519) + cura estrutural

> Aberto em 08/09/2026 ~21:2x BRT por ZCode (Qwen3.8-Max) — ordem do Miguel: "Teve vazamento dessa sujeira no post. Pode corrigir urgente primeiro e depois fazer investigação profunda para encontrar culpado e fechar uma cura estrutural." + "aproveita e tira os travessões, que estão proibidos no manual de estilo. estranho esse post."
> Memória irmã (log técnico completo): `Memorias/memoria_vazamento_scaffolding_269519_20260908.md`

## 1. O caso (269519)

- Post **«Enquanto Lula e Flávio travam empate, um nome quase desconhecido dá o salto da rodada»** — ID 269519, publicado 08/09 21:16:39, autor 5780 (redator2 = conta de autoria do Gabriel).
- Sujeira visível ao leitor no fim do corpo: `## Bloco "Leia Mais"` + link, e `## Opções alternativas de título` com 5 títulos — markdown cru (`##`, `**`) renderizado literalmente.
- 11 travessões (—) no corpo, incl. construções `— praticamente estável —,`.
- Conteúdo em si: **verificado e real** — pesquisa Quaest/SP divulgada hoje (Bing News RSS: «Quaest em SP: Flávio Bolsonaro, 31%, Lula, 30%; Cury, 8%; Caiado, 4%; Renan, 2%; Zema, 1%», 08/09 13:36 GMT; números do post batem 1:1). O "estranho" era a forma, não o fato.
- ⚠️ A URL que o Miguel colou (`/2026-09-08/slug/`, com TRAÇOS) dá **404** — permalink do canônico = `/%year%/%monthnum%/%day%/%postname%/` (barras: `/2026/09/08/slug/`). O LLM do Gabriel fabrica URLs com traços (o link "Leia Mais" vazado `/2026-08-30/soma-de-17-pesquisas…` = 404; o real com barras = 200). O plugin WP Telegram usa `{full_url}` canônico — não é dele.

## 2. Fix urgente (EXECUTADO ✅ 21:2x-21:5x)

- **269519**: backup `Backups/posts_editados/269519_pre_fix_20260908.md` → corpo reescrito (só travessões→vírgulas/ponto; texto verbatim preservado) + truncado antes do `## Bloco "Leia Mais"` → `wp post update` com `CAFEZINHO_EDITORIAL_HUMAN_OVERRIDE=1` (post de humano, §130; ordem explícita do Miguel) → purge Rocket+wp_cache+Redis → **página pública 200, zero vazamento, zero travessão, parágrafos íntegros** (auditoria python do HTML).
- Armadilha registrada: `--post_content=@arquivo` NÃO existe — o wp-cli gravou a string literal "@/tmp/…" no post (corrigido em segundos com arquivo POSICIONAL: `wp post update <id> /tmp/arquivo`).
- **Varredura SQL** (LIKE '%Opções alternativas de título%' OR '%Bloco "Leia Mais"%', todos os posts): + 1 publish doente — **267466** (24/08, «O cerco se fecha… TRE-SP/Marçal», versão HTML `<strong>Leia Mais:</strong>` + `<ol>` de 5 títulos) → **corrigido ✅** (backup `267466_pre_fix_20260908.md`, truncado, override, purge, página 200 limpa). Os 9 travessões do corpo dele NÃO foram tocados (ficam no relatório sistêmico). + 1 draft — **268459** (autor 5735): metatexto de LLM no topo («Sem sobreposição direta — episódio novo… Segue a matéria…») — NÃO tocado (rascunho humano; o mu-plugin novo limpa no próximo save; sweeper alerta).
- Travessões sistêmicos: **~58 posts publish desde 01/09** (tabela completa na memória irmã). Maiores: 269173 (30), 269144 (27), 268553 (18), 268993 (17), 269155 (16), 269085 (15), 268537 (15). Autores: maioria 5780 (Gabriel), mas também 5470, 5786, 5801, 5795, 2018, 1257.

## 3. Investigação — o culpado

- Meta `_cafezinho_origem` (mu-plugin de proveniência) prova: 269519 criado via **wp-admin, user 5735 (gabrielbarbosa = Gabriel), UA Android/Chrome Mobile, 21:12:27** → publicado 21:16:39. 267466: mesmo user 5735, **Windows/Chrome**, 24/08 11:56 → 12:00.
- Mecanismo: **Gabriel cola a resposta BRUTA do próprio LLM** (prompt pessoal que pede «Bloco "Leia Mais"» + «Opções alternativas de título» — o template NÃO existe no ecossistema: grep zero hits no workspace Dell) direto no editor e publica em <5 min. Pelo celular, sem revisar.
- Por que nenhum gate pegou: publicação humana direta (§130/§132 — gates de robô não barram humano; R1/R2 varrem draft/future em cron :05/:20 e a janela de 4 min escapou; 5780/5735 NÃO estão nas listas de autores automáticos do guardião `{5470,5786,5787}` e do filtro R1 `{5470,5786,5787,5801}` — corretamente, são humanos).
- Family history: 268459 (metatexto) e o caso 269169 (parecer como matéria, 06/09) são a mesma doença — LLM fala ANTES do texto e o operador cola tudo.
- Conteúdo factual: OK (ver §1). Mas posts do Gabriel NÃO passam por fact-check R1 — decisão pendente do Miguel desde a auditoria 07/09 ("fact-check LLM também p/ humanos?"). Este caso reabre a pergunta.

## 4. Cura estrutural (NO AR ✅ 21:5x)

1. **Camada 1 — mu-plugin `cafezinho-filtro-scaffolding.php`** (cafezinho-wp, wp-content/mu-plugins/): filter `wp_insert_post_data` remove no SAVE (qualquer autor, qualquer canal que passe pelo WP): blocos «Bloco "Leia Mais"»/«Opções alternativas de título» (markdown E HTML) cortando do 1º marcador até o fim + metatexto de abertura conservador («Sem sobreposição direta/Segue a matéria/Conforme pedido…», 1º parágrafo ≤500 chars) + aviso de markdown cru (≥2 sinais: `## `/`**negrito**`/`[x](http`). **NÃO toca status/data/autor (§130)**; original fica nas Revisões; log no option `cafezinho_scaf_log` (últimos 200); admin notice avisa o editor no wp-admin ("cole só a matéria — confira seu prompt na IA"). Testes: php -l OK + **7/7 PASS** em eval-file com os casos reais (md 269519, html 267466, metatexto 268459, 2 controles limpos sem falso-positivo, 2 resíduos zero). Precedente da casa: `cafezinho-legenda-limpa.php` (ordem Miguel 17/08).
2. **Camada 2 — sweeper `/root/verificador_vazamento.py`** (cafezinho-wp, cron `*/15` flock, marker `VAZAMENTO_SWEEPER_20260908`): varre publish+future+draft com post_modified ≤3h (qualquer autor), anti-loop sha1, NUNCA edita post — flags em `/root/agent_data/vazamento_flags.jsonl` (bloco_interno/metatexto_abertura/markdown_cru/travessoes:N). Prova ao vivo na 1ª corrida: 🔴 269523 (travessoes:8, recém-publicado do Gabriel), 267466 (travessoes:9 residuais), 269516 draft (travessoes:2 — útil p/ sessão dona do só-Kakay); 269519 pós-fix = ok limpo.
3. **Camada 3 — ronda ZM Vigia P2.6** (automation-94fb93f2 atualizada 21:5x): consome o JSONL a cada hora → Telegram ao Miguel (bloco_interno/metatexto/markdown_cru = 🔴 urgente; travessoes = 🟡 boletim) + se flag de bloco_interno aparecer em post salvo DEPOIS da cura = investigar falha do filtro.

## 5. Estado da missão

**O que aconteceu:** 2 posts publicados limpos e verificados (269519 completo: vazamento+11 travessões; 267466: vazamento) · culpado e mecanismo identificados com prova (meta origem + UA + horários) · URL-traços desmascarada (fabricação do LLM do Gabriel, 404 provado) · conteúdo factual confirmado · cura em 3 camadas no ar e testada · monitor com linha da missão.

**O que falta (AGUARDA "VAI" DO MIGUEL — nada aqui foi feito sem ordem):**
1. **Travessões retroativos**: ~58 posts publish desde 01/09 (lista na memória). Reescrever travessão exige juízo linguístico (vírgula? ponto? parênteses?) — proposta: missão em lote com revisão por post + backup, nos PIORES primeiro (269173=30, 269144=27, 268553=18…). Posts de humano = override só com ordem dele, um a um ou lote autorizado.
2. **269523** (Gabriel, 21:31, 8 travessões, publish): quer que eu limpe agora como fiz no 269519?
3. **Manual de escrita**: v2.1.1 diz "travessão: parcimônia… régua é preferência, não proibição" — sua ordem de hoje ("estão proibidos") é MAIS DURA. Atualizar o manual + regex do apêndice do verificador p/ travessão = proibido?
4. **Recado ao Gabriel** (e-mail, como o das apostas 25/08): orientar a colar só a matéria (o mu-plugin já limpa, mas o prompt dele devia parar de gerar scaffolding/URLs com traços). Minuta pronta mediante seu OK — envio externo precisa da sua autorização.
5. **Fact-check p/ textos humanos** (pendência da auditoria 07/09): reabrir?
6. Travessão nos robôs: incluir como flag de forma no R2/juiz2 V4.1 — arquivos NYC compartilhados com sessões ativas (§112); faço mediante "vai", sem colisão.

**O que preciso de você (Miguel):** itens 1-6 acima (cada um é um "vai" independente).

## 6. Registro

- Backups: `Backups/posts_editados/269519_pre_fix_20260908.md` + `267466_pre_fix_20260908.md` (conteúdo original verbatim + rollback de 1 comando).
- Catálogo: CEREBRO_NODE_BUGS_RESOLVIDOS.md + CEREBRO_NODE_ESTILO.md + CEREBRO_NODE_ATUALIZACOES.md.
- Relacionados: `forum_gate_data_dia_semana_269341_20260907.md` (mesma falha de cobertura: humano direto no wp-admin) · `forum_qualidade_curadoria_juiz_v41_20260907.md` (§11 auditoria R1/R2) · memória `wp-edit-human-post-423-cache-purge-20260827` (receita override+purge).

**➕ 10/09/2026 12:2x — item «recado/e-mail ao Gabriel» CUMPRIDO (ordem direta do Miguel no chat):** email enviado a **gabrielbarbosa@ocafezinho.com** (+ gmail dele em Cco e Miguel em Cco), assunto «Conteúdo comercial entra como PÁGINA, não como post (orientação editorial)» — regra: notícia/editorial = post; material comercial/promocional/serviço de terceiros = PÁGINA; caso-escola citado (269729 «Assinar PDF Online» — movido de post para página na mesma hora, com a porta CAFEZINHO_EDITORIAL_HUMAN_OVERRIDE prevista no próprio plugin de proteção, sob ordem do dono). Envio via Gmail da casa (SMTP_SSL, senha de app do cofre — nunca exposta), zero recusados. — ZM · ZCode/Qwen 3.8 Max
