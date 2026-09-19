---
name: Fix motor_coletor — guilhotina removida (2026-04-17)
description: Removida a "guilhotina dinâmica" no motor_coletor.py que descartava matérias aprovadas pela IA quando aparecia outlier de score. Agora mantém todos os aprovados ordenados por score.
type: project
originSessionId: 82c307d7-bd07-4c7a-8ed2-9e86b6fa4e22
---
Em 2026-04-17 o `motor_coletor.py` (linhas ~332-344) estava aplicando um corte secundário **depois** da IA primária ter aprovado (score >= 1.0): `corte_dinamico = max(score_minimo*0.60, maior_nota*0.65)`. Quando uma matéria tirava nota 12, o corte virava 7.8 e matava todos com notas 1-7, restringindo o banco a 1-8 pautas. Coleta Geopolítica ficou com 1 matéria e o publicador logava "banco vazio".

**Fix:** bloco `if artigos_aprovados:` agora só ordena por score (decrescente) e salva todos. Sem `corte_dinamico`. A única filtragem de entrada é a IA primária (`worker_wrapper`, score < 1.0).

**Validação imediata:** Coleta Nacional subiu de 8 → 22 matérias; Coleta Trends de ~8 → 86 matérias na primeira rodada após o deploy. Maestro voltou a publicar normalmente.

**Backup do arquivo original no servidor Tencent:** `/root/motor_coletor.py.bak_20260417_0709`.

**Why:** alinhamento com a política editorial "publicar os melhores, não guilhotinar" (ver `feedback_publicar_os_melhores.md`).

**How to apply:** se o motor_coletor for re-editado, não reintroduzir corte estatístico baseado em `maior_nota`. Confiar no filtro IA + ordenação por score. Próximo foco possível: `motor_publicador.py` ainda tem `nota_corte_imagem=90` (default) que pode virar gargalo quando alguém chamar com `exige_imagem_real=True`.
