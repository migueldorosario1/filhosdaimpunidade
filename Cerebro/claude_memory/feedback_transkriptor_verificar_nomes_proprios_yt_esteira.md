---
name: feedback-transkriptor-verificar-nomes-proprios-yt-esteira
description: "Posts do agente YouTube-esteira (cat 2403, embed YT + transcrição via Transkriptor) SEMPRE têm nomes próprios estrangeiros errados na transcrição automática. Antes de publish, WebSearch obrigatório em TODOS os nomes de convidados/jornalistas/entrevistados citados — o Transkriptor troca sílabas (Milei→Millet, Restivo→Rechivo) e distorce sobrenomes. Aplicar sistematicamente."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 73eca14d-c13b-47ac-a05e-3285ca9a2dc6
---

**REGRA:** Em toda matéria da esteira YouTube (worker Cafezinho/TV Fórum, categoria 2403, com embed `<iframe youtube>` + "transcrição via Transkriptor" no figcaption), **antes do publish**: extrair TODOS os nomes próprios de pessoas (convidados, jornalistas entrevistados, entrevistadores, autoridades citadas nas aspas) e **WebSearch obrigatório em cada um** para conferir grafia. Corrigir in-place antes de mandar para DS/GPT/publish.

**Why:** Miguel 09/08/2026 flagou dois erros consecutivos em posts YT-esteira, ambos causados por transcrição automática ruim do Transkriptor:

1. **264931 (09/08 09:00):** o corpo dizia "Fabián Rechivo, do Página/12" — nome correto é **Fabián Restivo** (WebSearch confirmou: colunista ativo do Página/12 com página de autor 2025-2026, ex-fotógrafo, viveu na Bolívia). Miguel apontou depois do publish; retifiquei in-place 7 ocorrências, backup em `264931_retif_bf1d82ed39f9ae22.json`.

2. **264931 (09/08 08:57):** o corpo tinha uma aspa do jornalista: "O presidente **Millet** não é excêntrico, ele é idiota" — nome correto é **Milei** (o próprio presidente citado no título e no corpo várias vezes escrito corretamente). Peguei antes do publish e corrigi.

Padrão: **Transkriptor troca sílabas em nomes hispano-falantes** (Milei→Millet, Restivo→Rechivo) mesmo quando o áudio é claro. É falha sistêmica da transcrição automática — se aconteceu 2 vezes em 1 post, vai acontecer em outros.

**How to apply:**

1. **Detecção do tipo de post:** se categoria inclui `2403` OU HTML contém `<iframe.*youtube>` OU figcaption contém `Transkriptor|transkriptor`, é YT-esteira. Ativar checagem reforçada.

2. **Extração de nomes:** ler o corpo, listar TODOS os nomes próprios de pessoas mencionadas — não só o convidado principal, mas qualquer pessoa citada em aspa ou referência (o Transkriptor erra até nomes muito conhecidos como Milei).

3. **WebSearch por nome:** para cada nome, `"[nome]" + [contexto — jornalista, veículo, cargo]`. Exemplo: `"Fabian Restivo" jornalista Página/12`. Se não achar com essa grafia, tentar variantes fonéticas (Restivo/Rechivo/Rechevo; Milei/Millet/Milet).

4. **Corrigir in-place** com `str.replace()` em TODAS as ocorrências (título, corpo, aspas). Rechivo apareceu 7 vezes em 1 post — não basta corrigir a primeira.

5. **Não confiar no `title` do iframe embed** — o YouTube pega o título original que o Cafezinho postou lá, pode carregar a grafia errada e não posso mudar (é oEmbed). Corrigir só o texto HTML do post + o `<title>` (WordPress).

6. **Regra irmã:** [[feedback-ceticismo-nao-apagar-investigar-lingua-original]] — quando fonte é estrangeira (Página/12 é argentino), a checagem tem que incluir busca no país de origem. Fabián Restivo só apareceu direito com busca em espanhol/site argentino.

7. **Se o nome citado numa aspa não bater com nenhuma pessoa real após 2-3 buscas:** trocar por descrição genérica (`"o jornalista argentino"` sem nome) ao invés de manter uma alucinação — aspa com nome errado é pior que aspa sem nome.

8. **Nunca confiar em "transcrição literal do Transkriptor" como se fosse verdade:** aspas com nomes vieram de máquina, não do jornalista. Se a máquina disse "Millet", o jornalista disse "Milei". Correção da transcrição é fidelidade ao original, não adulteração.

**Não ceder:** o Transkriptor tem viés fonético do português BR — nomes hispano-falantes, franceses, alemães, chineses vão vir errados por default. Aplicar a checagem MESMO se o nome parecer "encaixado" — Fabián Rechivo parecia plausível e passou por mim; era mentira.
