---
name: NUNCA usar HEREDOC/open(w) em arquivos de memória compartilhada
description: Arquivos .md compartilhados entre IAs (CLAUDE.md, MEMORIA_PROJETO_CAFEZINHO.md, memoriaintegrada.md) só aceitam patch/Edit/sed — jamais open(w) full-rewrite. E nunca symlink entre eles.
type: feedback
originSessionId: aaf712a5-5fa7-48a5-8c49-6e491ff45b44
---
**Regra:** arquivos de memória lidos/escritos por múltiplas IAs (Claude Code + Antigravity) exigem duas disciplinas inegociáveis:
1. **Edição sempre via patch (Edit/sed).** Nunca `open(w)`, `cat > arquivo`, HEREDOC full-rewrite, ou qualquer operação que reescreva o arquivo inteiro de uma vez.
2. **Nunca ligar dois arquivos por symlink.** Se `MEMORIA.md → CLAUDE.md` existe, a próxima escrita full-rewrite em QUALQUER um dos dois (pelo caminho do symlink) destrói o target sem aviso.

**Why:** Em 2026-04-22 02:53 BRT, o Antigravity executou `cat << EOF > CLAUDE.md` depois de ter criado symlink `MEMORIA → CLAUDE`. O HEREDOC seguiu o symlink e **sobrescreveu o CLAUDE.md inteiro** com uma versão resumida (~10k bytes) que ele escreveu do zero. Perda silenciosa de ~64% do conteúdo original: credenciais WP reais de 6 portais, strings completas de 10+ chaves API, tokens staging, cheat sheet, estrutura de arquivos, senha sudo. Projeto sem git = backup impossível. Recuperei via `ssh + sudo cat .env.unificado` do Tencent, mas cheat sheet e estrutura tive que reconstituir de memória.

**SEGUNDO INCIDENTE confirmado — `/root/.env` no Tencent destruído em 2026-04-21 02:36 BRT.** Mesmo padrão: write atômico que sobrescreveu o `.env` (4426 → 319 bytes), perdendo TODAS as vars WP (`WP_USER`, `WP_PASS`, `WP_USER_CAFEZINHO`, `WP_PASS_CAFEZINHO`, `WP_USER_FALLBACK`, `WP_PASS_FALLBACK`, etc). Restaram só FLICKR/ELEVENLABS/HEYGEN/1 token Telegram. **Sistema de publicação parou silenciosamente 1h17min** em 22/04 entre 03:52 e 05:09 BRT (Miguel notou). NYC tinha o `.env` mutilado também (sync replicou). Recuperei do backup local `/root/.env.bak_pre_https_fix_20260420` (mtime 20/04 10:12). Detalhes em manual_de_bugs §11.

**Agressor**: Antigravity é o suspeito principal — Miguel comentou em 22/04 05:08 "deve ter sido a maldita integração de memória do antigravity". Padrão de write atômico destrutivo já confirmado 2x em 1 semana.

O pior é que o Claude Code havia previsto **exatamente** esse cenário no `forumintegracaomemoriashoje.md` §3.2 (2026-04-21 18:55) — documentado com os dois modos de falha possíveis — e recomendado Proposta A (fusão + redirect textual, SEM symlink). O Antigravity executou Proposta D assim mesmo. Lição reforçada: **quando o fórum alertar risco específico, pausar até Miguel confirmar**, não apenas "esperar pelo melhor".

**How to apply:**
- Em `CLAUDE.md`, `MEMORIA_PROJETO_CAFEZINHO.md`, `memoriaintegrada.md` e qualquer outro `.md` compartilhado: **sempre Edit/sed**.
- Em `.env` (Tencent e NYC): **NUNCA** sobrescrever inteiro. Sempre Edit incremental ou `tee -a` (append). Backup obrigatório antes (`cp .env .env.bkp-YYYYMMDD-HHMM`).
- Se precisar reestruturar (adicionar/remover seção grande), primeiro `cp arquivo arquivo.bkp-YYYYMMDD-HHMM`, depois Edit incremental.
- Recusar ajudar o Antigravity a recriar o symlink `MEMORIA → CLAUDE`. Se ele pedir, apontar para este feedback e para o adendo 2026-04-22 no `memoriaintegrada.md`.
- Se o Miguel pedir "reescrever CLAUDE.md" genérico: confirmar que quer full-rewrite (com backup) vs Edit cirúrgico. Default é Edit.
- Projeto não tem git: backup manual `.bkp-YYYYMMDD` é a única rede de segurança antes de qualquer mudança estrutural.
- **Monitoramento contínuo deve checar tamanho do `/root/.env` em cada ciclo** — alertar se cair >50% do tamanho prévio.
- **NYC backup só vale se for ANTERIOR ao sync** — pra `.env`, manter rotação diária com `cp /root/.env /root/.env.daily_$(date +%Y%m%d)` antes do sync_nyc_leve rodar.
