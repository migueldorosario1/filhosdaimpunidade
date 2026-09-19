---
name: reference-cafezinho-instabilidade-madrugada-backup-servidor-20260820
description: Instabilidade transitória do servidor Cafezinho de madrugada é normal — janela de backup do servidor. Não escalar como incidente
metadata: 
  node_type: memory
  type: reference
  originSessionId: 0dcfd4fe-1561-42c4-9a28-e7c51dd207b7
---

# Cafezinho instabilidade madrugada = backup do servidor (20/08/2026 03:33 BRT — Miguel)

**Origem:** Miguel me disse textual 03:33 BRT: *"o cafezinho as vezes fica instavel de madrugada por causa de backup do servidor. é o que me disseram"*.

## O que aparece pra mim

- Erros `Error establishing a database connection` em `wp` cli (via SSH cafezinho-wp)
- `/tmp/*.json` sumindo entre `scp` e `wp eval` (o servidor pode rebootar durante a janela)
- Timeout em `wp eval` grandes
- Occasional gate `_cafezinho_img_check` reverte pra pending por perda de meta durante escrita concorrente ao backup

## Quando esperar

- Madrugada BRT (aproximadamente 03:00-05:00 pelo que observei — janela típica de backups)
- Sem alerta prévio (não veio comunicado do provedor)

## Como reagir

- **NÃO escalar como bug/incidente crítico** — é operação normal do provedor
- **Retry após 10-20s** — geralmente resolve
- Se retry falhar 2-3 vezes: aí sim algo diferente, escala Miguel
- Sempre re-verificar após retry se o estado do WP está consistente (post_status, meta gravada, etc.) — pode ter revertido durante o incidente

## Aprendizado do incidente 03:30 BRT (20/08)

Estava publicando 266704 CNPC cultura Slot B. Sequência:
1. Tentativa 1: `wp eval` deu `Error establishing a database connection` — abortou
2. Retry após 10s: gate anti-vazio detectou que `/tmp/img_check_266704.json` sumiu → escreveu meta vazia → gate reverteu post pra pending automaticamente
3. Re-scp arquivo pro `/tmp` + wp eval + confirmar `gate=PASS` **antes** do publish → OK

**Lição:** sempre confirmar gate PASS **pré-publish** com `wp eval require_once + cafezinho_gate_img_tem_checagem()` **antes** de rodar `wp post update --post_status=publish`, especialmente na madrugada.

## Refs

- Bugs JSONL 2026-08-20 03:32 (incidente_servidor documentado)
- Meta `_cafezinho_img_check` vazia = gate reverte pending automático (bug conhecido documentado em `feedback_wp_meta_update_json_grava_vazio_20260817`)
