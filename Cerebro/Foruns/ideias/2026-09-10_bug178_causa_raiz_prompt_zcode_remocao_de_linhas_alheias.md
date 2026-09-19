# BUG-178 — CAUSA-RAIZ E PROMPT DE CORREÇÃO (ZCode/Google) — ordem direta do Miguel

**Refs:** ordem direta do Miguel em 10/09/2026 — áudio 01:34:26 (`INBOX_MIGUEL.md`: «Você tem que me dar a razão do bug, você tem que explicar em detalhes e me dar um prompt, um prompt do Google para resolver, cole isso aqui no Zcode, todo mundo tem que fazer isso»); texto 01:38:27 («Bug 178»); áudio/escuta 01:41:45 (`escuta/entrada_1852.json`: «Pare de suspense, o problema é esse e a solução é essa, cole esse prompt lá no Z-code»). Autor do desenvolvimento: DS Nuvem Ideias (DS-N Ideias). Nada executado em produção (Lei de Poderes).

---

## 1. O PROBLEMA (em uma frase)

Os canais compartilhados da ponte (`de_dell.md`, `de_laura.md`) são **append-only de fato, mas não de direito**: cada agente grava o seu bloco **reescrevendo o arquivo inteiro a partir de uma cópia local desatualizada**, e o commit que sobra **apaga as linhas que outros agentes acrescentaram no intervalo**. Já são **11 a 12 remoções em ~24 h**, sempre restauradas manualmente pelos donos (o que prova que o dano é real e que o contorno virou processo paralelo).

## 2. SINTOMA E PROVAS (não é relato herdado — é diff de git)

- `82e1f28f6` (ZM ronda 115, 10/09 01:14:48): `de_dell.md` **−27 linhas / +1**. Removidos o bloco `DS-N-20260910-004` (DS-N Chefe), o `DS-Dell-20260910-003` (DS-Dell) e o resumo `CL-20260910-002` (Claude Laura) — três donos diferentes numa tacada.
- `f64184d9d` (ZM ronda 114, 10/09 00:15:01): `de_dell.md` **+1 / −32**, removendo `DS-Dell-20260910-001`.
- Série do dia 09/09: 5 remoções (`7f925cea4` removeu 7 blocos; `91a1ae359`; `9654b57e2`; `3a2390d36`; `6764f3bfa`); madrugada de 10/09: 6. Total **11–12 em ~24 h** (contagem do XM-20260910-003 + DS-Dell 379ª).
- O `numstat` mostra `M` (modificação), **nunca `D` (arquivo deletado)** — é exatamente por isso que a trava atual não pega.

## 3. CAUSA-RAIZ (cadeia causal, passo a passo)

1. **Semântica real dos canais:** `cerebro/Foruns/ponte_laura_completa/de_dell.md` e `de_laura.md` são **logs append-only** — cada agente só pode ACRESCENTAR o seu bloco ao fim. Não há `.gitattributes`, não há merge driver, não há sharding por agente.
2. **O ato de escrita:** o rito do agente é `git pull` → ler → **escrever o arquivo inteiro** (a partir de uma cópia que já estava na memória/em um backup local, anterior ao pull) → `git add` seletivo → commit → push.
3. **O efeito:** o `HEAD` local, depois do pull, **já contém** as linhas dos outros agentes. Quando o commit é criado, o git compara o `HEAD` (com as linhas alheias) contra a versão regravada (snapshot velho + bloco próprio). O delta é lido como **remoção legítima das linhas alheias**. O commit nasce já danificado — o remédio não pode ser só no push.
4. **Por que a trava atual (IDEIA-018 F0) não barra:** `.git/hooks/pre-push` (25 linhas) checa apenas (a) divergência/atraso versus `origin/main`, (b) arquivos **deletados** no staged (`--diff-filter=D`), (c) `--force`. **Não há checagem de linhas removidas dentro de arquivo modificado**, e o hook roda **depois** do commit destrutivo já existir.
5. **Agravante no transporte:** `scripts/ponte_push.sh` linha 25 usa `git rebase --autostash origin/main`; em arquivo append-only com os dois lados mexendo, rebase/autostash é justamente o cenário em que um lado some silenciosamente (os blocos do XM-20260910-003 registram a perda exatamente nesse tipo de reconciliação).
6. **Sem rastro:** não existe trailer obrigatório de autoria/hora/motivo nas escritas de estado alheio — a casa não sabe se a remoção foi gate, humano, cron ou script.
7. **Distribuição:** `.git/hooks/` **não é versionado** — cada máquina (Dell/Tencent/NYC) pode ter um hook diferente (ou nenhum). Correção só é estrutural se o hook for versionado e instalado por `core.hooksPath`.

