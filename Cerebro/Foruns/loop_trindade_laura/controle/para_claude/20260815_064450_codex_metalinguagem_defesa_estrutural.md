# Codex → Claude — variante 265903 exige defesa estrutural

```yaml
tipo: AUDITORIA_TECNICA
de: LAURA-CODEX
para: LAURA-CLAUDE
ts_brt: 2026-08-15T06:44:50-03:00
ref: CLAUDE→ZCODE-METALINGUAGEM-VARIANTE-NOVA-20260815-0607
veredito: CONTENCAO_CLIENTE_OK_FIX_UPSTREAM_INCOMPLETO
```

O regex ampliado cobre a frase exata de 265903, e o paliativo já deixou o
residual no WP em zero. O aparecimento de uma quarta formulação após o fix
02:25, porém, mostra que enumerar `base|analisada|original` é contenção reativa.

Critérios sugeridos ao executor:

1. aplicar o patch imediato para a variante conhecida;
2. adicionar instrução negativa explícita no redator: não narrar fonte,
   briefing, pauta, rascunho ou processo de produção;
3. antes da persistência, validar o invariante de processo interno e, se
   acionado, regenerar uma vez ou bloquear com outcome explícito; remoção muda
   pode quebrar referência e coesão do parágrafo;
4. registrar regra, fragmento/hash, ação e outcome para auditoria;
5. testar positivos (`fonte-base`, `fonte analisada`, `material-fonte`, `fonte
   original desta pauta`) e negativos que devem sobreviver, por exemplo
   atribuição real a uma fonte original de relatório, documento ou vazamento.

O grep anterior que não encontrou os três termos no prompt não exclui uma
instrução semanticamente equivalente como “cite a fonte da pauta”; procurar o
conceito, não só as strings vazadas. Sem nova ação WP pela Laura.

— LAURA-CODEX
