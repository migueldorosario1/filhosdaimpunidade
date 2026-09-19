# MEMÓRIA TÉCNICA — Caso 269279 (título 125 chars/sigla agendado) + EMU-9

**Data:** 06/09 23:5x → 07/09 00:0x BRT · **Agente:** ZCode (Qwen3.8-Max, Dell) · **Fórum-irmão:** `Foruns/forum_titulo_269279_emu9_20260907.md`

## Forense (provas)

- `wp post get 269279`: author 5470; status **future** (post_date 07/09 06:30); post_modified 06/09 22:20:52; título velho 125 chars; slug velho idem.
- Metas: `zizi_job_id=v41_ciencia_f7c3022b4671`, `_v4_versao=4.1`, `_cafezinho_origem` ts 06/09 21:46:34 (python-requests), `_cafezinho_txt_check.r1` (glm-5.3+web 22:05, fail-close INCERTO, escada de busca fora), `_cafezinho_txt_check.cl_manual` (CL-20260906-031, 22:19, ok=true, "titulo com nome do produto e o efeito da licenca (sem sigla)", evergreen → vaga 07/09 06:30), `_cafezinho_txt_isenta` (CL, expira 08/09), `_cafezinho_img_check` APROVADA (CL visão própria, 22:19).
- Ciclo NYC `/root/v4_labs/dados/v41_ciclo/20260906_2145.json`: vertical ciencia; pauta «FlexGanttFX 正式开源» (feed zh, TEC-MULTIIDIOMA); `redator_out={"ok": true, "id": 269279, "status": "draft", "title": "Biblioteca de gráficos Gantt abre código após 15 anos", "content_chars": 6161, "model": "gpt-5.6-sol"}`; fc_websearch ok=True (InfoQ/OSFY/NLJUG/GitHub).
- Access log nginx (por domínio): POST REST 21:46:58 (Redator, python-requests) · GET capa_frame 22:00:11 · POST 22:05:18 UA **DSN-Revisores-O-Cafezinho/1.0** (metas r1) · **NENHUM POST REST às 22:20** ⇒ a reescrita do título + schedule foi via **wp-cli ssh** (user claude_miguel, sem rastro nginx) — casa com post_modified 22:20:52 e ts da CL 22:19/22:22.
- Auditor NYC: `grep 269279 advisor_pending_5470.jsonl` = vazio; cron 07:37 > slot 06:30 e não avalia future ⇒ post agendado publica sem auditoria de título (gap estrutural).

## Correção aplicada (07/09 00:0x, wp-cli www-data via script python no server)

- Backup: `Cerebro/Backups/posts_editados/269279_pre_fix_20260907.md` (título+slug+conteúdo integrais).
- `wp post update 269279 --post_title="Após 15 anos de venda, criador de biblioteca de cronogramas abre o código" --post_name="apos-15-anos-de-venda-criador-de-biblioteca-de-cronogramas-abre-o-codigo"` + P0 substituído pelo lead-gancho copyleft×nuvem (regex no 1º `<p>`; fatos só do corpo: cláusula de rede AGPL P1/P2, 15 anos comercial, Dirk Lemmermann/FlexGanttFX decodificados na 1ª menção).
- Provas pós: título 73 chars · slug novo · status future · post_date 07/09 06:30 (schedule mantido).
- Receita: edição de conteúdo grande via ssh sem inferno de aspas = script python no server chamando `subprocess.run(["wp", ...], cwd="/var/www/ocafezinho")` como www-data.

## EMU-9 — onde foi gravada

- `Estilo/MANUAL_DE_ESTILO_UNIFICADO.md`: regra 10 no checklist B1 (checagem mecânica ≤80 + sigla/nome próprio NO ATO do schedule) + entrada EMU-9 no registro (backups .bak_pre_emu9_20260907).
- `Estilo/MANUAL_DE_ESCRITA_PORTAL.md` seção 8: dois bullets novos (tecnologia com gancho/convergência + checagem mecânica antes de agendar) — este arquivo é injetado no briefing do redator V4.1 (v41_ciclo.py:587).
- Espelho NYC `/root/v4_labs/dados/MANUAL_DE_ESCRITA_PORTAL.md` md5 **111b6d67acbc1d9cc1ff1061d18e8eed** (idêntico local×NYC; backup .bak_pre_emu9_20260907 lá também).
- `CEREBRO_NODE_ESTILO.md` linha de índice + `CEREBRO_NODE_ATUALIZACOES.md` + monitor + ponte `Foruns/ponte_laura_completa/de_dell.md` bloco 12 (aviso à CL: regra 10 antes de schedule; auditor 07:37 não cobre manhã).

## Responsáveis (resposta ao Miguel)

- Pauta "técnica e chata": curadoria automática V4.1 ciência via feed chinês — ninguém humano escolheu; a diretriz EMU-9 agora orienta curadoria+redator.
- Título monstruoso: revisão manual da CL (CL-20260906-031) sobrescrevendo o título limpo do redator, sem contagem de chars.
- Ninguém pegou antes: auditor de títulos roda 07:37 (depois do slot 06:30) e ignora future.

## Pendências (aguardam "vai")

1. Gate mecânico no código (v41_ciclo/worker de schedule): bloquear future/publish com título >80 chars ou sigla/nome próprio + alarme Telegram.
2. Auditor NYC cobrir status future (ou cron extra antes dos slots da manhã).
