# Sincronizar publicação WP com chatbots (celular + desktop)

**Atualizado:** 2026-06-20  
**Problema:** ChatGPT, Grok, Claude no celular **não leem** `Outros/chaves/agentes_labs/.env.unificado` no disco do Miguel.  
**Solução:** um **cartão de bolso** autocontido — credenciais + curl + fetch + Python — que Miguel cola uma vez em cada app.

---

## Arquivo-fonte (com credenciais)

```text
Outros/chaves/wp_cafezinho_chatbots.md
```

- Gitignored (pasta `chaves/`)
- Contém `WP_USER`, `WP_APP_PASSWORD`, exemplos prontos para copiar
- Regenerar após trocar Application Password:

```bash
cd "/home/migueldorosario/Downloads/Antigravity Google"
python3 Cerebro/scripts/gerar_cartao_wp_chatbots.py
```

---

## Onde colar (uma vez por app)

| App | Onde |
|-----|------|
| **ChatGPT** (celular/desktop) | Project → Add files → `wp_cafezinho_chatbots.md` **ou** Custom Instructions |
| **Claude** | Project Knowledge → upload do `.md` |
| **Grok Desktop** | Anexar ao projeto / colar na memória da sessão |
| **Grok celular** | Google Docs espelho (ver abaixo) + colar trecho no chat |
| **Google Gemini** | Gems → instruções + upload do arquivo |
| **Qualquer LLM** | Google Docs **“Cafezinho — Publicar WP”** no celular |

### Google Docs (recomendado para celular)

1. Abrir `Outros/chaves/wp_cafezinho_chatbots.md` no PC
2. Copiar tudo → novo Google Doc
3. Nome: **Cafezinho — Publicar WP (chatbots)**
4. No celular: abrir Doc → selecionar trecho → colar no chat quando for publicar

---

## Dois modos de operação

| Modo | Quem | Como |
|------|------|------|
| **A — Workspace** | Cursor, Claude Code, Codex no PC | `scratch/publicar_cafezinho_wp.py` + cofre `.env.unificado` |
| **B — Chatbot** | ChatGPT, Grok, Claude app | Cartão de bolso + imagem **anexada no chat** + curl/fetch/Python do cartão |

---

## Limitação importante (chatbots)

Chatbots **não acessam** arquivos locais do Miguel automaticamente. Para publicar:

1. Miguel **anexa a imagem** no chat (ou manda URL pública temporária)
2. Miguel cola o corpo HTML (ou pede ao LLM montar)
3. LLM usa credenciais do cartão e executa fetch/curl **se tiver ferramenta de código/rede**
4. Se o app **não executar rede**, o LLM monta os comandos curl prontos → Miguel cola no Termux/PC

---

## Links canônicos (sem senha)

| Recurso | Caminho |
|---------|---------|
| Node Cérebro | `Cerebro/CEREBRO_NODE_PUBLICACAO_WP_CAFEZINHO.md` |
| Tutorial completo | `Projeto Cafezinho Agentes/Foruns/forum_tutorial_publicar_wordpress_cafezinho_todos_llms_20260620.md` |
| Script PC | `scratch/publicar_cafezinho_wp.py` |
| Memória Grok | `Cerebro/memorias_provisorias/memoria_grok_viva.md` |

---

## Checklist Miguel (setup único)

- [ ] Gerar/atualizar `Outros/chaves/wp_cafezinho_chatbots.md`
- [ ] Copiar para Google Docs no celular
- [ ] Upload no ChatGPT Project / Claude Project
- [ ] Testar: criar draft de teste com imagem anexada no chat
- [ ] Apagar draft de teste no WP Admin se não for usar

— Grok, 2026-06-20