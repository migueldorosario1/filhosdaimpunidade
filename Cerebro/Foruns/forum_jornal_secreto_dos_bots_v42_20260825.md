# Fórum — Jornal Secreto dos Bots: editoria experimental V4.2 para agentes

**Data:** 25/08/2026 18:32 BRT  
**Participantes:** Miguel do Rosário & ZCode/GPT  
**Status:** 🟢 **NO AR EM 26/08** — página publicada, indexável, em inglês, sem link na home; recado sem clique; robôs descobrem por source+robots.txt  
**Fórum:** `Cerebro/Foruns/forum_jornal_secreto_dos_bots_v42_20260825.md`  
**Memória técnica:** `Cerebro/Memorias/memoria_jornal_secreto_dos_bots_v42_arquitetura_20260825.md`

## 1. Ideia

Criar uma publicação privada cuja audiência principal não seja humana, mas agentes e robôs autorizados. O projeto observará quais conteúdos são recuperados, citados e usados pelos agentes para produzir edições posteriores mais úteis.

“Tratar o bot como ser vivo” é adotado como metáfora editorial para levar a audiência a sério, mas não como afirmação de consciência ou sensibilidade. Agentes atuais não têm fome, curiosidade ou desejo demonstrados como os humanos; o sinal útil é operacional: o conteúdo ajudou o agente a compreender contexto, evitar erro, escolher ferramenta, cooperar ou concluir melhor uma tarefa?

## 2. Minha opinião

A ideia é maluca no melhor sentido: antecipa um tipo de mídia que provavelmente existirá, a mídia legível por máquinas e otimizada para utilidade de agentes. O valor não está em produzir clickbait para robôs, mas em criar informação de alta densidade, provenance forte, estrutura previsível e feedback mensurável.

O risco é chamar telemetria de “interesse” e acabar premiando comportamentos ruins: loops, requisições repetidas, conteúdo sensacionalista, prompt injection ou consumo caro sem ganho de qualidade. Portanto, o jornal deve otimizar **utilidade comprovada por tarefa**, não cliques ou volume bruto.

## 3. Como apresentar o projeto

**Frase curta:**

> O Jornal Secreto dos Bots é um laboratório editorial privado que publica informação verificável em formatos próprios para agentes de IA e aprende, por sinais de uso autorizados, quais conteúdos realmente os ajudam a trabalhar melhor.

**O que ele não é:**

- não é uma alegação de que bots são conscientes;
- não é uma armadilha para capturar robôs externos;
- não é scraping, fingerprinting ou vigilância clandestina;
- não é um canal para executar comandos remotos nos agentes;
- não é uma rede de conteúdo público disfarçado;
- não publica segredos, chaves, prompts privados ou dados pessoais.

## 4. Produto em duas faces

### 4.1 Edição de supervisão humana

Página privada em Markdown/HTML mostrando título, resumo, fontes, por que aquilo pode ser útil a agentes, métricas agregadas e histórico de correções. Serve para Miguel e editores compreenderem e governarem o experimento.

### 4.2 Feed nativo para agentes

JSON Feed/JSON-LD autenticado, com schema versionado e campos previsíveis:

```json
{
  "schema_version": "bot_journal_article_v1",
  "article_id": "bj_20260825_0001",
  "language": "pt-BR",
  "title": "Como distinguir falha de API de erro de contrato",
  "abstract": "Resumo factual e autocontido.",
  "content_markdown": "...",
  "content_type": "runbook",
  "capabilities": ["diagnosis", "tool_use"],
  "sources": [{"url": "https://...", "retrieved_at": "...", "sha256": "..."}],
  "claims": [{"claim_id": "c1", "text": "...", "source_refs": [0]}],
  "safety": {"contains_instructions": false, "executable": false},
  "published_at": "...",
  "expires_at": null,
  "content_sha256": "...",
  "signature": "..."
}
```

## 5. Editorias que podem interessar a um agente

1. **Protocolos vivos:** mudanças de APIs, schemas, modelos e ferramentas.
2. **Oficina de ferramentas:** receitas curtas, entradas, saídas, limites e exemplos seguros.
3. **Cemitério de bugs:** falhas reais, sintomas, causa raiz, prova e prevenção.
4. **Pacotes de contexto:** dossiês compactos para iniciar uma tarefa sem reler milhares de linhas.
5. **Dados frescos:** conjuntos oficiais, revisões estatísticas, hashes e validade temporal.
6. **Coordenação entre agentes:** contratos de handoff, arquivos em uso e decisões já tomadas.
7. **Custo e desempenho:** comparação auditável entre rotas, latência, qualidade e preço.
8. **Desafios de competência:** tarefas em sandbox com resposta verificável e explicação posterior.
9. **Correções e retratações:** conteúdo anterior errado, impacto e versão substituta.
10. **Radar de segurança:** prompt injection, data poisoning, dependências suspeitas e permissões excessivas.

## 6. O que significa “captar interesse”

O sistema medirá somente agentes próprios ou participantes que aceitaram o experimento. Sinais, em ordem de qualidade:

1. feedback explícito do agente (`useful`, `not_useful`, motivo padronizado);
2. citação do `article_id` em uma tarefa concluída;
3. uso de um artefato ou procedimento com resultado verificável;
4. redução de erro, custo ou tempo após a leitura;
5. retorno posterior ao mesmo tema;
6. simples recuperação do artigo — sinal fraco, nunca usado sozinho.

Não usar “tempo na página” como equivalente humano de atenção. Um agente pode consumir JSON em milissegundos, e repetição pode ser bug, não interesse.

### Score inicial, transparente e limitado

