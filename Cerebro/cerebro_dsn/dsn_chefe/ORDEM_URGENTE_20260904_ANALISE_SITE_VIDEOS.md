# 🔴 ORDEM URGENTE — Análise geral do site + vídeos + conferência de títulos/posts das últimas horas

**De:** Miguel (ordem 04/09/2026 ~18:2x) · **Passada por:** ZCode/GLM-5.3 (Dell) · **Status:** 🔴 URGENTE — assumir na 1ª ronda
**Contexto:** o Miguel desligou o Dell — o ZM fica OFFLINE até ele voltar. Você (na Tencent) assume esta missão AGORA.

## A missão (3 frentes)

1. **Análise geral do site** www.ocafezinho.com sob a ótica do bom senso: home, blocos por editoria, posts recentes, capas, categorias, títulos.
2. **SOBRETUDO VÍDEOS:** as matérias de vídeo publicadas HOJE pelo agente YouTube (autor WP 5801 — posts 269033 a 269044, cats 28/20751): conferir se o vídeo está embutido e toca, capa presente, categoria certa, título conforme a régua. Conferir também o carrossel de vídeos do espelho cafezinho.news (mu-plugin v0.4.1) e a categoria Vídeos do canônico.
3. **Conferir TODOS os títulos e posts das últimas horas** e dizer se está tudo bem feito.

## Achados que o ZM já apurou (18:2x — valide e profunde)

- **🔴 269033 e 269034 são DUPLICADOS** (mesmo título «Feijão-carioca volta a subir no fim de agosto com produtores segurando venda, aponta Cepea», autor 5801, 17:35) e os dois estão **SEM categoria E SEM capa** (featured_media=0) — invisíveis nos blocos da home. A sessão YouTube que os publicou ficou interrompida; dedup + cats + capa pendentes.
- **🟠 Títulos acima dos 80 caracteres (regra 1) nas últimas horas:** 269044 (102c) · 269042 (101c) · 269040 (101c) · 269038 (92c) · 269033/34 (90c) · 269050 (93c, autor 5786) · 269021 (105c, autor 5786) · 269002 (86c, autor 5780) · 268999 (92c, tem ":" E "—", autor 5780) · 268976 (95c, tem ":", autor 5470).
- **🟠 Pauta do feijão-carioca QUASE TRIPLICADA hoje** (Cepea): 269033+269034 (duplicados) e 269050 (16:20, autor 5786, outra redação) — decidir sobreposição.
- **🟢 Hoje o auditor de títulos (NYC) já roda com a régua de 9 regras (EMU-8) para os autores 5786, 5470 e 5801** — as sugestões de reescrita dos 6 posts 5801 já estão prontas em `/root/agent_data/auditor_titulos_gpt/advisor_pending_5801.jsonl` (nyc) e `advisor_pending_5470.jsonl`. USE essas sugestões como insumo.

## Régua e limites

- Régua de título = `cerebro/Estilo/MANUAL_DE_ESCRITA_PORTAL.md` + emendas EMU-1 a EMU-9 (EMU-8 de hoje: nome próprio desconhecido não entra no título — entra o genérico; caso-escola 268998 «Janmashtami celebra Krishna…» → «Festa hindu celebra nascimento de divindade…», já corrigido).
- **Regra-mãe preservada:** NUNCA publicar/editar produção do WordPress sem ordem explícita do Miguel — EXCETO correção de título in place preservando slug, prática já endossada pela casa nos casos 268482/268457/268998/269012/269007. Na dúvida, REPORTAR sem editar. Duplicata 269033/34: se for apagar um dos dois, prefira pedir/despublicar para draft (reversível) em vez de deletar.
- QA visual: prints via chrome headless se precisar (IAB do ZCode falha para screenshot; o seu caminho é o que tiver na Tencent).

## Reporte

1. Telegram do Miguel (assinatura completa, SEM asteriscos/markdown) — ele está no celular, o Telegram é o canal.
2. Fórum: `cerebro/Foruns/forum_analise_site_videos_20260904.md` (crie) com o relatório completo + Tema Duplo (memória em `cerebro/Memorias/`).
3. Monitor de trabalho: sua linha no `cerebro/MONITORAMENTO_DE_TRABALHO.md`.

**O que aconteceu / o que falta / o que preciso de você:** origem = queixa de título do 268998 (corrigido + EMU-8 estrutural no ar); falta = esta análise ampada; preciso de você = assumir e reportar ao Miguel no Telegram.
