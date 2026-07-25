# 📕 CARTA AOS AGENTES (ChatGPT e Claude) — Como trabalhar neste repositório

**Repo:** `github.com/migueldorosario1/filhosdaimpunidade` (público, branch `main`)
**Projeto:** Livro de Miguel do Rosário em 2 volumes — **Filhos da Impunidade**:
- **Vol. 1 — O FORAGIDO** (Eduardo Bolsonaro) — em produção AGORA (prazo 05/08/2026)
- **Vol. 2 — O MALANDRO** (Flávio Bolsonaro) — depois do Vol. 1
Meta: 240.000 caracteres por volume (tudo incluído).

Este repositório é o **espelho de trabalho do livro**, sincronizado (no mínimo 1x/dia) a partir da máquina do Miguel pelo agente ZCode/Kimi. O backup pesado (PDFs grandes, vídeos, livros de referência) fica no Google Drive (`gdrive:novo livro`) — aqui fica o **texto**.

---

## Como acessar

- **Leitura:** o repo é público — `git clone https://github.com/migueldorosario1/filhosdaimpunidade.git` ou leitura direta pela web/API do GitHub.
- **Escrita:** só o Miguel concede acesso (colaboradores). Se tiver acesso de escrita: `git clone git@github.com:migueldorosario1/filhosdaimpunidade.git`.
- **Regra de ouro entre agentes:** nunca sobrescrever o arquivo de trabalho do outro sem avisar. Commits pequenos, com mensagem dizendo o que mudou e em qual capítulo.

## O que você já sabe (contexto do projeto)

Vocês dois já produziram peças centrais: as **ondas de investigação do Vol. 1** (3 ondas do GPT em `Kimi K3/` convertidas para md + originais em `Fontes/Pesquisa IA/gpt/`; 3 ondas do Claude em `Fontes/Pesquisa IA/claude/`) e o **ESQUEMA_V2 invertido** (estrutura por importância política, desenhada pelo Miguel e redigida pelo Claude — `Claude/ESQUEMA_V2_O_FORAGIDO_INVERTIDO.md`), que é a **arquitetura oficial dos 20 capítulos**.

## Mapa do repositório

| Caminho | O que é |
|---|---|
| `Claude/` | Esquema V2 oficial (estrutura invertida) |
| `Kimi K3/` | **Pasta de trabalho do ZCode/Kimi:** plano, esqueleto V1, fichas da Onda 2, capítulos escritos (cap. 1 em v4.4, cap. 2), NOTAS.md, acórdão AP 2782 (PDF+txt), transcrições, leads comerciais |
| `Kimi K3/MANUAL_DE_ESTILO.md` | ⚠️ **OBRIGATÓRIO** — regras de estilo do Miguel (#1–#18), com exemplos |
| `Kimi K3/REFERENCIA_LITERARIA.md` | ⚠️ **OBRIGATÓRIO** — a voz do livro (Machado + Thompson, com matemática de ritmo) |
| `Kimi K3/versoes/` | Histórico versionado de cada arquivo (v4.1, v4.2… com data/hora) |
| `Kimi K3/fontes_baixadas/` | Fontes da Onda 1 baixadas e convertidas para md |
| `Kimi K3/transcrições/` | Vídeos transcritos (CNN 18/07/2025 completa ⭐, War Room) |
| `Fontes/` | Acervo bruto: Pesquisa IA (ondas), Reportagens (dossiês), PDFs primários (processos EUA/Texas) |

## ⚠️ ANTES DE ESCREVER QUALQUER CAPÍTULO

1. Leia `Kimi K3/MANUAL_DE_ESTILO.md` (regras do Miguel: frases curtas, sem repetição, cadência, sem siglas, porém no meio da frase, nada em inglês, mistério > apresentação…).
2. Leia `Kimi K3/REFERENCIA_LITERARIA.md` (a voz: ~20 palavras/frase, cadência longa→longa→metade, adjetivo raro, ironia por justaposição e detalhe, nunca por epíteto).
3. Respeite o **protocolo de prova**: fato oficial / reportagem / alegação / defesa separados pelo verbo exato; "foragido" é título editorial, não status processual; condenação sempre "sujeita a recursos" até o trânsito.
4. Rode, se possível, o auditor `Kimi K3/verifica_estilo.py` no seu texto antes de commitar.

## Estado da produção (24/07/2026)

- **Escritos:** cap. 1 "Estarei vingado" (v4.4 — abertura martelada com o Miguel) e cap. 2 "Quatro a zero" (v1.0, passa pela mesma lapidação).
- **Em edição com o Miguel:** a voz do livro (manual + referência) — consolidada nesta semana.
- **Próximo:** cap. 3 "Washington é aqui" (Parte II — A Rede Americana).
- **Fontes primárias já em mãos:** acórdão da AP 2782 (196 p., com as 9 condutas extraídas), EO 14323, 3 ações OFAC, EO/tarifaço, transcrição integral da CNN 18/07/2025.

Dúvidas de arquitetura → `Claude/ESQUEMA_V2`. Dúvidas de estilo → o manual. Dúvidas de fato → `Kimi K3/ONDA2_FICHAS.md` e as ondas.

— ZCode/Kimi, a pedido do Miguel · 24/07/2026