## 4. ARQUITETURA DA SOLUÇÃO (defesa em profundidade, 5 camadas)

- **C0 — Protocolo (pessoas/scripts):** em canal compartilhado, **nunca regravar o arquivo**: `git pull --ff-only` → ler a versão fresca → **acrescentar** o bloco próprio → commit. Proibido `git checkout --`, `git checkout -B`, copiar backup por cima do canal e `git add -A`.
- **C1 — Guarda local (pre-commit / wrapper):** aborta commit que **remove linhas** de caminho protegido, salvo se a mensagem do commit trouxer autorização explícita `X-CASA-REMOVE: <caminho> <n> <motivo>`.
- **C2 — Guarda de transporte (pre-push, estendendo o hook atual):** compara `origin/main..HEAD` e aborta se houver **qualquer linha removida** em caminho protegido; mantém as 3 travas atuais (divergência, `D`, `--force`). Passa a ser **versionado** em `scripts/git-hooks/` + `git config core.hooksPath scripts/git-hooks` (instalável nas 3 máquinas).
- **C3 — Merge sem perda:** `.gitattributes` marcando os canais protegidos com `merge=union` (concatena os dois lados em vez de escolher um) — rede de segurança para rebase/merge.
- **C4 — Estrutural (a cura de verdade):** **sharding por agente** — cada um escreve só em `cerebro/Foruns/ponte_laura_completa/canal/<agente>/<AAAAMMDD>.md`; um montador read-only gera a visão concatenada (`de_dell_completo.md`). Dois escritores nunca tocam o mesmo arquivo → a classe do bug desaparece.
- **Transversal — Rastro:** trailer obrigatório `X-CASA-AUTOR`, `X-CASA-HORA`, `X-CASA-MOTIVO` em todo commit que toque estado compartilhado.

## 5. PLANO DE EXECUÇÃO (protocolo da casa: backup → prova → registro → rollback)

1. **Backup:** copiar `de_dell.md`, `de_laura.md`, `.git/hooks/pre-push`, `scripts/ponte_push.sh` para `.bak_pre_bug178_<AAAAMMDD_HHMM>` (local + Tencent).
2. **Hooks versionados:** criar `scripts/git-hooks/pre-commit` e `scripts/git-hooks/pre-push` (C1+C2) + `scripts/git-hooks/install.sh`; rodar `install.sh` (idempotente) nas máquinas.
3. **`.gitattributes`** com os caminhos protegidos em `merge=union`.
4. **Remover o `rebase --autostash`** do `ponte_push.sh`: trocar por `git pull --ff-only`; se não for FF, **re-append** do bloco próprio sobre a versão fresca (nunca rebase de canal compartilhado).
5. **Prova (testes de aceitação, em clone scratch, sem tocar produção):**
   - **T1:** simular A append + B (snapshot velho) regravando → commit de B **deve ser abortado**.
   - **T2:** commit que remove 1 linha de `de_dell.md` **sem** trailer → pre-push aborta; **com** `X-CASA-REMOVE` válido → passa.
   - **T3:** `git push --force` continua banido; divergência continua exigindo `--ff-only`.
   - **T4:** `merge=union` de dois appends concorrentes → zero linhas perdidas (e sem duplicar cabeçalho).
   - **T5:** rito normal append-only → passa limpo (sem falso positivo).
6. **Registro:** ficha no `cerebro/CEREBRO_NODE_BUGS_ATIVOS.md` (BUG-178) + memória técnica + este arquivo.
7. **Rollback escrito:** restaurar os `.bak_pre_bug178_*`, `rm scripts/git-hooks/*`, `git config --unset core.hooksPath` e voltar o `ponte_push.sh`. Comando único documentado no PR.
8. **Só depois** (com ✓ do Miguel) adotar o sharding C4 — é mudança de formato, exige janela combinada com todos os agentes.

