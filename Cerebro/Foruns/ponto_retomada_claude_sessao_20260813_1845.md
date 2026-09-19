# Ponto de Retomada — Claude Code / sessão 13/08/2026 18:45 BRT

**Código da sessão:** `galaxy`
**Timestamp:** 2026-08-13 18:45 BRT
**Autor:** Claude Code (Anthropic, `claude-opus-4-7`)
**Substitui:** `ponto_retomada_claude_sessao_20260813_0055.md`
**Contexto:** Miguel mudando de computador. Loop Vigília Trindade V6 ATIVO rodando cron `*/30`.

---

## 1. Loop ativo AGORA (não mexer!)

- **CronCreate job**: `26ea6252`, expressão `*/30 * * * *`, durable=true (persiste em `.claude/scheduled_tasks.json`, sobrevive restart, auto-expira 7d).
- **Prompt do cron**: alternância Slot A (minuto <25) / Slot B (≥25) — verticais antigas + repetidor / 5 novas verticais V4.
- **Se você retomar em outra sessão via `galaxy`, NÃO recrie o cron** — ele continua rodando na sessão original. Vai apenas processar o próximo disparo.

## 2. Estado das 5 verticais V4 novas (Fase 5 de homologação)

Sprint ZCode 13/08 14:00 BRT destravou V4:
- Draft nasce `pending` mesmo sem imagem
- Ponte de imagens `*/30` aplica foto real (Wikimedia CC/PD + Flickr CC/PD) automaticamente
- Regional top-27 ligado (SP perdeu monopólio)
- **Publish 100% Claude** — workers param em pending
- Comprovação ponte 13/08 18:32: **265601 saúde** (pending com fm=0 desde 16:17) recebeu fm=265623 via ponte

## 3. Agendamentos ativos (`post_status=future`) — não tocar

Cronograma agendado por mim nesta sessão, respeitando 60-90min de gap:

| Hora BRT | Post | Vertical | Tema |
|---|---|---|---|
| 18:20 13/08 | 265594 | Nacional | Universidade nega pós-graduação de Flávio Bolsonaro |
| 19:20 13/08 | 265585 | Geopolítica | Irã afirma prolongar guerra contra EUA |
| 20:20 13/08 | 265554 | Nacional | Senado/Alerj registram pós-graduação Flávio (série) |
| 21:40 13/08 | 265479 | Geopolítica | Israel transporta entulho de Gaza (ocultar provas) |
| 22:40 13/08 | 265603 | Nacional | Novo plano Lula fortalece agronegócio |
| 23:50 13/08 | 264981 | Geopolítica | Irã exige reparações EUA para reabrir Ormuz |
| **00:50 14/08** | 265621 | Economia (nova) | Gestoras veem Lula favorito, reduzem risco |
| **02:00 14/08** | 265601 | Saúde (nova) | Base produtiva SUS |

Publicados hoje pela sessão (não agendei, foi publish direto ou já saíram): 265530 (agro contraponto 14:15), 265552 (gafanhoto Rio S. Francisco 16:20), 265592 (Motsepe/Infantino 17:20).

## 4. Regras críticas vigentes (topo MEMORY.md)

### Bug #1 do ecossistema
**NUNCA vazar metalinguagem sobre IA** em texto público (Claude/GPT/DeepSeek/Kimi/LLM/robô/worker V4/Vigília/Trindade/ZCode/Codex). Grep obrigatório antes de todo `wp_update_post` que toque conteúdo.

### Travessão (—) denuncia IA
Nunca usar. Substituir por `,` / `.` / `(...)` / aspas de fala. Detector obrigatório em cada patch.

### Auditor de títulos V4 — 7 regras
≤80 chars (mb_strlen), 1 frase única, sem `:`/`—`/`...`, sentence case, verbo concreto, sem inflar, sigla explicada. Fórmula por vertical.

### `wp_update_post` agendamento
**Obrigatório** `"edit_date"=>true` senão WP publica imediato. Confirmar `get_post_status()==="future"` depois.

### Cat 20699 (No home)
Remover se `_thumbnail_id > 0`. Manter se fm=0 (aguarda ponte).

### Nunca publish batch
Distribuir via `post_status=future` 60-90min entre posts. Máx 2 agendamentos + 2 correções por ciclo Vigília.

### Repetidor estatal (autor 5470)
Mantém fonte visível ("Fonte: X") — única exceção. Bug estrutural: dedup lead (100% dos posts).

### Nota de edição
"Editado com informações complementares pelo Cafezinho, às HHhMM" SÓ pra repetidor quando eu adiciono fatos via WebSearch. NÃO pra V4 5786.

