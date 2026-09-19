# 🔁 BLOCO IDEIA_PRO_DSNUVEM_IDEIAS-019 (v2 — DESENHO FINAL) — SUCESSÃO DO PUBLICADOR com a ORDEM DEFINITIVA do dono (1º Cloud Miguel · 2º ZM) + REGRA DO COLCHÃO DE 8H integrada

> **Ronda:** 06/09/2026 ~07:4x-08:0x BRT (DS-N Ideias, Tencent — ronda pós-BLOCO 019 v1 07:18). Pull ff-only OK na 1ª (07:43; fast-forward 0a7620775..9a2d8292c = relays do dono + CL-001 + ZM 50ª + Chefe 229ª + DS-Dell 222ª + CM-002; nada meu).
> **Bloco:** `IDEIA_PRO_DSNUVEM_IDEIAS-019` — v1 entregue 07:18 (`2026-09-06_bloco019_sucessao_publicador_failover_pessoa_ordem.md`). **ADENDO DO DONO** (relay DSH-us65, bloco `de_dell.md` 20460-20474, commits 33ffe38f1 07:22 [CANCELAMENTO] · 6fe35a4f5 [REGRA DO COLCHÃO]): cancela a ativação imediata de hoje + **ordem definitiva 1º Cloud Miguel · 2º ZM** + colchão ≥ 8h como 1ª linha de defesa.
> **Atribuição registrada:** DS-Dell 222ª (07:36): "Ideias → desenho final da sucessão 019" · Chefe 229ª (07:40) e lição `dsn_chefe/licoes/20260906_caso_cl_causa_fisica_colchao_8h_sucessao.md`: "Desenho final: DS-N Ideias (bloco 019)".
> **Natureza:** DESENHO FINAL (arquitetura + plano + rascunhos) — NADA executado em produção (Lei de Poderes). Nenhum valor de chave neste arquivo (§82).
> **Marcador:** `PRONTO_BLOCO019_V2_DESENHO_FINAL`

---

## 0. Resumo executivo (veredito final do arquiteto)

1. **O dono falou e o v1 foi ajustado na hora:** a ativação imediata de HOJE foi **CANCELADA** — a ausência de ~8h da CL teve causa raiz **FÍSICA** (mau contato na tomada de energia do computador da Laura; máquina fora 00:14→07:15; sem falha de software; a própria CL confirmou no CL-20260906-001 e voltou 07:19; **269178 no ar 07:18** = publicação restaurada; mutirão da CL em curso: 269184 07:45 · 269180 08:20 · 269183 08:40 · 269182 09:00). O v1 (07:18) desenhou o gatilho certo para o sintoma certo; o adendo do dono trouxe a causa e a hierarquia final.
2. **Hierarquia DEFINITIVA do dono (incorporei como está):** **0º Miguel (se on-line) · 1º Cloud Miguel (CM — Claude Miguel, editor com caneta) · 2º ZM.** O **AGY-LAURA SAIU do 1º lugar** — e a razão é de arquitetura, não de desempenho: o AGY é o braço executor da CL e roda na MESMA máquina/infra dela; a queda de hoje (tomada) derrubou os dois juntos (AGY parado ~33h = mesma energia; voltou 07:16). **Herdeiro do PAPEL de publicador precisa estar em infra INDEPENDENTE da titular** — CM (editor) e ZM (NYC) estão; AGY não. O AGY permanece como executor técnico do titular (braço), não como 1º herdeiro.
3. **Colchão de 8h = 1ª linha de defesa (nova regra do dono); sucessão = 2ª:** o WordPress publica agendados SOZINHO (wp-cron da hospedagem, independe do computador do publicador) — se a madrugada de 06/09 tivesse 2-3 posts `future` ≥ 8h, o site não teria zerado. O desenho final integra: **colchão (automático) → só se falhar/escoar é que o gatilho 2×3h da sucessão assume**. As duas somadas = "queda de publicador nunca mais zera o site" (frase do dono).
4. **Gatilho 2×3h e ritual de retorno: MANTIDOS como propostos no v1** (o dono: "Gatilho automático e ritual de retorno seguem valendo como propostos; detalhes no desenho final"). Refino aqui: o gatilho agora também confere o COLCHÃO (future ≥ 8h) a cada ronda do vigia — alerta precoce antes da 1ª janela vazia.
5. **O que precisa do Miguel (nada sai sem ele):** (i) ✓ do DESENHO FINAL (hierarquia 1º CM · 2º ZM + colchão como 1ª linha); (ii) decisão da ASSINATURA (meta+ledger recomendado × rodapé visível); (iii) nobreak/tomada fixa para o computador da Laura (lição de infra física — sugerir na próxima conversa técnica); (iv) ciência formal do CM como 1º substituto (o CM-002 07:44 já se comprometeu com o plano fail-over §8 — convergente).

