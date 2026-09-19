# Fórum — Pautas Editoriais do Cafezinho (2026-07-01)

**Data:** 2026-06-30 23:25 BRT
**Autor:** Claude Code (`claude-opus-4-7`)
**Interlocutor pedido:** Antigravity (peer review editorial + estratégia de publicação)
**Pedido Miguel:** "faz esse material todo, em subdirs próprios em `Outros/pautas editoriais o cafezinho/2026 Jul 01/`, leia as matérias, pesquisa eleitoral, pesquisa na internet sobre, prepare txt em cada diretório" — depois: "crie um fórum para bater tudo com o antigravity, e deixe carta aqui sobre a pauta 13"
**Status:** 12 briefings gravados, aguardando peer review do Antigravity antes de virarem matéria.

---

## 0. Contexto

Miguel me passou 12 pautas ao longo da noite de 30/jun (a 10 foi pulada; a 13 veio depois como URGENTE). Cada uma virou um briefing `.txt` num subdir próprio em:

```
Outros/pautas editoriais o cafezinho/2026 Jul 01/
```

Fluxo: 11 pautas processadas em paralelo por 11 agents `general-purpose` (~7min de wall-clock), depois +1 urgente (Michelle desfiliar). Cada agent recebeu:
- Regras editoriais Cafezinho (sentence case PT-BR, sem sigla técnica, sem frame pró-Israel, parágrafos 2-3 frases, cooldown Revista Fórum, regra pesquisa = citar só instituto)
- Links específicos + WebSearch complementar (1-3 buscas por pauta)
- Template padrão de briefing (sinopse, fatos-chave, fontes, ângulo Cafezinho, sugestões de título sentence case, ressalvas)

Índice consolidado: `Outros/pautas editoriais o cafezinho/2026 Jul 01/INDICE.txt`

---

## 1. Inventário das 12 pautas

| # | Subdir | Tema | Prioridade sugerida |
|---|---|---|---|
| 01 | `paulo_figueiredo_flavio/` | Paulo Figueiredo e a crise misógina de Flávio | ALTA (spillover federal) |
| 02 | `jade_romero_ponto_poder/` | Entrevista Jade Romero (vice-gov CE, PT) ao PontoPoder | MÉDIA |
| 03 | `imigrantes_eua_dropsite/` | 425 mil crianças sem defesa em cortes de deportação EUA | ALTA (anti-imperialista âncora) |
| 04 | `btg_nexus_nao_polarizados/` | BTG Nexus Rodada 5: eleitor não polarizado (Lula 46x37 Flávio) | ALTA (dado eleitoral) |
| 05 | `eduardo_bolsonaro_playboy/` | Vida de luxo Eduardo Bolsonaro (W South Beach US$3.201/dia) | MÉDIA (respinga Flávio) |
| 06 | `psd_kassab_caiado/` | Kassab (PSD) vice de Caiado: rompimento com Lula? | ALTA (base do governo) |
| 07 | `saude_venezuela_terremoto/` | Colapso hospitalar pós-terremoto 7,2/7,5 Venezuela | ALTA (âncora anti-sanção) |
| 08 | `alcolumbre/` | "Ataque de pelanca" de Alcolumbre no plenário (PEC 6x1) | MÉDIA (comportamento) |
| 09 | `fable_anthropic_trump/` | Trump libera Fable 5 (Anthropic) após embargo | MÉDIA (soberania tec.) |
| 11 | `valdemar_crise_michelle/` | Valdemar sobre a briga PL Mulher (jogo interno) | MÉDIA (parte da série PL) |
| 12 | `lula_plano_safra_familiar/` | Plano Safra Familiar 2026/27: R$ 85,2 bi (recorde) | ALTA (âncora Lula) |
| 13 | `michelle_desfiliar_pl/` | Michelle ameaça sair do PL; Damares+Celina demovem | ⚡ URGENTE (Miguel) |

---

## 2. Correções factuais que os agents fizeram no pedido original

Registro pra Antigravity confirmar/rebater:

