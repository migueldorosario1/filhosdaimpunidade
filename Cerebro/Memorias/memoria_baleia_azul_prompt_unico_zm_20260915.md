# Memória técnica — Baleia Azul: comando ZM + prompt único + fallback Laura (15/09/2026)

Log técnico completo da obra. Decisões resumidas no fórum gêmeo `Foruns/forum_baleia_azul_prompt_unico_zm_20260915.md`.

## Estado antes (provas)

- Última edição: `boletim_baleia_azul_20260911_manha.md` (ed. 46, commit b6bfdf7e3, "DS-N Chefe: Baleia Azul ed. 46 manha 11/09").
- Crons do Dell desligados em 01/09: `crontab -l` mostra `# BALEIA_DESLIGADA_20260901_ZM` nas linhas 08:00 e 19:30 (`enviar_baleia_azul_ponte.sh`).
- DS-N Chefe morreu no apagão de quota DeepSeek (commits 10/09 citam "5 rondas perdidas por QUOTA"); após 11/09 07:03, nada.
- Painel V6 baleia multi-fonte (patch 06/09): lê `v6_data/foruns/ponte_laura_completa/baleia_azul` → clone `/home/ubuntu/cerebro-miguel/cerebro/Foruns/...` → BASE_DIR legado; dedupe por (data, turno).

## Artefatos criados

1. `Foruns/ponte_laura_completa/baleia_azul/PROMPT_UNICO_BALEIA_AZUL.md` (canônico + repo) — TODO o rito: grade (manhã ≤07:10, tarde ≤19:15; atraso ok, zero nunca), entrega (arquivo no repo + push + Telegram completo limpo + V6 automático), formato 350-450 palavras com estrutura fixa, fontes de dados com comandos prontos, 10 regras editoriais consolidadas, rede de segurança, numeração via grep "Edição".
2. `~/bin/baleia_dados_ga4.py` — wrapper do coletor canônico com timeout ssh de 300s (o coletor original tem 60s internos e o GA4 frio estoura — causou RC=1 na 1ª tentativa hoje) + cache de fail-soft em /tmp/baleia_dados_ga4.json + saída resumida pronta para o editor.
3. `~/bin/baleia_fallback_laura.sh` (chmod +x, crontab Dell `30 7`/`30 19`) — git pull → se faltar a edição do turno: bloc URGENTE `BALEIA-FALLBACK-<AAAAMMDD>-<turno>` no de_dell.md (sed de marcadores de conflito antes do commit), commit seletivo + push com 1 retry rebase, Telegram ao Miguel via ponte_cafezinho, dedupe por marcador. PROVA caminho OK: `[15/09/2026 15:20:43] OK: edicao manha de 20260915 existe — fallback nao acionado`.
4. `/home/ubuntu/bin/baleia_watchdog_telegram.sh` (Tencent, crontab `45 7`/`45 19`, BRT — servidor está em -03) — git pull do clone (remote `nyc`) → edição ausente → Telegram direto pelo bot DSN Chefe (TELEGRAM_TOKEN_DSN_CHEFE_BOT + DSN_CHEFE_BOT_CHAT_ID do /home/ubuntu/.env.unificado, sem expor valores), flag anti-repetição /tmp.
5. Automação ZM `automation-15458117-897c-4d97-b38b-5438dd445f51` — cron `5 7,19 * * *` com PASSO 0 de autodetecção de turno (`date +%H` < 12 → manha). NOTA ESTRUTURAL: o ZCode só permite CRIAR 1 automação por sessão ("session already belongs to a scheduled task") e subagente NÃO tem CronCreate — a solução foi criar 1 automação e expandi-la para 2 slots via CronUpdate.
6. Edição 47: `boletim_baleia_azul_20260915_manha.md` — 449 palavras (régua 350-450; 1º rascunho 473 → aparado), dados: GA4 ontem 8.421 views/5.163 usuários vs 13/09 8.420/6.052; 7d 69.325 vs 80.473 (−13,8%); 14d 149.798 vs 138.522 (+8,1%); top ontem pesquisa STF×urnas 369 (271+98 AMP), Vorcaro doc 301 (sábado, perna longa), tarifaço 91 (04/09); 14d geopolítica 58,3% peso/média 877, campeão Horta/Teixeira 4.667; instantâneos FAROL 713 humanos/30min e LUMINA 1.430 distintos (15h). Commits 9ab7b262d + ajuste; push ok.

## Operação e provas

- Telegram da ed. 47 enviado via ponte (saída vazia = sucesso; tg_send só imprime linha `tg_send_erro` em falha — conferido no código).
- V6: `curl 127.0.0.1:8084/baleia` no Tencent retorna "Edição 47 · manhã (edição da retomada...)". Chegou por scp cirúrgico para v6_data (fonte 1 do painel) porque o clone estava divergente.
- Sync repo→GitHub→mirror NYC rodou após commit cirúrgico da telemetria viva `monitoramento_horario/porta_voz_zm/2026-09-15.jsonl` (worktree sujo recusa o sync — padrão conhecido).
- Clone Tencent: 175 atrás + 111 commits locais VIVOS do workflow DS YouTube (último às 15:10 de hoje) → `git merge --no-edit nyc/main` = 61135ee7a, limpo; `git diff HEAD^1 HEAD` introduziu 0 marcadores. Reset --hard PROIBIDO nesse clone enquanto o workflow viver.
- Falso alarme documentado: marcadores em `queue_youtube.md` são HISTÓRICOS (pré-merge), dono = workflow DS YouTube.

## Riscos e observações

- Automação só dispara com o app ZCode aberto no Dell → coberto pelos 2 backups determinísticos (fallback crontab 07:30/19:30 e watchdog Tencent 07:45/19:45).
- GA4 frio pode passar de 60s → usar sempre `baleia_dados_ga4.py` (300s), nunca o coletor direto em automação.
- A v6_data/foruns do Tencent não tem copiador vivo (o scp de hoje foi manual) — a cadeia sustentável é repo→mirror→clone (merge); v6_data fica como fonte 1 estática do histórico.
- Numeração: grep "Edição" na pasta; ed. 48 hoje à noite, 49 amanhã 07:05.

## Rollback

- Desligar tudo: desabilitar automation-15458117 (CronUpdate enabled=false ou delete), remover as 2 linhas `BALEIA_FALLBACK_LAURA_20260915` do crontab Dell e as 2 `BALEIA_WATCHDOG_TG_20260915` do Tencent. O prompt único é inerte (documento).

— ZM · ZCode/GLM-5.3 · 15/09/2026 15:2x BRT
