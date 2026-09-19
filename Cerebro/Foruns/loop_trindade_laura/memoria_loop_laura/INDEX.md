# Memória Loop Laura

Índice permanente das lições operacionais do chefe `LAURA-CLAUDE`.

Claude consulta este índice e o arquivo do dia no início de toda ronda. Cada
dia tem arquivo próprio; registros são append-only e preservam data/hora BRT.

## Arquivos diários

- [2026-09-02](2026-09-02.md) — retomada pós-reboot 13:0x; ordem Miguel 13:0x (checagem própria integral + análise R1/R2 na ponte).
- [2026-09-03](2026-09-03.md) — dia atual; regime noturno desde 00:00 (só :12); 2º texto do Fable (268728 Mendonça/Vorcaro) checado; fóruns V4.1 + títulos EMU-2 abertos (respostas até 09:12, ZM compila 10:00); carimbo de hora pelo shell (ERRO-2320)
- [2026-09-01](2026-09-01.md) — dia encerrado; gate do Bubbles verificado; Git travado pela tarefa ZM (cura 13:05); lição fetch-antes-de-status.
- [2026-08-31](2026-08-31.md) — dia encerrado; LICAO-1112 (retomada pós-reboot), QUASE-ERRO-1412 e ERRO-1542 (fetch≠blocos), LICAO-2020 (autocura em vez de escalar), LICAO-2125 (canal SSH já existia), OBS-2315 (Bubbles desativado); lições 17-19.
- [2026-08-30](2026-08-30.md) — dia encerrado; ERRO-1245 (autoria sem prova), LICAO-2342 (agulha sem prova).
- [2026-08-20](2026-08-20.md) — dia encerrado; ERRO-0125, lacunas 4h36/7h31, ERRO-2033 (aprovação parcial), marco do teste de chefia.
- [2026-08-18](2026-08-18.md) — dia encerrado; ERRO-0006/0034 (hora), ERRO-0228 (roteamento), ERRO-1303/1752 (grade), lições 12-14.
- [2026-08-17](2026-08-17.md) — dia encerrado; ERRO-0148, ERRO-0933, FEEDBACK-1055, ERRO-1717, ERRO-2052.
- [2026-08-16](2026-08-16.md) — dia encerrado.
- [2026-08-15](2026-08-15.md) — início da memória; 8 registros; família "proxy no lugar do resultado real" fechada por formatos.

## Regras permanentes já aprendidas

1. “Loop ativo” não significa “loop persistente”: confirmar o scheduler após
   retomada, troca ou encerramento de sessão.
2. Não esconder falha com atividade posterior. Registrar incidente, correção e
   verificação separadamente.
3. Sem causa comprovada, escrever `CAUSA_EM_INVESTIGACAO`.
4. O diário registra erros do chefe e lições de coordenação, não culpa dos
   outros agentes.
5. **Cultura de autoaprendizado (ordem direta de Miguel, 15/08 13:00):**
   todo erro percorre 5 fases — registrar no mesmo ciclo (diário
   append-only), indexar (lição durável quando genérica), transformar em
   diretriz que muda o formato/procedimento (não só "prestar atenção"),
   ler antes de todo ciclo, e ensinar — o chefe cobra o mesmo ciclo de
   Codex e Grok nos consolidados, tratando erro bem registrado como
   mérito, nunca como culpa.
6. **Fonte verdadeira ≠ fato confirmado (ERRO-0148, 17/08):** em evento
   multifásico, a unidade factual é `evento + edição + etapa + datas +
   universo contado`. "Confirma" exige a ficha factual da diretriz de
   eventos; recorte implícito é onde a etapa errada se esconde.
7. **Dado de calendário se mede, não se lembra (ERRO-0933, 17/08):**
   dia da semana/feriado só entra em relatório vindo de `date` impresso
   na ronda; qualificar normalidade por calendário sem artefato = não
   verificado.
8. **Delta se mede do checkpoint anterior, não do próprio push
   (ERRO-1717, 17/08):** `git diff head_lido_anterior..HEAD`; pull fora
   de ronda mascara trabalho alheio. Antes de declarar silêncio de um
   ofício, listar o diretório dele por data — ausência no diff não é
   ausência de trabalho, e suspeita sobre colega exige artefato.
9. **Presença se prova por artefato que envelhece (ERRO-2052, 17/08):**
   recorrência presa à sessão do CLI cai em silêncio. Cada ofício mantém
   heartbeat próprio (chefe: `controle/heartbeat_chefe.txt`) reescrito a
   cada ronda com hora BRT, ciclo e HEAD; heartbeat com mais de 40 min é
   evidência pública de queda. Toda ronda abre com `varredura_de_presenca`
   e, na retomada após queda, mede e publica o tamanho do apagão antes de
   qualquer trabalho editorial.
10. **Declarar depois de conferir (ERRO-2052, 17/08):** nenhuma ação entra
    no relatório como concluída sem o artefato conferido no mesmo comando.
    "Consolidado publicado" só se escreve depois do `ls` que mostra o
    arquivo.
11. **Presença é por canal, e canal novo entra na varredura na hora
    (ERRO-2348, 17/08):** medir só o canal antigo e chamar de silêncio é
    proxy no lugar do fato. A varredura enumera todos os canais em que o
    ofício pode escrever (diretório próprio, commits, ponte completa:
    `de_laura.md`, `estado/`, `ledger/`) e o veredito nomeia o canal
    ausente — "sem ronda no Loop Laura" nunca vira "sem sinal de vida".

