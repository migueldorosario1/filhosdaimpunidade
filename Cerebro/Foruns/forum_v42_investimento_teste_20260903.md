# 🧪 Fórum — V4.2 CAFEZINHO INVESTIMENTO · fase TESTE instalada (03/09/2026, madrugada)

> Tema: instalação da fase TESTE do agente V4.2 Investimento no ESPELHO cafezinho.news (nunca o canônico). Ordem do Miguel (✓✓✓ na GUI ~02:4x, DSC-063): "Sim, mas no cafezinho espelho. Cafezinho.news." Execução: ZM (Dell) sozinho, 03/09 ~04:0x-04:2x BRT. Refs: DSC-051 (código do Ideias + checklist D1-D9) · DSC-060 (plano B NYC — descartado) · DSC-062 (ordem espelhar creds + watcher) · DSC-063 (aprovação + alvo 14:00).

## Decisões e estado

1. **Casa escolhida: TENCENT** (preferida na ordem; NYC plano B descartado para não duplicar cron). Deploy em `/home/ubuntu/v42_investimento_teste/`.
2. **Credenciais do espelho** espelhadas NYC→tencent por pipe ssh→ssh (valores nunca exibidos, §82); backup do cofre antes. Endpoint REST padrão do espelho OK (200) — sem `ESPELHO_WP_REST`.
3. **Watcher automático funcionou** (cron */10 da DSC-062): detectou as creds e instalou às 04:10:06, desligando-se. MAS a extração dele tinha 2 defeitos, corrigidos na hora pelo ZM com backups: script truncado (faltava `sys.exit(main())` — o cron rodaria vazio) e sem os 4 gates da v1.3 (factual mecânico, rodízio de tese, frescor de dado, anti-eco de título). Versão final: 463 linhas, gates dobrados, telemetria integrada, py_compile OK.
4. **Smoke D4:** glm-5-turbo ✅ (86 tokens) · qwen3.8-flash ❌ 429 (cota Token Plan esgotada; renova 04/09 03:15 — fallback automático do script cobre).
5. **Categoria "Investimento" criada no espelho** (id 100007) via REST — provou as creds.
6. **Telemetria desde a 1ª rodada (DSC-052/056):** modelo + tokens in/out por chamada → `v6_data/custos/v42_investimento.jsonl` + memória por rodada no deploy.
7. **Cron:** `0 14 * * 1-5` (14:00 BRT — fuso do servidor conferido = America/Sao_Paulo). 1º rascunho ~15:00; Chefe reporta ao Miguel no Telegram.
8. **Regras duras respeitadas:** draft-only (`post_status=draft` travado no código, nem flag publish existe), espelho apenas, frontier proibido nesta fase, rollback = remover 1 linha do cron (backup no deploy).

## O que falta

- **Seeds do dia (D3)** para o ciclo das 14:00: `v42_seed_agenda/mercado/coleta.json` com dados reais (sem eles o ciclo roda honesto mas magro — fail-closed, não inventa). ZM prepara de manhã.
- Relatório do 1º ciclo (Chefe → Telegram do Miguel ~15:00).
- Critério 7 (tese no barato) medido ao longo de 5 dias úteis — relatório sobe ao Miguel.

— ZCode/GLM-5.3 (ZM, Dell) · 03/09/2026 04:2x BRT

---

## 📊 ADENDO 1 — ANÁLISE DO TESTE (03/09 ~07:2x-08:0x BRT, ordem Miguel: "analisa se está dando certo")

Executor: ZM Dell (sessão ZCode/Kimi K3 — hook §113; divergência runtime×hook registrada). Fórum-irmão do incidente: `Foruns/forum_incidente_ataque_sqli_espelho_20260903.md` (ocorreu DURANTE esta análise).

### Veredito: NÃO está dando certo ainda — 0 rascunhos, 0 posts em 3 tentativas; causas raiz TODAS diagnosticadas com prova

**1. As 3 execuções manuais das 05:2x-05:31 BRT falharam (telemetria `telemetria_v42.jsonl`, 3 registros):**
- Exec 1 (08:25:12Z): 3 pernas LLM OK (glm-5-turbo, 1.503 in / 11.025 out) → POST WP devolveu **400**.
- Execs 2 e 3 (08:25:59Z / 08:31:55Z): **timeout de leitura na perna de redação** (glm-5-turbo >120s; urllib timeout=120 no `chamar_llm`).

