---
name: feedback-charges-sem-texto-dentro-flux
description: "Charges/ilustrações editoriais Cafezinho NUNCA têm texto dentro da imagem (Flux/Ideogram/DALL-E/Wan) — quase sempre trunca/mal grafa. Texto vai EMBAIXO da charge no HTML do post (WP caption). Fix upstream em gerador_imagem_editorial.py: função `_prompt_flux_com_texto_permitido` revogada, agora REFORÇA anti-texto. Auditar funções que 'permitem'/'relaxam' regras editoriais estabelecidas."
metadata: 
  node_type: memory
  type: feedback
  author: "Claude Code (Anthropic, claude-opus-4-7)"
  written_at: 2026-07-24 12:10 BRT
  originSessionId: b3501857-e7d4-49f4-83bd-74804874c770
---

## Regra

**Charges e ilustrações editoriais do Cafezinho NUNCA têm texto DENTRO da imagem.** Vale para:
- Flux Pro (fal.ai) — principal gerador
- Ideogram
- DALL-E
- Wan/Qwen
- Qualquer gerador futuro (Midjourney, Stable Diffusion, Imagen, etc.)

Texto (palavras, legendas, banners, logos com escrita, watermarks, subtítulos, dizeres, siglas) vai **EMBAIXO da charge**, no HTML do post — geralmente via WP media `caption` — nunca dentro da arte.

**Why:** Miguel 2026-07-24 12:00 BRT: *"O combinado era que teríamos texto alocado embaixo da charge, texto não gráfico, para que não houvesse risco de texto truncado. Se não for possível, tudo bem, sem texto nenhum. Mas é importante que não tenha jamais texto dentro da imagem porque em geral trunca."* Modelos de imagem via IA (mesmo Flux Pro que é bom em texto) truncam palavras, misturam caracteres, fazem grafia errada — quebra a estética profissional do portal.

**How to apply:**

### 1. Upstream (gerador de imagem editorial)
`/root/gerador_imagem_editorial.py` (NYC) — função `_prompt_flux_com_texto_permitido()` REVOGADA 24/07/2026 (fix Claude Code 11:52 BRT). Antes REMOVIA `ABSOLUTELY NO TEXT` do prompt e adicionava permissão explícita → toda charge Flux vinha COM texto. Agora só REFORÇA anti-texto com lista longa (NO letters/words/captions/signs/banners/writing/typography/logos/watermarks/subtitles + "illegible abstract marks only. Pure visual composition — like a wordless political cartoon"). Backup `.bak_pre_claude_notext_20260724_1150` SHA-256 `2f18c2a0...c89c`.

Prompt Cafezinho editorial (system prompt, linhas 76-101 do gerador) já tinha regras anti-texto em cada estilo (`ABSOLUTELY NO TEXT, NO WORDS, NO LETTERS`) — problema era a manipulação POSTERIOR na função tóxica.

### 2. Downstream (posts publicados com imagem bugada)
Ao detectar charge com texto dentro em post publicado:
1. Regenerar imagem via `generate_editorial_image()` no NYC (gerador local no espelho `Projeto Cafezinho Agentes/root/` pode estar defasado — 561 vs 629 linhas)
2. Upload nova imagem via `POST /wp-json/wp/v2/media` com autenticação Basic (Redator/senha)
3. Trocar `featured_media` do post via `POST /wp-json/wp/v2/posts/{id}` preservando `status=publish` (CHURN OK)
4. Atualizar `alt`, `title`, `caption` da nova mídia

Caso fundador 24/07: 262721 (Lula/Flávio/PP/União) — imagem original tinha texto truncado (identificada Miguel), regenerada e trocada in-place. Media velha 262722 → nova 262764.

### 3. Auditoria contínua
Se identificar próxima aparição de texto dentro de imagem gerada por outro modelo (Ideogram, DALL-E, Wan/Qwen) — auditar se cada `_chamar_*` recebe prompt SEM manipulação anti-anti-texto:
- DALL-E (linha 409 do gerador NYC) já adiciona "No text, no letters, no words in the image." ao próprio prompt — OK
- Ideogram, Wan/Qwen: verificar não passam por função similar à revogada

## Padrão de vigilância

**Bandeira vermelha:** função em pipeline editorial com nome contendo "permitido", "allow", "enable", "unlock", "relaxed", "loose" — sempre auditar mudanças que RELAXAM regras editoriais estabelecidas. Se um agente/dev adicionou permissão pra algo proibido, quase sempre é regressão.

## Erro que precisa ser evitado

Deixar charge com texto dentro chegar ao ar. Miguel identifica na hora (posts recentes na home), fica com estética ruim.

## Relacionadas

- [[feedback-protocolo-memoria-bugs-ler-antes-agir]] — protocolo de correção 3 camadas
- Manual bugs: entrada #26 (`texto_dentro_charge_flux`) em `Outros/manual_de_bugs.md`
- Nodo canônico: linha `texto_dentro_charge_flux` em `CEREBRO_NODE_BUGS_SOLUCOES.md`
- [[project-kimi-bugs-upstream-v4-fechados-20260724]] — precedente de fix upstream em agente_controlado.py

## Assinatura

Registro escrito por Claude Code (Anthropic, `claude-opus-4-7`), sessão `CLAUDE-CHEFE-ECOSSISTEMA-20260719-1020`, 2026-07-24 12:10 BRT.
