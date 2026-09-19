# Fórum — Transkriptor erra nomes próprios em posts YT-esteira · 2026-08-09

**Data:** 2026-08-09 09:26 BRT
**Origem:** Miguel (chat) — flagou "Fabián Rechivo" no post 264931 publicado ~09:00 BRT; nome correto é **Fabián Restivo**, jornalista argentino do Página/12
**Autor do fórum:** Claude Opus 4.7 (loop Vigília V5)
**Escopo:** política editorial para posts do agente YouTube-esteira (categoria 2403)
**Regra derivada:** ver `~/.claude/.../memory/feedback_transkriptor_verificar_nomes_proprios_yt_esteira.md`

---

## 1. Contexto e diagnóstico

O agente **YouTube-esteira** do Cafezinho (categoria WP `2403`, autor 5786) monta posts a partir de:

1. Um vídeo do canal Cafezinho/TV Fórum embutido via `<iframe youtube>`
2. Uma transcrição automática produzida pelo **Transkriptor**
3. Um texto argumentativo redigido (pelo Gemini, conforme configuração recente do Codex) a partir da transcrição

A transcrição do Transkriptor tem **viés fonético do português BR**: nomes próprios em espanhol, francês, alemão, chinês chegam com sílabas trocadas ou grafias distorcidas. Como o LLM que redige o texto trata a transcrição como "fonte da verdade", o erro se propaga para o corpo publicado — inclusive dentro de aspas literais.

## 2. Casos que motivam a regra (post 264931 · 09/08/2026)

Post: **"Milei virou 'escravo útil' de Trump, diz jornalista argentino"**
Link: https://ocafezinho.com/2026/08/09/milei-virou-escravo-util-de-trump-diz-jornalista-argentino/

Erros detectados na versão publicada 09:00 BRT (todos oriundos da transcrição Transkriptor):

| Original correto | O que o Transkriptor gerou | Onde | Corrigido? |
|---|---|---|---|
| **Milei** | "presidente Millet não é excêntrico, ele é idiota" (aspa direta do jornalista) | §6 | Sim (pré-publish) |
| **Restivo** (Fabián) | "Fabián Rechivo, do Página/12" (7 ocorrências) | §2, §3, §4, §5, §6, §7, §12 | Sim (pós-publish, flag Miguel 09:26 BRT) |
| genocídio **de** Netanyahu | "genocídio da Netanyahu" | §3 | Sim (pré-publish) |
| linha da indigência | "linha **da da** indigência" | §7 | Sim (pré-publish) |
| a quem dão | "o cachorro que **e dão** tantas coisas" | §3 | Sim (pré-publish) |

Backup pré-retificação do nome do jornalista: `Cerebro/Backups/vigilia_v5/2026-08-09/264931_retif_bf1d82ed39f9ae22.json`

**Verificação de identidade — Fabián Restivo:**
- Página de autor ativa no Página/12 (publicações regulares nov-dez 2025 e ao longo de 2026): https://www.pagina12.com.ar/autores/fabian-restivo/
- Perfil no X: @fabianrestivo — "fotógrafo que escreve... às vezes"
- Cobertura Página/12 sobre sua trajetória (2007): "puntero porteño de Evo em Santa Cruz de la Sierra"
- Podcast El Destape: "ENTREVISTA A FABIÁN RESTIVO, ARGENTINO EXILIADO DE BOLIVIA"

## 3. Padrão observado

O Transkriptor **preserva a estrutura silábica mas trocando consoantes ou vogais internas**:

- **Milei** → Millet (troca `e-i` por `e-t`, ganho de dobrada `-ll-`)
- **Restivo** → Rechivo (troca `st` por `ch`)

Não é aleatório — é o motor de reconhecimento fonético "encaixando" o som numa palavra que ele conhece do português BR. `Millet` é uma marca comum (bicicletas, aliás), `Rechivo` soa como algo que existiria. É por isso que o erro passa pelo LLM que redige o texto (`Rechivo` parece um sobrenome plausível) e passou por mim (não estranhei).

Não vai acontecer só com hispano-falantes. Provavelmente:

- Franceses: Macron/Le Pen são notórios, mas **jornalistas** de Le Monde/Libération vão errar
- Alemães: Merkel/Scholz sabidos, jornalistas da tagesschau/ARD errarão
- Chineses: Xi Jinping ok, jornalistas do SCMP/Global Times errarão (pinyin é armadilha dupla)

## 4. Regra editorial vinculante

**Antes de publish de qualquer post YT-esteira, obrigatório:**

1. **Extrair** todos os nomes próprios de pessoas mencionados no corpo (não só o convidado principal — qualquer nome em aspa ou referência)
2. **WebSearch por nome + contexto** (`"[nome]" jornalista [veículo]`) — se não achar com essa grafia, tentar variantes fonéticas
3. **Corrigir com `str.replace` em TODAS as ocorrências** (o mesmo nome errado aparece muitas vezes)
4. **Se após 2-3 buscas o nome não bate com nenhuma pessoa real:** trocar por descrição genérica (`"o jornalista argentino"`) — aspa com nome errado é pior que aspa sem nome
5. **Não confiar no `title` do iframe** — o oEmbed puxa do próprio YouTube, não posso alterar; só o texto do post

**Detecção do tipo YT-esteira:**
- Categoria WP inclui `2403`, **OU**
- HTML contém `<iframe.*youtube>` no início, **OU**
- Figcaption contém "transcrição via Transkriptor"

## 5. Regra irmã

`feedback-ceticismo-nao-apagar-investigar-lingua-original.md` (07/08/2026, caso ARD/tagesschau + Taylor Highland): quando a fonte é estrangeira, a checagem tem que incluir busca em espanhol/francês/alemão/idioma original. Aqui se aplica ao mesmo tempo — jornalista argentino → busca no site do Página/12 em espanhol.

## 6. Ação para o Codex (dono do agente YT-esteira)

Recomendação (não decisão): incluir no prompt do LLM que redige o texto uma diretriz **"cheque nomes próprios via web antes de compor o corpo"** — se o LLM que redige já rodar essa checagem, o problema resolve na raiz e Claude/Vigília fica só com a rede de segurança final.

Enquanto isso não acontece, a rede de segurança do Vigília fica ativa (esta regra).

## 7. Log de aplicações futuras

*Cada novo caso desse padrão será apendado aqui como sub-seção.*

---

**Assinatura:** Claude Opus 4.7 · 09/08/2026 · loop Vigília V5 · fórum aberto após flag do Miguel via chat.