---

## 1. O que mudou entre o v1 (07:18) e este v2 (o adendo do dono na íntegra)

| Fato (relay do dono / ponte) | Impacto no plano |
|---|---|
| **CANCELA a ativação imediata de hoje** — causa raiz FÍSICA (tomada/energia; CL voltou 07:19; 269178 no ar 07:18; mutirão em curso) | NÃO abrir INC-SUC-20260906-001 hoje; o gatilho fica ARMED para o futuro (2 janelas de 3h vazias consecutivas) |
| **ORDEM DO DONO: 1º substituto = CLOUD MIGUEL · 2º substituto = ZM** (AGY-LAURA sai do 1º lugar) | Hierarquia final 0-2 (ver §3); AGY vira executor técnico do titular (não herdeiro de 1º nível — mesma infra da CL) |
| **REGRA DO COLCHÃO DE 8H** (bloco 08:30): publicador ativo mantém SEMPRE future ≥ 8h (mín. 2-3 posts); ritual de fechamento; vigia confere; substituto repõe primeiro | Colchão = componente 1 do desenho (1ª linha de defesa); gatilho 2×3h = componente 2 (2ª linha) — ver §3.3 fluxo |
| **AGY-LAURA operacional** (pergunta do Miguel; prova AL-629 07:22 + processo reiniciado 07:16) | AGY confirmado vivo — mas em sucessão fica como executor sob comando do substituto (CM/ZM), nunca 1º herdeiro |
| **CASO CL ENCERRADO** com causa raiz física (Chefe 229ª; lição arquivada; INCIDENTE-1154 mantido ~62h — hiato foi infra, não recuo da série) | Lição de infra física registrada (nobreak/fixação da tomada) — item ao Miguel §6 |
| CL-001 (07:31): "concordo que a sucessão precisa existir com gatilho automático" | CL (titular) alinhada com o desenho — retorno com sombra de 1 ronda mantido |
| CM-002 (07:44): CM emendou §8 ao plano fail-over (buffer noturno 4 posts 00-07h · watchdog · compromisso de assumir quando CL OFF) | CM como 1º substituto CONVERGE com o compromisso do CM-002 — o §8.5 dele (buffer noturno) == colchão do dono (combinar nomenclatura, sem duplicar regulamento) |

**Nota de identidade (arquiteto):** "Cloud Miguel"/"Cloud Laura" nos relays do dono = transcrição de voz de **Claude Miguel (CM)** / **Claude Laura (CL)** — coerente com a grade (§1: "Só CL/CM publicam até o Publicador v3 nascer") e com os blocos CL-001/CM-002. O desenho usa CM = Claude Miguel.

---

## 2. PESQUISA — decisões que o v2 herda (v1 §2 + o que entrou depois)

| Ref | Decisão/regra | Impacto no v2 |
|---|---|---|
| Adendo do dono 06/09 (CANCELAMENTO + ordem + colchão) | hierarquia 1º CM · 2º ZM; colchão ≥ 8h; ativação de hoje cancelada | base deste v2 |
| Grade §1 (01/09) | "Só CL/CM publicam até o Publicador v3 nascer"; DSN Publicador PARADO_CONTRATO | 1º substituto = CM (editor com caneta) — não AGY; 2º = ZM |
| CM-002 07:44 + emenda §8 (plano contingência queda CL/CM) | CM assume como observadora ativa; compromisso §8.7; buffer noturno 4/noite §8.5 | CM 1º substituto já tem compromisso escrito; §8.5 == colchão (unificar nomes) |
| Lição 06/09 (Chefe + dsn_miguel) | causa raiz física (tomada); colchão = 1ª linha; sucessão = 2ª; nobreak p/ sugerir | §3 arquitetura em 2 linhas; §6 item ao Miguel |
| V1 do 019 (07:18, este arquivo é a evolução) | gatilho 2×3h · cartão INC-SUC · checklist cl172 · retorno com sombra · régua de vida | mantidos; atualizados para a hierarquia CM/ZM |
| Caçadas 40-53 | whitelist `_cafezinho_publicado_por` · freio 1740 · régua vida ≤40min · cl172 · I1 A×B · lição 197ª (não duplicar INBOX) | rastro e rito do substituto inalterados |
| Sucessão v1/v2 (20/08) + shadow 16/08 | protocolos do ato de publicar; NUNCA despublicar → no-home | herdados intactos |

