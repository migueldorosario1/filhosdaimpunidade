# 📮 Fórum — Pesquisa: Substack tem API? Publicação programática? (17/09/2026)

**Quem:** ZCode/GLM-5.3 · **Pedido do Miguel (17/09 ~11:4x):** "vê se o sub-stake tem API, se ele permite postagem via API sem entrar lá e publicar, vê se existe senha de aplicação, que eu possa programar a publicação aqui com você, com uma tarefa agendada."
**Status:** ✅ PESQUISA CONCLUÍDA — NADA implementado. AGUARDA "vai" do Miguel.

## Resposta curta (as 3 perguntas dele)

1. **Tem API?** Tem uma API *oficial* minúscula, lançada com ToS em jan/2026 — mas ela é **só leitura de perfis públicos** (contagem de assinantes, rankings). **NÃO existe endpoint oficial de criar/publicar posts.**
2. **Permite postar via API sem entrar no painel?** **SIM, dá** — pela **API interna não documentada** do próprio site (os endpoints `/api/v1/...` que o navegador usa), via biblioteca não-oficial mantida: **`python-substack`** (ma2za; PyPI; MIT; 175★; atualizada 11/09/2026). Cria rascunho de Markdown, **agenda** (`drafts schedule --at 2026-08-01T09:00:00-03:00`) e **publica** (`drafts publish`, com `--no-send` p/ NÃO disparar e-mail aos assinantes).
3. **Existe "senha de aplicação"?** **NÃO** — o Substack não tem esse conceito (é coisa de WordPress). O que existe:
   - **login por e-mail+senha** (se a conta tiver senha definida — por padrão o Substack usa magic link), ou
   - **cookie de sessão do navegador** (`substack.sid`) colado num `.env` (`COOKIES_PATH`/`COOKIES_STRING`) — mais confiável quando há captcha/magic-link.
   - O cookie **expira** de tempos em tempos → renovar colando de novo. Isso é a "senha de aplicação" de facto: um segredo de sessão no cofre.

## Caminho pronto para quando o Miguel der o "vai"

1. Miguel define senha na conta OU exporta o cookie `substack.sid` do navegador logado.
2. Gravar o segredo no cofre unificado + espelhar (Regra Nº 4) + registrar no `CEREBRO_NODE_COFRE_CHAVES.md`.
3. Pilotinho: script que cria **rascunho** de teste → Miguel confere no painel → publicar com `--no-send` no primeiro disparo real.
4. **Tarefa agendada:** automation do ZCode (CronCreate) ou cron do Dell chama o script (Markdown → rascunho → agenda/publica). Flui igual à esteira de fios X+FB.

## Alternativas avaliadas

- `jakub-klys` não — **jakub-k-slys/substack-api** (TypeScript, 95★, ativa): interface por entidades; serve se preferirmos Node.
- **NHagar/substack_api** (Python, 225★): SÓ LEITURA — não publica. Descartada para o nosso fim.
- **MCP servers** (ty13r/substack-mcp-plus; IgnazioDS/Substak-MCP — único que cita schedule explicitamente): rota interessante se quisermos publicar via agente MCP no futuro.
- **Serviços de terceiros** (PublishPort, Narrareach): publicam por você, mas exigem entregar credenciais/conta a terceiros → **não recomendado** (segurança da casa).

## Riscos e salvaguardas

- Endpoints **não documentados** podem mudar sem aviso (a lib se ajusta; já vem sendo mantida desde 2023).
- Uso moderado com o próprio cookie **imita o comportamento do navegador** — sem relatos de ban por publicar na própria conta; ainda assim, ToS é por conta do usuário.
- A lib tem salvaguardas embutidas: criar rascunho é sempre seguro; publicar/excluir pedem confirmação (`--yes` em modo não-interativo); `--no-send` evita e-mail aos assinantes.

## O que aconteceu / o que falta / o que preciso de você (Miguel)

- **O que aconteceu:** pesquisa concluída com fontes primárias (README da lib, PyPI, topic GitHub, artigos). Veredito acima.
- **O que falta:** tudo de implementação (conta, segredo no cofre, script pilotinho, tarefa agendada).
- **O que preciso de você:** o "vai" + a conta do Substack ter senha definida OU você me entregar o cookie de sessão (e me dizer qual a publicação/domínio).

## Fontes

- https://github.com/ma2za/python-substack · https://pypi.org/project/python-substack/
- https://github.com/topics/substack-api
- https://iam.slys.dev/p/no-official-api-no-problem-how-i (método da engenharia reversa)
- https://github.com/NHagar/substack_api (read-only)
- https://www.publishport.app/blog/auto-publish-to-substack/ · https://substack.com/api-tos
- https://mostlypython.substack.com/p/automating-substack-notes (login/sessão do Substack)
