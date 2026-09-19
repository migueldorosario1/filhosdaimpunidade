---
name: project-limpeza-qualidade-r2-v3-20260623
description: Limpeza massiva R2 V3 (1059→754) removendo 330 imgs <800px + patch preventivo catalogador com PIL gate (min 800px / 30KB) populando largura/altura (bug crítico schema nunca populado). 23/06 04:35-10:40 BRT.
metadata:
  node_type: memory
  type: project
  originSessionId: 831ab0d8-9f43-4146-9bf9-65f536fabdf7
---

Limpeza massiva R2 V3 executada 23/06 04:35-10:40 BRT após Miguel flaggar erro de baixar imagens sem especificar qualidade mínima nos sprints 22/06. Threshold AUTH: **800px (portal ideal) — 330 removidas** (326 <800px originais + 4 novas do cron 23/06 também <800px).

**Why:** Miguel pediu "limpar imagens pequenas demais, sem definição, sem legenda, sem descrição, sem crédito. deixar apenas imagens boas e definidas". Erro meu: populei R2 V3 (sprints 22/06) sem gate de qualidade. Miguel corrigiu 23/06 ~10:15 BRT pedindo diagnóstico de qualidade — executei a limpeza.

**How to apply:** Ao diagnosticar problemas em R2 V3: checar `/root/validar_dims_completo.py` (baixa tudo via boto3+PIL), `/root/ruins_r2_v3.json` (lista de ruins), `/root/backups/ruins_r2_backup_20260623.tar.gz` (backup 318MB das 326 deletadas). Banco caiu 2.8MB→2.0MB pós-VACUUM. Counts: 754/754/754 sincronizados.

**Bug crítico de schema corrigido:** `agente_catalogador_midia_r2_v3.py` declarava campos `largura`/`altura` no schema (linha 82-83) mas **NUNCA os populava** — 100% das 1059 imagens estavam NULL. Patch agora abre PIL antes do upload, extrai width/height, popula no INSERT.

**Patch preventivo deployado (MD5 `2a5343fce44be617230e7985f0160994`):**
- Importa PIL com fallback graceful (try/except ImportError)
- Constantes `MIN_LADO_PX = 800`, `MIN_BYTES = 30000`
- Em `catalogar_arquivo` antes do upload: abre PIL, rejeita com `ValueError("GATE_QUALIDADE: menor lado {N}px < 800px")` se <800px OU bytes <30KB
- Bypass `entidade == 'smoke'` (teste técnico 1x1 placeholder)
- Popula campos `largura`/`altura` no INSERT SQL + ON CONFLICT update
- Backup pré: `/root/V3/agente_catalogador_midia_r2_v3.py.bak_pre_quality_gate_20260623`

**Distribuição final 754 imagens (todas >=800px):**
- Política 448 + Geopolítica 250 + IA 32 + Economia 23 + smoke 1 = 754
- Por bytes: <50KB=1 (smoke), 50-200KB=115, 200KB-1MB=404, >=1MB=234
- Top cobertura: Alexandre de Moraes 23, Alckmin 19, Tebet 19, Carmen Lúcia 18, Lula 18, Bolsonaro 16, Xi 16, Putin 16.

**Cobertura reduzida pós-limpeza (alerta p/ próximos sprints):**
- Khamenei: 16→0 (TODAS as 16 eram <800px — Wikimedia retornou thumbnails pequenos)
- Lula: 34→18
- Bolsonaros (Jair/Flávio/Eduardo/Carlos): 17-21→16 cada
- Arthur Lira, Sheinbaum, Milei, Raisi: perderam ~50% cobertura cada

**Próximo sprint repor:** usar fontes Wikimedia de alta resolução (categoria "Quality images" / "Featured pictures") + Flickr oficiais (Lula Oficial NSID 157736962@N05 tem 46.879 fotos CC BY-SA 4.0 em alta resolução).

**Vigília cron 04:00 BRT 24/06:** primeiro run com gate ativo. Log `/var/log/r2_joia.log` deve mostrar `ValueError: GATE_QUALIDADE` para imagens rejeitadas (esperado). Checar pós-04:30 BRT 24/06.

**Cartas paralelas:**
- Carta ao Codex 22/06 16:58 BRT (`Foruns/carta_codex_auditoria_compat_r2_v3_20260622.md`) com 5 pontos auditoria — AGUARDA resposta
- Adendo Codex 23/06 11:00 BRT (`Foruns/inbox_trindade/codex.md`) atualizando estado pós-limpeza + contexto cobertura reduzida

Fórum completo: `Foruns/forum_limpeza_qualidade_r2_v3_20260623.md`. Relacionado: [[project-cron-joia-r2-v3-20260622]] (sprint joia original), [[feedback-janitor-banco-midia-protocolo-20260621]] (protocolo limpeza), [[feedback-disco-tencent-100-emergencia]] (rotação backups).