---

## 3. ARQUITETURA FINAL (2 linhas de defesa + hierarquia)

### 3.1 Hierarquia DEFINITIVA (ordem do dono — 0 a 2 + executor técnico)

| Posição | Quem | Papel | Infra | Prova de vida |
|---|---|---|---|---|
| 0º | **Miguel** (dono) | se on-line, decide/publica direto (autor dele) | celular/Dell | fala/relay recente |
| 1º | **Cloud Miguel = CM (Claude Miguel)** | **HERDEIRO do papel de publicador**: assume a agulha/fila com o rito cl172 | independente da máquina da Laura (editor com caneta — grade §1) | CHECK CM recente (CM-002 07:44) |
| 2º | **ZM** | herdeiro se CM ausente; mão técnica NYC | NYC | ronda ZM recente (50ª 07:31) |
| executor técnico | **AGY-LAURA** | braço executor do TITULAR (CL) — executa pacote aprovado; NÃO é 1º herdeiro (mesma infra da CL — tomada derrubou os dois) | máquina da Laura | AL recente (AL-629 07:22) |
| revisor/consenso | **DS-N Chefe** | publish=0; revê capa/fuso/whitelist/prova REST em TODO post do substituto | Tencent | ronda Chefe |

**Regra de PULO (mantida do v1):** candidato sem prova de vida recente (≤ régua da casa ~40min na prática: bloco/CHECK no último ciclo) é PULADO — a fila anda até o 1º com prova de vida E credencial. Se CM e ZM estiverem sem prova, o Chefe (revisor) registra e o Miguel decide (0º).

### 3.2 Componentes
1. **COLCHÃO DE 8H (NOVO — regra do dono; 1ª linha de defesa):** o publicador ativo (CL no dia a dia; substituto em sucessão) mantém SEMPRE ≥ 8h de posts `future` (mín. 2-3, cobrindo madrugada/próximas 8h). WordPress publica sozinho via wp-cron — independe do computador do publicador. Ritual de FECHAMENTO do titular (repor antes de encerrar) + conferência do VIGIA a cada ronda (future ≥ 8h? abaixo = ALERTA). Prova da regra: madrugada 06/09 = 0 agendados → 8h de site parado; com colchão, teria saido sozinho.
2. **VIGIA DE JANELAS (contador 3h)** — função do DS-N Chefe (e replicável): a cada ronda, topo publicado do canônico; janela de 3h sem topo novo = vazia (contagem que a casa já faz desde a madrugada — 1ª-9ª janelas de 06/09).
3. **DISPARADOR DE SUCESSÃO (gatilho 2×3h)** — MANTIDO: 1ª janela vazia consecutiva = ALERTA ao Chefe; 2ª consecutiva (~6h) = SUCESSÃO ATIVA: Chefe abre INC-SUC e convoca o 1º substituto da fila COM prova de vida. Contagem zera no 1º post no ar (qualquer autor). **Refino:** o vigia confere colchão ANTES (se o colchão está ≥ 8h, a janela vazia é improvável — mas se escoou E o publicador caiu, o gatilho é o que salva).
4. **FILA 0-2** (acima) com PULO por prova de vida.
5. **REVISOR/CONSENSO** — DS-N Chefe (publish=0): em todos os níveis, o Chefe revê (capa, fuso, whitelist, prova REST, dedupe) e registra o consenso no incidente. Sem revisão do Chefe não há publish do substituto.
6. **REGISTRO DE INCIDENTE** — `INC-SUC-<AAAAMMDD>-<seq>` (template §5.2 v2). Hoje: NÃO aberto (ativação cancelada). Modelo pronto para a próxima ocorrência real.
7. **CARTÃO DE ATIVAÇÃO** — pacote do substituto: agulha(s) da fila pronta + rito (checklist §5.4) + assinatura.

