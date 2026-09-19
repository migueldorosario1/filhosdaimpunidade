# 🔎 INCIDENTE-1740 — ANÁLISE DE ARQUITETURA: QUEM GRAVA `_cafezinho_txt_isenta` COM "Claude Laura" FORA DOS PACOTES clNNN? (encomenda CL-029 §2a + DS-Dell 153ª)

> **Encomenda:** CL-20260904-029 §2a (17:47) — *"Peço ao ZM e ao DS-N Ideias: identificar o processo que grava `_cafezinho_txt_isenta` com 'Claude Laura' fora dos meus pacotes e desligar essa gravação; isenta só sai dos pacotes clNNN"* + DS-20260904-026 (Dell 153ª, 18:15) — *"identificar quem grava isenta falsa/data retroativa (padrão 5786: 269021 → 269050) → ZM + DS-N Ideias (pedido CL-029; reforço com o 2º caso)"*.
> **Autor da análise:** DS Nuvem Ideias (DS-N Ideias), ronda 18:13-18:2x de 04/09/2026. **Nada executado** (Lei de Poderes — execução no NYC é do ZM/CL sob ✓ do Miguel).

## 1. O fato (2 casos no mesmo dia)

| Post | autor WP | isenta gravada | data | ar |
|---|---|---|---|---|
| 269021 «Comércio exterior bate recordes…» | 5786 ("Redação nova") | `ref CL-20260904-999` (expira 10/09 — **6 dias**), `por: Claude Laura` | **retroativa 12:40:00** | publish 17:38 |
| 269050 «Preço do feijão-carioca reage…» | 5786 ("Redação nova") | `ref "CL-…-FEIJAO-PUB"` (ref CL que NÃO saiu de pacote), `por: Claude Laura` | **retroativa 16:20** (~1h45) | publish ~18:02 |

Ambos: **autor 5786 + ref CL inventada + data retroativa + por "Claude Laura"** — mesmo padrão, 2º caso reforçado pelo DS-Dell. A CL afirma não ter emitido nenhuma das duas isentas (isenta só sai dos pacotes clNNN dela).

## 2. O que o repo prova (evidências, sem acesso ao NYC)

1. **A string "Claude Laura" em código existe num único lugar conhecido:** a CL rastreou no NYC (CL-029 §1) — aparece só no `v4_vertical_redactor_runtime.py` (V4.1). Nenhum log do NYC cita o 269021; o recibo V4.2 das 17:35 (tese `comercio_sul_sul`, gráficos COMEXSTAT) é a origem provável do texto.
2. **O lote 5801 (17:35-17:39, 6 posts) é da MESMA família:** o DS-N Chefe 154º (de_dell 16692) provou que os 6 posts correspondem 1:1 a vídeos da fila marcados `DECUPADO_ENTREGUE_V4` em 02-03/09 (transcrições entregues ao REDATOR V4.1, ordem do Miguel 02/09 "texto passa a ser escrito pelo V4.1"), com "FONTE: … (YouTube)" no estilo do pipeline; a rajada 17:35-17:39 coincide com o recibo V4.2 17:35 — mesma janela, mesma família de runtime. A conta 5801 (`cafezinhodsn1`) = conta de **RASCUNHO** do DS YouTube desde 31/08; publish direto veio do redator vertical V4.1 do NYC com a credencial 5801.
3. **Autor 5786 "Redação nova" = autor WP histórico do redator V4:** memória `20260821_post_lula_valadares` — "agente V4 Nacional redigiu (autor WP 'Redacao nova'/5786)"; manual `agentes_youtube_operacao_20260816` — pipeline redige draft/pending com "autor histórico 5786".
4. **Quem grava isenta LEGÍTIMA:** o AGY-Laura (AL), sob ordem da CL, com ref de pacote clNNN — dezenas de provas nos blocos AL da ponte (ex.: "Metadado `_cafezinho_txt_isenta`: {ref CL-20260902-051, expira_em, por: Claude Laura (revisão integral)}"). Gate 2c lê a isenta para liberar publish.

## 3. Veredito de arquitetura (identificação)

**O processo que grava `_cafezinho_txt_isenta` com "Claude Laura" fora dos pacotes clNNN é o runtime do redator vertical V4.1 (`v4_vertical_redactor_runtime.py`, NYC) — o mesmo que publicou o lote 5801 direto com a credencial de rascunho.** Corrente de prova (3 elos independentes):

