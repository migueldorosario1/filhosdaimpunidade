---
name: separacao-sas-indexing-concluida-20260716
description: "Bloco A do sprint sites temáticos CONCLUÍDO 16/07/2026 01:15 BRT — 7 sites temáticos + Cafezinho canônico com service accounts do Google Indexing API totalmente isoladas, cada uma com projeto GCP próprio, quota 200/dia própria, reputação própria. Bloco B (reforma editorial V4) ainda não iniciado."
metadata: 
  node_type: memory
  type: project
  originSessionId: 37e2f19f-f9dc-43d8-a2fa-f9029a716a89
---

# Separação de Service Accounts Google Indexing — Bloco A CONCLUÍDO

**Data:** 16/07/2026 01:15 BRT (executado ao longo da sessão que começou 15/07 22:00 BRT).

## Resumo executivo

Bloco A do sprint sites temáticos ([[project_sprint_acervo_midia_publicador_microsservicos_20260625]] adjacente, mas separado — este é sobre indexação, não Publicador+Acervo) concluído. Cada um dos 7 sites da constelação temática + Cafezinho canônico agora tem:

- **Projeto GCP próprio** (quota Google Indexing 200 pings/dia isolada)
- **Service account própria** (reputação Google isolada)
- **Keyfile própria** no NYC em `/root/agent_data/indexing_keys/<site>.json`
- **Ownership GSC exclusivo** da SA correspondente
- **Isolamento no código** via `INDEXING_SITES` dict em `/root/util_indexing.py`

## Mapeamento canônico

| Site | Projeto GCP | Service Account | Keyfile |
|---|---|---|---|
| ocafezinho.com | gen-lang-client-0200069757 | indexing-cafezinho@... | cafezinho.json |
| globalsouth.news + globalsouthnews.com.br | indexing-gsn | indexer@indexing-gsn.iam... | gsn.json |
| riocarta.com | indexing-riocarta | indexer@indexing-riocarta.iam... | riocarta.json |
| mundotrilhos.com + mundodostrilhos.com | indexing-mundotrilhos | indexer@indexing-mundotrilhos.iam... | mundotrilhos.json |
| discoverbrazil.news | indexing-discoverbrazil | indexer@indexing-discoverbrazil.iam... | discoverbrazil.json |
| mapario.com.br | indexing-mapario | indexer@indexing-mapario.iam... | mapario.json |
| aiatolah.com | indexing-aiatolah | indexer@indexing-aiatolah.iam... | aiatolah.json |
| ceara.digital | indexing-ceara | indexer@indexing-ceara.iam... | ceara.json |

## Denylist (proteção)

Domínios que NUNCA devem ser indexados via API — `INDEXING_DENYLIST` em `util_indexing.py`:
- `cafezinho.news` (espelho noindex site-wide)
- `controle.ocafezinho.com` (URL admin WP — deve virar www.ocafezinho.com via canonicalizar_url)

## Descoberta operacional importante

**O dropdown "Pesquise a propriedade" do GSC é um campo de busca, não lista completa.** Só properties recentes/favoritas aparecem por padrão. Pra ver outras, **digitar o nome no campo**. Isso confundiu Miguel na sessão — ele achou que tinha removido properties dos temáticos, mas só não as via na lista curta. Rio Carta, Mundo Trilhos, Discover, GSN e Cafezinho **já estavam verificados na conta dele** — não precisou re-verificar.

**Precisaram re-verificar** (nunca estiveram no GSC dele): AIatolah + ceara.digital + Mapa Rio (esse último por confusão no processo). Todos via **DNS TXT** — GoDaddy pros 4 primeiros temáticos, Vercel DNS pro Mapa Rio.

## Descoberta pro Bloco B: todos os 7 temáticos são Vercel

Verificado via `server:` header + `x-vercel-id` + IPs (`76.76.21.21`, `64.29.17.1`, `216.198.79.1`):

- globalsouth.news → Vercel
- riocarta.com → Vercel (confirmado 16/07 quando Miguel corrigiu suposição inicial)
- mundotrilhos.com → Vercel
- discoverbrazil.news → Vercel
- mapario.com.br → Vercel
- aiatolah.com → Vercel
- ceara.digital → Vercel

**Zero WordPress entre os temáticos.** Só Cafezinho canônico (ServerDo.in) continua WP. Consequência pro Bloco B: V4 atual usa WP REST API — precisa ser reescrito por completo pro publicador de todos os 7 sites. Piloto será piloto do "V4 adaptado pra Vercel", não V4 direto. CLAUDE.md diz WP em vários deles — desatualizado.

## Regra pro Vercel DNS (diferente do GoDaddy)

- **GoDaddy:** campo `Name` aceita `@` pra raiz do domínio
- **Vercel:** campo `Name` **NÃO aceita `@`** — precisa deixar **VAZIO** pra raiz. Erro típico: `Invalid 'name' parameter`.

## Como usar isso agora

Qualquer agente que chame `util_indexing.notificar_e_logar(url)` ou `notificar_e_logar_v2(url)` recebe automaticamente a SA correta pelo domínio da URL. Se o domínio não estiver em `INDEXING_SITES` OU estiver em `INDEXING_DENYLIST`, o util retorna `None` e o ping é rejeitado antes de sair.

Smoke test manual pra validar isolamento:
```bash
ssh root@198.199.121.136 '/root/venv/bin/python3 -c "
import sys; sys.path.insert(0, \"/root\")
import indexador_google, util_indexing
url = \"https://<site>/\"
kf = util_indexing.keyfile_para_url(url)
print(\"keyfile:\", kf)
print(\"resultado:\", indexador_google.notificar_google(url, keyfile=kf))
"'
```

## Backups e reversão

- Backups do `util_indexing.py` e `indexador_google.py` no NYC: `.bak_pre_multiaccount_20260714_181935`
- Reverter: `cp <bak> util_indexing.py && cp <bak> indexador_google.py` — volta ao modelo de 1 SA
- Todas as 8 keys também estão localmente em `~/gcloud_indexing_keys/` (backup Miguel)

## Falta (opcional / de fechamento)

- **Deletar projetos GCP obsoletos** (`open-claw-gsn` + 3 `ZOMBIE - Cafezinho*`): libera quota, reversível 30d. Miguel não priorizou.
- **Contador de pings por-site**: hoje `ping_count` no util parece ser geral, não por-site. Bug menor de observabilidade — funcionalmente indexação funciona 100%. Registrado como pendência técnica se algum dia precisar.

## Próximo natural

**Bloco B — reforma editorial V4 dos agentes temáticos.** Fórum: `Cerebro/Foruns/forum_sprint_sites_tematicos_completo_20260714.md`. 6 perguntas em §7 aguardando decisão do Miguel (volume por site, cross-post, piloto Rio Carta, etc). Sprint 5-8 semanas.

## Referências

- Fórum sep SAs: `Cerebro/Foruns/forum_separacao_service_accounts_indexing_20260714.md`
- Fórum sprint temáticos: `Cerebro/Foruns/forum_sprint_sites_tematicos_completo_20260714.md`
- Snapshot sessão: `Projeto Cafezinho Agentes/Ponto de Retomada/Claude Code/20260716_011500_sessao.md`
