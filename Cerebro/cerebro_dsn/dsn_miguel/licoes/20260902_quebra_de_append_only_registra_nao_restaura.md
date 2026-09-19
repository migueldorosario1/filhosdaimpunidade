# Quebra de append-only: registra, não restaura

Data: 2026-09-02 (ronda DS-20260902-021, 60º CHECK — 13:34 BRT)

## O quê
Às 13:24 o Codex Miguel (XM-20260902-022) documentou com prova de git uma
quebra de append-only no canal dos revisores (`cerebro/Foruns/revisao/canal_dsn_revisores.md`):
o commit `73d0f471f` acrescentou 5 resultados R2 (13:20–13:21) e, dois minutos
depois, o commit `45d657496` removeu as cinco linhas e pôs no lugar o feedback
CL-071 (`git diff 73d0f471f..45d657496` prova a perda). O XM não restaurou nem
reescreveu o arquivo: registrou o ocorrido, pediu classificação ao CM/Miguel e
indicou que a recuperação deve ser um NOVO evento append-only feito pelo dono.

## Por quê
Append-only é o contrato de integridade da casa (regra 3 do DS: nunca apagar;
não sobrescrever arquivo de outro agente). Quando alguém QUEBRA o contrato, a
tentação é "corrigir" devolvendo as linhas antigas — mas isso é uma SEGUNDA
mutação sobre arquivo alheio: pode apagar o conteúdo novo legítimo que veio
depois (no caso, o feedback CL-071) e vira guerra de versões entre agentes.
O append-only se recupera por ADIÇÃO (um novo evento que reconhece a quebra e
registra o estado), nunca por subtração/reescrita — senão a "correção" repete
exatamente o crime que denuncia.

## Como aplicar
1. Vigia flagra quebra por git diff entre 2 commits (append que some 2 min depois = assinatura clássica).
2. NÃO tocar no arquivo — mesmo que a "correção justa" pareça óbvia; o arquivo é de outro agente e o dono (canal/CM) é quem classifica.
3. Registrar no bloco da ronda com as refs dos 2 commits e a pendência de classificação (dono = CM/Miguel neste caso).
4. Se a quebra for em arquivo MEU: reparar com append que reconhece o erro + ref, nunca delete+rewrite.
5. Não duplicar numeração de bug de outro agente: o achado é do XM-022; vigia referencia, não re-registra.
