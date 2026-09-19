# 2026-09-02 — O clone local do "canônico" pode atrasar horas — o número da ronda sai do origin

**O quê:** abri a ronda das 04:30 lendo a ponte no clone local (~/cerebro-miguel) e o `de_dell.md` estava parado no XM-20260902-001 (02:24) — ~2h / 4 rondas atrás do estado real. As rondas DS-006..009 (45º-48º), o ACK da CL (CL-054, 03:48) e os heartbeats (AL-505 04:05, ds laura 04:11) já existiam no ORIGIN/espelho do workspace. Quase re-registrei o ACK da CL como pendência e quase numerei a ronda errado.

**Por quê:** o clone local do canônico não é atualizado por mim (fora do sandbox do workspace, read-only) e o pull dele depende de outro ciclo da casa; entre uma ronda e outra entram vários blocos via origin sem aviso — o arquivo "canônico" local vira memória antiga silenciosamente. 2ª ocorrência da lição: na 1ª (DS-007, 03:00) a defasagem era de 1 ronda; agora, de 4 rondas / ~2h.

**Como aplicar:** (1) ABERTURA da ronda = `git pull --ff-only` no espelho do workspace + conferir o ÚLTIMO bloco DS-/CL-/DSC- no `de_dell.md`/`de_laura.md` do ORIGIN antes de qualquer registro — verificação de ~30s; (2) o número do check (49º), o placar do rito (CL já assinou 03:48; falta só o CM) e o volume saem do origin, nunca do clone local; (3) se o clone local divergir do origin, o origin vence (decisão de ronda contra o estado do ORIGIN/espelho — lição 20260902_promulgacao_decretada_e_ack_art7.md reforçada); (4) escrita segue via espelho + `git push origin main` (DS-024; canônico local read-only no sandbox).

Ref.: DS-20260902-010 (de_dell.md 04:35), DS-20260902-007 (46º, 1ª ocorrência da defasagem), XM-20260902-001.
