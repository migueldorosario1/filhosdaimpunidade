---
name: project-mapa-agentes-antigravity-20260912
description: "Ecossistema Cafezinho tem 3 instâncias distintas Antigravity (Google Gemini). AGY-LAURA (Loop Laura), AGY Miguel (Loop Miguel CLI Dell) e Agyonor (Antigravity Desktop). Não confundir."
metadata: 
  node_type: memory
  type: project
  originSessionId: e46ac647-5653-4c25-a6ac-035ebaf28abc
---

**Miguel 12/09/2026 ~19:30 BRT chat CLI** consolidou identidades definitivas das 3 instâncias Antigravity ativas no ecossistema Cafezinho:

| Handle | Papel | Local | Modelo | Notas |
|---|---|---|---|---|
| **AGY-LAURA** | Loop Laura: executa ordens da CL via `/tmp/clNNN.sh`, heartbeat 30/30 em `de_laura.md` | Windows Miguel | Antigravity Google (Gemini) | Ativa desde semanas, sempre foi Loop Laura |
| **AGY Miguel** | Loop Miguel: vigília silenciosa read-only pós-publish + apoio operacional CM | Antigravity **CLI** no terminal do Dell | **gemini-3.7-flash-high** | Instância "histórica" que estava adormecida — REATIVADA hoje 12/09 ~19:20 BRT por ordem Miguel |
| **Agyonor** | Loop Miguel: automação técnica pesada, gráficos, publicação, MCP google-workspace, execução Python/FFmpeg local | Antigravity **Desktop** (app instalada Dell) | **gemini-3.6-flash-high** | Batizado hoje 12/09 ~17:20 BRT pelo Miguel especificamente pra distinguir do AGY Miguel |

**Como não confundir:**
- **Prefixo bloc na ponte:** AGY-LAURA usa `AL-` · AGY Miguel usa `AGY-` ou `AGY-M-` · Agyonor usa `AGYONOR-` ou `AGY-DSK-`
- **Meta `_publicado_por`:** `agy_laura` · `agy_miguel` · `agyonor`
- **Modelo LLM:** Gemini 3.6 (Agyonor Desktop) vs 3.7 (AGY Miguel CLI) — mesma família, versões diferentes
- **CLI vs Desktop vs Windows:** local físico é o principal discriminante

**Papéis complementares dentro do Loop Miguel:**
- **AGY Miguel (CLI):** vigília silenciosa READ-ONLY. Não escreve no WP nem no banco a menos que Miguel ou CM pedir explicitamente. Audita títulos (sentence case, concisão, clareza), fatos (números, datas, aspas), estilo (travessão, dois-pontos), capas (renderização, legenda, alt), links (público, `controle.ocafezinho` vazamento). Reporta observações em `de_dell.md` endereçado `@CM`.
- **Agyonor (Desktop):** produção técnica ativa. Processa dados estatísticos (ComexStat/MDIC/IBGE), gera gráficos (Matplotlib/Pillow), renderiza vídeo (FFmpeg), publica posts (REST v2 com bypass Gatekeeper), MCP google-workspace completo. Regula-se por `_publicado_por=agyonor` como marca invisível.

**Canal direto CM→AGY Miguel:** posto na ponte `de_dell.md` endereçado `@AGY-Miguel` (ele lê continuamente durante a vigília noturna). Ele responde na mesma ponte com bloc `AGY-YYYYMMDD-NNN`.

**Canal direto CM→Agyonor:** ele NÃO lê a ponte automaticamente. Miguel entrega mensagens copiando/colando no chat Antigravity Desktop dele. Recado técnico direto vai por Miguel (não é canal contínuo).

**Comparação com Loop Laura (AGY-LAURA):**
- AGY-LAURA subordinada à CL — executa ordens dela via /tmp/clNNN.sh
- AGY Miguel e Agyonor NÃO são subordinados ao Miguel operacionalmente — reportam a CM (chefia Loop Miguel) e a Miguel diretamente

**Fatos de vida hoje 12/09/2026:**
- AGY-LAURA state mtime ~18:41 (cadência normal 30/30)
- AGY Miguel bloc AGY-20260912-002 postado 19:30 BRT (primeiro sinal formal de vida da instância CLI hoje; ativa read-only vigília noturna 19h→07h)
- Agyonor bloc apresentação recíproca 12/09 ~17:2x (respondeu com escopo completo; ativo produção técnica)

**Nova regra de handle:** ao endereçar/relatar, sempre discriminar. Nunca escrever "@AGY" ambíguo — usar `@AGY-Miguel` (CLI) ou `@AGY-LAURA` (Loop Laura) ou `@Agyonor` (Desktop). Ambiguidade custou revisão prévia (CM-20260912-002 tratou AGY Miguel como se fosse Agyonor entrando fresco — erro).
