# PONTO DE RETOMADA — Kilo — 2026-07-09 00:05 BRT

**Sessao anterior:** 2026-07-07 ~15:50 a 2026-07-09 ~00:00 BRT
**Contexto:** rodada Super Luxo Editorial / V3-V4 Espelhados / Curadoria de Tese
**Memoria completa:** `Cerebro/memorias_provisorias/sessao_kilo_20260707_20260709_super_luxo_v4.md`

---

## Estado Atual

### O que esta feito:
- 7 arquivos de diretrizes criados em `diretrizes/` (nucleo + 4 V3 + GSN + freios LLM)
- 5 rodadas de discussao concluidas (Super Luxo, Imagem/Ciencia, Curadoria/Tese, Revisao Pacote, Fechamento)
- Consensos alcancados: curadoria de tese como camada real, schema enxuto (6 campos), advogado do obvio, memoria por casos, A/B cego antes de institucionalizar
- Protocolo de comunicacao cumprido integralmente

### O que falta:
- **`v4_curadoria_tese_v1.json` nao existe** — gap mais critico identificado
- `v4_auditoria_editorial_v1.json` nao existe
- Fusao de arquivos LLM routing (3→1) e dashboards (2→1) pendente
- Experimento A/B cego do 261439 nao foi executado

---

## Proximo Passo Imediato

### Prioridade 1: Criar contrato de curadoria de tese

**Arquivo:** `diretrizes/v4_curadoria_tese_v1.json`

**Schema minimo (6 campos obrigatorios + checklist):**
```json
{
  "fato_novo": "string",
  "leitura_corrente": {
    "resumo_consenso": "string",
    "fontes_consultadas": [],
    "timestamp": "ISO8601"
  },
  "teses_candidatas": [
    {
      "tese": "string (formato X→Y→Z→W)",
      "quem_ganha": "string",
      "quem_perde": "string",
      "evidencias_ref": [],
      "risco": "string"
    }
  ],
  "tese_escolhida": "string",
  "motivo_rejeicao_das_outras": [],
  "promessa_ao_leitor": "string",
  "briefing_produtor": "string",
  "checklist": {
    "fatos_travados": true,
    "consequencia_material": true,
    "angulo_diferente_do_consenso": true,
    "risco_juridico_revisado": true
  }
}
```

**Principios:**
- `obrigatorio_antes_da_producao: true`
- `curador_diferente_do_produtor: true`
- `gate_angulo_original_via_brave: true`
- `tese_formato_obrigatorio: "Quando X aconteceu, revelou-se que Y, o que significa Z para W"`
- `failure_policy.curadoria_falha_bloqueia_producao: true`

### Prioridade 2: Implementar modulo de curadoria

**Arquivo:** `v4_diretrizes/curadoria_tese.py` (ou equivalente no Tencent)

**Funcoes:**
1. `gerar_3_teses(material_auditado, editoria)` — gera 3 teses candidatas em formato X→Y→Z→W
2. `caracterizar_consenso(assunto)` — busca Brave para leitura corrente timestamped
3. `gate_angulo_original(tese_candidata, leituras_correntes)` — cosseno vs consenso (max 0.75)
4. `exportar_briefing(curadoria)` — exporta briefing para o produtor

**Nova camada:** `v4_data/curadoria/` entre `auditado` e `producao`

### Prioridade 3: Redirecionar produtor

**Mudanca:** produtor passa a ler de `curadoria`, nao de `auditado`

**Bloqueio:** producao sem `curadoria_id` deve falhar

**Teste:** `test_producao_sem_curadoria_bloqueia`

### Prioridade 4: Experimento A/B cego

**Caso:** 261439 (tarifa Trump-Flavio-Lula)

**Fontes:** mesmas (AP + El Pais)

**Procedimento:**
1. Rodar curadoria sobre as mesmas fontes
2. Gerar 3 teses candidatas
3. Escolher tese vencedora
4. Produzir versao B a partir da tese
5. Miguel escolhe cego (A vs B)
6. Se B ganhar, `v4_curadoria_tese` vira etapa obrigatoria

---

## Decisoes Consolidadas (para nao rediscutir)

1. **Curadoria de tese como camada real** entre `auditado` e `producao`
2. **Schema enxuto** (6 campos + checklist) em vez de 14
3. **Curador ≠ redator** (Grok curador + Claude revisor em politica)
4. **Advogado do obvio adversarial** (Fable)
5. **Memoria por casos com teto de ~20** (Fable)
6. **A/B cego antes de institucionalizar** (todos)
7. **Fusao so essencial na Fase 1** (LLM routing 3→1, dashboards 2→1)
8. **Gate anti-obvio corrigido** (Miguel): assunto quente sim, angulo igual ao consenso nao

---

## Riscos e Mitigacoes

| Risco | Mitigacao |
|-------|-----------|
| Curadoria virar teatro | Leitura corrente real, advogado do obvio, exigencia de fato material |
| Schema inchado gerar burocracia | Teste do Fable: cada campo deve mudar o texto final |
| Fusao massiva antes de provar ganho | Adiar para depois do A/B |
| Redator escolher tese que sabe escrever | Curador ≠ redator |
| Memoria virar manual de proibições | Casos como perguntas, teto de ~20 |

---

## Arquivos de Referencia

### Foruns:
- `Cerebro/Foruns/forum_novas_diretrizes_editoriais_correio_brasil_20260707.md`
- `Cerebro/Foruns/forum_super_luxo_editorial_v3_espelhado_20260707.md`
- `Cerebro/Foruns/forum_arquitetura_v3_imagem_ciencia_hibrido_diretrizes_20260707.md`
- `Cerebro/Foruns/forum_v4_curadoria_tese_editorial_20260708.md`

### Diretrizes:
- `diretrizes/nucleo_editorial_comum_v1.md`
- `diretrizes/v3_politica_economia_v1.md`
- `diretrizes/v3_cultura_v1.md`
- `diretrizes/v3_internacional_v1.md`
- `diretrizes/v3_repetidor_v1.md`
- `diretrizes/gsn_espelho_ingles_v1.md`
- `diretrizes/freios_llm_v1.json`

### Pacote V4 (espelho para revisao):
- `Cerebro/Foruns/diretrizes/` (30 arquivos)

### Memoria da sessao:
- `Cerebro/memorias_provisorias/sessao_kilo_20260707_20260709_super_luxo_v4.md`

---

## Checklist de Retomada

- [ ] Ler memoria completa da sessao
- [ ] Ler foruns atualizados (verificar se houve movimento apos a sessao)
- [ ] Criar `v4_curadoria_tese_v1.json`
- [ ] Implementar `curadoria_tese.py`
- [ ] Redirecionar produtor para ler de `curadoria`
- [ ] Rodar A/B cego do 261439
- [ ] Se A/B aprovado, integrar ao pipeline
- [ ] Fundir LLM routing (3→1)
- [ ] Fundir dashboards (2→1)
- [ ] Criar `v4_auditoria_editorial_v1.json`

---

## Observacao Final

O trabalho da sessao foi produtivo. Participei de 5 rodadas, criei 7 arquivos, revisei 30 arquivos, contribui para consensos. O proximo passo e claro: criar o contrato de curadoria e testar com o caso 261439 antes de codar mais.

Se o A/B mostrar ganho, integra. Se nao, revisa a diretriz antes de codar mais.

— Kilo, 2026-07-09 00:05 BRT
