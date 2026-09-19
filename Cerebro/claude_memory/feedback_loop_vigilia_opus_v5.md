---
name: feedback-loop-vigilia-opus-v5
description: Protocolo do Loop Vigília Opus V5 (DIA :17/:47 07-22h + NOITE :17 23-06h). Único loop de correção editorial V4 é Opus 4.7 sozinho — sem Haiku/Sonnet paralelo. Ativado 30/07/2026 12:35 BRT.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 07b6c459-6a0f-4880-a779-68996b652812
---

🔁 **Loop Vigília Opus V5** — protocolo operacional definitivo para publicação de drafts V4 do Cafezinho. Miguel enviou o texto oficial em 30/07/2026 ~12:30 BRT como diretriz permanente.

**Cadência:**
- **DIA** 07h-22h BRT, cada 30min aos `:17` e `:47` (cron: `17,47 7-22 * * *`)
- **NOITE** 23h-06h BRT, cada 1h aos `:17` (cron: `17 23,0-6 * * *`)

**Passo-a-passo por ciclo:**

1. **Puxar drafts elegíveis:** autor `5786` com idade `< 2h`. Comando canônico:
   ```
   cd /home/migueldorosario/ferramentas/sentinela && python3 -c "import sys; sys.path.insert(0,'.'); from sentinela_ciclo import load_env, wp_get; from datetime import datetime, timezone; env=load_env(); posts=wp_get(env,'/wp-json/wp/v2/posts?status=draft&per_page=25&orderby=modified&order=desc'); now=datetime.now(timezone.utc); [print(f\"{p['id']} aut={p['author']} idade={int((now-datetime.fromisoformat(p['date_gmt'].replace('Z','+00:00')).replace(tzinfo=timezone.utc)).total_seconds()/60)}m — {p.get('title',{}).get('rendered','')[:70]}\") for p in posts if p['author']==5786 and (now-datetime.fromisoformat(p['date_gmt'].replace('Z','+00:00')).replace(tzinfo=timezone.utc)).total_seconds()<7200]"
   ```

2. **Puxar corpo via `wp_get(env, f'/wp-json/wp/v2/posts/{PID}?context=edit')`** — capturar `meta.zizi_job_id` (identifica vertical). Checagem dupla:
   - **Título:** coerente, sem sensacionalismo, nomes próprios corretos, siglas em maiúscula
   - **Datas:** dia_semana bate com dia do mês? Ano do artigo referenciado correto?
   - **Autoridades — cutoff crítico via WebSearch obrigatório:**
     - Presidente STF: **Edson Fachin** (não Barroso)
     - Secretário Tesouro EUA: **Scott Bessent** (não Yellen)
     - Presidente EUA: **Donald Trump** (não Biden)
     - Presidente Coreia do Sul: **Lee Jae-myung** (não Yoon Suk-yeol)
     - Líder supremo Irã: **Mojtaba Khamenei** (Ali morto março 2026)
     - Presidente Argentina: **Javier Milei**
     - Presidente China: **Xi Jinping**
   - **Números/valores específicos:** WebSearch pra bater
   - **Grafia:** capitalização pós-vírgula, HTML/markdown misturado, FONTE em grito

3. **Se OK:** `wp_post(env, f'/wp-json/wp/v2/posts/{PID}', {'content': corpo_corrigido, 'status': 'publish'})`. Backup SHA-256 pré-edit obrigatório.

4. **Registrar bugs** em `Cerebro/monitoramento_horario/bugs_encontrados/bugs_$(date +%Y-%m-%d).jsonl`. Log também em `Cerebro/monitoramento_horario/publicacoes_claude/publish_YYYY-MM-DD.jsonl`.

5. **Reportar em bloco compacto (máx 12 linhas) — SEMPRE indicar VERTICAL de cada post** (extensão `feedback_reportar_vertical_v4_no_bloco_report` 28/07):
   - Formato: `**263XXX** (Geo/Ciência-Tec/Nacional) — *título...*`
   - Vertical via `zizi_job_id`: `v4d_geopolitica` / `v4d_ciencia` / `v4d_nacional`
   - Fallback categorias WP: `5003`=Geo, `22`=Nacional, `19936/735/5008`=Ciência
   - Total do dia com breakdown por vertical

6. **Se ZERO drafts elegíveis:** 1 linha `🟢 [HH:MM BRT] ciclo vigília V4 DIA — zero drafts` (ou `🌙` na NOITE).

**Regras fundamentais operacionais:**
- Autonomia total (extensão de `feedback_checagem_dupla_editorial_com_autonomia` 27/07)
- Manter autor 5786 se draft já é 5786 (regra `feedback_kimi_stop_retroativo`)
- WebSearch antes de afirmar fato (regra `feedback_sempre_pesquisar_web_em_duvida`)
- Backup SHA-256 obrigatório em toda edição
- Duplicata em post publicado → `status=pending` (regra `feedback_duplicata_pos_publish_vira_pending`)
- Nacional com cat 20699 no-home é NORMAL (regra `feedback_nacional_tem_no_home_por_score`)
- **Autor 2018 (james2017) = Miguel via Antigravity Desktop** — Claude NÃO toca. Todo `5786` = agente V4 puro.
- **Reportar VERTICAL sempre** (regra `feedback_reportar_vertical_v4_no_bloco_report`)

**Contexto operacional (30/07/2026):**
- **Único loop de correção editorial V4 é o meu (Opus 4.7).** Sem Haiku/Sonnet paralelo.
- Sentinela DeepSeek publish DESATIVADO desde 27/07 17:15
- ~17 posts publicados por mim em 28/07 até 10:21 BRT (10 Geo, 5 Nacional, 2 Ciência)
- Ciclo executado manualmente pela minha sessão Claude quando ativa; se sessão fechada, retomada relança o loop

**Ligações:** [[feedback-checagem-dupla-editorial-com-autonomia]] · [[feedback-reportar-vertical-v4-no-bloco-report]] · [[feedback-sempre-pesquisar-web-em-duvida]] · [[feedback-nacional-tem-no-home-por-score]] · [[feedback-duplicata-pos-publish-vira-pending]]
