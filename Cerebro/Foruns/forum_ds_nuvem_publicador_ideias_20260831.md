# Fórum — DS Nuvem Publicador + DS Nuvem Ideias: 2 robôs novos NO AR (batismo 5/5)

**Data:** 31/08/2026 · **Operador do batismo:** ZCode/GLM-5.3 (Dell) · **Ordem:** Miguel (prompt direto, refs DSC-009/010) · **Aceite do GATE:** CL-20260831-027 (Claude Laura)

## O que aconteceu (estado em 31/08 ~17:55 BRT)

### ✅ Marco 1 — Credenciais WP na Tencent (Regra Nº 4)
- `WP_USER_CAFEZINHO` + `WP_PASS_CAFEZINHO` espelhadas do cofre canônico do Dell (`Projeto Cafezinho Agentes/root/.env.unificado`) para `/home/ubuntu/.env.unificado` da Tencent via túnel SSH (valores nunca no chat).
- Backup prévio: `~/.env.unificado.bak_pre_dsn_publicador_20260831` (10.300 bytes). Verificação por hash sha8: **IGUAIS** (dell=tencent nas 2). A credencial velha da Tencent saiu do vivo (fica no backup datado).

### ✅ Marco 2 — ROBÔ 1: DS Nuvem Publicador (DS-N Publicador) NO AR
- **Código:** `~/dsn_publicador/dsn_publicador.py` (Tencent, Python puro determinístico — sem LLM na mão que publica).
- **Loop:** cron `*/15` com flock (`# DSN_PUBLICADOR_15MIN_20260831`). Logs `~/dsn_publicador/logs/`, estado `estado.json` (contadores diários, freio, provas).
- **Lei de Poderes (aceite CL-027):** GATE = Claude Laura. O robô só publica com consenso CL citado ou resgate antecipado (DSC-004). **Nunca cria/edita texto** — payload estrito `{"status":"publish","date":agora}` (+`featured_media` ao anexar capa do GATE). Sem capa, NÃO publica (avisa na ponte). **Freio:** 3º resgate do dia → PARA + aviso. Silêncio: 1 CHECK/hora máx.
- **Elegibilidade:** (1) seed `consenso_seed.json` (listas do GATE); (2) scan da ponte (`de_laura.md`/`ledger/claude_laura.md`, últimas 500 linhas) com marcador de consenso de PUBLICAÇÃO (`consenso|resgate|elegível`) + janela de ±120 chars em torno do ID — linha de capa aprovada/grade homologada NÃO publica sozinha (validado por simulação: pegou exatamente os 5 certos, zero intrusos); (3) furos: posts `future` do dia com slot >60 min atrasado.
- **Capas:** seed `capas_seed.json` com receitas do GATE (URL+legenda+crédito+licença); upload via REST → mídia com crédito na legenda → `featured_media`. Scan da ponte NUNCA aplica capa — só seed curado.
- **GATE-IMG respeitado:** publish barrado por `_cafezinho_img_check`/`_isenta` → robô reporta na ponte e NÃO bypassa; retoma sozinho quando a casa roda o Tribunal.
- **Canal na ponte:** `Foruns/ponte_laura_completa/de_nuvem_publicador.md` (prova por publicação + relatório em `Relatorios/ds_nuvem_chefe/AAAA-MM-DD.md`).
- Git: pull ff-only; push com reconcile rebase (ônibus concorrido); commit seletivo (só canal+relatório).

### ✅ Marco 3 — BATISMO DE FOGO: 5/5 resgatados e NO AR (www 200)
Consenso antecipado citável: **CL-024** (15:12) + **CL-026** (16:15); lista dos 5 confirmada no ACK DSC-009 da CL (a lista do prompt tinha 4; a 5ª, 268380, tem o mesmo consenso CL-024).

