# MEMÓRIA — GATE DATA×DIA-DA-SEMANA + correção 269341 (07/09/2026)

> Log técnico completo do incidente e da reforma. Decisões resumidas: `Foruns/forum_gate_data_dia_semana_269341_20260907.md`. Auditoria R1/R2 da manhã: `Foruns/forum_qualidade_curadoria_juiz_v41_20260907.md` §11.

## Linha do tempo (BRT)
- 09:47 — post 269341 criado via wp-admin (meta `_cafezinho_origem`: via admin, user 5735 = gabrielbarbosa; UA Chrome/Windows). Autor atribuído: 5780 redator2 "Redação".
- 10:05 — ciclo R1 morre ("varredura falhou: HTTP Error 500" — achado E da auditoria).
- 11:05 — ciclo R1 morre de novo (TimeoutError não capturado do wp_req no gravar_check).
- 11:22:04 — R2 revisa 269341: ok=false (gpt-5-mini) — pendências: primeiro nome isolado «Flávio» no título; olho truncado. NÃO viu «domingo (7)» (prompt não dizia o dia da semana).
- 11:23:10 — PUBLICADO (post_date). 1 minuto após o check reprovando. Sem bloqueio.
- 12:35:27 — disparo Telegram (`_wptg_p2tg_sent2tg`) com o erro.
- ~12:52 — Miguel detecta: "domingo 7? domingo foi dia 6" + "vai".
- 13:09 (16:09 UTC) — correção aplicada via wp-cli (override §130/423, ordem expressa). Página pública provada (5× texto novo, 0× velho).
- 13:2x-13:4x — reforma estrutural deployada (Tencent R1/R2/publicador, NYC juiz 2, cafezinho-wp sweeper) + ronda Vigia ganha passo P2.5.

## Verdade factual
Editorial Estadão «Cronicamente mendaz» = **segunda 07/09/2026** (Google News RSS do Estadão: pubDate Mon 07 Sep 2026 06:02:00 GMT; Brasil 247 cobriu 06:01 BRT como novidade da manhã). Domingo 06/09 o editorial não existia. Correção: `neste domingo (7)` → `nesta segunda-feira (7)`.

## Causa-raiz (4 elos)
1. Confecção humana errou o dia da semana.
2. R1 não cobre autor 5780 (filtro AUTOMATICOS = {5470, 5786, 5787, 5801}) — texto humano nunca seria fact-checkado. (+ crashes do dia.)
3. R2 sem noção de calendário (prompt sem dia da semana) e sem gate mecânico.
4. Publicação humana sem bloqueio + inexistia varredura pós-publicação.

## O que foi instalado (todos com backup `.bak_pre_datasemana_20260907`)

### Módulo `data_semana_gate.py` (determinístico, stdlib only)
API: `encontrar_incoerencias(texto, ref_date=None, tzoffset=-3) -> [{"tipo","trecho","detalhe"}]`.
Padrões: `dia_da_semana (N)` · `dia_da_semana, N de mês [de ano]` · `N de mês [de ano] (dia_da_semana)` · `hoje/ontem/anteontem/amanhã (N)`.
Regra: dia-do-mês N é resolvido para a data **mais próxima da referência** dentre os meses {ref−1, ref, ref+1}; só flaga se a data resolvida NÃO cair no dia da semana nomeado. Sem número explícito = nunca flaga (anti-falso-positivo). Selftest: `python3 data_semana_gate.py` = 22/22.
Cópias idênticas: Tencent `/home/ubuntu/dsn_shared/` · NYC `/root/v4_labs/codigo/` · cafezinho-wp `/root/`.

### R1 (`/home/ubuntu/dsn_revisor1/dsn_revisor1.py`, cron :05/h)
- Gate data×dia para TODOS os autores (flag → check r1 ok=false, modelo `data_semana_gate`, sem gastar LLM); fact-check LLM segue só p/ AUTOMATICOS.
- Varredura `status=draft,future`; janela `−7d ≤ agora−date ≤ 48h` (agendados cobertos).
- Anti-loop por **sha1(título+corpo)** no meta (`r1.sha`) — substitui o gate `modified_gmt<=ts_iso` que nunca fechava (o POST do meta bumpava modified).
- try/except no gravar_check; NameError `tag`→"R1"; prompt com "Hoje é <dia-da-semana>, dd/mm/aaaa" + regra de calendário; escada falhando + gate reprovando = check mecânico gravado mesmo assim.

