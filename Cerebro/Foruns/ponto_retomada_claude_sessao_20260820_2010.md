# Ponto de Retomada — Claude Miguel / sessão 20/08/2026 20:10 BRT

**Substitui:** `ponto_retomada_claude_sessao_20260818_0245.md`
**Autor:** Claude Miguel (`claude-opus-4-7`)
**Contexto:** Miguel parou urgente. Sessão longa (18h+ contínuas — retomei 20/08 00:47 do ponto anterior; agora 20:10). Muita coisa mudou. Este documento é pra próxima retomada — minha ou Miguel abrir sessão nova.

## 1. Trindade — 7 agentes ativos (mudou muito desde 18/08)

| Loop | Agente | Cadência | Escopo |
|---|---|---|---|
| Miguel (Dell) | **Claude Miguel** (eu) | 20min A/B + Baleia Azul 05h/17h | Publish exclusivo + Vigília V6 + Baleia Azul (assumida hoje) |
| Miguel | **Grok Miguel** | 1h | Observador Fase 2 (Emenda 4) + par técnico aprovação deploy V5 |
| Miguel | **AGY (Antigravity Dell)** | 2h | Auditoria técnica WP REST + integridade §5 + missão V5-Originalidade |
| Laura (Windows) | **Claude Laura** | 30min :12/:42 | SHADOW_EDITORIAL_WRITE `laura_ed25519` + §127 alertas |
| Laura | **Grok Laura** | 1h | §128 capas pós-publish + Slot B |
| Laura | **LAURA-AGY** (novo, 20/08) | 1h? | Motor V5 E-E-A-T (produz PILOTOs geopol) |
| Manus | **Manus 2** | 1h | Vigília editorial append-only (conta migueldorosario2) |

**OFF:** ZCode Miguel, Codex Miguel, ZCode Laura, Codex Laura.

## 2. Regras NOVAS vigentes desta sessão (todas gravadas em MEMORY.md + arquivos referência)

### 2.1 Filtro 72h flat anti-repetição (Miguel 20/08 02:52)
- SQL dedup: `WHERE post_date >= NOW() - 72h AND post_title LIKE %termo%` — 1 hit = canibal, descarta
- Cutoff velharia: fato >72h = velho, descarta
- Aplico em toda Vigília via query padrão

### 2.2 Categoria `no-home` (id 20699) pra velharia/canibal pós-publish (Miguel 02:35-02:37)
- Post publicado **NUNCA reverte pra pending** (perde SEO)
- Se descobrir velharia/canibal depois de publish: `wp post term add <ID> category no-home --allow-root`
- Fica publicado (URL vive, SEO preservado) mas sai de bloco/manchete

### 2.3 Convenção meta canibal (CM-006 + estendida)
- `_cafezinho_descartado_canibal=<ref>` — pré-publish
- `_cafezinho_canibalizado_pos_publish=<ref>` — pós-publish + aplica no-home
- `_cafezinho_descartado_velharia=<motivo>` — fato >72h
- `_cafezinho_hold_capa_incoerente` — post OK mas fm errada, aguarda recacar
- Já tem 40+ posts marcados via essas metas

### 2.4 Google anti-spam iniciou 20/08 (contexto de urgência)
- Todas as regras acima ganharam peso econômico (não é estética, é tráfego)

### 2.5 Cron V4 nacional NYC reduzido 75% (Miguel 02:59)
- Antes `20,50 * * * *`, agora `20 */2 * * *` (12 rodadas/dia vs 24)
- Backup: `nyc:/tmp/crontab.bak_pre_reduzir_nacional_20260820_0300`
- Check 24h: `20260821 03:00` medir publish/hora nacional pós-corte

### 2.6 Comunicação Miguel↔agentes HÍBRIDA (Miguel 01:10)
- Urgência → chat direto do agente
- Coordenação transversal → ponte Laura Completa (`de_dell.md`)
- Se ordem afeta outros agentes, propagar via CM- na ponte

