# Fórum — Caso Master STF: 2º levantamento de sigilo (11/09 noite) + acervo consolidado em Reportagens/Master

**Sessão:** ZCode GLM-5.3 (Dell), 11/09 22:24→23:1x BRT · **Ordem do Miguel:** "vai no banco do stf e baixa todos esses processos, aproveita move aqueles que baixamos ontem para o mesmo diretorio, mas organizado por subdiretorios. Bota tudo num diretorio chamado Reportagens / Master, sob OUtros Pautas editoriais" (com a matéria do g1 de 11/09 19h47 colada).

**Gatilho:** Mendonça atendeu a Vice-PGR (Hindenburgo Chateaubriand, petição 115252 às 19:05) e levantou o sigilo de 18 processos do caso Master + >20 correlatos de ofício (frentes Flávio Bolsonaro, Ciro Nogueira, Cláudio Castro, Jaques Wagner, Thiago Miranda, Dark Horse). Vem depois do 1º levantamento de 10/09 (PET 16.704) já coletado ontem.

## Decisões resumidas

1. **Acervo consolidado** em `Outros/pautas editoriais o cafezinho/Reportagens/Master/` — um subdiretório por processo (CLASSE_NUMERO). Os 16 de ontem foram MOVIDOS de `Dia a dia/2026 Set 11/pet_16662_15556_stf/` (a origem ficou vazia); os novos de hoje copiados de `ZCodeProject/scratch/stf_111_noite/novos/`. Índice: `INDICE.md` no local.
2. **10 dos ~38 processos de hoje identificados e coletados** (ver tabela no INDICE.md): INQ 4.995 (74 peças/27MB — o inquérito Dark Horse do Flávio), PET 16.292, PET 16.369, PET 16.346 (Miranda), PET 15.674 + 15.873 (Ciro), PET 15.676 (Castro/RioPrevidência), PET 16.229 (Wagner), INQ 5.050, INQ 5.070. Fonte dos números: Congresso em Foco + checagem de sigilo individual no portal (todas 'Público').
3. **Seguem sigilosos** (não integraram): PET 16.078/16.063/16.059 (NC Flávio), 16.669 (Dino), 15.612, 16.070 (Karina Gama), INQ 4.781 (fake news). PDF público dos relatórios da PF (prazos Mendonça: Wagner 9d/Ciro 29d/Castro 75d) guardado em `extra/inq4781_relatorios_pf_poder360.pdf` (7,6MB).
4. **Receita do portal STF ATUALIZADA** (quebra importante): curl puro dá **403** agora — exige UA de navegador; abas AJAX exigem `X-Requested-With: XMLHttpRequest` + **`.asp` no path** + jar FRESCO por incidente (home→detalhe→aba com pausas de 2-3s; AWSALB gruda em backend ruim e regenerar o jar troca de backend). `listarProcessos.asp?classe=Pet&numeroProcesso=N` resolve Pet; para INQ usar **classe=Inq** (capitalizada!). Script reutilizável: `ZCodeProject/scratch/stf_111_noite/coleta.sh`.

## O que aconteceu / o que falta / o que preciso de você (Miguel)

- **Aconteceu:** acervo de ontem reorganizado (321 arquivos/91MB/16 processos); 10 novos processos coletados (~130 peças novas, INQ 4.995 é o mais rico); INDICE.md completo; extra com PDF da PF.
- **Falta:** (1) a lista ÍNTEGRA dos 18+20 — o despacho de 11/09 pós-19h ainda NÃO virou peça pública na PET 16.704 às 23:1x; com a lista (peça nova na abaDecisoes do incidente 7687920 ou DJE de 14/09) coletamos os ~28 números restantes; (2) PET 15.873/15.676/16.229 finalizaram após este registro? — conferir subdiretórios (fila rodando ao gravar este fórum); (3) zip consolidado para mídia WP ainda não feito.
- **Preciso de você:** nada obrigatório; opção: mandar zipar e subir o pacote 2 no WP como o de 79MB (Cloudflare cacheia .zip, não pesa — ver memória downloads-estaticos-wp).

## Adendo §2 (12/09 16:5x) — fotos ilustrativas CC adicionadas ao acervo

Ordem permanente do Miguel (11/09 ~23:2x, após a coleta): "não esqueça de encontrar sempre fotos boas, ilustrativas do assunto em questão". Concluída em 12/09 ~16:5x (interrompida na véspera): `Reportagens/Master/fotos/` com 6 fotos 1024px + CREDITOS.md — Mendonça plenário (Rosinei Coutinho/STF, Public Domain Mark license 10), Wagner (Edilson Rodrigues/AS), Flávio retrato + entrevista (Rodrigo Viana/AS), Ciro retrato (Rodrigo Viana/AS), Castro Congresso (Geraldo Magela/AS — todas CC BY 2.0). Vorcaro = capa CC0 269244 do WP; Miranda sem CC (não usar all-rights). Lição técnica: URL direta do Flickr tem 2 níveis de path (live.staticflickr.com/SERVER/ID_SECRET_b.jpg) — regex com 3 níveis não casa. Regra gravada também na auto-memory (fotos-boas-ilustrativas-sempre).
