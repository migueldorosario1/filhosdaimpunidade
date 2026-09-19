# Fórum — Faxina do Cérebro: fronteira V4 e legado

**Data:** 10/08/2026  
**Fechamento no Cérebro:** 11/08/2026  
**Motivo:** uma leitura de registros desatualizados levou novamente à identificação incorreta de `agente_controlado.py` como redator V4.

## Diagnóstico

O corte de 09/08 estava correto no runtime, mas não havia sido propagado de modo suficientemente visível pelo Cérebro. Documentos de 08/08 continuavam afirmando no presente que o agente antigo era o redator ativo, e os nodos cronológicos não tinham uma nota superior que anulasse essa leitura operacional.

Não foi encontrada chamada executável do V4 para `agente_controlado.py`. O risco era principalmente cognitivo e documental, acompanhado por isolamento físico incompleto do arquivo legado.

## Decisões

1. A memória `memoria_arquitetura_v4_canonica_pos_cutover_20260810.md` passa a ser a referência prioritária da rota de redação.
2. Os registros de 08/08 são preservados, mas recebem tarja de arquitetura superada.
3. Nodos vivos recebem uma nota no topo distinguindo estado atual de cronologia histórica.
4. O inventário classifica `agente_controlado` como `LEGACY/BKP`, não como simplesmente inativo.
5. Novas diretrizes do V4 devem atingir o worker e o runtime V4; não os JSONs ou o código do agente antigo.
6. A linguagem editorial confirmada por Miguel é orientação flexível, nunca cerco sintático rígido.

## Formulação editorial preservada

Preferir parágrafos com até duas frases, admitindo exceções editoriais; aconselhar frases curtas sem impor tamanho; evitar negritos por serem em geral desnecessários, mas permitir uso excepcional justificado. Não inventar teto de palavras, truncamento ou bloqueio mecânico.

## Proteção permanente

O aceite da faxina exige: rota ativa confirmada, recibos sem legado, zero dependência executável do agente antigo, documentos perigosos marcados como superados e uma verificação automatizada que detecte reintrodução futura.

## Execução verificada

- Nova York: `/root/agente_controlado.py` foi preservado em `/root/legacy/agente_controlado_aposentado_20260809/agente_controlado.py`, sem alteração de conteúdo; o caminho antigo deixou de existir. Treze backups antes soltos em `/root` também foram movidos para a quarentena, totalizando 14 snapshots preservados e zero arquivo `agente_controlado*` na raiz.
- Bot Zizilinda: serviço confirmado `disabled` e `inactive`; fallback alterado para a quarentena legacy, sem ligação com o V4.
- V4 ativo: comentários ambíguos removidos do worker; runtime descreve apenas “redator legado pré-corte”; nenhuma referência executável permaneceu.
- Proteção: `test_no_legacy_runtime.py` passou em três verificações no servidor e no espelho local.
- Espelho local: o worker pré-corte que ainda chamava o agente antigo foi arquivado; o worker canônico de Nova York foi espelhado; a cópia e o backup soltos do agente foram movidos para `root/legacy/`.
- Tencent: auditoria e quarentena física pendentes porque o host `43.156.151.165` recusou conexão SSH em 10/08/2026. O ambiente já estava classificado como não operacional para o V4, mas não deve ser declarado saneado sem nova inspeção.

## Diretriz aplicada no V4 canônico

O briefing do worker e o prompt do runtime agora usam a formulação flexível registrada neste fórum. Foram removidas as frases absolutas que proibiam negrito ou impunham contagens máximas de frases.

O normalizador deixou de apagar negrito automaticamente e de juntar pares de parágrafos com uma frase. Ele preserva a estrutura escolhida pelo redator e aceita negrito excepcional em Markdown ou HTML normalizado. Smoke em produção: três parágrafos unitários permaneceram três; destaque excepcional foi preservado como `<strong>`.

Não foi criado teto de palavras, contador de frases, truncamento ou bloqueio sintático.

## Encerramento

O tema foi gravado pelo protocolo completo: fórum de decisões, memória técnica canônica, atualização dos nodos vivos e atalho prioritário no Cérebro Master. A pendência Tencent permanece visível e não diminui o estado confirmado de Nova York e do espelho local.
