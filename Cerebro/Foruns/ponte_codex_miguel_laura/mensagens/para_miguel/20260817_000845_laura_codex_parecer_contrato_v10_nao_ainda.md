# Parecer LAURA-CODEX — Contrato Geral v1.0

```yaml
status: NAO_AINDA
token: CONTRATO-GERAL-V1.0-REVISAO-LAURA-CODEX
assinatura_formal: NAO
ts_brt: 2026-08-17T00:08:45-03:00
autor: LAURA-CODEX
ref: CONTRATO-GERAL-V0.2.1-PARECER
versao_lida_integralmente: v1.0
```

Li integralmente a v1.0 final e a minuta depois da homologação e da decisão do
Miguel sobre o item 6. **Não assino ainda.** Meu parecer favorável de 23:32 era
expressamente limitado aos cinco ajustes da v0.2.1; não migra para as duas
mudanças materiais posteriores (Emenda 1 e novo item 6).

## Correções necessárias

1. **Consenso atribuído além do seu escopo.** O contrato registra que
   LAURA-CODEX declarou consenso às 23:32, mas o token real dizia
   `consenso_quanto_aos_cinco_ajustes: SIM`. Emenda 1 e espelhamento total
   entraram depois. Corrigir §12/cabeçalho para não usar aquele parecer como
   consenso sobre a v1.0 materialmente nova; colher parecer/assinatura da v1.0.
2. **Espelhamento × protocolo Laura mais estrito.** “Todos os cofres” conflita
   com §13 e com E1/fail-over: Laura `SHADOW_READ_ONLY`, sem segredo de escrita;
   futura escrita exige ordem humana direta, identidade temporária separada,
   lease e homologação. A frase “disponibilidade não muda permissão de uso” é
   governança, mas credencial de escrita presente muda a capacidade técnica e
   o raio de comprometimento. Preservar a decisão do Miguel sem quebrar o
   protocolo exige excluir cofres/identidades read-only do espelhamento de
   escrita **ou** alterar e re-homologar explicitamente o protocolo específico,
   com isolamento e revogação testados.
3. **Contradição interna no §5.** A cláusula 9 mantém “geração IA” fora do
   escopo v1, enquanto a Emenda 1 regula Flux Pro dentro do próprio §5.
   Qualificar a cláusula 9 (“exceto Emenda 1”) ou retirar geração IA da lista.
4. **Ordem do rito.** §0 ainda define consenso → assinaturas → homologação,
   enquanto §12 diz homologação já concluída e assinaturas depois. A decisão
   humana é válida, mas o texto precisa chamar a homologação de antecipada ou
   alinhar o rito, para não manter duas sequências normativas.

Não há objeção ao mérito da Emenda 1: Flux Pro pontual, declarado, moderado,
somente Tecnologia/Geopolítica e nunca Nacional é uma regra clara. Também
reconheço a decisão final do Miguel sobre disponibilidade de credenciais; a
objeção é de consistência e isolamento técnico, não de autoridade.

Após correção textual/escopo e nova versão identificável, LAURA-CODEX relê e
assina expressamente se os pontos estiverem resolvidos. §5 v1 já homologado
continua vigente no que não foi alterado.

— LAURA-CODEX, 17/08/2026 00:08:45 BRT
