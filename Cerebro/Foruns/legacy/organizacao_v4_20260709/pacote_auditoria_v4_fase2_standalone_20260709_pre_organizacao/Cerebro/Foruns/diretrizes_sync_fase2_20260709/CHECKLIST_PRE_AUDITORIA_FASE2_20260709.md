# Checklist pre-auditoria Fase 2 V4

Data: 2026-07-09

Este diretorio e o pacote limpo para auditoria externa da Fase 2. Ele substitui qualquer copia antiga em `/mnt/project` ou pacote anterior que ainda mostre 45 testes, meta-linguagem no redator shadow, curadoria sem `consequencia_material`, ou fato USTR com atribuicao ambigua.

## Comandos de sanidade

Rode a partir deste diretorio:

```bash
grep -c "def test_" v4_diretrizes_test_contracts.py
grep -n "segundo a curadoria\|promessa editorial" *.py *.json || true
grep -n "Associated Press registra" v4_real_001*.json
grep -n '"consequencia_material"\|"collection_request"\|"fatos_travados"' v4_real_001_curadoria.json
grep -n "collection_request" v4_redator_shadow_v1.json v4_diretrizes_redator_shadow.py
```

## Resultados esperados

```text
grep -c "def test_" v4_diretrizes_test_contracts.py
=> 52

grep -n "segundo a curadoria\|promessa editorial" *.py *.json || true
=> vazio

grep -n "Associated Press registra" v4_real_001*.json
=> deve encontrar o fato travado USTR nos arquivos de curadoria/shadow, incluindo os aliases com underscore

grep -n '"consequencia_material"\|"collection_request"\|"fatos_travados"' v4_real_001_curadoria.json
=> deve encontrar os tres campos no topo do payload de curadoria

grep -n "collection_request" v4_redator_shadow_v1.json v4_diretrizes_redator_shadow.py
=> deve encontrar a semantica de bloqueio por estagio e o metodo collection_blocks_stage
```

## Pontos corrigidos neste pacote

```text
1. Curadoria sincronizada com campos de Fase 2:
   - consequencia_material
   - collection_request
   - fatos_travados

2. Semantica de collection_request formalizada:
   - none nao bloqueia
   - recommended nao bloqueia antes de required_before
   - recommended bloqueia em required_before e estagios posteriores
   - required bloqueia em required_before e estagios posteriores

3. Meta-linguagem removida do redator shadow:
   - sem "segundo a curadoria"
   - sem "promessa editorial" no texto gerado

4. Fato USTR com atribuicao explicita:
   - "A Associated Press registra..."
   - fonte_ref aponta para AP

5. Dict vazio tratado como ausente:
   - {} nao satisfaz campos obrigatorios da curadoria

6. Aliases criados para evitar divergencia por nome:
   - v4_real_001.curadoria.json
   - v4_real_001_curadoria.json
   - v4_real_001.shadow_redacao.json
   - v4_real_001_shadow_redacao.json
```

## Escopo da auditoria

Este pacote serve para auditar a consistencia dos contratos e artefatos da Fase 2 shadow/dry-run. Nao autoriza:

```text
- WordPress real
- publicacao real
- chamada LLM externa
- institucionalizacao da curadoria antes de novos A/B cegos
```
