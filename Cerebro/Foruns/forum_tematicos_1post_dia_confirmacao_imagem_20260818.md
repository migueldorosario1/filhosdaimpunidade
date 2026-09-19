# Fórum — Temáticos V4: 1 post/dia + sistema de confirmação de imagem (ordem Miguel)

**Data:** 18/08/2026 ~21:30–21:45 BRT · **Autor:** ZCode/DeepSeek · **Sessão:** "TEMÁTICOS: 1 POST/DIA + CONFIRMAÇÃO DE IMAGEM" (ZCodeProject)

**Ordem do Miguel (voz):** "O Rio Carta está com imagens erradas. Vamos fazer o seguinte: vamos reduzir para 1 post por dia para todos os temáticos e incluir sistema de confirmação de imagem para todos."

## 1. Cadência — 1 post por dia em TODOS os temáticos

- **Configs (PC do Miguel, `agent_data/configs/*.json`):** `generation.posts_por_rodada` 2→**1** nos 8 sites (aiatolah, ceara, discoverbrazil, globalsouth, mapario, mundotrilhos, railpost, riocarta). Backups `.bak_pre_1post_dia_20260818`.
- **Crontab local:** rodada `--all` das 03h REMOVIDA (mantida só a das 13h BRT); crons extras `*/8` do ceara e riocarta REMOVIDOS (o `--all` diário cobre todos). Backup `/tmp/crontab.bak_pre_1post_dia_20260818`.
- **NYC:** pipeline paralelo do Ceará (`cicero_remote`): `CEARA_BATCH_SIZE` 2→**1** (cron `15 9 * * *`). Backup `/tmp/crontab.bak_pre_1post_dia_20260818` no NYC.
- Resultado: no máximo **1 post/site/dia** (limite no código + cron 1×/dia = defesa em profundidade).

## 2. Sistema de confirmação de imagem para TODOS os temáticos

- **Causa das imagens erradas (diagnóstico):** o juiz visual era FAIL-OPEN (sem visão disponível, liberava) e o **acervo default não passava por juiz nenhum**; além disso a cascata stock (Pexels/Pixabay) vence fácil quando o Wikimedia não acha, casando por "tema amplo". Varredura nos últimos 12 posts do RioCarta: quase todos com foto de stock genérica (ex.: "CET-Rio interdita Rebouças" com foto genérica de estrada; "Fitch eleva nota do Rio" com foto genérica).
- **Novo gate final (fail-close):** `confirmar_imagem()` em `nucleo_visao.py` — veredito binário CONFIRMADA/NAO_CONFIRMADA com critério mais estrito (imagem deve retratar o sujeito/lugar/tema específico; stock genérica para fato específico = NAO_CONFIRMADA). **Provedores indisponíveis = NAO_CONFIRMADA** (post adiado, alerta Telegram 1×/dia) — o oposto do juiz.
- **Aplicado no `publicador.py`:** gate obrigatório após a hero ser resolvida, ANTES do commit — vale para TODAS as fontes (banco, Wikimedia, stock, IA, acervo default) e para TODOS os sites. Reprovada → imagem removida + post ADIADO (mecanismo `_adiar_por_falta_de_hero`, já testado).
- **Testes:** py_compile OK (pyenv 3.10.13, o do cron); **teste unitário PASSOU** — hero de cultura × matéria de cultura = CONFIRMADA; mesma imagem × título de trem Paris-Londres = NAO_CONFIRMADA (Gemini). Duas rodadas reais (mundotrilhos, globalsouth, limite 1) rodaram sem erro (posts adiados por hero indisponível — fluxo correto; o cron de amanhã completa o ciclo com o gate).

## Pendências / observações

- **Faxina retroativa do RioCarta:** os posts já publicados com imagem de stock errada continuam no ar — propor troca por imagens casadas (precedente 06/08: `fix_heroes_banco.py`). AGUARDA ordem do Miguel.
- Observação do fluxo: quando a vencedora da cascata cai na checagem de duplicação pós-padronização, o loop não testa a próxima candidata do lote (publicador.py ~L595-614) — causa adiamentos desnecessários. Correção pequena, fora do escopo desta ordem.

**O que aconteceu:** as duas ordens aplicadas e testadas. **O que falta:** a prova do gate em publicação real acontece no cron das 13h de amanhã; faxina das imagens antigas do RioCarta aguardando seu aval. **O que preciso de você (Miguel):** nada obrigatório — decidir se quer a faxina retroativa do RioCarta.

Backups: configs `.bak_pre_1post_dia_20260818` · crontabs `/tmp/crontab.bak_pre_1post_dia_20260818` (local + NYC) · snapshots `nucleo_visao.py/publicador.py.bak_pre_confirmacao_img_20260818` (pós-edição; rollback pré-edição = reversão cirúrgica documentada na memória).

## Adendo 18/08 ~22:00 — operação transferida para o LOOP LAURA (ordem Miguel ~21:50)

Ordem: "usa o loop laura, mas 1 post por dia para os temáticos." Executado: (1) crons de publicação dos temáticos DESATIVADOS no Dell (5 crons: orquestrador 13h, ceara_youtube, kimi_busca_imagem, ga4_destaques, banco_midia_sync — backup `/tmp/crontab.bak_pre_laura_tematicos_20260818`) e no NYC (pipelines `ceara-digital` e `cicero` comentados, backups idem) — Dell em SKIP; (2) pacote de 8,3MB publicado na ponte (`ponte_laura_completa/pacote_tematicos_laura_20260818.zip`: código agentes_tematicos + configs + contratos + estado dos bancos + LEIA_ME com passo a passo e nomes das chaves — valores ficam no cofre da Laura); (3) carta ZM-20260818-041 no de_dell.md pedindo ACK + 1ª rodada até 19/08 12h BRT. O banco de mídia V4 (2GB) segue no Dell por ora. **Falta:** Laura montar a operação na máquina dela e reportar ZL- com a prova.