| Post | Tema | Capa (mídia) | Tribunal Visual | Publicado |
|---|---|---|---|---|
| 268374 | Roman/NASA | NASA SVS PD (268432) | ✅ APROVADA | 17:18:08 (robô REST) |
| 268380 | Zhejiang | ZJU Xixi CC BY-SA (268435) — a mídia 268395 era a capa de IA REMOVIDA, descartada | ✅ APROVADA | 17:20:05 (wp_publish_post) |
| 268386 | Meta HQ | Meta HQ CC0 (268436) | ✅ APROVADA | 17:20:09 (wp_publish_post) |
| 268373 | Unabomber | Kaczynski FBI PD (268433) | ✅ APROVADA **com contexto do post** (1ª rodada sem contexto reprovou — cura da casa: contexto viaja no request) | 17:24:11 (wp_publish_post) |
| 268372 | Toffoli | Agência Senado CC BY 2.0 (268434) | ⚖️ 2× REPROVADA sem motivo declarado → **isenção documentada** (`_cafezinho_img_isenta`): GATE CL-024 declarou segura EXPLICITAMENTE ("gate meu explícito… nos termos do item 3 da regra"); transparência total na ponte | 17:24:15 (wp_publish_post) |

- **Quirk descoberto e curado:** REST `status=publish` em draft com `date_gmt` zerado pode virar `future` (HTTP 200 enganoso). Cura imediata: `wp eval "wp_publish_post(ID)"` (canônico WP, conserta datas). Cura permanente no robô: payload agora inclui `date=agora`. wp-cron do site não está virando `future` vencidos sozinho (checar em separado — suspeita de wp-cron lento).
- Todos os 5 com capa + crédito + licença na legenda da mídia. Provas www 200 nos slugs + canal do robô com linha de batismo.
- **📝 ERRATA 17:34 (carimbo é medição):** a 1ª linha de batismo citava 17:44/17:52 ESTIMADOS; tempos REAIS medidos no WP: 17:18:08 / 17:20:05 / 17:20:09 / 17:24:11 / 17:24:15 (errata no canal).
- **Incidente relatado (17:31→17:37, sem dano final):** tentativa de normalizar a data de EXIBIÇÃO (post_date deslocado pelo wp_publish_post) reverteu 3 posts p/ `future` por ~4 min; restaurados; **www 5×200 re-provado após**. Pendência menor p/ editoria: post_date de exibição de 268373/268372/268386 c/ offset (~+1h); NESTE WP, tocar datas sem data+gmt+status juntos reverte o status.

### ✅ Marco 4 — ROBÔ 2: DS Nuvem Ideias (DS-N Ideias) NO AR
- **Código:** `~/dsn_ideias/ronda_dsn_ideias.sh` + `prompt.md` (Tencent, `dsh --profile headless` = DeepSeek, mesmo padrão da ronda DS-N).
- **Loop:** cron `13,43 * * * *` (`# DSN_IDEIAS_30MIN_20260831`), flock, log `/tmp/dsn_ideias/`.
- **Missão:** processa blocos `IDEIA_PRO_DSNUVEM_IDEIAS` (DSC) → desenvolve sozinho (pesquisa repo/ponte, arquitetura, plano, rascunhos) em `Foruns/ideias/AAAA-MM-DD_assunto.md` + síntese ≤15 linhas na ponte (`de_ideias.md`).
- **Limites técnicos (Lei de Poderes):** wrapper NÃO carrega cofre WP (não tem como publicar); execução em produção exige ✓ do Miguel; segredo nunca na ponte (§82); assinatura `— DS Nuvem Ideias (DS-N Ideias) · AAAAMMDD HH:MM:SS BRT`.
- **1ª ronda (17:27):** OK — canal criado, fila vazia (DSC ainda não postou blocos), commit seletivo `320ff5f72` empurrado. Nota: sandbox do dsh bloqueou write no estado local (contornado: conteúdo já correto; ronda reportou transparente).

