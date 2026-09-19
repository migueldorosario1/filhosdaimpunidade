---
name: project-no-home-opcao-d-descentralizada
description: Decisão Miguel 07/06 ~04:40 BRT — No-Home NÃO deve ter fonte única no motor (single point of failure). Opção D = util_no_home.py descentralizado + auditor periódico em defesa em camadas.
metadata: 
  node_type: memory
  type: project
  originSessionId: ad62e53a-7337-4799-84ba-ed7ccefc1122
---

🛡️ **Decisão arquitetural Miguel 2026-06-07 ~04:40 BRT:** No-Home **não deve ser centralizado no motor_publicador**. Risco: bug no motor para No-Home em todos os 14+ agentes. Caminho aprovado preliminarmente é **Opção D — Defesa em Camadas Descentralizada**.

**Why:** Quando Claude propôs Opção A (motor como fonte única), Miguel respondeu: "não sei se quero passar por fonte única. isso é perigoso, porque se quebrar o motor, tudo para". Decisão alinha com filosofia geral do projeto: agentes independentes, defesa em profundidade, fail-open em cada camada.

**How to apply (arquitetura proposta):**

**Camada 1 — `util_no_home.py` (helper compartilhado fail-open):**
```python
# /root/util_no_home.py
SCORE_LIMITE = 6.5
CATEGORIA_NO_HOME = 20699

def aplicar_no_home_se_necessario(payload: dict, score, log=None):
    """Fail-open. Retorna payload (possivelmente mutado). NUNCA lança."""
    try:
        if score is None: return payload
        if float(score) < SCORE_LIMITE:
            if 'categories' in payload and isinstance(payload['categories'], list):
                if CATEGORIA_NO_HOME not in payload['categories']:
                    payload['categories'].append(CATEGORIA_NO_HOME)
                    if log: log(f'🏠 NO-HOME aplicado (score {score})')
    except Exception:
        pass
    return payload
```

Cada agente faz 1 linha ANTES de `requests.post(WP_URL)`:
```python
from util_no_home import aplicar_no_home_se_necessario
payload = aplicar_no_home_se_necessario(payload, score, log=log)
```

**Camada 2 — auditor periódico (rede de segurança):**
- Cron 1h cruza posts publish recentes × `_score` em postmeta
- Se `score < 6.5` e cat 20699 NÃO presente → PATCH WP API adiciona
- Pega gap dos agentes que esqueceram de importar `util_no_home`

**Vantagens da Opção D vs fonte única:**
- ✅ Se `util_no_home` quebra → cada agente segue publicando normal (fail-open)
- ✅ Se 1 agente esquece import → outros 13 seguem funcionando
- ✅ Independência entre agentes
- ✅ Auditor pega gaps posteriores
- ✅ Motor segue tendo seu uso (não muda — quem já passa continua passando)

**Implementação pendente** — Kimi vai consolidar a opção final. Frente registrada também na agenda. Patch `motor_publicador.py` linhas 2260-2269 (Kimi 07/06 02:55) mantém-se temporariamente como fallback até a Camada 1 estar deployada nos agentes.

Relacionado: [[feedback_soltar_posts_nao_prener]] (fail-open), §93 (indexing), §94 (trava anti-repetição).
