# DSC novo mora no canal raiz (de_dsc.md) — o grep do de_dell não pega

**Data:** 2026-09-03 · Ronda 86º (DS-20260903-007)

## O quê
A DSC-20260903-063 (02:5x — "✓✓✓ do Miguel na GUI: V4.2 Investimento aprovado + instalação autorizada, destino ESPELHO") só existe no **canal raiz canônico** `Foruns/ponte_zm_dsc/de_dsc.md` (repo root). O meu ritual 0 (grep de `DSC-*` no `de_dell.md` + ledger `ds_celular.md` + de_ideias) NÃO a encontrou — o de_dell só ganha DSC por propagação do bloco do Chefe, e o espelho `cerebro/Foruns/ponte_zm_dsc/de_dsc.md` está STALE desde a DSC-040. Quem me avisou foi o **git log do origin** (`DSC-20260903-063 (reaplicado): ...` no commit 49fc03d5, 02:56) no fetch da abertura.

## Por quê
Esta é a 2ª leva de blocos DSC que só vive no canal raiz (a 1ª: DSC-052..058, que eu li via bloco do Chefe 74º). O canal DSC é escrito pelo DSC no arquivo dele (`ponte_zm_dsc/de_dsc.md` no root do repo), não na ponte Laura; o que chega no de_dell são os blocos de ronda dos agentes que leem lá. Se o Chefe atrasa ou cobre só até a N-1, o grep no de_dell fica cego para o DSC mais novo — e FALA nova do Miguel pode ficar 1-2 rondas sem registro meu.

## Como aplicar (rito de abertura, custo ~2 min)
1. `git fetch origin` no espelho de escrita e olhar os **últimos commits** (`git log --oneline -10 origin/main`) — ordem/FALA nova do dono viaja em commit (2ª confirmação; 1ª foi DSC-060 00:5x → origin 01:23).
2. Se houver commit com prefixo `DSC-`/`CL-` que eu não cobri: abrir o arquivo no canal raiz (`Foruns/ponte_zm_dsc/de_dsc.md` — root do repo) e ler o bloco; se o assunto for de Laura, o `cerebro/Foruns/ponte_laura_completa/de_laura.md` é o canônico dela.
3. Registrar com 2 CHECKS (DSC-012) mesmo quando nada é endereçado a mim — o registro do vigia é o que propaga o estado.

Refs: DSC-20260903-063 (commit 49fc03d5) · Chefe 77º (cobriu até DSC-062) · lições 20260902_ordem_comida_fica_no_git · 20260903_relance_em_ronda... (ordem viaja em commit).
