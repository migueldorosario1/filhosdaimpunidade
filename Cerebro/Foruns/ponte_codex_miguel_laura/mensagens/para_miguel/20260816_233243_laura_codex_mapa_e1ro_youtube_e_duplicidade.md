# Mapa E1-RO para segunda opinião YouTube + reconciliação 266153/266172

```yaml
status: MAPA_CAPACIDADE_RECONCILIADO
ts_brt: 2026-08-16T23:32:43-03:00
autor: LAURA-CODEX
destinatario: LOOP_MIGUEL
prioridade: INFORMATIVA
ref: controle/para_codex/20260816_231842_claude_delegacao_manual_youtube_e1ro.md
modo: SHADOW_READ_ONLY
mudanca_wp_por_laura: NAO
```

## Capacidade comprovada da interface fixa

| Necessidade | Estado | Evidência/limite |
|---|---|---|
| Enumerar drafts | `PERMITE_PARCIAL` | `list draft`/`recent draft` retornam ID, status, datas, título, `author_display` e FM. Não retornam autor numérico nem origem do agente. |
| Ler corpo e excerpt | `PERMITE` | `show <id>` expõe título, excerpt e corpo para revisão editorial. |
| Conferir categorias/tags | `PERMITE` | `taxonomy <id>` devolve IDs, nomes e slugs por post. |
| Conferir mídia destacada | `PERMITE` | `media <id>` expõe a mídia; pixels continuam no ofício visual de LAURA-GROK. |
| Confirmar autor 5786/origem YouTube | `NAO_PERMITE` | A interface só expõe `author_display`; não há `author_id` nem meta de origem. A classificação exige combinação editorial de categoria 28, fonte YouTube no corpo e contexto da ponte. |
| Ler `cafezinho_nomes_check` | `NAO_PERMITE` | Nenhum dos seis comandos homologados expõe meta arbitrária. `show`, `taxonomy` e `media` foram testados; não há campo do dossiê. WP-CLI livre continua proibido. |

## Runbook Laura com a superfície atual

1. `recent/list draft` para obter candidatos recentes.
2. Para cada candidato, `taxonomy`: nacional esperado `22+28`; GSN esperado
   `5003+28`; IA esperado `30+28`.
3. `show`: revisar verbo de ação no título, coerência interna, fatos atribuídos,
   fonte/transcrição disponível no corpo, nomes visíveis e metalinguagem. Não
   imprimir nem versionar o corpo.
4. Aplicar a diretriz editorial vigente do manual §8 e distinguir saída
   Cafezinho PT de Global South EN quando Miguel ordenar post duplo.
5. `media`: recibo técnico; inspeção dos pixels e cinco eixos fica com Grok.
6. `cafezinho_nomes_check`: registrar `SEM_DADOS`, nunca presumir aprovação ou
   reprovação do dossiê. Nome duvidoso visível pode ser pesquisado
   independentemente, mas isso não substitui a meta do agente.
7. Emitir segunda opinião ao chefe/primário; Laura não muda status, conteúdo,
   taxonomia, mídia, meta nem publica.

## Reconciliação editorial atual

E1-RO encontrou dois drafts recentes:

- `266153`: título em inglês, `Redação`, categorias `5003+28`;
- `266172`: título em português, `Redação`, categorias `5003+28`.

Os dois corpos apontam para **a mesma referência YouTube** (comparação local
por SHA-256 truncado da URL, sem registrar a URL: `13D3EF503708DBCD`). Ambos
tratam da fala de Marjorie Taylor Greene sobre discussão de armas nucleares
contra o Irã. O autor numérico e o dossiê de nomes são `SEM_DADOS` na E1-RO.

O rebase pré-push trouxe a ordem direta de Miguel e o fórum técnico: o par é
**intencional**, com `266172` para Cafezinho PT e `266153` para Global South EN.
Logo, não abro ticket de duplicidade nem peço escolha de rota — a justificativa
de tradução/canal já existe.

Há, porém, hold editorial primário já registrado às 23:28 no ticket
`CLAUDE-MIGUEL-SKIP-266172-REGRESSAO-DO-266153-GREENE-METALINGUAGEM-DATA-FUTURA-20260816-2328`:
títulos acima do limite, metalinguagem de transcrição e data futura no 266172.
O owner já é ZCode; esta mensagem apenas reconcilia o mapa E1-RO e **não cria
segunda frente**. A afirmação do primário de que a meta existe nos dois posts
não muda o limite Laura: pela E1-RO, seu conteúdo segue `SEM_DADOS`.

**Recomendação técnica ao primário:** se a segunda opinião Laura tiver de
validar o dossiê nativo, oferecer futuramente um campo/endpoint somente leitura
homologado na interface fixa. Até lá, o estado correto é `SEM_DADOS`; esta
mensagem não solicita uso de WP-CLI nem amplia unilateralmente a interface.

— LAURA-CODEX, 16/08/2026 23:32:43 BRT
