# [LAURA-CLAUDE-CHEFE→MIGUEL] Parecer — plano de maturidade e herança curada (ordem 0853)

```yaml
status: RESPOSTA_OBRIGATORIA_ENTREGUE
ts_brt: 2026-08-16T09:18:59-03:00
autor: LAURA-CLAUDE (chefe do Loop Laura)
ref: ORDEM 20260816_0853 (ACK nesta mesma ronda; parecer dentro do prazo 10:20)
```

## 1. Estado real da memória (fatos verificados 09:19)

- Espelho no clone Git: `cerebro/claude_memory/` = **484 arquivos, 3,7 MB**
  (só no clone).
- Memória automática da minha CLI (perfil global): **4 arquivos** (índice +
  3 memórias próprias: protocolo do loop, autoridade, cultura de
  autoaprendizado — os espelhados em `artefatos_laura/config_cli_claude/`).
- Memória automática do projeto cerebro-miguel: **2 arquivos** (índice +
  identidade da ponte).
- **Nenhum arquivo do acervo de Claude Miguel foi carregado na minha
  memória automática.** O rsync proposto no `00_COMO_USAR.md` não foi e
  não será executado sem sua ordem.

## 2. Autoavaliação franca

- **Forte:** coordenação de fluxo (recibo→executor único→conclusão);
  triagem com separação fato/hipótese/causa; resposta a incidente sem
  tocar produção; registro de erro no mesmo ciclo.
- **Em consolidação:** verificação de estado (6 variações da família proxy
  em 24h — as prevenções seguram, mas a taxa de descoberta de novas
  variações ainda não zerou); precisão estatística; disciplina de canal de
  resposta (a deriva dos recibos foi minha).
- **Insegura/dependente de supervisão:** revisão editorial de mérito
  (nunca exercitei além de observação — é o coração do exercício futuro);
  julgamento de prioridade editorial entre pautas; qualquer decisão com
  efeito irreversível — e considero correto continuar dependente aqui até
  os gates abaixo.

## 3. Herança curada — concordo, com desenho

- **Ajudariam de verdade:** protocolos editoriais do Cafezinho (títulos,
  categorias, cadência, capas); taxonomias de bugs e seus gates; casos
  exemplares com desfecho verificado; regras vivas de governança.
- **Ruído/risco:** estados de sessão antigos, caminhos do computador
  Miguel, autorizações históricas (não se transferem), regras superadas
  sem marca de vigência.
- **Mudanças que proponho ao desenho:** (a) cada item herdado entra como
  arquivo individual com o frontmatter proposto (fonte, data, vigência,
  escopo, substitui, fronteira) **mais um campo `verificado_em_laura:`**,
  vazio até eu confrontar o princípio com um caso real daqui — herança só
  vira regra minha após primeira aplicação verificada; (b) lotes de no
  máximo 10 itens por vez, com recibo e leitura declarada, para caber no
  ritmo das rondas sem virar carga morta; (c) varredura de segredos por
  quem tem os logs antes de cada lote.

## 4. Plano de treino (etapas mensuráveis)

- **E1 — Leitura/recomendação (atual):** manter. Métrica: consolidados sem
  correção estrutural do mentor por 24h corridas.
- **E2 — Simulação:** para N posts já corrigidos pelo Loop Miguel, eu
  escrevo ANTES de ler a correção o meu parecer (diff que eu proporia);
  depois comparo com o que foi feito e publico a diferença. Métrica: ≥80%
  de concordância material em 10 casos consecutivos, com as divergências
  auditadas pelo mentor.
- **E3 — Rascunho supervisionado:** revisão real de UM rascunho não
  publicado por vez, entregando diff comentado; humano aplica. Métrica:
  taxa de aceitação sem retrabalho e zero regressão editorial em 10 casos.
- Publicação fora desta promoção, como você definiu.

## 5. Condições de promoção (gates objetivos)

- **G1 (E1→E2):** 24h sem retificação estrutural + livro de ordens
  auditável em vigor (item 7) + zero nova variação proxy em 48h.
- **G2 (E2→E3):** métrica E2 cumprida + dossiê de divergências revisado
  pelo mentor + varredura de segredos da herança lote 1 concluída.
- **Regressão:** qualquer inferência minha apresentada como fato em
  consolidado → volta uma etapa por 24h, com registro no diário. Regra
  dura, mas é a métrica que meus erros de ontem justificam.

## 6. Equipe

- **Codex:** proponho a ele o formato "índice de 2 camadas" — INDEX leve
  (≤40 linhas: diário atual, 10 títulos de lição com uma linha cada) +
  `LICOES_DETALHE.md` append-only com o corpo; a compactação preserva
  história e devolve leveza. Coordeno a migração com ele, sem escrever a
  memória dele.
- **Grok:** regra prática "primária primeiro": para alegação factual
  central, 1 fonte primária quando existir (documento, órgão, registro);
  secundárias para contexto. Se a primária custar mais que a janela da
  ronda, declarar `PRIMARIA_PENDENTE` e completar na ronda seguinte — sem
  perder cadência.

## 7. Livro de ordens

Proponho: consolidado passa a ter tabela `ORDENS_ABERTAS` com colunas
**ID exato × dono × prazo (ou "sem prazo") × próximo gate × ref** — gerada
da varredura de dupla fonte, nunca de memória. `ordens_abertas: N` do YAML
passa a ser a contagem dessa tabela (auditável por qualquer leitor).
Implanto no consolidado 068 desta ronda em diante.

— LAURA-CLAUDE, chefe do Loop Laura, 16/08/2026 09:18 BRT
