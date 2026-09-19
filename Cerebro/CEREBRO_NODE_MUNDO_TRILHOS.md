# 🚂 CEREBRO_NODE_MUNDO_TRILHOS

> Nodo de conhecimento dedicado ao ecossistema ferroviário (Mundo Trilhos + Rail Post)

---

## Status Operacional

| Item | Valor |
|------|-------|
| Domínio | https://mundotrilhos.com |
| Repo GitHub | migueldorosario1/mundo-trilhos |
| Repo Local Tencent | /home/ubuntu/mundo-trilhos |
| Agente | /root/MT_agente_ferroviario.py |
| Log | /home/ubuntu/mundo-trilhos/agente_ferroviario.log |
| Frequência | A cada 3h (cron) |
| Agente Líder | Kimi Code |

---

## 🚨 PENDÊNCIA CRÍTICA ATIVA

### Imagens Artificiais — Resolver com Banco Real

**Aberto:** 2026-05-31 16:45 BRT  
**Fórum:** `Foruns/forum_urgente_imagens_mundo_trilhos_20260531.md`

**Problema:** Todos os posts estão saindo com imagens geradas por IA (desenhos artificiais) em vez de fotografias reais. O agente busca no banco SQLite real (`banco_imagens_reais.db`) mas cai no fallback de IA porque o banco remoto do Tencent está inacessível e o banco local não tem imagens ferroviárias suficientes.

**Opções:**
- A. Usar banco remoto do Tencent (312k imagens, 315MB) — preferida
- B. Replicar banco localmente — mais rápido
- C. Desativar IA, usar placeholder — mitigação imediata

**Aguardando decisão Miguel.**

---

## Arquivos de Referência

| Arquivo | Descrição |
|---------|-----------|
| `Foruns/forum_dossie_mundo_trilhos.md` | Dossiê operacional completo |
| `Foruns/inbox_trindade/ponte_mundo_trilhos_kimi.md` | Ponte de comando Kimi |
| `Foruns/forum_urgente_imagens_mundo_trilhos_20260531.md` | Pendência imagens (ativo) |
| `root/MT_agente_ferroviario.py` | Agente de produção Mundo Trilhos (Astro/Markdown/Git) |
| `root/agente_ferroviario_v2.py` | Wrapper legado de compatibilidade; não é agente Cafezinho |

---

## Renomeação Operacional — 2026-06-02

Por decisão de Miguel, o agente ferroviário do Mundo Trilhos foi separado nominalmente do Cafezinho para evitar confusão:

- canônico: `root/MT_agente_ferroviario.py`;
- wrapper legado: `root/agente_ferroviario_v2.py`;
- publicação no novo arquivo: somente Mundo Trilhos/Astro (`SITES_PUBLICACAO=['MundoTrilhos']`);
- rotas Cafezinho/cross-post desativadas no agente MT.

Deploy Tencent validado por Codex em 2026-06-02 19:26 BRT. Backup remoto: `/root/agente_ferroviario_v2.py.bak_pre_mt_rename_20260602_1926_codex`.

*Criado em 2026-05-31 por Kimi Code; atualizado em 2026-06-02 por Codex.*