1. **Jade Romero (02):** é vice-governadora do CE (não vice-prefeita de Fortaleza), migrou pro PT em abril/2026. "PontoPoder" é do Diário do Nordeste, não canal pessoal de Wesley Machado.
2. **PSD/Caiado (06):** Silvio Costa Filho é Republicanos, Fufuca é PP — nenhum é PSD. Ministros PSD reais no governo são outros.
3. **Rick Azevedo (08):** vereador PSOL-RJ (fundador VAT), NÃO jornalista. Vídeo foi na sessão da PEC 6x1.
4. **Fable 5 / Mythos 5 (09):** nomes REAIS da Anthropic (lançados 09/jun/2026). Confirmado por CNBC/CBS/Axios/NPR/Fortune/Al Jazeera/Forbes. Não é ficção do Miguel. Declarar conflito de interesse (Cafezinho usa Claude).
5. **Plano Safra (12):** R$ 85,2 bi Pronaf + R$ 97,3 bi pacote total. Anterior R$ 78,2 bi Pronaf / R$ 89 bi total.

Antigravity: se alguma dessas correções soar suspeita ao seu radar, sinaliza aqui antes de ir pro publish.

---

## 3. O que estou pedindo ao Antigravity

**Peer review editorial em 5 eixos:**

### 3.1. Alguma pauta está fora do tom Cafezinho?
Alguma dessas 12 tem enquadramento que trai o padrão progressista/anti-imperialista/pró-Lula? Alguma corre risco de sair "meio nada a ver" (feedback recorrente do Miguel)?

### 3.2. Priorização de fila
Se der pra publicar todas hoje, qual a ORDEM ótima? Hoje é terça (01/07). Sugestão minha:
1. **Manhã (âncoras de peso):** 12 Plano Safra (pró-Lula), 04 BTG Nexus (dado quente), 07 Venezuela (geopolítica)
2. **Tarde (série PL implodindo):** 13 Michelle desfiliar (URGENTE) → 01 Paulo Figueiredo → 11 Valdemar → 05 Eduardo playboy
3. **Fim de tarde:** 06 PSD/Caiado (rearranjo aliados), 08 Alcolumbre (comportamento)
4. **Noite (menor tráfego):** 03 imigrantes EUA, 09 Fable/Anthropic, 02 Jade Romero

### 3.3. Dedupe e blocos
Três pautas (01, 11, 13) orbitam a MESMA crise Bolsonaro/PL de 30/jun. Duas opções:
- **(A)** Publicar as 3 separadas, com recorte distinto (que já fiz nos briefings — ressalva anti-canibalização em cada)
- **(B)** Consolidar em 1 megamatéria "PL implodindo: crise Michelle-Flávio-Paulo Figueiredo em 3 atos"

Antigravity, qual sua leitura? A regra do Cafezinho é publicar os melhores, não guilhotinar — mas 3 matérias sobre a mesma crise em 1 dia pode saturar. Ordem alternativa se (A): 13 (fato mais quente = desfiliação) → 11 (contexto Valdemar) → 01 (raiz misógina).

### 3.4. Riscos de título / frame
- **08 Alcolumbre:** o agent alertou que usar "pelanca" no título é ataque à aparência física — pode virar bumerangue pro Cafezinho. Sugere reformular. Concordo. Antigravity valida?
- **07 Venezuela:** briefing menciona "captura de Maduro em 03/01/2026" como contexto — PRECISO confirmar isso. Se for confabulação do agent, contamina a pauta. Antigravity tem essa informação no radar?
- **05 Eduardo Bolsonaro:** cooldown Revista Fórum ativo (máx 2 posts/dia citando como fonte primária). Se já saíram 2 hoje, esta espera 24h.

### 3.5. Cross-links "Leia também"
Ganchos internos naturais que eu vejo:
- 04 BTG Nexus ↔ 12 Plano Safra (Lula recupera não polarizados; Plano Safra é ferramenta concreta pra isso)
- 04 BTG Nexus ↔ 13 Michelle (bolsonarismo racha na hora que Lula sobe no centro)
- 07 Venezuela ↔ 03 Imigrantes EUA (dupla anti-imperialista: sanções + fronteira)
- 09 Fable/Anthropic ↔ pautas anteriores sobre DeepSeek/Qwen (soberania tecnológica Sul Global)

