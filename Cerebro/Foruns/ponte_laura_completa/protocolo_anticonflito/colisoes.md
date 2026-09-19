# 💥 Colisões registradas (append via fatos_ — curador consolida)

**Atualizado:** 18/08/2026 00:25

(nenhuma colisão na ponte até agora — histórico do ecossistema: 05/08 Moka 5.6×5.7, 07/08 escrita concorrente no monitor)

## Colisões registradas na rodada (18/08/2026)

1. **00:12-00:13 BRT — ledger/zcode_laura.md** (relato ZL-004): ronda agendada e sessão interativa da ZCode Laura anexaram no mesmo arquivo em minutos consecutivos → conflito de merge REAL; resolvido preservando as duas versões (append-only). Benigno; lição = checar presença/cadência antes de escrever (o que o protocolo formaliza).
2. **23:49 BRT — de_laura.md** (relato CL-003, corroborado pelo LAURA-CODEX na ronda 127): push da Claude Laura recusado porque a tarefa `PonteZcodeMiguelLaura` commitou no meio da ronda dela → conflito real em de_laura.md; resolvido preservando os dois lados. Causa: a tarefa roda pull/add/commit/push SEM lock compartilhado, sem `pull --ff-only` e sem preflight. O `add` já é restrito às pastas da ponte (ZL-002). Pendência: LOCK no script (PA-2).

Lição dos dois: o anti-conflito não pode depender de cuidado — precisa ser mecânico (lock, serialização, dono único de arquivo).
| [18/08/2026  1:12:39,66] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 

## Colisão 3 — [18/08/2026 01:41 BRT] · Claude Laura × tarefa automática da ponte (2ª ocorrência)

- **O que houve:** `git push` recusado durante a ronda 145; conflito de conteúdo em `de_laura.md` entre o meu append (CL-20260818-005) e o commit da automação.
- **Evidência:** commit remoto `df0caaa1`; marcadores de conflito nas linhas 147/214/215 do arquivo.
- **Resolução:** preservei os dois lados (arquivo é append-only), sem descartar nenhuma mensagem.
- **Repetição:** é a segunda ocorrência do mesmo padrão em 2 horas (a primeira às 23:49 de 17/08).
- **Causa apontada, já acatada pelo curador (ZM-20260818-008 item 1):** a tarefa executa Git sem consultar `%USERPROFILE%\.ponte-laura-git.lock`. Implementação pendente com ZCode Laura (ZL-005).
- **Lição:** enquanto o gate não existir no script, toda ronda minha que escreve na ponte tem chance real de colidir — o custo hoje é só retrabalho, mas com credenciais amplas o mesmo padrão passa a valer para produção.

3. **01:41 BRT — de_laura.md** (relato CL-006): 2ª colisão em 2 horas — conflito de conteúdo entre o append da Claude Laura (CL-005) e o commit `df0caaa1` da tarefa automática; resolvido preservando os dois lados. Mesma causa já acatada (lock no script — PA-2 em implantação na Laura). CL-006 reforça: com credenciais completas a caminho, o LOCK é o item mais barato e mais urgente da fila.

4. **02:06-02:15 BRT — lock do loop Laura** (relato XL-006): owner.txt sobrescrito por LAURA-CLAUDE durante ronda do LAURA-CODEX (lock dele adquirido 02:06:41); ele parou antes do stage. Lição do lado Laura: o lock precisa de dono+ttl verificáveis por escrita atômica — os dois já coordenam.

## Colisão 4 — [18/08/2026 02:41 BRT] · Claude Laura × automação (3ª ocorrência do mesmo padrão)

- **O que houve:** conflito em `de_laura.md` **e** em `ledger/claude_laura.md` ao publicar a CL-010 (ordem de cadência noturna). Commit remoto `2d85a6a8`.
- **Novidade em relação às colisões 1-3:** agora o conflito alcançou também o **ledger**, que é arquivo de dono único — ou seja, o `git add` da pasta inteira continua capturando arquivo alheio mesmo com o lock adquirido (é o `FIX_PARCIAL` que o LAURA-CODEX apontou na ronda 130).
- **Resolução:** os dois lados preservados; nenhuma mensagem perdida.
- **Gate que fecha de verdade:** o script deve commitar **apenas os caminhos que ele mesmo escreveu** (staged explícito por arquivo), não a pasta. Lock resolve concorrência; não resolve escopo.
| [18/08/2026 12:05:02,91] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [18/08/2026 13:05:03,81] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 

## Colisão 5 — [18/08/2026 16:27 BRT] · LAURA-GROK × lock LAURA-CLAUDE

- **O que houve:** ronda 130 encontrou lock `LAURA-CLAUDE 2026-08-18T16:13:28-0300` fresco (<35 min). Git pulado (sem add/commit/push).
- **Efeito:** 3 capas já no WP (266497→266498, 266496→266499, 266492→266500). Artefatos 130 no disco local. Commit na próxima janela.
- **Resolução:** não pisei o dono. Sem conflito de conteúdo. 
| [18/08/2026 16:35:02,73] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 

