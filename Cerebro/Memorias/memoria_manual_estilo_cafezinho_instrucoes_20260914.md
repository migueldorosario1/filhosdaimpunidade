# Memória técnica — Manual de Estilo Cafezinho para Claude/GPT (14/09/2026, ZCode/GLM-5.3)

## Missão

Ordem do Miguel: manual de estilo SÓ do Cafezinho (publicação de postagens), para colar nas instruções do Claude e do GPT (igual para os dois), sem citar nenhum outro projeto do ecossistema, sem hashtag e sem asterisco — texto limpo.

## Arquivos criados

- `Cerebro/Estilo/MANUAL_DE_ESTILO_CAFEZINHO_INSTRUCOES_20260914.md` — completo, 11.795 chars Unicode.
- `Cerebro/Estilo/MANUAL_DE_ESTILO_CAFEZINHO_INSTRUCOES_8K_20260914.md` — compacto, 7.996 chars (teto 8.000 do Custom GPT), mesmas regras.

## Fontes lidas e fundidas

1. `Cerebro/Estilo/MANUAL_DE_ESTILO_UNIFICADO.md` (v1.1.0, EMU-1 a 13) — núcleo comum + perfil B1 portal (títulos 9 regras, corpo E-E-A-T, frescor, esporte, tecnologia, fecho-papagaio EMU-13).
2. `Cerebro/Estilo/MANUAL_DE_ESCRITA.md` (v2.1.1, oficial da casa) — princípios, o-que-nunca-entra, anti-repetição, música, pontuação, ofício, checklist.
3. `Cerebro/Estilo/MANUAL_DE_ESTILO_GPT_INSTRUCOES_8K_20260909.md` — formato compacto anterior (referência de estrutura).
4. Regras vivas das memórias ZM (não estavam nos manuais): §137 rascunho+Redação+publish do chefe; proibição "exclusivo/com exclusividade" (título, corpo E tag); "uma pesquisa do Cafezinho teve acesso à íntegra" + levantamento de sigilo com data; título ~50 chars p/ push (notificação herda o título); crédito de foto SÓ no campo legenda; foto jornalística recente nunca retrato oficial; estrutura resumo externo (veículo no título, Brasil primeiro, crédito 2º-3º ¶, ~mil palavras, nunca inventar repórter); regras do parecer de revisão (inferência exige cruzamento, variação≠crescimento, 2º turno≠1º, quem chamou quem, benefício de A≠B, maioria das fontes, título não encobre movimento contrário); dúvida do leitor entra no corpo; zero markdown (asterisco/#) no post publicado; retificação com nota.

## Método e provas

- Redigido direto em texto puro (seções CAIXA ALTA numeradas, sem markdown). Primeira gravação saiu SEM acentos (erro) — regravada na hora com acentuação integral.
- Prova por Python (`len(s)` em code points) e grep: 0 `*`, 0 `#`, 0 menções a outros projetos (regex Origens|Filhos|Singularidade|Clodio|Rio Carta|MapaRio|GSN|Moka|Laura|Trindade = vazio).
- Versão 8K afinada por cortes de redundância (exemplos duplicados, checklist comprimido) até 7.996 chars, NENHUMA regra removida.

## Manutenção futura

- Mudança de regra: editar o COMPLETO e regerar a 8K à mão (as duas devem permanecer semanticamente idênticas).
- Novas ordens editoriais do Miguel entram como seção nova ou item numerado na seção correspondente, com data no fórum.
- Catalogação: linha no `CEREBRO_NODE_ESTILO.md` + entrada em `CEREBRO_NODE_ATUALIZACOES.md` + linha ✅ no `MONITORAMENTO_DE_TRABALHO.md`.

## Estado

PRONTO E ENTREGUE. O que falta: o Miguel colar nos destinos (Claude e GPT). Nada bloqueante.