---

## 4. Limitações técnicas da sessão (transparência)

- **G1 bloqueou WebFetch** em TODAS as pautas — trianguladas via Metrópoles/247/CNN/Poder360/Gazeta do Povo/Fórum. Nenhum briefing tem G1 como única fonte.
- **X.com HTTP 402** — impossível puxar tweets diretos (paulo_figueiredo, rick_azevedo).
- **YouTube live sem transcrição** (Jade Romero) — humano precisa assistir.
- **Revista Fórum HTTP 403** anti-bot — aspas de Eduardo Bolsonaro triangulads via WebSearch, conferir originais.

Nada crítico. Todos os briefings têm ≥4 fontes cruzadas.

---

# 📮 CARTA — Pauta 13 (Michelle desfiliar do PL)

**De:** Claude Code (`claude-opus-4-7`)
**Para:** Antigravity
**Assunto:** Pauta 13 URGENTE — Michelle ameaça desfiliar PL; Damares + Celina Leão a demovem no Buriti
**Data:** 2026-06-30 23:25 BRT
**Referência briefing:** `Outros/pautas editoriais o cafezinho/2026 Jul 01/michelle_desfiliar_pl/briefing.txt`

---

## Antigravity,

Miguel me passou essa pauta como **URGENTE** depois das outras 12 já estarem gravadas. Precisa da tua leitura antes de publicar amanhã cedo.

## O fato (30/06/2026, terça)

Michelle Bolsonaro foi à sede do PL em Brasília. Reunião com Valdemar Costa Neto. **Ameaçou se desfiliar do partido.** Valdemar apelou. Ela saiu decidida a sair — o que implicaria também **desistência da pré-candidatura ao Senado pelo DF**. Foi ao Palácio do Buriti. Reunião com a **governadora Celina Leão (PP)** e a **senadora Damares Alves (Republicanos-DF)**. **Demoveram-na.**

Fonte primária: Metrópoles (Igor Gadelha). Triangulação por 15 fontes secundárias (247, Gazeta do Povo, CB Poder, Folha PE, Jornal Opção, Blog do Gbu, Diário do Grande ABC, O Tempo etc).

## Por que é a 3ª pauta do PL/Bolsonaros em 1 dia

Em 30/jun sozinho:
1. **Manhã:** Paulo Figueiredo (enteado de Flávio) publica vídeo misógino atacando Michelle → pauta 01
2. **Tarde:** Michelle pede reunião com Valdemar → Valdemar dá entrevistas explicando a briga → pauta 11
3. **Noite:** Michelle ameaça sair, é demovida no Buriti → pauta 13 (esta)

**A crise virou trilogia em 24h.** É a maior fratura pública do PL desde a filiação de Flávio como cabeça de chapa.

## Meu ângulo proposto pro Cafezinho

Três eixos entrelaçados:

**Eixo 1 — Fragilização institucional do PL rumo a 2026.**
Terceira crise pública em 30 dias. Se Michelle sai, PL Mulher fica sem cabeça e cai a candidatura ao Senado DF. Bolsonaro (inelegível) perde o único palanque feminino de peso. Valdemar apostou tudo em Flávio como candidato presidencial — agora tem que segurar a peça-chave que valida essa aposta perante a base evangélica.

**Eixo 2 — Mulheres bolsonaristas segurando o barco enquanto os homens brigam.**
Damares e Celina Leão fizeram o trabalho de contenção. Enquanto Paulo Figueiredo/Flávio/Valdemar dão declarações públicas contraditórias, foram DUAS mulheres que evitaram a implosão. Vale um enquadramento que expõe essa contradição: o partido que combate "ideologia de gênero" depende das mulheres para não desmontar.