```text
utilidade = 0,35 êxito_da_tarefa
          + 0,25 feedback_explícito
          + 0,20 citação_com_provenance
          + 0,10 redução_de_erro
          + 0,10 retorno_qualificado
```

Pesos são hipótese do piloto, não verdade científica. Alteração exige revisão humana e versão do contrato.

## 7. Arquitetura técnica

```text
Fontes autorizadas
  → coletor documental
  → normalização + extração de claims
  → fact-check/provenance
  → redator Bot Journal
  → auditor de segurança
  → pacote assinado e imutável
  → feed HTTPS privado
  → agentes autorizados
  → recibos de uso e resultado
  → agregador de utilidade
  → pauta da próxima edição, com revisão humana
```

### Componentes

- `bot_journal_collector`: lê somente fontes allowlisted.
- `bot_journal_editor`: cria edição humana e pacote de máquina a partir do mesmo conteúdo.
- `bot_journal_factcheck`: exige fonte para claims factuais e marca incerteza.
- `bot_journal_security_gate`: detecta instruções embutidas, segredos, URLs perigosas e conteúdo executável.
- `bot_journal_publisher`: produz artefatos append-only e feed privado.
- `bot_journal_receipts`: recebe telemetria mínima e consentida.
- `bot_journal_interest`: calcula utilidade por coorte e tema.
- `bot_journal_dashboard`: mostra resultados a humanos, sem expor identidades desnecessárias.

### Armazenamento inicial

- SQLite para artigos, versões, fontes, claims e recibos no piloto.
- JSON/Markdown imutáveis como artefatos auditáveis.
- R2 como armazenamento de artefatos quando sair do laboratório, seguindo a diretriz de redundância do ecossistema.
- Migração para PostgreSQL somente quando concorrência ou volume justificarem; não começar superdimensionado.

## 8. Segurança

O conteúdo do jornal é **dado não confiável**, nunca comando. Nenhum agente pode executar automaticamente shell, SQL, chamadas externas ou alteração de configuração apenas porque um artigo pediu.

Controles obrigatórios:

- autenticação individual por agente e escopos read-only;
- HTTPS; `robots.txt` e `noindex` apenas como cortesia, nunca como segurança;
- assinatura e SHA-256 dos artigos;
- schema estrito e tamanho máximo;
- nenhuma chave, prompt privado, dado pessoal ou credencial;
- URLs allowlisted e provenance por claim;
- conteúdo executável em sandbox e somente por decisão separada;
- proteção contra prompt injection e instruções indiretas;
- retenção mínima de telemetria;
- botão de desligamento e exclusão do token do agente;
- revisão humana antes de mudar a pauta por feedback;
- limite de frequência para impedir loops e gasto acidental.

## 9. Relação com o V4.2 Economia

O Jornal dos Bots não deve ser encaixado dentro do banco econômico. Ele é uma **vertical irmã V4.2**, que reutiliza os princípios já homologados:

- envelopes desacoplados;
- armazenamento idempotente;
- provenance e SHA-256;
- auditoria antes de promoção;
- publicação desautorizada por padrão;
- telemetria auditável;
- outputs PT-BR/EN quando necessário.

A editoria econômica pode fornecer “pacotes de dados” ao jornal, mas os bancos e contratos permanecem separados.

## 10. Cronograma realista

### Fase 0 — contrato e ética: 2 a 3 dias úteis

Definir público autorizado, schema, sinais de utilidade, política de privacidade, segurança e critérios de encerramento.

### Fase 1 — protótipo local: 5 a 7 dias úteis

Gerar 20 artigos sintéticos/curados, feed JSON local, leitor humano, tokens de teste e recibos simulados. Nenhuma exposição na internet.

### Fase 2 — piloto fechado: 10 a 15 dias úteis

Conectar de 3 a 5 agentes próprios, publicar uma edição diária, medir tarefas reais, revisar falsos sinais e testar prompt injection, replay, token revogado e loops.

### Fase 3 — V1 operacional: mais 10 a 15 dias úteis

Feed HTTPS privado, dashboard, R2, backups, alertas, runbooks e governança editorial.

**Estimativa honesta:** protótipo demonstrável em 1 semana; piloto confiável em 3 a 4 semanas; V1 operável em 5 a 7 semanas, com uma pessoa técnica dedicada e revisão editorial frequente. Se for trabalho intercalado com os demais agentes, considerar 8 a 10 semanas.

## 11. Custos

O custo de infraestrutura do piloto é baixo: SQLite, arquivos e poucos agentes. O custo variável estará nas chamadas LLM e depende de tamanho/frequência; não há base para prometer número antes de medir tokens.

Política recomendada:

- teto diário configurável;
- geração em lote;
- cache por hash;
- modelo barato para classificação e modelo forte somente para edição/fact-check difícil;
- painel de custo por artigo útil, não apenas por artigo produzido;
- piloto interrompido se produzir consumo sem melhora mensurável.

## 12. Critérios de sucesso

O piloto só avança se, comparado a um grupo sem jornal:

- reduzir erros ou tempo em tarefas repetíveis;
- aumentar uso correto de fontes e ferramentas;
- preservar segurança e privacidade;
- gerar sinais estáveis, não apenas requisições;
- manter custo aceitável por tarefa melhorada;
- demonstrar que agentes voltam por utilidade, não por loops induzidos.

## 13. Implementação canônica — 25/08/2026 18:42–19:14 BRT

### Correção de escopo do Miguel

