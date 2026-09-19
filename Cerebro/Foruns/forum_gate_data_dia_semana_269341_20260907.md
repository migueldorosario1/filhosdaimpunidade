# FÓRUM — GATE DATA×DIA-DA-SEMANA + correção do post 269341 (07/09/2026)

> **Tema:** erro de calendário publicado no portal («neste domingo (7)» numa SEGUNDA-feira 07/09) → correção pontual + aperto estrutural da cadeia de qualidade (juízes, revisores R1/R2, publicador externo + sweeper pós-publicação novo).
> **Ordem do Miguel (07/09 ~12:5x):** "confere esse texto. domingo 7? domingo foi dia 6. analisa isso e corrige da melhor maneira" + "e a depender da gravidade do erro, abre forum e faz as correções estruturais necessárias, apertando juizes, revisores, além do publicador externo" + "vai".
> **Executor:** ZCode (Kimi K3) — sessão Dell 07/09 tarde. **Gravidade: ALTA** (erro factual de calendário na 1ª frase de post publicado, com ~1h50 no ar e disparo ao Telegram às 12:35).

## 1. O caso

Post **269341** «Estadão esgota a paciência com as versões de Flávio sobre o dinheiro de Vorcaro» (publicado 07/09/2026 11:23:10) abria com: *"O Estado de S. Paulo publicou, neste domingo (7), um editorial…"* — **07/09/2026 é segunda-feira; domingo foi dia 6**.

**Verdade factual apurada (3 fontes):** o editorial «Cronicamente mendaz» saiu na **segunda-feira 07/09**: (a) Google News RSS do próprio Estadão: pubDate `Mon, 07 Sep 2026 06:02:00 GMT` (03:02 BRT); (b) Brasil 247 noticiou como novidade às 06:01 BRT de 07/09; (c) o post foi criado às 09:47 e o editorial nem existia no domingo. Demais fatos do texto conferem (US$ 1,666 mi → Havengate em 16/09/2025, via piauí ✓; "quatro meses depois" de maio/2025 ✓; 2º editorial duro em <1 semana ✓; PF/Mendonça ✓).

## 2. Forense — como passou por TODOS os filtros (4 elos falharam)

1. **Confecção:** texto escrito por HUMANO via wp-admin (meta `_cafezinho_origem`: via admin, user 5735 gabrielbarbosa, 09:47; autor atribuído 5780 redator2 "Redação").
2. **R1 (fact-check) NUNCA o veria por desenho:** a varredura filtra autor ∈ {5470, 5786, 5787, 5801} — autor 5780 está FORA da lista. (E no dia os ciclos 10:05/11:05 ainda morreram — achados A/E da auditoria.)
3. **R2 revisou às 11:22:04 e reprovou (ok=false)** — mas por título/olho; o erro de data não estava no radar (o prompt dizia só "Hoje é 07/09/2026", sem dia da semana).
4. **Publicação ignorou o check:** com ok=false gravado às 11:22, o post foi publicado às 11:23:10 — nenhuma camada tem poder de bloqueio sobre publicação humana, e não havia varredura pós-publicação.
5. Resultado: erro no ar 11:23→13:09 (~1h50) e no Telegram 12:35 (mensagem enviada com o erro — não editável aqui; registrado).

## 3. Correção do post (FEITA e provada)

- `neste domingo (7)` → `nesta segunda-feira (7)` — wp-cli no canônico com `CAFEZINHO_EDITORIAL_HUMAN_OVERRIDE=1` (post de humano, ordem expressa do Miguel); status/data/slug intactos; `post_modified` 16:09 UTC.
- **Prova pública:** página ao vivo com 5 ocorrências do texto novo e 0 do velho (og:description, excerpt, corpo, schema).
- Backup + rollback de 1 comando: `Cerebro/Backups/posts_editados/269341_pre_fix_20260907_content.md` + `..._meta.json`.

