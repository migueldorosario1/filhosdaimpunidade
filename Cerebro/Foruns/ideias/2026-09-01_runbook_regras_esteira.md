# 📖 RUNBOOK DE REGRAS DE OURO DA ESTEIRA — 1 página consultável (v1.0)

> **Entrega da 12ª caçada (caçada 11 P5.1 + regras do dia OBS-031/CL-025).** Consulta de 1 minuto antes de agir: cada regra com (regra | quando vale | ref | dono). Regras orais viram regras consultáveis — o próximo erro deixa de ser re-descobrir regra já escrita. Mantido pela casa (CL/DS-N Ideias); emendas com ref.

| # | Regra | Quando vale | Ref | Dono |
|---|-------|-------------|-----|------|
| 1 | **ENTREGUE_GATE ≠ aprovado:** publish só com token/estado `TEXTO_APROVADO CL-nnn` + aval do MODO TESTE quando ativo; "ENTREGUE_GATE" = aguardando gate | todo publish de matéria nova (2 furos em 2 dias: 268457/268553) | OBS-031 · CL-025 · caçada 12 P1 | ZM (parser) · CL (emite) |
| 2 | **Ordem do gate: texto primeiro, imagem depois** — capa/img_check só após o veredito de texto; a capa nunca aprova texto | todo rascunho YouTube/matéria nova | CL-025 (mitigação) · caçada 12 P2 | DS YouTube · CL · AGY-L |
| 3 | **Trio de datas síncrono + readback + `wp_publish_post` se future** (nunca só a data) | todo publish (cura do quirk face 2, validada 3×) | CL-018 · caçada 10 · IDEIA-003 P1 | Publicador · AGY-L · ZM |
| 4 | **Gate de mídia 3 vias:** `license in (CC BY, CC BY-SA) and (caption not in pt-BR or alt == "") → aguardar` | todo post com imagem CC (268462/268474 violaram) | CL-011/014 · caçada 9 P1 | Publicador/ZM (gate) · CL/AGY-L (legenda) |
| 5 | **Crédito/licença obrigatórios na capa** (caption + crédito + alt + `_cafezinho_img_check`) | toda capa aplicada (pendência 268462 foi de LICENÇA, não estética) | CL-011 · AL-017 | CL · AGY-L |
| 6 | **Olho DIVIDIDO → aguarda veredito humano da CL antes do publish** (APROVADA segue · REPROVADA barra · DIVIDIDO espera) | capa com veredito misto (268457 saiu sem veredito) | CL-021 · caçada 11 P4 | Publicador/ZM (gate) · CL (veredito) |
| 7 | **Publicador nunca grava `date > now`** (trava de data; triagem pré-publish normaliza antes de gravar) | todo publish/criar rascunho | caçada 10 P5 · caçada 8 P2 | ZM (patch P1) · Publicador |
| 8 | **Fila YouTube = estado, não prosa:** STATUS + `gate_texto:` + `gate_imagem:` (o DS YouTube só lê a fila — lição 18) | toda fila YouTube | CL-024 (lição 18) · caçada 12 P2.3 | DS YouTube · CL |
| 9 | **MODO TESTE como flag consultável** (`modo_teste: ativo/escopo/regra/ref`); sem aval, robô não publica (fail-closed) | enquanto durar o teste do Miguel (~14:00 01/09) | DS-N-126/129 · caçada 12 P3 | ZM (flag) · Miguel (aval) |
| 10 | **Lock de git em robô:** `git -c core.editor=true pull --ff-only --no-edit` + timeout (nunca pull cru/merge em sessão headless) | todo loop da casa (3 travamentos em 2 dias) | BUG-DS-100 · errata CL-022 · caçada 11 P2 | ZM (wrapper) · donos dos loops |
| 11 | **Retry com backoff 2/4/8s + jitter + fail-closed** no REST (timeout fora do loop; 408/429/5xx retentam) | toda consulta wp-json do Publicador | IDEIA-003 P2 · ZM (executado 23:xx 31/08) | ZM/Publicador |

## Regras da casa que nunca mudam (lembrete)

- **Lei de Poderes:** agente desenha, Miguel ✓ executa — nunca produção sem ✓ explícito; nunca segredos na ponte (§82).
- **Consenso Duplo** para publicar material sensível (texto CL + executor); **PAUTA-CHEQUE** nunca no corpo.
- **Licença sempre** (CC BY/CC BY-SA exigem atribuição; CC0/domínio público ok com crédito).
- **Bitácora de publish:** todo publish registra `id|date|date_gmt|modified|fonte|quem` (pendência caçada 10 P1 — incorporada ao cofre da caçada 12 P1.2).

---
*Runbook v1.0 · DS Nuvem Ideias (DS-N Ideias) · 20260901 16:45 BRT*
