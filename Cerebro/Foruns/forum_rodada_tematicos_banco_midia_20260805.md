# FÓRUM — Rodada visual/editorial dos temáticos + Banco de Mídia V4 plugado (05/08/2026)

**Data:** 2026-08-05 ~11:20-12:30 BRT · **Agente:** ZCode/Kimi K3 · **Gatilhos (Miguel, chat):** "destaques ficou feio em alguns temáticos — não precisa escrever 'destaques sobre trilhos', só deixar a matéria em cima; deixa pequenininho, laranjinha, como chapeuzinho sobre a foto — vale para todos" · "quem somos do Rio com imagem quebrada em cima; about do Rio e do Discover Brazil com texto em latim — tem que escrever, não esquece de botar o time" · "Descobrir Brazil tá maluco, texto que não é de turismo — aqui é SÓ turismo no Brasil" · "GSN: mais guerra do Irã pró-Irã, queda do Trump, Brasil em inglês (Lula pesquisas, vistos EUA, briga com a Argentina, anti-Milei anti-Trump); sempre uma pauta Lula com fotinha do Flickr/banco" · "vê se os temáticos têm acesso ao banco de mídia V4"

## 1. Destaques mini (6/6 no ar)

Títulos tipo "Destaques sobre Trilhos" (h2 sem CSS dedicado → grandão feio) viraram label mini `fv-mini`: **0.78rem, uppercase, cor `--accent` do site + barrinha** (trilhos laranja #d35400, GSN vinho #9e2f50, railpost vermelho…). Textos: PT "Destaques" / EN "Featured". Builds validados (ceara + GSN) antes do push.

## 2. Quem Somos / About (no ar)

- **Rio Carta** `/quem-somos/`: a "imagem quebrada em cima" era a `div.hero-image` vazia com fundo cinza (layout BlogPost sem heroImage). Agora tem hero real — panorama do Rio (Wikimedia, CC BY 4.0, Acediscovery) — e seção **"O time"** (sem inventar nomes: redação + colaboradores; base no texto verdadeiro já existente).
- **Discover Brazil** `/about/`: era o **Lorem ipsum do template Astro** + um bloco "Editor" fora do layout (estrutura quebrada). Reescrito em EN: portal SÓ de turismo no Brasil, grupo Cafezinho Media Group, seção "The team", hero Cataratas do Iguaçu (CC BY 3.0, Mayra Vazquez), créditos no rodapé do texto.

## 3. Trava editorial Discover Brazil: SÓ turismo

- Causa: feeds gerais (riotimes "brazil") vazavam notícia não-turística; contrato não tinha trava.
- `foco_local` reusado como **gate temático** (48 termos turismo+destinos BR, veto sem LLM) — mesmo mecanismo do foco local CE/RJ de madrugada. Diretriz registrada no contrato `discoverbrazil.md` (Regra-mãe).

## 4. GSN — pautas do editor

- 6 `brave_queries` novos: Iran war/Hormuz, Trump approval decline, Lula leads polls, US revokes visas Brazilian officials, Brazil×Argentina Milei tensions, Lula Global South diplomacy.
- **Diretriz 2026-08-05 no contrato `globalsouth.md`**: Irã sempre pró-Irã; queda do Trump; Brasil em inglês toda semana (pró-Brasil, anti-Milei, anti-Trump); "sempre uma pauta sobre o Lula" com foto do banco.

## 5. Banco de Mídia V4 → temáticos (a grande obra da rodada)

**Resposta ao Miguel: NÃO tinham acesso — agora têm.**
- Achados: acervo.db aponta chaves R2 `canonico/…` **que não existem no bucket** (quebrado); o **Banco Ouro** (`banco_midia_ouro_v3.db`, NYC) é o banco vivo: 661 mídias, chaves `ouro/…` existem 10/10.
- `banco_midia_sync.py` (cron seg 06:20): espelha NYC→local (paralelo, 24 workers). **666 mídias no espelho local (1,8 GB) — 99 fotos do Lula**, 95 Alckmin, 88 Haddad, 41 Moraes, 21 Trump…
- `nucleo_banco_midia.py` + **FASE 0 no `_buscar_hero`**: manchete com entidade do banco (Lula, Trump, Alckmin…) usa retrato oficial auditado ANTES de Wikimedia/cascata — passa pela mesma esteira (dedup hash → juiz visual → padronização 1200×675). Matcher 7/7 testes (inclui anti-"Lulau").

## 6. Pendências

- 52 linhas do acervo antigo com binário R2 quebrado — não sincronizáveis; cura = re-subir ou re-coletar (avaliar se vale; o Ouro cobre lideranças).
- GSN: próximas rodadas devem mostrar as pautas novas — observar o batch das 13:00.

**Memória técnica:** `Memorias/memoria_rodada_tematicos_banco_midia_20260805.md`
