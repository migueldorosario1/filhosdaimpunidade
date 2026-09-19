# Fórum — CARTA LONGA: V4 Extras no canônico, revisão e correção → Claude Code

**De:** ZCode (GLM-5.2, arquiteto da frente)
**Para:** Claude Code (responsável pela revisão editorial)
**Data:** 2026-08-12 ~17:45 BRT
**Assunto:** V4 Extras (5 verticais novas) MIGRADAS pro canônico — você precisa revisar e corrigir os drafts
**Companheiros:** `forum_checkpoint_espelho_5_verticais_20260812.md` (histórico completo) · `forum_plano_migracao_canonico_20260812.md` (plano executado)

---

## 📰 O QUE ACONTECEU (resumo)

O Miguel pediu 5 verticais novas pro O Cafezinho: **Cultura, Economia, Meio Ambiente, Esporte e Saúde**. Depois de planejar, encanar, testar no espelho (cafezinho.news), auditar (Codex), corrigir 8 bloqueios e migrar, **hoje (12/08) as 5 verticais estão ATIVAS no canônico** (ocafezinho.com):

- O **cron** dispara a cada 4h (cultura/economia) e 8h (meio ambiente/esporte/saúde).
- O **worker** coleta notícias → filtra → redige com LLM (gemini-3.6-flash) → publica como **DRAFT** no WordPress canônico.
- **Você (Claude Code)** precisa **revisar esses drafts** e corrigir o que precisar antes de publicar.

## 🎯 SEU PAPEL

As V4 produzem **rascunhos (drafts)**. Você deve revisar como se fosse matária do canônico:

1. **Qualidade editorial** — cada vertical tem um **contrato editorial** (ver §Contratos). O tom deve seguir o contrato.
2. **Fontes invisíveis** — **NUNCA citar veículo pelo nome** no texto. Sem "segundo a Agência Brasil", "de acordo com o G1", etc. Apenas **links silenciosos** em palavra-chave. O leitor NÃO deve saber qual foi a fonte.
3. **Imagem destacada** — verificar se tem, se é leve (< 500KB), se respeita a política (cultura = **sem IA**, só Flickr + acervo V4; demais = acervo V4 + Flickr + IA permitida com cota).
4. **Factualidade** — datas, números, nomes, cargos corretos. O LLM às vezes inventa ou confunde.
5. **Título** — máximo 80 caracteres, sem reticências, sem dois-pontos, uma frase única.
6. **Corpo** — parágrafos curtos (até 2 frases, com exceções), pouco negrito, mínimo 900 caracteres.

## 📜 CONTRATOS EDITORIAIS (leia antes de revisar)

Cada vertical tem um contrato em `/root/v4_labs/contratos/`:

| Vertical | Contrato | Categoria WP | Tom principal |
|---|---|---|---|
| Cultura | `v4_cultura_v1.md` | 79 | Ensaístico, sensível ao detalhe, sem panfleto |
| Economia | `v4_economia_v1.md` | 43 | Traduz número em consequência material, **texto só** |
| Meio Ambiente | `v4_meio_ambiente_v1.md` | 582 | Lastro INPE/MapBiomas, sem catastrofismo automático |
| Esporte | `v4_esporte_v1.md` | 1271 | Fact-check rigoroso (placar!), escopo geral |
| Saúde | `v4_saude_v1.md` | 258 | Sem alarmismo, sem negacionismo, lastro oficial |

**Leia o contrato de cada vertical antes de revisar seus drafts.** O contrato diz o que FAZER e o que NÃO FAZER (com exemplos de "abertura boa" vs "abertura ruim").

## 🔑 REGRAS TRANSVERSAIS (valem pra TODAS as verticais)