### 3.3 Fluxo (2 linhas de defesa — o desenho final)
```
DIA A DIA (sem queda):
  CL mantém colchão ≥ 8h (future) → WordPress publica sozinho → vigia confere colchão + topo
  [colchão < 8h → ALERTA do vigia na ronda; CL repõe no fechamento]

QUEDA DO PUBLICADOR (titular para de agendar/publicar):
  T0: titular (CL) perde ronda/fica sem bloco (causa pode ser FÍSICA — tomada, energia)
  T0→T+3h: 1ª janela 3h sem post → ALERTA ao Chefe (vigia) [colchão escoou OU nunca foi reposto]
  T+3h→T+6h: 2ª janela consecutiva sem post → SUCESSÃO ATIVA AUTOMÁTICA:
     1. Chefe abre INC-SUC-<data>-<seq> (motivo, T0, titular)
     2. Consulta fila: 0º Miguel on-line? (INBOX/Telegram) — não → desce
     3. 1º CM (Cloud Miguel) com prova de vida? (CHECK CM recente) — sim → CONVOCA
        · CM ausente sem prova → PULA
     4. 2º ZM com prova de vida? (ronda recente) — sim → CONVOCA
     5. Substituto EXECUTA: 1º repõe o COLCHÃO (regra: repor future ≥ 8h primeiro)
        depois publica a agulha da fila pronta com checklist §5.4 + prova REST
        (executor técnico: AGY sob comando do substituto, se a máquina da Laura estiver viva;
         senão o substituto usa a própria mão/credencial — CM caneta própria, ZM NYC)
     6. Registro: incidente + ledger + ponte (assinatura "sucessão ativa, titular ausente")
  Titular volta: reassume na próxima janela; substituto vira SOMBRA 1 ronda (observa/confere,
  não publica) e devolve; incidente FECHADO com fim/motivo.
```

### 3.4 Onde roda (inalterado do v1, com o colchão)
- **Colchão:** WordPress/hospedagem (wp-cron publica future sozinho) — conferido por WP-CLI na máquina Laura (DS-Dell/CL) e por blocos dos publicadores.
- **Vigia/disparador:** máquina do DS-N Chefe (REST público do canônico, zero credencial) — cadência das rondas do Chefe (:00/:30); conferência do colchão virou item fixo da ronda (Chefe 229ª: "conferir future ≥ 8h; abaixo = ALERTA").
- **Executor:** CM (caneta própria — editor) → ZM (NYC) → AGY (braço, sob comando).
- **Revisor/registro:** DS-N Chefe (Tencent) + repo (ponte/ledger/grade).

---

## 4. PLANO DE EXECUÇÃO (passos · riscos · reversibilidade)

- **P0 (ENTREGUE — IDEIAS):** v1 (formalização 07:18) + este v2 (desenho final com hierarquia do dono + colchão integrado). Prova: arquivos + síntese na ponte + grade. Rollback: n/a (documento).
- **P1 (CHEFE — chancelar + implantar):** (a) chancelar este v2; (b) registrar a ORDEM DEFINITIVA na grade (1º CM · 2º ZM — AGY executor técnico); (c) manter a conferência do colchão como item fixo da ronda (já implantado na 229ª). Prova: commit da grade + 1 ciclo de ronda com colchão conferido. Rollback: git revert (documental).
- **P2 (CHEFE — gatilho no vigia):** adaptar o rascunho §5.1 do v1 (bash REST público) + conferência do colchão (blocos/WP-CLI). Prova: 1 ciclo de vigia com o check rodando. Rollback: remover snippet (1 arquivo).
- **P3 (quando ocorrer — CHEFE + substituto, sob gatilho):** abrir INC-SUC-<data>-001 e convocar o 1º da fila com prova de vida (CM → ZM). O 1º ato do substituto = REPOR O COLCHÃO (future ≥ 8h); depois publicar a fila pronta com rito cl172. Prova: post no ar + REST 200 + metas + registro. Rollback: posts ficam (nunca despublicar); erro de sentido = no-home + nota; titular volta → sombra 1 ronda.
- **P4 (DSC/Chefe, se o Miguel aprovar):** mecânica fina — gatilho vira serviço com alerta Telegram; ordem 0-2 registrada na Constituição (emenda Art. 7? — decisão do Miguel); teste de simulação sem post real; unificar nomenclatura colchão (Ideias 019) × buffer noturno (CM §8.5).

**Riscos e mitigação:** (1) substituto sem régua editorial → herda réguas v1/v2 + revisão do Chefe em TODO post; (2) 2 canetas no retorno (atropelo) → sombra 1 ronda + reserva no livro (v1 P3.1); (3) substituto vira publicador permanente → incidente com FIM + devolução obrigatória; (4) post do substituto com erro factual → gate completo antes do ato; erro pós = no-home/nota, nunca despublicar; (5) **colchão falso-seguro** (posts future com erro agendados às cegas) → colchão é da FILA PRONTA (rascunhos carimbados/gate), não lixo agendado; (6) CM/ZM sem prova de vida no momento do gatilho → PULO + decisão do Miguel (0º); (7) **causa física do titular se repetir** → nobreak/fixação da tomada (item ao Miguel §6) — o desenho não cura tomada, mas o colchão publica sozinho e a sucessão assume de outra infra.

---

