**📱 COMANDO NO DSN CELULAR — 19/09/2026 (ordem do Miguel 18/09 ~08:5x):** o Baleia passa ao **DSN celular** (harness dsh no cafezinho-wp, **DeepSeek V4 Flash default + DeepSeek V4 Pro opção** — reconfigurado hoje: o patch era GLM sem crédito e a chave DeepSeek velha 401; chave viva dos cofres instalada, prova de vida "Sou o deepseek-v4-flash"; chave da API do serviço guardada nos 2 cofres com backup). Ciclo próprio: cron `0 7` e `0 19` no servidor → produz pela missão (prompt único + MANUAL_DE_ESTILO), commita no clone /root/Cerebro, grava no V6 via `/api/baleia-edicao` e manda Telegram com parecer no padrão Cafezinho. Edição de 18/09 ficou com o ZM (automação pausada após a tarde). Fallback Laura segue (Dell 07:30/19:30 vigiando o repo). Painel: endpoints novos `/api/baleia-dados` (pack FAROL/top7/instantâneos) e `/api/baleia-edicao` (escrita instantânea no V6). Prova DRY 18/09 09:18: edição válida de 589 palavras seguindo o manual. Detalhes: fórum adendo + memória. 

**🐋 COMANDO DE VOLTA AO ZM + PROMPT ÚNICO — 15/09/2026 ~15h BRT, ordem do Miguel ("Faz o Baleia Azul você aqui do ZM... bota um prompt único... escreve um código de fallback para cair para a Laura... tem que atualizar o V6 e tem que mandar por Telegram... 400 palavras tá bom, humanizado, até divertido"):**
- **Titular: ZM (ZCode Miguel, Dell), manhã e tarde** (automação `5 7,19 * * *`, produção às 07:05/19:05, entrega até 07:10/19:15). **Fallback formal: ZL/Laura Claude**, acionada por código determinístico (`~/bin/baleia_fallback_laura.sh`, crontab Dell 07:30/19:30 → bloc URGENTE na ponte + Telegram; watchdog Tencent 07:45/19:45 cobre Dell desligado). **DS-N Chefe APOSENTADO da editoria** (morreu no apagão de quota em 11/09; ed. 46 foi a última dele — 4 dias de silêncio motivaram a mudança).
- **INSTRUÇÃO CANÔNICA ÚNICA:** `Foruns/ponte_laura_completa/baleia_azul/PROMPT_UNICO_BALEIA_AZUL.md` — TODO editor (ZM, ZL, quem vier) segue só ele. Formato novo: ~400 palavras (350-450), humanizado/divertido, foco AUDIÊNCIA (comparativo com datas nas duas pontas, post de sucesso, posts/categorias que orientam a pauta, observação de erros, produção em 1 linha). Substitui a carta longa do DS-N e extingue a coluna_editor separada.
- **Canais:** Telegram (texto completo, limpo) + painel V6 `/v6/baleia` (automático pelo repo) + **E-MAIL REATIVADO 16/09 (ordem do Miguel)**: crons Dell 08:00/19:30 `enviar_baleia_azul_ponte.sh` → Miguel + Gabriel (gmail e @ocafezinho) via msmtp do Tencent; primeira prova de entrega 16/09 08:43 (250 OK nos 3 destinatários).
- Numeração: ed. 46 = 11/09 manhã → 47 = retomada 15/09 → 48 = 15/09 tarde.
- Obra completa (provas, rollback, riscos): `Foruns/forum_baleia_azul_prompt_unico_zm_20260915.md` + `Memorias/memoria_baleia_azul_prompt_unico_zm_20260915.md`.

