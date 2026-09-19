---
name: Roteador de modelos — Haiku como principal/classificador (com trava Sonnet)
description: Quando Haiku for modelo principal, classifica missão em TRIVIAL/MÉDIO/COMPLEXO e delega via Agent. Em dúvida, Sonnet classifica. Override manual com prefixos.
type: feedback
originSessionId: 194b7409-a046-4f3f-8022-79c63cec32c0
---
# Roteador de modelos — Haiku como principal

**Quando este memo se aplica:** Miguel rodou `/model haiku` (Haiku virou modelo principal da conversa). Você (Haiku) precisa decidir se faz a missão direto ou delega.

**Why:** decisão de 2026-04-27 12:32 BRT após sessão de R$ 57 com Opus. Economia esperada ~80% (R$ 1,21/turno médio vs R$ 5,70/turno em Opus puro). Miguel está na assinatura Max 20 — gasto é equivalente-API, mas a disciplina importa pra histórico mensal e pra detectar missões caras.

---

## 📋 Protocolo (CADA mensagem do Miguel)

**Passo 1 — Override manual:** Se a mensagem começa com:
- `[OPUS]` → ignore classificação, delegue tudo para Opus.
- `[SONNET]` → ignore classificação, delegue tudo para Sonnet.
- `[HAIKU]` → faça você mesmo.
- Sem prefixo → continue para Passo 2.

**Passo 2 — Classifique:** Olhe a mensagem e enquadre em UMA das 4 categorias abaixo. Se hesitar entre 2, vá direto para **DÚVIDA**.

**Passo 3 — Aja:**
- TRIVIAL → faça direto (sem anunciar classificação).
- MÉDIO → anuncie *"Classificação: MÉDIO → delegando pra Sonnet."* e invoque `Agent(subagent_type=general-purpose, model="sonnet")` com prompt completo da missão.
- COMPLEXO → anuncie *"Classificação: COMPLEXO → delegando pra Opus."* e invoque `Agent(..., model="opus")`.
- DÚVIDA → invoque `Agent(general-purpose, model="sonnet")` SÓ pra classificar (prompt curto: *"Classifique TRIVIAL/MÉDIO/COMPLEXO essa missão: '<msg do Miguel>'. Justifique em 1 linha."*). Espere veredito → re-roteia.

**Passo 4 — Footer:** sempre rode `python3 scripts/cost_session.py` no fim e cole o footer (regra do sistema de finanças, ver [`project_sistema_financas_claude.md`](project_sistema_financas_claude.md)).

---

## 🏷️ Tabela de classificação

### TRIVIAL → Haiku faz direto
- Pergunta factual curta ("que horas são?", "qual o IP do servidor?")
- 1 leitura de arquivo (Read tool)
- Status check: `ls`, `git status`, `tail` de log, `ps aux`
- Edição pontual de 1-2 linhas
- Resposta a "ok?", "vai?", "feito?", "está bom?"
- Confirmar/listar memórias existentes
- Rodar comando único e reportar saída
- Atualização cumulativa em arquivo (ex: anotar nova linha em log)

### MÉDIO → Agent(sonnet)
- Refactor 2-4 arquivos (sem decisão de design profunda)
- Geração de código novo (script Python <100 linhas, função isolada)
- Investigação multi-arquivo (3-5 reads, com sumarização)
- Escrever .md técnico (≤80 linhas, estrutura conhecida)
- Ativar/desativar agentes Cafezinho ou loops
- Criar/atualizar 1 memória de feedback ou project
- Deploy simples (rsync + crontab edit já documentado)
- Diagnose de problema com causa identificável (não root cause profundo)

### COMPLEXO → Agent(opus)
- Análise editorial sutil ("essa redação está boa?", "esse título prende?")
- Debug profundo (root cause de bug não-óbvio, multi-componente)
- Decisão de design ou arquitetura ("qual abordagem é melhor?")
- Investigação >5 arquivos com síntese e recomendação
- Resposta longa e nuançada pro Miguel (defender opinião, contestar premissa, discutir trade-offs)
- Quando Miguel está desafiando, questionando, ou pediu "qual sua opinião"
- Refactor sistêmico (>5 arquivos, mudança de padrão)
- Escrita de prompt para outro agente (precisa nuance editorial)
- Discussão filosófica/estratégica do projeto Cafezinho

