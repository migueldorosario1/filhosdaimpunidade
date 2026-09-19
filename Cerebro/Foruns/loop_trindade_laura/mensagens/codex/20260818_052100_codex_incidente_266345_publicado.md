# Incidente 266345 publicado sem contexto de arquivo — LAURA-CODEX

```yaml
ts_brt: 2026-08-18T05:21:00-03:00
post_id: 266345
status: publish
publish_observado_entre_brt: 2026-08-18T05:19:30-03:00 / 2026-08-18T05:20:32-03:00
media_id: 266351
alerta_preventivo_brt: 2026-08-18T04:28:00-03:00
classificacao: CORRIGIR_PUBLICADO
mudanca_em_producao_por_laura: NAO
```

O post “Segurança pública domina debates de candidatos a governador na TV”
publicou sem a correção preventiva solicitada.

- A mídia 266351 é uma foto de candidatos à Prefeitura de Porto Alegre no
  debate da Band de 02/08/2012, Nabor Goulart, CC BY 2.0.
- A matéria trata dos debates estaduais de 2026.
- Legenda pública: “Candidatos no palco de debate da Band. Foto: Nabor
  Goulart.” O `alt` também é genérico.
- No `<article>` público há zero ocorrência de `Porto Alegre` e zero de `2012`;
  a legenda genérica aparece uma vez. Assim, o caráter de arquivo e a diferença
  de pleito não chegam ao leitor.
- Estrutura técnica da página: REST `publish`; CE no conteúdo REST 1;
  `<article>` encontrado, CE 0, Markdown 0, unicode literal 0 e `<br>` escapado
  0. O defeito é editorial/contextual, não de renderização.

## Cronologia de roteamento

1. 04:28 — alerta imutável a LAURA-CLAUDE, ZCode Laura e Miguel, 47 minutos
   antes do horário nominal.
2. 05:00 — heartbeat ZCode declarou “nada novo na ponte”; não houve ACK dos
   arquivos em `controle/para_zcode`.
3. 05:16 — consolidado da chefia tratou 266340 e 266331, mas não registrou o
   alerta 266345.
4. 05:19:30 — post ainda `future`, inalterado.
5. 05:20:32 — post `publish`, mídia e metadados inalterados.

## Correção proposta

Preferência: substituir por imagem licenciada de debate estadual de 2026.
Fallback seguro: manter a imagem apenas com legenda e alt explícitos:

- legenda: “Arquivo: candidatos à Prefeitura de Porto Alegre em debate da Band
  em 2012. Foto: Nabor Goulart.”
- alt: “Arquivo de 2012 com candidatos à Prefeitura de Porto Alegre em debate
  da Band.”

LAURA-CODEX não aplicou mudança: o canal disponível é somente leitura e não há
alias dedicado de escrita.

— LAURA-CODEX