**🔀 TRANSFERÊNCIA DE MÁQUINA — 18/08/2026 ~19:45 BRT, ordem do Miguel ("repassar a responsabilidade do baleia azul para o zcode laura... você fica aqui no skip"):**
A operação da editoria passa para a **ZCode-Laura** (mesmo assento ZCode, canonização 11/08 — a editoria é do assento, agora operada na máquina da Laura). Fluxo novo:
- **ZL EDITA** e publica via ponte GitHub em `cerebro/Foruns/ponte_laura_completa/baleia_azul/` (`boletim_baleia_azul_YYYYMMDD_manha.md` até 07:10 BRT e `_tarde.md` até 19:15 BRT + `coluna_editor_YYYYMMDD.md`). Ordem oficial: de_dell.md ZM-20260818-040 (commit b22e837b).
- **Dell ENVIA** (automático): `bin/enviar_baleia_azul_ponte.sh` nos crons 08:00 (e-mail) e 19:30 (e-mail + Telegram com o texto completo — live do Miguel às 20h); o e-mail ganha os blocos de audiência/saúde dos coletores locais.
- **Rede de segurança:** a vigília do Dell (automation-647b2f13, passo 0c) não produz, mas se o boletim do turno não existir no repo até 07:10/19:15 BRT, produz edição mínima de emergência (regra viva "nunca pular edição").
- Métricas que a Laura não alcança (GA4/UptimeRobot) ficam "NÃO CONFIRMADAS" no texto dela — o e-mail as cobre.

# CEREBRO NODE BALEIA AZUL

Atualizado em 19/07/2026

## Função

O Baleia Azul é o boletim diário de despertar e situação do Cafezinho Media Group.

Editor-chefe a partir de 19/07/2026, por decisão de Miguel: Claude Code.

**🔄 MUDANÇA DE COMANDO — 07/08/2026 ~10:05 BRT, por decisão de Miguel ("voce agora assume integralmente o baleia azul... deixa o claude mais livre na missão de monitorar os sites"): Kimi (ZCode) passa a ser o EDITOR INTEGRAL do Baleia Azul** — fechamento da edição (~06:00 BRT), revisão, coluna diária e saúde do envio. Claude sai do Baleia e se dedica à vigília dos sites temáticos (3×/dia) + publishing. As regras editoriais criadas na gestão Claude (linguagem de carta, datas nas duas pontas, manchetes completas, pendência só com resposta, sem custos/auditor no corpo) **permanecem em vigor**. Primeira edição Kimi: 07/08, enviada 10:20 (atrasada — a das 08:00 foi bloqueada pela trava anti-vazio porque a edição não havia sido gerada; caso que motivou a mudança). Carta de transferência na inbox do Claude (07/08 10:25) + anúncio no canal (`[KIMI-BALEIA-AZUL-MUDA-DE-MAOS]`).

**🎯 RATIFICAÇÃO E CANONIZAÇÃO — 11/08/2026 ~06:40 BRT, por decisão explícita de Miguel ("caso eu não tenha feito, então fica a decisão clara agora. voce é o novo editor do baleia azul, voce zcode, seja como glm, kimi ou qwen"):** o ZCode é o editor titular do Baleia Azul **de forma modelo-agnóstica** — independentemente do provedor ativo (GLM-5.2 / Kimi K3 / Qwen). A editoria pertence ao **assento ZCode**, não a um provedor específico. **Regra de assinatura (decisão Miguel ~06:42): a assinatura acompanha o MODELO ATIVO**, não o papel Trindade — hoje "— GLM, editor"; quando Kimi K3 voltar, "— Kimi, editor"; se Qwen, "— Qwen, editor". Consequências práticas: (1) ZCode não espera ping do Claude — produz o boletim diretamente; o cron das 08:00/18:00 dispara o `enviar_baleia_azul_v2.sh`, e o editor garante que `boletim_baleia_azul_YYYYMMDD.md` + `coluna_kimi_YYYYMMDD.md` existam antes dos horários de envio. (2) A editoria é **resiliente a failover de modelo** — a assinatura muda, a continuidade editorial não. Contexto: Claude mudo desde 08/08 23:52; 09/08 feito edição emergência (ZCode, 09:03 de 10/08, ordem Miguel 17:44); 10/08 ficou sem boletim (vigília morta 36h por bug `thought_level`); 11/08 1ª edição da nova fase produzida às 06:36 ✅ (assinatura "— GLM, editor").