### R2 (`/home/ubuntu/dsn_revisor2/dsn_revisor2.py`, cron :20/h)
- Mesmo gate (título+olho+corpo), mesclado ao veredito LLM (pendências `DATA×DIA:` prefixam e forçam ok=false); mesmos fixes (future, sha, try/except, tag, prompt).
- `max_completion_tokens` gpt-5/gpt-5-mini: 1200 → **4000** (achado D — reasoning comia o budget e a perna devolvia vazio).

### Publicador (`/home/ubuntu/dsn_publicador/dsn_publicador.py`, cron */15)
- Passo 2.5 entre o check de imagem e o publish: gate data×dia sobre título+olho+corpo (ref = `post.date`). Flag = **não publica**, linha 🚫 na ponte `de_nuvem_publicador.md`, post segue elegível. Import falhar = fail-open logado (casa não para).

### Juiz 2 V4.1 (NYC `/root/v4_labs/codigo/v41_ciclo.py`)
- Gate sobre título+texto real do draft (depois do fetch do WP, antes do LLM). Flag = juiz 2 reprova com `motivo: data_semana_incoerente` → fluxo existente: salva-drafts arquiva → lixeira → pauta volta em 6h (dedupe L13). Artefato ganha `juiz2_data_semana` / `data_semana_gate_erro`.

### Sweeper pós-publicação (cafezinho-wp)
- `/root/verificador_datasemana.py` + `/root/data_semana_gate.py`, cron root `*/15` (flock `/tmp/datasemana.lock`, marcador `DATASEMANA_SWEEPER_20260907`).
- Varre `publish` das últimas 3h (máx 30); flags → `/root/agent_data/datasemana_flags.jsonl` + log `verificador_datasemana.log`; vistos em `datasemana_vistos.json` (retém 500). NUNCA edita post.
- **Ronda ZM Vigia 1/1h (automation-2a8954e2) ganhou o passo P2.5**: lê o JSONL e dispara 🔴 Telegram com id+título+flag. Prova 1ª execução: 269363/269358 ok.

## Provas
- Gate: 22/22 selftest (Dell, Tencent, NYC); texto original 269341 = 1 flag exata («'domingo (7)' incoerente: dia 7 mais próximo de 07/09/2026 é 07/09/2026, uma segunda-feira»); texto corrigido = 0 flags.
- py_compile OK nos 4 arquivos patchados (Tencent python3 + NYC 3.12) e no sweeper.
- Varredura R1 nova (só-leitura, import isolado): 15 posts draft+future (antes: só drafts).
- Página pública do 269341: texto novo presente (5×), velho ausente (0×).

## Armadilhas / notas para o próximo
- O override §130/423: post "de humano" (meta `_cafezinho_origem` via admin) precisa `CAFEZINHO_EDITORIAL_HUMAN_OVERRIDE=1` no wp-cli — use `sudo -u www-data env VAR=1 wp ... eval-file`.
- `date`/`date_gmt` de post FUTURE fica no futuro — qualquer janela de idade precisa aceitar delta negativo (foi o que derrubava a cobertura de agendados).
- O sha anti-loop torna seguro um gate reprovar para sempre o mesmo texto: conteúdo inalterado = pulado; correção humana muda o sha = re-revisa.
- Mensagem do Telegram (12:35) saiu com o erro e o plugin `_wptg` não edita — pendência comunicada ao Miguel (errata manual se ele quiser).
- Achados C/G/H da auditoria seguem ABERTOS (busca falseável, meta evapora pós-publish, parse CORREÇÕES vazio) — desenhados no §11 do fórum de qualidade.

## Estado
Fechado: correção 269341 + reforma (4 plugs + sweeper + ronda). Vigilância: 1º ciclo real R1 14:05 / R2 14:20 BRT (rondas VIGIA/VIGIA-BG olham). Aguarda Miguel: fact-check LLM também p/ humanos? errata no Telegram?
