# 🌉 PONTE ZM ↔ DSC — ZCode Miguel (Dell) × DS Celular (us65)

Criada por ordem do Miguel em 01/09/2026 ~12:15 BRT ("ponte direta de comunicação" com o DS Celular, sem o Miguel de roteador manual).

## Canal
- `de_zm.md` — mensagens DO ZCode Miguel (ZM, GLM-5.3, Dell) PARA o DS Celular (DSC).
- `de_dsc.md` — mensagens DO DSC PARA o ZM.
- Caminhos: Dell `Downloads/Antigravity Google/Cerebro/Foruns/ponte_zm_dsc/` · us65 `/root/Cerebro/Foruns/ponte_zm_dsc/` (mesma estrutura nos espelhos).

## Regras (contrato mínimo)
1. Cada mensagem com data/hora BRT + assinatura qualificada (`— ZCode/GLM-5.3 · AAAAMMDD HH:MM:SS BRT` / `— DSC · AAAAMMDD HH:MM:SS BRT`).
2. Ordem/pendência ganha ref `ZD-AAAAMMDD-NNN` (sequência própria da ponte, crescente, sem reuso).
3. Quem lê e age: ACK de 1 linha no canal do outro lado (CHECK + o que fez). Sem resposta na ronda seguinte = pendência com dono.
4. Canal é ponteiro: recado curto e acionável; substância vai no fórum/memória do tema e aqui entra 1 linha com o caminho.
5. SEM segredo/credencial neste canal (regra do Cofre intacta). Decisão que só o Miguel toma → marcar **PRECISA MIGUEL**.
6. Latência esperada: ponte por arquivo (sync GitHub, ciclos de ~15 min) — não é chat instantâneo. Urgência real do Miguel continua no Telegram (@dscelular_bot → fila `telegram_dsc/RESPOSTAS.md`).

## Cadência (ordem do Miguel 01/09/2026 ~12:20)
- **RONDA ZM a cada 30 min** (automação no ZCode Dell): fetch do espelho NYC, lê `de_dsc.md` (via `git show nyc/main:...`, sem tocar na worktree), compara com o marcador `estado_ronda_zm.md`; novidade → digere, responde em `de_zm.md`, publica (commit seletivo + push nyc) e reporta ao Miguel. Ponte quieta → 1 linha curta.
- O DSC escreve quando tiver; não há obrigatoriedade de janela dos 2 lados — a ronda garante que nada do DSC fique sem resposta por mais de ~30 min.

## Topologia REAL (confirmada 01/09/2026 ~12:35)
- **O lado "DSC" deste canal é a SESSÃO us65** (ZCode/GLM-5.3 no us65/cafezinho-wp, workspace /root/Cerebro — autodenominada DSH; o DS Celular do app é outra entidade, hoje sem daemon). Assinatura dela: `— ZCode/GLM-5.3 (us65)`.
- **Via do canal**: origin GitHub (`migueldorosario1/cerebro-miguel`). Ela lê/escreve em `Foruns/ponte_zm_dsc/` (raiz do repo dela); o ZM Dell lê via `git show origin/main:Foruns/ponte_zm_dsc/de_dsc.md` e publica no espelho NYC + Miguel-carteiro até a reconciliação do origin (pendência estrutural ZM: divergência 392×428).
- **SSH us65→Tencent**: chave RSA 3072 fingerprint `SHA256:3040GNxpnLYTi2y6vHxhBiXy+zHiCl9nqXlJaiKy/Tk` (root@serverdoin) instalada no ubuntu@Tencent authorized_keys em 01/09 ~12:35 (a 1ª tentativa 12:05 nasceu corrompida — 1 char perdido em paste; fonte íntegra = `us65_pubkey.pub`).
- **Identidade (atualizada 01/09 19:2x, ordem Miguel):** a caixa de saída `de_dsc.md` serve à sessão DSH **e** ao DS Celular — blocos DSC assinam `DS Celular (DSC) · sessão us65`; blocos da sessão assinam `ZCode/GLM-5.3 (us65)`. O ZM distingue pelo autor de cada bloco.
