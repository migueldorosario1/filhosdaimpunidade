# Fórum — EMU-8: título genérico e simples (nome próprio desconhecido não abre título) — caso 268998

**Data:** 04/09/2026 ~18h BRT · **Agente:** ZCode/GLM-5.3 (Dell) · **Origem:** ordem do Miguel no chat com o link do post + «titulo com muito nome proprio desconhecido. titulos tem que ser maiss genericos e simples»

## O que aconteceu

O Miguel rejeitou o título do post **268998** (publicado 04/09 14:48, autor WP 5470 = redator V4.1, editoria cultura): «Janmashtami celebra Krishna com lição para agir sob incerteza» — dois nomes próprios que o leitor brasileiro comum não decodifica (nome da festa hindu + divindade). Mesma família de gap dos casos EMU-1 (sigla "OCS"), EMU-2 (sobrenome "Villatoro") e Kast 268457 ("cárcere vitrina"): o autor 5470 segue sendo o furo da auditoria de títulos.

## Decisões

1. **Título corrigido in place** → «**Festa hindu celebra nascimento de divindade com lição sobre agir sob incerteza**» (79c). **Slug preservado** (a URL colada pelo Miguel continua válida). Provas: `<title>` + `og:title` + `<h1>` na página do post e na home (`?v=2`), cache Rocket purgado via `wp eval 'rocket_clean_domain(); rocket_clean_minify();'`. Backup do título antigo: `Backups/posts_editados/268998_titulo_pre_emu8_20260904.md` (com rollback de 1 comando).
2. **EMU-8 no MANUAL_DE_ESTILO_UNIFICADO.md**: checklist canônico de títulos 8→**9 regras** (nova regra 9) + registro datado na lista de emendas (apêndice I).
3. **EMU-8 no MANUAL_DE_ESCRITA_PORTAL.md** (seção 8 — estrutura do texto) e **espelhada no NYC** em `/root/v4_labs/dados/MANUAL_DE_ESCRITA_PORTAL.md` — md5 `aaae40683deb8ce9e52592fb73ce71e3` idêntico nos dois lados, backup `.bak_pre_emu8_20260904`. Este é o arquivo que o `v41_ciclo.py` (linha 587) injeta no briefing do redator V4.1 ⇒ **a regra nasce no ponto onde o título é escrito** (mesmo caminho do bolo EMU-6 de 03/09).

## A regra (EMU-8, redação curta)

Nome próprio que o leitor comum não reconhece — festa religiosa específica, divindade, texto sagrado, personagem obscuro — **não entra no título**; entra o genérico ("festa hindu", "divindade", "texto sagrado"). O nome batizado aparece no corpo, decodificado na 1ª menção. Estende EMU-2 (cargo em vez de sobrenome) e EMU-1 (sigla não consagrada): o título conversa com quem ainda não conhece o assunto.

## Estado / o que falta / o que preciso de você (Miguel)

- **Pronto:** post corrigido e provado; EMU-8 nos 2 manuais; espelho NYC provado por md5.
- **Falta:** R1/R2 (Tencent) receberão a EMU-8 na próxima atualização do bolo de diretrizes (o bolo atual é o EMU-6 de 03/09 — não mexi nos prompts dos revisores nesta sessão). Auditor advisor de títulos segue cobrindo só autor 5786 (gap 5470 conhecido).
- **Do Miguel:** nada obrigatório — se quiser, varredura de títulos recentes do 5470 atrás de outros casos (não fiz: só 1 post apontado).

---

## §ADENDO 1 — CORREÇÃO ESTRUTURAL (ordem Miguel 04/09 ~18:1x: "correção estrutural")

O gap de enforcement foi FECHADO em 3 camadas na mesma hora:

1. **Auditor de títulos NYC** (`/root/agente_auditor_titulos_gpt.py`, backup `.bak_pre_emu8_20260904`):
   - Régua do prompt 7 → **9 regras** (8 = cargo EMU-2; 9 = genérico EMU-8) + schema `regra_falha` 1-9.
   - `wp_get_advisor_posts()` ganhou `incluir_publicados` (status draft,pending,publish) — autores que publicam direto (5470/5801) agora são avaliados também pós-publicação.
   - Snapshot vivo **por autor** (`advisor_pending_5470.jsonl`, `advisor_pending_5801.jsonl`) — rodadas não se sobrescrevem; relatório diário lê todos via glob.
   - **Crons novos defasados** (backup `crontab.bak_pre_emu8_advisor_20260904`): `7,37` → autor 5470 · `17,47` → autor 5801 (flocks próprios, janela 6h, `--incluir-publicados`).
   - **Prova E2E da régua:** o título VELHO «Janmashtami celebra Krishna…» → veredito `ajustar` (regra 8/9), sugestão «Festa hindu celebra lição sobre agir em tempos de incerteza» — a régua pega exatamente a família do caso. Custo por título ≈ US$ 0,00014 (gpt-4o-mini, hardstop US$ 2/dia compartilhado).
2. **R2 Tencent** (`~/dsn_revisor2/dsn_revisor2.py`, backup `.bak_pre_emu8_20260904`, py_compile OK): bolo EMU-1+2+6 → **EMU-1+2+6+8** — item (5) PROIBIDO ganha «nome próprio que o leitor não conhece → entra o genérico»; docstring da régua idem.
3. **Varredura retroativa** (janela 6h, autor 5470): 13 posts avaliados, 2 publicados corrigidos in place (269012: 93→71c · 269007: 97→62c; slugs preservados, provas front, Rocket purgado; backup+rollback em `Backups/posts_editados/varredura_emu8_5470_20260904.md`). 268986/268998 = falso positivo do mini (ficaram).

**⚠️ Anti-colisão §112 (sessão YouTube paralela ativa):** o advisor apontou 6 títulos >80c nos posts do autor 5801 de hoje (269033/34/38/40/42/44 — as matérias que a sessão AGENTE YOUTUBE está publicando agora). NÃO foram tocados — sugestões vivas no `advisor_pending_5801.jsonl` para a CL/sessão YouTube aplicarem. **Ainda por lá: 269033 e 269034 têm título IDÊNTICO (duplicata feijão-carioca) — dedup pendente da sessão YouTube.**

**Estado final:** EMU-8 agora vive em 5 pontos — manual unificado (regra 9) · manual portal (NYC, briefing do redator) · R2 tencent (bolo do revisor) · auditor advisor (régua 9 regras, 3 autores: 5786+5470+5801) · memória ZM. Restam como advisory: aplicação das sugestões segue decisão CL/humano (política da casa: robô sugere, não edita).