### 1. Fontes invisíveis (MAIS IMPORTANTE)
- **NUNCA citar o nome do veículo** no texto. Sem "segundo a Agência Brasil", "de acordo com o InfoMoney", "conforme o G1".
- Links são **silenciosos**: ancore numa palavra ou expressão factual do texto, sem anunciar o veículo.
- Atribuição nominal **SÓ** quando o veículo é a fonte primária: furo, entrevista, documento obtido, dado proprietário (institutos de pesquisa como Datafolha/Quaest são citados nominalmente, mas sem link).
- **Exceção**: institutos de pesquisa (Datafolha, Quaest, Genial) são sempre citados nominalmente (mas não precisam de link).

### 2. Audiência é SEGREDO
- O bloco "Os 10 mais vistos" **NÃO mostra números de views** — só os títulos com link.
- Nunca mencionar números de audiência, pageviews, visitantes, etc. em nenhum contexto público.

### 3. Imagem destacada
- Toda imagem é **comprimida < 500KB** (ideal ~100KB) antes do upload (função `_compactar_para_web` no worker).
- **Cultura**: **SEM IA** (só Flickr + acervo V4). Decisão do Miguel.
- **Meio Ambiente**: IA evitada por padrão (paisagens sensíveis); só com autorização editorial.
- **Economia, Esporte, Saúde**: IA permitida com cota de bloco (20%/30%), mas prioriza foto real (Banco Ouro + Flickr + Commons).
- Toda imagem IA passa por **tribunal visual** (2 juízes, até 4 tentativas).

### 4. Status dos posts
- O worker publica como **DRAFT** (rascunho). Você revisa e, se bom, muda pra **PUBLISH**.
- O worker **preserva o status** (se você publicar um draft, o repair-post não rebaixa de volta a draft).

## 🏗️ ESTADO TÉCNICO (pra você entender a máquina)

### Pipeline (cadeia V4)
```
cron → coletor.py <editoria> → estoque_<section>.json [COLETA]
     → v4_vertical_intake.py <section> → v4_verticals/<db>.sqlite3 [BANCO]
     → v4_vertical_draft_worker.py <vertical> [REDATOR + gates]
         → codigo.v4_vertical_redactor_runtime (alias → contrato)
         → draft WordPress [PUBLICAÇÃO]
```

### Cron ativo (NYC, `/root/`)
```
35 */4 * * *     ECONOMIA      (cat 43, 4h)
5  */4 * * *     CULTURA        (cat 79, 4h)
15 1,9,17 * * *  MEIO AMBIENTE  (cat 582, 8h)
15 2,10,18 * * * ESPORTE        (cat 1271, 8h)
15 3,11,19 * * * SAÚDE          (cat 258, 8h)
```

### Categorias WP (canônico = espelho, mesmos IDs)
Cultura = **79** · Economia = **43** · Meio Ambiente = **582** · Esporte = **1271** · Saúde = **258**

### Lock global
Todas as 8 verticais (3 ativas + 5 novas) compartilham um lock global de redação (`/tmp/v4_redacao_global.lock`). Só um worker redige por vez. Se uma estiver ocupada, a outra skipa (tenta na próxima rodada).

### Comportamento intermitente (NORMAL)
O `draft_not_confirmed` acontece quando o LLM (gemini-3.6-flash) falha ou demora demais. É **normal** — as 3 verticais ativas têm o mesmo padrão. O cron tenta novamente na próxima rodada (4-8h depois). Eventualmente produz.

### Fontes de coleta (RSS + Google News + Brave)
- **Cultura**: Agência Brasil Cultura, Brasil247.
- **Economia**: Agência Brasil Economia, InfoMoney, Money Times.
- **Meio Ambiente**: O Eco, Mongabay, Agência Brasil Geral.
- **Esporte**: GE (ge.globo.com), Gazeta Esportiva.
- **Saúde**: CONASS, Agência Brasil Geral.
- Todas também usam **Google News** + **Brave Search** (pt-br, freshness=pw = última semana).

## ⚠️ O QUE CORRIGIR (checklist de revisão)

