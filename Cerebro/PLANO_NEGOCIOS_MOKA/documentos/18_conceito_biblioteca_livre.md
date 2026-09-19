# 18 — CONCEITO: "A Biblioteca Livre do Moka" (campanha do programa + livraria embutida + fórum multilíngue)

> Criado por ZCode/Kimi com o Miguel, 28/07/2026. Documento de conceito para apresentação no programa e execução.

---

## 1. O CONCEITO EM UMA FRASE

**"O conhecimento é de todos. O Moka prova — de graça, no seu bolso, em 2 minutos."**

---

## 2. A CAMPANHA (para o programa do Miguel)

### O meme central
O Miguel, ao vivo, distribui **livros de graça** — os livros que formam a cabeça política do país e do mundo: **Maquiavel, Platão, Tocqueville, Marx, Machado de Assis, Nietzsche**. Pergunta pra plateia: *"Quanto custa O Príncipe?"* Resposta: **zero.** *"E pra entender em 2 minutos, na sua língua?"* — mostra o Moka resumindo na hora.

### Os slogans (escolher 1-2 oficiais)
1. **"A elite tem tempo. O povo tem o Moka."** ⭐ (minha favorita — política + verdade)
2. "Platão, Machado, Marx e Nietzsche — de graça, no seu celular, resumidos em 2 minutos."
3. "A biblioteca pública do século 21: no seu bolso, na sua língua, de graça."
4. "Código aberto, conhecimento livre, para todo mundo."

### A mecânica no programa
1. Mostra o app baixando "O Príncipe" GRÁTIS da Biblioteca Livre do Moka
2. Resume em 2 minutos AO VIVO (a IA trabalhando)
3. QR code na tela → a plateia baixa o Moka e ganha o livro + 50 pontos de amostra
4. Chamada democrática: "Isso é código aberto. Isso é conhecimento livre. Isso é pra todo mundo — é pra você."

---

## 3. A LIVRARIA LIVRE DO MOKA (livraria embutida no app)

### O que é
Seção "📚 Biblioteca Livre" DENTRO do Moka: catálogo de livros de **direitos expirados (domínio público)** que a pessoa baixa direto pro app e já lê/resume/ouve. **O Moka nasce com livros dentro — experiência completa no 1º uso.**

### Legalidade (a "limiar da pirataria" que NÃO é pirataria)
- Só **domínio público**: autores mortos há 70+ anos (regra brasileira). Maquiavel, Platão, Machado, Nietzsche, Marx, Eça, Tocqueville, Cervantes, Austen — **100% legal, sem limiar nenhum.**
- Fontes: Project Gutenberg (multi-idiomas), Domínio Público (gov.br), Wikisource.

### Acervo inicial (MVP, ~30 títulos, 5 idiomas)
| Área | Títulos |
|---|---|
| Política/Ciência Política | O Príncipe, Contrato Social, Democracia na América, Sobre a Liberdade, Manifesto |
| Filosofia | Platão (República), Aristóteles, Nietzsche (Além do Bem e do Mal), Meditações (Marco Aurélio) |
| Literatura PT | Dom Casmurro, Memórias Póstumas, O Cortiço, O Guarani, Iracema, Eça (O Primo Basílio) |
| EN | Pride and Prejudice, Moby Dick, Dickens |
| ES | Dom Quixote |
| FR | Voltaire (Cândido), Rousseau |

### Técnica
- Hospedagem: nosso **Backblaze B2** (bucket privado, URLs assinadas ou públicas do catálogo — "secreto" no sentido de não-depender de terceiros)
- No app: seção/catálogo JSON (título, autor, idioma, capa, link B2) → botão "Baixar" → entra na estante → lê/resume/ouve
- Curadoria inicial: ZCode baixa de Gutenberg, limpa, gera capas (o motor novo de capas), publica no B2, atualiza o catálogo

---

## 4. O FÓRUM MULTILÍNGUE (comunidade do site)

### O que o Miguel pediu
Um fórum no site onde pessoas dão opinião — internacional, multilíngue.

### Opções avaliadas
| Opção | O que é | Esforço | Veredito |
|---|---|---|---|
| **Discourse** (self-hosted) | O padrão-ouro de fóruns (o que roda fóruns gigantes), i18n nativo (UI em dezenas de idiomas), grátis/open-source | Docker na Tencent + DNS | ✅ **RECOMENDADO** |
| Flarum | Fórum PHP leve | médio | plano B |
| Giscus | comentários via GitHub Discussions por página | baixíssimo | não serve (exige conta GitHub do público) |
| Nativo no app | nosso próprio | alto | fase 3 |

### Plano Discourse
- Subdomínio **forum.mokareader.com** (DNS na GoDaddy → Tencent)
- Docker oficial do Discourse na Tencent (SMTP = info@mokareader.com, que já funciona)
- Categorias: 🇧🇷 Português · 🇺🇸 English · 🇪🇸 Español · por tema (Moka, Livros, Ideias)
- SSO futuro com a conta de pontos (fase 2)
- **Bônus:** o fórum É a "comunidade" prometida na /ajuda (substitui o grupo Telegram como casa oficial)

---

## 5. COMO TUDO SE CONECTA (o funil democrático)

```
PROGRAMA (Miguel distribui livros de graça ao vivo)
   ↓ QR code na tela
MOKA com 50 pts de amostra + livros grátis dentro
   ↓ a pessoa vicia
RESUME/OUVE/TRADUZ com a IA (gasta pontos)
   ↓
TESTE R$5 → PONTOS R$40+ → LICENÇA
   ↓
FÓRUM multilíngue (comunidade fica, opina, traz amigos)
```

