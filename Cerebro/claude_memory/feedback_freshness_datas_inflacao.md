---
name: Inflação — freshness de datas + marca de IA em citações
description: Depois do dia 15 do mês, qualquer matéria sobre mês anterior é ultrapassada. Citação inline `([fonte.com](url))` é marca de IA proibida.
type: feedback
originSessionId: 50202c88-5137-43d9-ac6f-5fb1c3ffc1d6
---
Em 2026-04-21 Miguel sinalizou 2 problemas no draft do `agente_inflacao.py` (título: "Alta de gasolina dispara 4,59% em março..."):

**Rule 1 — Freshness por idade do índice (RELATIVIZADA 2026-04-21 21:30):**
- Aborta se TODOS os 4 índices (IPCA, IPCA-15, IGP-M, IGP-DI) têm **idade de divulgação > 15 dias**
- Publica se pelo menos um foi divulgado há ≤ 15 dias
- Idade é calculada pela data ESTIMADA de divulgação (fim do mês ref + atraso por série), não pelo mês de referência em si.

**Why:** Miguel inicialmente pediu "dia>15 + SIDRA velho = aborta" — mas isso silenciava o agente ~19 dias por mês. Reconsiderou: "basta ajustar a regra. o índice não pode ter mais de 15 dias". IPCA-15 e IGP-M/IGP-DI preenchem os gaps do IPCA oficial — ignorá-los era desperdício editorial de um tema de primeira página.

**How to apply:**
- `agente_inflacao.py`: `indices_frescos_15d()` consulta BCB SGS (séries 433, 7478, 189, 190), estima data de divulgação por série e filtra idade ≤ 15d.
- Se pelo menos um fresco → publica com headline dos índices frescos injetado no contexto do LLM via `contexto_sidra += bloco_indices`.
- Se nenhum → aborta (raro; só acontece em janelas curtas entre ciclos de divulgação).
- Atrasos típicos mapeados em `_ATRASO_DIVULGACAO_DIAS`: IPCA +10d, IPCA-15 -8d, IGP-M 0d, IGP-DI +10d.

**Rule 2 — Citação inline estilo LLM é proibida:**
- Padrão: `([cnabrasil.org.br](https://cnabrasil.org.br/...))` — hostname entre colchetes seguido de URL entre parênteses, todo o bloco entre parênteses externos. Típico de Perplexity/GPT com web-search.
- Removido via `publicador_tematicos._limpar_citacoes_ia` — regex só pega quando texto visível é hostname reconhecido (tem TLD `.com`, `.org`, `.gov`, `.br`, `.io`, etc). Frases normais e `<a href>` legítimo ficam intactos.

**Why:** Miguel: *"o texto está cheio de marcas de IA"*. Citação inline com hostname cru quebra a prosa brasileira jornalística e denuncia máquina.

**How to apply:**
- Sanitização roda em todos os temáticos via `publicar_wp_premium` (IA, Mercado, Inflação, Matriz Energética)
- Prompt do inflação também ganhou regra explícita proibindo o formato
- Fonte segue saindo no rodapé via `_injetar_atribuicao_fonte` + atribuições em prosa ("segundo o IBGE")