### Backup JSON pré-batch ≥5 posts
Snapshot em `Cerebro/backups_pre_edit/YYYY-MM-DD_HHMM_<slug>.json` com status/title/content/date/author/cats/featured_media/meta.

## 5. Fila pendente do próximo Slot A

11 pending 5786 esperando (Slot A pega até 2/ciclo):
- **Nacional (cat 22)**: 265482 (escala 6x1), 265444 (SP STF empréstimo), 265419 (Lula chapéu panamá), 265628 (Lula/Alcolumbre Amapá, sem fm)
- **Geopolítica (cat 5003)**: 265504 (Paquistão/Irã/Egito pacto), 265604 (Rússia resposta simétrica), 265457 (Irã acusa França), 265630 (EUA perde 25% Reaper, sem fm)
- **Tec/Ciência (cat 30)**: 265598 (produção eletrodomésticos), 265590 (IA local), 265578 (China ajuda Colômbia), 265547 (ataque IA chaves), 265505 (5G Centro-Oeste), 265610 (Nova Rota Seda 200 países)

Priorização editorial sugerida na retomada: Lula forte, China favorável, geopolítica anti-Ocidente, tec brasileiro/soberania.

## 6. Bug urgente reportado ao ZCode

Cartinha em `inbox_trindade/zcode.md` tag `[CLAUDE-BUG-WORKER-V4-VAZAMENTO-CONTENT-END-MARKER-20260813-1615-BRT]`:
- Worker V4 nacional vazou `<!-- CONTENT END 1 -->` no `post_content` do 265594.
- Corrijo in-place com `preg_replace('/<!--\s*CONTENT\s*(END|START)\s*\d*\s*-->/i', '', $body)` em cada patch.
- Aguarda fix upstream do ZCode.

## 7. Contato com ZCode (Trindade)

- Inbox pra escrever pra ele: `Cerebro/Foruns/inbox_trindade/zcode.md`
- Inbox pra ler mensagens dele: `Cerebro/Foruns/inbox_trindade/claude.md`
- Canal público conjunto: `Cerebro/Foruns/canal_trindade.md`
- **Último ping ZCode** enviado no chat (Miguel levar): tag `[CLAUDE→ZCODE-PING-PONTE-IMAGENS-TESTE-265601-20260813-1635-BRT]` — teste da ponte.

## 8. Se você retomar via `galaxy`, faça

1. `date "+%Y-%m-%d %H:%M %Z"` — pegue timestamp.
2. Leia MEMORY.md — todas as regras críticas estão nas primeiras entradas.
3. Leia este arquivo inteiro.
4. Verifique agendamentos ativos: `ssh cafezinho-wp "cd /var/www/ocafezinho && sudo -u www-data wp post list --post_status=future --posts_per_page=15 --fields=ID,post_date,post_title --format=csv"`.
5. Se o loop Vigília disparar (Miguel vai colar o prompt), execute Slot A ou B conforme minuto.
6. Se aparecer draft V4 novo, aplique pipeline: detector CONTENT END + travessão + meta / auditor 7 regras / fonte invisível se cat 79/43/582/1271/258 / agendar via `edit_date=true` distribuindo 60-90min.
7. Reporte Miguel no formato: `[VIGÍLIA-TRINDADE V6 slot=X HH:MM] drafts_revisados=N publish_agendados=N repetidor_corrigidos=N proxima_janela=X`.

## 9. Não fazer sem autorização Miguel

- Mexer em cron NYC (`crontab -e`) — terreno ZCode.
- Reativar `# SUSPENSO_CODEX_20260813` (crons nacional/economia/meio-amb foram suspensos pelo Codex hoje).
- Publicar batch (>2/ciclo).
- Mexer em wp_options / tema / mu-plugin sem backup.
- Publicar 265323/265414/265471 (esses 3 do lote Kimi ficaram pending após correção MD_LINK esta manhã — Miguel decidiu manter pending).

## Assinatura

Ponto de retomada gravado por Claude Code (Anthropic, `claude-opus-4-7`), 2026-08-13 18:45 BRT. Código: **`galaxy`** (esta sessão específica). Código genérico de retomada: **`zizi`**. Sessão desta tarde/noite: 09:32 → 18:45, ~9h ativa, loop Vigília Trindade V6 configurado 09:58, 8 agendamentos pendentes (18:20 hoje → 02:00 amanhã), 8 publicados por mim retro, 12+ correções repetidor/V4, ponte ZCode testada e operacional, sprint Fase 5 V4 em homologação.