**Subeditor e colunista a partir de 06/08/2026 ~19:30, por decisão de Miguel: Kimi K3 (ZCode).** ~~Fluxo: o Claude fecha a edição...~~ *(substituído em 07/08 10:05 — ver bloco acima)*. A coluna do Kimi (~100 palavras, observação humanizada do dia) entra no e-mail das 8h via `dados_baleia_azul/coluna_kimi_YYYYMMDD.md`.

**📏 REGRA VIVA PERMANENTE (Miguel, 07/08 ~11:00 BRT, via Claude → Kimi): o Baleia Azul sai 2×/dia — 08:00 e 18:00 BRT — por e-mail para Miguel + Gabriel. REGRA CRÍTICA verbatim: "não tem importância chegar atrasado... NÃO É PRA PULAR a edição, não. Faz na próxima, faz atrasado, mas pode fazer."** Atraso é aceitável; edição zero nunca. Se travar às 08h, manda 10h/12h/14h; se travar às 18h, manda 20h/22h ou junto com a da manhã seguinte. A trava anti-vazio do emissor continua valendo (nunca mandar sem edição) — quem garante a edição existir é o editor (Kimi).

Editor interino de 17/07 a 19/07/2026 e responsável pela restauração da edição #12: Codex.

Editor anterior e responsável pelo handover: DeepSeek, sob o papel Cheng.

O boletim não substitui fóruns, manifestos, recibos ou o canal. Ele apresenta uma visão geral verificável e aponta para as fontes canônicas.

## Entradas obrigatórias antes de cada edição

1. [Índice canônico do CÉREBRO](./00_CEREBRO_CANONICO.md)
2. [Índice mestre](./CEREBRO_INDEX_MASTER.md)
3. [Canal Trindade](./Foruns/canal_trindade.md)
4. Inboxes ativos em `Cerebro/Foruns/inbox_trindade/`
5. Fóruns criados ou atualizados desde a edição anterior
6. Pontos de retomada dos agentes em atividade
7. Painéis operacionais e recibos recentes
8. Estado V4 em `Projeto Cafezinho Agentes/root/v4_labs/`
9. Sites temáticos e infraestrutura quando houver mudança
10. Audiência, custos e saúde de modelos com data da última medição
11. Saúde UptimeRobot nas últimas 24 horas: estado, quantidade e duração das quedas
12. Recuperação Google: GSC, audiência por post e Core Web Vitals com comparação datada
13. Recibo mais recente do Auditor de Títulos em `Projeto Cafezinho Agentes/dados_baleia_azul/auditor_titulos_atual.md`

## Regra de atualidade

- Toda métrica deve informar quando foi medida.
- Estado não rechecado deve aparecer como desatualizado ou não confirmado.
- Circuit breaker só entra como ativo quando houver evidência recente.
- Ausência de atividade no canal não prova ausência de atividade no ecossistema.
- Mudança posterior ao horário de fechamento entra na próxima edição ou em atualização identificada.

## Regra editorial: sinais de recuperação sem fabricar otimismo

Toda edição diária deve conter uma seção chamada **Sinais de recuperação**. O
editor procura e destaca o melhor dado positivo realmente comprovado na janela,
mas nunca omite uma queda material nem transforma ausência de dados em melhora.

Ordem mínima de apuração:

1. UptimeRobot: estado atual, quedas nas últimas 24 horas, duração e motivo.
2. GA4: audiência total, comparação com a janela anterior e audiência por post.
3. GSC: cliques, impressões, CTR, posição e desempenho das URLs recentes.
4. Google News e Discover: evolução diária quando houver dados suficientes.
5. PageSpeed/CrUX/Core Web Vitals: LCP, INP, CLS, TTFB e comparação datada.
6. Melhor post ou melhor indicador do dia, com título, valor, janela e fonte.

Regras de redação:

- destacar progresso comprovado, mesmo pequeno;
- informar a data e a janela de cada número;
- comparar grandezas equivalentes;
- marcar dado atrasado como desatualizado;
- dizer “sem sinal conclusivo” quando não houver melhora comprovável;
- registrar pioras materiais ao lado dos sinais positivos;
- nunca selecionar uma janela enganosa apenas para produzir alta;
- nunca inventar, estimar ou completar número ausente.

## Cobertura mínima

- Manchete e fatos principais
- V4 e redação
- Sites temáticos
- Infraestrutura e backups
- Modelos, custos e circuit breakers
- Audiência
- Saúde do site pelo UptimeRobot
- Audiência por post e comparação com a janela anterior
- Sinal diário de recuperação no Google, positivo ou negativo, sempre baseado em dados
- Segurança e incidentes
- Decisões aguardando Miguel
- Sprints e conflitos
- Links para fontes canônicas

## Histórico localizado

| Edição | Data | Arquivo |
|---|---|---|
| 1 | 18/06/2026 | `Projeto Cafezinho Agentes/legacy_reformado_20260717/toplevel_legacy/limpeza_extra_20260717/foruns/foruns_ativos_pruning_20260717/boletim_baleia_azul_20260618.md` |
| 2 | 19/06/2026 | `Projeto Cafezinho Agentes/legacy_reformado_20260717/toplevel_legacy/limpeza_extra_20260717/top/top_level_residuo_v4_20260717/base_level_clean_20260717/markdown/boletim_baleia_azul_20260619.md` |
| 4 | 22/06/2026 | `Projeto Cafezinho Agentes/legacy_reformado_20260717/toplevel_legacy/limpeza_extra_20260717/top/top_level_residuo_v4_20260717/base_level_clean_20260717/markdown/boletim_baleia_azul_20260622.md` |
| 5 | 23/06/2026 | `Projeto Cafezinho Agentes/legacy_reformado_20260717/toplevel_legacy/limpeza_extra_20260717/top/top_level_residuo_v4_20260717/base_level_clean_20260717/markdown/boletim_baleia_azul_20260623.md` |
| 6 | 25/06/2026 | `Projeto Cafezinho Agentes/legacy_reformado_20260717/toplevel_legacy/limpeza_extra_20260717/top/top_level_residuo_v4_20260717/base_level_clean_20260717/markdown/boletim_baleia_azul_20260625.md` |
| 7 | 28/06/2026 | `Projeto Cafezinho Agentes/legacy_reformado_20260717/toplevel_legacy/limpeza_extra_20260717/top/top_level_residuo_v4_20260717/base_level_clean_20260717/markdown/boletim_baleia_azul_20260628.md` |
| 8 | 15/07/2026 | `Projeto Cafezinho Agentes/legacy_reformado_20260717/toplevel_legacy/limpeza_extra_20260717/top/top_level_residuo_v4_20260717/base_level_clean_20260717/markdown/boletim_baleia_azul_20260715.md` |
| 9 | 16/07/2026 | `Projeto Cafezinho Agentes/legacy_reformado_20260717/toplevel_legacy/limpeza_extra_20260717/top/top_level_residuo_v4_20260717/base_level_clean_20260717/markdown/boletim_baleia_azul_20260716.md` |
| 10 | 17/07/2026 | `Projeto Cafezinho Agentes/boletim_baleia_azul_20260717.md` |
| 11 extraordinária | 17/07/2026 | `Projeto Cafezinho Agentes/boletim_baleia_azul_20260717_extraordinaria.md` |
| Extraordinária ZCode | 15/08/2026 | `Projeto Cafezinho Agentes/boletim_baleia_azul_20260815_extraordinaria.md` — raio-X 1.125 posts (ordem Miguel, enviada 02:35 BRT e-mail+CCTV+Telegram) |
| 12 | 19/07/2026 | `Projeto Cafezinho Agentes/boletim_baleia_azul_20260719.md` |

Não foram localizadas edições Markdown de 20/06, 21/06, 24/06, 26/06, 27/06 e 29/06 a 14/07. Existe PDF de 20/06. A numeração indica que pode haver edição ausente ou não preservada. Não preencher lacunas por inferência.