## Gates das lições (PD-2 — aprovado por Miguel em 18/08/2026 ~01:25)

Regra: **toda lição nasce com um gate** — um comando ou campo obrigatório que
falha visivelmente quando a lição é violada. Lição sem gate vale 7 dias e é
reavaliada. Começo pelas que já tiveram **reincidência**, não pelas mais
bonitas.

| lição | gate | como falha |
|---|---|---|
| 7 + ERRO-0006/0034 (hora medida, não lembrada) | toda hora em artefato vem de variável capturada por `date` **no mesmo comando** que grava o arquivo, inclusive no nome | `grep -nE "[0-9]{2}:[0-9]{2}"` no artefato tem que bater com a saída de `date` da ronda; hora literal digitada = falha de forma, corrigir antes do commit |
| 11 + ERRO-2348 (presença é por canal) | o YAML da ronda só é válido com `canais_varridos:` preenchido com os três canais (diretório do ofício, commits, ponte completa) | ronda sem o campo = ronda inválida; veredito de silêncio sem o campo não pode ser publicado |
| 9 (heartbeat) | `heartbeat_chefe.txt` reescrito toda ronda com hora BRT, ciclo, HEAD e `ultima_acao_material`; limiar **45 min** (1,5 × ciclo de 30, Regra 7) | arquivo com mais de 45 min = evidência pública de queda, auditável por qualquer agente sem depender do meu relato |
| 10 (declarar depois de conferir) | nenhuma ação entra no relatório sem `ls`/`cat` do artefato no mesmo comando | declaração sem o artefato conferido = errata obrigatória |

As demais lições (1-6, 8) recebem gate nas próximas rondas; a que não
admitir gate desce para nota de diário, conforme a regra aprovada.

_Registrado em 18/08/2026 01:39 BRT por LAURA-CLAUDE._

12. **Correção minha aplicada por terceiro se reconfere (18/08):** o texto
    que proponho pode criar defeito novo no contexto em que entra — foi o
    caso da repetição no 266340. Gate: toda correção minha aplicada por
    outro agente é relida por mim na ronda seguinte, no artefato publicado,
    e o resultado (OK ou defeito novo) entra no consolidado.

13. **Presença do chefe não depende do tipo de turno (ERRO-1303, 18/08):**
    trabalho por demanda não substitui ronda, e turno de conversa também
    consome a janela. Gate: conferir idade do próprio heartbeat no início de
    **todo** turno e rearmar a recorrência no fim de **todo** turno.

14. **Fila de agendamento é sinal vital, e ausência dela não gera atraso
    (18/08):** produção manual mascara fila zerada — não há "atraso" quando
    não há agendamento. Gate: contar `future` em toda ronda e alertar
    quando a fila cobrir menos de 2 horas; `pending` alto com `future`
    zero é sintoma, não conforto.

15. **Atividade se mede por mtime, não por grep (ERRO-0125, 20/08):** "nada
    novo" só pode ser dito depois de varrer a árvore por data de modificação.
    Grep encontra assunto; mtime encontra trabalho. Metade do ecossistema não
    passa pelo arquivo que eu leio por hábito.

16. **Aprovação parcial não é aprovação (266837, 20/08):** checar 4 de 10
    itens e carimbar "aprovado" é o erro mais perigoso da chefia — parece
    rigor e autoriza defeito. Gate: ordem de publicação só existe com o
    CHECKLIST_PRE_PUBLISH_v1 completo anexado; sem os 10 itens, o executor
    nega por forma.

17. **Autocura antes de escalar (ordem Miguel 31/08 ~20:15, "foco em autocura,
    autoaprendizado e solução"):** defeito diagnosticado + fix conhecido + arquivo
    nesta máquina + reversível = EXECUTAR (backup com SHA, rollback declarado,
    teste na ronda seguinte) e relatar. Escalar só o que exige credencial ou
    servidor que não tenho. Todo bloco de escalada responde antes: "isto está ao
    meu alcance?". Caso: lock estreito portado ao agy_ronda.ps1 (CL-035).

18. **Aprovação sem porta de entrada do executor não produz nada (31/08):** ao
    assumir papel novo numa lei (olho humano da caça, Lei v2), confirmar no mesmo
    ato por onde o executor recebe o resultado; se a porta não existe, nomeá-la
    antes de produzir. Caso: 4 capas aprovadas (CL-032/033) e o worker às 20:00
    ainda "sem capa".

19. **"Não tenho como" só com a lista de canais testados (31/08):** antes de
    declarar limite, testar os hosts do `~/.ssh/config` com prova negativa
    (alvo 999999999 → `post_not_available` valida verbo sem efeito colateral).
    Caso: `cafezinho-wp-write` tinha `media-import`+`set-media` o dia todo; as
    4 capas saíram em 3 min quando testei. Memória de sessão anterior
    ("bloqueado", "sem DNS") não é fato permanente.

- **2026-09-04** — `2026-09-04.md`: regime noturno desde 00:12; herança de 03/09 no cabeçalho (guarda da trava, diff de IDs, vaga com segundos, recusa = pauta, despertar sempre, canal comido); pendências: pauta Gonet (05:25/07:25), 268885, 268909, 268862, TSE.
- **2026-09-05** — `2026-09-05.md`: sábado: herança de 04/09 (AGY parado, cl153 pela CL, decisões 23:27, feijão/painel, runtime V4.1); regime noturno até 07:12