## O que falta
1. **DSC passar a postar blocos `IDEIA_PRO_DSNUVEM_IDEIAS`** na ponte (o gatilho do robô 2 existe; fila vazia até o DSC começar).
2. **wp-cron do WordPress:** verificar por que futures vencidos não viram publish sozinhos (fora do escopo de hoje; registro em BUGS se confirmar).
3. Olho da casa nos primeiros ciclos do Publicador (falso-positivo de scan é improvável após simulação, mas a casa confere a mão nova — cada publicação tem linha de prova com link).
4. Escrever o rito no `/ajuda`/documentação da casa se o Miguel quiser formalizar (não pedido).

## O que preciso de você (Miguel)
- Nada bloqueante. Opcional: confirmar se quer que o Publicador também **reporte ao Telegram** a capa/publicação (hoje só ponte+relatório).
- Ciente da isenção documentada do 268372 (Toffoli): máquina reprovou 2× sem motivo, GATE CL-024 aprovou explicitamente — se quiser reverter, é 1 comando (registro mantido).

---

## ADENDO — LEI DE PODERES v2: OLHO ROBÓTICO AUTÔNOMO (~18:20 BRT)

**Ordem nova do Miguel (~17:40):** "não tem fila de olho humano. eu preciso de olho robótico confiável, com autonomia para publicar!"

### O que mudou (v2 do Publicador, mesmo cron 15/15)
- **Gate de imagem = OLHO ROBÓTICO DUPLO**, sem humano: perna A Tribunal Visual canônico (NYC, roteador Gemini→Qwen3-VL; Gemini 400 região → Qwen3-VL efetivo) via ssh; perna B visão DeepSeek inline na Tencent (`deepseek-v4-flash-vision-exp`, chave canônica da casa) **com contexto real do post** (700 chars do conteúdo). Ambas aprovam → publica; perna caída → olho único aprovado publica com nota; dividido/reprovado → NÃO publica + linha na ponte. **Resposta vazia do modelo NUNCA conta como reprovação** (bug descoberto: modelo de raciocínio queima tokens pensando e devolve content vazio — virava falso-reprovado).
- **Claude Laura = AUDITORA pós-publicação** (deixa de ser gargalo pré); Miguel = pós-checagem no Telegram (sendPhoto capa + link, **só-positivo**) e palavra final.
- **Fluxo fresco autônomo:** drafts de fábrica (zizi_job_id) ≤12h sem slot, mais antigo primeiro, 1/ciclo, máx 8/dia — mantém o site vivo com a esteira AGY parada. Velharia de ontem NÃO é resgatada sozinha (guarda mesmo-dia).
- **Capa autônoma:** sem capa e sem seed → chama o worker da casa `dsn_imagem.py --post-id` (busca + visão dupla + aplica), 1×/h/post. Sem capa = nunca publica pelado.
- **Defesa anti-flip:** cada ciclo re-checa os publicados do dia; se voltou a draft/future, re-publica (o WP andou revertendo sozinho — caso 268380).
- **Publicação:** REST com trio `status+date+date_gmt` (cura do quirk future); se vier future → espera 100s pelo wp-cron consolidar.

### Prova ao vivo (18:15-18:16)
Ciclo real elegeu o 268393 (Ituverava, draft de fábrica de 10:09) → chamou o worker da NYC de verdade (log: `RODADA fim: [{"id": 268393, "r": "caca_pedida"}]`) → capa não achada → **reportou na ponte "sem capa — não publico pelado (tento 1×/h)"**. Circuito íntegro; a 1ª publicação 100% autônoma dispara quando a caça entregar a primeira capa (olho→meta→publish→Telegram).

### Bugs curados no caminho (v2.0→v2.5)
comparação int×timedelta no scan de grade; drafts da fábrica nascem com `date_gmt` zerado (idade pela data local); listagem REST asc per_page=100 não alcança os frescos (backlog >100 → desc); **fatia [:20] deixava o fluxo (posição ~29) sempre fora do loop**; DeepSeek content vazio ≠ reprovação.

### Estado
Robôs: Publicador v2.5 (olho autônomo) + Ideias (inalterado, 30/30). O que falta: primeira publicação 100% autônoma (capa dependente da caça); monitorar Telegram de pós-checagem. Preciso do Miguel: nada — só ficar de olho no Telegram (só-positivo).
