# 🎨 MOKA — Spec de Refinamento de Cores v2 ("degradês sutis, mais sofisticado")
> Diretor de design: CLAUDE (resposta ao prompt do ZM, 31/08 ~21:3x). Base: código real (globals.css @ obra/memoria). Recomendação: **B — Amanhecer Azul**.

## DIREÇÃO A — "Porcelana e Ouro"
Livraria de aeroporto: quase branco, luxo no fio dourado só no hover.
- Card repouso: 180deg #ffffff → #fbfcfe; hover → #f8fafd
- Borda: repouso rgba(203,213,225,0.5); hover rgba(217,119,6,0.45) (dourado #d97706 a 45%)
- Sombras: repouso 0 1px 2px rgba(15,23,42,0.04), 0 2px 6px rgba(15,23,42,0.04); hover 0 4px 12px rgba(15,23,42,0.07), 0 10px 28px rgba(15,23,42,0.08)
- Caixinha 48px: sólido #f0f4f9 c/ borda interna rgba(30,64,175,0.08); hover #dbeafe. (Ícones de linha futuros: #1e40af, hover #172554)
- Tipografia: nome 17.5px/700 #0f172a; descrição 13px/400 #475569 (REMOVER opacity 0.72)
- Fundo geral NÃO muda. Secundários: branco sólido, borda rgba(203,213,225,0.4), hover borda rgba(217,119,6,0.35) sem elevar. Pílulas leitor: branco, borda rgba(203,213,225,0.5), hover #dbeafe/#172554, ZERO degradê
- Dark: card #16161a→#18181d; bordas rgba(46,46,54,0.8)/rgba(245,158,11,0.4); caixinha #0a0a0c hover #1e293b; sombras 0 2px 5px rgba(0,0,0,0.4)/0 6px 18px rgba(0,0,0,0.55)

## DIREÇÃO B — "AMANHECER AZUL" ⭐ recomendada
Degradê no AMBIENTE, cards louça branca. "Nenhum usuário consegue apontar o que mudou."
- Fundo geral: 180deg #f4f7fb → #e8eef7, background-attachment: fixed (desktop)
- Card repouso: 180deg #ffffff → #f9fbfe 92% → #f4f8fd 100% (pé azul); hover → #eff5fc
- Borda: repouso rgba(203,213,225,0.45); hover rgba(30,64,175,0.4)
- Sombras (tingidas safira): repouso 0 1px 2px rgba(23,37,84,0.05), 0 3px 8px rgba(23,37,84,0.05); hover 0 6px 16px rgba(23,37,84,0.09), 0 12px 32px rgba(23,37,84,0.08)
- Caixinha: 135° #eaf1fb → #dbeafe; hover #dbeafe → #c7dcfa. (Ícones linha: #1e40af)
- Tipografia: idem A (17.5/700 #0f172a; 13/400 #475569)
- Secundários: #ffffff → #fafcfe (sem pé azul), borda rgba(203,213,225,0.4), hover borda rgba(30,64,175,0.3)
- Pílulas leitor: FORA do amanhecer — branco, borda rgba(203,213,225,0.5), hover #dbeafe/#172554
- Dark: fundo #0b132b → #0a0f22; card #1c2541 → #192138; bordas rgba(51,65,85,0.7)/rgba(96,165,250,0.45); caixinha 135° #1e293b → #233252; sombras 0 2px 8px rgba(0,0,0,0.4)/0 8px 24px rgba(0,0,0,0.5)

## DIREÇÃO C — "Safira e Porcelana"
A joia: caixinha cobalto sólida; resto mais quieto.
- Card: 135° #ffffff → #fafbfd; hover → #f5f8fc
- Borda: rgba(226,232,240,0.9); hover rgba(23,37,84,0.35) (safira, mais grave)
- Sombras: 0 1px 3px rgba(15,23,42,0.05), 0 2px 8px rgba(15,23,42,0.04); hover 0 5px 14px rgba(23,37,84,0.10), 0 12px 30px rgba(23,37,84,0.08)
- Caixinha: 135° #1e40af → #172554 (receita do primary v1.0); hover #2563eb → #1d4ed8; ícones linha #ffffff
- Fundo: #f0f4f9 + véu radial fixo atrás do MOKA: radial-gradient(ellipse 720px 320px at 50% 120px, rgba(219,234,254,0.5), transparent 70%)
- Secundários: branco SEM caixinha azul (joia exclusiva dos 6); hover borda rgba(23,37,84,0.25)
- Pílulas: branco; ATIVO (menu aberto) = receita da caixinha 135° #1e40af→#172554 texto branco
- Dark: card 135° #16161a→#141419; caixinha #2563eb→#1d4ed8 ícone branco; halo rgba(30,58,138,0.25)

## REGRAS DE ELEGÂNCIA (obrigatórias na implementação)
1. Um degradê por elemento; Δ máx ~4% de luminosidade entre pontas; nunca empilhar degradê em card+borda+sombra.
2. Sombras sempre tingidas #172554 (nunca preto puro), alfa total ≤0.17 no hover; contraste: nome ≥7:1, descrição ≥4.5:1 contra o ponto mais escuro do degradê.
3. Hierarquia fixa: 6 cards > secundários > pílulas. Só os 6 cards têm degradê+elevação; leitor zero degradê; os 6 cards SEMPRE idênticos entre si.

Restrições: módulos idênticos ✔ · sem ilustração ✔ · emojis mantidos (caixinha muda; emoji não recolore — cores de ícone previstas p/ migração futura) ✔
