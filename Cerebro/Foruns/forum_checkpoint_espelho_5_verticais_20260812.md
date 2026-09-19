# Fórum — CHECKPOINT COMPLETO: Teste 5 verticais no espelho (12/08/2026)

**Data:** 2026-08-12 ~16:30 BRT
**Sessão:** ZCode GLM-5.2 (Kimi/Qwen 🔴🔴, fim da cadeia)
**Status:** 🔄 Teste no espelho ATIVO — muito feito, **canônico INTACTO**
**Retomável:** ler este fórum + `forum_teste_espelho_5_verticais_20260812.md` (viabilidade) + SSH NYC/espelho.

---

## CANÔNICO (ocafezinho.com): 100% INTACTO
Nenhuma modificação. Só leitura (baixei tema, li `performance_weights.json`, li top posts via REST GET). As 3 verticais ativas (nacional/geopolitica/ciencia) seguem publicando no canônico.

## ESPPELHO (cafezinho.news @ 159.65.177.60): estado atual

### 1. Pipeline V4 (5 verticais novas) — PRONTO (no NYC, publica no espelho)
- **Worker com `VERTICAIS_ESPELHO`**: as 5 novas (cultura/economia/meio_ambiente/esporte/saude) publicam no ESPPELHO; as 3 ativas seguem no canônico.
- **`FORCE_ESPELHO_WP=1`**: permite forçar espelho pra qualquer vertical (repair-post manual).
- **Bug do status draft CORRIGIDO**: repair-post preserva o status original (`post.get("status")`).
- **Compressão de imagem < 500KB** (`_compactar_para_web`): toda imagem destacada é redimensionada (max 1600px) + JPEG quality iterativo antes do upload.
- **Contratos** v4_cultura/economia/meio_ambiente/esporte/saude_v1.md deployados no NYC + espelho.
- **Fontes RSS** válidas: Agência Brasil + InfoMoney + GE + O Eco + Mongabay + CONASS + Google News + Brave (pt-br, freshness=pw).
- **Mapa** `mapa_v4_contexto_llm.json`: 5 editorias nobres + aliases (v4_cultura etc.).
- **Lock global** de redação (`flock /tmp/v4_redacao_global.lock`); `--repair-post` pula o lock.

### 2. Tema sincronizado (canônico → espelho) — reforma V2.5
- **Tema inteiro portado via tar** (functions.php, style.css 30KB, header, footer, template-parts, img/).
- **Mu-plugin** `cafezinho-real-image-gate.php` portado (tem `cafezinho_get_real_highlight`, usada no front-page linha 5).
- **front-page**: reforma V2.5 do canônico (🔥 balão comentários) + **5 blocos novos** (Cultura/Economia/Meio Ambiente/Saúde/Esporte — ordem com Saúde antes de Esporte) + **"Os 10 mais vistos"** (no lugar da Linha do Tempo, gap `g-3`) + **"Outros Recentes"** (renomeado).
- **CSS customizado** (append style.css): `hr.bar { display:none }` (linha vermelha removida) + `.coluna-editor-nome { color:#8B0000 }` (nome editor vermelho mais escuro).

### 3. Bloco "Os 10 mais vistos" — automatizado
- Script `/root/atualizar_top10_espelho.py` no NYC: lê GA4 (`performance_weights*.json`) + busca URLs no canônico (REST GET read-only) + scp pro espelho.
- **Filtro: só posts dos últimos 30 dias** (`after=30d`).
- **Sem views** (audiência é segredo) + **sem sufixo "O Cafezinho"** nos títulos + **links públicos** (`ocafezinho.com`, não `controle.`).
- **Cron diário 06:00 BRT** (`0 9 * * *`) no NYC.
- JSON: `/var/www/cafezinho-news/wp-content/themes/ocafezinho-portal/top10_canonico.json`.