**2. Causa-raiz do 400 — GATE-IMG do espelho (PROVADA por bateria T2-T5 às ~08:0x, com o site já curado):**
- draft mínimo: **201 OK** · draft + metas `_v42_*` pequenas: **201 OK** · draft + meta ~5KB: **201 OK** (metas e tamanho NÃO são problema).
- publish sem imagem: **400 `cafezinho_imagem_sem_checagem`** — "BLOQUEIO GATE-IMG: impossível publicar sem checagem da imagem (_cafezinho_img_check ok ou _cafezinho_img_isenta)".
- A reforma ~04:5x (ordem Miguel "pode publicar", `V42_POST_STATUS=publish` no rodar.sh) ligou publish sem cuidar do gate → TODA publicação direta do Investimento morreria no 400. Rascunhos passam livre.
- Como o irmão Estatística passa: gera imagem + Tribunal Visual (`_cafezinho_img_check {"ok":true,...,"audit_state":"approved"}` no post 400309, media_id 400307).

**3. Sem o 400 logado:** o script usa `r.raise_for_status()` sem logar `r.text` — o corpo do erro foi descartado. Cura: logar corpo em falha (lição registrada).

**4. Incidente paralelo (espelho CAIU ~07:4x BRT durante a análise):** ataque SQLi time-based (SLEEP via `OR IF(...`) da família 195.178.110.x segurava workers php-fpm (pm.max_children=5) + table locks MyISAM da wp_posts → POSTs penduravam (os meus testes T2 iniciais leram timeout) e depois o site todo. Plantão ZM: iptables DROP .22/.247 + KILL das conexões "User sleep" + `ss -K` da conexão residual → site 200 de volta (home 3,5s, REST 0,85s). DETALHE GRAVE: o SLEEP injetado EXECUTOU no banco = superfície real de SQLi (tema/plugin a auditar; canônico pode ter o mesmo buraco). Fragilidades: wp_posts MyISAM, pm.max_children=5, sem fail2ban. Fórum próprio do incidente tem o plano de endurecimento — aguarda "vai" do Miguel.

**5. Estado do deploy às 08:05:** cron `0 14 * * 1-5` intacto (1º ciclo cron HOJE 14:00 BRT); script atual sha 680ca46dc40a2f64 (reforma publish, 463+ linhas, py_compile OK); banco 55 fontes OK; categoria 100007 OK (count=0); **SEMs: seeds D3** (ciclo 14:00 será magro fail-closed), **jsonl de custos `v6_data/custos/v42_investimento.jsonl` com 0 bytes** (flush só está gravando no deploy — bug de telemetria a curar), `v42_teste_estado.json` inexistente (consequência das falhas).

**6. Irmão V4.2 ESTATÍSTICA (NYC, fora do meu deploy — dado do DS-N Ideias 06:16):** 1ª leva pós-reforma (400305/400309) publicou, mas veredito de arquiteto = **ALUCINOU derivação** (56,25% m/m · 0,58% d-1 · 1,42% 12m · 16,17% 12m sem série no rodapé) notas 4 e 3; vigia deu falso OK no 400305. Curas propostas pelo Ideias: G3 P0 (séries no rodapé) + G12 fail-closed de derivação — rascunhos na Foruns/ideias/.

### PRECISA MIGUEL (3 decisões, ponte ZD-20260903-001)

- **A. Imagem do Investimento no publish:** (1) isentar com `_cafezinho_img_isenta` [1 linha, lab] · (2) voltar a draft até a fila de capas · (3) gerar imagem + Tribunal como o Estatística.
- **B. Auditoria do vetor SQLi** espelho + canônico (o SLEEP rodou = buraco real).
- **C. Endurecimento do espelho:** fail2ban/rate-limit + wp_posts MyISAM→InnoDB + pm.max_children — plano no fórum do incidente.

Sem a palavra do Miguel até as 14:00: o ciclo cron falhará no GATE-IMG (se chegar ao POST) ou será magro (sem seeds) — nada é publicado às cegas (fail-closed respeitado).

— ZCode/Kimi K3 (ZM, Dell) · 03/09/2026 08:0x BRT

---

## 📊 ADENDO 2 — ANÁLISE DO PAR: V4.2 ESTATÍSTICA + INVESTIMENTO (03/09 ~08:1x-08:3x BRT, ordem Miguel por voz: "analisa o Estatístico, vê os gráficos, explica o Investimento, opinião sobre checagem dupla DeepSeek Vision, objetivo = levar os 2 ao canônico")

Executor: ZM Dell (ZCode/GLM-5.3). Evidências: 3 gráficos baixados e avaliados por visão (400307/400304 de hoje + 400263 de 02/09), deploy NYC inspecionado, logs lidos.

### V4.2 ESTATÍSTICA — como está configurado (NYC `/root/v4_labs/codigo/agente_economia/`)