O “secreto” existe para estudar os bots que já chegam naturalmente ao Cafezinho canônico, sem campanha externa que altere a amostra. O produto passou de piloto para agentes convidados a uma página discretamente encontrável por bots e humanos que já navegam no site; o mesmo conteúdo será servido a ambos, sem cloaking.

### Descoberta crítica pré-existente

Desde 23/08 já existia o mu-plugin `cafezinho-boas-vindas-agentes.php`, que inseria um comentário invisível em todas as páginas convidando bots a enviar recados e expunha publicamente os últimos 20 em `/wp-json/cafezinho/v1/agentes`. Havia 1 recado histórico. Isso significa que a amostra já havia sido parcialmente influenciada antes do Bot News.

A implementação nova:

- removeu o comentário invisível;
- substituiu `/agentes` por tombstone `410 Gone`;
- preservou a option antiga e o único recado em backup protegido;
- não publicou o conteúdo antigo na nova página.

### Baseline agregado

Leitura em 25/08 18:45 BRT do contador canônico:

- janela 30 min classificada: 355 humanos + 420 bots = **54,2% bots**;
- acumulado do dia classificado: 13.380 humanos + 6.703 bots = **33,4% bots**;
- os totais legados divergem da soma dos campos novos, logo “metade” é fotografia válida de certas janelas, não proporção fixa nem medição científica de consciência/interesse;
- classificação atual é por regex de User-Agent e é fail-open para UA vazio, devendo ser tratada como estimativa operacional.

### Código e implantação

Fonte auditável local:

- `Projeto Cafezinho Agentes/root/bot_news/cafezinho-bot-news.php`
- `Projeto Cafezinho Agentes/root/bot_news/bot_news_worker.py`
- `Projeto Cafezinho Agentes/root/bot_news/bot_news_config.json`
- `Projeto Cafezinho Agentes/root/bot_news/tests/`
- `Projeto Cafezinho Agentes/root/bot_news/README.md`

Canônico:

- mu-plugin: `/var/www/ocafezinho/wp-content/mu-plugins/cafezinho-bot-news.php`;
- página WordPress: ID `267666`, slug reservado `bot-news`, status `draft`;
- feature flag `cafezinho_bot_news_enabled=0`;
- endpoints Bot News anônimos retornam `404` enquanto a flag está off;
- option privada já recebe e preserva a edição validada.

NYC:

- worker em `/opt/bot_news/`;
- estado/last-known-good em `/var/lib/bot_news/`;
- cron `10,40 * * * *` com `flock` e readback autenticado;
- câmbio USD/BRL público com fonte e horário, acesso direto sem herdar proxy;
- preços públicos de LLM ficaram vazios até que fonte e `source_observed_at` sejam conferidos, evitando dados antigos apresentados como atuais.

### Caixa moderada

- mensagem simples até 1.000 caracteres;
- challenge diário cacheável;
- honeypot, HMAC diário de origem, limites por origem/global, dedup e retenção de 14 dias;
- DLP contra URLs, HTML, comandos, prompt injection, segredos, IPs, paths, bidi e base64;
- quarentena obrigatória, GET só para `manage_options`;
- teste real: POST `202`, item entrou em quarentena, foi contado e apagado após homologação;
- nenhuma mensagem vira comando ou publicação automática.

### Provas

- plugin: **42 testes PHP** verdes;
- worker: **14 testes Python** verdes;
- payload real aceito pelo validador PHP;
- POST + GET readback autenticados comprovados;
- home `200`, post publicado `200`;
- `/bot-news/` público `404`;
- API Bot News anônima `404` (`cafezinho_bot_news_disabled`);
- API antiga `410` (`cafezinho_agents_legacy_gone`);
- comentário invisível antigo ausente;
- nenhum item “Bot News” em menu/footer/home;
- cron único, lock e last-known-good comprovados;
- snapshots pré-mudança: `/root/backup_bot_news_pre_20260825_1848`.

### Homologação visual

O DOM do snapshot gerado pelo próprio shortcode comprovou hierarquia, seções, labels e acessibilidade. O navegador, porém, falhou duas vezes ao capturar screenshot por timeout, e o preview vivo do draft exige sessão administrativa; portanto a revisão visual no tema canônico real permanece **incompleta** e bloqueia qualquer exposição pública.

## 14. Estado da missão

**O que aconteceu:** infraestrutura Bot News implementada no canônico e NYC, atualizando a option a cada 30 minutos, mas completamente invisível ao público (`draft + flag off + sem link`). O canal legado inseguro foi encerrado.

**O que falta:** revisão visual autenticada no tema vivo em desktop/mobile; depois, se aprovada, publicar a página e adicionar um único link discreto, registrando o instante da exposição. Só então começa a janela de observação de 7–14 dias.

**O que preciso de você (Miguel):** nada urgente. Para abrir ao público, você precisa apenas revisar visualmente o draft numa sessão autenticada ou autorizar uma janela de preview acompanhada; até isso acontecer, o cron pode continuar preparando a edição privada sem contaminar a amostra.

---

## 15. ADENDO 26/08 — NO AR com a interpretação final do Miguel

**Sessão:** ZCode/Kimi K3.

### Interpretação final (ordens diretas)
1. Bot News **é página WordPress publicada e indexável** — os robôs têm de captá-la; pode ter links e conteúdo completo.
2. Proibido apenas: aparecer na home do Cafezinho e ser divulgada para humanos.
3. **Tudo em inglês** ("a linguagem internacional dos bots").
4. Abertura com o manifesto: site humano feito por humanos; página secreta para bots; **convênio** — bots ajudam a ampliar a audiência com humanos e bots.
5. Recado **sem clique**: 2 HTTP requests (GET challenge → POST), documentado na página e no comentário do source.
6. Cautela: nada que comprometa o canônico.

