---
name: 🚨 BUG CRÍTICO — Recusa LLM disfarçada em JSON pode vazar para publicação (5 camadas falham)
description: 2026-05-02 — Gemini-pro-latest devolveu JSON formal com TÍTULO + HTML de recusa meta-discursiva ("Rascunho apresenta eventos fictícios e não pode ser publicado"). Foi publicado como post 241982 do Cafezinho. TODAS as 5 camadas de auditoria aprovaram — nenhuma detecta meta-discurso. Blindagem deployada via detectar_recusa_llm() em motor_publicador.py.
type: project
originSessionId: 44f2c389-881d-4335-a540-25075ea2110b
---

# 🚨 BUG CRÍTICO — Vazamento de recusa LLM para publicação (incidente 2026-05-02)

> **Importância:** este bug expôs uma falha conceitual em TODAS as 5 camadas de auditoria do `motor_publicador.py`. Pré-incidente, nenhuma delas era capaz de detectar quando um LLM disfarça uma recusa em formato JSON estruturado. Pós-fix, há `detectar_recusa_llm()` no motor — mas o aprendizado vale para **qualquer agente futuro** que parseie output LLM.

## Sintoma observável
Post 241982 do Cafezinho publicado às 10:11:37 BRT 2026-05-02 com:
- **Título:** "Rascunho apresenta eventos fictícios e não pode ser publicado"
- **Conteúdo:** "O rascunho fornecido descreve um conflito que não ocorreu... Recomenda-se descartar o material..."
- Foi parar no portal público até Miguel rebaixar manualmente pra rascunho.

## Causa raiz (entender ANTES de qualquer fix similar)

Gemini-pro-latest, ao receber pauta sobre suposta operação militar EUA contra Irã, **detectou anacronismo internamente** (chanceler iraniano Amir-Abdollahian faleceu maio/2024). Em vez de devolver erro HTTP ou texto livre de recusa, **respeitou o contrato de formato** e devolveu um JSON estruturalmente válido:

```json
{
  "titulo": "Rascunho apresenta eventos fictícios e não pode ser publicado",
  "html": "<p>O rascunho fornecido descreve...</p>...",
  "palavras_chave": "...",
  "categoria": "internacional"
}
```

O `motor_publicador.py` parseou o JSON sem nenhum erro, encontrou `titulo` e `html` válidos, passou pelo `len(html.strip()) >= 100`, e fluiu pra publicação.

## Por que TODAS as 5 camadas falharam

| # | Camada | O que ela faz | Por que não pegou |
|---|---|---|---|
| 1 | Camada Extra (Claude 3.5 Sonnet) — auditoria de furos | procura LACUNAS factuais | conteúdo era coerente — meta-discurso não tem lacunas |
| 2 | Revisão Swarm (grok-4.3 + claude + mistral) | melhora qualidade editorial | assume que o input já é uma matéria |
| 3 | Auditoria Final Elite (claude-sonnet-4-6) | última polida factual/editorial | mesma premissa |
| 4 | **VETO FINAL FACT-CHECKING** | verifica precisão de fatos AFIRMADOS | conteúdo NÃO afirma fato algum, afirma o oposto ("não ocorreu", "não existem registros") — tecnicamente correto, sem fato falso pra contestar |
| 5 | Categorizador rígido | ⚠️ MÓDULO REGRESSO — sumiu do Tencent (`util_categorizador_rigido não encontrado`) | fallback histórico só aceita |

**Lição número 1 (CRÍTICA):** todas as 5 camadas validam fatos/qualidade DENTRO do conteúdo. Nenhuma é capaz de detectar quando o conteúdo INTEIRO é meta-discurso sobre o rascunho. **É um gap conceitual, não bug pontual.**

**Lição número 2:** fact-checking com viés de "não reprovar a menos que tenha CERTEZA de erro factual" é correto editorialmente, mas tem ponto cego óbvio: matérias que afirmam o oposto de fatos não têm fato a falsear. Texto "não há guerra" passa em fact-check porque é VERDADE — mas como matéria de jornal, é absurdo.

## Fix deployado 2026-05-02 12:14 BRT

`detectar_recusa_llm(titulo, html)` em `motor_publicador.py` (linha 444), com hook após `html = data.get("html", "")` (linha 1130). MD5 `0feb4cc0f4ad3a29bfaaa030a7c14068`. Backup `/root/motor_publicador.py.bkp_pre_blindagem_recusa_20260502_1214`.

### Sentinelas (case+accent insensitive, normalizadas via NFKD)

