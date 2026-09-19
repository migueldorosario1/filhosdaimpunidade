# Memória — Cerco a títulos longos no V4 (log técnico)

> [!CAUTION]
> **CORTE ARQUITETURAL POSTERIOR NESTE MESMO DIA.** O diagnóstico e o histórico do gate de títulos continuam válidos, mas alterações em `agente_controlado.py` não definem o V4 atual. Desde o corte de 09/08, diretrizes de redação pertencem ao worker/runtime V4 canônico. Ver `memoria_arquitetura_v4_canonica_pos_cutover_20260810.md`.

**Data:** 2026-08-09 ~03:50–07:15 BRT
**Sessão:** ZCode (GLM-5.2, builtin:zai-coding-plan)
**Par:** `forum_cerco_titulos_longos_v4_20260809.md`
 **Cofre usado:** `/home/migueldorosario/Downloads/Antigravity Google/Outros/chaves/agentes_labs/.env.unificado` (WP_USER_CAFEZINHO/WP_PASS_CAFEZINHO; nunca exposto).

---

## Arquivos tocados

### Servidor NYC (`ssh nyc` = root@198.199.121.136, ProxyJump direto)
- `/root/gate_titulo.py` — **NOVO** (6007 bytes). Fonte única de regras de título.
- `/root/motor_publicador.py` — editado (2764→2806 linhas). Gate inserido após linha 2493.
- `/root/agente_controlado.py` — editado (5 mudanças pontuais via patch).
- `/root/titulo_utils.py` — **não tocado** (só backup por segurança).
- Backups: `*.bak_pre_cerco_titulos_20260809` (3 arquivos).

### Local (máquina do Miguel)
- `Cerebro/Foruns/forum_cerco_titulos_longos_v4_20260809.md` — **NOVO**.
- `Cerebro/Memorias/memoria_cerco_titulos_longos_v4_20260809.md` — **NOVO** (este).
- `Cerebro/MONITORAMENTO_DE_TRABALHO.md` — linha de sessão adicionada + `.bak`.
- `/tmp/gate_titulo.py`, `/tmp/patch_motor_publicador.py`, `/tmp/patch_agente_controlado.py`, `/tmp/busca_post_miguel.py`, `/tmp/audit_titulos_recentes.py`, `/tmp/checklist_titulos.py`, `/tmp/fix_marcola.py` — scripts de trabalho.

## Código do `gate_titulo.py` (essência)

```python
TITULO_MAX = 80          # hard limit (era 90; apertado por ordem Miguel 09/08)
TITULO_IDEAL_MIN = 55
TITULO_IDEAL_MAX = 75
TITULO_MIN_PALAVRAS = 4
_TRAVESSOES = ("—", "–", "−", "―")

def validar_titulo(titulo):       # -> (ok, motivo)  hard rules
def aplicar_gate_titulo(titulo, corpo, llm_fast):  # -> str  sempre válido (LLM×2 ou fallback local)
def _sanitizar_local(titulo):     # fallback determinístico (corta :/travessão, trunca 78c)
```

## Patch `motor_publicador.py` (inserção)

Após `payload["title"] = remover_citacao_crua(limpar_markers(...))` (linha ~2493), antes do `requests.post(WP_URL)` (linha ~2586):
```python
from gate_titulo import aplicar_gate_titulo, validar_titulo
def _llm_fast_titulo(prompt, temperature=0.3, max_tokens=120):
    from agente_roteador_llm import gerar_texto
    return gerar_texto("Reescritor de títulos. Devolva APENAS o título.", prompt,
                       agente_nome="gate_titulo", contexto="titulo_curto",
                       max_tokens=max_tokens, temperature=temperature)
_tit_depois = aplicar_gate_titulo(_tit_antes, corpo=payload.get("content",""), llm_fast=_llm_fast_titulo)
if _tit_depois and _tit_depois != _tit_antes: payload["title"] = _tit_depois
```
Tudo envolvido em `try/except` — **falha no gate nunca aborta publicação**.

## Patch `agente_controlado.py` (5 mudanças)

