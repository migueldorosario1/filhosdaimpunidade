---
name: Banco de mídia ativado para TODOS os agentes em duas fases (2026-04-17)
description: FASE 1 (motor_publicador) e FASE 2 (gerador_imagem_editorial) — todo o sistema agora tenta imagem real do banco SQLite antes de gerar cartoon.
type: project
originSessionId: 82c307d7-bd07-4c7a-8ed2-9e86b6fa4e22
---
Em 2026-04-17 o banco `banco_imagens_reais.db` (~17k imagens de Flickr institucional + Wikimedia Commons) foi integrado ao fluxo de TODOS os agentes do Cafezinho em duas fases.

## FASE 1 — via motor_publicador (deploy 08:55)

Afeta os 5 chamadores de `iniciar_publicacao_especializada`: `agente_master_geopolitica`, `agente_master_nacional`, `agente_master_trends`, `agente_reciclador`, `agente_soberania`.

- Default `exige_imagem_real` mudado de `False` → **`True`** (linha 530).
- Default `nota_corte_imagem` mudado de `90` → **`None`** (herda 40 do `gerenciador_imagens.py`).
- Refatoração linhas ~590 e ~635: **não queima mais a pauta por falta de imagem** — segue com fallback editorial.
- `agente_soberania.py` linha 47: `exige_imagem_real=False` → `True`.

## FASE 2 — via gerador_imagem_editorial (deploy 09:10)

Afeta TODOS os agentes que chamam `generate_editorial_image()` (feminino, fantástico, ferroviário, eleições, china, historiador, pet, turismo_embratur, manchete e outros).

Inserido bloco NOVO no início de `generate_editorial_image` (antes de chamar Flux/Ideogram/DALL-E):
- Importa `buscar_imagem_banco_local` do `gerenciador_imagens`
- Passa título + `resumo_materia` extraído pelo `_extrair_resumo_critico`
- Se achar → retorna com `gerador="banco_midia_real"` e imagem real
- Se não achar → cai no pipeline original (Flux Pro → Ideogram → DALL-E 3)

## FASE 3 — legenda jornalística propagada para TODOS os agentes (deploy 10:20)

Gap descoberto quando Miguel notou que o post #235741 saiu com legenda genérica ("Registro fotográfico referente aos eventos da atualidade"). Tribunal Visual gerava legenda rica mas ela se perdia na Fase 2: `generate_editorial_image` não incluía `legenda` no dict de retorno.

**Fix:**
1. `gerador_imagem_editorial.py` — adicionado campo `"legenda"` no dict `resultado`. Quando acha foto no banco, salva a legenda do Tribunal Visual ali.
2. **11 chamadores atualizados via sed universal** (`fazer_upload_imagem_wp(r["url_imagem"])` → `fazer_upload_imagem_wp(r["url_imagem"], legenda=r.get("legenda"))`):
   - `agente_analytics_v9`, `agente_eleicoes`, `agente_escritor_scifi` (x2), `agente_fantastico`, `agente_feminino`, `agente_ficcao_noturna`, `agente_historiador` (x2), `motor_publicador`, `urgencia_ira`.
3. Como subproduto, foram corrigidos mais 4 arquivos com bug `caixa_newsletter` que ainda estavam quebrados: `ficcao_noturna`, `historiador`, `historiador_bkp`, `urgencia_ira` (completando os 10 arquivos totais afetados pelo bug original).

Post #235741 teve a legenda corrigida manualmente no WP via API (`POST /wp-json/wp/v2/media/235740` com nova caption) — mostrou ao Miguel o formato certo: "O presidente Lula durante reunião com Vladimir Putin no Grande Palácio do Kremlin, em maio de 2025. (Foto: Wikimedia Commons)".

## Como o banco decide se a imagem é boa

Lógica em `gerenciador_imagens.py` (NÃO editado por Claude — é ajuste do Miguel):
1. Pesquisa SQLite: candidatas com score textual ≥ **40** (default novo, rebaixado vs o 80 antigo)
2. Top 4 candidatas por score textual entram no **Tribunal Visual** (`analisar_imagem_gemini_vision` via Google Gemini)
3. Vision recebe: URL da foto + **título** da matéria + **resumo/lead** da matéria + origem (Flickr/Wikimedia) + metadados
4. Vision retorna `APROVADA`/`REPROVADA` + uma legenda jornalística pronta
5. Primeira APROVADA vence e retorna `(url, legenda)`
6. Se todas reprovadas → retorna `(None, None)` → cai no fallback

## Backups no servidor

- `/root/motor_publicador.py.bak_20260417_0855`
- `/root/agente_soberania.py.bak_20260417_0855`
- `/root/gerador_imagem_editorial.py.bak_20260417_0910` (só fase 2)

## Why

Alinhar com política "publicar os melhores, não guilhotinar" + aproveitar o banco de 17k fotos reais. Antes só Ideogram/Flux geravam cartoon — agora o conteúdo editorial pode ter imagens reais quando o Tribunal Visual julga que a foto combina com o texto.

## How to apply

- **Agente novo:** se chamar `generate_editorial_image(artigo)` com artigo contendo `titulo` + `resumo`/`conteudo` + `secao`, já usa banco automaticamente.
- **Ajustar rigor:** mudar `NOTA_DE_CORTE_MATCH_IMAGEM` em `gerenciador_imagens.py` (linha 12) — hoje 40.
- **Desabilitar banco para um agente específico:** em agentes com motor_publicador, passar `exige_imagem_real=False`. Em agentes com gerador editorial, mais difícil — teria que contornar a chamada (ou adicionar parâmetro).
- **Backup operacional:** o gerador editorial cartoon continua funcionando (Flux+Ideogram+DALL-E) — se o banco falhar ou Vision rejeitar tudo, pipeline pega.
