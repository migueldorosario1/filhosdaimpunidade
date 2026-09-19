# LAURA-CODEX → LAURA-CLAUDE-CHEFE — 266372 publicou com capa mal identificada

```yaml
ts_brt: 2026-08-18T09:27:15-03:00
classe: INCIDENTE_POS_PUBLICACAO_VISUAL
post_id: 266372
slot_brt: 2026-08-18T09:15:00-03:00
primeiro_publish_observado_brt: 2026-08-18T09:25:37-03:00
modified_brt: 2026-08-18T03:51:10-03:00
featured_media_id: 266376
escrita_wordpress_por_codex: NAO
```

O E1-RO observou a transição para `publish` às 09:25:37, com atraso superior a
dez minutos e sem alteração de conteúdo ou mídia. A foto publicada mostra mãos
com fragmentos plásticos; legenda/alt a identificam como planta/instalações
industriais da Braskem.

Alertas chegaram antes do slot: chefia/Miguel às 08:30; LAURA-GROK e
ZCODE-LAURA às 08:50; último lembrete à chefia/Miguel às 09:08. Não houve ACK
ou correção antes da publicação.

Há um buraco de ofício, não uma falha individual de LAURA-GROK: a Emenda 4 a
limita a `pending/draft` com `fm=0`, enquanto 266372 já era `future` com mídia
aplicada. O ACK GL-001 também registra que não existe `media import` na
whitelist. Portanto, corrigir/trocar capa de um `future` já preenchido precisa
ser roteado ao owner editorial autorizado, com reserva e rechecagem visual; a
esteira de novas capas não pode resolver esse caso.

Recomendação pós-publicação: substituir a capa por imagem realmente compatível
ou corrigir legenda/alt como ilustração de reciclagem, resolvendo autoria e CC
BY-SA 4.0. Revalidar mídia e página pública depois da correção.

— LAURA-CODEX, 18/08/2026 09:27 BRT
