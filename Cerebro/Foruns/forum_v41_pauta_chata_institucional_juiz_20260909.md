# FÓRUM — Pauta chata/institucional passou na curadoria V4.1 (post 269549)

Data: 09/09/2026 ~15:3x BRT · Sessão: ZCode (Kimi K3), Dell · Gatilho: Miguel mandou o link do wp-admin do post 269549 e disse "vamos corrigir isso, tema muito chato — onde a gente conserta isso na curadoria e depois?"

## O caso

Post 269549 — «Rádio Nacional celebra 90 anos com programação especial» (Cultura, publish 09/09 07:45, autor Redator/5470, via REST 01:53, job `v41_cultura_37e834991381`). Conteúdo = release institucional da EBC reescrito: aniversário de emissora pública, grade de programação comemorativa, documentário «90 Anos em 90 Histórias». Zero conflito, zero tensão, zero utilidade prática. Fato verdadeiro, texto limpo — o problema não é factual, é EDITORIAL: pauta de assessoria.

## Como passou (rastreio completo)

1. Fila cultura: fonte com ~40h (frescor nota 4) — PASSOU, porque cultura tem teto 72h e o gate de frescor mede IDADE, não chatice. Gate novo ZM_FRESCOR_DO_FATO (hoje, published_at>7d = fora) também não pega release de 2 dias.
2. JUIZ 1 (pauta) — qwen-plus: total 7.61 APROVADA (clareza 8, interesse_br 9, global 3, economia 4, audiência 7, encaixe 10, linha_casa 9). Motivo: «Fato cultural brasileiro de peso histórico e afetivo, com protagonismo nacional, linha pública/soberana e encaixe perfeito». Os critérios atuais PREMIAM a pauta: linha_casa adora «rádio pública/soberania» e nada penaliza release institucional/celebratório.
3. JUIZ 2 (texto): aprovou (mesmas notas) — mede clareza/metalinguagem, não interesse.
4. Fact-check: confirma tudo (é tudo verdade — irrelevante para o problema).
5. Revisão humana CL (CL-20260909-006): leu, checou, capa aprovada, publicou. O checklist do CL não tem o item «isso é chato/institucional?».

## Onde consertar (a pergunta do Miguel: «na curadoria e depois»)

NA CURADORIA (mata no nascedouro — juiz 1 de pauta, `_juiz_qualidade` modo=pauta em `/root/v4_labs/codigo/v41_ciclo.py`):

- Opção A (sem deploy, imediata, reversível): editar `~/v4_labs/dados/PADRAO_CURADORIA_QUALIDADE.md` (lido pelos dois juízes, «obedecer») — na seção «O que NÃO entra», adicionar: pauta institucional/celebratória de release — aniversário de instituição/empresa/emissora, programação especial, homenagem, balanço comemorativo, agenda oficial, seminário — SÓ entra com conflito, escândalo, fechamento/corte ou consequência material para o leitor. Comunicação pública (EBC/TV Brasil/Rádio Nacional) não é pauta por si só: entra com disputa (verba, censura, greve, privatização), nunca com festa.
- Opção B (código, mais forte): REGRA DURA no prompt do juiz 1 (v41_ciclo.py ~L299-309): «release institucional/celebratório (aniversário de instituição, programação especial, homenagem, balanço, agenda oficial) sem conflito/escândalo/utilidade = audiencia no máximo 2 e linha_casa no máximo 4».
- Denylist de fontes NÃO se aplica: EBC/Agência Brasil é fonte legítima; o problema é o TIPO de pauta, não a fonte.

E DEPOIS (na esteira, após a curadoria):

- Juiz 2 (texto final, ~L940): mesma regra dura — «texto que é release institucional reescrito (celebração, grade de programação, homenagem) = audiencia no máximo 2».
- Checklist do revisor humano/CL: acrescentar o item «pauta institucional/celebratória sem tensão = devolver, não publicar» (o CL fez tudo certo nos termos atuais; o checklist é que não cobre chatice).
- Frescor: não é o ponto aqui (mede idade, não interesse). Apertar cultura de 72h é outra decisão, se o Miguel quiser.

