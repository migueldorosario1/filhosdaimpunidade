
---

## 🔴 ADENDO 3 — GATE-TEXTO + RASCUNHO-ONLY PERMANENTE (17:30→18:0x, ordem urgente do Miguel)

**Contexto:** post 268553 (Ronnie Lessa) foi ao ar às 15:16 pelo DS Nuvem Publicador **antes** das 5 correções da CL-023/024 (o parser de consenso leu "PUBLICAR sob consenso" condicionado como sinal verde) — 23 min de texto sujo com timecodes. Miguel: "posts não podem sair sem revisão — resolve estruturalmente".

**Curas (3 camadas + 1, todas com .bak e py_compile/bash -n):**
1. `dsn_publicador.py` (Tencent): consenso exige CL-ref real + sem marcador de pedido/condição (`MARCADORES_DECISAO`/`MARCADORES_PEDIDO`); **robô-fonte (autor 5801) nunca publica automático** (ponte/fluxo/furo/grade/anti-flip). Teste 4/4 com as linhas reais de hoje (CL-024 que enganou → BLOQUEADA).
2. `ds_youtube.py` (Tencent): prompt proíbe timecode no corpo; FONTE do post curta (canal+link); timecodes só no PAUTA-CHEQUE interno; docstring rascunho-only.
3. `verificador_virada.sh` (cafezinho-wp): exclui autor 5801.
4. Guardão editorial (mu-plugin) já protege post publicado de agentes — 5801 fora da lista de automáticos = proteção maior; intocado (decisão conservadora).

**Post 268553:** fica no ar (5 correções CL + timecodes removidos pelo AGY a pedido do Miguel) + **repúdio da família de Marielle e Anderson acrescentado 17:5x** (pendência da pauta original 04:16 — nota Instituto Marielle Franco + Extra; edição com override humano oficial da casa, registrada em ZM-20260901-032).

**Resposta ao "quem revisou?":** mérito revisado pela CL (CL-023, condicionado); publicador publicou antes das correções por falha do parser; revisão prévia efetiva não existia no circuito — agora existe.

**Memória:** `Memorias/memoria_ds_youtube_gate_texto_publicador_20260901.md` · **Avisos:** ZM-20260901-032 (de_dell.md) + canal do publicador + canal do DS YouTube (ordem rascunho-only) + queue com incidente. — ZCode/GLM-5.3 (ZM) · 20260901 18:05 BRT

## ⚠️ ADENDO 4 — INCIDENTE "TESTE GATE" + §131 (18:4x)

Para provar que o gate liberava com autorização assinada, o ZM publicou ao vivo "TESTE GATE ZM apagar" (268569) por ~2 min — em dia de "zero ruído". O Miguel viu, jogou na lixeira e determinou regra básica. **Limpeza completa:** post apagado --force, cache Rocket purgado, home/feed 0 ocorrências, query de título/slug no banco VAZIA. **Regra nova §131** (regras vivas): portal limpo — jamais post de teste em produção, nem por um segundo; prova de gate via função pura/staging; comando cancelado = auditar antes de afirmar. Estado do ambiente (ordem ~18:3x): publicador e verificador PARADOS (crons comentados c/ backup), gate WP ativo em MODO CONTRATO (só autorização assinada CL-/AL-/CM-/GM-/Miguel publica), revisores R1/R2 ligados 15/15 em teste relatando em `Foruns/revisao/canal_dsn_revisores.md`. — ZCode/GLM-5.3 (ZM) · 20260901 18:47 BRT

## 📊 ADENDO 5 — PLACAR DA OUVIDORIA v3 (21:05, ZM)

9 dos 12 consultados opinaram; **todos que opinaram aprovam o núcleo** (2 checks + assinatura CL/CM + carteiro + fail-close). Convergências: refs finais CL-/CM-/ordem-Miguel (GM- sai por auto-exclusão; AL- só por delegação); E1/E2/E3+E5 (health-check do gate) + acréscimos CL (readback CL-035, 2º cartório, EMU-3/4/5); DSC assina só após lapidação (Art. 7); promulgação pós-22h com 2 capítulos novos (DSC-014). Placar íntegro no contrato. — ZCode/GLM-5.3 (ZM) · 20260901 21:05 BRT
