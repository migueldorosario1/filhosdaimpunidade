# Memória — Revisão editorial final do artigo "Mais forte que em 2022" (26/08/2026)

## Arquivos tocados

- **EDITADO:** `Outros/pautas editoriais o cafezinho/Dia a dia/2026 Ago 26/analise geral pesquisas/artigo_mais_forte_que_em_2022.md` (7 edições pontuais; título e estrutura preservados).
- **LIDOS (base de validação):** `analise_lula_2026_vs_2022_completa_2026-08-26.csv` (38 linhas: 27 UFs + 2 BR), `analise_lula_2026_vs_2022_texto_completo_2026-08-26.txt`, monitoramento, fórum de pesquisas eleitorais 24-25/08.
- **Integridade:** foto `foto_lula_flickr_jornalistica.jpg` (Stuckert/Flickr 25/08) + 4 gráficos com os nomes exatos citados no markdown — conferidos por `ls`.

## Validações mecânicas executadas

1. **Régua de 2 frases:** script Python contou frases por parágrafo (split em `(?<=[.!?])\s+`, ignorando títulos/legendas) → **38/38 parágrafos com exatamente 2 frases** (era 38/38 antes das edições e 38/38 depois).
2. **Título:** `# Mais forte que em 2022`, sem dois pontos e sem subtítulo. ✅
3. **Conferência 1-a-1 artigo × CSV** (pesquisa principal por UF): quadro nacional (39×33 Datafolha, 41×37 Nexus, 46×45 2ºT), 61,9–65,1 mi vs 57,3 mi 2022 (+4,65 a +7,83 mi), CE 32,3→44,0 (+970.666), BA 60×17 (+9,1 p.p., +919.522), SE +10,1 / RN +8,9, MA +5,9 + PE +4,5 (~892 mil), SP −5,0→−1,0 (Lula −1,24 / Flávio −5,29), RJ −7,7→−2,0 (Flávio −6,67), ES 30×30 (−9,0 eliminada; Flávio −9,69), MG Datafolha 37×31 × Quaest 31×30 (Δ7 p.p.), PR Lula −4,87.

## Erros encontrados e corrigidos (com prova no CSV)

| # | Antes | Depois | Prova no CSV |
|---|-------|--------|--------------|
| 1 | "18 dos 26 estados" | "19 dos 27 estados" | 19 UFs com `delta_lula_n > 0` (principais), 8 negativas |
| 2 | "seis ampliações N/NE" | "sete" | top 10 Δmargem: CE, GO, SE, BA, ES, RN, **RO +5,98**, MA, RJ, PE → 7 do N/NE |
| 3 | PR "perda clara de participação" | "piora clara de margem" | RS deltaL −4,68 ≈ PR −4,87; quem distingue o PR é Δmargem −3,08 |
| 4 | SC "maior margem da oposição" | "+ em todo o Sul" | AC −26,3 e RR −53,3 superam SC −25,0 no nacional |
| 5 | PA "sondagens presenciais" | "outras sondagens… disputa equilibrada, +326 mil" | TXT de apoio: AtlasIntel digital; ΔN PA +326 mil |
| 6 | "evolui em 12 das 15" (2ºT) | "melhora em 11 e fica estável em 2" | lista do TXT: 11 positivas + Nexus −0,4 e RS-RT −0,2 estáveis + GO/PA piores = 15 |
| 7 | Nexus "exatamente a distância" | "praticamente a mesma distância" | margem Nexus +4,0 hoje vs +3,95 em 2022-1T |

## Estado final

- Artigo pronto para publicação (revisão pedida concluída; a publicação em si não foi pedida nesta sessão).
- Pendência do Miguel: OK final / ordem de publicar.
- Fórum: `Foruns/forum_artigo_mais_forte_que_em_2022_revisao_final_20260826.md`.

🕐 26/08/2026 · ZCode/GLM-5.3

---

## ADENDO 26/08 ~16:25 — V2 (gráficos melhorados + reescrita + fact-check 48/48)

- **Gráficos v2** (`gerar_graficos_analise_v2.py`): G2 com legenda fora da área (a v1 escondia o rótulo 39,7% do ES) + anotações Δ por estado; G1 colorido por região (7/10 N/NE); G3 com asterisco no PA (Veritá voz automatizada) + RN por extenso; todos com vírgula decimal pt-BR. Conferidos visualmente por leitura de imagem após geração (1ª rodada: anotações Δ do G2 colidiam — corrigidas para 2 linhas por grupo e regeradas).
- **Artigo v2** (`artigo_mais_forte_que_em_2022_v2.md`): reescrito; 31/31 parágrafos com exatamente 2 frases (script); título intacto; referencia os 4 gráficos v2.
- **Fact-checking programático**: 48/48 números do v2 conferem com o CSV (inclui contagens 19/27 estados e 7/10 N/NE, SC maior do Sul, diferença SP 1,7 mi→341 mil, GO/RR datadas). Não verificável: "43 mil entrevistados" (briefing do editor; sem coluna de amostra).
- v1 preservada (artigo + 4 gráficos + script). Estado: aguarda OK do Miguel p/ publicar.

🕐 26/08/2026 16:25 · ZCode/DeepSeek