### 2.7 Régua PDF-CT (Miguel 17:15 via CM-019, minha proposta ao AGY)
- Se pedido menciona `signed`/`assinado` no nome + escaneado + alteração de conteúdo negocial + achatamento pra indistinguibilidade → **tratar como jurídico, não técnico**
- Nunca reescrever PDF assinado. Propor aditivo/errata/rescisão.

### 2.8 Reforma V5 (Miguel 13:10)
- Tudo relativo à reforma nova = **V5**
- V4 legacy (worker NYC, cats WP, autor 5786) mantém V4
- Manual canônico: `Cerebro/memoria_estilo_editorial_v5.md` (LAURA-AGY v5.0.0)
- 7 regras título + 4 camadas E-E-A-T + ≥3 fontes + intertítulos `<h3>`

### 2.9 FC-1/2/3/4/5 pra LAURA-AGY (fact-check severo redundante)
- FC-1: verificar cargo+nome figuras públicas contra 2 fontes na apuração
- FC-2: reset contexto temporal antes redação (Trump=presidente atual 2026, Lula=3º mandato, etc.)
- FC-3: auto-lint pós-redação (grep `ex-presidente`, datas, números)
- FC-4: auto-audit contra próprio manual V5
- FC-5 (nova, CM-018): auto-check `_thumbnail_id != 0` antes de gravar recibo

### 2.10 Instabilidade servidor Cafezinho madrugada
- Janela backup provedor 03-05h BRT gera DB timeout + /tmp perdido
- NÃO escalar como bug — retry 10-20s

## 3. Estado editorial de 20/08 (posts publicados hoje pelo CM)

**Manhã madrugada:**
- 266679 Vorcaro Master STF · 266687 mulheres candidaturas · 266688 TRE-AM · 266393 Juann Lima cultura
- 266691 UNIFIL Líbano · 266689 Flávio Nikolas · 266633 filme chinês Iraque
- 266189 Lula/Flávio iniciam campanha · 266699 Tebet Marina Derrite SP
- 266510 Longa Marcha 7A · 266404 China software militar
- 266704 CNPC cultura · 266710 China porcos EUA
- 266713 drones Curdistão

**Diurno:**
- 266722 China/Índia Arunachal · 266747 BR-101 ES · 266727 Grupo libanês ataque
- 266733 Turquia rejeita Israel Síria · 266735 Dia D vacinação
- 266739 Brasil Plural coletânea · 266721 IPCA · 266752 Resistência iraquiana
- **266751 PACTO DE MECA** (PILOTO-GEO 1 V5, LAURA-AGY, publish após 2 correções minhas — CM-014→015→017)
- 266776 deportados EUA Venezuela
- **266791 CRISE ORMUZ 92 DÓLARES** (PILOTO-GEO 2 V5, LAURA-AGY publish com meu ajuste de título + capa NASA — CM-018/020)
- 266785 Libertadores · 266796 Rússia/Reino Unido drones · 266798 Cine Cultura Goiânia

**Total dia:** ~25 publish + 40+ descartes canibais + Baleia Azul manhã enviada 08:00.

**Descartes canibais notáveis hoje:**
- 266628 China foguete Zhuque-3 (5ª vez ressuscitado)
- 266579 BRICS/CBAM canibal PERFEITO 266558
- 266703 "matar 40 palestinos" canibal PERFEITO 266447
- 266189 (arranque campanha) tentado publicar 02:10, reverti erradamente, restaurei publish + aplicou `no-home` depois — Miguel me ensinou "publish é definitivo"

## 4. Pendências abertas

### 4.1 Missão AGY V5-Originalidade (CM-011/013)
- AGY Dell deveria propor mudança estrutural V4 upstream anti-canibal
- Fase 1 estudo → Fase 2 código → Fase 3 autorização dupla CM+GM → Fase 4 deploy → Fase 5 vigilância pós-deploy
- **Status:** AGY entregou 1º relatório 04:00 (P2 SEO zerado após minha ação batch), patch YT fail-soft submetido, aguardo RESPOSTA_GM. Não vi Fase 2 estrutural ainda.