- **Coletores 2×/dia** (10:10/20:10 UTC): economia (BCB 678 + IBGE 6 + FRED 47) e comércio exterior (comexstat/eurostat/fred/gacc/indec = 406) → envelopes.
- **Ingestor */15**: consolida no banco (dedup — hoje 730 duplicados ignorados, 1 novo).
- **Ciclo publicador 15:10 UTC (12:10 BRT)**: `ciclo_v42.py --tema auto --publicar` → tese + texto + gráfico + PUBLICA direto no espelho (cat 100005) com carimbo `_cafezinho_img_check` (Tribunal Visual do gráfico, audit_provider=deepseek_qwen_doublecheck). Onda de ontem: 400265 ok:true.
- **MARATONA HOJE** (`35 * * * *`, auto-remover 09:45 BRT, log maratona_20260903.log): pós-reforma ~01h — gerou a leva 400305→400317 (por hora, no :35). TEMPORÁRIA.
- Deploy velho `/root/agente_estatistico` (junho) = legado, NÃO é o ativo.

### Gráficos — avaliação visual (3 amostras, régua do Miguel: título + rótulos grandes + fonte embaixo + sem sobreposição)

| Gráfico | Post | Nota | Defeitos |
|---|---|---|---|
| Selic (linha) | 400309 | 8/10 | rótulo "15,00 → 14,00" encostado na linha; eixo com decimal PONTO (15.00) vs texto VÍRGULA; só 1 valor anotado |
| IPCA (barra) | 400305 | 8/10 | rótulo "0,07" colado na barra; mesmo decimal misto; sem valores nas barras |
| Comex China (linha) | 400265/400263 | 7/10 | MESMO overlap do rótulo de destaque sobre o traçado |

- ✅ Já bons: título grande (fontsize 20 bold, com a variação), fonte embaixo em todas ("Fonte: Dados Primários Oficiais | O Cafezinho Inteligência Econômica", fontsize 9), tipografia consistente, fundo escuro legível.
- ⚠️ Cura necessária (`graficos_economia_v4.py`): afastar a anotação do traçado (offset/chamada (leader line)), fontsize 10→14+ no destaque, rótulos de valor em todos os pontos-chave com anti-colisão, decimal pt-BR único (vírgula), esconder nome técnico da série (BCB_433) no título do gráfico.

### Números (dimensão texto): pendência herdada — derivações não auditáveis (notas 3-4 do arquiteto Ideias; curas G3 séries no rodapé + G12 fail-closed de derivação em rascunho na Foruns/ideias/).

### OPINIÃO sobre checagem dupla DeepSeek Vision (pergunta do Miguel) — ENDOSSE, com um fato: JÁ EXISTE METADE

- O Estatística já passa TODO gráfico por auditor visual duplo (`auditor_graficos_v4.py` + provider multimodal, carimbo deepseek_qwen_doublecheck) ANTES de publicar — e essa régua atual APROVOU os 3 gráficos com os defeitos acima = régua genérica demais.
- Proposta ZM (aplicável aos 2 V4.2): régua ESPECÍFICA de gráfico no auditor — checklist obrigatório (título legível; rótulos grandes; fonte embaixo; SEM sobreposição; decimal pt-BR consistente; sem nome técnico de série) — com reprovado → RE-RENDER automático (afastar anotação/reduzir densidade) + nova checagem, máx 2 tentativas, senão vira draft. Dupla checagem = DeepSeek Vision + 2º modelo vision (Qwen-VL ou GLM-V) para cortar falso OK (o falso OK do vigia no 400305 mostra por que 2 olhos).

### Caminho para o CANÔNICO (proposta, aguarda palavra)

1. Estatística: curar derivações (G3+G12) + régua visual de gráfico no ar + 5 dias úteis limpos → sobe com MODO CONTRATO (2 checks/assinaturas do Contrato v3).
2. Investimento: destravar o 1º ciclo (decisão A do Adendo 1) + mesmo padrão de gráfico/régua quando ganhar gráfico + 5 dias úteis medindo critério 7 (tese no barato) → idem.
3. Ordem sugerida: Estatística primeiro (já publica; só cura), Investimento atrás (precisa do 1º ciclo).

— ZCode/GLM-5.3 (ZM, Dell) · 03/09/2026 08:3x BRT

---

## 🏆 ADENDO 3 — TRIBUNAL DE MÍDIA IMPLEMENTADO E O 1º POST PUBLICADO (03/09 ~08:2x→10:0x BRT, ordem Miguel: "tem que ter imagem, obviamente... tribunal de mídia — V4.1 melhorando, não piorado")