## Adendo 18/08 ~22:10 — FAXINA DAS FOTOS DO RIOCARTA EXECUTADA (ordem Miguel ~21:55)

Ordem: "troca as fotos erradas nos posts por fotos corretas, mas não gasta muito; faz só dos últimos e deixa no rascunho outros." Executado com custo mínimo (só visão barata Gemini-flash na confirmação; zero LLM de texto; fotos novas do Wikimedia CC — grátis):
- **Últimos 10 publicados** avaliados pelo gate de confirmação: **2 fotos TROCADAS** (RioLuz/Praça São Roque → Wikimedia CC BY-SA Donatas Dabravolskas; Força Municipal/Freguesia → Wikimedia CC BY-SA Virgílio Gomes); **7 mantidas** (a confirmação aprovou a foto atual); **1 sem substituta correta → rascunho**.
- **Demais posts com hero de stock (57 antigos) → draft:true** (saem do site, ficam no repo — reativáveis com foto boa depois).
- Commit `06806ae` + push (Vercel redeploy). Custo total estimado: alguns centavos de dólar (visão).
- Pendência da faxina FECHADA. Os posts draftados podem voltar depois, um a um, quando tiverem foto casada.

## Adendo 18/08 ~22:15 — VARREdura nos outros 7 temáticos (pergunta do Miguel: "também tem erros?")

Método: últimos 10 publicados de cada site; só os com hero de stock (Pexels/Pixabay/...) avaliados pela confirmação de visão (Gemini flash, custo mínimo). **Resultado: 6 fotos erradas confirmadas em 4 sites; 3 sites limpos:**
- 🌵 **Ceará (2):** "Idosa resgatada de trabalho escravo..." (Pexels) · "Elmano: Estado tirou R$ 3,3 bi do crime" (Pixabay)
- 🌍 **GSN (2):** "Colombia's New Far-Right President..." (Pixabay) · "Venezuela Launches National Dialogue..." (Pixabay)
- 🚂 **Mundo Trilhos (1):** "Corredor inter-aeroportos... Delta do Rio" (Pexels)
- 🛤️ **RailPost (1):** "Benex wins Mainfranken rail contract..." (Pixabay)
- ✅ Limpos: Discover Brazil, Aiatolah, Mapa Rio.
- Aguardando ordem do Miguel para a faxina (mesmo método do RioCarta) ou só o gate novo cuidar daqui pra frente.

## Adendo 18/08 ~22:20 — FREIO TOTAL + faxina dos outros temáticos (ordem Miguel ~22:10)

Ordem: "vamos puxar o freio de todos. deixar publicando apenas 1 artigo por dia, com foto confirmada por visão." → regime já ativo no código (1/dia + gate fail-close) e reforçado na ponte (**ZM-20260818-042**).

**Faxina dos 6 alvos confirmados:** 1 TROCADA (Elmano/ceara — foto oficial EBC do banco de mídia, visão confirmou); 5 sem foto boa → **rascunho** (ceara idosa; GSN Venezuela; GSN Colômbia; Mundo Trilhos corredor Delta; RailPost Benex). Commits: ceara `bc9e9fe`, globalsouth `f720675`, mundotrilhos `cd806f0`, railpost `28886b6`.

**⚠️ INCIDENTE (conteve, restaurou):** o script da varredura das 22:02 apagou 23 hero images de posts no ar (bug: `os.remove` do arquivo do repo em vez de cópia em /tmp) em 6 repos. Restauradas do git na hora (`git checkout -- public/hero` — nenhuma perda; deploy Vercel não foi afetado pois a restauração antecedeu qualquer push). Lição registrada: scripts de análise NUNCA apagam arquivos do repo — trabalhar só com cópia em /tmp e apagar só o que o próprio script criou.

## Adendo 19/08 ~01:50 — caso CET-Rio "A Caminho da Escola" (foto errada apontada pelo Miguel)

O Miguel apontou o post https://www.riocarta.com/blog/20260818-cet-rio-amplia-escuta-comunitaria-em-nova-fase-do-a-caminho/ com foto errada (idoso atravessando rua — stock Pixabay). **Falso positivo do gate:** a confirmação da faxina tinha aprovado por "tema amplo". **Calibração aplicada** no `_CONFIRM_PROMPT` (nucleo_visao.py, compilado): programa/projeto/campanha/evento específico NÃO confirma com foto genérica do domínio — precisa mostrar o próprio programa/contexto exato.
- **Troca automática tentada 3×:** achou candidata perfeita no Commons ("Crossing guards mentors to our children") mas a **rede de visão pendurou** (padrão noturno conhecido — nem o timeout interno respondeu; git/dns geral ok).
- **Ação tomada:** post para **RASCUNHO** (sai do ar; commit+push OK) + candidata guardada em `agent_data/v4/riocarta/candidatas_pendentes/cet-rio-caminho-da-escola-crossing-guards.jpg`.
- **Pendência (dono: ZCode/DeepSeek, próxima sessão):** confirmar a candidata por visão (rede normalizada) e reativar o post com a foto correta — ou a Laura cuida no ciclo dela.
