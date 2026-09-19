# 💰 Banco Ouro — Relatório do Dia 1 (01/09/2026, 18:0x BRT) — maestro ZM

**Missão:** degraus 1+2 executados na madrugada (adapter + medição em sombra nos ciclos reais). Este relatório consolida e recomenda o degrau 3.

## O que foi feito (24h)
1. **Degrau 1 (02:0x):** `banco_ouro_adapter.py` no v4_labs — consulta SQLite read-only (474 fotos uso automático), flag OURO_CAMADA1 (0/log/1), rollback = rm (commit + ROLLBACK_INDEX).
2. **Degrau 2 (02:0x):** hook de medição no dsn_imagem (flag `log` via chaves.sh) — nenhum fluxo alterado.
3. **Prova de conceito (11:1x):** 1ª capa semeada DO acervo (Trump/EBC) — subiu bem (via url_origem; R2 interno/portal dão 400 p/ download externo) e o **olho duplo REPROVOU por unanimidade: foto = Trump com Lula; matéria = Trump×Rússia no G20**. O gate funcionou como rede de segurança perfeita.

## Números da medição (sombra_camada1.jsonl)
| Tipo | Consultas | Com foto no acervo |
|---|---|---|
| Em ciclos reais (worker) | 1 (Trump×G20) | **1 (3 fotos)** — 100% |
| Provas manuais do maestro | 6 | 4 (67%) |

**Leitura honesta:** a amostra real é pequena porque o worker só consulta posts NOVOS não-tentados (o dia teve fila de caça rápida). A cobertura tende alta nas verticais política/geopolítica (entidades top do acervo: Lula, Flávio Bolsonaro, Trump, Haddad, Alckmin, Alcolumbre, Bolsonaro, Moraes, Motta) e nula em empresas/produtos (Caterpillar, Shein, E-goi = miss).

## Recomendação do degrau 3 (para o "vai" do Miguel)
Ligar `OURO_CAMADA1=1` (acervo como camada 1 da cascata) **com 3 pré-requisitos já desenhados:**
1. **Rank contextual:** casar entidade E palavras-chave do título/descrição da foto com o tema da matéria (a reprovação do Trump×Lula ensinou: pessoa certa, contexto errado);
2. **url_origem como fonte de download** (R2 da casa é fechado; alternativa: expor domínio público do portal — decisão futura);
3. **Olho duplo continua juiz inalterado** — o acervo propõe, a visão decide (provado: barruja não passa).

**Custo/benefício:** degrau 3 não elimina a caça externa (misses seguem para Commons/Flickr), mas cobre o maior gargalo (política/geopolítica = maior volume da casa) com foto APROVADA, fresca e licenciada — zero custo de busca externa.

## Estado dos demais fios
- Seeds do maestro: 12 receitas ativas; Kast saiu pelo fluxo autônomo; Lionel com capa aplicada aguardando editoria.
- Verificador de virada (futures): 0 atrasados desde a instalação.
- Sombra continua ligada (mais dados = melhor calibração do rank pós-degrau 3).
