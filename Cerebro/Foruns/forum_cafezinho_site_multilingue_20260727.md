# 💬 Fórum — Cafezinho Multilíngue: versão em inglês do site (ideia de Miguel)

**Data:** 2026-07-27 · **Status:** EM ESTUDO — aguardando decisão de Miguel · **Memória pareada:** `MEMORIA/memoria_cafezinho_site_multilingue_20260727.md`

## A ideia (palavras de Miguel, 27/07)

Transformar o Cafezinho em site multilíngue: toda matéria produzida em português sai também em outras línguas, com **tradução de alto nível**, nas editorias de **geopolítica, ciência e política brasileira**. Publicar no Cafezinho, indexar no Google em inglês e "quem sabe abrir um mercado novo". Perguntas levantadas por Miguel:

1. O que é hreflang?
2. Vale a pena redirecionar automaticamente quem acessa do exterior para a versão em inglês?
3. O indexador (agente) precisa mudar para indexar texto em outra língua?
4. O que o Google diz oficialmente sobre isso? Outros sites fazem? Vale a pena?

## Pesquisa executada (ZCode/Kimi, 27/07)

Fontes verificadas ao vivo: documentação oficial do Google Search Central (hreflang, sites multi-regionais, locale-adaptive, spam policies, Indexing API) + 2 agentes de pesquisa web (casos reais e discussões SEO — buscadores bloquearam parte das queries ao vivo; achados não verificados estão marcados como tal na memória).

## Conclusões da pesquisa (resumo)

1. **Hreflang** = etiqueta no código da página que diz ao Google "esta página tem versões em outros idiomas, em tais URLs". Serve para o Google **exibir** a versão certa para cada usuário (brasileiro vê PT, americano vê EN). Não é obrigatória, mas é o mecanismo oficial.
2. **Redirect por IP: NÃO fazer.** O Google recomenda explicitamente *contra* redirecionamento automático por localização. O Googlebot rastreia dos EUA sem header de idioma — se o site redirecionar por IP, o bot só veria a versão em inglês e a versão PT (o negócio principal) poderia perder indexação. Solução oficial: **banner/sugestão de idioma** (usuário escolhe) + links de troca de idioma em todas as páginas.
3. **Indexador não muda.** A Indexing API é cega a idioma — o agente `indexador_google.py` apenas enviaria as novas URLs `/en/`. A propriedade `sc-domain:ocafezinho.com` do Search Console já cobre subdiretórios — **não precisa de "indexador novo" nem nova propriedade**. O Google detecta o idioma pelo conteúdo visível (não usa hreflang nem `lang` para detecção).
4. **Política de spam (mar/2024, "scaled content abuse"):** tradução automática é citada como abuso **quando aplicada a conteúdo raspado de terceiros** para multiplicar páginas sem valor. Traduzir o **próprio** conteúdo original, com qualidade, **não viola** — o critério é valor ao usuário, não o método. Nosso gate de qualidade (Kimi 3 / revisão de agente) é a proteção.
5. **Casos reais (leads, parcialmente não verificados ao vivo):** padrão documentado de expansões linguísticas de notícias é de **retração** quando exigem redação paga no exterior — El País Brasil abriu 2013/fechou 2017; HuffPost e BuzzFeed fecharam edições internacionais. Contrapontos: Le Monde in English (2022) e El País English (2023) com estratégia de assinatura internacional; The Local (Europa) multilíngue desde a origem. **Insight-chave:** os fracassos foram de custo de redação estrangeira — nosso custo marginal por tradução é de centavos (pipeline LLM já existente), o que muda a equação.
6. **Estrutura recomendada:** subdiretório `ocafezinho.com/en/` (aproveita a autoridade do domínio; Google lista ccTLD/subdomínio/subdiretório como opções válidas; parâmetros `?lang=` "not recommended").

## Recomendação preliminar (a deliberar por Miguel)

**Piloto reversível de 60–90 dias:** editorias geopolítica + ciência + política BR → `/en/`, hreflang bidirecional + `x-default`, **banner de idioma (não redirect)**, tradução LLM + gate de qualidade, medição no SEO Observatory (já existente) comparando cliques/impressões/queries EN vs PT. Se não houver tração, remove o subdiretório. Custo estimado: centavos/matéria.

## Decisões pendentes (Miguel)

- [ ] Aprovar piloto? Escopo: só manchetes ou editorias inteiras?
- [ ] Só inglês primeiro, ou inglês + espanhol? (ES = América Latina, competição menor)
- [ ] Implementação técnica: plugin (WPML/Polylang) vs mu-plugin próprio (padrão aditivo da reforma visual)
- [ ] Quem assina/valida a qualidade da tradução EN (gate)
- [ ] Sinergia com a **Editora Multilíngue** (memória de 27/07: livros PT/EN/ES/FR/中文/RU via Moka) — o site EN vira vitrine dos livros EN?

## ⚡ Atualização 27/07 ~17h — dossiê de evidências verificadas (memória §10)

Após feedback de Miguel ("não inspirou confiança"), tudo foi verificado **diretamente** (código, curl ao vivo, banco Tencent, API Search Console). Fatos novos que mudam o desenho:

1. **GSN já é o braço inglês do ecossistema e está no ar publicando hoje** (`globalsouth.news`, lang="en", geopolítica Sul Global). O "experimento inglês" já existe — medir o tráfego dele é o piloto natural.
2. **Canibalização GSN × Cafezinho hoje: ZERO** (verificado: línguas e temas separados; queries EN do Cafezinho ≈ 2 cliques/16 dias). **Mas** se o Cafezinho-EN fizer *geopolítica em inglês*, CRIA sobreposição real com o GSN. Divisão limpa proposta: **GSN = mundo visto do Sul · Cafezinho-EN = Brasil explicado ao mundo** (política BR + ciência para leitor internacional).
3. **Separação de contas Google CONFIRMADA** (8 portais → 8 projetos Cloud + 8 Search Consoles próprios, via API): memória de Miguel ("fiz tudo à parte") está correta.
4. **🚨 SEO Observatory MORTO desde 18/jun** (último log 03:02 "CONCLUÍDO COM SUCESSO"; cron ausente no Tencent; banco NYC = 0 bytes). Órfão da migração p/ NYC. **É o sistema que mediria o piloto EN — religá-lo é pré-requisito.** Registrado em BUGS_ATIVOS.
5. Prova de código: `indexador_google.py` não tem nenhuma referência a idioma e já é multi-domínio — indexar EN não muda nada no indexador.
6. `globalsouthnews.com` (.com) redireciona para site alheio — canônico é .news; avaliar recuperar o .com.

**Recomendação revisada:** antes de construir `/en/` no Cafezinho: (a) religar o Observatory; (b) puxar os números do Search Console do GSN (audiência EN real que já existe); (c) decidir divisão editorial GSN × Cafezinho-EN. Piloto continua barato e reversível, mas agora com mapa de território para não criar canibalização nova.

## Referências

- Memória técnica completa: `MEMORIA/memoria_cafezinho_site_multilingue_20260727.md`
- Nodo SEO: `CEREBRO_NODE_SEO_OBSERVATORY.md` (§12 — tema catalogado)
- Sinergia livros: `MEMORIA/memoria_plano_editora_multilingue_20260727.md`
- V4 ciência bilíngue (pipeline já fala EN): `CEREBRO_NODE_ATUALIZACOES.md` (27/07 13:30)
- Docs Google: search/docs/specialty/international/localized-versions · managing-multi-regional-sites · locale-adaptive-pages · essentials/spam-policies · apis/indexing-api
