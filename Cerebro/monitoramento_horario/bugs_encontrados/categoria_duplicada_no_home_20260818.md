# Bug de taxonomia — categoria "No home" duplicada (18/08/2026 ~02:15)

- **Sintoma:** existe uma categoria espúria com name "20699" (term_id 21164, slug "20699") além da verdadeira "No home" (term_id 20699, slug no-home, term_taxonomy_id 20699). Comandos wp-cli por número ("20699") resolvem para a espúria (name/slug casam primeiro) — quase apliquei a categoria errada no post 266268.
- **Fix do caso:** post 266268 ficou com Economia (43) + No home (20699) — aplicada pelo slug único `no-home`; espúria removida por name.
- **Teste:** WP_Query category__not_in=[20699] exclui o post da home ✅.
- **Pendência faxina:** a categoria espúria (term_id 21164, agora count=0) deve ser excluída pelo protocolo da faxina (validação SEO 404 antes). Lição: usar SLUG nas operações de categoria no-home; nunca o número.