## 4. Correções estruturais (o "aperto" — NO AR 07/09 ~13:2x BRT)

### 4.1 Novo módulo determinístico `data_semana_gate.py` (zero LLM, custo zero)
Valida coerência data×dia-da-semana contra a data de referência do post: padrões `domingo (7)`, `terça, 8 de setembro`, `7 de setembro (domingo)`, `ontem (5)`/`hoje (7)`/`amanhã (8)`. **Regra anti-falso-positivo: só sinaliza com data numérica EXPLÍCITA contraditória** («neste domingo» sem número é válido). Suíte: **22/22 casos OK**; prova real: flaga o texto original do 269341 e não flaga o corrigido. Cópias: Tencent `/home/ubuntu/dsn_shared/`, NYC `/root/v4_labs/codigo/`, cafezinho-wp `/root/`.

### 4.2 Revisor R1 (Tencent, `dsn_revisor1.py`, cron :05/h)
- **Gate data×dia roda para TODO autor** (inclusive humano/redator2 — fecha o elo 2 da forense); incoerência = check `ok=false` com pendência `DATA×DIA: …` mesmo sem gastar LLM.
- Fact-check com busca segue só para autores automáticos (economia).
- **Achado A fechado:** varre `draft,future` (antes: só draft → CL agendava em ~15 min e o post publicava sem check); janela aceita agendados até +7 dias.
- **Achado B fechado (loop de re-revisão):** gate de "já revisei" por **sha1 do conteúdo** (o POST do meta bumpava `modified_gmt` e o gate antigo nunca fechava — re-revisão horária).
- Achado E: `gravar_check` com try/except (crash 11:05 não se repete). Achado F: NameError `tag` corrigido.
- Prompt passa a dizer o **dia da semana de hoje** + regra explícita de calendário.

### 4.3 Revisor R2 (Tencent, `dsn_revisor2.py`, cron :20/h)
- Gate data×dia mesclado ao veredito (pendência automática força `ok=false`); se a escada LLM cair mas o gate reprovar, o check mecânico é gravado mesmo assim.
- Mesmos fixes: `draft,future`, hash anti-loop, try/except, NameError, prompt com dia da semana.
- **Achado D fechado:** `max_completion_tokens` gpt-5 1200→4000 (reasoning comia o budget → "resposta vazia" recorrente).

### 4.4 Publicador externo (Tencent, `dsn_publicador.py`, cron */15)
- **Gate data×dia BLOQUEANTE** entre o check de imagem e o publish: incoerência = NÃO publica, linha na ponte `de_nuvem_publicador.md`, post segue elegível (quem corrigir o texto destrava). Import do módulo falhar = fail-open logado (não para a casa).

### 4.5 Juiz 2 do V4.1 (NYC, `v41_ciclo.py`)
- Gate sobre título+texto real do draft (pós-cura do texto-vazio): incoerência = **reprovação de forma** (`modelo: data_semana_gate`) → salva-drafts arquiva o texto, post à lixeira, pauta volta ao lote pelo cooldown de 6h.

### 4.6 Sweeper pós-publicação (cafezinho-wp, `/root/verificador_datasemana.py`, cron */15) — **a rede final que faltava**
Varre posts PUBLICADOS nas últimas 3h (cobre **publicação humana**, que não passa pelo publicador nem sempre pelos revisores na janela). Nunca edita post (regra da casa) — grava flag em `/root/agent_data/datasemana_flags.jsonl` + log. **A ronda ZM Vigia 1/1h (automation-2a8954e2, :12/h) ganhou o passo P2.5**: lê as flags e dispara 🔴 Telegram ao Miguel na hora. 1ª execução ao vivo: OK (varreu 269363/269358, sem flags).

### 4.7 O que NÃO foi fechado (documentado, sem "vai" específico)
Achados C (busca falseável do R1 — flag `busca:sim` por nome de perna), G (meta some pós-publish — apurar com a CL), H (CORREÇÕES com pendências vazias — re-parse gpt-5). Desenhados na auditoria da manhã (§11 do fórum de qualidade); aguardam janela própria.