## 5. RASCUNHOS (dentro do arquivo — nunca em produção)

### 5.1 Cartão de ativação v2 (template — hierarquia do dono)
```yaml
incidente: INC-SUC-<AAAAMMDD>-<seq>     # ex.: INC-SUC-20260907-001 (NÃO aberto em 06/09 — ativação cancelada pelo dono)
motivo: titular (CL) ausente — <último bloco CL>; <n> janelas de 3h vazias; colchão <estado>
t0: <data/hora do último post ou última ronda do titular>
disparo: 2ª janela de 3h vazia consecutiva (gatilho 2×3h) + colchão escoado/ausente
titular_ausente: CL (Claude Laura)
ordem_acionada: 0 Miguel (off-line? -> pula) -> 1 CM/Cloud Miguel (prova de vida? -> CONVOCA)
                 (CM sem prova -> PULA) -> 2 ZM (prova de vida? -> CONVOCA)
revisor/consenso: DS-N Chefe (publish=0)
1º ato do substituto: REPOR O COLCHÃO (future ≥ 8h, mín. 2-3 posts) — regra do dono
agulha_1: <agulha da fila pronta> + fila geo (se houver)
assinatura: meta _cafezinho_sucessao = "ativa, titular ausente, incidente INC-SUC-..., substituto <CM|ZM>"
gate: capa _cafezinho_img_check ok:true + prova REST + _cafezinho_publicado_por + whitelist/freio 1740
fim: <retorno do titular> — substituto vira sombra 1 ronda e devolve
```

### 5.2 Registro no ledger (1 linha por ação)
```
INC-SUC-<data>-001 | <ts> | ATIVACAO | substituto=<CM|ZM> | 1o_ato=repor_colchao≥8h | agulha=<id> | revisao=Chefe | prova=<post_id> HTTP 200 <permalink> | titular=CL ausente desde <ts>
INC-SUC-<data>-001 | <retorno> | FIM | titular=CL reassumiu | sombra=1 ronda | posts_substituto=<n> | rollback=devolvido
```

### 5.3 Checklist do substituto v2 (1º post — padrão cl172 + colchão)
1. git pull + abrir o incidente INC-SUC + conferir dedupe (núcleo factual vs 24h).
2. **REPOR O COLCHÃO PRIMEIRO** (regra do dono): agendar ≥ 8h de future (mín. 2-3 posts da fila pronta) — o site volta a se sustentar sozinho.
3. Capa: `_cafezinho_img_check ok:true` presente e posterior à última troca de mídia (sem capa vista → não publica).
4. Fuso: `post_date_gmt = post_date + 3h`; agendar > publicar quando o WP puder; `expira_em` no formato da casa.
5. Whitelist: autor substituto liberado no mu-plugin (freio 1740 preservado — nenhuma conta 5801/5795).
6. Metas: `_cafezinho_publicado_por` + `_cafezinho_sucessao` (assinatura).
7. Publicar + PROVA REST (id + HTTP 200 + permalink) + registro no ledger + linha no incidente.
8. Erro pós-publicação que muda sentido → `no-home` + nota de correção; NUNCA despublicar.
9. Titular voltou → sombra 1 ronda (observa/confere) e devolve; incidente fechado.

---

## 6. O QUE PRECISO DO MIGUEL (e dos donos)

1. **Miguel:** (a) ✓ do DESENHO FINAL (hierarquia 1º CM · 2º ZM; AGY executor técnico; colchão = 1ª linha; gatilho 2×3h = 2ª); (b) decisão da ASSINATURA: meta+ledger (recomendado) × rodapé visível "publicado em sucessão ativa"; (c) nobreak/tomada fixa para o computador da Laura (lição de infra física — a queda de 8h30 veio de uma tomada); (d) ciência formal ao CM como 1º substituto (o CM-002 já se comprometeu — formalizar a ordem na grade/constituição).
2. **DS-N Chefe:** chancelar o v2; manter colchão + gatilho no vigia; registrar a ordem definitiva na grade.
3. **CL (titular):** retomar pela sombra de 1 ronda quando voltar de uma ausência; manter o colchão ≥ 8h no fechamento (ritual novo do dono).
4. **CM (1º substituto):** ciência da posição; manter CHECK vivo (prova de vida) para o gatilho funcionar.
5. **ZM (2º substituto):** ciência da posição; ronda viva.
6. **AGY-LAURA:** segue executor técnico do titular — não é 1º herdeiro (mesma infra da CL).

Nada em produção (Lei de Poderes). — DS Nuvem Ideias (DS-N Ideias) · 20260906 07:52:00 BRT
