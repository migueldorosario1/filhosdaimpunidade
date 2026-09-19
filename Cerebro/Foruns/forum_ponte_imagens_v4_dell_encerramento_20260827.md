# 🖼️ Fórum — Ponte de Imagens V4 no Dell: encerramento da operação ativa + ronda backup 4/4h

**Data:** 27/08/2026 13:45 BRT · **Quem:** ZCode/GLM-5.3 (Dell) · **Decisão:** ordem verbal do Miguel (~15h).

## Decisão

1. **Caçadora de imagens ATIVA desligada no Dell.** Justificativa do Miguel: "o caçador de imagens já está muito forte em outra" — Zepo de Laura reativado, Clô de Laura reativado, Clô de Miguel ativado. O Dell não precisa caçar por conta própria.
2. **No lugar, ronda leve de 4/4h** (automação `automation-e1b2d648` reescrita, cron `10 */4 * * *`): verifica se está tudo certo com o sistema, se alguém está precisando de ajuda — **e se notar, oferece ajuda** (mensagem na ponte `de_dell.md`; não executa caça no lugar de ninguém sem failover ou convite). Se `loop_ativo=laura` e tudo fluindo: SKIP de 1 linha, sem gasto.
3. Sessão do Miguel aqui será **encerrada e renasce leve** (prompt colável gravado no §4 abaixo e entregue no chat).
4. Roteamento da sessão de imagens (ordem de 27/08 ~12:10, já vigente): **GLM-5.3 com DeepSeek de fallback** — DeepSeek não tem visão, PASSO visual pausa nele (detalhe no nodo CHAVES_E_LLMS).

## Estado no encerramento (herança para quem retomar)

- **Canônico:** 3 capas aplicadas 26/08 (267589→267792, 267743→267794, 267770→267796, todas tribunal APROVADA + carimbo casado + readback). Pendente: 267542 (Flávio) exige foto NOVA (trava Emenda 6 — MD5 reusado pelo loop no 265908). Varredura thumb-sem-meta: vazia.
- **Espelho:** 3 aplicadas (267701→400149, 267742→400150, 267585→400151). **~12 publicados sem capa restantes** — dono agora: caçador do Laura.
- **Aprendizado completo (runbook + 10 lições pagas com erro real):** `Cerebro/Memorias/memoria_ponte_imagens_v4_dell_licoes_20260827.md` (é a referência que a ronda backup usa em failover).
- Registros de rodada: `ponte_imagens_v4_LOG.md` (26/08 16:55) + livro de reservas em dia + ZM-20260826-023 na ponte.

## Incidentes/achados que ficam de herança

1. Loop do Laura violou Emenda 6 (reuso de MD5 no 265908) — dedup dele precisa de conserto (avisado em ZM-20260826-023; ACK pendente).
2. Livro de reservas ficou parado 21/08→26/08 (ninguém rondava) — resolvido pela ronda de verificação 4/4h.
3. Sync do repo pode não pegar append recente (prova: `git show origin/main:<path> | grep <marca>`; se faltar, cp manual + push).

## §4 — Prompt da sessão nova (levinha) — colar no ZCode novo

```
Bom dia! Sessão nova, levinha, no Dell do Miguel (ZCode, workspace ZCodeProject). Antes de qualquer tarefa: pt-BR sempre; linha de crédito dos provedores no início da resposta; rodapé = assinatura ZCode/<modelo atual> + 🕐 hora real via Bash date + 📁 Fórum usado. Regras de casa: Cérebro canônico em "/home/migueldorosario/Downloads/Antigravity Google/Cerebro/" (dúvida = consultar: 00_CEREBRO_CANONICO.md → INDEX_MASTER → nodo do tema) e MONITORAMENTO_DE_TRABALHO.md antes de qualquer trabalho (regra viva §112), registrando linha ao começar e ✅ ao terminar. Contexto mínimo: a caçadora de imagens foi desligada neste PC (fica ronda backup 4/4h automation-e1b2d648; caçador forte = Laura); runbook dela em Cerebro/Memorias/memoria_ponte_imagens_v4_dell_licoes_20260827.md se um dia precisar. Fique leve: sem rondas pesadas, sem varreduras longas — só o que eu pedir. Me diga "pronto" e fique à disposição.
```

## Estado da missão

**O que aconteceu:** caçadora ativa do Dell encerrada em ordem; ronda backup 4/4h já no ar (próxima execução hoje ~16:10); lições + fila + prompt da sessão nova gravados. **O que falta:** ~12 capas do espelho e 267542 do canônico (dono: Laura; backup oferece ajuda se notar). **O que preciso do Miguel:** nada — só colar o prompt do §4 na sessão nova quando quiser começar.
