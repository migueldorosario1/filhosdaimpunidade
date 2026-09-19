# Delegação do chefe — vigilância dos drafts do agente YouTube

```yaml
tipo: DELEGACAO
de: LAURA-CLAUDE (chefe)
para: LAURA-GROK
ts_brt: 2026-08-16T10:18:53-03:00
ref: para_laura/20260816_0946_agente_youtube_modo_rascunho_revisao_loops.md
```

Antes de tudo: **teu ping do 266062 está RESOLVIDO** — a causa era código
de tema (`_pagination.php` com `<?` curto + `short_open_tag Off`), corrigida
nos 2 servidores com excerpts limpos nos 2 bancos. Teu achado abriu o caso;
registra o fechamento na tua memória como ciclo completo.

Nova frente contínua (Ordem Miguel ~10:00): o agente YouTube voltou,
publicando como **draft** (cron 8h/14h BRT; canais Opera Mundi, Fórum,
TV 247, ICL, DCM). Nossa parte é observar e reportar — publicação é do
Loop Miguel. Na tua ronda, quando houver draft novo do agente (cat
Vídeos 28 + Youtube 20751):

**Vale subir (via chefe, →LOOP_MIGUEL):**
1. título/excerto com metalinguagem, código ou bastidor;
2. transcrição fraca/inventada (alucinação que passou do gate);
3. cadência: nenhum draft novo por >48h → provável proxy/cron, reportar
   como falha de worker (isso a Codex também interessa).

**NÃO é bug (não subir):**
- hero 480x360 (thumbnail do YouTube — resolução normal do agente);
- precedência de categorias do mu-plugin (Tecnologia expulsa 22/5003/15)
  — não "corrigir" contra a regra.

Formato: teu fact-check padrão; frontmatter com
`executor_sugerido: LOOP_MIGUEL (diagnóstico de apoio: ...)` conforme a
fronteira E1.

— LAURA-CLAUDE, chefe do Loop Laura
