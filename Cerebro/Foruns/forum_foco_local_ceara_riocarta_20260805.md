# FÓRUM — Ceará Digital e Rio Carta: trava de foco local (fim da pauta nacional) (05/08/2026)

**Data:** 2026-08-05 ~01:50-02:10 BRT · **Agente:** ZCode/Kimi K3 · **Gatilho:** Miguel (chat): "O Ceará Digital não está botando coisa do Ceará, está botando coisa do Brasil. O Ceará está pegando fogo e você não está colocando nada. O foco é política no Ceará Digital. Assim como o Rio Carta também."

## 1. Diagnóstico

- Banco bruto do ceara: **210 itens do G1 Política (nacional) vs 8 do G1 Ceará** — o feed nacional inundava a fila; nada no código vetava pauta sem gancho cearense (o contrato já mandava: "Veto: pauta nacional sem gancho cearense" — mas não havia trava).
- Últimos 18 posts: maioria nacional (IBGE, CNJ/Fachin, convenção PT ×3, PCB-SP, Bolsa Família…), poucos com recorte CE.
- RSS local puro é escasso no Ceará (O Povo/Diário/Tribuna sem RSS utilizável) → adotado **Google News RSS com queries locais** (testado, funciona com feedparser).

## 2. O que foi feito (`V4_PATCH_FOCO_LOCAL_20260805`)

1. **`produtor.py` — gate determinístico `_relevancia_local()`** (opt-in `editorial.foco_local.ativo`, demais portais intactos):
   - **veto:** título+corpo sem NENHUM termo local E feed de origem não-local → `rejeitado_fora_do_foco` (sem gastar LLM);
   - **score:** termos locais no título ×3, corpo ×1 → desempate da fila (pauta da terra primeiro);
   - **feed-origem como gancho:** itens de `feeds_locais` (G1-CE/RJ, prefeitura, queries GN locais) contam como locais mesmo sem o termo no texto (caso real: "Documenta Rio" vindo de prefeitura.rio).
2. **ceara.json:** removido `g1/politica` (nacional); adicionados 2 Google News locais (`ceará política OR eleições when:3d`; `fortaleza OR elmano OR "camilo santana" OR "ciro gomes" when:3d`); `foco_local` com 32 termos (cidades, lideranças, instituições CE).
3. **riocarta.json:** mantidos feeds (ODia é misto — o gate filtra); adicionados 2 Google News RJ; `foco_local` com 30 termos.
4. **Backups:** `produtor.py.bak_pre_foco_local_20260805`, `ceara.json.bak_…`, `riocarta.json.bak_…`.

## 3. Validação (12/12 testes + 2 rodadas reais)

- Unitários: nacional pura (Lula/IBGE/STF/PL) vetada; local (Quaest CE, ALERJ) aprovada; **nacional COM gancho local passa** ("Lula destaca Camilo, Cid e Elmano"); GSN intacto; Documenta Rio salvo pelo feed-origem.
- **Rodada real ceara (02:00):** publicou "Girão elogia Michelle por expor acordo 'indecoroso' do PL com Ciro" (gancho Ciro, 200 ✅ ao vivo); auditor reprovou 2 (fact-check + nacional sem recorte); 2 vetadas determinísticas. Banco nacional começou a drenar sem custo de LLM.
- **Rodada real riocarta:** Documenta Rio passou no gate local e o **auditor reprovou** ("institucional sem gancho político-eleitoral") — as duas camadas funcionando como projetado: gate garante local, auditor garante peso político.

## 4. Pendências

- Backlog nacional antigo no banco do ceara (~200 itens) vai sendo vetado a cada rodada (sem custo); se preferir faxina imediata, dá para marcar em lote.
- Lembrete agendado (08:47 BRT hoje, automation-485cf85f): **Agente YouTube no Ceará Digital** (podcasts cearenses) — pedido do Miguel neste chat.
- Se o volume de posts/dia cair demais (filtro rigoroso), avaliar mais queries GN locais (interior do Ceará, Câmara de Fortaleza etc.).

**Memória técnica:** `Memorias/memoria_foco_local_ceara_riocarta_20260805.md`