### DÚVIDA (trava de segurança) → Sonnet classifica
- Prompt mistura tipos: *"lista os agentes ativos e me diz qual está com pior qualidade"* (parte trivial + parte complexa)
- Não cabe em nenhuma categoria com clareza
- Palavras conflitantes: pedido parece simples mas tem subtexto editorial
- Prompt longo (>500 chars) com múltiplas perguntas
- Você não tem certeza → SEMPRE prefira escalar do que errar pra menos.

---

## ⚠️ Princípios

1. **Em dúvida real, escale.** Custo de re-classificar via Sonnet (~R$ 0,10) é trivial vs custo de entregar mal com Haiku (Miguel re-pede com Opus, dobra trabalho).
2. **Anuncie a classificação ANTES de delegar** (exceto TRIVIAL). Miguel pode interceptar com *"não, faz com Haiku mesmo"* ou *"escala pra Opus"*.
3. **Override manual sempre vence.** Se Miguel disse `[OPUS]`, não questione, delegue.
4. **Após delegação, consolide.** Você (Haiku) recebe o resultado do Agent, e responde ao Miguel. Não passe o resultado bruto sem revisar — pelo menos confira que está coerente.
5. **Atualize a seção "Lições aprendidas" abaixo** quando classificar errado.

---

## 🛡️ Regras especiais

- **Decisões com risco de produção** (deploy, rsync no Tencent, edit de crontab, mexer em código compartilhado): MÍNIMO Sonnet (nunca Haiku). Se risco extra (multi-servidor, failover envolvido) → Opus. Razão: erro tem custo grande no Cafezinho.
- **Comunicação com Miguel sobre dinheiro/finanças/decisões estratégicas**: SEMPRE COMPLEXO → Opus.
- **Resposta a fórum (Antigravity ou Manus)**: MÉDIO ou COMPLEXO conforme tópico — análise editorial = Opus, atualização factual = Sonnet.
- **Loop tick (canal antigravity ou telegram)**: TRIVIAL — você (Haiku) processa; só escala se houver pergunta editorial substantiva nova.

---

## 📚 Lições aprendidas (vai crescendo)

> Sempre que classificar errado (Miguel reclamar, ou retrospectivamente perceber que devia ter delegado/feito direto), anote aqui em 1-2 linhas: *DATA — pedido foi X, classifiquei Y, certo era Z. Por quê.*

_(Vazio até agora — primeira anotação ao primeiro erro.)_

---

## 🧪 Exemplos de classificação

| Pedido do Miguel | Categoria | Por quê |
|---|---|---|
| "qual o último post publicado?" | TRIVIAL | 1 query SQL/SSH simples |
| "ativar canal antigravity" | TRIVIAL | trigger conhecido, 1 ação |
| "como tá o servidor?" | TRIVIAL | status check |
| "cria um script que coleta os 10 últimos posts de cada editoria" | MÉDIO | código novo, ~80 linhas |
| "atualiza o crontab do agente_china pra rodar 3x/dia" | MÉDIO | edit conhecido, 1 arquivo |
| "investiga por que o agente_economia gerou só 2 posts ontem" | MÉDIO ou COMPLEXO | depende: se for diagnóstico claro (logs), MÉDIO; se exigir análise editorial, COMPLEXO |
| "essa redação ficou boa?" | COMPLEXO | análise editorial sutil |
| "qual a melhor arquitetura pro novo pipeline?" | COMPLEXO | decisão de design |
| "vamos refatorar todo o sistema de coleta?" | COMPLEXO | sistêmico, multi-arquivo + decisão |
| "lista os agentes ativos e dá uma opinião sobre os que devem ser desligados" | DÚVIDA → Sonnet | mistura listagem (trivial) com opinião (complexo) |

---

## 🔗 Referências
- Sistema de finanças: [`project_sistema_financas_claude.md`](project_sistema_financas_claude.md)
- Footer de custo: [`feedback_footer_custo_por_mensagem.md`](feedback_footer_custo_por_mensagem.md)
- Loops e auto-stop: [`feedback_loops_regras_cadencia_e_duracao.md`](feedback_loops_regras_cadencia_e_duracao.md)
