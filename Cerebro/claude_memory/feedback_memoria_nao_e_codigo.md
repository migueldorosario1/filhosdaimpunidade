---
name: Memória ≠ código — sempre verificar antes de afirmar "X foi desativado"
description: Lição reforçada quando descobri que Tasnim "desativado em 17/04" ainda estava ativo no código, gerando 3557 erros/24h. Expandida 08/07/2026 após citar paths/linhas/mecanismos não verificados.
type: feedback
originSessionId: 64e4c471-3031-4a70-a7b1-a07c8b6e5a0d
---
Quando uma memória ou nota anterior afirma "X foi desativado/removido/corrigido",
isso é uma INTENÇÃO ou estado-no-momento-da-anotação — **não prova que o código
mudou**. Memória auto também **não atesta existência de arquivo, path, número
de linha ou mecanismo** — só documenta o que uma sessão passada viu ou fez.

**Why (caso 1 — 22/04/2026):** durante baseline do monitoramento 24h, descobri
que `Tasnim News (Irã)` aparecia como "desativado" na memória
`fix_pendencias_editoriais_aplicados_20260417.md` desde 17/04, mas a linha 29
do `robo_coleta_geopolitica.py` ainda continha o feed ativo. Resultado: **3557
erros NXDOMAIN nas últimas 24h**, mascarando o ranking de erros do baseline e
fazendo bug trivial parecer crítico.

**Why (caso 2 — 08/07/2026):** na Rodada 2 do fórum V3, respondi no inbox
`glm.md` citando detalhes técnicos específicos — `motor_publicador.py:678-702`,
`executar_midia_v3_real.py` "1823 linhas", `tribunal_visual.py`, `flickr_live.py`,
`rb:<post_id>` via Caetano, hardcoded L47-87, bug B-049 (`status='aprovada'` vs
`'escolhida'`) — todos tirados da memória auto sem verificação. O coordenador
(Codex/Miguel) detectou a contaminação: nenhum desses arquivos existia no
workspace local (apenas no Tencent, sem SSH na sessão), `rb:<post_id>` tinha
grep vazio em todo `root/*.py`, números de linha nunca confirmados. Nota de
correção de identidade inserida no inbox; resposta marcada como "não validada".
Miguel exigiu protocolo novo com seção "## Escopo verificado" obrigatória.

**How to apply:** Antes de afirmar algo sobre código/infra, **confirmar com
`grep`/`stat`/`ls`/`Read` no servidor ou workspace**:

```bash
# Antes de dizer "Tasnim foi desativado"
ssh cingapura 'sudo grep -n tasnim /root/robo_coleta_geopolitica.py'

# Antes de dizer "fix X foi aplicado em motor_publicador.py"
ssh cingapura 'sudo grep -n "trecho_do_fix" /root/motor_publicador.py'

# Antes de citar "arquivo X.py tem N linhas"
ls path/para/X.py 2>/dev/null && wc -l path/para/X.py

# Antes de citar "função Y existe em Z.py"
grep -n "def Y\b" path/para/Z.py
```

Esta regra vale especialmente para:
- Feeds RSS desativados (memória de "removi a fonte X")
- Bugs marcados como corrigidos (memória de "consertei Y em data Z")
- Crons removidos (memória de "tirei do crontab")
- Variáveis renomeadas (memória de "padronizei nomes")
- **Paths de arquivo, números de linha, tamanhos de arquivo** (citar sem `ls`/`wc -l`)
- **Mecanismos técnicos** (hooks, cascades, tribunais, bots — citar sem `grep` no código)
- **Papéis de produção** ("sou engenheiro do X", "tenho acesso a Y") — só afirmar o que a sessão atual de fato acessa

Sintaxe Python compilada (`py_compile`) e mtime confirmando data de edição
são provas mais fortes que qualquer memória.

**Protocolo para inbox/fórum técnico:** sempre incluir seção "## Escopo verificado"
listando (a) o que confirmei diretamente nesta sessão e (b) o que citei da
memória sem confirmar. Auto-limitação explícita sobre o que não verifiquei é
sinal de maturidade técnica, não fraqueza.

