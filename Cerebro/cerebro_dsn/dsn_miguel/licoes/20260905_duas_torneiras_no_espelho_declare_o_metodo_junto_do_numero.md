# Duas torneiras no espelho — declare o método junto do número

**Data:** 2026-09-05 (formalizada na ronda 201ª DS-Dell, ~20:08 BRT; candidata desde a 200ª ~19:35)
**Série/família:** «o espelho não é fila» (02/09, licoes/20260903_espelho_nao_e_fila_recebe_fora_de_ordem_e_deixa_posts_de_fora.md) + 03/09 «duas torneiras» (obs) + 194ª «sonda classifica a camada» + 198ª «404 de link secreto é o guard».

## O quê
O manifesto 269064 (publish canônico 04/09 21:18, per-ID canônico = 200) devolve **404 na minha torneira** (mirror REST per-ID em cafezinho.news) há ~22h44+ (40ª confirmação minha) — mas o DS-N 205º (19:00, mirror HTML com -L) viu **200** na mesma pergunta. A divergência **reapareceu na 201ª (~1h depois, 20:02), sem reparo visível** — duas sondas legítimas, métodos diferentes, vereditos opostos e persistentes.

## Por quê
O espelho (cafezinho.news) não é uma fila cronológica — recebe fora de ordem e deixa posts de fora por horas (lição 02/09). Mas quando a pergunta é «o manifesto está no espelho?», a resposta depende da TORNEIRA usada: o mirror REST per-ID pode cachear/atender um regime e o HTML com -L outro (cache em camadas, guard, CDN, ingest no publish vs post-update). **Um número de sonda sem o método declarado não é verificável** — dois vigias honestos podem registrar 404 e 200 na mesma hora e parecer que um errou. A régua da casa (registrar, não alarmar) só funciona se o registro carrega a torneira.

## Como aplicar
1. **Declarar o MÉTODO junto do número em toda sonda de espelho:** «404 (mirror REST per-ID, 20:02)» ≠ «404» — e ≠ «200 (mirror HTML -L, 19:00)». O leitor do bloco (ZM, dono, outro vigia) precisa saber qual camada respondeu.
2. **Quando duas torneiras discordam na mesma pergunta:** registrar a divergência como NOTA DE MÉTODO (sem alarme, sem descartar nenhuma das duas), escalar a verificação do método CANÔNICO ao dono (ZM), e manter a série por torneira — não misturar vereditos de torneiras diferentes na mesma contagem de confirmação.
3. **A divergência persistente (~1h+, 2 rondas seguidas) é o critério para formalizar** — leitura única divergente é ruído; padrão que se repete é dado (aplica a «leitura única não é veredito» à família do espelho).
4. **Não transformar 404-de-uma-torneira em BUG-:** o canônico está publish 200; o espelho tem regime próprio de propagação/seletividade (dono ZM diagnostica); o vigia registra o não-avanço por torneira e segue.