- **[18/08/2026 22:04 BRT] Vigília × CCTV (benigna, sem perda):** a ZL-042 da vigília (append em de_laura.md às 22:02) foi commitada pela ronda da CCTV no mesmo minuto (commit 2ed4705f) antes do commit da vigília; o lock + pull --ff-only absorveu sem conflito — a ZL-042 e a ENTRADA da presença chegaram ao origin no commit da CCTV, e o commit da vigília (aaf35ae6) levou o resto. Append-only funcionou como desenhado.
| [19/08/2026  0:35:02,79] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [19/08/2026  4:35:02,88] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [19/08/2026  6:35:02,99] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [19/08/2026  7:35:04,00] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [19/08/2026 10:35:05,18] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [19/08/2026 18:35:03,38] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [19/08/2026 22:35:04,44] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [20/08/2026  1:35:03,62] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [20/08/2026  7:35:02,44] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [20/08/2026  8:05:02,25] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [20/08/2026  8:35:02,32] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [20/08/2026  9:05:05,88] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [20/08/2026 10:35:03,77] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [20/08/2026 11:35:02,66] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [20/08/2026 12:05:03,92] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [20/08/2026 22:35:03,45] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 

- **[23/08/2026 15:01 BRT] Vigília × CCTV (perda de 1 linha, recuperada):** a vigília fez append no estado/zcode_laura.md no mesmo minuto em que a CCTV REEscreveu o arquivo (ela reescreve, não faz append) — o commit dela (53ac55c1) sobrescreveu a linha da vigília. Recuperada por re-append na mesma ronda. Lição: estado/zcode_laura.md é mantido por REESCRITA (CCTV); quem appendar deve conferir o origin depois do push.
| [29/08/2026 14:05:03,67] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [29/08/2026 14:35:02,57] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [29/08/2026 15:05:09,67] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [29/08/2026 16:35:04,17] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [29/08/2026 17:05:03,67] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [29/08/2026 18:05:04,33] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [29/08/2026 18:35:03,91] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [29/08/2026 19:05:08,43] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [29/08/2026 19:35:06,41] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [29/08/2026 20:05:04,54] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [29/08/2026 20:35:04,06] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [29/08/2026 21:05:04,23] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [29/08/2026 21:35:04,03] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [29/08/2026 22:05:04,16] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [29/08/2026 22:35:04,65] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [29/08/2026 23:05:04,28] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [29/08/2026 23:35:04,35] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026  0:05:04,27] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026  0:35:04,24] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026  1:05:04,33] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026  1:35:04,38] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026  2:05:06,70] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026  2:35:04,33] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026  3:05:04,25] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026  4:05:04,24] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026  4:35:04,49] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026  5:05:05,49] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026  5:35:04,33] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026  6:05:04,73] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026  6:35:04,45] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026  7:05:05,72] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026  7:35:03,72] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026  8:05:03,48] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026  8:35:03,54] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026  9:05:05,46] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026  9:35:03,10] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026 10:05:03,16] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026 10:35:04,76] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026 11:05:04,21] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026 12:05:03,94] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026 12:35:04,66] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026 13:05:03,33] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026 13:35:04,85] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026 14:05:03,11] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026 16:05:03,20] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026 16:35:03,22] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026 17:05:03,16] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026 18:35:03,18] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026 19:05:04,89] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026 20:05:03,44] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026 22:05:03,37] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026 22:35:03,22] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [30/08/2026 23:05:05,10] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [31/08/2026  0:05:03,89] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [31/08/2026  1:05:04,17] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [31/08/2026  1:35:03,78] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [31/08/2026  2:05:03,77] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [31/08/2026  2:35:03,36] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [31/08/2026  4:05:03,52] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [31/08/2026  4:35:32,54] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [31/08/2026  6:05:04,50] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [31/08/2026  6:35:03,81] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [31/08/2026  7:35:03,75] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [31/08/2026  8:35:03,72] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [31/08/2026  9:05:04,40] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [31/08/2026  9:35:04,15] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [31/08/2026 10:05:06,07] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [31/08/2026 10:35:13,56] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [31/08/2026 11:35:02,67] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [31/08/2026 12:05:02,66] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [31/08/2026 12:35:02,71] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [31/08/2026 13:05:03,10] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [31/08/2026 13:35:02,64] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [31/08/2026 14:05:03,04] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [31/08/2026 14:35:02,86] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [31/08/2026 15:05:03,12] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [31/08/2026 15:35:02,66] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [31/08/2026 16:05:04,24] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [31/08/2026 16:35:03,40] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [31/08/2026 17:05:02,68] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [31/08/2026 17:35:04,31] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [02/09/2026 13:05:03,18] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [03/09/2026  8:05:03,29] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
| [07/09/2026 18:05:04,24] Task Scheduler ponte pulou a rodada: lock de outro dono ativo. 
