# FÓRUM — Tribunal Visual do Rio Carta + plano econômico (08/09/2026)

> Ordem do Miguel (08/09 ~22:3x, voz + link da matéria): "Tem que instalar juiz, juiz de
> imagem, tribunal de imagem… matéria sobre o Rio, foto do Aécio Neves de Minas Gerais.
> Corrige isso e monta isso para mim. Monta um plano de emergência para ter um tribunal
> visual no Rio Carta. Mas monta um plano econômico apenas, bota uma matéria por dia,
> porque não tem mais dinheiro para ficar pagando Rio Carta. Uma matéria por dia, mas
> pelo menos uma certa, bem escrita. A titulação está americana, com tudo maiúsculo,
> tem que consertar isso."
> Sessão: ZCode/Qwen 3.8 (Dell) executando no pipeline V4 do NYC.

## 1. O que estava errado (diagnóstico provado)

1. Matéria `20260908-eleicoes-2026-no-rj-dezesseis-candidatos-disputam-duas-vagas`
   (riocarta.com) no ar com hero = foto do AÉCIO NEVES (MG), adesivo "45" do PSDB no
   peito, crédito no frontmatter: `hero_credit: "Aécio Neves - Senador via Openverse (by)"`.
   A busca de imagem (Openverse) achou a foto pelo tema "senador"; o juiz visual único
   (Gemini, prompt calibrado p/ aprovar na dúvida) e a confirmação de 18/08 deixaram passar.
2. Título em TITLE CASE americano: "Eleições 2026 no RJ: Dezesseis Candidatos Disputam
   Duas Vagas no Senado Federal" — o prompt de produção não tinha nenhuma regra de
   caixa; LLM escreveu como manchete em inglês.
3. Cadência cara: Rio Carta publicava 3×/dia (cron `--all` 12:00 + extras 02:00 e 20:00).

## 2. O que foi feito (tudo testado)

1. FIX AO VIVO (22:5x): hero trocada p/ foto oficial do Congresso Nacional ao entardecer
   ("Fotos produzidas pelo Senado", Wikimedia Commons, CC BY 2.0 — sede do Senado, capa
   honesta p/ matéria de Senado); título e legenda em sentence case pt-BR; crédito novo
   explícito. Commit `180320f` no riocarta-v4 → Vercel no ar (md5 da hero viva = md5 da
   fonte; título vivo em sentence case).
2. TRIBUNAL VISUAL no NYC (`/root/tematicos/agentes_tematicos/v4/`), opt-in por site
   (`"tribunal_visual": true` no `agent_data/configs/riocarta.json`), hook no publicador
   ANTES do gate de confirmação de 18/08:
   - Camada 0 (CUSTO ZERO): `gate_credito_nomes()` — nome de PESSOA no crédito da foto
     que não aparece no título+corpo = REPROVA sem gastar visão (pega o caso Aécio pelo
     crédito; corta em " via ", ignora tokens de instituição/veículo: senado, congresso,
     youtube, wikimedia, fotos…).
   - Camada 1 (2 juízes): Gemini (cascata c/ proxy tencent) E Qwen-VL votam com prompt
     ESTRICTO de GEOGRAFIA/PESSOA (político identificável de outro estado = reprova;
     pessoa não nomeada no título = reprova; exceção explícita: conjunto institucional de
     Brasília é capa válida p/ matérias de Senado/Câmara/eleições de qualquer estado).
   - Camada 2 (desembargador): voto 1×1 → `confirmar_imagem()` (prompt estrito de 18/08)
     desempata. Sem visão disponível = FAIL-CLOSE (post adiado, nunca publica cego).
   - Custo: ≤2 chamadas de visão por hero (mesmo teto de antes: julgar+confirmar), só
     nos sites com tribunal ligado, 1 matéria/dia → centavos.
3. TITULAÇÃO pt-BR: regra no prompt de produção ("sentence case, title case americano é
   PROIBIDO") + gate determinístico `_sentence_case_ptbr()` no produtor: só age com ≥3
   capitalizadas no meio; preserva 1ª palavra, siglas e nomes próprios confirmados pelo
   CORPO (o próprio texto é o dicionário). Testes: título da matéria → sentence case
   exato; "Benedita Da Silva Lidera…" → "Benedita da Silva lidera… ao Senado no RJ";
   idempotente em título já correto.
4. PLANO ECONÔMICO: cron extra do riocarta (`0 2,20`) comentado com marcador
   `# ECONOMIA_RIOCARTA_1DIA_20260908` (backup `/tmp/crontab.bak_pre_economia_riocarta_20260908`
   no NYC). Rio Carta passa a 1 matéria/dia (slot `--all` 12:00), com tribunal + titulação.

## 3. Provas (testes de 08/09 ~23:0x no NYC)

- Gate de crédito: Aécio → `(False, 'crédito nomeia pessoa fora da matéria: Aecio Neves')`;
  crédito Congresso e crédito YouTube → `(True, '')`.
- Tribunal na foto do Aécio: reprovada NAS DUAS camadas (crédito; e só-visão 2×0 com
  crédito genérico).
- Tribunal na hero do Congresso: aprovada 2×0 ("Sede do Senado Federal" nos 2 juízes).
  (1ª rodada antes da calibração deu 2×0 REPROVA — juízes liam Brasília como "lugar
  errado"; a exceção institucional no prompt curou sem enfraquecer a regra de pessoa.)
- Página viva: título sentence case no `<title>` e `og:title`; md5 da hero servida =
  md5 do arquivo fonte.

## 4. Estado da missão

- PRONTO: fix ao vivo, tribunal instalado+testado, titulação curada, cron 1/dia, Cérebro
  atualizado (este fórum + memória + nodos BOLETIM_NEWS_RIOCARTA/BUGS_RESOLVIDOS/ATUALIZACOES).
- FALTA (opcional, aguarda "vai"): ligar `tribunal_visual` nos outros sites pt-BR
  (ceara, mapario — 1 linha de config cada); retrofit de titulação nos posts JÁ
  publicados com title case (varredura + `_sentence_case_ptbr` em lote); o juiz de TEXTO
  (auditoria) já existe e não foi mexido.
- PRECISO DE VOCÊ (Miguel): nada bloqueante. Se quiser o tribunal nos outros sites ou o
  retrofit dos títulos velhos, diga "vai".

## 5. Regra viva proposta (§ nova)

"Site temático não publica hero cujo crédito nomeie pessoa ausente da matéria; e título
pt-BR sai em sentence case — title case americano é defeito de tradução, não estilo."
