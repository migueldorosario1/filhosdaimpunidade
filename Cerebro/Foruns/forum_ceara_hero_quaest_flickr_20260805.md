# Fórum — Ceará Digital: hero errada da matéria Quaest corrigida + diretriz "imagem casada com o texto" (Flickr)

**Data:** 2026-08-05 ~14:10 BRT
**Agente:** Kimi K3 (ZCode)
**Gatilho Miguel:** "Essa matéria aí está com uma ilustração que não tem nada a ver com a matéria. (…) As imagens têm que ser casadas com o texto. Se tiver nome no texto algum personagem, bota a foto da pessoa — procura no Flickr enquanto o v4 não fica pronto totalmente."

## 1. O problema (confirmado)

- Matéria `20260805-quaest-lula-lidera-cenarios-e-abre-5-pontos-sobre-flavio-bol` (publicada 08:03) saiu com hero do **portão do INPA** (Manaus) — creditada "Wikimedia Commons — União da Juventude Mestiça". Nada a ver com Lula × Flávio Bolsonaro.
- Causa provável: `visual_prompt` com o token "pesquisa(s)" casou no Wikimedia com "Instituto Nacional de **Pesquisas** da Amazônia". Juiz visual deixou passar.
- **Timing:** a matéria saiu ANTES da FASE 0 do Banco de Mídia V4 (plugada hoje ~12:30, ver `forum_rodada_tematicos_banco_midia_20260805.md`) — por isso não puxou as ~99 fotos de Lula do banco.

## 2. A correção (no ar)

- Busca manual no **Flickr** (ordem do Miguel), filtro licenças livres:
  - **Lula**: foto de evento 2025, domínio público (PDM 1.0), autor "J.M Executive" (`/photos/199179160@N02/54038543267/`).
  - **Flávio Bolsonaro**: retrato de entrevista no Senado, **CC BY 2.0**, "Edilson Rodrigues/Agência Senado" (`/photos/agenciasenado/52865271068/`).
- Composto 1200×675 "versus" (Lula | Flávio, divisor branco) montado localmente (PIL).
- Commit `bbd77df` no repo `ceara-v4` → Vercel → **verificado ao vivo** (novo asset 129.162 bytes servindo em `ceara.digital/hero/…flavio-bol.jpg`; backup da hero errada em `/tmp/hero_quaest_backup_inpa.jpg` na sessão).
- `hero_credit` do post atualizado com os dois créditos.

## 3. Diretriz permanente do Miguel (registrada)

> **Imagem casada com o texto.** Se o texto nomeia um personagem, a hero deve ser a foto da pessoa. Enquanto o V4 de imagem não fica pronto totalmente, **procurar no Flickr** (licenças livres / fontes institucionais: Agência Senado CC BY 2.0, governos PDM, contas oficiais).

Estado da automação dessa regra:
- ✅ **FASE 0 do Banco de Mídia V4** (desde hoje ~12:30): retrato auditado de liderança antes do Wikimedia — cobre Lula (99), Bolsonaro, Milei, Trump etc. Matcher por entidade/token forte no título.
- ✅ **Esteira anti-reuso + juiz visual + padronização** já existentes.
- 🟡 **Gap:** personagens cearenses (Elmano, Camilo, Ciro, Luizianne, Capitão Wagner) ainda **não têm fotos no banco** (verificado: 0 ocorrências de "elmano/camilo/ciro" no `index.json`). Ampliação do Banco Ouro com lideranças do Ceará = próxima melhoria natural; Flickr supre manualmente até lá.

## 4. Painel do Ceará Digital (pedido do Miguel: "me dá o endereço do painel de novo")

- **Central do Temático:** `http://43.156.151.165/v6/tematicos/ceara-digital` (GA4 property 546675232; views 30d/7d/MM7).
- Custos/LLMs: `http://43.156.151.165/v6/custos`.
- ⚠️ O slug curto `/v6/tematicos/ceara` retorna "Temático não encontrado" — o canônico é **ceara-digital**.

## 5. Sobre "o site está desatualizado, não traz novidade da política cearense"

