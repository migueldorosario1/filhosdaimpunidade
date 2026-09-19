---
name: Pendências editoriais 2026-04-17 (turismo + master_trends parágrafos)
description: Dois problemas editoriais diagnosticados em 17/04 mas ainda NÃO aplicados — aguardando autorização do Miguel.
type: project
originSessionId: b8d23953-06f2-4699-9a68-275c279163e9
---
Em 2026-04-17 o Miguel apontou dois problemas editoriais que foram diagnosticados mas os fixes ainda não rodaram:

**1. Agente Turismo Embratur — prompt promocional e Title Case americano**
- Arquivo: `/root/agente_turismo_embratur.py` (servidor tem versão 12/04, local 17/04 05:41 tem ajustes). Titulos saindo no estilo "O Paraíso das Águas: Descubra as Cachoeiras Mais Deslumbrantes!" (posts 235761, 235747, 235770, 235784 do dia 17/04).
- Causa: o próprio prompt sistema pede "otimista, bem escrita e chamativa", o user prompt pede "TÍTULO CHAMATIVO" e "imagem realista e deslumbrante" — adjetivos vagos vazam pro output. Além disso o agente NÃO aplica `titulo_utils.corrigir_capitalizacao_titulo` na saída (o `agente_youtube.py` aplica).
- Fix proposto (NÃO aplicado): reescrever system+user prompt seguindo CLAUDE.md ([Sujeito]+[Verbo Forte]+[Consequência], zero adjetivos vagos, sentence case PT-BR), com exemplos do padrão jornalístico vs clickbait. Importar e aplicar `corrigir_capitalizacao_titulo` antes de postar.

**2. Master Trends — parágrafos de 1 frase**
- Post 235789 ("Pesquisa desvenda onde o rio Colorado sumiu...") teve os 4 primeiros parágrafos com 1 única frase cada. A regra CLAUDE.md exige 2-3 frases por parágrafo (padrão FT).
- Causa: o prompt do Redator da Trindade Editorial (`agente_master_trends_v9.py` ou prompt central em `motor_publicador.py`) não força a regra de 2 frases mínimas. Apenas o `agente_youtube.py` tem a regra explícita.
- Fix proposto (NÃO aplicado): adicionar no prompt do Redator: *"Padrão FT — cada parágrafo DEVE ter 2 a 3 frases curtas. Proibido parágrafo de frase única, EXCETO no primeiro parágrafo quando funcionar como lead seco."*

**Why:** Miguel interrompeu com "espera um pouco" / "vou te mostrar a imagem" e a conversa virou pro fix do Tribunal Visual (que ele autorizou e foi aplicado). Esses dois itens ficaram em pendência pra próxima rodada.

**How to apply:** Antes de rodar qualquer um desses fixes, checar mtime local vs servidor — o Antigravity também edita esses arquivos. E pedir confirmação explícita antes do deploy porque mudanças de prompt editorial são sensíveis.