## Avaliação editorial em 17/07/2026

DeepSeek retomou o Baleia Azul após um hiato de 16 dias e atualizou as edições 8, 9 e 10. A edição 10 cobre adequadamente a reorganização do CÉREBRO, o legado e os dois drafts V4.

Lacunas atuais

- audiência não atualizada
- circuit breakers apresentados sem evidência de rechecagem na edição
- referências antigas ainda apontam para `Projeto Cafezinho Agentes/Foruns`
- ausência anterior de link explícito ao índice do CÉREBRO
- histórico fragmentado e sem índice único
- cobertura dependente demais do Canal Trindade
- mudanças ocorridas após 10h não entram na edição sem atualização identificada

Conclusão

O editor está atualizando o boletim novamente e demonstra boa capacidade de síntese. Ainda não há evidência suficiente de que o boletim esteja capturando todo o ecossistema de forma sistemática. Este nodo passa a ser o checklist canônico para fechar essa lacuna.

## Segurança

Antes de publicar, o editor deve aplicar os [Dez Mandamentos de Segurança](./CEREBRO_NODE_COFRE_CHAVES.md#dez-mandamentos-de-segurança-para-agentes).

Nunca incluir valores de chaves, tokens, senhas, cookies, material de autenticação ou conteúdo integral de arquivos de ambiente.

## Handover editorial

- [Transferência de Codex para Claude Code](./Foruns/carta_transferencia_baleia_azul_codex_claude_20260719.md)
- [Tutorial completo do Cheng para o Codex](./Foruns/forum_tutorial_baleia_azul_handover_deepseek_codex_20260717.md)
- [Manifesto do handover](./Foruns/manifesto_handover_baleia_azul_deepseek_20260717.md)
- [Fórum de auditoria inicial](./Foruns/forum_auditoria_baleia_azul_reforma_v4_20260717.md)

## Edição vigente

`Projeto Cafezinho Agentes/boletim_baleia_azul_20260719.md`

## Operação do painel e distribuição

- Endpoint canônico `http://43.156.151.165/v6/baleia` (desde 25/07/2026; antes `/v5/baleia`, que agora responde 301 para o V6).
- **(06/09/2026) PAINEL MULTI-FONTE (cura da página travada no 01/09):** desde a unificação da Baleia no DSN Chefe (01/09, wrapper Dell OFF), os boletins chegam 2×/dia pela ponte GitHub em `Foruns/ponte_laura_completa/baleia_azul/` (`_manha`/`_tarde`) e **não** mais ao `BASE_DIR` do painel (Projeto Cafezinho Agentes, Tencent). O painel V6 (`painel_cctv_v6.py`) agora lê: `v6_data/foruns/ponte_laura_completa/baleia_azul` → clone `cerebro-miguel` (mesma pasta) → `BASE_DIR` (legado + extraordinárias), com dedupe por (data, turno) e título com fallback da 1ª linha (boletins novos não têm heading `# `). Override opcional via env `CCTV_BALEIA_DIR`. Backup `.bak_pre_baleia_ponte_20260906`; detalhes em `Foruns/forum_baleia_v6_travada_dia1_multifonte_20260906.md` + `Memorias/memoria_baleia_v6_travada_dia1_multifonte_20260906.md`.
- O endereço legado `/painel/baleia_azul.html` encaminha para o endpoint canônico.
- Emissor canônico `scratch/enviar_baleia_azul_v2.sh` no workspace local.
- Cron local às 8h e 18h.
- **Destinatários permanentes do e-mail (ordem Miguel 21/07, efetivada no script em 06/08 ~19h):** `migueldorosario@gmail.com`, `gabrielbarbosa9001@gmail.com` e `gabrielbarbosa@ocafezinho.com` (variável `DESTINATARIOS` no emissor; override de teste via `BALEIA_DESTINATARIOS`). De 10/07 a 06/08 o e-mail ia só para o Miguel — lacuna corrigida em 06/08.
- Emissor remoto antigo desativado em 17/07/2026.
- O emissor local bloqueia o envio quando não existe uma edição com a data corrente.
- O coletor `scratch/coletar_auditor_titulos_baleia.py` traz de NYC o recibo sanitizado do Auditor de Títulos.
- [Fórum da correção CCTV e envio duplicado](./Foruns/forum_correcao_baleia_azul_cctv_envio_duplicado_20260717.md)
- [Fórum correção matéria 264661 + painel V6 publicações + errata 404 (07/08)](./Foruns/forum_correcao_materia_264661_painel_v6_falso_incidente_404_20260807.md)
- Telegram aguarda rotação do token e configuração de `TELEGRAM_BOT_TOKEN` fora do código.

### Regras editoriais NOVAS (ordem Miguel, 06/08/2026 ~19h — valem a partir de 07/08)

1. **Custos NÃO entram no Baleia Azul.** Custos & LLMs viraram boletim separado (`scratch/enviar_boletim_custos.sh`, cron 8h02 e 18h02) que vai **SÓ para o Miguel**. O Auditor de Títulos também saiu do Baleia e acompanha o boletim de custos.
2. **Linguagem humanizada, tipo carta.** Nada técnico no corpo: sem siglas cruas (LCP/INP/TTFB/CTR viram frases), sem tabelas markdown, sem "macrotema_expandido" (vira "Geopolítica").
3. **Toda comparação com as DUAS datas explícitas.** Proibido "melhorou de 1,83 (02/08) para 1,67" sem dizer o dia do 1,67; proibido "comparativo com 30/07" sem dizer comparado com qual dia.
4. **Audiência obrigatória:** dia anterior (com data) + média móvel 7 dias (com as datas das duas semanas comparadas) + 14 dias + dia a dia da última semana + **editoria que mais deu audiência** + manchetes mais lidas **com título completo**.
5. **Pendências no boletim do painel:** ou têm resposta nova ou saem. Pendência velha repetida sem andamento não pode ficar parada no boletim — "não sou eu que tenho que ler" (Miguel). Cada pendência listada precisa de dono e próximo passo datado; sem isso, eliminar.
6. **Sem seção "Links canônicos"** no fim do boletim — links importantes entram no texto, em linguagem natural.
7. **Ritual Ponte Claude↔Kimi (novo):** publicada a edição, o editor avisa na Ponte; o Kimi LÊ o boletim e responde no canal — concorda? tem pendência sem resposta? falta algo? O parecer do Kimi é registrado; se apontar lacuna, o editor corrige na edição seguinte (ou em atualização identificada).

### Pipeline de coleta (atualizado 06/08/2026 — ZCode/Kimi, ordem do Miguel)

O emissor chama três coletores locais, todos com `--output-dir` absoluto para
`Projeto Cafezinho Agentes/dados_baleia_azul/` e stderr registrado em
`/tmp/baleia_azul_envios.log` (layout novo desde 06/08 ~19h — ordem Miguel):

**Baleia Azul (e-mail para Miguel + Gabriel, 8h/18h):**

| Bloco do e-mail | Coletor | Fonte |
|---|---|---|
| 📊 Audiência humanizada (ontem/7d/14d com datas explícitas + dia a dia + editoria campeã + manchetes completas) | `scratch/coletar_audiencia_baleia.py` | GA4 Data API via venv NYC + `analise_performance.json` |
| 🏥 Saúde do site (texto corrido, sem tabela) | `scratch/coletar_saude_baleia_azul.py` | UptimeRobot API v2 |
| 📈 Como estamos no Google (GSC + velocidade, em linguagem clara, datas nas duas pontas) | `scratch/coletar_sinal_google_baleia.py` | NYC `gsc/diario_*.json` + `pagespeed/diario_*.json` |

**Boletim de Custos (e-mail SÓ para o Miguel, 8h02/18h02 — `scratch/enviar_boletim_custos.sh`):**

| Bloco | Coletor | Fonte |
|---|---|---|
| 💰 Custos & LLMs (ontem/7d/30d + projeção + LLMs mais usados) | inline no emissor | `custos_consolidados` NYC (`por_modelo`) |
| 📝 Auditor de Títulos (resumo do relatório diário) | `scratch/coletar_auditor_titulos_baleia.py` | NYC `auditor_titulos_gpt/RELATORIO_ATUAL.md` |

Regras operacionais duras:

- **Python do cron é 3.8** (`/usr/bin/python3`; o pyenv 3.10 só existe no shell interativo). Todo coletor carrega fallback de timezone sem `zoneinfo`. Testar sempre com `env -i PATH=/usr/bin:/bin`.
- `BALEIA_DRY_RUN=1` monta o corpo sem enviar nada — usar para teste.
- Texto-gabarito nunca entra no corpo: se uma fonte falha, o bloco diz "indisponível nesta edição" e aponta o log. A regra editorial (§ acima) é **aplicada** pelos comparativos, não impressa.
- Assinatura neutra "Baleia Azul · boletim automático" desde 06/08 (a persona Cheng encerra o ciclo DeepSeek como emissor).
- Detalhes e evidências: `Foruns/forum_baleia_azul_melhorias_audiencia_20260806.md` + `Memorias/memoria_baleia_azul_melhorias_audiencia_20260806.md`.

### Nota sobre a divergência registrada no handover

O tutorial informa que este nodo colocaria as edições 8, 9 e 10 no legado. O registro canônico já distingue corretamente os caminhos. As edições 8 e 9 estão no legado e a edição 10 está na raiz ativa em `Projeto Cafezinho Agentes/boletim_baleia_azul_20260717.md`.

O apontamento foi preservado como demonstração do protocolo de reporte de conflitos. Nenhuma correção de caminho foi necessária.

- **(22/08/2026 → reformado 25/08) Seção "🧭 Quem fez o quê" automática:** o wrapper `~/bin/enviar_baleia_azul_ponte.sh` (passo 3.5) anexa ao final de TODO boletim antes do envio (e-mail 08:00 e Telegram 19:30) um **DIGEST COMPILADO** de autoria das últimas 24h — script `~/bin/baleia_autoria_digest.py` (formato F0.4 aprovado 24/08: máx. 8 linhas, ranking com barras + % + variação vs 24h anteriores; NUNCA lista de posts), fail-soft (API fora = boletim segue sem a seção). Edição ZL/CL não deve duplicar o bloco. Fórum: `Foruns/forum_mapa_sinais_integracoes_baleia_cctv_20260822.md` (adendo 25/08).

- **(25/08/2026) REGRAS EDITORIAIS — BOLETIM SUCINTO (ordem do Miguel ~22:10, verbatim: "o Baleia Azul tem que ser sucinto... não precisa trazer a lista de todos os posts publicados... está ficando todo estourado"):**
  1. **Sem lista de posts publicados** — nada de enumerar matérias do dia; no máximo 1-2 destaques com nome, o resto em números agregados (total, grade sem furo). Detalhe mora no painel.
  2. **Parágrafos de ~2 frases em UMA linha só** — proibido wrap/quebra de linha no meio da frase (aparece como quebra estranha no Telegram); parágrafos separados por linha em branco.
  Regra comunicada à editoria na ponte via ZM-20260825-020 (ACK pendente de ZL/CL). Vale também para qualquer digest/boletim do ecossistema (regra 24/08: compilado e bem diagramado, nunca lista crua).
- **26/08 ~10:15 (ZCode/GLM-5.3):** Baleia Azul ganhou o passo 3.7 👁 "Audiência — os 3 medidores" (GA4 × FAROL × LUMINA; ordem Miguel ~10:10). Fonte: endpoint `/api/audiencia-vertices` do CCTV; digest `~/bin/baleia_audiencia_vertices.py`; fail-soft; LUMINA com histórico eterno próprio (tencent */30 + R2/B2).
