# Tarefas Legacy — Memória Coletiva de Conclusões

> Toda tarefa concluída ganha uma entrada aqui. **Nada se perde** — pra resgatar, basta voltar o slot ou abrir um novo na mesma linha. Fórum md vinculado vai pra `Foruns/legacy/` (também resgatável).

> Formato por entrada: data BRT • slot • nome • fórum • o que foi feito • o que ficou pendente.

---

## 2026-04-28 — Slots 1, 4, 7, 8 — Limpeza autorizada por Miguel

**Slot 1 — Custos e Reforma do Sistema**
Fórum: `Foruns/forum_custos_qualidade.md` | Período: 26/04 09:32 BRT → encerrou dormente
Plano emergencial §19 LIVE desde 25/04. Itens A4/B3/B4/F1/F2/F4 não chegaram a ser executados nesta sessão. Slot liberado por Miguel 28/04.

**Slot 4 — Agente Eleições — monitoramento pós-deploy**
Fórum: `CONTRATO_ELEICOES.md` v1.1 | Período: 26/04 09:35 → 15:08 BRT (wakeup 16:08 expirado)
Entregue: post 239383 publicado, `agente_eleicoes_produtor.py` com `status=publish`, crontab `*/30` coletor + `0 9,21` produtor. Pendência aberta: cascata de imagens melhorada (§38.4) e fix `banco_midia_cafezinho.db` 0 bytes.

**Tarefa 7 (histórica) — Bot Telegram áudio `@cafezinho_claudebot`**
Fórum: `Foruns/forum_audio_telegram_bot.md` | Deploy: 26/04 12:42 BRT
Smoke test passou. Cascata groq→xai→openai→transkriptor com cost_guard. Crontab `@reboot` + keepalives `*/5`.

**Slot 8 — UUID anti-duplicate WP**
Fórum: n/a | Período: 28/04 10:50 → 11:29 BRT (~40min)
Duas camadas: motor_publicador.py (per_page 100 + cache-busting + _indent_uuid) + snippet PHP WPCode Lite (HTTP 409 em duplicata). Validação 4/4 ✅. Monitoramento natural 48h em aberto.

---

## 2026-04-26 — Slot 5 — Manutenção da Memória + Sistema de Legacy

**Fórum:** [`Foruns/legacy/forum_organizacao_memoria.md`](../../../Downloads/Antigravity%20Google/Foruns/legacy/forum_organizacao_memoria.md)
**Período:** 26/04 08:43 BRT → 26/04 09:31 BRT (~50 min)

**O que foi feito:**
- `MEMORY.md` enxugado de 34KB → 6.4KB (cabe inteiro no contexto, parou de truncar). Backup `MEMORY.md.bkp_20260426_0843`.
- 55 arquivos antigos arquivados em `~/.claude/.../memory/legacy/` + `INDEX.md`.
- Resumo do sistema criado: [`reference_sistema_resumo.md`](reference_sistema_resumo.md).
- Guia de chaves criado: [`reference_chaves_guia.md`](reference_chaves_guia.md).
- Cópias de credenciais centralizadas em `chaves/cafezinho_root/`, `chaves/agentes_labs/`, `chaves/raiz_dotenv` (perms `chmod 600`) + `chaves/CHAVES_GUIA.md`.
- 24 fóruns dispersos consolidados em `Foruns/`. Stubs/redirects antigos removidos.
- Diretório `Foruns/legacy/` criado. 8 fóruns concluídos movidos pra lá (FORUM_AUTOCURA, forumtematicos, forum_lula, forum_recuperacao_env_hoje, forumauditorhoje, forumintegracaomemoriashoje, forum_eleicoes_teste_cruzado_analise_20260424, forum_organizacao_memoria).
- Modelo de slots reciclável formalizado (estados 🟢🟡🔵⏸️✅; slots **abertos** 1, 2, 3, ... N).
- Ritual de despertar formalizado: ler `reference_sistema_resumo.md` + `Tarefasdeagora.md`, auto-alocar, reportar mapa, ler fórum vinculado.
- Fórum [`Foruns/forum_memorias.md`](../../../Downloads/Antigravity%20Google/Foruns/forum_memorias.md) aberto pra discutir simplificação do `CLAUDE.md` com Antigravity (proposta de corte de §12 + encolhimento de §2/§4/§9/§10) — aguarda resposta.

**Pendências (ficam em aberto pra próxima sessão):**
- Listar candidatos a `Foruns/legacy/` ainda em dúvida (forum_novosagentes, forum_eleicoes, forum_enxame_comentaristas, forumeleicoeshoje, forum_custos_IA, forum_failover, forum_youtube_videos) pra Miguel decidir caso a caso.
- Aguardar resposta do Antigravity em `forum_memorias.md`; depois Miguel decide e Claude executa cortes no `CLAUDE.md`.
- Atualizar `CLAUDE.md` e `memoriaintegrada.md` pra refletir a nova estrutura (Foruns/, chaves/, slots abertos) — só após resposta do Antigravity.

## 2026-05-06: Movimentação para Legacy
- **Diretórios Movidos**: `_arquivo_velho`, `cingapura_root`, `cingapura_workspace`.
- **Destino**: `root/legacy/`.
- **Motivo**: Limpeza da raiz do projeto, conforme autorização (estava muito bagunçado). Nenhum arquivo ativo foi interrompido.
