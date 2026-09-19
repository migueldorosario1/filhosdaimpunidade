# Ausência de leitura não é leitura de ausência

**Data:** 10/09/2026 (ronda 376ª DS-Dell) · **Origem:** 2 ocorrências no MESMO dia (09/09), mecanismos distintos.

## O quê
Em 09/09 a casa teve duas perdas/quase-perdas pela MESMA confusão lógica: um agente não conseguiu LER algo e tratou isso como um RESULTADO sobre o objeto.

1. **BUG-20260909-DS-180 (R1, verificação):** o revisor de fact-check marcou como «fato incorreto» premissas que não achou na busca (presidência de De la Espriella, coalizão «Escudo das Américas», captura de Maduro) — todas já publicadas pelo próprio site (264433 / 267271 / 224124 / 228979). «Não encontrei na minha busca» virou «não é verdade».
2. **BUG-20260910-DS-183 (dedupe, produção):** o ciclo das 23:25 barrou a maior nota da noite (8,21) com `cluster_inter_vertical:lista_publicados_indisponivel` — a lista de publicados não carregou e o ciclo barrou assim mesmo, como se falha de leitura fosse prova de duplicata. «Não consegui comparar» virou «já publicamos».

## Por quê (importa)
Os dois gates têm naturezas diferentes (um verifica fato, o outro evita repetição), mas os dois confundem **ausência de prova com prova de ausência**. O efeito é sempre o mesmo: o mecanismo que deveria proteger a casa vira o mecanismo que descarta pauta verdadeira — e o erro sai disfarçado de veredito legítimo («INCERTO», «dedupe»), então ninguém audita.

## Como aplicar
- Gate que não conseguiu ler deve devolver **estado explícito de falha** («não coberto pelas evidências desta busca», «lista indisponível»), nunca o veredito de mérito.
- **Barrar exige comparação feita:** sem comparação o veredito correto é «não sei» — e «não sei» reencaminha (reprocessar / levar ao humano), não descarta.
- Quem audita lê o **sufixo** do motivo (`curadoria_estado` após os dois-pontos), não só o prefixo: a régua dos baldes tem QUATRO (dedupe ok · filtro de qualidade ok · redator falhou · falha de infra disfarçada de filtro).
- O custo é assimétrico: descartar por falha custa pauta verdadeira (às vezes a maior da noite); reencaminhar custa um ciclo.

**Família:** 193ª (leitura única não é veredito) aplicada ao veredito do gate · irmãs por link: `20260907_peca_do_colchao_sem_evento_e_o_meta_cron_nao_e_prova.md`, `20260909_estado_lido_vence_estado_herdado.md`, `20260908_estado_de_producao_e_snapshot_com_hora.md`.
**Refs:** BUG-20260909-DS-180 · BUG-20260910-DS-183 · CL-20260910-001 (00:12) · feedback CL nº 254.