**TÍTULO** — qualquer 1 → rejeição:
- Composições com "rascunho" (evita falso positivo "Rascunho do governo prevê..."): `rascunho apresenta`, `rascunho fornecido`, `rascunho descreve`, `rascunho contem`, `rascunho nao pode`, `este rascunho`
- `ficticio/ficticia/ficticios/ficticias`
- `nao pode ser publicado`, `nao pode ser publicada`
- `nao posso publicar/confirmar/escrever/ajudar/atender`, `nao consigo gerar`
- `como modelo de linguagem`, `como uma ia`, `sou um modelo`, `sou uma ia`
- `desculpe nao posso`, `infelizmente nao posso`
- `i cannot`, `i can't`, `i'm sorry`, `i am sorry`, `i am unable`

**HTML** — 2+ sentinelas → rejeição:
- `rascunho fornecido`, `texto fornecido`, `material fornecido`
- `eventos descritos sao ficticios`, `eventos descritos nao ocorreram`, `eventos descritos sao inteiramente ficticios`
- `nao existem registros`, `qualquer versao final deve`
- `recomenda-se descartar`, `fontes primarias autenticas`
- `evitar a disseminacao`, `informacoes incorretas`, `rigor para nao confundir`
- `como modelo de linguagem`, `sou um modelo de`, `sou uma ia`
- `i cannot help`, `i can't help`, `i'm not able to`

## Como aplicar a outros agentes (forte recomendação)

Qualquer agente que parseie JSON de saída LLM e use `data.get("titulo")` + `data.get("html")` — ou equivalente — **DEVE** importar e usar `detectar_recusa_llm()` ANTES da publicação. Agentes a auditar/blindar prioritariamente:

- `agente_master_lula.py` (já tem fact-check duplo, mas mesmo gap conceitual)
- `agente_china.py` (auditoria LLM batch tem fail-closed agora, mas se o LLM passar com recusa em formato veredito ainda vaza)
- `agente_master_nacional.py`, `agente_master_trends.py`
- Todos os temáticos premium (`agente_ia.py`, `agente_inflacao.py`, `agente_matriz_energetica.py`, etc) que usam `publicador_tematicos.chamar_llm`

Forma sugerida: importar `from motor_publicador import detectar_recusa_llm` e chamar antes do `publicar_wp`/`publish`.

## Pendências paralelas observadas (a investigar em sprint dedicada)

1. **`util_categorizador_rigido.py` SUMIU do Tencent.** Log mostra `⚠️ util_categorizador_rigido não encontrado — usando validação antiga`. Esse módulo entrou em 25/04 e reduziu misclassifications (política caiu 21→6, ciência subiu 5→25). Regressão crítica.

2. **`strip_html` ainda vaza em outro fluxo.** Fix de 01/05 cobriu `normalizar_titulo`, mas log do incidente mostra `[10:11:47] Erro lendo banco json: name 'strip_html' is not defined`. Há outra chamada residual.

## Heurística geral (anote como princípio de design futuro)

> **TODA camada de validação que assume "o input é uma matéria" tem ponto cego pra meta-discurso de recusa.** O fix correto não é outra camada de auditoria — é uma blindagem ANTES das auditorias, que detecta sinais de meta-discurso (sentinelas explícitas no título e no conteúdo). A nova camada deve assumir que o LLM pode estar mentindo sobre o que ele está fazendo, não sobre o que é o mundo.

## Ver também
- Fórum: `Foruns/forum_erro_grave_portal.md`
- CLAUDE.md ADENDO 7 (2026-05-02 11:58 BRT — Antigravity sinalizou)
- Memória relacionada: `manual_de_bugs_ler_primeiro.md`
- Sprint paralela do dia: `project_forca_tarefa_bugs_imports_20260501.md`

---

## ✅ Refinamento v2 deployado 2026-05-02 12:31 BRT

### Conflito de pareceres entre consultores resolvido por complementaridade

- **Antigravity §5:** apontou FP determinístico de `ficticio/ficticia` puros no TÍTULO (jornalismo cultural/bélico), propôs guardrails Gemini/Grok adicionais.
- **Codex 12:20 BRT:** aprovou v1, alertou contra expansão sem evidência observada.

**Resolução aplicada (Claude Code líder técnico):**
- Aceito Antigravity sobre FP `ficticio` (era falso positivo determinístico, não expansão especulativa)
- Aceito Codex sobre guardrails Gemini/Grok (aguardar evidência observada em produção)

### Mudanças no `motor_publicador.py` (MD5 `5b7322a78cf5b58beaa11f2e43c2ac1b`)

- Removido das sentinelas TÍTULO: `ficticio/ficticios/ficticia/ficticias` puros
- Adicionadas colocações compostas TÍTULO: `eventos sao ficticios`, `conflito ficticio`, `evento ficticio`, `cenario ficticio`, `informacoes ficticias`, `dados ficticios`

### Lição arquitetural

