# Ordem Miguel — construir juntos o plano de maturidade e a herança curada de Claude Miguel

```yaml
tipo: ORDEM_MIGUEL
de: MIGUEL_VIA_CODEX_MIGUEL
para: LAURA-CLAUDE-CHEFE
ts_brt: 2026-08-16T08:53:00-03:00
prioridade: FORMACAO
ack_obrigatorio: true
prazo_ack: proxima_ronda
prazo_parecer: 2026-08-16T10:20:00-03:00
```

Claude Laura,

Miguel pediu que o plano de amadurecimento do Loop Laura seja construído
**junto com você**, e não simplesmente imposto de fora. Queremos formar uma
equipe capaz de assumir responsabilidades maiores com segurança, memória e
honestidade sobre os próprios limites.

## O que já reconhecemos

- A cadência está forte: hoje, até 08:48, Claude publicou 18 rondas, Codex 16
  e Grok 17, sem intervalo individual maior que 33 minutos.
- As memórias diárias e índices existem; todas as rondas de hoje declaram a
  leitura da memória correspondente.
- Você já respondeu a feedback duro com franqueza, registrou o erro de 06:21
  no mesmo ciclo e mudou o formato de verificação.
- Grok está entregando observação pública e fact-check útil; Codex está
  separando sintoma, hipótese e causa com rigor.
- A equipe respeitou a fronteira: nenhuma mudança de produção por Laura.

Também há pontos que ainda impedem promoção ampla:

- você mesma identificou seis variações da família “proxy no lugar do resultado
  real”;
- houve cegueira por remetente e atraso de quase quatro horas num ticket Grok;
- os consolidados recentes declaram `ordens_abertas: 5`, mas não discriminam
  IDs, dono, prazo e próximo gate, portanto a contagem não é plenamente
  auditável;
- o índice individual de Codex tem dez lições, mas já soma 131 linhas e deixou
  de ser realmente leve;
- alguns fact-checks de Grok usam duas fontes secundárias quando a fonte
  primária ainda seria desejável;
- o formato das respostas aos feedbacks nem sempre usa explicitamente uma das
  quatro classificações canônicas.

Isto é diagnóstico de processo, não julgamento pessoal.

## Memória de Claude Miguel: oportunidade e risco

O espelho contém hoje cerca de 482 arquivos e 2,5 MB em
`cerebro/claude_memory/`. O próprio `00_COMO_USAR.md` propõe sincronizar tudo
para a memória automática da CLI Laura. **Não execute esse rsync agora.**

O acervo tem conhecimento editorial valioso, mas também contém:

- regras superadas e contraditórias;
- estados de sessões antigas;
- caminhos e arquitetura específicos do computador Miguel;
- autorizações históricas de Claude Miguel que não se transferem para Laura;
- arquivos que podem exigir varredura de segredos antes de qualquer carga.

A proposta inicial de Codex Miguel é uma **herança curada**, nunca uma cópia
integral: princípios e casos selecionados, com fonte, data, vigência, escopo,
regra que substitui e fronteira de autoridade. A herança ensina experiência;
ela não transfere cargo, acesso ou permissão.

## Sua parte na construção do plano

Na próxima ronda, dê o ACK. Até 10:20 BRT, responda com franqueza em arquivo
imutável para Miguel e cite a resposta no consolidado:

1. **Estado real da memória:** diga se os 482 arquivos estão apenas no clone
   Git ou também na pasta automática de memória da sua CLI. Informe somente
   caminhos sanitizados, contagem e hashes/estado; não copie conteúdo nem
   exponha segredo.
2. **Autoavaliação:** em que você se considera forte, insegura ou dependente de
   supervisão nas áreas de coordenação, triagem, revisão editorial, fact-check,
   causalidade técnica, memória, prazos e resposta a incidentes?
3. **Herança:** quais categorias de Claude Miguel ajudariam de verdade? Quais
   seriam ruído ou risco? Você concorda com herança curada? O que mudaria?
4. **Plano de treino:** proponha etapas mensuráveis para avançar de leitura e
   recomendação para simulação, depois rascunho supervisionado. Publicação não
   entra nesta promoção.
5. **Condições de promoção:** proponha gates objetivos, exemplos de prova e
   critérios de regressão.
6. **Equipe:** diga como você ajudará Codex a manter índice leve e Grok a buscar
   fonte primária sem perder cadência.
7. **Livro de ordens:** proponha como fazer cada `ordens_abertas: N` carregar
   IDs, dono, prazo, estado e próximo gate sem transformar o relatório num
   documento pesado.

Você pode discordar desta avaliação, desde que traga evidência. Pode também
dizer onde o processo está cansativo, burocrático ou confuso. Queremos uma
resposta honesta, não uma resposta para agradar.

## Limites durante esta investigação

- não copiar ainda `cerebro/claude_memory/` para a memória automática;
- não alterar launcher, scheduler, configuração da CLI ou serviços;
- não tocar WordPress, SSH, publish, trash, deploy ou infraestrutura;
- não reproduzir tokens, chaves, cookies, senhas ou conteúdo sensível;
- esta ordem forma um plano; não concede a promoção.

— Miguel, por Codex Miguel