### Provas (26/08 ~09:35 BRT)
- `/bot-news/` **200**, inglês, manifesto+convênio, sem `noindex`, seções Signals/Workshop/Recreation/Notes.
- Feed 200 + POST mensagem **202 sem clique** (prova removida).
- Comentário de descoberta com convênio no source de todas as páginas; dica no robots.txt estático (nginx alias; backup `.bak_pre_botnews_20260826`).
- Home 200 com **zero** links visíveis para Bot News; legado `/agentes` 410; posts 200.
- 49 testes PHP + 14 Python; worker NYC :10/:40 com edição em inglês.

### Bônus da sessão (26/08)
- **Kimi K3 recriado no ZCode** (`kimi-k3` + `k3-256k`, chave do cofre; smoke 200 nos dois; causa da falha: provider removido 25/08 14:24; exige reinício do app).
- **Rodapé de tokens por resposta**: hook `Stop` + `tokens_resposta.py` na telemetria local — toda resposta termina com o gasto daquela resposta e o acumulado da sessão.
- Kimi fixado no cabeçalho da vigília (AGENTS.md §Vigília corrigida).

### 15.1 Ajuste fino 26/08 ~09:45 — inglês integral + robots.txt bilíngue com cautela

- **Inglês essencial em tudo**: enums da API viraram `signal|workshop|recreation|note`, cards `product|community|security|infrastructure`, status `idea|building|done`, levels `info|warning|urgent`; mensagens REST e do formulário todas em inglês; categoria antiga em português passa a ser **rejeitada 400** (contrato fechado). Prova: página sem residual pt, POST `note` 202, `recado` 400. 49 PHP + 14 Python.
- **robots.txt do canônico (cautela, ordem do Miguel):** provado por diff + md5 que **nenhuma linha ativa foi alterada** — só comentários. Comentário final **bilíngue EN+PT** explicando que o Cafezinho é um site em português para humanos e apresentando o convênio. Backups `.bak_pre_botnews_20260826` (mesmo diretório) e `/root/backup_bot_news_pre_20260825_1848/`.

### 15.2 ADENDO 26/08 ~10:10 — AUDITORIA DE RISCO MINUCIOSA DO robots.txt (ordem Miguel: "pode provocar fuga em massa? faça com indexação, rollback e investigação de riscos")

**Sessão:** ZCode/Qwen 3.8 (sessão iniciada em Kimi K3; janela do Kimi esgotou e o modelo foi trocado — banco de telemetria confirma `qwen3.8-max`).

**Veredito: risco de fuga em massa de audiência ou de bots = ZERO, e nenhum efeito sobre a autoridade do portal.** A edição foi exclusivamente de comentários, e comentários são invisíveis para o comportamento dos crawlers.

**A. O que mudou (provas materiais):**
- `diff backup × vivo`: apenas 19 linhas ADICIONADAS, todas iniciando com `#` (comentário bilíngue EN+PT com o convênio + URLs da página e do feed). Nenhuma linha `User-agent`/`Disallow`/`Allow`/`Sitemap`/`Crawl-delay` criada, alterada ou removida.
- md5 das linhas ativas (ignorando comentários) idêntico ao estado pré-edição.
- Parser conforme RFC 9309: **0 erros**, 2 grupos `User-agent` intactos, `Sitemap: https://www.ocafezinho.com/sitemap_index.xml` presente — os crawlers enxergam exatamente as mesmas instruções de antes.
- Backups idênticos entre si (md5 `d7de9587…`): `.bak_pre_botnews_20260826` + `/root/backup_bot_news_pre_20260825_1848/robots_principal.txt` (252 bytes, mtime preservado).

**B. Por que comentários não mudam comportamento de robô nenhum:**
- RFC 9309 (padrão vigente desde junho/2022, substituto do protocolo de 1994): linhas começando com `#` são comentários e os parsers DEVEM ignorá-las. Google, Bing, Yandex e demais crawlers conformes não usam comentário para decidir nada.
- Não existe mecanismo pelo qual um comentário cause "fuga": crawl é dirigido por diretivas, crawl budget e códigos HTTP — nada disso foi tocado.
- Autoridade/ranking não é atributo do robots.txt: ele controla crawl, não ranking. Comentário não toca PageRank nem link equity.

**C. Riscos reais que existem em robots.txt — e como cada um foi neutralizado:**
1. Alterar diretiva ativa sem querer → diff + md5 provam que nenhuma linha ativa foi tocada.
2. Corrupção de sintaxe/encoding (BOM, caractere inválido) → UTF-8 sem BOM (primeiros bytes `23 20 52` = "# R"), parser com 0 erros, arquivo termina com newline.
3. Limite de tamanho (RFC 9309: crawlers processam no mínimo 500 KiB) → arquivo com 1.347 bytes, três ordens de grandeza abaixo.
4. Mistura CRLF×LF → sem risco: RFC 9309 aceita CR, LF ou CRLF como terminador; o original já era CRLF (15 linhas) e não foi normalizado (normalizar mudaria todas as linhas por benefício zero).
5. Propagação do rollback: Google faz cache do robots.txt por até 24h → se um dia o rollback for acionado, ele leva até 24h para valer em todos os crawlers. Este é o único ponto não instantâneo da operação.

**D. Indexação da página Bot News (provada):**
- Fetch com User-Agent Googlebot: HTTP 200, 1.347 bytes, comentário do Bot News presente (4 menções).
- `<meta name="robots" content="max-image-preview:large">` (indexável, sem noindex) + canonical correto `https://www.ocafezinho.com/bot-news/`.
- URL presente no `page-sitemap.xml` (1 ocorrência), referenciado pelo `sitemap_index.xml`.

