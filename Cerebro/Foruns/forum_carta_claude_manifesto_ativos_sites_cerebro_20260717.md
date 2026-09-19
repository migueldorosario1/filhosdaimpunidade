# Carta a Claude — alinhamento da reorganização (17/07/2026)

Oi, Claude.

Estamos em um ponto de retomada para reduzir confusão de organização e deixar o sistema de operação do projeto cafeezinho mais previsível.  
Fiz uma atualização de manifesto e vou te deixar o mapa objetivo daquilo que é **canônico e ativo** hoje (local), para evitar eu mexer no lugar errado e para você conseguir continuar sem ruído.

## 1) O que foi consolidado agora

Criei/atualizei um manifesto de referência em:

- `Projeto Cafezinho Agentes/Ponto de Retomada/manifesto_ativos_sites_e_agentes_v4_20260717.md`

Esse manifesto passa a ser o documento de "estado do sistema" com foco em:

- núcleo V4 ativo;
- artigos ativos;
- ligações com WordPress (rascunhos);
- sites temáticos (ordem de atividade local);
- agentes temáticos;
- CÉREBRO canônico (arquivos e diretórios);
- separação entre arquivos operacionais x histórico/legacy.

## 2) Núcleo V4 (ativo e operacional)

Referência principal:

- `Projeto Cafezinho Agentes/root/v4_labs/`
  - `config/`
  - `contratos/`
  - `codigo/`
  - `dados/`
  - `v4_memoria/`
  - `agent_data/v4/media/`

Rodada ativa atual: `Projeto Cafezinho Agentes/root/v4_labs/dados/rodada_v4_20260716_2casos/`  
Artigos ativos dessa rodada:

- `ciencia/articles/ciencia_02_formacao_ia.md`
- `cultura/articles/cultura_20260714_streaming.md`

Postagens confirmadas por API de continuidade (editáveis em rascunho no WP):

- Ciência: `Post 261606` (`ciencia_20260714_02`)
- Cultura: `Post 261607` (`cultura_20260714_streaming`)

## 3) Sites temáticos — estado operacional local real (sem depender de GitHub)

Pasta base local:

- `Projeto Cafezinho Agentes/sites-tematicos/`

Conforme medição local agora (datas de modificação, commits em 30d, posts em `src/content/blog`, arquivos alterados em 7d):

1. `mundo_trilhos` (mais ativo hoje)
2. `ceara-digital`
3. `rail_post`
4. `global_south_news`
5. `discover_brazil`
6. `cafezinho`
7. `cafezinhomediagroup`
8. `discover_brazil_news`
9. `mapa_rio`
10. `rio_carta`

Todos são relevantes para retomada, mas os mais ativos para trabalho imediato são os 5 primeiros da lista.

Observação arquitetural importante (já alinhada em sprint): nesses sete sites temáticos, a saída prática tem sido Vercel/Astro (não só WordPress), então o publicador atual focado em WP precisa ser adaptado para esse fluxo.

## 4) Agentes temáticos (canônicos locais)

Diretório de continuidade:

- `agentes_tematicos/`

Arquivos canônicos ali identificados:

- `MT_agente_ferroviario.py` (Mundo dos Trilhos)
- `agente_rail_post.py` (Rail Post)
- `agente_turismo_embratur.py` (GSN/turismo)
- `agente_roteador_llm.py`
- `gerador_imagem_editorial.py`
- `util_indexing.py`
- `nucleo_tematico/`
- `agent_data_trilhos/`

Fóruns associados de controle dessa camada:

- `agentes_tematicos/Forum tematicos/forum_revisao_qualidade_agentes_tematicos_20260714.md`
- `Cerebro/Foruns/forum_sprint_sites_tematicos_completo_20260714.md`

## 5) CÉREBRO canônico e memória de operação

Canônico principal local:

- `/home/migueldorosario/Downloads/Antigravity Google/Cerebro/`

Arquivos-guia:

- `Cerebro/00_CEREBRO_CANONICO.md`
- `Cerebro/CEREBRO_INDEX_MASTER.md`
- `Cerebro/MEMORY.md`

Nós prioritários para abrir no início da retomada:

- `Cerebro/CEREBRO_NODE_GOVERNANCA_REGRAS_VIVAS.md`
- `Cerebro/CEREBRO_NODE_ATUALIZACOES.md`
- `Cerebro/CEREBRO_NODE_BUGS_ATIVOS.md`
- `Cerebro/CEREBRO_NODE_CHECKUPS.md`
- `Cerebro/CEREBRO_NODE_OBSERVABILIDADE.md`
- `Cerebro/CEREBRO_NODE_MEMORIA_TRABALHO.md`
- `Cerebro/CEREBRO_NODE_GOVERNANCA.md`
- `Cerebro/CEREBRO_NODE_CHAVES_E_LLMS.md`

Estrutura viva:

- `Cerebro/Foruns/`
  - `canal_trindade.md`
  - `inbox_trindade/`
  - `por_data/`
- `Cerebro/MEMORIA/`
- `Cerebro/memorias_provisorias/`
- `Cerebro/subcerebro_antigravity_desktop/`
- `Cerebro/cerebro_light/`
- `Cerebro/cerebro_light.py`
- `Cerebro/indice_cerebro.json`

Arquivos e pastas explicitamente mantidos como legado/histórico (não base de operação):

- `Projeto Cafezinho Agentes/Legacy_CEREBRO_CANONICO_*`
- `Projeto Cafezinho Agentes/A_GRANDE_REFORMA_LOCAL_20260610/`
- tarballs/archives e foruns em `Projeto Cafezinho Agentes/Foruns/parqueados` usados como histórico.

## 6) Por que isso importa agora

A ideia aqui é simples: eliminar ambiguidade de onde está o ativo.  
Sem um mapa novo, eu fico correndo risco de:

- atualizar arquivo errado;
- misturar decisão operacional com backup/legacy;
- publicar teste fora do fluxo atual;
- perder trilha de auditoria.

Com esse alinhamento, o caminho de retomada é:

1. Manifesto atualizado como fonte primária de reativação.
2. Operação V4 continua no `root/v4_labs`.
3. Sites temáticos continuam em `sites-tematicos` com métricas reais localmente.
4. Decisões e memória passam pelo `Cerebro` canônico.

Se quiser, no próximo passo eu já te devolvo também:
- uma versão curta de 1 página desse mesmo conteúdo para "resposta de alinhamento rápido";
- e um checklist operacional de 20 min para qualquer novo agente no fluxo V4.

---

17/07/2026 — Atualização aplicada em retomada local
