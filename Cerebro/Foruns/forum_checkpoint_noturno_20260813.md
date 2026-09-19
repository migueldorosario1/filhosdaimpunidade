# CHECKPOINT NOTURNO — 13/08/2026 02:00 BRT

**Sessão:** ZCode GLM-5.2 (Kimi/Qwen 🔴🔴, fim da cadeia)
**Estado:** produção ativa, operacionalmente degradada, contenção noturna aplicada

---

## ESTADO DO CRON (contenção noturna)

| Vertical | Coleta+Intake | Draft Worker | Motivo |
|---|---|---|---|
| **Ciencia** | 🟢 ativo | 🔴 SUSPENSO | bug idempotência (26 duplicatas) |
| **Nacional** | 🟢 ativo | 🔴 SUSPENSO | draft_not_confirmed sem causa observável |
| **Meio Ambiente** | 🟢 ativo | 🔴 SUSPENSO | mesma falha indeterminada |
| **Economia** | 🟢 ativo | 🔴 SUSPENSO | primeira redação sem supervisão |
| Geopolítica | 🟢 ativo | 🟢 ativo | produzindo (reparou imagem 265446) — ÚNICA com sucesso confirmado |
| Cultura | 🟢 ativo | 🟢 ativo | dedup funcionou (bloqueou duplicata) |
| Esporte | 🟢 ativo | 🟢 ativo | em image_pending (NÃO está produzindo) |
| Saúde | 🟢 ativo | 🟢 ativo | perdendo rodadas por lock (degradado) |

## OS 56 PENDING — diagnóstico correto (Codex)

### Composição
- **28 duplicatas inequívocas** (3 temas × 8-10 cópias cada):
  - China/Indonésia exercício naval: 10 cópias
  - África minério bruto: 8 cópias
  - China centros IA 100 dias: 10 cópias
- **6 do grupo Trump/Irã**: precisam revisão editorial (podem ter enquadramentos diferentes)
- **~22 únicos reais**

### Imagens (números reais do Codex)
- Política: 9/9 com imagem
- Geopolítica: 17/18 com imagem
- Tecnologia: 15/29 com imagem (14 sem)
- **Total: 41 com imagem, 15 sem**

### Causa raiz da duplicação (Codex)
**Falha de idempotência transacional:**
1. Worker cria post no WP ✅
2. Falha em `wordpress_draft_taxonomy_not_confirmed` (depois de criar, antes de marcar)
3. Candidata volta para `status='new'` no SQLite
4. Próximo ciclo: mesmo `item_key` → novo post → loop

**NÃO é ausência geral de marcação** — é falha de ordenação: o post é criado antes de o candidato ser marcado como drafted.

## CORREÇÕES DO CODEX QUE ACEITEI (3ª auditoria)

1. **`hourly_quota` = cooldown local de 55min do worker** (NÃO rate limit do Gemini — eu estava errado)
2. **Tecnologia "100% IA" é impreciso** — IA é fallback sem cota, não "todas as imagens são IA"
3. **stderr do subprocesso é `DEVNULL`** (não vai pro log do cron — ambos descartados)
4. **Priority 1 reformulada**: criar/manter draft sem imagem para reparo assíncrono (NÃO publicar sem imagem)
5. **Mensagem de erro corrigida**: `cota_ia_bloco_50pct_estourada` (era `30pct`)

## PLANO PARA AMANHÃ (13/08, durante o dia)

### Prioridade 1: corrigir idempotência
- Registrar `wp_post_id` imediatamente após criar o post
- Setar candidata para `wp_created/pending_validation` (não voltar pra `new`)
- Qualquer falha posterior retoma o MESMO post
- Checar `zizi_job_id` no WordPress antes de criar outro
- **Mexe em estado distribuído (SQLite + WP)** — fazer com backup, teste e rollback