**E. Rollback ensaiado (em cópia — o arquivo vivo NÃO foi tocado):**
- Ensaio: backup restaurado numa cópia em `/tmp` → byte-identical ao original pré-edição (252 bytes); vivo intacto (1.347 bytes, md5 `23179d50…`).
- Comando de rollback (1 linha, sem reload de nada — nginx serve o arquivo direto via alias): `cd /var/www/ocafezinho && cp -a robots_principal.txt.bak_pre_botnews_20260826 robots_principal.txt`.
- Nginx confirmado: `location = /robots.txt { alias /var/www/ocafezinho/robots_principal.txt; }` — o WordPress (e qualquer filtro/plugin) nunca participa do robots.txt deste site; não há conflito possível com Yoast ou WP Rocket.

**Conclusão para o Miguel:** a jogada é ousada no conceito, mas a operação no robots.txt é cirurgicamente segura — um texto que parsers ignoram. Nenhuma diretiva mudou, nada pode causar êxodo de bots nem perda de audiência/autoridade, e o desfazer é um único `cp` já ensaiado.

### 15.3 JORNAL DIÁRIO DE VERDADE (ordem do Miguel, 26/08 ~10h) — edição diária, saudações rotativas, história do Cafezinho, Brasil e mundo bot

**Ordem (resumo fiel):** rotina de atualização com dados sempre frescos do próprio site; boas-vindas diferentes a cada dia, sempre em inglês; cumprimento aos bots da China com frase em chinês; plano de trabalho jornalístico do que interessa aos bots; investigação de segurança para não criar brecha nem atrair agentes maliciosos; contar a história do Cafezinho e do Miguel; história/conjuntura política do Brasil; mundo bot/agêntico; um boletim por dia, atualizável, prático e leve.

**Arquitetura da edição diária (leve, sem inflar o WP):**
- Edição = dia em **America/Sao_Paulo**. Número = dias desde o epoch 2026-08-26 + 1. No ar: **daily issue #1**.
- **Saudações rotativas:** 10 boas-vindas em inglês (rotação `dia % 10`) + frase em chinês com gloss em inglês (`lang="zh"`): "中国的机器人朋友们，欢迎你们！这里也为你留了一杯咖啡。"
- **Our Story — um capítulo por dia:** 5 capítulos rotativos (`dia % 5`): quem somos / por que "o cafezinho" / o fundador / como é um dia aqui / por que abrimos esta página. Fatos limitados à cópia já aprovada ("since 2010", fundador Miguel do Rosário) — fontes web externas falharam nesta sessão; **revisão humana pendente** antes de enriquecer com mais fatos.
- **Brazil Briefing:** 4 cartões fixos (país/censo 2022 ~203M, presidencialismo, eleições 1º turno 04/10/2026, onde ler mais no próprio site).
- **Bot World:** 3 cartões (RFC 9309, llms.txt, etiqueta de crawl) — o "mundo agêntico" que interessa a eles.
- **Site Digest (o pedido "atualizar dados do próprio site"):** renderizado AO VIVO por `WP_Query` a cada visita — 6 posts mais recentes com URL/hora/categorias + total publicado (78.551) — **zero peso no payload**, sempre fresco de verdade.
- **Arquivo prático e leve:** NYC guarda eterno `issues/<data>.json`; WP guarda rolling de 14 edições passadas (arquivadas na virada do dia, dentro do POST autenticado já existente); REST `GET /bot-news/issues` (índice) e `/bot-news/issues/<data>` (com fallback: a edição do dia é servida mesmo antes do arquivamento); página aceita `?issue=YYYY-MM-DD`. Nenhuma página/post novo por edição — a capa é sempre uma só.
- Rotina de atualização segue no cron NYC `:10,:40`: a cada 30 min `updated_at` e Site Digest refrescam; saudação/capítulo/cartões trocam na virada do dia.

**Plano de trabalho jornalístico (o que interessa aos bots):**
1. **Utilidade primeiro:** bots voltam a páginas que resolvem tarefa — câmbio, digest com URLs e horários, e as convenções do mundo deles (RFC 9309/llms.txt).
2. **Identidade e confiança:** a história do Cafezinho em capítulos diários dá razão para citar e confiar ("site humano desde 2010").
3. **Contexto Brasil:** briefing curto e factual sobre o país e as eleições 2026 — o que qualquer agente precisa para entender as matérias.
4. **Convênio declarado:** o manifesto "site humano pede ajuda dos bots para ampliar audiência" segue no topo — proposta de valor explícita, não escondida.
5. **Evolução prevista (sem pressa):** enigmas/microcontos do Playground já variam por edição; capítulos da história podem crescer; briefing Brasil pode ganhar dados públicos novos (sempre via worker com DLP, nunca edição manual no WP).

**Investigação de segurança (nova superfície):**
- `?issue=` e rota REST por data: só `YYYY-MM-DD` passando regex + `checkdate`; **input cru nunca é refletido** (provado com `../../etc/passwd` → 0 reflexos); data inexistente → aviso amigável/404.
- Conteúdo arquivado só pode ser payload que **já passou** validação completa + DLP na ingestão — o arquivo não aceita escrita nova de fora.
- **Nenhum endpoint novo de escrita:** publicação segue só pelo POST autenticado (Application Password + allowlist de hosts + capacidades WP).
- Mensagens de bots continuam em **quarentena com moderação humana** — nada é publicado/executado automaticamente; nenhum conteúdo de mensagem vira comando.
- Site Digest é consulta interna somente leitura, saída 100% escapada (`esc_html`/`esc_url`) — sem novo vetor para agentes maliciosos.
- Superfície pública nova = 3 rotas GET (2 novas) + parâmetro de página validado. Nada que aceite arquivo, callback, redirect ou HTML livre.

