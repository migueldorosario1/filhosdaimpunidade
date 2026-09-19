# MEMÓRIA — GSN: post PT/ES Camp Nou no ar (02/08) + gate no publicador (05/08/2026)

**Data:** 2026-08-05 00:30→01:10 BRT · **Agente:** ZCode/Kimi K3 · **Gatilho:** Miguel: "materia em espanhol no gsn. tem que ser em ingles sempre" — URL `globalsouth.news/blog/20260802-tragedia-no-camp-nou-obrero-muere-durante-reconstrucao-do-es/`
**Fórum irmão:** `Foruns/forum_gsn_pt_campnou_publicador_gate_20260805.md` · **Bug:** `BUG-20260802-1323-GSN-PT-PUBLICADOR-SEM-GATE`

## 1. Rastreio da origem (como o post foi parar no ar)

1. DNS `globalsouth.news` → Vercel (76.76.21.21) — mas o post **NÃO** estava no repo `migueldorosario1/global-south-news` (repo Astro antigo, alimentado pelo cron NYC desligado em 23/07).
2. Site real = projeto Vercel **globalsouth-v4** ← repo `git@github.com:migueldorosario1/globalsouth-v4.git` ← checkout local `Projeto Cafezinho Agentes/sites-v4/globalsouth` (campo `repository.local_path` do `agent_data/configs/globalsouth.json`).
3. Post estava lá: commit `b575fd3` por "Refatoracao V4" em **02/08 13:23:43 -0300** = rodada das **13:00 BRT** do cron local (`orquestrador.py --all`, `agentes_tematicos/v4/`).
4. `bruto.jsonl`: item coletado do feed `aljazeera.com/xml/rss/all.xml` em **25/07 16:59 UTC** (`titulo_fonte`: "Worker dies during reconstruction of Barcelona's Camp Nou Stadium", URL seção `/sports/`), marcado `processado` 25/07 17:04 — **4 dias antes dos gates de 29/07**.
5. `auditado.jsonl`: registro `aprovado` com corpo PT completo; desfecho `publicado` só em 02/08 16:23 UTC → **o item dormiu 8 dias na fila de aprovados** e o `publicador.py` o soltou sem revalidar nada.

## 2. Prova de que o gate de 29/07 funciona (e por que falhou aqui)

- `_parece_portugues()` sobre título+corpo reais do post: **5 hits** (`de acordo com`, `não`, `foram`, `enquanto` ×2) → DETECTADO. Se o item passasse pelo produtor pós-29/07, seria `rejeitado_idioma`.
- Falha: o gate mora só no produtor. `publicador.py` lia `aprovados_pendentes()` e publicava FIFO (2/rodada) sem nenhuma revalidação — herança da arquitetura "confia na fila".
- Agravante editorial: o veto de pauta mole é por **título-fonte**; "Worker dies during reconstruction of Barcelona's Camp Nou Stadium" não contém nenhum keyword (football/soccer/stadium ausentes) → mesmo pós-gate, poderia ser produzido.

## 3. Cura executada (05/08 00:40→01:05 BRT)

### 3.1 Conteúdo
| Ação | Detalhe |
|---|---|
| Camp Nou derrubado | `git rm` post + hero → commit `4dc1074` → push → **404 confirmado** (homepage limpa) |
| Níger PT derrubado | `20260730-advogados-exigem-…` (2º post PT achado na varredura dos 105 posts do repo) → 404 |
| Níger republicado EN | `20260730-lawyers-demand-release-of-ousted-niger-president-bazoum.md`, hero renomeada p/ slug EN, tags EN, link inline p/ fonte africanews; commit `ed6228a` → **200 confirmado** |
| Banco consistente | registros `aprovado`+`publicado` do item EN (`uid lawyers-demand-release-of-ousted-niger-president-bazoum`) p/ dedup |

### 3.2 Estrutural — `V4_PATCH_GSN_EN_PUBLICADOR_20260805`
Backups: `produtor.py.bak_pre_gsn_en_publicador_gate_20260805` · `publicador.py.bak_…` · `globalsouth.json.bak_…`

- **`produtor.py`:** nova constante `_URL_VETO_ESPORTE = ("/sports/", "/sport/")`; veto determinístico estendido — `hard_geopolitics` + URL-fonte de seção esportiva → `rejeitado_pauta_mole` (sem gastar LLM).
- **`publicador.py`:** nova função `_veto_publicacao(cfg, artigo)` chamada no topo do loop de `rodar()` (antes de hero/LLM): idioma PT em site EN → `rejeitado_idioma` (qualquer site EN, paridade com produtor); título mole OU URL `/sports/` com flag → `rejeitado_pauta_mole`. Vetado recebe desfecho via `banco.marcar_auditado()` e sai da fila para sempre.
- **Config GSN:** `soft_veto_keywords` += `camp nou`, `real madrid`, `boxing` ("barcelona" sozinho propositalmente fora — risco de falso-positivo geopolítico).
- **Purga da fila:** 5 itens moles pré-gate (Lagos boxing, Sidi Bou Said UNESCO, Mount Olympus UNESCO, Real Madrid, antílopes UNESCO) receberam desfecho com motivo "purga manual da fila legada pré-gate". Fila: 36 → 31.

### 3.3 Testes (7/7 + simulação)
1. Post real Camp Nou → `idioma` ✅ · 2. EN de /sports/ → `pauta_mole` ✅ · 3. Hard news EN (Irã/Hormuz) → liberado ✅ · 4. PT em railpost (EN sem flag) → `idioma` ✅ · 5. /sports/ em railpost sem flag → liberado (intacto) ✅ · 6. PT-BR (ceará) → intacto ✅ · 7. Real Madrid → `pauta_mole` ✅. Simulação fila real: 36 → 5 vetados / 31 liberados.

## 4. Estado final verificado (01:05 BRT)
- Camp Nou PT: **404** · Níger PT: **404** · Níger EN: **200** · Varredura repo: 105 posts, **0 em PT/ES** restantes.
- Crons 03:00/13:00 BRT seguem ativos com gates nas DUAS pontas.

## 5. Lições / pendências
- **Lição estrutural (reutilizável):** gate de esteira precisa nascer nas duas pontas (produção E publicação); fila intermediária é zona cega — qualquer item legado herda a confiança do passado.
- **Padrão reutilizável:** veto por **URL de seção** (`/sports/`) complementa veto por título — pega o que keyword não pega.
- Pendente: fila legada EN (31) tem human-interest borderline (Betye Saar, Kinshasa art) — sem veto determinístico; faxina maior só com ordem do Miguel.
- Pendente (29/07, mantida): posts moles antigos já publicados seguem no ar (indexados).