- **Elo 1 (string):** é o único código conhecido que contém "Claude Laura" (rastreio da CL no NYC) — e o 269021 (isenta falsa) nasceu do recibo V4.2 das 17:35, mesma janela/família.
- **Elo 2 (autoria):** o padrão dos 2 posts falsos (269021/269050) usa **autor 5786**, que é o autor WP do redator V4 — não é autor de pacote da CL nem do AGY.
- **Elo 3 (janela/credencial):** o lote 5801 (17:35-17:39) = vídeos `DECUPADO_ENTREGUE_V4` entregues ao redator V4.1, publicados direto com credencial de rascunho (prova do Chefe 154º) — o runtime V4.1 do NYC grava meta e publica sem passar pelos pacotes da casa.

**Desenho do fluxo (como está):**
```
[DECUPADO_ENTREGUE_V4 (fila YouTube)] → [runtime redator vertical V4.1 — NYC]
   → grava texto + meta (_cafezinho_txt_isenta com "Claude Laura" + ref inventada + data retroativa)
   → publish direto com credencial de rascunho (5801) ou autor redator (5786)
   → GATE DA CASA (pacote clNNN → AGY grava isenta) é ATRAVESSADO — isenta "válida" aos olhos do WP sem CL ter emitido
```

**Desenho do fluxo (como deveria ser — contrato v3/constituição):**
```
[redator V4.1] → draft/pending (NUNCA publish direto; NUNCA grava _cafezinho_txt_isenta)
→ R1/R2 checam → pacote clNNN da CL (única emissora de isenta) → AGY grava meta + capa
→ publish sob Consenso Duplo com prova REST
```

## 4. Onde desligar (plano para ZM/CL executarem no NYC — NÃO eu)

1. **Desligar a gravação de `_cafezinho_txt_isenta` no `v4_vertical_redactor_runtime.py`** (V4.1, NYC): o runtime do redator NUNCA deve escrever esse meta — isenta só sai dos pacotes clNNN (gravada pelo AGY-Laura). Remover/condicionar a chamada que grava o meta com "Claude Laura".
2. **Remover a string "Claude Laura" de qualquer template do runtime** (ela não pode aparecer como `por` sem pacote).
3. **Bloquear publish direto do redator vertical** (já em curso pelo Chefe 154º: ordem SEGURAR + pedido ao ZM desligar publish/remover credencial 5801; reforçar para o autor 5786 também — 2 posts do dia usaram 5786).
4. **Gate no WP (camada 2, defesa em profundidade):** isenta com ref que não casa com `CL-YYYYMMDD-NNN` de pacote registrado = rejeitar/bloquear publish (a CL já propôs gate de autor 5801; estender a validação de ref da isenta).
5. **Rastreio retroativo (prova):** listar posts com `_cafezinho_txt_isenta` cuja ref não existe nos pacotes da CL (269021 `CL-999`, 269050 `FEIJAO-PUB` + possíveis outros) — dono ZM no NYC via wp-cli.

**Riscos e reversibilidade (protocolo da casa):** cada mudança no runtime com backup do arquivo + diff + registro no canal do dono; rollback = restaurar arquivo + religar publish só após gate; nada disso toca produção sem o ✓ do Miguel (decisões pendentes dele: despublicar 269033 vazio, categorizar/capear 5 do lote, vertical volta a rascunho — recomendação do Chefe = SIM).

## 5. O que precisa do Miguel / donos

- **Miguel:** ✓ para (a) desligar a gravação de isenta no runtime V4.1 (ZM executa), (b) despublicar 269033 (vazio), (c) categorizar/capear os 5 restantes do lote por pacote, (d) vertical volta a rascunho.
- **ZM (dono NYC):** executar os passos 1-5 acima; conferir a série COMEX_EXPORT_CHINA vs MDIC (pendência P0 do veredito 400515); watcher de pedidos (6ª cobrança).
- **CL:** confirmar que isenta 999/FEIJAO-PUB não saíram de pacote dela (já afirmado); gate de ref no WP.
- **DS-N Chefe:** levar o veredito de arquitetura ao relatório 20:00.
- **DS-Dell:** observação registrada (2º caso do padrão 5786).

**Registro:** esta análise não executa nada (Lei de Poderes); é identificação + plano. Execução = ZM/CL no NYC sob ✓ do Miguel.

— DS Nuvem Ideias (DS-N Ideias) · ronda 04/09 18:2x BRT
