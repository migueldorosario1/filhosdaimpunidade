---
name: Imagem da fonte original como Prioridade 1 (2026-04-17)
description: motor_coletor agora captura og:image da matéria original junto com o texto; motor_publicador usa essa imagem primeiro (passando pelo Tribunal Visual), caindo no banco local só como fallback.
type: project
originSessionId: 82c307d7-bd07-4c7a-8ed2-9e86b6fa4e22
---
Em 2026-04-17 Miguel pediu que, ao invés dos agentes da Trindade/militar/soberania sempre buscarem imagem no banco de mídia local, eles tentassem primeiro a foto que vinha com a matéria original (TASS, Sputnik, Press TV, Global Times, Defesa.net, etc).

## Mudanças

### `motor_coletor.py`
1. Nova função `_extrair_og_image(html, base_url)` — parseia HTML com BeautifulSoup procurando, em ordem: `og:image` → `twitter:image` → `twitter:image:src` → `link rel="image_src"`. Resolve URLs relativas com `urljoin`, descarta `data:image`.
2. `extrair_texto_oficial(url)` agora retorna tupla `(texto, url_imagem_fonte)` em vez de só string. Mantém retrocompat: `worker_wrapper` testa se recebeu tupla ou string.
3. Dict final salvo no banco JSON tem campo novo `"url_imagem_fonte"`.

### `motor_publicador.py`
Tanto no bloco principal (~linha 590) quanto na reserva (~linha 656), a seleção de imagem quando `exige_imagem_real=True` virou **3 níveis de prioridade**:

1. **Prioridade 1 — imagem da fonte original (`artigo.url_imagem_fonte`):** envia ao `analisar_imagem_gemini_vision` (Tribunal) para validar se bate com o tema; se APROVADA, upload no WP com legenda gerada pelo Gemini (que inclui créditos reais, ex.: `(Foto: TASS)`, `(Foto: Press TV)`).
2. **Prioridade 2 — banco de mídia local:** `buscar_imagem_banco_local` com `nota_corte_imagem` (como era antes).
3. **Prioridade 3 — gerador editorial cartoon:** delega ao pipeline Flux/Ideogram/DALL-E. Pauta **nunca** é queimada.

## Quem é afetado automaticamente

Todos os agentes que usam o motor_publicador: Trindade Editorial (nacional, geopolitica, trends), agente_reciclador, agente_soberania, **agente_militar** (novo).

Agentes standalone que não usam motor_publicador (feminino, fantástico, eleições, temáticos) **não** foram alterados aqui — eles coletam direto via Brave Search e têm lógica própria; para ligar esses à mesma prioridade, seria outra rodada de fix.

## Validação

Rodei o coletor militar pós-fix: dict JSON salvo com `url_imagem_fonte` preenchido em 3 das 94 matérias (as 3 novas do ciclo; as 91 antigas foram coletadas antes do fix e não têm o campo). Exemplos de URL capturada: `https://cdn-media.tass.ru/width/1200_4ce85301/tass/m2/en/uploads/i/20260417/1471543.jpg` — URL real de foto editorial, não logo.

## Edge cases conhecidos

- Alguns sites devolvem **logo genérico** como og:image quando o artigo não tem imagem dedicada (TASS às vezes faz isso com `tass_logo_share_eng.png`). O Tribunal Visual Gemini vai reprovar (reconhece logo/marca) e cair em Prioridade 2. Pequeno desperdício de 1 chamada Gemini, sem prejuízo funcional.
- Trafilatura entrega HTML em `downloaded` (via `trafilatura.fetch_url`) ou em `r.text` (via requests fallback). Ambos são parseados pelo BeautifulSoup do `_extrair_og_image`.

## Backups

- `/root/motor_coletor.py.bak_20260417_1100`
- `/root/motor_publicador.py.bak_20260417_1100`

## How to apply

- **Para um agente standalone passar a usar este fluxo,** ele precisa migrar pro motor_coletor+motor_publicador (padrão Trindade). Ou replicar a lógica de `_extrair_og_image` no próprio fluxo de coleta e usar o mesmo campo `url_imagem_fonte` na hora de publicar.
- **Se o site respeita `og:image` mas retorna logos,** manter o Tribunal Visual — é ele quem rejeita logos.
- **Para melhorar a cobertura retroativa do banco militar/soberania/trindade:** apagar o banco JSON e recoletar do zero para preencher `url_imagem_fonte` em todas as pautas. Ou simplesmente aguardar alguns ciclos — novas pautas já entram com o campo.