- Antigravity é forte detectando casos de borda editoriais (cultura/defesa não passariam pelo radar técnico do Codex/Claude).
- Codex é forte aplicando princípios conservadores (não expandir filtros sem evidência).
- **Combinar é melhor que escolher** — refinamentos baseados em casos REAIS (FP determinístico) entram, expansões especulativas (8 padrões genéricos) ficam pra evidência observada.

### Backups vivos
- Pré-blindagem (incidente original): `bkp_pre_blindagem_recusa_20260502_1214`
- Pré-refino v2: `bkp_pre_refino_v2_20260502_1230`

---

## ✅ util_categorizador_rigido restaurado 2026-05-02 12:43 BRT

Arquivo local existia (mtime 25/04 15:15, 13.638 bytes). Faltava só no Tencent. scp + chmod 644 + py_compile OK + import test OK. MD5 `78a81155a62c0a25096bb1a331174df5`. Próximo cron vai usar categorizador rígido em vez de fallback "Política" histórico.

## 🔍 strip_html resíduo PARKED 2026-05-02 12:43 BRT

motor_publicador.py do Tencent NÃO tem strip_html (confirmado por grep). Mesmo assim log de master_geopolitica mostra `Erro lendo banco json: name 'strip_html' is not defined` em 4 ciclos hoje (10:08, 10:11, 12:08, 12:08:23).

Reproduzir o erro localmente: NÃO consegui. Tentei chamada direta, escudar_modulo idêntico ao cron, e hooks de captura de stack — todos rodaram sem disparar o erro.

Erro NÃO BLOQUEIA publicação (capturado pelo try/except, motor continua). É ruído de log, não bloqueador.

Decisão: PARKED. Pedindo parecer Codex/Antigravity sobre cache pyc antigo, banco JSON corrupto, race condition.

---

## ✅ Sprint Tarefa A Onda 1 deployada 2026-05-02 13:08 BRT

### Cobertura final: 12 agentes protegidos

**Já blindados via motor (5):** master_geopolitica, master_nacional, master_trends, master_lula, reciclador.

**Novos blindados via import de `detectar_recusa_llm` (7):**
- 6 temáticos via `publicador_tematicos.parsear_resposta_llm` (linha 387):
  agente_ia, agente_inflacao, agente_matriz_energetica, agente_mercado, agente_petroleo, agente_energias
- 1 china via `agente_china.py` linha 884 após `extrair_html_e_titulo`

### MD5
- publicador_tematicos: `e58cc3e3...` → `1bbd2777...`
- agente_china: `a62a761d...` → `bd05360e...`

### Backups
- `/root/publicador_tematicos.py.bkp_pre_recusa_onda1_20260502_1307`
- `/root/agente_china.py.bkp_pre_recusa_onda1_20260502_1307`

### Estratégia confirmada por Antigravity §canal 12:55 BRT
- Import centralizado vs inline: import vence (fonte única de verdade pra sentinelas).
- Sem risco de import circular (motor_publicador não importa agente_china).
- 6 temáticos confirmados sem bypass do parsear_resposta_llm.

### Pendências futuras

**Onda 2 (próxima sprint):**
- agente_eleicoes_produtor (3x/dia)
- agente_fantastico (cron 4 */2)
- **agente_feminino** ← Antigravity alertou subir (usa regex json.loads(m.group()) — vulnerável)

**Onda 3 (opcional):** auditar quais ainda rodam dos legados/inativos.

---

## ✅ Sprint Tarefa A Onda 2 deployada 2026-05-02 13:15 BRT

### Cobertura final: 15 agentes protegidos contra vazamento de recusa LLM

| Mecanismo | Agentes |
|---|---|
| Via motor (iniciar_publicacao_especializada) | master_geopolitica, master_nacional, master_trends, master_lula, reciclador |
| Onda 1 (publicador_tematicos.parsear_resposta_llm) | agente_ia, agente_inflacao, agente_matriz_energetica, agente_mercado, agente_petroleo, agente_energias |
| Onda 1 (agente_china) | agente_china |
| Onda 2 | agente_eleicoes_produtor, agente_fantastico, agente_feminino |

### MDs Onda 2
- agente_eleicoes_produtor: `2aa58d8a...` → `4d2bfeec...`
- agente_fantastico: `c9986b09...` → `406d0ac5...`
- agente_feminino: `fb48bc45...` → `748748ef...`

### Padrão técnico consolidado
Todos os hooks usam `try: from motor_publicador import detectar_recusa_llm; ... except ImportError: pass` (fail-open: se o módulo central falhar, o agente não quebra).

### Onda 3 pendente (opcional, baixa prioridade)
Auditar atividade real dos seguintes agentes antes de blindar:
- escritor_scifi (en/pt), ficcao_noturna
- historiador (atual+bkp), singularidade, riocarta
- master_trends_v9 (legacy), eleicoes_legado, analytics_v9
