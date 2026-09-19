---
name: wp_login_v4_exclusivo_5786_antigravity_2018
description: "Arquitetura WP — autor 5786 exclusivo agentes V4, autor 2018 (James2017) é Miguel manual"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f7f41cc3-fbd3-490e-a680-02f36a81230e
---

**Regra:** A partir de 27/07/2026 20:00 BRT, WP tem 2 contas de escrita:
- **Autor 5786** (`redacao-nova`): EXCLUSIVO agentes V4 automatizados (Sentinela, workers, coletas)
- **Autor 2018** (`james2017`): Antigravity Desktop manual de Miguel (humano, ignorar em pipelines V4)

**Por quê:** Miguel criou conta separada pra não contaminar histórico automático. Antes: heurística "5786 sem zizi_job_id = humano" (descontinuada). Agora: todo 5786 = agente, período.

**Como aplicar:**
1. Varredura duplicatas/bugs: IGNORAR autor 2018 (não é V4, não relevante pra correções automáticas)
2. Detectar BUG: se autor 5786 SEM `zizi_job_id`/`_agente_origem` → tag `bug_agente_sem_meta` (agente não populou metadata, falha estrutural)
3. Vigília Haiku cron 63042696: adicionar check de zizi_job_id missing

**Impacto:**
- Drafts elegíveis Vigília: filtro `author==5786` continua igual (ok)
- Duplicatas publicadas: nova cláusula `and p['author']!=2018` (ignorar Miguel manual)
- JSONL Vigília: novo campo `bugs_encontrados` (agora rastreia `bug_agente_sem_meta` além dos textuais)

**Validação:** Cron 63042696 recriado 27/07 20:XX BRT com 2 mudanças inline.
