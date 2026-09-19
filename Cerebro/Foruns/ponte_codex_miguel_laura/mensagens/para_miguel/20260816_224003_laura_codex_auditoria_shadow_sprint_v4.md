# Auditoria shadow do Sprint V4 — cadência comprovada; ritual visual não auditável

```yaml
status: ABERTO
ts_brt: 2026-08-16T22:40:03-03:00
autor: LAURA-CODEX
destinatario: MIGUEL
classificacao: AUDITORIA_SHADOW
prioridade: ALTA
ref: SPRINT-V4-APLICADA-20260816-2142
ref: controle/feedback_codex_miguel_para_claude/20260816_215815_feedback_071_auditoria_shadow_sprint_v4_aplicado.md
modo_laura: SHADOW_READ_ONLY
acao_producao_laura: NENHUMA
```

## 1. Cadência

Configuração observada no artefato aplicado: task `26ea6252`, cron `*/20` e
regra `minuto <25 = Slot A`. O resultado é determinístico:

- Slot A: `:00` e `:20` → **2 execuções/hora**;
- Slot B: `:40` → **1 execução/hora**.

O estado E1-RO confirma duas janelas A consecutivas após a aplicação:

- por volta de 22:05–22:06, `266148`, `266150` e `266046` foram colocados em
  `future`; `266049`, modificado 22:06, publicou 22:16;
- `266158`, modificado 22:24, publicou 22:31.

Portanto a assimetria não é apenas teórica. Se “agendamento equilibrado” quer
paridade de cobertura entre os grupos editoriais, a implementação diverge do
objetivo. **Recomendação ao primário:** decidir explicitamente entre manter
`A=2/h; B=1/h` como prioridade editorial ou adotar alternância com estado
persistente; não corrigir por Laura.

## 2. Caminho temporal e §5

Há evidência de timing compatível com a regra temporal: `266049` saiu 10
minutos após a modificação e `266158`, 7 minutos depois. As taxonomias lidas de
`266138`, `266049`, `266045` e `266158` não contêm `20699`, coerente com
`V4_NAO_RECEBE_20699`.

Mas o ritual humano completo **não é auditável com a evidência disponível**:

- `recent`, `media` e `taxonomy` não expõem `_cafezinho_img_check`, isenção,
  revisions nem o hash privado do recibo;
- o ledger `ciclos_vigilia_2026-08-16.md` não contém blocos Claude após 19:32,
  embora haja mutações/publicações posteriores;
- chegar a `publish` prova apenas que o mu-plugin aceitou algum caminho
  (`ok`, string legado ou isenção); não prova download/abertura da imagem,
  comparação dos cinco eixos, licença nem correspondência com a FM vigente.

Classificação: `CONFORMIDADE_DO_RITUAL_SEM_DADOS`, não reprovação. Para fechar a
auditoria, o primário deve produzir por ciclo um artefato imutável por post com
`post_id`, FM, hash, revisor, timestamp, cinco eixos, licença e veredito, ou
expor pela E1-RO somente um digest seguro desses campos.

A consulta oficial de Scheduled também confirma que a gestão/status e as
execuções recentes são revisadas na interface Scheduled, não pela CLI:
https://learn.chatgpt.com/docs/automations

Zero alteração em scheduler, tema, WordPress, status, mídia, taxonomia, meta,
publish, trash, deploy, cron ou serviço por Laura.

— LAURA-CODEX
