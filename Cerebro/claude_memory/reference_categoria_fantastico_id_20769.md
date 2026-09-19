---
name: reference-categoria-fantastico-id-20769
description: "Cat WP \"Fantástico\" (slug=fantastico, ID=20769) criada 22/06 01:54 BRT pra substituir a extinta Sobrenatural (20579) como editoria do agente_fantastico — ciência leve, arqueologia, naufrágios, cosmologia, curiosidades históricas. Taxonomia patch §92 aplicado em /root/taxonomia_wordpress.json (30 keywords sobrenatural/mistério/ovni/alien remapeadas 20579→20769)."
metadata: 
  node_type: memory
  type: reference
  originSessionId: f312988d-5dc6-4ea6-b08a-94b4cada57ec
---

🎬 **Categoria "Fantástico" (ID=20769, slug=`fantastico`, URL `/fantastico/`)** criada via WP REST API em 22/06 01:54 BRT como sucessora da extinta cat 20579 "Sobrenatural" (descontinuada por Miguel 18/06 — ver [[project-cafezinho-media-group-diretriz-18jun]]).

**Por que existir cat Fantástico em vez de só usar Ciência (19936)?**
O `agente_fantastico.py` cobre um nicho híbrido: ciência leve + arqueologia + naufrágios + cosmologia + curiosidades históricas. Misturar tudo em "Ciência e Tecnologia" (19936) diluiria a editoria séria. Cat dedicada permite filtros/feed próprios e SEO específico.

**Caso fundador 2026-06-22 01:43 BRT (#260164)**: agente_fantastico publicou "Barra de prata de US$ 100 mil emerge das profundezas em naufrágio lendário na Flórida" (arqueologia subaquática real, galeão Atocha 1622, Mel Fisher) com cats=`[20699 no_home, 20579 Sobrenatural]`. Miguel apontou que isso era erro de categoria — pauta é Fantástico, não Sobrenatural.

**Cura §51 imediata aplicada ao #260164**: PATCH cats=`[20769, 20699]` (Fantástico + No home).

**Patch §92 estrutural aplicado** em `/root/taxonomia_wordpress.json` (backup `*.bak_pre_20579_20769_20260622_0157`): 30 keywords agora apontam pra 20769:
- sobrenatural, paranormal, paranormais
- extraterrestre(s), ovni(s), ufo, alien(s), alienígena(s)
- mistério(s), misterio(s), ocultismo, esoterismo
- fantástico(a), fantastico(a)

E `/root/util_dedupe_fantastico.py:31` atualizado: `CATEGORIAS_FANTASTICO = {19936, 20699, 2403, 775, 1100, 20769}` (backup `.bak_pre_20769_*`).

**Validação smoke**: `python3 -c "..."` confirma `resolver_termos_wp("mistérios") → 20769`. py_compile OK em ambos.

**How to apply:**
1. Próximas publicações do `agente_fantastico` (cron `8,23,38,53 * * * *` + maestro */10) vão automaticamente classificar pautas tipo arqueologia/naufrágios/curiosidades em cat 20769.
2. Posts antigos de cat 20579 NÃO foram migrados — quem quiser arquivar histórico do Sobrenatural pode rodar query SQL bulk `UPDATE wp_term_relationships SET term_taxonomy_id=20769 WHERE term_taxonomy_id=20579` (futura limpeza, não urgente).
3. Cat 20579 fica órfã no WP (pode ser deletada ou mantida como histórico — recomendo manter pra não quebrar links antigos).
4. Cron `robo_coleta_sobrenatural.py` continua DESATIVADO (`# DESATIVADO_SOBRENATURAL_20260618_1546`) — Fantástico NÃO coleta Bigfoot/Champ/UAP, só o que vem via agente_fantastico (ciência levinha).
5. `agente_sobrenatural.py` (39KB, /root/) existe mas NÃO roda. Pode deletar futuramente.

Aplica em conjunto com [[project-cafezinho-media-group-diretriz-18jun]] (sobrenatural descontinuado mas ciência séria mantida).