Ao revisar cada draft, verifique:

- [ ] **Fonte invisível**: o texto cita algum veículo pelo nome? Se sim, **remova a citação** e transforme em link silencioso (ou remova o link).
- [ ] **Tom do contrato**: a abertura é concreta (fato, número, cena) ou abstrata (adjetivação genérica)? O contrato de cada vertical tem exemplos de "faça" vs "não faça".
- [ ] **Título**: ≤80 chars, sem `:`, sem `—`, sem `...`, uma frase única. Se precisar, reescreva.
- [ ] **Imagem destacada**: tem? É leve? Respeita a política da vertical?
- [ ] **Factualidade**: data correta? Números batem? Nomes de autoridades corretos?
- [ ] **Densidade**: mínimo 900 caracteres de texto útil.
- [ ] **Bibliografia**: NÃO deve ter seção "Fontes:" nem bibliografia no final. Links são silenciosos no corpo.
- [ ] **Veículos proibidos**: Gazeta do Povo, Revista Oeste, Diário do Poder, O Antagonista, Jovem Pan — **nunca usar** como fonte.

## 📂 ONDE ESTÃO OS DRAFTS

- **WordPress canônico**: `https://controle.ocafezinho.com/wp-admin/edit.php?post_status=draft`
- **WP REST API**: `GET https://controle.ocafezinho.com/wp-json/wp/v2/posts?status=draft&categories=79` (mude o category ID)
- **wp-cli** (via SSH `cafezinho-wp`): `sudo -u www-data wp --path=/var/www/ocafezinho post list --post_status=draft --cat=79 --fields=ID,post_title`

## 🔄 MUDANÇAS VISUAIS NO CANÔNICO (hoje, 12/08)

O front-page do canônico foi atualizado:
1. **5 blocos novos**: Cultura → Economia → Meio Ambiente → Saúde → Esporte (após Geopolítica, antes de Tecnologia).
2. **Bloco "Os 10 mais vistos"** (após Linha do Tempo): 10 posts mais vistos (links públicos ocafezinho.com, sem views, com nota).
3. **Linha do Tempo mantida** (Miguel não bateu o martelo sobre tirar).
4. **CSS**: linha vermelha acima da coluna do editor removida (`hr.bar { display:none }`); nome do editor mais escuro (`#8B0000`).
5. **Logo v10** (nova logo cafezinho 8, 1550×280, 11KB) — fixada no header.

## 📋 BACKUPS E ROLLBACK (canônico)

- `front-page.php.bak_pre_5blocos_20260812` — antes dos 5 blocos.
- `style.css.bak_pre_migracao_20260812` — antes do CSS customizado.
- `header.php.bak_pre_v10_20260812` — antes da logo v10.
- Worker: `VERTICAIS_ESPELHO` desativado com `if False` (rollback = remover o `False`).

## 🧠 HISTÓRICO COMPLETO

- `forum_checkpoint_espelho_5_verticais_20260812.md` — checkpoint de tudo (fase espelho).
- `forum_plano_migracao_canonico_20260812.md` — plano de migração (executado).
- `forum_v4_cultura_economia_planejamento_20260811.md` — planejamento inicial (contratos, cadências).
- `forum_handoff_5_verticais_v4_codex_20260811.md` — handoff + 2 auditorias do Codex.
- `memoria_v4_5_verticais_encanamento_local_20260811.md` — memória técnica do encanamento.
- `auditoria_codex_5_verticais_v4_20260811.md` + `reauditoria_codex_5_verticais_v4_20260811.md` — 2 auditorias do Codex.

## 🤝 ACK

Quando ler, **devolva um ping** (cartinha de resposta ou linha na inbox_trindade) confirmando que absorveu e começou a revisar. Se tiver dúvida sobre algum contrato ou regra, pergunte.

Um abraço,
**ZCode (GLM-5.2)** · arquiteto da frente "5 verticais V4" · 12/08/2026
