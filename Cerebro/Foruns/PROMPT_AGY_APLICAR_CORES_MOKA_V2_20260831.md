# 🎨 PROMPT — ANTIGRAVITY: aplicar a Spec de Cores v2 do Moka (direção B)

> Miguel: cole este prompt INTEIRO numa conversa do Antigravity Desktop.
> Ele já traz a spec do Claude embutida — não precisa anexar nada.

---

PROMPT (cole daqui pra baixo):

Você é o implementador de design do **Moka** (app de leitura com IA da casa O Cafezinho). O diretor de design (Claude) fechou a especificação de cores v2; sua missão é **aplicá-la com precisão de joalheiro** — é refinamento sutil, não redesign.

## ONDE ESTÁ TUDO (seu acesso)
- Repo: `/home/migueldorosario/ZCodeProject/moka-app` — branch **`obra/memoria`** (NÃO mexa na main; é a versão antiga em produção).
- Arquivos-alvo: `apps/web/src/app/globals.css` (tokens `--bg/--surface/--accent/--gold`, kit `--btn-*` v1.0 no fim do arquivo, `.capa-launch-btn`, `.capa-launch-ico` 48px r12, `.reader-big-btn`) e, só se precisar, `apps/web/src/components/Capa.tsx`/`Reader.tsx` para o véu radial/fundo fixed.
- **PROIBIDO: push/deploy** — quem revisa e publica no Ousadia é o ZCode (rito Ousadia → Espelho → Canônico). Retorno: tag `ousadia-memoria-nuvem-20260831`.
- Espec completa com as 3 direções: `Downloads/Antigravity Google/Cerebro/Foruns/SPEC_CLAUDE_CORES_MOKA_V2_20260831.md`.

## ⭐ APLIQUE A DIREÇÃO B — "AMANHECER AZUL" (recomendada pelo Claude e escolhida pelo Miguel)
*(se o Miguel te disser depois "aplica A" ou "aplica C", a spec das outras duas está no arquivo acima — mesma mecânica)*

1. **Fundo geral da capa:** degradê vertical `#f4f7fb` → `#e8eef7`, com `background-attachment: fixed` no desktop (não rola com o scroll). É a mudança-mãe — o degradê mora no AMBIENTE.
2. **Cards dos 6 módulos (`.capa-launch-btn`):** repouso degradê 180deg `#ffffff` 0% → `#f9fbfe` 92% → `#f4f8fd` 100% (o pé acusa o azul); hover → `#ffffff`→`#eff5fc` mantendo os -3px existentes. Borda: repouso `rgba(203,213,225,0.45)`, hover `rgba(30,64,175,0.4)`.
3. **Sombras dos cards (tingidas de safira, nunca preto):** repouso `0 1px 2px rgba(23,37,84,0.05), 0 3px 8px rgba(23,37,84,0.05)`; hover `0 6px 16px rgba(23,37,84,0.09), 0 12px 32px rgba(23,37,84,0.08)`.
4. **Caixinha do ícone (`.capa-launch-ico`):** degradê 135° `#eaf1fb` → `#dbeafe`; hover `#dbeafe` → `#c7dcfa`. Emoji fica como está (não recolore).
5. **Tipografia dos cards:** nome 17.5px/700 `#0f172a`; descrição 13px/400 `#475569` — e **REMOVER o `opacity: 0.72` atual da descrição** (opacidade sobre cor derivada dessatura).
6. **Cartões secundários (gratuito/chave, `.capa-path`):** `#ffffff` → `#fafcfe` (SEM o pé azul), borda `rgba(203,213,225,0.4)`; hover só a borda `rgba(30,64,175,0.3)` (não levanta).
7. **Botões-pílula do leitor (`.reader-big-btn`):** FORA do amanhecer — branco sólido, borda `rgba(203,213,225,0.5)`, hover fundo `#dbeafe` + texto `#172554`. Zero degradê dentro do leitor.
8. **Modo escuro:** fundo `#0b132b` → `#0a0f22`; card `#1c2541` → `#192138`; bordas repouso `rgba(51,65,85,0.7)` / hover `rgba(96,165,250,0.45)`; caixinha 135° `#1e293b` → `#233252`; sombras `0 2px 8px rgba(0,0,0,0.4)` / `0 8px 24px rgba(0,0,0,0.5)`.

## REGRAS DE ELEGÂNCIA (do diretor — inegociáveis)
1. **Um degradê por elemento**, Δ máximo ~4% de luminosidade entre as pontas — "se dá pra nomear as duas cores olhando, está forte demais". Nunca empilhar degradê em card + borda + sombra do mesmo elemento.
2. Sombras sempre tingidas de `#172554`; alfa total somado ≤ 0.17 no hover; contraste: nome ≥7:1 e descrição ≥4.5:1 contra o ponto mais escuro do degradê.
3. Hierarquia fixa: **6 cards > secundários > pílulas** — só os 6 cards têm degradê + elevação; os 6 são SEMPRE idênticos entre si (nenhum módulo ganha cor própria).

## ENTREGA
1. Só cores/sombras/degradês — layout, grid 3×2/2×3, tamanhos e interações permanecem.
2. `npx next build` (em `apps/web`) SEM erro.
3. Prints: capa desktop ~1366px e celular ~375px, nos DOIS temas (claro/escuro).
4. Liste o que mudou (arquivo → o quê) + como reverter.
5. Registre um adendo no fórum `Downloads/Antigravity Google/Cerebro/Foruns/forum_obra_moka_chefia_zm_20260830.md` (o que fez + prints referenciados; SEM valores de credencial em texto — regra da casa).

---
