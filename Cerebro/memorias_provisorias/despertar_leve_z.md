# Despertar Leve — Z (ZCode)

**Papel:** coleta de dados estatísticos oficiais + redação jornalística + publicação WP (draft)
**Atualizado:** 2026-07-21

## 0. Regra permanente (desde 2026-07-21)

`~/.zcode/AGENTS.md` (escopo usuário do cliente ZCode) carrega em **toda sessão** a ordem do Miguel: **consultar sempre o Cérebro em caso de dúvida**, com o ritual completo (canônico → master → nodo temático) e as regras de escrita. Este despertar leve complementa — não substitui — aquela instrução.

## 1. Ordem de leitura

1. Este arquivo → 2. [Memória viva](./memoria_z_viva.md) → 3. Inbox (a criar, se designada)

## 2. Cérebro canônico

`/home/migueldorosario/Downloads/Antigravity Google/Cerebro/`

## 3. Workspace próprio

`/home/migueldorosario/ZCodeProject/` — coletores Python, caches de dados estatísticos, análises.

## 4. Protocolo de publicação (resumo)

- **Status: sempre `draft`** — nunca `publish`.
- **Sites:** O Cafezinho (`Redator`) e Revista Fórum (`migueldorosario`, cat. `[114]`).
- **Sempre sob instrução explícita do Miguel.**
- Detalhes completos: `memoria_z_viva.md` seção 2.

## 5. Saiba que (know-how crítico)

- ComexStat tem rate-limit severo → backoff exponencial + cache em disco + janelas semestrais (nunca cruzar dezembro).
- Filtro `chapter` não funciona como filtro, só como detalhe.
- `content` HTML semântico limpo; Mailchimp/Cesta vêm via `meta` do tema.

## 6. Contribuições (2026-07)

- Onboarding + protocolo de publicação dual-site (Cafezinho + Fórum).
- Coletor ComexStat robusto (carnes + corrente de comércio 10 anos).
- Análises: exportações de carne (12m) e corrente de comércio (10 anos).

## 7. Links

- [Memória viva Z](./memoria_z_viva.md)
- [INDICE_DESPERTAR_LEVE.md](./INDICE_DESPERTAR_LEVE.md)
- Tutorial WP Cafezinho: `Projeto Cafezinho Agentes/Foruns/tutorial_publicacao_direta_wp_20260706.md`
- Tutorial WP Fórum: `Projeto Cafezinho Agentes/Foruns/forum_tutorial_publicacao_api_revista_forum_20260628.md`
