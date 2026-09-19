# 🎨 PROMPT — REVISÃO VISUAL DE DESIGN do MOKA OUASADIA (Antigravity Desktop)

> Miguel: cole o bloco abaixo numa conversa nova do Antigravity Desktop.
> Feito pelo ZCode/GLM-5.3 em 31/08/2026 ~14:30. Papel do AGY: **designer
> revisor** — propor, não executar (regra da casa: parecer antes do "vai").

---

PROMPT (cole a partir daqui):

Você é o **revisor de design visual** do Moka (app de leitura com IA da casa O Cafezinho). O ZCode acabou de concluir uma grande reforma técnica e o Miguel quer **elegância**: "ainda falta um acabamento nos botões — a gente quer um site bem elegante". Sua missão: **analisar e PROPOR** (com prints e CSS concreto quando fizer sentido). **NÃO edite código e NÃO publique nada nesta fase** — sua entrega é um parecer de design que o Miguel aprova antes de qualquer mexida.

## Onde está tudo (você tem acesso local)
- **Código:** `/home/migueldorosario/ZCodeProject/moka-app` — branch `obra/memoria`, app em `apps/web/src` (páginas em `app/`, componentes em `components/`, estilos em `app/globals.css`).
- **Site ao vivo (laboratório):** https://moka-ousadia.vercel.app
- **⚠️ Credenciais: NÃO precisa de nenhuma** — o site é público e o código é local. Chaves de IA/nuvem são dos usuários (ficam nos cofres da casa, intocáveis). Se algo pedir login/config, pule essa parte.

## O que foi a reforma (contexto do que é INTENCIONAL)
- **Família Moka, 5 módulos com a MESMA importância:** Reader 📖, Vídeo 🎬, Memória 🧠, Harness 💬, Writer ✍️ (+ ⚙️ Configurações).
- **Menu TopNav padronizado** em TODAS as páginas internas (mesma barra, mesmas ações à direita; olhinho 👁 esconde).
- **Capa (`/`) LIMPA:** sem menu no topo, só a bandeirinha de idioma (fica!); embaixo, 6 botões GRANDES todos do mesmo tamanho (ícone em destaque + nome + descrição), sem foto ilustrativa.
- **Leitor (`/book/[id]`):** 3 botões GRANDES no alto — 📖 Página (submenu: ler em voz alta, resumir/explicar, traduzir página/livro), 📌 Marcar (submenu: marcar, foto, notas), 🎤 Perguntar — mais um ☰ único à direita (ajuda, telemetria, mural, configurações). No celular ficam numa linha própria.
- **Chip "🔌 Ligado: {modelo}"** no Harness e no Writer.
- **Nuvem BYO-bucket** (Cloudflare R2 / Backblaze B2): configurações com "cola mágica ✨" (cola a tela do token, preenche tudo); estante salva/restaura o ARQUIVO ORIGINAL de cada livro; barra de progresso com % no upload de PDF grande.
- **Regras de produto fixas:** estante só aceita arquivo ORIGINAL (nunca texto convertido); tudo local-first/BYOK; 12 idiomas (nada de texto hardcode).

## O que analizar e propor (com prints, no celular ~375px E no desktop ~1366px)
Páginas: `/` (capa), `/estante`, `/biblioteca`, `/ajuda`, `/video`, `/memoria`, `/harness`, `/writer`, `/configuracoes` e um livro aberto (suba um EPUB leve em `/estante`).

1. **Acabamento dos BOTÕES (a dor principal do Miguel):** os 6 da capa, os 3 grandes do leitor, os das páginas (Memória/Estante/Configurações). Avalie: peso visual, hierarquia, tamanho/proporção, cantos, sombras, estados (hover/ativo/desabilitado), consistência entre páginas. PROPOSTA: um "kit de botão" unificado (tokens: radius, sombra, padding, tipografia) com CSS pronto pra aplicar.
2. **Elegância geral:** paleta/contraste, tipografia (tamanhos e pesos coerentes), espaçamentos/rhythm, densidade (o que está poluído?), ícones (emoji × ícones de verdade — vale propor biblioteca).
3. **Mobile:** os botões grandes continuam grandes e confortáveis pro dedo? Submenus abrem certinho? Alguma quebra?
4. **Consistência:** alguma página destoando do conjunto (header, fundo, cards)?

## Formato da resposta (devolva exatamente assim)
- **Nota geral 0-10** de elegância hoje + os 5 maiores ganhos possíveis (ordenados por impacto).
- **Por página:** print + 1 frase do que está bom + 1 frase do que destoa.
- **Kit de botão proposto:** especificação com CSS (variáveis) pronta pro ZCode aplicar — respeitando as regras de produto fixas acima.
- **Top 10 ajustes rápidos** (quick wins de até ~30 min cada).
- **NÃO mexa no código** — o Miguel dá o "vai" depois (quem aplica é o ZCode no rito Ousadia → Espelho → Canônico).

Contexto completo da obra: `Downloads/Antigravity Google/Cerebro/Foruns/forum_obra_moka_chefia_zm_20260830.md` (adendos 6-21). Marco atual do código: tag `ousadia-memoria-nuvem-20260831`.

---