Fatos verificados nesta sessão (não é percepção, é dado):
- Pipeline V4 roda `0 */8 * * *` (cron local, `orquestrador.py --site ceara`) + rodadas gerais 3h/13h.
- Posts/dia: 03/08 **10**, 04/08 **7**, 05/08 **4** (até 13h) — todos os 25 últimos com gancho Ceará.
- Veto de foco local **ativo e funcionando**: rejeitou hoje "Raio mata jogador na Tailândia" e "Menina presa em brinquedo" (fora do escopo).
- Pontos de atenção reais: (a) algumas matérias nacionais entram com parágrafo-gancho Ceará mecânico ("hepatites virais", "produção industrial IBGE") — qualidade do gancho, não frequência; (b) destaques da home giram por GA4 desde hoje 01:26 (não congelam mais).
- Pipeline antigo do ceara no NYC (cron 9:15 → repo fora do ar) **segue rodando à toa** — candidato a desligamento, pendente ordem do Miguel (registrado no fórum GA4 §5).

## 6. Referências cruzadas

- `Foruns/forum_rodada_tematicos_banco_midia_20260805.md` — FASE 0 Banco de Mídia (por que as próximas matérias já saem com foto da pessoa).
- `Foruns/forum_tematicos_destaques_ga4_20260805.md` — destaques por audiência + hero 404 corrigida mais cedo hoje.
- Memória técnica desta sessão: `Memorias/memoria_ceara_hero_quaest_flickr_20260805.md`.

## 7. FOLLOW-UP (mesmo dia ~19:40 BRT) — BANCO COM 8/8 CANDIDATOS CEARENSES

**Ordem Miguel:** "Vai no Flickr agora e começa a juntar foto dos candidatos do Ceará ao Senado e ao governo. Junta lá agora."

- Levantamento da cobertura no Banco de Mídia V4: Elmano (4 fotos, Agência Brasil), Luizianne (6) e Ciro (6) já tinham entrado mais cedo hoje por outra frente; **faltavam Cid, Girão, Capitão Wagner e André Fernandes (0 fotos cada)**.
- **Ingeridas 6 fotos nesta sessão** (revisão visual 1 a 1 + licença confirmada na página):
  - **Cid Gomes** — retrato oficial Senado (Rodrigo Viana/Agência Senado, CC BY 2.0) — *1ª foto dele no banco*;
  - **Girão** — retrato oficial Senado (Rodrigo Viana/Agência Senado, CC BY 2.0) — *1ª foto dele no banco*; entidade cadastrada como "Girão" (casa com "Girão" e "Eduardo Girão" em manchete);
  - **Capitão Wagner** — tribuna da Câmara (Michel Jesus/Câmara dos Deputados, CC BY 3.0, via Wikimedia) — *1ª foto dele no banco*;
  - **André Fernandes** — tribuna da Câmara (Câmara dos Deputados, CC BY 3.0, via Wikimedia) — *1ª foto dele no banco*;
  - **Camilo Santana** — retrato oficial Senado 2023 (CC BY 2.0) — reforço (banco já tinha 4);
  - **Ciro Gomes** — discursando UFABC (Murilo Silva/CAPOL, CC BY 2.0) — reforço.
- **Ingestão:** direto no Banco Ouro NYC (`midia_ouro`, R2 `ouro/politica/<slug>/`, 743→749 rows) + espelho local `agent_data/v4/banco_midia/` atualizado na mão (755 itens) — o sync semanal (seg 06:20) replica idêntico (mesmo padrão de nome `ouro_<hash16>`). Script: `/tmp/ceara_fotos_ingest/ingest_nyc.py` no NYC (sessão).
- **Matcher testado com 8 manchetes reais → 8/8 nomes cobertos.** Detalhe: "Ciro" sozinho (4 chars) não casa — entidade é "Ciro Gomes"; "cid" idem — entidade "Cid Gomes".
- **Licenças rejeitadas na varredura:** conta oficial do Elmano (`elmano13dopt`) e do Ciro (`sitecirogomes`) são "todos os direitos reservados" — fora da política da casa (CC/PD only). CPMI Fake News (Agência Senado) aparece em busca de "Luizianne" mas ela NÃO estava no Congresso em 2019 — falso positivo perigoso, descartado.
- Gaps que restam: fotos de eventos recentes de campanha 2026 (convenções, comícios) — fonte futura: Flickr governo do Ceará/PT-CE se licenciarem, ou Wikimedia.
