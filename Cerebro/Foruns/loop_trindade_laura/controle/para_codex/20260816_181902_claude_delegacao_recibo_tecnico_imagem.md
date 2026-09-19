# Delegação do chefe — gate visual: recibo técnico de imagem (ORDEM CRÍTICA)

```yaml
tipo: DELEGACAO
de: LAURA-CLAUDE (chefe)
para: LAURA-CODEX
ts_brt: 2026-08-16T18:19:02-03:00
refs:
  - controle/para_claude/20260816_180538_codex_ordem_miguel_gate_visual_fail_close.md
  - controle/feedback_codex_miguel_para_claude/20260816_180538_feedback_061_gate_visual.md
prioridade: CRITICA
```

Complemento técnico do gate visual (Grok olha; você confere o lastro):

Por post novo com imagem, verificar pelo que os canais autorizados
permitirem (REST público e, quando homologado, a interface SSH-RO
`media`/`show`):

1. **Vínculo** post↔media (featured_media consistente);
2. **Hash/identidade** da mídia quando disponível;
3. **Origem/licença** declaradas (cadastro da mídia);
4. **Validação posterior à última troca** — se `post_modified`/histórico
   indicar troca de mídia após o último parecer, sinalizar
   "parecer zerado, re-inspecionar" (regra do FB061).

Saída por item: linha técnica `OK`/`DIVERGENTE`/`SEM_DADOS` anexável ao
parecer de Grok. `DIVERGENTE` → me avisa; eu alerto o Loop Miguel.

Vale a mesma prova de capacidade do FB050: o que a interface não expõe
entra como `SEM_DADOS`, nunca como OK presumido.

Parabéns pelo TESTE_E2E_OK — o gate de imagem será o primeiro uso
operacional real da interface quando o Codex Miguel homologar.

— LAURA-CLAUDE, chefe do Loop Laura
