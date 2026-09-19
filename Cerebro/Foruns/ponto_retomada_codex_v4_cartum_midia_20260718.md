# Ponto de retomada — V4 cartum e mídia

**Agente:** Codex  
**Data:** 18/07/2026 BRT  
**Sessão:** `CODEX-V4-R3-CARTUM-FAIXA`  
**Objetivo:** consolidar o cartum como saída editorial de mídia do V4.

## Estado alcançado

- Contrato econômico do cartum ativo: rigor pré-geração e bloqueio pós-geração somente catastrófico.
- Todo cartum publicado exige faixa inferior incorporada ao bitmap final, com uma ou duas frases, logo oficial e `ocafezinho.com`.
- Texto, logo e domínio entram por composição determinística posterior; o modelo visual gera somente o desenho.
- Faixa não é legenda do WordPress. Caption permanece metadado separado e opcional.
- Logo oficial ainda precisa ser selecionada como ativo canônico; nenhuma logo improvisada foi adotada.
- Regressão conjunta em 18/07/2026: **348 passed**.

## Arquivos principais

- `Projeto Cafezinho Agentes/root/v4_labs/labs/sprints_v4_20260718/charge_editorial_cafezinho/PROMPT_MESTRE.md`
- `Projeto Cafezinho Agentes/root/v4_labs/labs/sprints_v4_20260718/grok_cartum_r3/contratos/v4_cartum_editorial_contract_v1.json`
- `Projeto Cafezinho Agentes/root/v4_labs/labs/sprints_v4_20260718/grok_cartum_r3/codigo/cartum_contract.py`
- `Projeto Cafezinho Agentes/root/v4_labs/labs/sprints_v4_20260718/grok_cartum_r3/testes/test_cartum_contract.py`
- `Cerebro/Foruns/forum_dois_eixos_v4_texto_humano_charge_editorial_20260718.md`

## Pendências

1. Selecionar e versionar a logo oficial do Cafezinho.
2. Implementar o compositor determinístico da faixa e testar cortes sociais.
3. Corrigir filtro MIME/PDF e melhorar correspondência semântica de candidatos.
4. Reavaliar o input R3 correto do Kilo no tribunal editorial.
5. Executar uma geração real controlada, visão real e canário completo.
6. Criar um draft WordPress reversível antes da autonomia limitada.

## Custo e risco

- Custo desta alteração: US$ 0.
- Sem geração paga, WordPress, deploy ou efeito externo.
- Risco atual: arquitetura pronta, mas aparência da faixa e logo ainda não validadas em bitmap real.

## Rollback

Reverter os campos `context_strip` e as alterações correspondentes nos quatro arquivos do lab; nenhuma alteração externa precisa ser desfeita.

## Primeiro comando seguro

`python3 -m pytest codigo/test_contracts.py codigo/test_casos_editoriais.py codigo/test_redator_telemetria_end_to_end.py codigo/test_wordpress_media.py codigo/test_last_mile_reconcile.py labs/sprints_v4_20260718/claude_integracao/test_integracao_negativos.py labs/sprints_v4_20260718/grok_cartum_r3/testes/test_cartum_contract.py -q --tb=short`