**A lógica de ouro:** a livraria grátis não é custo — é a **prova viva do produto**. Cada download gratuito é um usuário que experimenta a IA sem fricção. O conhecimento livre é o anzol; os pontos são o peixe.

---

## 6. BACKLOG DE EXECUÇÃO (ordem)

1. **Curadoria + upload B2**: ~30 títulos domínio público (Gutenberg/Domínio Público), capas, catálogo JSON
2. **Seção "Biblioteca Livre" no app**: catálogo → baixar → estante (1 sprint pequena)
3. **QR code do programa** (link com UTM do programa + cupom coletivo "PROGRAMA" de 50 pts)
4. **Discourse na Tencent** (forum.mokareader.com): Docker + DNS + SMTP + i18n
5. **Roteiro do programa** (2 min): a entrega ao vivo com QR
6. Fase 2: SSO pontos×fórum, livros pedidos pela comunidade

---

# ADENDO (28/07 ~18h) — "Sugestões do Moka": videoteca legal + fluxo opt-in (decisões do Miguel)

## A regra de ouro do Miguel
**Nada é empurrado.** O app pergunta: *"Quer ver nossas sugestões de livros e vídeos?"* — o internauta escolhe o que inserir na SUA biblioteca, e pode **remover qualquer item ou limpar tudo** quando quiser. A biblioteca é da pessoa; as sugestões são um catálogo, nunca uma imposição.

## Fluxo (UX)
1. Botão ✨ na estante/videoteca (e no 1º acesso): "Quer ver sugestões do Moka?"
2. Modal com 2 abas: **📚 Livros** (~30, domínio público, baixa do B2) · **🎬 Vídeos** (~30, links YouTube curados — o Moka lê por link, transcrição na 1ª abertura)
3. Cada item: **[+ adicionar]** (ou "adicionar todas")
4. Rodapé fixo: "Sua biblioteca é sua: remova o que quiser, inclusive limpar tudo."

## VIDEOTECA LEGAL (~30 vídeos — links curados)

**Ciência — Física/Espaço:** Kurzgesagt (EN/PT-legendas), SpaceToday (Salvador Nogueira), Física Total, Veritasium (EN), Cosmos (Carl Sagan — clássico)
**Ciência — Biologia/Evolução:** Atila Iamarino (Nerdologia), Canal do Pirulla, BlaBlaLogia, Amoeba Sisters (EN)
**Filosofia:** Filosofia Vermelha, Tempero Drag, School of Life (EN), Clóvis de Barros Filho (aulas clássicas), LUI Pondé
**Política (educativa, linha do Cafezinho):** Meteoro Brasil, Tese Onze, Jones Manoel, Ian Neves, Central do Conhecimento

*Nota ZCode: os links exatos (URLs) serão resolvidos na construção via busca YouTube/Data API por canal+tema — catálogo curado por canal e assunto, não URL solta. Os ~30 títulos finais entram no catálogo JSON com título, canal, tema, duração e link.*

## Por que links e não download
O Moka Video trabalha por LINK (transcrição sob demanda) — a "videoteca legal" é uma lista de links curados: zero problema de direitos (o vídeo fica no canal do autor), e o usuário ganha a curadoria. Adicionar = o app registra o vídeo na videoteca da pessoa e transcreve quando ela abrir.

---

# ADENDO 2 (29/07) — Acervo estrangeiro EXPANDIDO (pedido do Miguel: "mais livros em língua estrangeira, para os internautas treinarem o aplicativo")

## A lógica
Livro estrangeiro = demo perfeita da TRADUÇÃO: internauta abre em inglês/francês/alemão → traduz pro português na hora → a mágica do Moka. Todos domínio público (autor morto há 70+ anos — regra BR).

## 🇺🇸🇬🇧 INGLÊS (10)
- Austen — *Pride and Prejudice*
- Dickens — *A Tale of Two Cities*
- Melville — *Moby Dick*
- Twain — *The Adventures of Tom Sawyer*
- Conan Doyle — *A Study in Scarlet* (Sherlock)
- Mary Shelley — *Frankenstein*
- Stoker — *Dracula*
- **Orwell — *1984*** (d. 1950 → PD no Brasil desde 2020 ✅)
- H.G. Wells — *The Time Machine*
- Sun Tzu — *The Art of War* (trad. Giles, 1910)

## 🇫🇷 FRANCÊS (6)
- Voltaire — *Candide*
- Rousseau — *Du contrat social*
- Victor Hugo — *Les Misérables*
- Dumas — *Le Comte de Monte-Cristo*
- Jules Verne — *Vingt mille lieues sous les mers*
- Flaubert — *Madame Bovary*

## 🇪🇸 ESPANHOL (3)
- Cervantes — *Don Quijote*
- Unamuno — *Niebla*
- Quevedo — *El Buscón*

## 🇩🇪 ALEMÃO (4)
- **Kafka — *Die Verwandlung* (A Metamorfose)** (d. 1924 → PD ✅)
- Goethe — *Faust* / *Werther*
- Nietzsche — *Also sprach Zarathustra*
- Schiller — selecionados

## 🇮🇹 ITALIANO (3)
- Machiavelli — *Il Principe* (original)
- Dante — *Divina Commedia*
- Collodi — *Pinocchio*

## Total do acervo livre agora
~56 títulos: 30 da lista-temática (biologia/física/história/espionagem/política/filosofia/literatura BR) + 26 estrangeiros acima. Cada item com capa + sinopse (escrita por ZCode) + idioma + tema + link B2. Sugestões de "treino de tradução" marcadas no catálogo com a tag `demo_traducao` (o app pode destacar: "quer treinar? abra este e traduza!").
