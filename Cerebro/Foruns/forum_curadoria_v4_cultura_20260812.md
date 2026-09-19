# Fórum — Curadoria V4 Cultura: pautas, festivais, websearch e ficha técnica jornalística

**Data:** 2026-08-12 ~18:15 BRT
**Sessão:** ZCode GLM-5.2
**Assunto:** Expandir e refinar a curadoria editorial da vertical Cultura — o que cobrir, como cobrir, e garantir websearch robusto

---

## O que o Miguel quer (diretrizes de curadoria)

### Áreas de cobertura (ampliar)
1. **Festivais de cinema** — Brasília, Rio, São Paulo, Gramado, Cannes, Berlim, Veneza, Sundance, Tribeca. Cobrir seleção oficial, vencedores, filmes brasileiros em competição, polêmicas do júri.
2. **Literatura** — lançamentos de livros (especialmente sobre política e não-ficção brasileira), romances, coletâneas. Perfil de autores. Bienal do Livro.
3. **Séries e TV** — novas séries nacionais e internacionais, streaming (Globoplay, Netflix, Prime, Max, Disney+), produções brasileiras originais.
4. **Teatro** — montagens em cartaz, festivais de teatro, prêmios (Shell, APTR).
5. **Artes plásticas** — exposições, bienais (São Paulo, Mercosul), leilões, leilões de arte brasileira.
6. **Música** — festivais (Rock in Rio, Lollapalooza, Festival de Inverno), prêmios (Grammy Latino, Multishow), novos álbuns.
7. **Cinema nacional** — estreias da semana, bilheteria, ANCINE, Lei do Audiovisual.

### Como cobrir (método jornalístico)
- **NÃO acadêmico** — linguagem acessível, sem jargão de crítica cultural.
- **Ficha técnica pode aparecer** — mas abordada **jornalisticamente**, não como lista seca. Exemplo: *"O filme, dirigido por Wagner Moura e coproduzido pela O2 Filmes com orçamento de R$ 12 milhões, chegou aos cinemas após passar por Cannes..."*
- **Websearch é fundamental** — o redator DEVE pesquisar as obras (sinopse, elenco, direção, ficha técnica, recepção, bilheteria, prêmios) antes de escrever. Não inventar dados.
- **Voz própria** — reescrever com voz do Cafezinho, nunca copiar frases da fonte.

### Pautas fortes de Cultura (prioridade)
- **Festival em andamento** → cobertura de seleção/vencedores (ex: "Festival de Brasília anuncia seleção oficial com 16 filmes em competição")
- **Estreia da semana** → filme/série/livro que chega ao mercado com contexto (ex: "Série brasileira sobre o Cerrado estreia na Netflix após prêmio em Berlim")
- **Prêmio/indicação** → quem ganhou, o que significa (ex: "Brasileiro leva Urso de Ouro em Berlim por documentário sobre Amazônia")
- **Lançamento de livro** → sobre tudo, política, memória, reportagem (ex: "Novo livro de Mário Magalhães sobre os anos de chumbo chega às livrarias")
- **Polêmica cultural** → censura, corte de verba, disputa simbólica (ex: "ANCINE nega certificado a filme sobre golpe de 1964")
- **Indústria cultural** → mercado, bilheteria, streaming, políticas públicas (ex: "Cinema brasileiro fecha 2025 com melhor bilheteria em 10 anos")

### O que NÃO é pauta de Cultura (vai pro Repetidor)
- Agenda cultural fria (programação sem ângulo)
- Release de plataforma sem ângulo
- Lista de indicações sem conflito
- Resenha subjetiva sem fato concreto
- Fofoca sem lastro

## Websearch no V4 Cultura (importante)

O redator do V4 (runtime) já faz **pesquisa web nativa** (o prompt diz: *"Faça pesquisa web nativa para confirmar datas, cargos, acontecimentos e afirmações atuais"*). Mas para Cultura, é **especialmente crítico** porque:

- Obras têm **ficha técnica** (diretor, elenco, roteiro, produção, orçamento, distribuidora) que precisa ser verificada.
- **Festivais** têm calendário (Cannes em maio, Veneza em setembro, Brasília em outubro) que muda.
- **Prêmios** têm vencedores específicos que o LLM pode confundir (inventar vencedor errado).
- **Bilheteria** e números de mercado mudam semanalmente.

### Recomendação
O contrato `v4_cultura_v1.md` deve ter uma instrução adicional reforçando:
> *"Antes de escrever sobre qualquer obra (filme, série, livro, peça), FAA PESQUISA WEB para confirmar: título correto, diretor/autor, elenco, data de estreia, distribuidora, bilheteria (se houver), prêmios recebidos. Nunca invente ficha técnica."*

## Próximos passos
1. **Atualizar o contrato** `v4_cultura_v1.md` com estas diretrizes (festivais, websearch reforçado, ficha técnica jornalística, não-acadêmico).
2. **Adicionar fontes RSS** culturais específicas ao coletor (festival de cinema, literatura, séries).
3. **Discutir com o Miguel** quais festivais/áreas são prioridade absoluta.

## Estado atual do V4 Cultura
- Cron ativo: a cada 4h (`5 */4 * * *`).
- Fontes RSS: Agência Brasil Cultura + Brasil247 Cultura + Google News + Brave (pt-br, freshness=pw).
- Estoque: 11 candidatas.
- Contrato: `v4_cultura_v1.md` (escopo, tom, faça/não faça, imagem sem IA).
- Já produziu: draft "Margareth Menezes apresenta verba recorde do Fundo Setorial a cineastas" (2177 chars, gemini).

## Continuidade
Este fórum é vivo — o Miguel e os agentes podem adicionar ideias de pauta, ajustar prioridades, sugerir fontes. O objetivo é fazer do V4 Cultura uma editoria vibrante que cobre o melhor da produção cultural brasileira e internacional com voz própria.