### 4. Logos (testando — Miguel vai escolher)
- v6 (aprovada, 55KB, 1550×280, md5 `fa5a3e02...`) — no /img/ do tema, **igual ao canônico** (confirmado).
- v7 (site 5, 111KB), v8 (site 6, 14KB), v9 (site 7, 15KB) — todas no /img/, redimensionadas 1550×280 + FASTOCTREE.
- Header atual: **v9** (sed v8→v9). Rollback: `header.php.bak_pre_v7_20260812`.

### 5. Infra do espelho
- **Basic Auth DESATIVADA** temporariamente (religar ao fim). Backup nginx: `cafezinho-news.bak_pre_v4_espelho_20260812`.
- **App Password WP** espelho: user `Redator` (ID 5470), no cofre (`ESPELHO_WP_SITE/USER/PASS` no `chaves.sh` NYC + `.env.unificado` local).
- **SSH NYC→espelho** configurado (chave ed25519 do NYC no `authorized_keys` do espelho).

### 6. Posts corrigidos (espelho)
- Post 265302 (Irã/Hellfire): imagem destacada 400013 (IA flux-pro), status publish.
- Post 265282 (inflação/Lula): imagem destacada 400016 (setado manualmente _thumbnail_id; era órfã 215386).
- Post 263883 (Irã/família): título corrigido → "EUA bombardeiam família no Irã e matam criança".

## Backups no espelho (rollback por componente)
- Tema anterior (tar): `/tmp/ocafezinho-portal-espelho-BK-20260812.tar.gz`.
- front-page: `.bak_pre_blocos_v4`, `.bak_pre_reordenar`, `.bak_pre_mais_vistos`, `.bak_pre_sem_views`, `.bak_pre_sync_canonico_20260812`.
- style.css: `.bak_pre_editor_fix_20260812`.
- header.php: `.bak_pre_v7_20260812`.
- nginx: `.bak_pre_v4_espelho_20260812`.

## Pendências (próximos passos)
1. **Logo**: Miguel escolhe qual fixar (v6/v8/v9).
2. **Cron das 5 verticais**: NÃO ligado (plano faseado 1/dia, começando Economia — ver `forum_plano_lancamento_faseado_5_verticais_20260811.md`).
3. **Basic Auth**: religar quando teste acabar (1 linha + reload).
4. **Fontes invisíveis**: contrato v4_* JÁ tem a regra "links silenciosos, sem citar veículo" (write_briefing). Verificar se algum post cita "Agência Brasil" e reforçar se preciso. Miguel quer: link em palavra-chave, sem citar fonte nenhuma.
5. **GITHUB_TOKEN do NYC**: morto (`Bad credentials`). Não usado (SSH). Vale rotacionar no cofre.
6. **3ª auditoria Codex**: condições atendidas (quarentena, lock global, fontes, cron+teste). Pode ser curta.
7. **Creds espelho**: App Password do Redator criada (Redator/zLSzJ8gcfPt4fwsFP4fpOBXP). Basic Auth do espelho: cafezinho/000 (desativada).

## ADENDO FINAL 12/08 ~17:00 — CRON LIGADO + LOGO V10 FIXADA + CARTINHA CLAUDE CODE

- ✅ **Cron das 5 verticais LIGADO** no NYC (5 linhas no crontab: economia/cultura 4h, meio_ambiente/esporte/saude 8h). Produzindo DRAFT no espelho.
- ✅ **Logo v10** (nova logo cafezinho 8, 1550×280, 11KB) **FIXADA NO CANÔNICO + ESPELHO** (header trocado v6→v10 no canônico, v9→v10 no espelho). Backups: `header.php.bak_pre_v10_20260812` (canônico), `header.php.bak_pre_v7_20260812` (espelho).
- ✅ **Cartinha Claude Code** escrita: `Foruns/cartinhas/cartinha_claude_code_fase0_v4_espelho_20260812.md` (Fase 0, creds no cofre, revisão de drafts).
- ✅ **Plano de migração canônico** criado: `Foruns/forum_plano_migracao_canonico_20260812.md` (5 etapas, ~40 min, rollback).

---

## Continuidade
Retomar: ler este fórum + `forum_teste_espelho_5_verticais_20260812.md` + SSH NYC/espelho pra confirmar estado. Canônico intacto.