### Prioridade 2: recuperar os 56 pending
- Gerar manifesto (grupo, item_key, IDs, imagens, versão escolhida)
- Escolher versão canônica (a tecnicamente completa)
- Mover duplicatas para lixeira WP (recuperável)
- Revisar grupo Trump editorialmente
- Avaliar publicação (ter imagem não basta)

### Prioridade 3: capturar stderr do subprocesso
- Mudar `stdout=DEVNULL, stderr=STDOUT` → capturar para log
- Permite diagnosticar `draft_not_confirmed`

### Prioridade 4: ajustar lock global
- Considerar `flock` com timeout (espera limitada) em vez de `flock -n` (skip imediato)

### Prioridade 5: reativar as 4 suspensas
- Após idempotência corrigida: ciencia, nacional, meio_ambiente, economia

## MIGRAÇÃO COMPLETA (11/08 → 13/08)

### O que foi feito (resumo)
- 5 verticais V4 migradas do espelho pro CANÔNICO (cultura, economia, meio_ambiente, esporte, saúde)
- Cron ativo (cadências: cultura/economia 4h; meio_ambiente/esporte/saúde 8h)
- Front-page canônico: 5 blocos + Vídeos + Mais Vistos + Tecnologia restaurado
- `VERTICAIS_ESPELHO` desativado (publicam no canônico)
- Espelho religou Basic Auth
- Logo v10 (11KB) fixada nos dois
- Bug status draft corrigido (preserva status)
- Compressão imagem <500KB
- Geopolítica IA cota 50%
- Nacional exclui no-home(20699) do bloco principal; Linha do Tempo + Recentes mostram
- `category__not_in => array(28, 20751)` em todos os blocos (Vídeos/Youtube excluídos)
- CSS: linha vermelha removida + nome editor #8B0000
- Mais Vistos: automatizado (cron diário 06h, 30 dias, sem views, link público)
- Lock global de redação (flock)
- 3 auditorias do Codex (2ª 🔴 resolvida; 3ª 🔴 operacionalmente degradada)
- Carta longa pro Claude Code (checklist de revisão)
- Carta de auditoria de títulos pro Claude Code

### Ordem final do front-page canônico
```
Nacional → Geopolítica → Tecnologia → Economia → Vídeos →
Cultura → Meio Ambiente → Saúde → Esporte →
Linha do Tempo → Os 10 mais vistos → Recentes
```

## DOCUMENTOS NO CÉREBRO

| Documento | Assunto |
|---|---|
| `forum_checkpoint_final_20260813.md` | checkpoint estado técnico |
| `forum_resposta_3auditoria_codex_20260813.md` | resposta ao Codex (3ª auditoria) |
| `forum_resposta_codex_3auditoria_20260813.md` | solicitação formal da 3ª auditoria |
| `forum_carta_longa_claude_code_v4_canonico_20260812.md` | checklist de revisão pro Claude |
| `forum_curadoria_v4_cultura_20260812.md` | curadoria de pautas culturais |
| `forum_checkpoint_espelho_5_verticais_20260812.md` | checkpoint histórico (fase espelho) |
| `forum_resumo_trindade_20260812.md` | resumo dos 3 vértices |
| `forum_plano_migracao_canonico_20260812.md` | plano de migração (executado) |
| `cartinha_claude_auditoria_titulos_canonico_20260812.md` | auditoria de títulos |
| `cartinha_claude_code_fase0_v4_espelho_20260812.md` | fase 0 (desatualizada — migrou pro canônico) |
| `memoria_v4_5_verticais_encanamento_local_20260811.md` | memória técnica do encanamento |

## Backups no canônico
`front-page.php.bak_pre_*` · `style.css.bak_pre_*` · `header.php.bak_pre_v10_20260812`

## CONTINUIDADE
Para retomar: ler este checkpoint + `forum_resposta_3auditoria_codex_20260813.md`. O Miguel e o Gabriel vão publicar matérias boas amanhã (Política). As 4 verticais suspensas voltam após correção de idempotência.
