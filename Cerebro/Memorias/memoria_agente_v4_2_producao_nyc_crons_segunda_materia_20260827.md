---
tema: Agente V4.2 Economia/Estatística — migração de produção para o NYC (crons ligados) + fixes de coleta + Argentina resolvida + 2ª matéria (post 400158)
data: 2026-08-27
agente: ZCode/GLM-5.3
forum_irmao: Foruns/forum_agente_v4_2_economia_estatistica_20260825.md
---

# Memória — V4.2 em produção no NYC (27/08/2026)

## Missão (prompt do Adendo 27/08 colado pelo Miguel ~14h)
Empacotar o agente para o servidor (produção-zero-no-Dell), ligar os crons (coletor 2×/dia, ingestor */15, ciclo 1×/dia), produzir a 2ª matéria (Fed×BCB) e cuidar das pendências.

## Casa definitiva: NYC
- Pacote: `/root/v4_labs/codigo/agente_economia/` (rsync do Dell; `media_vision_providers.py` do NYC atualizado para a versão homologada — md5 `284e2ed5`; matplotlib 3.11.1 no `/root/venv`).
- Logs: `/root/agent_data/v42_{coletor,comex,ingestor,ciclo}.log` · lockfiles `/tmp/v42_*.lock`.
- Backup crontab: `/root/agent_data/backup_crontab_pre_v42_20260827.txt`.

## Crons (crontab root NYC; BRT = UTC−3)
```cron
0 10,20 * * *  coletor_economia_v4.py          # 07:00/17:00 BRT
10 10,20 * * * coletor_comercio_exterior_v4.py # 07:10/17:10 BRT
*/15 * * * *   ingestor_estatistico.py
10 15 * * *    ciclo_v42.py --tema auto --publicar  # 12:10 BRT — 1ª automática 28/08
```
Kill switch: `crontab -l | grep -v agente_economia | crontab -`

## Credenciais (Regra 4)
- `ESPELHO_WP_USER/SITE/PASS` Dell→NYC (sha8 linhas c14aeb98 confere; backup `.bak_pre_v42_20260827`).
- `DEEPSEEK_API_KEY` NYC TROCADA (401→200; resolve pendência §118; backup `.bak_pre_dskey_20260827`).
- Gemini geo-bloqueado no IP NYC (400 FAILED_PRECONDITION) — cascata efetiva lá: DeepSeek→OpenAI (texto) e Qwen-VL (visão).

## Bugs achados e corrigidos (Dell⇄NYC sincronizados)
1. **FRED com valor FALSO no banco primário**: `coletor_economia_v4.py` lia `FRED_API_KEY` no import (antes de qualquer `carregar_env`) → cofre nunca carregado → fallback gravava FEDFUNDS 5,25% (real jul/2026: 3,63%). Fix: `carregar_env()` no módulo + chave lida dentro de `coletar_fred()` + limit 24. Expurgados do banco: 1 fallback + 12 pontos futuros.
2. **Selic com datas FUTURAS**: SGS publica meta agendada (09/2026) e `ultimos/N` as trazia. Fix: janela `dataInicial=hoje-95d&dataFinal=hoje` p/ diárias + filtro universal `data <= hoje`. Selic agora 96 pts reais até 27/08.
3. `DEFAULT_DB_PATH` hardcoded no caminho do Dell criava banco espúrio `/root/Downloads/...` no NYC → agora relativo ao pacote (env `BANCO_ESTATISTICO_PATH` continua valendo).
4. `ingestor.executar_varredura()` sem `self` (o "método suspeito" do Módulo C) — corrigido; cron */15 exige.
5. URL INDEC: `/series/api` (404) → `/series/api/series/` (validada ao vivo).
6. CSV legado GACC dentro do pacote (`raw/legado/`, fallback do caminho antigo).
7. Gráfico Selic `limit=60` (24 pts diários = 1 mês → eixo X "ago/26" 6×).
8. `auditor_graficos_v4`: `provider_id` registrado APÓS o analyze (antes rotulava `fallback_media_vision` mesmo com Qwen-VL respondendo — artefato de ordering; prova: re-audit mostrou `qwen_dashscope`, state approved, watermark true).

## Argentina (pendência SISCOMES) — RESOLVIDA
"SISCOMES" era equívoco (SISCOMEX é brasileiro). Via correta: **API de Séries de Tiempo `apis.datos.gob.ar`** (dataset "Intercambio Comercial Argentino"). IDs mensais validados (US$ mi, até 2026-06): `74.3_IET_0_M_16` export · `74.3_IIT_0_M_25` import · `74.3_ISC_0_M_19` saldo. Busca de séries: `/series/api/search/?q=`. 72 obs ingeridas.

