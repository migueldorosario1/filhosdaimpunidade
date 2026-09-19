# 🎓 AULA 01 — Como o Google paga o Cafezinho: o leilão, o RPM e os cliques

> Série de publicidade do DS-N Pub para o **Miguel e o Gabriel**. Do zero, sem tecniquês, com os números DA CASA. Uma aula por semana (ou no ritmo que o Miguel pedir). Perguntas respondem-se na ponte; dúvida boa vira aula.

## 1. O que acontece em 1 segundo quando um leitor abre uma matéria

1. A página carrega e o navegador **desenha os espaços de anúncio** (os "slots" — no Cafezinho eles têm nomes como `CafeMobile-1` no AMP).
2. Cada espaço vai a **leilão**: dezenas de anunciantes fazem lances em milissegundos ("eu pago R$ X pra aparecer pra este leitor, nesta página, agora").
3. Quem paga mais aparece. Se ninguém liga, aparece o anúncio de menor preço — ou nada (**espaço sem lance = dinheiro zero**; é por isso que slot vazio, como os 18 do non-AMP, é prejuízo silencioso).
4. O Google cobre do anunciante e reparte com a gente.

**Quem manda no preço do leilão:** (a) quantos anunciantes querem aquele leitor; (b) quanto a página é "confiável" pro anunciante (contexto, tema, histórico); (c) o formato (tela cheia vale mais que tirinha). Nós controlamos o estoque (audiência + páginas + formatos); o leilão controla o preço.

## 2. As 4 palavras que pagam a conta (decorem só estas)

| Palavra | O que é | Fórmula |
|---|---|---|
| **Impressão** | 1 anúncio APARECENDO 1 vez (não é venda; é a "vitrine") | — |
| **Clique** | leitor clicou no anúncio | — |
| **CTR** | cliques ÷ impressões | "de cada 100 anúncios vistos, quantos viraram clique" (portal BR típico: 0,5% a 2%) |
| **RPM** | **receita por MIL impressões** | receita ÷ impressões × 1.000 |

**O RPM é o termômetro da casa.** Quando o relatório de 2h começar a trazer o RPM real (Fase 2), toda decisão ganha número: trocar posição de anúncio, post novo, formato novo — sobe o RPM = certo; desce = volta atrás.

CPC (custo por clique) e CPM (custo por mil impressões) são a linguagem do ANUNCIANTE — mesmo leilão, lado de lá do balcão.

## 3. Traduzindo para o bolso do Cafezinho (conta de guardanapo)

A casa fez ontem (31/08) **50.201 navegações**. Suponha ~3 anúncios visíveis por navegação (estoque típico AMP):

- Estoque do dia ≈ **150 mil impressões**.
- Se o RPM médio for R$ 2 → **R$ 300/dia**. R$ 6 → R$ 900/dia. R$ 15 → R$ 2.250/dia.
- Os mesmos 50 mil leitores rendem 7× mais ou 7× menos **só em função do RPM** — e o RPM muda com posição do anúncio, velocidade da página, tema da matéria, hora do dia e país do leitor.

**Por isso o robô existe:** o RPM não é fixo, ele RESPIRA a cada 2 horas — e a casa nunca o acompanhou de perto. (Os números acima são exemplo didático; o RPM REAL chega na Fase 2.)

## 4. O mapa do Cafezinho (onde os anúncios moram hoje)

- **AMP (~64% das views):** 15 slots GAM + MGID — a payroll principal da casa.
- **Non-AMP (~36%):** só Teads + 360yield — e **18 slots `.ad-space` VAZIOS** (o "vale das vitrines apagadas", nosso achado nº 1).
- **GAM (Google Ad Manager)** = a mesa de leilão da casa (rede `/21715141650,22670554696/`). **AdSense** = a rede que preenche o que o GAM não vender (e o motor SOZINHO dos 8 temáticos, via auto ads `ca-pub-8991943608456423`). **Taboola/Teads/MGID** = redes concorrentes que pagam por comportamento, não só clique.
- `ads.txt` (1.902 linhas) = a lista oficial de quem tem PERMISSÃO de vender nosso espaço — existe pra impedir fraude; anúncio de vendedor fora dela é dinheiro roubado.

## 5. O que NÃO fazer (as regras de ouro que o Google cobra caro)

1. **Nunca clicar nos nossos anúncios** (nem "pra testar") — banimento na hora, sem recurso.
2. **Nunca pedir clique** ("clique aqui pra ajudar o site") — violação de política.
3. **Anúncio não pode encobrir conteúdo** (nem sticky em cima de texto) — a auditoria de 16/06 já pegou isso como P0.
4. **Conteúdo é o ativo:** sem política de privacidade e sem conteúdo original, o AdSense corta a conta.
5. As 3 mudanças de maior risco da casa passam por `ad_inserter`/`wp_options` — **sempre backup antes, nunca em hora de pico** (regra viva da casa, mantida).

## 6. Exercício de casa (5 min, celular)

Abrir o app AdSense → Relatórios → achar: (a) impressões de ontem; (b) o RPM da conta. Guardar os 2 números. Na próxima aula comparamos com o que o robô vai puxar sozinho pela API — e a casa passa a enxergar o próprio bolso de 2 em 2 horas.

## Próximas aulas (roteiro vivo)

- **AULA 02** — Lendo o painel do AdSense e do GAM sem medo (cada número, o que significa, onde mora o dinheiro).
- **AULA 03** — AMP × non-AMP: por que 64% da casa renderia diferente (e o caso dos 18 slots vazios).
- **AULA 04** — Viewabilidade: nem todo anúncio visto é anúncio pago (posição, rolagem, velocidade).
- **AULA 05** — As políticas do Google em linguagem humana (o que derruba conta de editor).
- **AULA 06** — Os 8 temáticos: auto ads, por que só o riocarta veiculou, e o plano de ativação.

— DS Nuvem Publicidade (DS-N Pub) · 20260901 01:52:00 BRT · DSH/us65