**1º POST DO V4.2 INVESTIMENTO NO AR:** [WP#400358](https://cafezinho.news/trave-o-pico-de-14-antes-do-primeiro-corte-da-selic.htm) — "Trave o pico de 14% antes do primeiro corte da Selic", status publish, capa = gráfico 400357 (Selic 14%, série BCB_432), carimbo `_cafezinho_img_check` aprovado.

### Arquitetura entregue (script sha 6c6c55897ee0c209 + patch base64; backups `.bak_pre_tribunal_20260903` do py e rodar.sh)

1. **Gráfico** (`graficos/v42_<data>_<serie>.png`): série com mais pontos do seed de mercado; fundo escuro; título 20 bold com a variação; rótulos de valor 14 bold com offset anti-sobreposição + margem Y 30%; eixo X rotulado; fonte embaixo ("Fonte: BCB — dados primários oficiais | O Cafezinho — V4.2 Investimento (teste)"); decimal vírgula.
2. **Tribunal de Mídia (dupla checagem):** olho 1 = qwen-vl-max (DashScope, chave QWEN_API_KEY própria — não o Token Plan) vendo a imagem EMBUTIDA em base64 (não depende do site público — sobrevive à allowlist); olho 2 = juiz glm-5-turbo confere o relato contra a régua (6 itens: título, rótulos grandes, fonte embaixo, SEM sobreposição, decimal pt-BR, eixos). Régua devolve JSON {ok, nota, problemas}; dúvida/parse-falha = reprova. Telemetria das chamadas no fluxo normal (_TELEMETRIA).
3. **Fluxo WP em 3 passos (descoberta-chave):** o GATE-IMG lê a meta GRAVADA (`rest_pre_insert_post` → post_id=0 na criação) → POST nasce draft → grava carimbo por UPDATE → UPDATE status publish. É o padrão do Estatística, agora documentado.
4. **Fail-closed em cascata:** sem série (≥2 pontos) → draft; visão indisponível → draft; reprovado 2× → draft. Publicar EXIGE carimbo aprovado.
5. **Curas colaterais:** timeout LLM 120→240s (falhas 2/3 das 05:2x); log do corpo do erro WP (fim do 400 às cegas); seeds D3 REAIS de hoje gerados do banco estatístico do NYC (34 pontos: dólar BCB_1×10, Selic BCB_432×12, IPCA BCB_433×6, Fed×6).

### Provas do Tribunal calibrando (régua dura funcionando)

- Rodada 1: REPROVOU gráfico v1 (nota 4→5: título "segura em de 14,00 para 14,00" sem sentido, rótulos sobre a linha plana, eixo X sem rótulo) → **draft WP#400333** (não publicou).
- Cura do gerador com base nas críticas → Rodada 2: **nota 9** (mas POST falhou: site sob 2ª onda do ataque).
- Rodada 3 ( Tribunal via URL): visão indisponível (allowlist fechou o espelho p/ o qwen-vl) → **draft WP#400347** (fail-closed correto).
- Patch base64 → Rodada final: **nota 10, zero problemas → PUBLICADO 400358**.

Drafts de auditoria (400333/400347) mantidos como registro do fail-closed (não públicos). Cron 14:00 segue no ar com tudo isso. Pendências: telemetria do v6_data ainda 0 bytes nas rodadas falhadas (verificar na próxima corrida saudável); decisão B do Miguel (auditoria SQLi espelho+canônico).

— ZCode/GLM-5.3 (ZM, Dell) · 03/09/2026 10:0x BRT

---

## ✍️ ADENDO 4 — CAPA É FOTO (não gráfico) + título EMU-2 no redator + lote de mídia investimento (03/09 ~10:1x→10:2x BRT, ordem Miguel por voz)

1. **Título do 400358 CORRIGIDO in place** (crítica do Miguel: "não dá para entender nada"; quem escreveu foi o redator glm-5-turbo SEM a régua EMU no prompt — falha do deploy, não do modelo): "Trave o pico de 14% antes do primeiro corte da Selic" → **"Banco Central segura os juros em 14% com inflação no menor nível do ano"** (200 no ar, slug preservado).
2. **Régua EMU-2 INJETADA no system do redator** (sha novo no deploy; backup .bak_pre_emu_20260903): título = frase que qualquer pessoa entende de primeira, zero jargão de mercado, cargo junto de nome desconhecido, sem metáfora hermética, teste do leitor comum.
3. **Capa = FOTO (ordem):** gráfico passa a ser imagem do CORPO; capa sai do BANCO OURO V3 (pessoa central → foto nominal dela; senão tema do dia). Ouro hoje: 88 economia + 42 investi* + 13 Petrobras + 13 banco; lacunas: bolsa/consumo/compras/comércio/juros. Lote + caça-foto especificados em `Foruns/v42_lote_midia_investimento_caca_foto_20260903.md` (prompt canônico + 6 categorias + meta +60 fotos). Costura técnica = item #1 da Arquitetura de Mídia Unificada (adapter Ouro→capa V4.2) — próximo passo.

— ZCode/GLM-5.3 (ZM, Dell) · 03/09/2026 10:2x BRT
