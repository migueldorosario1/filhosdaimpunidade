# 🧠 Memória técnica — Pesquisa API Substack (17/09/2026, ZCode/GLM-5.3)

Log técnico completo da pesquisa. Nenhum código foi escrito; nenhum segredo foi criado.

## Metodologia

- WebSearch: "Substack official API publish post programmatically 2026" + "Substack API key application password publish newsletter automation" + query de endpoints.
- WebFetch: github.com/ma2za/python-substack · github.com/NHagar/substack_api · github.com/topics/substack-api · iam.slys.dev/p/no-official-api-no-problem-how-i.

## Fatos verificados (com fonte)

1. **API oficial do Substack NÃO publica.** ToS de API desde jan/2026 (substack.com/api-tos); documentação pública cobre endpoint de busca de perfil público (assinantes/rankings). PublishPort e discussões no Reddit/n8n confirmam ausência de endpoint de publicação oficial.
2. **API interna existe e é usada pelo próprio web app**: endpoints `/api/v1/...` autenticados por cookie de sessão (`connect.sid`/`substack.sid`). O post do slys.dev documenta o método de engenharia reversa (DevTools → replay cURL → generalizar). Geralmente legal imitando comportamento do navegador com as próprias credenciais (afirmação do autor, não parecer jurídico).
3. **Lib recomendada: `python-substack` (ma2za)** — PyPI `pip install python-substack`, MIT, 175★, 120 commits, atualizada 11/09/2026, aceita contribuições.
   - Auth: `Api(email=..., password=..., publication_url=...)` OU cookies via `.env` (`COOKIES_PATH` / `COOKIES_STRING`). README: cookie é mais confiável quando Substack pede captcha/magic-link.
   - CLI: `substack drafts create post.md --title "..." --tag python --slug my-post` (sempre cria rascunho não publicado); `substack drafts publish 12345 --no-send`; `substack drafts schedule 12345 --at 2026-08-01T09:00:00+03:00`; `substack drafts unschedule 12345`.
   - Python: `from substack import Api; api.create_draft_from_markdown(title=..., markdown=..., tags=[...])` (publica só com `publish=True`).
   - Salvaguardas: publicar/excluir exigem confirmação (`--yes` não-interativo); `--no-send` não e-maila assinantes; exports são read-only.
   - Também expõe MCP (Draft, publish, schedule via MCP server).
4. **NHagar/substack_api** (Python, 225★): READ-ONLY (posts, podcasts, chats com cookie). Não serve para publicar.
5. **jakub-k-slys/substack-api** (TypeScript, 95★, atualizada 03/09/2026): cliente por entidades (publications, posts, comments) — do autor do artigo de engenharia reversa; adotada por integração n8n.
6. **IgnazioDS/Substak-MCP**: único repo do topic que menciona "schedule" explicitamente; **ty13r/substack-mcp-plus** (23★): 12 ferramentas, auth por navegador.
7. **Substack não tem senha por padrão**: login é magic link por e-mail (mostlypython.substack.com/p/automating-substack-notes). Conta PODE ter senha definida. **Não existe "application password"/API key** — o análogo é o cookie de sessão, que expira e precisa ser renovado.

## Decisões da casa

- Rota eleita: `python-substack` (ma2za) + cookie de sessão no cofre + script pilotinho (rascunho → conferência → publish `--no-send`) + tarefa agendada (CronCreate ZCode ou cron Dell). Igual ao padrão da esteira de fios X+FB (só dispara com "vai").
- Descartado: serviços terceiros (PublishPort/Narrareach) por exigirem entrega de credenciais a terceiros.

## Estado

- Pesquisa: CONCLUÍDA. Implementação: 0% — aguarda "vai" + segredo (senha definida ou cookie `substack.sid`) + URL da publicação.

## Arquivos relacionados

- Fórum: `Cerebro/Foruns/forum_substack_api_pesquisa_20260917.md`
- Nodo de catálogo: `CEREBRO_NODE_PUBLICACAO_WP_CAFEZINHO.md` (seção canais externos)
- Caso irmão (padrão de esteira agendada): fóruns da esteira de fios X+FB de 17/09
