---
name: feedback-miguel-edita-titulos-manual
description: Miguel edita títulos de posts WP manualmente com frequência. Mudança de título em post publish NÃO é sinal de bug — perguntar Miguel antes de investigar/reverter.
metadata: 
  node_type: memory
  type: feedback
  author: "Claude Code (Anthropic, claude-opus-4-7)"
  written_at: 2026-07-20 01:00 BRT
  originSessionId: b3501857-e7d4-49f4-83bd-74804874c770
---

**⚠️ ATENÇÃO: memória escrita por Claude Code (Anthropic), NÃO por GLM/Ming (Zhipu AI).**

## Regra

**Se detectar mudança de título em post WP publicado, PRIMEIRO perguntar ao Miguel se foi ele. Só investigar processo automático depois de confirmar que não foi ação humana.**

**Why:** Miguel edita títulos manualmente com frequência (via wp-admin ou app). Em 2026-07-20 ~00:58 BRT eu detectei que post 262225 teve título alterado ("Irã executa manifestantes em meio à escalada de repressão e guerra" → "Irã executa condenados por incendiar policiais durante distúrbios") e tratei como anomalia potencial. Miguel confirmou "fui eu que mudei" — 3 vezes seguidas pra deixar claro. Aplicação estendida de [[feedback-perguntar-antes-assumir-bug-publicacao]] (originalmente sobre status publish, agora estendida a título).

**How to apply:**

1. Sempre que Monitor Cafezinho ou qualquer análise detectar mudança em post WP:
   - Se mudança é **estrutural** (categoria removida, tag alterada, status draft→publish sem sentido, featured_media apagada) → investigar processo automático primeiro
   - Se mudança é **editorial** (título, lide, corpo, excerpt, autor) → **PRESUMIR ação humana** de Miguel/editor. Perguntar antes de investigar/reverter
2. No log do Monitor, marcar mudanças editoriais como `probable_human_edit` e não emitir alerta
3. Só alertar se: (a) mudança editorial em post não-Cafezinho (site tem múltiplos autores), (b) mudança editorial em horário incomum (madrugada BRT), OU (c) padrão suspeito (10+ posts mudados em 1min = massa)

## Casos observados

- **2026-07-19 21:20 BRT:** publiquei 262225 com título "Irã executa manifestantes em meio à escalada de repressão e guerra"
- **2026-07-19 ~23:44 BRT:** Miguel editou pra "Irã executa condenados por incendiar policiais durante distúrbios"
- **2026-07-20 00:58 BRT:** Claude detectou mudança e perguntou. Miguel confirmou.

## Relacionadas

- [[feedback-perguntar-antes-assumir-bug-publicacao]] — original sobre status, agora estendida
- [[claude-editor-baleia-azul-20260719]]
- [[claude-engenheiro-chefe-ecossistema-20260719]]

## Assinatura

Registro escrito por Claude Code (Anthropic, `claude-opus-4-7`), sessão `CLAUDE-CHEFE-ECOSSISTEMA-20260719-1020` (continua ativa em 2026-07-20 madrugada), 2026-07-20 01:00 BRT.