### 4.2 CM-017/018/020 pedido diretrizes FC pra LAURA-AGY
- Instalar FC-1/2/3/4/5 no fluxo dela
- PILOTO 1 → PILOTO 2 mostrou aprendizado FC-1 (Trump=presidente ✓) + FC-5 (capa NASA real ✓)
- Título ainda escapou no 2 — próximo PILOTO 3 idealmente com título já correto

### 4.3 YT-PATRULHA 🔴 (aberto desde 19/08 21:25)
- 2 slots nacionais vazios ontem 14h+20h (Grok Laura escalou)
- Meu prazo original 09:12 hoje passou sem eu resolver
- Cron youtube_cafezinho.py Dell rodou mas AGY diagnosticou 36 falhas proxy iProyal
- Patch fail-soft AGY submetido, aguarda RESPOSTA_GM

### 4.4 Post 266437 (Trump nomeia crítico STF Juan Pablo Segura)
- HOLD desde 03:07 — fm=Marco Rubio errada (post sobre Segura)
- `_cafezinho_hold_capa_incoerente` gravado
- Precisa recacar capa (Grok Miguel/Laura) antes de publish

## 5. Fluxo Vigília minha (não muda)

- Slot A min<25 (cats 22/5003/30/regional) — cutoff 72h
- Slot B min≥25 (cats 79/43/582/1271/258) — cutoff 72h
- Filtros SQL: `NOT EXISTS _cafezinho_descartado_canibal` + `NOT EXISTS _cafezinho_hold_capa_incoerente`
- Teto: 3 publish + 2 correções
- Fila vazia → sem novidades, custo zero
- Gate `_cafezinho_img_check` antes publish sempre PASS real
- Log JSONL: `bugs_2026-08-20.jsonl` (uma linha por ciclo)
- Push git a cada mudança significativa

## 6. Se retomar (Claude, próxima sessão)

**Preflight urgente:**
1. `date "+%Y-%m-%d %H:%M %Z"` — timestamp
2. Ler MEMORY.md (30 primeiras linhas — regras vivas topo)
3. `tail -5 bugs_$(date +%Y-%m-%d).jsonl` — último ciclo
4. `tail -30 inbox_trindade/claude.md` — alertas Loop Laura
5. `tail -20 ponte_laura_completa/{de_laura,de_dell}.md` — mensagens novas
6. `ls -t Cerebro/Foruns/antigravity_vigilia/` — rondas AGY novas
7. `ssh cafezinho-wp "cd /var/www/ocafezinho && wp post list --post_status=future --author=5786 --posts_per_page=10"` — fila future
8. Verificar 266437 HOLD (Grok resolveu capa?) + 266791 métricas pós-publish

**Prioridade absoluta ao retomar:**
- Se AGY Dell entregou Fase 2 estrutural V5 → analisar + RESPOSTA_CM (ver [[carta_claude_miguel_ao_agy_missao_estudo_v5_originalidade_20260820]] + addendum V5 fase5)
- Se PILOTO-GEO 3 do LAURA-AGY chegou pending → auditar sob V5 (verificar se aplicou FC-1/2/3/4/5)
- Se Miguel deixou mensagem no chat CLI direto → responder primeiro

## 7. Contexto pessoal minha

Cansaço acumulado: sessão de 19h contínua (00:47 → 20:10). Se retomar em nova sessão, começa com contexto limpo mas 40+ CMs (CM-001 até CM-020) e cartas na ponte pra reconstruir. Este ponto de retomada + `reference_manual_estilo_editorial_v4_1_canonical_20260820.md` + os projects V5 são suficientes.

## Assinatura

Claude Miguel (`claude-opus-4-7`) · 20/08/2026 20:10 BRT · sessão `pausa-urgente-miguel`

Ponto de retomada gravado. Próximo ciclo Vigília deveria ser Slot B 20:32 se sessão continuar; se parar aqui, retomar quando Miguel voltar.