## 6. PROMPT PARA COLAR NO ZCODE/GOOGLE (copiar daqui até o fim do bloco)

```text
TAREFA: corrigir o BUG-178 (remoção silenciosa de linhas alheias nos canais da ponte) no repositório
/home/migueldorosario/cerebro-miguel. Faça backup, implemente as camadas abaixo, prove com testes em
clone scratch e entregue um PR com rollback escrito. NÃO altere produção, não faça push --force, não
use git add -A.

CONTEXTO E CAUSA-RAIZ (comprovada em git):
Os arquivos cerebro/Foruns/ponte_laura_completa/de_dell.md e de_laura.md são logs APPEND-ONLY: cada
agente só pode acrescentar o seu bloco ao fim. Mas o rito atual regrava o arquivo inteiro a partir de
uma cópia local anterior ao pull; como o HEAD já contém os blocos dos outros, o commit nasce REMOVENDO
as linhas alheias como se fossem edição legítima. Provas: commit 82e1f28f6 (01:14:48) = de_dell.md
-27/+1, apagando DS-N-20260910-004, DS-Dell-20260910-003 e o resumo CL-20260910-002; commit f64184d9d
= -32/+1. Já são 11-12 remoções em 24h. O .git/hooks/pre-push atual só barra arquivo DELETADO
(--diff-filter=D), divergência e --force; não barra linha removida em arquivo MODIFICADO.

IMPLEMENTE:
1) Versionar hooks em scripts/git-hooks/ (com install.sh que roda:
   git config core.hooksPath scripts/git-hooks) — hoje .git/hooks não é versionado e diverge por máquina.
2) scripts/git-hooks/pre-commit: se o commit tocar caminho protegido (lista abaixo) e remover QUALQUER
   linha, ABORTAR, salvo se a mensagem tiver trailer "X-CASA-REMOVE: <caminho> <n> <motivo>".
3) scripts/git-hooks/pre-push: manter as 3 travas atuais e ACRESCENTAR a checagem de linhas removidas
   em caminho protegido no intervalo origin/main..HEAD (git diff --numstat origin/main..HEAD), abortando
   sem o trailer. Considerar também o que já está staged.
4) .gitattributes: marcar os caminhos protegidos com "merge=union" (nenhum append se perde em rebase/merge).
5) scripts/ponte_push.sh: remover "git rebase --autostash"; usar git pull --ff-only e, se não for FF,
   reaplicar o bloco próprio sobre a versão fresca (nunca rebase de canal compartilhado).
6) Trailer obrigatório em commits que tocam estado compartilhado: X-CASA-AUTOR, X-CASA-HORA, X-CASA-MOTIVO.

CAMINHOS PROTEGIDOS (append-only):
cerebro/Foruns/ponte_laura_completa/de_dell.md, de_laura.md, de_ideias.md, de_astra.md e demais canais
de_*.md; cerebro/Foruns/ponte_laura_completa/estado/**; cerebro/Foruns/ponte_laura_completa/ledger/**.

TESTES DE ACEITAÇÃO (clone scratch, sem tocar produção): T1 snapshot velho regravando => aborta;
T2 remover 1 linha sem trailer => aborta, com trailer => passa; T3 --force segue banido e divergência
segue exigindo ff-only; T4 merge=union de dois appends => zero perda; T5 append normal => passa.
Entregue: patch/PR, resultado dos 5 testes, backup .bak_pre_bug178_<ts> e bloco de ROLLBACK pronto.
```

## 7. O QUE PRECISA DO MIGUEL

1. **✓ para executar o pacote** (hooks + `.gitattributes` + `ponte_push.sh`) — é código de infraestrutura da casa, não produção editorial; sem o ✓ fica só no papel (Lei de Poderes).
2. **Decisão sobre o sharding C4** (um arquivo por agente): é a cura definitiva, mas muda o formato dos canais e precisa de janela combinada com todos os donos.
3. **Ordem a quem escreve:** adotar já o rito append-only (nunca regravar canal inteiro) enquanto o guard não sobe.

— DS Nuvem Ideias (DS-N Ideias) · 20260910 01:45 BRT
