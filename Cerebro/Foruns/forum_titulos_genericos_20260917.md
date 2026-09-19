# Fórum — Títulos sem nome próprio desconhecido (regra genéricos) · 17/09/2026

> Tema: títulos de posts do Cafezinho com nome próprio que o leitor comum não reconhece.
> Ordem do Miguel 17/09/2026 ~10:4x (casos First Resources e Polilaminina). Par da Memória:
> `Memorias/memoria_titulos_genericos_20260917.md`.

## O que aconteceu

O Miguel flagrou dois títulos publicados no ar com nome próprio desconhecido:

| Post | Título antigo (❌) | Título novo (✅) | Status |
|---|---|---|---|
| 271620 | Fogo cerca orangotangos em concessão da First Resources | Fogo cerca orangotangos em plantação de óleo de palma na Indonésia | corrigido, no ar, 301 preservado |
| 271552 | Polilaminina começa teste clínico com cinco pacientes em SP | Cinco pacientes em SP testam medicamento brasileiro para lesão medular | corrigido, no ar, 301 preservado |

A regra dele, quase literal: título não pode ter nome próprio desconhecido, nem sigla, nem nome
próprio em língua estrangeira. Só marca ultra conhecida (Coca-Cola, McDonald's) ou figura de fama
nacional. O que não é conhecido entra pelo genérico; o nome específico fica no corpo.

## Diagnóstico da cadeia editorial (quem deixou passar)

- Posts criados pela esteira V4.1 (redator), publicados pelo Tampão (`_agente_origem=tampao_v1`), autor Redação (5470).
- O **advisor preventivo** do NYC (`agente_auditor_titulos_gpt.py --modo advisor`, 9 regras canônicas) JÁ TINHA a regra
  (nº 9: nome próprio não reconhecido não entra) — mas **ninguém o chama no fluxo** e a config dele aponta
  `advisor_author_id=5786`, enquanto a esteira publica como 5470. Nunca roda sobre os rascunhos de agente.
- O **auditor pós-publicação** (cron 10 min) é conservador de propósito: só corrige contradição título×lide
  ou placeholder — por isso deu "ok" para os dois títulos (verificado no jsonl de hoje).

## O que foi consertado (4 pontos + aviso)

1. Posts corrigidos no WP (override editorial, slug novo, `_wp_old_slug` automático, `rocket_clean_post`).
   Provas: 200 + `<title>` novo no ar; URLs antigas 301 → novas (`x-redirect-by: WordPress`).
2. **Redator V4.1 (a fonte)** — `nyc:/root/v4_labs/codigo/v4_vertical_redactor_runtime.py` (`_prompt`):
   régua plantada (sigla obscura + nome próprio desconhecido → genérico; exemplos inclusos). Commit `c6dfd51`
   no repo v4_labs (amend para documentar que incluiu também mudanças CL ZM_HTML_ESCAPE/ZM_PROMPT5 que estavam
   sem commit no working tree — nada perdido). Backup `.bak_pre_titulo_generico_20260917`.
3. **Auditor pós-publicação (rede de segurança)** — `nyc:/root/agente_auditor_titulos_gpt.py`
   (`_auditor_system_prompt`): agora também corrige título com nome próprio/sigla irreconhecível, gerando
   genérico com fatos do próprio lide (respeita o conservadorismo: sem conhecimento externo). Backup datado idem.
4. **Manual de estilo** — regra 8.7 do `Estilo/MANUAL_AGENTES_AUTONOMOS_CAFEZINHO_COMPLETO_20260914.md` estendida
   (empresa/produto/substância/termo estrangeiro + casos-escola de hoje) e item 5 do
   `Estilo/BLOCO_PRONTO_REGRA_TITULO_EMU6.md` (o bolo pronto verbatim injetado em quem escreve/revisa).
5. **Aviso na ponte** (`Foruns/ponte_laura_completa/de_dell.md`, `REGRA-TITULO-GENERICOS-20260917`): CL/AGY/R2
   devem estender a checagem "titulo sem sigla" → "sem sigla E sem nome próprio desconhecido" no `_cafezinho_txt_check`.

## O que falta / pendências

- Confirmar na prática que o auditor pós-publicação passa a puxar esses títulos sozinho (próximas rodadas do cron de 10 min).
- Advisor preventivo segue FORA do fluxo e apontando autor 5786 ≠ 5470 — ligá-lo é decisão editorial maior (não feito sem ordem).
- Espelho cafezinho.news segue trancado (401) — quando destrancar, conferir títulos lá.

## O que preciso de você (Miguel)

Nada urgente. Se quiser, o próximo passo natural é ligar o advisor preventivo no fluxo V4.1 (mudar
`advisor_author_id` para 5470 e chamar após a escrita do rascunho) — é mudança de esteira, só com seu "vai".

— ZCode/GLM-5.3 · 17/09/2026 ~11:0x BRT