1. `validar_titulo()` (linha ~1554): corpo substituído por delegação `from gate_titulo import validar_titulo as _gate_validar; return _gate_validar(titulo)` + fallback local.
2. `ajustar_ou_regenerar_titulo()`: 3 substituições de string (faixa 60-80→55-75, aceitação 60-85→55-78, docstring).
3. Prompt `gerar_noticia` bloco TITULO: "Máximo 8 palavras" → "Máximo 8 palavras **e** 75c" + "NUNCA travessão".
4. Prompt `revisar_com_claude`: "5. Sem travessão…" → + "6. TÍTULO 55-75c, sem `:`, sem travessão, regência correta".
5. Prompt `auditar_com_deepseek`: lista de problemas + 3 itens (título >80c, com `:`, com travessão, regência).

## Provas de teste

```
$ python3 -m py_compile motor_publicador.py agente_controlado.py gate_titulo.py  # todos OK
$ # gate contra 3 títulos reais:
Caso 1 (193c) validar=False [título muito longo (193 chars, máx 80)]  → sanitizado 75c
Caso 2 (134c) validar=False [título muito longo (134 chars, máx 80)]  → sanitizado 77c
Caso 3 (168c) validar=False [título muito longo (168 chars, máx 80)]  → sanitizado 75c
$ # fluxo real (roteador LLM down no momento):
DEPOIS (77c): China vai à Lua com cães robôs Academia Espacial planeja patrulha robótica na
validar: True [ok]   ← fallback segurou mesmo com IA fora
```

## Post corrigido ao vivo

- **#264875** título 193c → 72c: "Marcola sai da campanha de Lula por empréstimo de R$ 249 mil com lobista"
- Verificado: `WP REST POST /posts/264875` 200; novo title retornado = 72c.

## Checklist — 18 posts pendentes (decisão Miguel)

| ID | chars | trecho do título atual |
|---|---|---|
| 264871 | 134 | China vai à Lua com cães robôs: Academia… |
| 264869 | 163 | Marina Silva saiu do MMA… Lula arquiva Autoridade Climática — |
| 264865 | 164 | Flávio promete mulheres no STF… 'Café Entre Elas'… |
| 264858 | 165 | EUA acusam China… 'reserva natural'… Scarborough… |
| 264861 | 161 | 26 x 16 em palanques… Tarcísio lidera em SP: … |
| 264852 | 168 | 78 kWh de diferença… ar-condicionado… — Hisense… |
| 264853 | 183 | Mendonça manda PT… 'Porta-Vozes de Lula' — … |
| 264845 | 168 | Pequim ajusta a torneira das terras raras: corte… |
| 264851 | 194 | Pré-candidata… MBL… 'patriarcado é biológico' — … |
| 264842 | 155 | Pequim conquistou o governo de Modi… Índia: … |
| 264843 | 156 | Do MTST à Vila Euclides — … Lula promete 3 milhões… |
| 264839 | 145 | Amazônia bate menor desmatamento… (−36,87%) — … |
| 264832 | 153 | 'Não confiamos, verificamos': Vance cobra Irã… — |
| 264830 | 145 | US$ 20 bilhões em um ano: AstraZeneca… |
| 264833 | 126 | Nikolas usa Fauci… 'inocentar' Bolsonaro… — |
| 264821 | 138 | Chapéu de palha, terno azul… Lula estreia visual… |
| 264818 | 162 | Julho fez história… BYD ultrapassa Chevrolet… — |
| 264828 | 124 | Petecão troca Paraná Pesquisas… 5º lugar… |

## O que aconteceu / o que falta / o que preciso de você (Miguel)

- **Aconteceu:** Marcola corrigido ao vivo; cerco de título aplicado no publicador + gerador + 3 revisores (Claude/DeepSeek/GPT via prompt). Gate funciona mesmo com LLM fora (fallback). Backups no servidor.
- **Falta:** confirmação do novo teto (80c); decisão sobre os 18 posts antigos; espelho do `gate_titulo.py` no Tencent se ele publica.
- **Preciso de você:** (1) aprovar 80c como teto? (2) quer que eu reescreva os 18 antigos — manual/automático/deixa? (3) Tencent publica? Se sim, copio o gate lá.
