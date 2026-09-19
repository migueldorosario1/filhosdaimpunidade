---
name: Master Lula corrigido após auditoria F1-F6 — pronto local
description: agente_master_lula.py reescrito no padrão canônico Trindade + pré-processamento Stuckert; coletor marca origem_coleta; ainda não foi pro Tencent; banco local de fotos parou em 2026-04-15
type: project
originSessionId: da85d7d2-f66a-4b5a-b9db-6d27f8e11791
---
Em 2026-04-20 Antigravity entregou Master Lula com 6 furos. Claude Code aplicou as correções localmente (sem tocar Tencent/motor_publicador/crontab).

**Mudanças em `agente_master_lula.py`:**
- Reescrito no padrão canônico (igual master_nacional): só chama `iniciar_publicacao_especializada(...)` com `como_rascunho=True`.
- Removido `publicar_no_wordpress` inventado, taxonomia hardcoded, prompts customizados.
- Adicionado pré-processador `preparar_banco_lula()` que aplica F4 (regex word-boundary lula/presidente/planalto) + F6 (classifica doméstica/internacional via origem_coleta + lista FONTES_INTERNACIONAIS).
- Para pautas domésticas: `buscar_foto_stuckert()` faz match SQLite ±36h + Jaccard ≥0.18 com tokens lematizados (stopwords PT removidas). Se acha foto, sobrescreve `url_imagem_fonte` com URL Stuckert (motor pega via Prioridade 1 og:image + Tribunal Visual).
- Sem foto + doméstica → marca `processado_v9=True` (skipa este ciclo, sem fila própria conforme F2).

**Mudanças em `robo_coleta_lula.py`:**
- Coletor agora marca `origem_coleta="rss"` ou `"brave"` em cada artigo. Necessário pra F6 funcionar no Master.
- Tracking de origem via dict `{future: origem}` no ThreadPoolExecutor.

**Smoke test 2026-04-20 21:08:** imports OK, dry-run pré-processo: 5 pautas → 3 skip_sujeito + 2 skip_sem_foto + 0 injetadas. Comportamento correto da regra editorial.

**🚨 Achado importante:** banco LOCAL `banco_imagens_reais.db` parou em **2026-04-15** (5 dias atrás). Logo, hoje 100% das pautas domésticas batem em "sem foto Stuckert". Possíveis causas:
1. Banco local não está sync com Tencent (provável — não há cron de sync para baixo).
2. `robo_coleta_flickr_rapido.py` no Tencent pode estar com bug e Stuckert não postou nada há 5 dias (improvável — verificar log).
3. Stuckert/Planalto realmente não postou (feriado de Páscoa + emenda?).

**Status:**
- Arquivos corrigidos: `root/agente_master_lula.py`, `root/robo_coleta_lula.py`.
- NÃO deployado no Tencent (Miguel pediu cautela com sistema em produção).
- Crontab NÃO modificado.

**REVISÃO 21:30** — Miguel pediu Flickr API ao vivo (não SQLite — "no caso do agente lula tem que ir direto no flickr, eu assinei o flickr e tudo só pra isso"). `agente_master_lula.py` reescrito:
- Removido SQLite. Função `consultar_flickr()` chama API ao vivo (`flickr.people.getPublicPhotos`) com cache em memória por execução.
- 3 planos cascata: A (conta Lula 157736962@N05, ±36h, Jaccard 0.18) → B1 (amplia para Planalto+MRE+Senado, ±7d, Jaccard 0.12) → B2 (aceita og:image se fonte é EBC/Planalto — Agência Brasil já embeda foto Stuckert).
- FLICKR_API_KEY carregada via load_dotenv do .env.unificado.

**Smoke test final 2026-04-20 21:29:** 5 pautas → 3 skipadas (1 sem sujeito Lula correto: "Brasil e Alemanha firmam acordo" é pauta institucional Nacional, não Lula; 2 internacionais sem foco no presidente) + 2 prontas via plano_b2 (Lula+Merz, Lula+África do Sul). Plano A vazio porque Jaccard tags-Flickr (evento) vs título-AB (fala) diverge — limitação conhecida, B2 cobre. Conta Planalto deu 503 transient na chamada B1.

**Próximos passos sugeridos:**
1. Validar no Tencent se banco de fotos lá está atualizado. Se sim, `rsync` dos 2 arquivos novos + cron de teste manual antes de automação.
2. Se banco Tencent também parou em 15/04: investigar `robo_coleta_flickr_rapido.py` em produção.
3. Cron sugerido para Master Lula: `0 8,12,16,20 * * *` — mas só após validação manual de 2-3 drafts.
