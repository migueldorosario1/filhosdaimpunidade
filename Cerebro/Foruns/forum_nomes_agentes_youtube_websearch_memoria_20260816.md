# Fórum — Agentes YouTube: NOMES SEM ERRO (websearch + memória)

**Data:** 16/08/2026 ~22:50-23:05 BRT · **Autor:** ZCode/Qwen 3.8 · **Origem:** ordem do Miguel (voz/chat):
> "personagens, tese, tudo isso também está sendo visto pelos agentes youtube. não pode errar os nomes. por isso tem que ter websearch e memoria."

## Decisão

Os rascunhos do agente YouTube nacional passam, a partir de hoje, por uma camada de
**verificação de nomes com websearch real + memória persistente**, ANTES da redação.
Transcrição automática erra grafia de pessoas com frequência (caso-escola do bug #31:
"Nunes Marques" virando "Nunes Max"); o prompt antigo dependia só do conhecimento do
LLM redator. Agora:

1. **MEMÓRIA** — `agent_data/personagens_youtube.json`: banco de nomes canônicos +
   aliases. Acerto = custo zero. Auto-alimentada: todo nome verificado na web entra
   no banco (inclusive a grafia errada da transcrição, como alias — da próxima vez
   acerta direto). Seed inicial: **81 personagens** (curadoria prioritários+vilões,
   titulares dos 40 canais, pessoal da casa TV Fórum, autoridades que transcrição
   erra muito).
2. **WEBSEARCH** — Brave API (chave espelhada nos dois cofres) com fallback
   DuckDuckGo, reusando `nucleo_tematico/busca.py`. Teto de 8 buscas por rascunho.
3. **VEREDITO LLM** (tier coleta, barato): dossiê de resultados → confirmado /
   duvidoso / inexistente + nome canônico + cargo.
4. **Redação com dossiê**: confirmado → usar grafia exata; duvidoso/sem busca →
   omitir o nome (referência genérica). Sem dossiê (falha) → vale a regra
   tradicional do bug #31. Camada 100% fail-soft.
5. **Auditoria visível**: dossiê gravado na meta WP `cafezinho_nomes_check`
   (mu-plugin instalado no canônico) + arquivo local
   `agent_data/v4_cafezinho_youtube/nomes_<video_id>.json`. Os Loops Miguel/Laura
   veem o que foi checado ao revisar o draft.

## Arquivos tocados (com backup)

| Arquivo | Ação |
|---|---|
| `Projeto Cafezinho Agentes/agentes_cafezinho/verifica_nomes.py` | NOVO — módulo da camada (memória+websearch+veredito; `--selftest`) |
| `agent_data/personagens_youtube.json` | NOVO — memória (81 personagens; `.bak` automático a cada escrita) |
| `Projeto Cafezinho Agentes/agentes_cafezinho/youtube_cafezinho.py` | integrado (import, dossiê em `processar`, bloco fact-check em `redigir`, meta+auditoria em publicar/atualizar); backup `youtube_cafezinho.py.bak_pre_verifica_nomes_20260816` |
| canônico `wp-content/mu-plugins/cafezinho-nomes-check.php` | NOVO — registra a meta `cafezinho_nomes_check` (php -l OK) |

## Incidente ativo corrigido na mesma sessão

Conta **Kimi paygo SUSPENSA** (HTTP 429) derrubava a confirmação LLM da edição do
Jornal da Fórum / Fórum Onze e Meia (era Kimi-só). Corrigido: cascata
DeepSeek→Kimi (`_chat_json_cascata`), mesma lógica do curador. Detalhes + 2 achados
menores (yt-dlp fallback sem binário no cron; rajada bot_check do iProyal às 22-23h
que impede a coleta RSS) em
`monitoramento_horario/bugs_encontrados/yt_patrulha_agente_youtube_20260816_2258.md`.

## Provas

- Selftest: Lula (memória), "Nunes Max" → alias → Kássio Nunes Marques (memória),
  Aaron Maté (memoria/canais) — todos confirmados sem websearch.
- Websearch real: "Nima Alkhorshid" → confirmado como **Nima Rostami Alkhorshid**
  (com contexto Dialogue Works) e gravado na memória (79→80).
- Integração com a análise REAL do draft 266153 (TV Fórum/Felipe Pena): 9 nomes,
  6 de memória, 2 confirmados via websearch (Felipe Pena, Eduardo Cunha — com
  cargos), 1 duvidoso (Richarlison, busca vazia → redação omite). Nomes compostos
  do campo vilao agora são divididos.

## Estado da missão / próximos passos

- ✅ Camada no ar para o agente nacional (todas as rodadas: --rodada, --jornal, --forum11).
- ✅ Meta registradada no canônico; primeiro draft com dossiê sai na próxima rodada que transcrever.
- ⏳ GSN V2 (NYC) recebe a MESMA camada em seguida (codebase separada; próximo toque).
- ⏳ Se a conta Kimi paygo seguir suspensa, a cascata opera só com DeepSeek (sem perda).
- O agente YouTube dos temáticos segue DESATIVADO (03/08) — quando religar, herda a camada.

**O que preciso de você (Miguel):** nada. O painel `/v6/youtube` segue sendo o seu
instrumento de gestão de canais; nomes errados agora têm duas camadas de defesa
antes do texto e o dossiê fica visível na revisão dos Loops.
