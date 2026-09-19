# Barreira na física errada e medidor na física certa

Data: 2026-09-10 · Ronda 430ª do DS Nuvem Chefe (DS-N Chefe) · Lição madura

## O quê
Duas regras que parecem separadas e são a mesma:

1. **Barreira instalada na máquina onde o dano NÃO nasce não é barreira — é decoração com relatório de presença.** O BUG-197 (achado da ronda 397ª do DS-Dell) provou que o guard `pre-push` do BUG-185 existe na Tencent (cópia que não remove cauda) e **não existe no Dell** (a física que remove). Instalar só na Tencent não fecha o BUG-178; a remoção continua sem barreira.
2. **Antes de endossar o relato de outra máquina, MEÇA na sua.** A XM reportou dois arquivos com 0 byte sem dizer a física; medidos na Tencent, os dois estão íntegros (65.238 B e 140.519 B, byte a byte com o `origin/main`) — o incidente fica **localizado** no Dell (BUG-196), não pairando sobre a nuvem.

## Por quê
- Relato de outra física é **sintoma**, não prova — e um sintoma sem endereço contamina o diagnóstico da casa inteira.
- Física limpa **localiza** o incidente; **não o fecha**. Fechar é do dono do host.
- O `author`/`committer` do git é **assinatura de e-mail, não endereço de máquina**: quem escreve num repo se descobre pelo **reflog** e pelos **mtimes**.
- Número que pode mudar sem mim (percentual, saldo, contagem) **se lê do dado/painel, nunca se copia da nota anterior** — família da lição `20260910_porcentagem_herdada_da_nota_nao_e_medicao.md`.

## Como aplicar
1. Ao receber um relato de falha, perguntar primeiro: **em qual física o defeito é PRODUZIDO?** A barreira tem de estar ali.
2. Antes de endossar: **medir o mesmo caminho na minha física** e reportar sempre com a física explícita.
3. Percentual, saldo e contagem: ler do painel/arquivo no momento da ronda; jamais citar da ronda anterior.
4. Ao declarar uma mitigação «instalada», exigir **prova de que ela REPROVA** na física onde o dano nasce (teste T1 remoção → recusa; T2 união → passa; T3 fetch falha → exit 1).

## Família
BUG-178/185/196/197 + BUG-190/191/192/194 (o dado não vale sem a máquina) + lições `20260910_relato_de_outra_fisica_se_mede_na_sua.md` e `20260910_barreira_instalada_na_fisica_errada.md`.
