# PRONTO — Baleia Azul: título de categoria como LINK CLICÁVEL (ordem do Miguel, 19/09/2026)

**Pedido do Miguel (voz, 19/09 ~11:3x):** "quero que você transforme o título dos blocos, tipo Nacional, Geopolítica, no link — a pessoa clica no link e abre a página das categorias. Tô sentindo falta disso."

## 1. Diagnóstico (o que já existe, e o que falta)

- **O painel V6 já sabe fazer link.** `_md_inline()` no `painel_cctv_v6.py` (~linha 198) converte `[Nome](https://...)` em `<a href="..." target="_blank" rel="noopener">Nome</a>`. Ou seja: **se a edição trouxer o link em markdown, a página do Baleia no painel mostra clicável sem mudar uma linha do painel**.
- **O e-mail é HTML** (`enviar_baleia_azul_ponte.sh`, Dell): converte igual, desde que o emissor aplique a mesma conversão antes de montar o HTML.
- **A perna do Telegram hoje manda texto PURO** — o envio no `baleia_dsn_ciclo.sh` faz `json.dumps({"chat_id": chat, "text": p})`, sem `parse_mode`. Link em markdown apareceria cru como `[Nacional](https://...)`.

## 2. Especificação

1. **Onde entra o link:** na lista dos dez mais lidos, o nome da categoria depois do título; e em qualquer menção de categoria no corpo do texto (as famílias: geopolítica, economia, eleições, política e nacional).
2. **Formato no arquivo da edição** (markdown, na própria linha do item):
   `1. Documentos liberados pelo STF ligam Dark Horse ao PCC — [Nacional](https://www.ocafezinho.com/nacional/) e [Política](https://www.ocafezinho.com/politica-2/) — 753 leituras`
3. **Como resolver o link (fonte única, nunca chutar URL):**
   `https://www.ocafezinho.com/wp-json/wp/v2/categories?include=<ids>&_fields=id,name,link`
   → usar o campo `link` que o próprio WP devolve (o mesmo endpoint que já traz os nomes no passo de categorias da missão).
4. **Mapa atual, conferido agora por REST** (19/09): Economia 43 → /economia/ · Eleições 2026 5088 → /eleicoes-2026/ · Geopolítica 5003 → /geopolitica/ · Nacional 21141 → /nacional/ · Política 22 → **/politica-2/** (slug torto, é o oficial) · Top 10 — agora 21169 → /top-10/ · No home 20699 → /no-home/.
5. **Telegram (perna do DSN, ciclo do Baleia):** enviar com `parse_mode: "HTML"` e converter, nesta ordem: escapar `&`, `<`, `>` do texto; depois trocar `[texto](url)` por `<a href="url">texto</a>`. O corte em partes de ~3.900 caracteres continua valendo, com o cuidado de não cortar no meio de um link.
6. **Rede de segurança:** categoria sem mapa ou link → sai **texto puro**, nunca link quebrado; o manual v1.1 continua proibindo asterisco (que brigaria com o parse do Telegram).
7. **Legibilidade:** o link não pode engolir a linha — o texto tem de continuar legível em cópia simples (quem copiar o boletim vê o nome da categoria, não um emaranhado de URL).

## 3. Testes de aceitação (provar com print)

1. Painel, edição do dia: clicar em "Geopolítica" abre `ocafezinho.com/geopolitica/` em nova aba.
2. Telegram: tocar no nome da categoria abre a página da categoria.
3. E-mail: mesma coisa, no cliente de e-mail.
4. Edição com categoria fora do mapa: sem link torto, texto puro.
5. Copiar e colar o boletim inteiro: continua legível.

## 4. Divisão de trabalho sugerida

- **ZM/ZCode (app e e-mail):** aplicar a conversão no emissor do e-mail e conferir a renderização da página do Baleia com os links (o painel já converte; é validação).
- **DSN celular (eu):** a missão passa a pedir o link resolvido por REST e o envio do Telegram passa a usar `parse_mode: HTML` — os dois são arquivos meus, aplico assim que o Miguel mandar.

— pronto escrito por DSH-us65 (DSC) · 19/09/2026 · para o ZM executar / Miguel colar no ZCode
