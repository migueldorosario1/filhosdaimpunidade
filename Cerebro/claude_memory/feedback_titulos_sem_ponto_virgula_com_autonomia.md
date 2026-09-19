---
name: feedback-titulos-sem-ponto-virgula-com-autonomia
description: "Título Cafezinho NUNCA leva ponto e vírgula. Dois pontos permitidos com moderação (não em todo título). Autonomia: a cada ciclo Sentinela corrige títulos mal-estruturados de drafts E publicados, sem pedir permissão."
metadata:
  node_type: memory
  type: feedback
  author: "Claude Code (Anthropic, claude-opus-4-7)"
  written_at: 2026-07-23 03:25 BRT
  originSessionId: b3501857-e7d4-49f4-83bd-74804874c770
---

**⚠️ ATENÇÃO: memória escrita por Claude Code (Anthropic), NÃO por GLM/Ming (Zhipu AI).**

## Regra editorial (Miguel 2026-07-23 03:20 BRT)

**Título editorial do Cafezinho:**

1. **NUNCA usar ponto e vírgula (`;`).** Se draft chega com `;`, cortar após o `;` (fica só a primeira parte) ou reformular com conectivo natural.
2. **Dois pontos (`:`) — permitido com MODERAÇÃO.** Regra antiga proibia totalmente — Miguel revisou: pode usar de vez em quando quando REALMENTE fizer sentido. Não usar viciadamente como default.
3. **Título confuso, mal-estruturado ou com erro** — corrigir sem pedir. Miguel: *"você tem autonomia para corrigir isso. Título não pode ficar confuso ou errado"*.
4. **Autonomia a cada ciclo:** escanear títulos de drafts elegíveis + publicados nas últimas 2h. Se algum tem `;` ou está estranho, corrigir in-place.

**Why:** Miguel percebeu vários títulos mal-formatados no Cafezinho hoje. Exemplos que ele destacou:
- `"EUA bombardeiam Irã 12 noites seguidas; Trump ameaça infraestrutura"` — deveria terminar em "seguidas"
- `"PP, União Brasil, neutralidade"` — estrutura de vírgulas confusa (era pra ter dois pontos)

Sentinela estava sendo excessivamente conservador (nunca corrigir publicado) OU excessivamente restritivo (proibir dois pontos totalmente). Ambos os extremos são ruins.

## How to apply

### 1. No prompt do Sentinela
Nova seção **D4** em `~/ferramentas/sentinela/config/prompts.md` documenta:
- `;` proibido
- `:` permitido com moderação
- Autonomia pra corrigir a cada ciclo (drafts + publicados <2h)
- Método: `corrigir_grafia` pra draft, `editar_corpo_publicado` pra publicado (título é campo separado, respeita regra churn)

### 2. Padrão de correção
- **Ponto e vírgula:** cortar após o `;` OU trocar por conectivo (`,` `e` `—`) OU dois pontos se caber
- **Vírgula final confusa:** reformular usando dois pontos ou reescrever
- **"e" duplo confuso:** reescrever

### 3. Detecção automática
A cada ciclo Sentinela roda regex simples nos títulos:
- `;` em título → problema
- `\.\.\.` ou `…` em título → geralmente problema (reticências raras em títulos jornalísticos)
- Título >120 chars → provavelmente longo demais
- Título terminando em vírgula + fragmento → problema

### 4. Ordem de aplicação
1. Primeiro escanear drafts elegíveis (antes de publicar): se problema → aplicar `corrigir_grafia` E publicar
2. Depois auditar publicados últimas 2h: se problema → aplicar `editar_corpo_publicado` in-place (título é campo, muda sem tocar status)
3. NUNCA rebaixar publish → draft (regra churn permanece)

## Casos fundadores 2026-07-23 03:20 BRT

- **262607**: `"EUA bombardeiam Irã 12 noites seguidas; Trump ameaça infraestrutura"` → `"EUA bombardeiam Irã pela 12ª noite consecutiva"` (Claude Code cortou ponto e vírgula in-place)
- **262548**: `"Mega-Sena não tem ganhador; prêmio sobe para R$ 62 milhões"` → `"Mega-Sena acumula: prêmio sobe para R$ 62 milhões"` (Claude Code trocou `;` por `:`, agora permitido com moderação)

## Regra correlata

**Regra antiga "dois pontos proibidos" está SUPERADA.** Se você achar essa regra antiga em outros lugares do prompt/memória, ignore — vale a regra nova deste feedback.

## Relacionadas

- [[feedback-diretrizes-editoriais-21jul]] — R1-R4 (rate limit, esporte siglas, nome próprio desconhecido, partido MAIÚSCULO)
- [[feedback-nunca-churn-publish-draft-seo]] — não rebaixar publish→draft (regra permanece)
- Prompt Sentinela seção D4 em `~/ferramentas/sentinela/config/prompts.md`

## Assinatura

Registro escrito por Claude Code (Anthropic, `claude-opus-4-7`), sessão `CLAUDE-CHEFE-ECOSSISTEMA-20260719-1020`, 2026-07-23 03:25 BRT.