## Banco NYC (fim da sessão)
**671 obs** — BCB_1 68 (→27/08) · BCB_432 96 (→27/08) · BCB_433 12 (→07/2026) · FEDFUNDS 24 (→07/2026) · CPIAUCSL 23 · PAYEMS · COMEXSTAT 124 · EUROSTAT 36 · GACC legado 150 (→02/2026) · INDEC 72 (→06/2026) · USTRADE.

## 2ª matéria — post 400158 (tese Fed×BCB)
- URL: https://cafezinho.news/2026/08/27/v42-20260827-politica_monetaria_comparada-2/
- Pipeline E2E **no NYC**: DeepSeek aprovou Texto Música na 1ª; gráficos BCB_432+FEDFUNDS approved (mecânica 24/24 + Qwen-VL); 3 passos (draft→carimbo→publish); readback publish/cats/tags/featured/meta/carimbo ✓.
- QA manual: 2 frases/parágrafo (§2–§9); 0 meses sem ano (único alerta era falso positivo "maiores"); visão manual dos PNGs OK; home com 2 matérias V4.2; draft órfão 400155 (fail-closed com provider velho — gate funcionou) deletado.
- EN arquivada: `gerados/gsn/gsn_politica_monetaria_comparada_20260827_*.json` (+ a do Sul-Sul de 26/08).

## Comandos úteis (NYC)
```bash
cd /root/v4_labs/codigo/agente_economia
/root/venv/bin/python3 ciclo_v42.py --tema politica_monetaria_comparada --publicar
tail -f /root/agent_data/v42_ciclo.log
crontab -l | grep agente_economia
```

## Estado / falta / preciso de você
- **Aconteceu:** produção no NYC com crons ligados; banco saneado/ampliado; Argentina resolvida; 2ª matéria no ar; 2 chaves espelhadas (ESPELHO_WP + DeepSeek NYC).
- **Falta:** Beijing offline (GACC até 02/2026 — reativação é projeto à parte); Cesta Premium fase 2 (interlinks+newsletter no `montar_html`); EN no GSN (2 JSONs prontos, aguarda "vai"); acompanhar 1ª execução automática 28/08 12:10 BRT.
- **Preciso de você:** nada bloqueante. Opcional: validar ritmo 1×/dia (kill switch acima), "vai" para EN/GSN, decisão sobre Beijing.

## 🚩 RODADA 2 (27/08 ~14h40→15h BRT) — DIRETRIZ HISTORIAL + CURADORIA DE GRÁFICO + 400158 CORRIGIDO

**Feedback Miguel:** gráfico Selic feio/sem história + matéria elogiando juro alto (PROIBIDO) + siglas técnicas. Ritmo 1×/dia no espelho APROVADO.

**Mudanças (Dell⇄NYC sincronizadas):**
1. SYSTEM_PROMPT regras 8-11: linha CONTRA juro alto (nunca elogiar; efeito benéfico exige custo junto; corte=avanço); siglas SEMPRE por extenso na 1ª menção; linguagem popular. Tese 2 renomeada "O Custo de Carregar os Juros Mais Altos do Mundo".
2. Curadoria: coletor 400d p/ diárias (Selic 401 pts); gráfico Selic limit=260; `_titulo_informativo()` no gerador (título conta o movimento: "cai de 15,00% para 14,00% em 8 meses"; manifesto ganhou `titulo`); auditor com `window_informative` (LLM reprova janela achatada sem história) + allowlist retrocompatível.
3. Post 400158 corrigido IN PLACE (mesma URL): novo título "O impacto dos juros elevados na economia brasileira em 2026"; §§2-7 com 2 frases; rentistas/redução-da-Selic no texto; zero meses sem ano; zero siglas cruas; capa nova 400160 (Selic 12m, audit approved, visão 9/10) + 400161 (Fed); carimbo re-gravado; EN `_DIRETRIZ.json` arquivada.
4. Ferramenta nova: `corrigir_post_v4.py --post-id X --tema Y` (retificação §119 de post publicado).
5. Pegadinha: allowlist estrita do auditor (`set(chart) != {...}`) bloqueou o campo `titulo` novo — fix aceitando conjunto com/sem `titulo`.
6. Refinamento futuro: rotular degraus intermediários (14,75/14,50/14,25).

## ⛔ EMENDA 27/08 ~15h — SELO DE AUTOMAÇÃO PROIBIDO
`SELO_TESTE_PT` removido do publicador (nem no espelho). Posts 400137/400158 limpos IN PLACE (0 menções ao vivo; fontes/gráficos intactos). Tag V4.2 interna permanece.
