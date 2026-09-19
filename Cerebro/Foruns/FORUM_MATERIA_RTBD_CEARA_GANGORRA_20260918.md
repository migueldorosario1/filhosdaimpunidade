# 📰 FÓRUM — Matéria Real Time Big Data Ceará (gangorra Elmano×Ciro) — 18/09/2026

**Sessão:** ZCode/Kimi K3 (Dell, ZCodeProject) · **Monitor:** ZM-MATERIA-CE-RTBD-20260918
**Ordem do Miguel (18/09 ~08:4x):** matéria sobre a pesquisa Real Time Big Data mostrando Elmano à frente de Ciro; gangorra com Paraná/Datafolha; custo no TSE; PDF original para download; foto jornalística Elmano+Lula; publicar como RASCUNHO (§137) em Regional/Nordeste/Ceará. Pasta de trabalho: `Outros/pautas editoriais o cafezinho/Dia a dia/2026 Set 18/Real Time Ceara/` (PDF + 4 gráficos + CSV feitos por outra IA + HTML final).

## ✅ O QUE ACONTECEU / ESTÁ PRONTO

**RASCUNHO WP 271920** — "Gangorra no Ceará: Real Time Big Data mostra Elmano à frente de Ciro no 1º e no 2º turno" — status `draft`, autor 5470 (Redação), slug `gangorra-no-ceara-real-time-big-data-mostra-elmano-a-frente-de-ciro`, 760 palavras.
- Categorias: Regional (4986), Nordeste (4984), Ceará (4968), Eleições 2026 (5088), Redação (2403).
- Tags: Elmano de Freitas, Ciro Gomes, Ceará, Eleições 2026, pesquisa eleitoral, Real Time Big Data, Senado, Cid Gomes.
- Capa (featured 271911): Lula+Elmano+Riedel+Mercadante no Planalto 26/09/2024, foto Ricardo Stuckert/Lula Oficial, **CC BY-SA 2.0 via Wikimedia Commons** (1920px). Foto real, jornalística, todos sorrindo/joinha.
- 4 gráficos do Miguel embutidos (271912 espontânea, 271913 1º turno, 271914 2º turno, 271915 aprovação).
- Botão final verde #2d5a3d: "📥 Baixe aqui a íntegra da pesquisa (PDF)" → PDF original 271910 (`/wp-content/uploads/2026/09/ceara-ce-04380-2026-set26.pdf`).
- Link interno à matéria da Paraná (271877, publicada hoje 06:26).

**Números no texto (conferidos no PDF oficial):** 1º turno Elmano 47×42 (Huggo 2, Vera Lúcia 1); 2º turno 48×45 (empate técnico, margem ±2); rejeição Ciro 44×Elmano 41; aprovação binária 59×39 (ótimo/bom 40, regular 36, ruim/péssimo 22); espontânea Elmano 28×24 com 40% NS/NR; Senado Cid 26, Wagner 20, Luizianne 20, Alcides 19, Theophilo 4; recortes (Ciro: homens 47×43, 60+ 48×41, +5SM 53×29; Elmano: mulheres 50×37, até 2SM 52×40, 35-59a 50×41).

**Custo (dado que o Miguel colou do sistema TSE):** R$ 20.000,00, contratante Rádio e Televisão Record S.A.; R$ 12,50 por entrevista (1.600); registro CE-04380/2026 em 12/09, divulgação 18/09; estatística Isabela Zara Cremoneze (CONRE 10839); metodologia mista humanos+IA, telefone+digital.

**Gangorra mapeada:** Paraná Pesquisas (madrugada de hoje, CE-04259/2026, DON7 Media, 1.352 entrev.): Ciro 47,4×39,9 e 50,4×42,4 → matéria 271877. RTBD anterior (08/09): empate 46×43. Veritá (11/09): 0,2 ponto. **Datafolha (O POVO, 1.204 entrev., 14-17/09, CE-01290/2026) sai hoje à tarde** — anterior: Ciro 46×37, vantagem caiu 19→9 pontos. Atlas/Focus (1.800, campo até 20/09) sai segunda 21/09.

## 🔧 LIÇÕES TÉCNICAS

- Sistema de pesquisas do TSE = `https://pesqele-divulgacao.tse.jus.br/app/pesquisa/listar.xhtml` (linkado por `www.tse.jus.br/eleicoes/pesquisa-eleitorais/consulta-as-pesquisas-registradas`). WAF Akamai: **WebFetch 403 e IAB (navegador embutido) recebe HTML vazio; curl com UA de browser passa (200, ~684KB)**, mas o POST JSF (busca por número) não retornou resultados nas 2 tentativas (ajax e full submit). Detalhe de registro (valor, contratante) fica na tela "Visualizar" — desta vez o Miguel colou manualmente.
- Openverse API (`api.openverse.org/v1/images/?q=...&source=flickr`) acha fotos do **Flickr oficial do Lula (user 157736962@N05)** e republicações CC BY-SA no Commons — caminho sem chave quando a busca do Flickr bloqueia robô.
- Fluxo WP usado: scp para /tmp + `wp media import` (PDF+JPG+PNG ok) + `wp post create <arquivo.html>` (lê conteúdo do arquivo) + `wp post term set` + `wp post meta set _thumbnail_id`. Tudo com `--allow-root` (sem ele, wp-cli falha em silêncio neste servidor, stderr suprimido). Docroot: `/var/www/ocafezinho` (nginx; fastcgi 9083). Post 271877 usou autor 5780; segui a regra §137 com 5470 (Redação).

## ⏭️ O QUE FALTA / O QUE PRECISO DE VOCÊ (MIGUEL)

1. **Revisar e mandar publicar** o rascunho 271920 (§137: quem publica é o Chefe de Publicação; se quiser que eu publique por ordem expressa, diga).
2. **Valor declarado da Paraná (CE-04259/2026)** não consegui (JSF travou); se quiser a comparação R$/entrevista das duas no texto, cole o valor da tela de Visualizar que eu insiro.
3. Quando o **Datafolha** sair (tarde), posso atualizar o post ou fazer matéria separada, conforme o resultado.
4. O 1º turno nacional da Real Time (BR-03822/2026) não foi tratado (escopo = Ceará).

**Preview (logado):** https://www.ocafezinho.com/?p=271920&preview=true

## ✅ ADENDO (18/09 10:16) — PUBLICADO

- O Miguel publicou o post às **09:55** (post_date) pelo wp-admin. URL no ar: https://www.ocafezinho.com/2026/09/18/gangorra-no-ceara-real-time-big-data-mostra-elmano-a-frente-de-ciro/
- Adendo editorial do Miguel (~10:1x): Datafolha CE sai **hoje ~16h30**, primeiro em **live d'O POVO** e depois no portal; arco reforçado (1º Datafolha: Ciro +19; 2º: +9, 46×37). Texto atualizado no rascunho→publicado via `wp post update` (post_modified 10:15:32).
- Cache: página pública não refletiu o update até rodar `rocket_clean_post(271920)` + `rocket_clean_home()` + `opcache_reset()` — prova pública pós-limpeza: "16h30" e botão PDF presentes (HTTP 200).
- Lição: editar post recém-publicado exige limpeza Rocket/opcache na sequência (padrão já conhecido na troca de capa).