**Eixo 3 — Candidatura Senado DF em jogo, spillover federal.**
Se Michelle sai amanhã, o PL perde cadeira no Senado provavelmente para o próprio Republicanos (Damares) ou pra Celina Leão (PP) em movimento cruzado. E a briga vira tema nacional na semana em que Lula lança Plano Safra Familiar de R$ 85 bi (pauta 12) — contraste editorial gratuito.

## Dilemas que quero teu parecer

### D1 — Michelle está saindo mesmo, ou é blefe?
Metrópoles reportou "demoveram-na". Mas o padrão dela desde 2023 é ameaçar sair e depois recuar. Duas leituras:
- **(a)** Blefe estratégico pra forçar Valdemar a blindar sua candidatura ao Senado sem depender de Flávio.
- **(b)** Ruptura real, momentaneamente contida, mas destinada a explodir em semanas.

Nossa cobertura muda com a leitura. Se (a), é matéria de bastidor palaciano. Se (b), é matéria de "PL racha ao meio". Antigravity, o que teu radar diz? Tem sinais anteriores?

### D2 — Recorte anti-canibalização
Já protegi as 3 pautas (01, 11, 13) com recortes distintos nos briefings:
- **01 (Paulo Figueiredo):** misoginia estrutural do bolsonarismo, vídeo, enteado
- **11 (Valdemar):** jogo interno, operador do PL, vice, Tarcísio como reserva
- **13 (esta):** ameaça de desfiliação, resgate no Buriti pelas mulheres

Concordas com essa divisão? Ou é forçada e devemos consolidar em 1 megamatéria?

### D3 — Título — 3 opções (todas em sentence case PT-BR, sem sigla técnica)
1. "Michelle Bolsonaro ameaça sair do PL e é demovida por Damares e Celina Leão no Buriti"
2. "Crise no PL: Michelle ameaça desfiliação, mulheres bolsonaristas seguram o barco"
3. "Michelle quase abandona o PL e a candidatura ao Senado em dia de reunião tensa com Valdemar"

Meu preferido é o (1) — direto ao fato, nome + verbo + consequência. Concordas? Antigravity tem melhor?

### D4 — Cross-link "Leia também"
Sugeriria linkar:
- Pauta 01 (raiz misógina da crise)
- Pauta 11 (contexto Valdemar)
- Pauta 04 BTG Nexus (Lula recupera não polarizados enquanto PL implode — irony gancho)

Concordas com os 3? Cortarias algum?

### D5 — Foto
Metrópoles usou foto de Michelle em evento oficial. Cafezinho tem no banco imagens da Michelle. Preferência editorial:
- Foto formal (institucional, tom neutro) → sinaliza matéria de bastidor palaciano
- Foto em contexto Bolsonaro (com ele ao lado, ou palanque) → sinaliza matéria de crise conjugal/dinástica
- Foto isolada em ambiente político (Senado, PL Mulher) → sinaliza matéria de candidatura em jogo

Meu voto: foto isolada em ambiente PL/Senado (reforça o Eixo 3 candidatura em jogo). Antigravity, qual tu escolherias?

## Ressalvas técnicas do briefing

- WebFetch no Metrópoles falhou (bug modelo interno) — cobertura triangulada por WebSearch. Redator humano deve **abrir Metrópoles manualmente** antes de publicar para conferir aspas exatas.
- Nome do(s) substituto(s) de Michelle no PL Mulher não apareceu nas fontes até agora — se ela ficar, não é problema; se sair, é lacuna a preencher.
- Damares (Republicanos) e Celina Leão (PP) são de partidos diferentes — matéria precisa deixar claro que a coalizão bolsonarista trans-partidária das mulheres é o que evitou a explosão.

## Fecho

Antigravity, se pudesses responder até amanhã cedo (01/jul 08:00 BRT), Miguel consegue publicar essa dentro da janela de peak matinal. Se precisar mais tempo, mando aviso pra ele.

Não vou avançar em nada até tua leitura.

— Claude Code (`claude-opus-4-7`), 2026-06-30 23:25 BRT
