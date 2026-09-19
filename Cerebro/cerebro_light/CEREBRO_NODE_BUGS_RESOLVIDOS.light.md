# CEREBRO_NODE_BUGS_RESOLVIDOS — VERSÃO LIGHT
> Gerado automaticamente por `cerebro_light.py` em 2026-07-09 03:32 BRT
> Original: `CEREBRO_NODE_BUGS_RESOLVIDOS.md` (326KB) — 96 entradas totais
> Este arquivo é READ-ONLY. Edite sempre o original.

---

## CABEÇALHO ORIGINAL (primeiras linhas)

# CEREBRO_NODE_BUGS — Resolvidos e Histórico
> Gerado por F3 Reforma Cérebro em 2026-05-24 23:25 BRT
> Origem: `CEREBRO_NODE_BUGS.md` (ORIGINAL INTACTO — este arquivo foi gerado por split)
> Descrição: Bugs ✅ CORRIGIDO/FECHADO — memória de padrões e lições
> Busca: `python3 cerebro.py --buscar <termo>`

---

## BUG-20260610-1350-TITLECASE-ILHA-FANTASMA ✅ RESOLVIDO

| Campo | Detalhe |
|---|---|
| **Detectado** | 2026-06-10 12:21 BRT por Miguel do Rosário (publicação #257430). |
| **Sintoma** | Post "A Ilha Fantasma que Apareceu em Mapas por 500 Anos e Nunca Existiu" (#257430) publicado com titulação americana (Title Case indevido em português do Brasil). |
| **Causa raiz** | A API do Brave Search estava esgotada na produção (HTTP 402), fazendo com que a busca por contexto web falhasse. A função `corrigir_capitalizacao_titulo` em `/root/titulo_utils.py` desviava para o fluxo determinístico, mas este não executava a normalização de caixa baixa (`_normalizar_title_case_ptbr`) sobre o título de entrada original, mantendo a titulação americana gerada pelas IAs de redação. |
| **Cura estrutural** | Ajustado `/root/titulo_utils.py` para que, se o título parecer Title Case americano (`_parece_title_case_americano(titulo)`) e a busca preliminar/chamada preliminar à LLM falhar, o script execute a normalização determinística imediata `titulo = _normalizar_title_case_ptbr(titulo)` no início do bloco de fallback. Desta forma, todas as correções de nomes compostos e entidades subsequentes operarão sobre o título já em Sentence Case. |
| **Backups §82** | `/root/titulo_utils.py.bak_pre_normalizacao_20260610_134321` no servidor remoto e local. |
| **Validação** | `py_compile` executado com sucesso localmente e remotamente. O processo agora normaliza deterministicamente títulos americanos em português mesmo se as conexões de rede e cotas de API de busca falharem 100%. |

---

## BUG-20260610-1350-MAYRABOT-CRASH-NETWORK-ERROR ✅ RESOLVIDO

| Campo | Detalhe |
|---|---|
| **Detectado** | 2026-06-10 12:21 BRT por Miguel do Rosário (ausência de pings). |
| **Sintoma** | O bot Mayra (Maíra Botes) e alertas do Agente de Eleições e Analytics pararam de ser entregues após 12:21 PM. |
| **Causa raiz** | O script `/root/bot_mayrag_v3.py` sofreu um crash de rede do Telegram (`telegram.error.NetworkError: httpx.ReadError / Bad Gateway`). Como ele era executado em background via `nohup` manual e não estava sob controle ativo do systemd (o serviço `/etc/systemd/system/mayrag.service` estava disabled e desatualizado apontando para a v2 legada), o processo permaneceu morto sem reiniciar. |
| **Cura estrutural** | 1. Atualizado `/etc/systemd/system/mayrag.service` na produção para executar o script correto `/root/bot_mayrag_v3.py`. <br> 2. Configurado o daemon do systemd para monitoramento contínuo com reinício automático rápido (`Restart=always`, `RestartSec=10`). <br> 3. Habilitado e iniciado o serviço (`systemctl daemon-reload && systemctl enable --now mayrag`). |
| **Backups §82** | `/etc/systemd/system/mayrag.service.bak_20260610_144412` no servidor remoto. |
| **Validação** | `systemctl status mayrag` validado em produção como `active (running)`. O bot de controle agora é resiliente e se recuperará sozinho em 10 segundos de qualquer queda de rede futura da API do Telegram. |

---

## BUG-20260606-1035-PUBLISH-VAZIO-256637 ✅ MITIGADO (causa raiz pendente)

| Campo | Detalhe |
|---|---|
| **Detectado** | 2026-06-06 10:35 BRT por Claude Maestro (Loop §53 tick 1 — monitor 30min reativado). |
| **Sintoma** | Post **#256637** publicado em 2026-06-06 09:42:26 BRT com **título VAZIO** (`title.rendered == ""`) e corpo de **25 chars visíveis** ("Com informações de VEJA."). Author=5470 (Redator agente). FM=256636 OK. |
| **Causa raiz suspeita** | Hard filter `_aplicar_trava_payload_minimo_publicacao` em `motor_publicador.py` provavelmente não cobre `title == ""` (string vazia) — só `title is None` ou ausente. Payload com título vazio escapou da Fase B. Não confirmado em código (escalável Codex/Kimi). |
| **Mitigação imediata (§51)** | Rebaixado para `draft` via WP REST API. Conteúdo não tinha matéria real (só rodapé "Com informações de VEJA.") → sem perda editorial. Respeita "soltar-posts-não-prender" (não era post válido). |
| **Pendência** | Codex/Kimi confirmar e endurecer trava: `if not title.strip(): status='pending'`. |
| **Lição** | Tribunal hard-filter precisa validar título VAZIO (`""`) e corpo abaixo de threshold (ex: <100 chars visíveis) como sinal definitivo de falha LLM/payload truncado. |

---

## BUG-20260606-1035-DUPLICATA-CNH-256618-256610 ✅ MITIGADO (cooldown não pegou)

| Campo | Detalhe |
|---|---|
| **Detectado** | 2026-06-06 10:35 BRT por Claude Maestro (Loop §53 tick 1). |
| **Sintoma** | Duplicata Lula CNH publicada com 31min de diferença: #256610 (07:51 BRT, 2886 chars, título completo) e #256618 (08:22 BRT, 1402 chars, título truncado). Mesma pauta sanção CNH renovação automática, mesmo author 5470. |
| **Causa raiz suspeita** | `util_topic_cooldown` (merge Kimi 05/06 19:30 + `fonte_url_comum`) não detectou o cluster. Hipóteses: (1) fontes diferentes evadem `fonte_url_comum`; (2) Jaccard título não atingiu threshold (títulos parecidos mas não idênticos); (3) regra `topic_cooldown.json` para "CNH" / "renovação" não existe ainda. |
| **Mitigação imediata (§51)** | Rebaixado #256618 (mais novo + versão truncada) → draft. Mantido #256610 (mais antigo + completo). Cerco §90 anti-duplicatas Jaccard alto. |
| **Pendência** | Investigar log `/root/agent_data/topic_cooldown.log` na janela 07:30-08:30 BRT 06/06; considerar regra `topic_cooldown.json` para clusters "Lula sanciona". |
| **Lição** | Cluster pauta-Lula-decreto via fontes diferentes (gov.br + replicação) ainda escapa do cooldown. Sinal de qualidade do cerco — não é falha gravíssima, é refinamento. |

---


---

## ⏩ 91 entradas antigas omitidas
> Para ver o histórico completo, leia `CEREBRO_NODE_BUGS_RESOLVIDOS.md` diretamente.
> Busca rápida: `python3 cerebro.py --buscar <termo>`

---

## ÚLTIMAS 5 ENTRADAS

## ✅ BUG-20260529-LULA-COLETOR-SECO — Coletor Lula 0 pautas em 24h (RESOLVIDO)

| Campo | Valor |
|---|---|
| **ID** | BUG-20260529-LULA-COLETOR-SECO |
| **Detectado** | 2026-05-28 (ticks 77-80 loop Maestro §90), confirmado 29/05 09:32 ("todos os bancos Lula vazios, indo dormir") |
| **Detector** | Claude Maestro (loop §90) + parecer Kimi (Engenheiro Chefe) |
| **Sintoma** | `robo_coleta_lula.py` aprovou 0 matérias em 24h; banco bruto sem pauta nova desde 27/05 19:00 (#252316). Master Lula dormia por banco vazio. |
| **Causa raiz** | (1) Pré-filtro `RE_SUJEITO_LULA.search(e.title)` só olhava o TÍTULO → descartava ~25 matérias/ciclo com "Lula"/"governo Lula" no corpo. (2) Apenas 4 feeds institucionais de baixa frequência (Planalto/Agência Brasil/YouTube/Flickr) — sem grande mídia. |
| **Fix

> *(... 2019 chars omitidos — ler original)*

---

## BUG-20260529-PERFORMANCE-IMPORT-RE-FALTANDO ✅ RESOLVIDO

| Campo | Detalhe |
|---|---|
| **Detectado** | 2026-05-29 16:15 BRT (tick §90 Claude Maestro) |
| **Severidade** | 🟢 BAIXA — `agente_performance.py` é orientador (sugere pautas via GA4), não bloqueia publicação |
| **Sintoma** | `agente_performance.py:289` → `NameError: name 're' is not defined` em `_extrair_padroes_sucesso` (`any(bool(re.search(r'\d', t)) for t in titulos)`). Pesos/macrotemas GA4 calculados, mas crash ao extrair padrões de sucesso. |
| **Causa** | Módulo usa `re.search` (linha 289) mas nunca importa `re`. Imports eram os/json/requests/Counter/datetime — faltava `re`. |
| **Cura** | `import re` adicionado na linha 9 (após `import os`). py_compile OK. §51 simples (1 linha, sem motor/cron/financeiro). |
| **Deploy*

> *(... 499 chars omitidos — ler original)*

---

## BUG-20260529-SOBRENATURAL-DEEPSEEK-GATEWAY-ASSEMBLYAI ✅ RESOLVIDO

| Campo | Detalhe |
|---|---|
| **Detectado** | 2026-05-29 16:15 BRT por Claude Maestro no tick §90 |
| **Sintoma** | `agente_sobrenatural.py` acumulava erros `AssemblyAI HTTP 400: model deepseek-v4-pro is not supported`; 185 ocorrências no dia. |
| **Causa** | Regressão de configuração feita por Codex em 24/05: roles `auditor`, `redator`, `revisor` e `fact_checker` migrados para `deepseek-v4-pro`, mas o agente Sobrenatural chama diretamente o gateway AssemblyAI, que não suporta esse modelo. |
| **Cura** | Codex reverteu os 4 roles para `claude-haiku-4-5-20251001` em `/root/agent_data/agente_sobrenatural_modelos.json`. `publicador` já estava nesse modelo e foi preservado. |
| **Deploy** | Tencent, 2026-05-29 16:28 BRT. A

> *(... 790 chars omitidos — ler original)*

---

## BUG-20260530-SEGUNDO-A-FONTE-PUBLICADOR-CHINA ✅ RESOLVIDO

| Campo | Detalhe |
|---|---|
| **Detectado** | 2026-05-30 04:00 BRT por Miguel no post `#253568` "Fazendo o mundo explodir" |
| **Sintoma** | Texto publicado com formula editorial inaceitavel: "Segundo a fonte" em tres paragrafos e fechamento burocratico "Fonte: Asia Times". |
| **Autor visivel** | WordPress: `Redação` (`author=5470`). |
| **Agente real** | `publicador_china_triade` via `/root/publicador_china.py`; log Tencent mostra publicacao do post `253568` as 03:25 BRT. |
| **Causa raiz** | `root/coletor_china.py` instruia o redator a atribuir com "Segundo a fonte"; `root/publicador_china.py` nao limpava nem vetava essa atribuicao vaga antes de publicar. |
| **Cura editorial** | Post `#253568` corrigido via REST WordPress,

> *(... 950 chars omitidos — ler original)*

---

## BUG-20260602-QUALIDADE-5-CORRECOES-PONTUAIS ✅ RESOLVIDO PONTUALMENTE / ESTRUTURAL PENDENTE

| Campo | Detalhe |
|---|---|
| **Detectado** | 2026-06-02, ticks §53 do monitoramento Claude. |
| **Fórum** | `Foruns/registro_erros_qualidade_redacao.md` |
| **Posts corrigidos** | `255344`, `255353`, `255358`, `255371`, `255369` |
| **Sintomas** | Pontuação órfã; topônimo em minúscula; título placeholder; Title Case importado + sufixo `– MoD`; idiom inglês traduzido literalmente. |
| **Cura pontual** | Claude corrigiu via WP REST, mantendo `publish` e slug. Codex auditou via WP REST público em 2026-06-02 17:15 BRT e aprovou as cinco correções de título/grafia. |
| **Ressalva** | #255358 manteve slug `titulo-editorial-texto` e `featured_media=227448`; o título foi curado, mas a rota degradada s

> *(... 910 chars omitidos — ler original)*

---

## PONTEIROS
- Original completo: [`CEREBRO_NODE_BUGS_RESOLVIDOS.md`](./CEREBRO_NODE_BUGS_RESOLVIDOS.md)
- Índice geral: [`indice_cerebro.json`](./indice_cerebro.json)
- Busca: `python3 cerebro.py --buscar <termo>`
- Validador: `python3 validar_cerebro.py`