## 5. Backups / rollback (1 comando cada)
- Tencent: `dsn_revisor1.py.bak_pre_datasemana_20260907`, `dsn_revisor2.py.bak_pre_datasemana_20260907`, `dsn_publicador.py.bak_pre_datasemana_20260907` (+ `cp` de volta por cima).
- NYC: `v41_ciclo.py.bak_pre_datasemana_20260907`.
- cafezinho-wp: remover linha `DATASEMANA_SWEEPER_20260907` do crontab root + `rm /root/verificador_datasemana.py`.
- Gate inteiro desliga por máquina removendo o módulo `data_semana_gate.py` (todos os plugs são fail-open na ausência dele, exceto o publicador que também é fail-open — nada trava).

## 6. Estado da missão (o que aconteceu / o que falta / o que preciso de você)
- **Aconteceu:** erro confirmado (domingo 7 inexistia — editorial saiu segunda 03:02 BRT); post corrigido e provado no ar; gate mecânico criado (22/22 testes + prova no texto real) e plugado em R1, R2, publicador, juiz 2 e sweeper pós-publicação; revisores agora cobrem `future` e não entram mais em loop; ronda Vigia consome as flags; CL avisada na ponte (ZM-20260907-022).
- **Falta:** observar o 1º ciclo real dos revisores com o código novo (R1 14:05 / R2 14:20 BRT — rondas vigiam); achados C/G/H da auditoria seguem abertos; mensagem do Telegram das 12:35 saiu com o erro (imutável por aqui).
- **Preciso de você (Miguel):** nada bloqueante. Se quiser, decidir: (a) estender o fato-check com busca do R1 também a textos de humanos (custo ↑, hoje só o gate mecânico cobre); (b) mensagem corrigida no Telegram do post (o plugin não edita — seria um post novo de errata ou edição manual no canal).

## 8. Incidente paralelo (§112) — colisão no v41_ciclo.py, curada sem perda
~16:24 BRT uma sessão ZM paralela aplicou no NYC o patch "descer a lista" + denylist (outro "vai" do Miguel, 15:5x); ~16:29 esta sessão sobrescreveu o vivo com a cópia pré-16:23 + o plug do gate — derrubando o patch dela do vivo (o backup `.bak_pre_datasemana_20260907`, 1.106 linhas, preservou o trabalho dela). Ela detectou, avisou na ponte (ZM-20260907-022) e re-aplicou o patch SOBRE o vivo. **Estado final verificado por mim 16:5x: vivo = 1.126 linhas com os DOIS patches, py_compile OK, meu plug intacto (linhas 965-979).** Minha falha: sessão longa (12:5x→16:2x) sem reler o monitor imediatamente antes de escrever em produção. Lição endurecida: em sessão >1h, o monitor se RELÊ na hora do deploy, não só no início. Coordenação respondida em ZM-20260907-023.

## 9. Prova ao vivo dos primeiros ciclos com o código novo (07/09 17:05/17:20 BRT)
- **R1 17:05:** ciclo completo, zero traceback, revisados=5. Escada LLM com quedas nas pernas de busca (GLM 429 — janela semanal 94% mordendo; qwen 403; brave JSON intermitente — achado C, pré-existente) → deepseek-chat respondeu. Transição do anti-loop: posts sem sha de check velho foram revistos 1× (gravam sha); a partir do próximo ciclo, conteúdo inalterado é pulado.
- **R2 17:20:** ciclo completo, zero traceback, e **gpt-5 respondeu em TODOS os 4 posts** (antes o budget 1200 era comido pelo reasoning e a perna caía vazia para o mini — fix D confirmado ao vivo).
- Nenhum flag DATA×DIA nos posts vivos da janela (correto — nenhum tem incoerência); gate silencioso = saudável.