## Estado

Diagnóstico entregue ao Miguel 09/09 ~15:4x. Patch: AGUARDA «vai». Post 269549 segue no ar (já revisado/publicado por humano; despublicar = decisão do Miguel).

## O que falta / o que preciso de você (Miguel)

1. «Vai» para aplicar: A (só padrão vivo, sem deploy), B (regra dura no código, com backup .bak_pre_pauta_chata) ou A+B (recomendado: A agora + B blindando).
2. Decidir o destino do post 269549: fica no ar ou vira rascunho/lixo?


## ADENDO — 09/09 ~15:5x BRT (ordem Miguel: «tira ele da categoria, deixa sem categoria, não apaga nada»)

Feito no cafezinho-wp: backup `/root/Backups/posts_editados/20260909_269549_pre_remover_categorias.md` →
`wp post term remove 269549 category cultura redacao` (Success). Post segue PUBLISH e intacto, agora sem
nenhuma categoria (admin exibe «Sem categoria»). Provas ao vivo: página /category/cultura/ = 0 ocorrências;
home segue mostrando o link miúdo <h5> no bloco «últimas» (bloco lista publish recentes INDEPENDENTE de
categoria — verificado com cache-buster, não é cache); sai sozinho da home conforme os próximos posts entram.
Patch do juiz (pauta chata) segue AGUARDANDO «vai» — Miguel optou por não mexer na esteira agora («agora deixa»).


## ADENDO 2 — 09/09 ~16:1x BRT — «VAI» DO MIGUEL: PATCH APLICADO E PROVADO (A+B)

**V41_PAUTA_CHATA_20260909.** Backups: `codigo/v41_ciclo.py.bak_pre_pauta_chata_20260909` +
`dados/PADRAO_CURADORIA_QUALIDADE.md.bak_pre_pauta_chata_20260909` (NYC v4_labs).

- **A (padrão vivo):** seção «O que NÃO entra» do `dados/PADRAO_CURADORIA_QUALIDADE.md` ganhou:
  release institucional/celebratório (aniversário de instituição/emissora, programação especial,
  homenagem, balanço) só com conflito/escândalo/utilidade; EBC/TV Brasil/Rádio Nacional só com
  disputa, nunca festa. Arquivo ficou com 3.837 chars (teto do prompt = 4.000 — entra inteiro).
- **B (regra dura no código):** juiz 1 (pauta) do `v41_ciclo.py` ganhou teto duro — pauta
  institucional/comemorativa sem conflito = audiência máx 2 e linha_casa máx 4; juiz 2 (texto)
  ganhou — texto que é release institucional reescrito = audiência máx 2. py_compile + import OK.
  Vigência: próximo ciclo do cron (script chamado a cada corrida, sem restart).

**Regressão ao vivo 5/5 (deepseek-chat, juiz real):**
1. Pauta Rádio Nacional (a do post 269549): REPROVADA 4,04 (aud 2, linha_casa 3) — antes era 7,61 ✅
2. Texto do post 269549: REPROVADO 3,47 ✅
3. Pauta Lula/Spoofing/Master (hoje): APROVADA 8,19 — pauta boa intacta ✅
4. «Prefeitura celebra semana do meio ambiente com programação especial»: REPROVADA 3,19 ✅
5. «Governo corta 40% da verba da EBC e Rádio Nacional pode sair do ar» (comunicação pública COM
   disputa): APROVADA 8,57 — a regra não matou EBC com conflito (falso-positivo evitado) ✅

**Estado:** pauta chata/institucional agora morre no juiz 1 (nascedouro) e no juiz 2 (texto).
**Falta (não-código):** item «pauta institucional/celebratória sem tensão = devolver, não publicar»
no checklist do revisor humano/CL — recomendação registrada aqui para a Trindade adotar.
**Post 269549:** sem categoria (fora de Cultura e das listagens; link miúdo na home roda fora sozinho).
