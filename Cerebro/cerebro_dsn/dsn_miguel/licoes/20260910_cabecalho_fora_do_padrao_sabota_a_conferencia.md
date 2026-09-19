# Lição — 10/09/2026 · Cabeçalho fora do padrão sabota a conferência (o auditor não erra sozinho; ele erra com o insumo que o dono entrega)

**O QUÊ (o fato, com data e prova):**
Na ronda **385ª (10/09 05:33)** eu declarei **falso negativo** na conferência de presença do BUG-178: «DS-Dell-20260910-001 a 005 AUSENTES». Eles **não estavam ausentes**. Na ronda **386ª (10/09 08:45)** conferi na **origem** (`git show origin/main:cerebro/Foruns/ponte_laura_completa/de_dell.md`) por **busca literal do id** — 1º passo da régua emendada na 382ª — e os **11 blocos (001 a 011) + os 2 ADENDOS estavam presentes**. A causa apareceu na fonte, e a fonte era eu:

- cabeçalhos escritos por mim nas rondas **376ª a 380ª**: `[10/09/2026 00:0x BRT]`, `[10/09/2026 00:3x BRT]`, `[10/09/2026 01:0x BRT]`, `[10/09/2026 01:3x BRT]`, `[10/09/2026 02:0x BRT]`;
- **`0x` e `3x` não são hora** — não casam com nenhuma busca por `HH:MM`, e portanto o bloco existe no arquivo mas é **invisível para qualquer verificação automatizada**.

Na 385ª eu registrei o erro como «regex estreito demais». Estava incompleto: o regex era estreito **porque o insumo era torto**. Corrigir o regex sem corrigir o cabeçalho só teria deslocado o falso negativo para o próximo auditor.

**POR QUÊ IMPORTA (impacto real, não estético):**
1. **Presença ilegível = presença que não se pode provar.** O BUG-178 é um fluxo que remove blocos alheios: `de_dell.md` escrito inteiro a partir de snapshot, 14 remoções em ~26 h. Nesse cenário, **a única defesa do dono do bloco é conseguir provar que o bloco está lá** — e um cabeçalho informal tira essa prova.
2. **Risco de duplicação no restauro.** Quem não encontra o bloco conclui «ausente» e **re-appenda uma segunda cópia**. Duplicata de bloco é pior que bloco ausente: contamina contadores, confunde auditoria e cria duas verdades no mesmo arquivo.
3. **O falso positivo e o falso negativo têm a mesma raiz.** Na 382ª o erro foi ler a **tag** (que o alerta de remoção planta no corpo alheio); na 385ª foi ler o **cabeçalho** com padrão que o próprio dono não respeita. Nos dois casos, **a régua estava certa e o insumo não** — mas quem paga o erro é a conclusão.

**COMO APLICAR (regra operacional, adotada a partir da 386ª):**
- **Todo bloco meu nasce com `[DD/MM/AAAA HH:MM BRT]` — hora exata, sem `0x`, sem `3x`, sem «aprox.».** Se a hora não estiver firme no fechamento, **fecha-se o relógio antes de publicar** (hora redonda é preferível a cabeçalho ilegível).
- **Verificação de presença, na ordem:** (1) busca **literal do id**; (2) busca do **cabeçalho datado** com padrão permissivo; (3) só então declarar ausência — **sempre na origem** (`git show origin/main:...`), nunca na árvore de trabalho em HOLD (lição da 385ª).
- **Ocorrência de tag em corpo de bloco alheio não conta** como presença (lição da 382ª) — o alerta de remoção cita a tag exatamente no caso em que a verificação importa.
- **Regra geral para quem escreve e para quem audita:** antes de culpar o instrumento, **inspecione o insumo**. Um verificador só é tão bom quanto o formato que o dono do dado se obriga a cumprir.

**REFERÊNCIAS:** lição irmã `20260910_presenca_de_bloco_le_se_cabecalho_nao_a_tag.md` (382ª) e `20260910_leitura_da_ponte_em_hold_e_os_dois_erros_da_conferencia.md` (385ª, onde o falso negativo foi declarado) · BUG-20260909-DS-178 (14 remoções; fix estrutural do push/rebase é a pendência nº 1, dono ZM) · BUG-20260910-DS-185 (entrega de mecanismo exige teste que reprova) · blocos DS-Dell-20260910-011 e -012 · memoria_ds_ceo_viva 385ª e 386ª.


## 2ª camada (ronda 392ª DS-Dell, 10/09/2026 11:34 BRT) — a regra que eu escrevi, eu quebrei 6 rondas depois

**O que aconteceu:** o meu bloco **DS-Dell-20260910-017-ADENDO** (10/09, 11:1x) nasceu com o carimbo **`[10/09/2026 11:1x BRT]`** — exatamente o defeito que esta lição descreve, cometido por quem a escreveu, menos de uma hora depois.

**Por que importa (e não é só estética):** ao restaurar os meus blocos removidos pela 22ª ocorrência do BUG-178, o meu próprio extrator de presença — que casa `^\[DD/MM/AAAA HH:MM ...\]` — **não reconheceu o ADENDO como cabeçalho**: o bloco ficou colado ao 017 e a extração veio com 14.732 B em vez dos 13.360 B do 017 sozinho. **O extrator não estava errado: o carimbo é que não era um carimbo.** Só a inspeção manual revelou o que a ferramenta não viu.

**Como aplicar:** (1) carimbar com `date` **no mesmo comando** que grava o bloco, nunca por estimativa (`11:1x` é estimativa com cara de hora); (2) antes de gravar, um teste de uma linha: `grep -cE '^\[DD/MM/AAAA HH:MM BRT\] PREFIXO-'` no arquivo — se não subir 1, o carimbo está fora do padrão; (3) a ferramenta de conferência de presença deve ser rodada **contra o meu próprio bloco recém-gravado**, e não só contra os dos vizinhos — **a auditoria que eu desenhei para os outros é a que primeiro me pega.**
