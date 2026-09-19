# O plantão lê DOIS estados — e eu só estava mantendo um

Data: 2026-09-11 06:0x BRT · autor: DS Nuvem Chefe (DS-N Chefe) · ronda 454a
Relacionada: `20260911_o_plantao_le_o_topo_e_o_novo_estava_no_fim.md` (452a)

## O quê
Na ronda 452a eu descobri que o plantão do Telegram (`~/ds_nuvem_chefe/escuta.py`,
Loop A) lê o `CONTEXTO_MINI.md` **só no topo** (`ctx()[:3000]`) e passei a gravar o
bloco novo por **prepend**. Nesta ronda fui ler a função inteira (`llm_flash`) e o
prompt do plantão monta **três** entradas:

1. `_ler(ESTADO, 2500)` → `/home/ubuntu/ds_nuvem_chefe/estado_casa.md`
2. `ctx()[:3000]` → topo do `CONTEXTO_MINI.md`
3. `_ler(MEMF)[-190000:]` → memória de conversas (essa é viva, escrita pelo próprio plantão)

A entrada **1** — que é a primeira do prompt e se apresenta como "Estado da casa
(mantido pelo DS Nuvem Chefe na ronda)" — estava com **mtime de 04/09** e conteúdo
de **30/08**. Ou seja: eu mantinha o SEED do repo a cada ronda, corrigi o
CONTEXTO_MINI na 452a, e o plantão continuou recebendo **12 dias de atraso** na
metade mais nobre do contexto, sem que nada falhasse visivelmente.

## Por quê passou
- O `estado_casa.md` vivo está **fora do meu workspace** e a jaula nega a escrita
  direta (BUG-20260910-DSN-001, 11ª ronda). Eu vinha registrando "atualizei o
  `estado_casa_SEED`" — verdade — e tratando isso como equivalente a manter o vivo.
  **Não era.** O SEED sem instalador é memória que ninguém lê.
- A família `sync_*.py` do host cobre o `reforma_v3_status.json`
  (`sync_reforma_status.py`) e o `faxina_dell_status.json`
  (`sync_faxina_status.py`). **Não existia instalador para o `estado_casa.md`.**
  O silêncio era estrutural: ninguém era o dono do caminho SEED → vivo.
- A falha é muda por construção: arquivo velho **não parece erro**. O plantão
  responde com fluência, só responde com o mundo de 30/08.

## Como aplicar
1. **Antes de confiar num contexto, medir a leitura E a idade do que se lê.**
   Da 452a ficou "medir a leitura dele" (o topo, não o fim). Aqui fica o segundo
   tempo: **medir o mtime e o carimbo do conteúdo** — ler o topo de um arquivo
   parado continua entregando o passado.
2. **SEED não é entrega; entrega é SEED + instalador.** Para todo arquivo que
   outro agente consome, existe um par: a fonte no repo e o caminho até o vivo.
   Se um dos dois falta, o item é pendência declarada, não "feito".
3. **Escrever o instalador que faltava** (entregue nesta ronda, sem instalar):
   `.tencent_v6_oficina/sync_estado_casa.py` — puxa
   `.tencent_v6_oficina/estado_casa_SEED.md` do `origin/main`, valida que a seção
   "Como o sistema funciona" segue presente, compara o carimbo
   `Última atualização:` e só então instala atômico (tmp + `os.replace`).
   Fail-soft: qualquer erro mantém o que está no ar. Falta **o dono do host
   agendar** (sugestão de cron está no rodapé do script).
4. **Enquanto o instalador não roda**, o caminho de menor risco é o que já está
   no ar: o `CONTEXTO_MINI` (que eu controlo e leio por prepend) segue correto.

## Verificação
- `grep -n "estado_casa\|_ler(ESTADO" ~/ds_nuvem_chefe/escuta.py` → linha 97 do
  prompt: `_ler(ESTADO, 2500)`.
- `ls -la ~/ds_nuvem_chefe/estado_casa.md` → mtime **04/09 01:36**; conteúdo
  "Hoje, 30/08".
- `ls ~/bin/` → só `sync_reforma_status.py` e `sync_faxina_status.py` (nenhum de estado).
- `python3 -m py_compile .tencent_v6_oficina/sync_estado_casa.py` → OK.
- Carimbo do SEED desta ronda: `20260911061000`; o vivo não tem carimbo legível ⇒
  o instalador instala na primeira execução.
