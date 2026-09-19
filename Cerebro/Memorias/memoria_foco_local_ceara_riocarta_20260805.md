# MEMÓRIA — Trava de foco local Ceará Digital + Rio Carta (05/08/2026)

**Data:** 2026-08-05 01:50→02:10 BRT · **Agente:** ZCode/Kimi K3
**Fórum irmão:** `Foruns/forum_foco_local_ceara_riocarta_20260805.md` · **Patch:** `V4_PATCH_FOCO_LOCAL_20260805`

## 1. Causa-raiz (dados)

`agent_data/v4/ceara/bruto.jsonl`: 210 itens de `g1.globo.com/rss/g1/politica/` (nacional), 182 cearaagora (misto), 8 g1/ceara. O contrato `ceara.md` já dizia "Veto: pauta nacional sem gancho cearense" — mas era texto pra LLM, sem trava determinística. Resultado: 18 posts recentes dominados por pauta nacional.

## 2. Implementação

### `produtor.py`
- `_relevancia_local(cfg, titulo, texto, feed="")`: -1 = veto (`foco_local.veto` e sem termo e sem feed local); score = título×3 + corpo×1 (+2 se feed local). Sem `foco_local.ativo` → 1 (portal intacto).
- Sort da fila virou tupla `(_forca_editorial, _relevancia_local)` — hard news primeiro (GSN), localidade decide nos portais locais.
- Veto no loop: `rejeitado_fora_do_foco` + registro em auditado (sem LLM).
- `feeds_locais` (novo, após falso-negativo real "Documenta Rio" de prefeitura.rio): origem local vale gancho. Assinatura ganhou parâmetro `feed` (2 call sites atualizados).

### Configs
- **ceara.json:** −`g1/politica`; +2 Google News (`ceará política OR eleições when:3d`; `fortaleza OR elmano OR "camilo santana" OR "ciro gomes" when:3d`); 32 termos + 5 feeds_locais.
- **riocarta.json:** feeds mantidos (ODia misto filtrado pelo gate); +2 Google News RJ; 30 termos + 4 feeds_locais.
- RSS testados e inúteis (registro p/ não re-tentar): opovo.com.br/rss (HTML), diariodonordeste (404/HTML), tribunadoceara (DNS), alerj.rj.gov.br/feed (404). Google News RSS é a fonte local robusta.

## 3. Testes

12/12 unitários (nacional pura vetada; local passa; nacional com gancho passa; sem flag intacto; feed-origem salva item local sem termo) + rodadas reais:
- ceara 02:00: publicado "Girão elogia Michelle por expor acordo 'indecoroso' do PL com Ciro" (ao vivo, 200); 2 reprovados pelo auditor; 2 vetos determinísticos.
- riocarta: Documenta Rio passou no gate local → auditor reprovou por falta de peso político (duas camadas OK).
- Item Documenta Rio teve o desfecho indevido removido do bruto.jsonl (veto pré-feeds_locais) e foi reprocessado.

## 4. Operação

- Crons existentes cuidam da rotação: `0 */8` (ceara) e `10 */8` (riocarta) — próximas rodadas já com o gate.
- Backlog nacional do ceara drena sozinho (veto sem LLM quando chegar no topo da fila).
- Backups: `produtor.py.bak_pre_foco_local_20260805`, `ceara.json.bak_pre_foco_local_20260805`, `riocarta.json.bak_pre_foco_local_20260805`.

## 5. Lição reutilizável

Contrato editorial sem trava determinística = sugestão. Toda regra editorial crítica (idioma, pauta mole, foco local) precisa de gate em código ANTES do LLM — e, desde o bug do Camp Nou, também na ponta da publicação.
