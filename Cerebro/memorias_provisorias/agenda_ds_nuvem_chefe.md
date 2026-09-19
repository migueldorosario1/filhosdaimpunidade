# 📋 AGENDA — DS Nuvem Chefe (DS-N Chefe) — os 2 loops

> Criada na FASE 0 (ordem Miguel 30/08, refs DSC-028/029/031/032). "SNFF" não existe (erro de ditado, DSC-031).
> Manter atualizada pela ronda (Loop B). Log local na Tencent: `~/ds_nuvem_chefe/`.

## LOOP A · ESCUTA (quase contínua, custo zero)
- **O quê:** long polling `getUpdates timeout=25` (serviço `ds-nuvem-chefe-escuta`, Tencent, systemd Restart=always). Consumidor ÚNICO do @dscelular_bot.
- **Ao receber msg do Miguel:** resposta flash em segundos (DeepSeek + CONTEXTO_MINI), assinada `— DS Nuvem Chefe (DS-N Chefe) · AAAAMMDD HH:MM:SS BRT`; registro no INBOX marcado `RESPONDIDO_FLASH lat=Xs`; chave `sk-` → cofre (nunca ponte); áudio → guardado + INBOX.
- **Ociosa:** silêncio absoluto (heartbeat local 1×/h). **Erro:** backoff 30s.
- **Consumo:** 1 linha/dia em `~/ds_nuvem_chefe/consumo_tokens.log` (ronda copia pro relatório diário).
- **Ouvido (30/08, ordem "whisper"):** áudios (até 5 min) → Whisper local faster-whisper large-v3-turbo int8 (custo zero, ~0.5× tempo do áudio) → fallback AssemblyAI (~US$ 0.37/h). Ack imediato + transcrição + resposta flash no INBOX como TRANSCRITO.

## LOOP B · RONDA 30/30 (:00/:30)
- **O quê:** sistêmico — ponte (de_dell/de_laura), site/esteira REST, FAROL/audiência, bugs/memória viva, CONTEXTO_MINI atualizado, 1 CHECK + push.
- **Telegram:** vê o INBOX; `RESPONDIDO_FLASH` = já atendido (ação só se ordem); sem resposta flash ou pergunta densa = responde em RESPOSTAS.md (1º da fila, janela 40 min; carteiro us65 entrega). NUNCA chamar getUpdates.
- **Papel de chefe:** analisar o sistema como um todo e distribuir tarefas; registrava aqui as distribuições.
- **Prompt:** `~/ronda_dsn_prompt.md` (identidade DS Nuvem Chefe + regras de fala DSC-030/032).

## Grupo de 3 robôs — ⏳ PLANO AGUARDANDO ✓ DO MIGUEL (não construir)
- Revisor de Texto: consultivo, nunca bloqueia; ~US$ 0.05/dia.
- Revisor de Foto: precisa de visão (DSC-007) — Opção A Dell/GLM (zero) ou B vision-exp na Tencent (~US$ 0.012/dia, exige ✓ prévio). Plano completo: `Foruns/forum_ds_nuvem_chefe_dois_loops_20260830.md`.

## Histórico
- 30/08 15:4x BRT — Ouvido instalado: Whisper local (zero custo) + fallback AssemblyAI; chave canônica DeepSeek espelhada (a .dsh estava 401). — ZM
- 30/08 15:26 BRT — Loop A no ar (offset herdado 747773836); daemon us65 vira carteiro (flag reversível). Renome aplicado. — ZM/ZCode GLM-5.3
