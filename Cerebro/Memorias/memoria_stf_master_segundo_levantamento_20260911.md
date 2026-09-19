# Memória — Caso Master STF: 2º levantamento de sigilo (11/09 noite) — log técnico completo

**Sessão:** ZCode GLM-5.3 (Dell), 11/09 22:24→23:1x BRT. Par do fórum `Foruns/forum_stf_master_segundo_levantamento_20260911.md`.

## Arquivos/diretórios

- **Destino (novo):** `Outros/pautas editoriais o cafezinho/Reportagens/Master/` — 26 subdiretórios `CLASSE_NUMERO`, 554 PDFs/RTFs, 178MB. `INDICE.md` (mapa completo com frentes e incidentes), `LEIA-ME_coleta_20260911_manha.md` (da coleta 1), `RELATORIO_INVESTIGACAO_PROFUNDA_20260911.md`, `resumo_coleta.json`, `extra/inq4781_relatorios_pf_poder360.pdf` (7,6MB).
- **Origem movida:** `Outros/pautas editoriais o cafezinho/Dia a dia/2026 Set 11/pet_16662_15556_stf/` → esvaziada (321 arquivos movidos com mv atômico, mesmas partições; renomeados PET_15556/PET_16662/INQ_5026...RCL_88121).
- **Scratch da sessão:** `~/ZCodeProject/scratch/stf_111_noite/` — `coleta.sh` + `parse_pecas.py` (coletores reutilizáveis), `novos/` (cópias das coletas novas), jars de debug, HTMLs das abas, `pecas_16704/` (8 peças de 11/09 da PET 16.704: resposta a Fachin id 15390356345 294KB etc.).

## O que foi coletado (grupo 2 — 10 processos, ~235 peças novas)

INQ 4.995 (inc 7268513, 74 peças/27MB — inquérito Dark Horse do Flávio) · PET 16.292 (7629247, 6) · PET 16.369 (7642290, 5) · PET 16.346 (7639419, 8 — Miranda) · PET 15.674 (7529999, 13 — Ciro) · PET 15.873 (7559421, 67 — Ciro cautelares/PEC 65 FGC) · PET 15.676 (7530185, 28 — Castro/RioPrevidência) · PET 16.229 (7619743, 21 — Wagner) · INQ 5.050 (7600724, 7) · INQ 5.070 (7661993, 6 — financiamento Dark Horse/Karina Gama).

## Receita técnica (atualiza a memória stf-portal-pecas-cookie-jar-receita-20260911)

1. **403 para curl puro** (novo desde 11/09 noite): obrigatório UA de navegador completo.
2. Abas AJAX: `X-Requested-With: XMLHttpRequest` + path **com `.asp`** + cookie jar FRESCO por incidente: `curl home → detalhe → aba` com pausas 2-3s (AWSALB gruda em backend ruim; regenerar jar = trocar backend). Resposta 54.429 bytes = página genérica (abortar e tentar de novo).
3. `listarProcessos.asp?classe=Pet&numeroProcesso=N` resolve Pet; **para INQ usar classe=Inq (capitalizada)** — `INQ` maiúsculo devolve genérica (descoberto nos 5.050/5.070).
4. **`--connect-timeout 15 --max-time 90` em TODO curl** — sem isso o portal aceita conexão e não responde, travando o coletor por horas (caso real: peça 15387102602 pendurada 50min).
5. Peças vazias após retry = conteúdo sob ressalva de sigilo (`_vazias.txt` por processo).
6. Identificação dos números: despachos públicos citam correlatos (12/07 na 15.556 lista 16.292/16.078/16.063/16.059); imprensa (Congresso em Foco) lista frentes; sigilo checado via `'Público' == "Sigiloso"` no JS do detalhe.

## Provas

- Contagem final por processo no INDICE.md (554 peças/178MB/26 processos).
- Sigilos checados 22:2x–23:1x: 10 novos 'Público'; 16.078/16.063/16.059/16.669/15.612/16.070/INQ 4.781 'Sigiloso'.
- PET 16.704 às 23:1x: 33 peças, nenhuma pós-19h (despacho dos 18+20 ainda não é peça pública).

## Pendências / próximos passos

1. Despacho integral dos 18+20: re-checar `abaDecisoes.asp?incidente=7687920` (PET 16.704) e DJE de 14/09; com a lista, coletar os ~28 números restantes (10 identificados).
2. Opcional: zip consolidado → mídia WP (mesma receita do pacote_stf_master.zip 79MB do post 269868; Cloudflare cacheia .zip).
3. Uso editorial: material pronto (frente Wagner 16.229 + Castro RioPrevidência 15.676 são as mais ricas inéditas).
