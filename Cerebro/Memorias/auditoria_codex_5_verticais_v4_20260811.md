# Auditoria Codex — cinco verticais V4

Data: 11/08/2026, BRT  
Escopo: Cultura, Economia, Meio Ambiente, Esporte e Saúde  
Modo: auditoria somente leitura; nenhum cron ligado e nenhum arquivo operacional alterado

## Veredito

🔴 Bloqueante para ligar o cron.

O deploy físico está íntegro e a sintaxe está válida, mas o encanamento editorial não está completo. Quatro das cinco verticais carregam silenciosamente o contrato do Repetidor, e há falhas adicionais de data, concorrência, imagens e fontes.

## Evidências aprovadas

- Os nove arquivos ativos auditados são idênticos no espelho local e no NYC por SHA-256: quatro arquivos Python e cinco contratos.
- O backup `/root/.bak_pre_v4_novas_20260811/` existe. A comparação confirmou que o deploy preservou as alterações canônicas anteriores do NYC.
- `py_compile` passou nos quatro arquivos.
- O cron das cinco novas verticais não está ligado.
- Os cinco bancos SQLite existem e são pequenos.
- Os IDs de categoria mãe `[79]`, `[43]`, `[582]`, `[1271]` e `[258]` são coerentes. Classificação fina pode ser adicionada futuramente por classificador temático.
- Dispensar uma ramificação específica em `write_briefing()` é aceitável, desde que o registro editorial e o roteamento reconheçam cada vertical.

## Bloqueios

### 1. Quatro contratos não entram na composição

O runtime converte Economia, Meio Ambiente, Esporte e Saúde em `v4_economia`, `v4_meio_ambiente`, `v4_esporte` e `v4_saude`. Esses nomes não existem em `contratos/mapa_v4_contexto_llm.json`.

O `V4Registry` aplica então o fallback `v4_repetidor` sem erro. Teste direto no NYC:

- Cultura → `v4_cultura_v1.md` e `v4_super_luxo_redacao`.
- Economia, Meio Ambiente, Esporte e Saúde → `v4_repetidor_v1.md` e `v4_repetidor_limpo`.

Assim, o dry-run de Economia não validou o contrato de Economia. Validou o contrato genérico do Repetidor.

Correção necessária: registrar explicitamente as quatro editorias e seus aliases no mapa canônico, com testes que falhem se uma vertical nobre cair no fallback. O fallback silencioso não deve aceitar nomes `v4_*` desconhecidos.

### 2. A correção de data da Brave inventa atualidade

O código usa `page_age` ou `last_updated` e, quando ambos faltam, grava o horário da coleta como data de publicação. Na resposta real da Brave auditada, `page_age` existe, `last_updated` não apareceu e vários resultados não tinham data.

O fallback `now()` fez páginas permanentes e páginas de índice parecerem notícias novas. No banco de Economia, páginas como o painel de opções do Copom da B3 e a capa de Economia do InfoMoney receberam `published_at` praticamente igual a `collected_at` e passaram pelo filtro temporal.

Correção necessária: conservar `page_age` quando válido; sem data verdadeira, manter o campo ausente e rejeitar no intake, ou extrair uma data verificável da página. Nunca substituir data editorial por data de coleta.

### 3. O cron proposto colide com o cron atual

Geopolítica já começa nos minutos `0,30` de toda hora. A proposta inicia Cultura no minuto `0` e Economia no minuto `30`, exatamente nos mesmos instantes.

Os locks atuais são separados por vertical e não impedem concorrência entre redatores. É preciso escalonar horários e restaurar uma exclusão global do estágio de redação, ou introduzir um lock global interno compartilhado pelas oito verticais.

### 4. A política de imagem não é cumprida

O Banco de Mídia Ouro V4 só é consultado para Política, Geopolítica, Ciência e Regional. Nenhuma das cinco novas verticais consulta esse banco, embora os contratos prometam acervo V4.

Além disso, a válvula final de reparo libera imagem de IA para qualquer vertical após três tentativas. Isso contraria a decisão explícita de Cultura sem IA.

Correção necessária: incluir as novas verticais na busca do Banco Ouro e criar uma permissão por vertical para IA. Cultura precisa de bloqueio editorial explícito na válvula final enquanto vigorar a política sem IA.

### 5. A orientação editorial recente não chegou ao V4

O núcleo de redação não registra a preferência por parágrafos de até duas frases, com exceções criativas, nem a orientação de evitar negritos salvo razão excepcional. Cultura ainda manda alternar parágrafo curto e longo.

Correção necessária: atualizar o núcleo canônico, sem teto de palavras e sem transformar a orientação sintática em regra rígida. A formulação deve ser preferencial, não um gate mecânico.

## Ajustes importantes antes da ativação

- Cinco dos seis RSS diretos testados falharam: Cultura.gov teve falha de DNS; InfoAmazonia, Ministério da Saúde e OPAS retornaram 404; O Eco redirecionou e não entregou itens ao parser. Apenas Mongabay entregou entradas, em inglês e de alcance global.
- `collect_brave` usa `search_lang="en"` para toda seção que não seja Política. As cinco novas verticais brasileiras precisam de configuração de idioma adequada por vertical.
- As novas seções não têm TTL explícito no estoque e caem no padrão de seis horas. Isso deve ser alinhado às cadências de quatro e oito horas.
- O dry-run do worker terminou com dois eventos `failed`, apesar de o subprocesso retornar zero, porque não houve ID de rascunho WordPress. É comportamento compreensível do fluxo atual, mas não constitui um teste verde de ponta a ponta.
- Corrigir os termos em inglês remanescentes no contrato de Saúde (`approval`) e pequenos erros de revisão antes da ativação.

## Condições para nova auditoria

1. Registrar os quatro contratos e impedir fallback silencioso de editoria nobre.
2. Remover o `now()` da data Brave e testar resultados sem data.
3. Reprojetar horários e exclusão global da redação.
4. Cumprir Banco Ouro e política de IA por vertical.
5. Propagar ao núcleo a orientação flexível de parágrafos e negrito.
6. Substituir ou corrigir RSS inválidos e ajustar idioma da Brave.
7. Rodar testes de composição das cinco editorias e um dry-run que registre claramente sucesso sem publicar.

Depois desses pontos, o cron pode ser reavaliado. Até lá, manter as cinco novas entradas desligadas.