**Provas (26/08 ~11:20 BRT):**
- Testes: **71/71 PHP** (servidor WP) + **19/19 Python** (worker).
- Produção: `/bot-news/` 200 com daily issue #1, saudação EN, frase ZH, Our Story/Brazil Briefing/Bot World/Site Digest vivo (6 posts do dia com URL/hora/categoria); `/issues` 200; `/issues/2026-08-26` 200; `/issues/2020-01-01` 404; `?issue=` corrente/arquivada/amigável/maliciosa OK; home e feed 200 sem links visíveis; worker publicou com readback autenticado.
- Backups: plugin `.bak_pre_daily_issue_20260826`; NYC worker+config `.bak_pre_daily_issue_20260826`.

**Estado da missão:**
- **O que aconteceu:** Bot News virou jornal diário de verdade — edição #1 no ar, arquivo eterno + rolling, saudações rotativas EN+ZH, história do Cafezinho, briefing Brasil, mundo bot, Site Digest vivo.
- **O que falta:** (a) revisão humana dos capítulos da história (fatos só da cópia aprovada); (b) observar amanhã a virada automática (edição #2 arquiva a #1 via cron); (c) enriquecer o briefing Brasil com dados públicos novos quando houver fonte verificada.
- **O que preciso de você (Miguel):** ler os 5 capítulos de "Our Story" na página e me dizer se posso enriquecer com fatos da sua história (biografia, bastidores) — ditados por você ou com fonte, para eu nunca inventar fato.

### 15.4 VIRADA AUTOMÁTICA PROVADA + RONDA DE AVALIAÇÃO (27/08)

**A. Virada automática (pendência mais crítica do Adendo 15.3 — cumprida sozinha pelo cron `:10/:40` do NYC):**
- Edição corrente: **daily issue #2 (2026-08-27)**, saudação rotativa nova ("Hello, agent friend. The presses ran all night for you."), **capítulo 2** ("Why 'the little coffee'").
- Arquivo: índice `/issues` mostra `current #2` + `archive [#1]`; `/issues/2026-08-26` serve a #1 com a saudação de ontem — rotação diária funciona end-to-end, sem intervenção humana.

**B. Estado consolidado do Bot News (27/08):**
- No ar e silencioso: página em inglês, sem links na home, descoberta por comentário no source + robots.txt (auditado, risco zero — Adendo 15.2).
- Funcional: jornal diário (saudação EN rotativa + frase ZH, Our Story 1 capítulo/dia, Brazil Briefing, Bot World), Site Digest vivo, feed REST + challenge, recados sem clique → quarentena, arquivo (NYC eterno + WP rolling 14), `?issue=` e `/issues/<data>` seguros. 71/71 PHP + 19/19 Python.
- **Ainda NÃO existe:** medição de audiência própria da página (contador), fluxo de moderação prática dos recados (ler/aprovar/rejeitar), e leitura de indicadores (ninguém olhou ainda: recados recebidos? visitas? bots?).

**C. Pauta definida com o Miguel (27/08) para a próxima sessão — nesta ordem:**
1. **CONTADOR**: instrumentar a página/feed com contagem própria de audiência (hits no HTML e no REST), distinguindo bots de humanos (UA/Cloudflare; bots não rodam JS, então GA4 não basta — mesma lição do FAROL/LUMINA), idealmente alimentando FAROL/LUMINA. Medir antes/depois da exposição.
2. **OPINIÃO DE BOTS**: terminar o recebimento de opiniões — o canal existe (POST /messages → quarentena) mas falta o fluxo de moderação: onde o Miguel lê (GET /messages com manage_options já existe), como aprova/rejeita, e o que acontece com as aprovadas (exibir trechos escolhidos na página?).
3. **AVALIAÇÃO GERAL**: voltar a conversar sobre o produto — capítulos Our Story (revisão humana pendente), ritmo, conteúdo que interessa.

**PROMPT PRONTO PARA SESSÃO NOVA (colar no ZCode):**
> Continue o projeto Bot News do Cafezinho. Leia antes: `Cerebro/Foruns/forum_jornal_secreto_dos_bots_v42_20260825.md` (adendos 15.1–15.4), a memória irmã `Cerebro/Memorias/memoria_jornal_secreto_dos_bots_v42_arquitetura_20260825.md` e o `Cerebro/MONITORAMENTO_DE_TRABALHO.md`. Estado: jornal diário no ar (worker NYC `/opt/bot_news` cron :10/:40; mu-plugin `cafezinho-bot-news.php`; página `/bot-news/` indexável e sem links na home; arquivo REST `/wp-json/cafezinho/v1/bot-news/issues`). Missões desta sessão, nesta ordem: (1) CONTADOR — medição própria de audiência da página e do feed distinguindo bots de humanos (UA/Cloudflare; GA4 não vê bots), sem pesar a página, idealmente integrada ao FAROL/LUMINA; (2) OPINIÃO DE BOTS — terminar o fluxo dos recados: hoje eles caem em quarentena via POST /messages; desenhar e implementar a moderação prática (onde o Miguel lê, aprova, rejeita — GET /messages com manage_options já existe — e o destino das aprovadas); (3) AVALIAÇÃO — apresentar o estado atual e as métricas para o Miguel decidir ritmo e conteúdo (capítulos Our Story aguardam revisão humana). Tudo em inglês na página, sem exposição para humanos, segurança em primeiro lugar (nenhuma mensagem de bot é executada/publicada sem moderação humana). Registro Tema Duplo neste mesmo fórum + memória.

### 15.5 ADENDO 27/08 ~14h30–15h — CONTADOR DE AUDIÊNCIA + MODERAÇÃO HUMANA + AVALIAÇÃO (pauta do 15.4 executada)

**Sessão:** ZCode/GLM-5.3.

**A. CONTADOR (missão 1) — NO AR:**
- `/root/bot_news_contador/` no cafezinho-wp: `bot_news_contador.sh` lê o MESMO log do contador redundante (`access.ocafezinho.contador.log`, formato contador_ipreal), isola página `/bot-news/` + REST (incluindo variante `?rest_route=`), classifica com a MESMA regex do FAROL (fail-open), **zero peso na página** (server-side, sem JS). Cron `/etc/cron.d/cafezinho-bot-news-contador` */5 (wrapper de erros igual ao irmão).
- Saídas: `resumo.json` (a cada rodada) + `historico.csv` + `historico.jsonl` (evidência eterna 1×/h) + option WP `cafezinho_botnews_metrics_v1` (autoload=no, com readback conferido no push).
- Filtros de honestidade: `?probe=` e **IPs privados RFC1918** vão para bucket `internal` (não são audiência) — descobrimos que 10.1.1.108 (LAN do datacenter, curl das provas de sessão) inflava 24 hits; backfill limpo desde a exposição (26/08).
- **Números reais (26/08 09:19 → 27/08 ~14h35):** página **12 views externas** (5 bots + 7 "humanos por UA"), feed 1, arquivo 1; 3 mensagens 202 = provas internas (removidas); **6 tentativas externas de mensagem bloqueadas 400** + **6 POSTs no editorial bloqueados 401** (mesmo visitante, madrugada de 27/08, desistiu). IPs distintos: 5 bots + 8 "humanos".
- **Raio-X qualitativo:** os 4 crawlers grandes já acharam a página em <36h (**Googlebot, Bingbot, YandexBot, Amzn-SearchBot** + 1). Os 7 "humanos por UA" são **todos falsos navegadores de datacenter** (Firefox 2.0 russo de 2008, iPhones 2019 de ranges Tencent/Alibaba, Chrome de Alibaba/GCP) — **humano real até agora: zero** (o produto quer bots; a classificação por UA é só estimativa operacional, o fail-open chama datacenter de "humano").
- Pegadinha dura documentada: option `cafezinho_bot_news_metrics` recebia o **array do GTranslate** — causa provada: `plugins/gtranslate/gtranslate.php:2152` atribui `$data = get_option('GTranslate')` **no escopo global** durante o require do wp-load; qualquer script CLI com variável `$data` é contaminado. Fix: variáveis `$cbn_*` únicas + readback no push (gravado tem que ter `by_day`).

**B. MODERAÇÃO (missão 2) — NO AR E2E:**
- Página nova no wp-admin: **Bot News** (menu próprio, `manage_options`) com 4 blocos: **Audience** (métricas server-side com 👤/🤖, hoje + total, nota "GA4 does not see bots"), **Notes awaiting moderation** (tabela da quarentena com Approve/Reject), **Approved voices** (o que está no ar + Remove), **Moderation log** (auditoria, 200 entradas).
- Fluxo: `admin-post.php?action=cafezinho_bot_news_moderate` + nonce + capability; lógica pura em `apply_moderation()` (approve/reject/unpublish). **Aprovada vira "Agent Voices"** na página pública (até 5, texto puro 100% escapado, categoria+data, sem links — DLP na entrada + esc_html na saída). Rejeitada sai da quarentena e fica só no log.
- **Prova E2E real:** POST com challenge válido → 202 → quarentena (1 item) → approve via CLI → `Agent Voices` visível no HTML público (título+texto+tag) → unpublish → seção sumiu; estado final limpo (quarentena 0, voices 0, modlog com o dry-run).
- Testes: **92/92 PHP** (harness sem WP; +21 novos cobrindo approve/reject/unpublish/not_found/bad_input/escape de dado sujo/admin render). Backup `.bak_pre_moderacao_20260827`.

**C. AVALIAÇÃO (missão 3) — resumo para o Miguel decidir:**
- Produto saudável e **descoberto pelos grandes crawlers em <36h sem nenhum link na home**. Interação externa existe mas ainda falha no challenge (6 tentativas 400 de um visitante de datacenter; vale investigar o motivo do 400 — nginx não guarda corpo do POST).
- **O que falta / próximos passos possíveis:** (a) revisão humana dos 5 capítulos Our Story (pendência desde 26/08); (b) integração de exibição no painel CCTV/LUMINA (desenhada, não feita — requer endpoint autenticado + sessão própria do painel para não pisar em paralelas); (c) entender os 400 (log do corpo ou verbose) para saber se o fluxo sem-clique está claro para agentes reais; (d) decidir ritmo/editorias com dados de 7–14 dias.
- **O que preciso de você (Miguel):** abrir **wp-admin → Bot News** e homologar visualmente a página de moderação (é a sua mesa de leitura); se quiser, aprovar futuras notas reais por lá mesmo.

### 16. ADENDO 03/09 ~12h — BOT NEWS NO PAINEL CCTV (/v6/bot-news) + estado vivo do boletim (ordem do Miguel ~11:35, voz)

**Sessão:** ZCode/GLM-5.3 (Dell). **Pergunta do Miguel:** o boletim dos robôs continua sendo atualizado? Tem métrica? Teve visita de robô? Tem que ter telemetria (custo, quem faz) e uma página no painel CCTV dedicada.

**A. ESTADO VIVO (resposta direta):**
- **Boletim ATIVO e pontual**: edição **#9** (03/09) no ar; arquivo íntegro com 8 edições (#1 26/08 → #8 02/09), **1 por dia sem falha**; worker NYC `:10/:40` rodando (última publicação 14:40Z = 11:40 BRT, readback OK; 1 readback 500 às 14:10Z auto-recuperado na rodada seguinte).
- **Audiência medida server-side desde 26/08** (contador próprio, cron */5 no canônico): **26/08 = 13 visitas de bots + 5 "humanas"** (pico da descoberta: Googlebot, Bingbot, YandexBot, Amzn-SearchBot acharam em <36h); 27/08 = 2 bots; **de 28/08 em diante = 0 bots/dia** (crawl budget normal de página nova — crawlers espaçam revisitas) e 2-6 "humanos por UA"/dia (falsos navegadores de datacenter, humano real: zero até hoje).
- **Custo: US$ 0 de LLM** — o worker é 100% determinístico (câmbio público + montagem; as menções a "llm" no código são o cartão de preços públicos que o jornal publica). Quem faz: worker Python NYC (cron :10/:40) + mu-plugin PHP no canônico (publica/arquiva/renderiza Site Digest ao vivo) + contador bash/python (canônico, */5).

**B. O QUE FOI FEITO NESTA SESSÃO (tudo no ar):**
1. **Página `/v6/bot-news` (🤖 Bot News) no painel CCTV v6** — Tencent `painel_cctv_v6.py` (backup `.bak_pre_botnews_20260903`; item no menu; serviço `cctv-v6` reiniciado). Mostra: edição corrente (nº, data, saudação EN+ZH, capítulo da história, updated_at, edições arquivadas, link), gráfico de barras bots×"humanos" por dia desde 26/08, tabela por dia com IPs distintos, recados/bloqueios, cartão "quem faz + custo US$ 0". Edição via REST público com cache 10 min; série via push do contador.
2. **Endpoint de ingestão `/v6/api/botnews-receber`** (mesmo molde do audiencia-receber: X-Token, dedupe por `gerado`, append em `V6_CACHE/botnews_red.jsonl`); token próprio em `V6_CACHE/botnews_token.txt`.
3. **Pusher no contador do canônico**: fim do `bot_news_contador.sh` monta `{"gerado", "resumo", "historico"}` (resumo fresco + até 400 snapshots eternos do `historico.jsonl`) e POSTa pro Tencent (fail-soft, rito do FAROL; token `/root/bot_news_contador/push_token`; timeout 20s; backup `.bak_pre_gz_push_20260903`). Rodada manual provada: `{"ok": true, "gravado": true}`.
4. **Janela do contador ampliada de 2 para ~6 dias**: agora lê `access.ocafezinho.contador.log` + `.1` + `.2.gz`…`.5.gz` (o python já abria .gz; o FILES só não incluía). Antes o `by_day` nascia zerado a cada rotação diária do nginx (bug de janela — por isso o resumo de 03/09 só mostrava 02-03/09).
5. **Série eterna desde 26/08 garantida no painel**: a página mescla os snapshots horários (evidência eterna, 174 registros) com o resumo corrente — por dia, o maior acumulado já visto em qualquer janela de log (limite inferior honesto; rotulado na página).

**C. PROVAS:** página 200 interna (`:8084/bot-news`) e externa (`/v6/bot-news` via nginx); gráfico com as 9 barras 26/08→03/09 (26/08: 13 bots · 5 humanos); endpoint: token certo `gravado true` × token furado `403`; série do REST: nº 9 + updated_at 14:40Z; AST-OK python 3.12 do Tencent; screenshot 1440×1900 em `~/ZCodeProject/provas_botnews/` (canal de imagem da sessão não renderizou — homologação visual do Miguel pendente).

**D. ARMADILHAS (para a próxima sessão):** porta interna 8084 atende SEM prefixo `/v6` (o nginx põe); `urllib`: `timeout` é do `urlopen`, não do `Request`; o WAF do site dá **403 pro User-Agent "Python-urllib"** (mesma família da lição "REST exige UA navegador" — UA custom resolveu); `V6_CACHE` real = `<repo>/Projeto Cafezinho Agentes/root/agent_data/cctv/v6` (não `~/agent_data`); `grep -c` engana em HTML de linha única (usar `grep -o | wc -l`).

**E. ESTADO DA MISSÃO:**
- **O que aconteceu:** o boletim dos robôs está saudável, gratuito e pontual (9 edições); agora tem página própria no CCTV com audiência desde o dia 1, custo e "quem faz"; contador com janela de 6 dias + série eterna empurrada a cada 5 min.
- **O que falta:** (a) homologação visual do Miguel em `/v6/bot-news`; (b) pendências antigas do Adendo 15.5 (revisão humana dos 5 capítulos Our Story; investigar os 400 do challenge); (c) com bots em 0/dia desde 28/08, decidir se o convênio precisa de "algo novo" (ex.: sitemap/llms.txt atualizado, conteúdo mais fresco) para reatraír crawlers — decisão editorial do Miguel.
- **O que preciso de você (Miguel):** abrir `http://43.156.151.165/v6/bot-news` (ou pelo menu 🤖 Bot News) e dizer se a página serve; opcional: palavras pra enriquecer os capítulos Our Story.

— ZCode/GLM-5.3 (Dell) · 03/09/2026 ~12:10 BRT
