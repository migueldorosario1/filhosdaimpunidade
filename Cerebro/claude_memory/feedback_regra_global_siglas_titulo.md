---
name: feedback-regra-global-siglas-titulo
description: "Regra editorial GLOBAL pra todos os agentes (LEGADO + V3 + YT V2 + REFORMA): NÃO usar sigla no título do post, EXCETO se for sigla muito famosa (ONU, CBF, FBI, OTAN, BRICS, STF, PT, PL, EUA, etc). Siglas técnicas ou raras (OCR, LLM, API, MoE, NCM, SUS, ECT, CGU) devem ser substituídas no título por descrição funcional. Caso fundador #260250 título OCR removido por Miguel 22/06 15:10 BRT."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f312988d-5dc6-4ea6-b08a-94b4cada57ec
---

📰 **REGRA EDITORIAL GLOBAL — siglas no título**

Miguel definiu 2026-06-22 15:10 BRT como **regra geral aplicável a TODOS os agentes** do Cafezinho (LEGADO, V3, YT V2, REFORMA, etc):

> *"Bota isso como regra. Regra geral, pra todos os agentes."*

## Princípio

Título do post **NÃO pode conter sigla** que o leitor leigo não reconheça de cara. Se o leitor precisa parar pra pensar "o que significa essa sigla?", o título já está errado.

## ✅ Siglas PERMITIDAS no título (lista positiva)

Apenas siglas **muito famosas** que TODO brasileiro reconhece de cara:

**Instituições**: ONU, OTAN, BRICS, FMI, OMS, OEA, União Europeia (UE)
**Brasil política**: STF, STJ, TSE, PF (Polícia Federal — OK), MP (Ministério Público), CPI, MPF, AGU, CGU, MEC, INSS, IBGE
**Brasil esportes/cultura**: CBF, COB, COI, USP, UFRJ, UnB
**Países/povos**: EUA, URSS (histórico), UK (limite), CIA (sigla famosa em internacional), FBI, KGB
**Partidos com sigla canônica**: PT, PL, PSOL, MDB, PP, PSDB, PCdoB, NOVO, UB, REPUBLICANOS, PODE
**Tipos de organização**: ONG, S/A, LTDA, MEI

## ❌ Siglas PROIBIDAS no título (lista negativa expandida)

Siglas técnicas/raras que **devem virar descrição funcional**:

**Tecnologia/IA**: OCR, LLM, API, GPU, TPU, MoE, RAG, ML, NLP, MMLU, HumanEval, B parameters
**Saúde**: SUS pode ser exceção (todo brasileiro conhece), ANS, ANVISA OK, mas DPI, DRG, AIH → fora
**Comércio**: NCM, ICMS, IPI, COFINS → simplificar pra "imposto", "código", "taxa"
**Comunicação**: ECT (Empresa Brasileira de Correios) → "Correios"
**Geral**: qualquer sigla com mais de 4 letras OU criada nos últimos 3 anos OU que precise contexto técnico

## ❌ Caso fundador 22/06 15:10 BRT (#260250)

**Antes (errado)**: "Nova IA chinesa de OCR lê texto em 50 idiomas e roda até em celular"
- OCR não é sigla famosa pro leitor médio
- Fica esquisito ("IA chinesa de OCR" — soa técnico)

**Cura aplicada (certo)**: "Nova IA chinesa lê texto em 50 idiomas e roda até em celular"
- Funcionalidade descrita ("lê texto em 50 idiomas") substitui a sigla
- Leitor entende o que o produto faz sem precisar saber o que é OCR

## Como aplicar

### No corpo do post
A sigla técnica PODE aparecer **expandida na 1ª ocorrência** (regra antiga, mantida): *"OCR (Optical Character Recognition / reconhecimento óptico de caracteres)"* aparece no corpo, mas NUNCA no título.

### No título
Substituir sigla por:
1. **Descrição funcional**: "OCR" → "lê texto em imagens"
2. **Função observável**: "LLM" → "modelo de IA"; "API" → "sistema online"; "GPU" → "placa gráfica"
3. **Função pro leitor**: "RAG" → "IA que busca antes de responder"; "MoE" → "IA com comitê de especialistas"

### Quando sigla famosa pode entrar
- Se ALL caps + ≤4 letras + reconhecível (ONU, STF, EUA, FBI) → OK
- Se contexto político brasileiro evidente (PT, PL no contexto eleitoral) → OK
- Em dúvida: substituir. **Default = SEM sigla.**

## Aplicação por agente (responsabilidade)

| Agente | Patch §92 sugerido | Prioridade |
|--------|-------------------|------------|
| **agente_ia.py** | regex deny-list no título + dicionário siglas tech | 🔴 alta (já tem casos) |
| **agente_master_trends** | mesma deny-list | 🟡 média |
| **agente_china** | siglas chinesas (PCC, Xinhua → OK; CCP, BRI, RPC → substituir) | 🟡 média |
| **agente_singularidade** (se rodando) | siglas tech | 🟡 média |
| **executar_producao_editorial_v3** (V3) | system prompt do redator | 🟡 média |
| **agente_youtube_v2_produtor** | guest_name no título já está sendo trabalhado (B-001+B-002); adicionar regra siglas | 🟢 baixa |
| **Demais (lula/flavio/eleicoes/soberania/militar/latam/sheinbaum/crime)** | system prompt geral | 🟢 baixa (já fazem ok mostly) |

## Implementação genérica sugerida (Kimi/Codex)

`/root/util_validador_titulo_global.py`:

```python
SIGLAS_FAMOSAS = {"ONU","STF","STJ","TSE","PF","MP","MPF","CPI","AGU","CGU","MEC","INSS","IBGE",
                  "CBF","COB","COI","USP","UFRJ","UnB","EUA","UK","CIA","FBI","ONG","SUS",
                  "PT","PL","PSOL","MDB","PP","PSDB","PCdoB","NOVO","UB","REPUBLICANOS","PODE",
                  "OTAN","BRICS","FMI","OMS","OEA","UE","ANS","ANVISA"}

def titulo_tem_sigla_proibida(titulo: str) -> tuple[bool, list[str]]:
    """Retorna (True, lista_siglas) se título contém siglas não-famosas (≥2 chars all-caps)."""
    import re
    siglas = re.findall(r'\b[A-Z]{2,}[A-Z0-9-]*\b', titulo)
    proibidas = [s for s in siglas if s not in SIGLAS_FAMOSAS]
    return (len(proibidas) > 0, proibidas)
```

Usar em qualquer agente antes do POST:
```python
ok, proibidas = titulo_tem_sigla_proibida(titulo)
if not ok:
    log(f"⚠️ Título tem siglas não-famosas: {proibidas} — reformulando via LLM")
    titulo = chamar_llm_reformular_titulo(titulo, remover_siglas=proibidas)
```

## Why

Cafezinho é portal **generalista de esquerda progressista** — leitor diverso, maioria não-técnica. Título técnico afasta. Métrica observada: posts com sigla técnica no título têm CTR no GA4 ~30-40% menor que título descritivo equivalente (estimativa Miguel/observação editorial histórica).

## Aplica em conjunto com

- [[feedback-titulos-simples-siglas-explicadas-agente-ia]] — regra anterior só do agente_ia, esta é versão GLOBAL ampliada
- [[feedback-yt-v2-titulo-analista-nominal-corpo-7p]] — YT V2 tem regra de nome do guest no título (similar princípio: clareza, função, observável)
