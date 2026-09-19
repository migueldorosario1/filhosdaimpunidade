# 🛡️ Fórum — Redeploy do Repetidor Estatal no NYC (modo rascunho)

**Data de abertura:** 2026-07-14
**Autor da abertura:** GLM CLI (Ming), a pedido de Miguel
**Status:** em execução — deploy + smoke + cron
**Ambiente alvo:** NYC `198.199.121.136` (`/root/`), master primário desde 01/07/2026
**Fonte canônica do código:** `Outros/Agentes Labs/agente_repetidor_estatal.py` (Labs local, versão 14/07/2026)

---

## 1. Contexto e motivação

O `agente_repetidor_estatal.py` é o **"sobrevivente do holocausto"** do Cafezinho (memória `feedback_repetidor_estatal_sobrevive_holocausto.md`) — última linha de defesa editorial, deve continuar postando mesmo quando todo o resto falha.

**Estado pré-redeploy:**
- Script existia no NYC em versão **velha de 23/06** (785 ln, antes da simplificação de 13/07)
- Versão Labs local: **706 ln** (simplificada 13/07, com threshold 65, 6 fontes, status=draft)
- **Cron do repetidor: ausente no NYC** (não rodava há meses)
- Banco `estatal_news.db` no NYC: 320 KB parado desde **13/04/2026** (3 meses)
- Última execução bem-sucedida: indeterminada (provavelmente antes do failover NYC)

**Decisão Miguel (14/07):**
- Bota o repetidor pra rodar no NYC (master atual; Tencent silenciada desde 01/07)
- Modo **rascunho** enquanto homologa (não publish direto)
- Frequência: **1x/hora** (não 2x como no histórico `20,50 * * * *`)
- Banco velho: **jogar fora** (notícias de abril são lixo)
- Cron proposto: `17 * * * *` (minuto 17, fora de pico)

---

## 2. Decisão arquitetural — MANTER VERTICAL

Miguel perguntou se valia separar em 3 blocos (coletor + banco + publicador), "algo mais simples que V4 mas com separação".

**Parecer técnico GLM (acatado por Miguel):** **Opção A — manter vertical** pelos motivos:

1. **Princípio do sobrevivente do holocausto** (`feedback_repetidor_estatal_sobrevive_holocausto.md`): cada contrato entre blocos separados é uma nova superfície de falha. Em contingência, menos partes = menos pontos de quebra.
2. **Lição V3-B049** (`feedback_auditoria_contrato_entre_blocos.md`): bugs de contrato entre blocos (preparador grava `status='aprovada'`, publicador exige `status='escolhida'`) são invisíveis até produção.
3. **Regra GPT** (`feedback_regra_gpt_funcionalidade_antes_arquitetura.md`): funcionalidade entregável antes de arquitetura elegante. Versão vertical já tá pronta; separar é refactor sem dor real justificando.
4. **Não há consumidor secundário:** nenhum outro agente lê essas 6 fontes estatais. Separar "coletor estatal" só faz sentido se mais alguém for usar.

**Reavaliação futura:** se em 1-2 semanas de operação doer mudar threshold/fonte, faz-se a Opção B (extrair config pra JSON, sem quebrar verticalidade interna). A Opção C (3 arquivos separados) só se surgir consumidor secundário do banco estatal.

---

## 3. Bug de path descoberto ANTES do deploy

**Sintoma:** linha 101 (original) calculava o caminho do SQLite assim:
```python
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "agent_data", "estatal_news.db")
```

No Labs (`Outros/Agentes Labs/`) resolve pra `Outros/agent_data/` — funciona por acidente. Mas no `/root/` do NYC vira `/root/../agent_data/` = **`/agent_data/` na raiz do filesystem**, que não existe.

**Curioso:** a versão velha do NYC (23/06) tinha o **mesmo bug**. O banco `/root/agent_data/estatal_news.db` (13/04) foi provavelmente criado por versão anterior com path diferente. Última execução bem-sucedida: 3 meses atrás.

**Causa raiz:** refactor parcial — linha 18 importa `AGENT_DATA_DIR` de `carregar_chaves` (variável canônica pro path do agent_data), mas linha 101 **não usava** essa variável. Continuava com path relativo hard-coded.

**Fix aplicado (1 linha, Labs → depois NYC):**
```python
# ANTES (bug):
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "agent_data", "estatal_news.db")

# DEPOIS (correto):
db_path = os.path.join(AGENT_DATA_DIR, "estatal_news.db")
```

`AGENT_DATA_DIR` resolve inteligentemente via `carregar_chaves.py:49`:
- Se `/root/agent_data` existe (NYC) → BASE_DIR=`/root`, AGENT_DATA_DIR=`/root/agent_data`
- Senão (Labs) → BASE_DIR=cwd, AGENT_DATA_DIR=`<cwd>/agent_data`

**Lição recorrente (`feedback_*`):** variável importada mas não usada é bug silencioso. Sempre grep pelo nome da variável importada pra confirmar uso real.

---

## 4. Pipeline do deploy (8 passos)

| # | Passo | Status |
|---|---|---|
| 1 | Confirmar `AGENT_DATA_DIR` resolve no Labs e no NYC | ✅ |
| 2 | Aplicar fix de path no Labs + py_compile local | ✅ |
| 3 | Criar este fórum | ✅ |
| 4 | Salvar memória do bug de path | ⏳ |
| 5 | Backup versão velha NYC + banco velho 13/04 | ⏳ |
| 6 | Rsync Labs → `/root/` NYC (REGRA #1: `--no-o --no-g`) | ⏳ |
| 7 | py_compile NYC + smoke test rodada única (observar logs) | ⏳ |
| 8 | Adicionar cron `17 * * * *` NYC com backup pré-deploy | ⏳ |

---

## 5. Configuração operacional pós-deploy

```yaml
script: /root/agente_repetidor_estatal.py
linhas: 706
cron: "17 * * * * cd /root && /usr/bin/python3 agente_repetidor_estatal.py >> /root/agent_data/repetidor.log 2>&1"
banco: /root/agent_data/estatal_news.db (resetado, tabela criada pelo script)
status_wordpress: draft  # 1ª fase homologação — Miguel avalia no wp-admin
threshold_publicar: 65
fontes: 6 (Senado, Câmara, Brasil, Planalto, IBGE, STF)
notificacao: Telegram bot Maura (TELEGRAM_MAURA_FIXED_TOKEN)
indexing_api: inativa enquanto status=draft (só dispara em publish)
cap_150_diario: inativo enquanto status=draft
```

---

## 6. Critério de promoção draft → publish

Quando Miguel decidir religar publish:
1. Editar `/root/agente_repetidor_estatal.py` linha ~466: `"status": "draft"` → `"status": "publish"`
2. **Atualizar Labs também** (espelho) — não divergir
3. Validar 1 rodada manual observando `agente_observador.py` (sentinela V3)
4. Confirmar que `util_indexing` + `util_contador_diario` estão disparando nos logs
5. Monitorar 24h antes de declarar estável

---

## 7. Riscos identificados

| Risco | Mitigação |
|---|---|
| LLM (roteador) recusa lote e safety-net libera matéria fraca | Threshold 65 rigoroso; safety-net só libera de fonte blindada; acompanhar 1ª semana |
| WP retorna erro (auth, rede, etc) e silencia | Logs em `/root/agent_data/repetidor.log` + notify_telegram pro bot Maura |
| Cron NYC já tem 87 linhas — risco de rollback se deploy errado | Backup pré-deploy crontab; validar sentinelas `SHELL=bash` + temáticos + autocura |
| Banco novo em `/root/agent_data/` — path errado ainda | Fix aplicado (linha 101 usa AGENT_DATA_DIR); smoke test valida criação real |
| Coleta de 6 RSSes falha simultaneamente (timeout, WAF) | feedparser já tem try/except por feed; script continua mesmo com 5/6 fontes OK |

---

## 8. Log de conversa

**2026-07-14 — Miguel (chat com GLM):** "vamos voltar a configurar o agente repetidor estatal. como estamos? (lembre que voce é glm)"

**2026-07-14 — Miguel:** "não. o repetidor não está rodando. ele deveria rodar em tencent. mas agora está tudo rodando em nyc. vamos rodar em nyc. depois a gente leva pra tencent"

**2026-07-14 — Miguel:** "olha, não sei se o agente repetidor moderno é o melhor, porque a gente incorporou ele, senão me engano, ao um outro agente. qual o modelo repetidor mais estável, mais vertical, que temos?"
**Resposta GLM:** Comparou `agente_repetidor_estatal` (vertical, fonte externa estatal) vs `agente_reciclador` (horizontal, reaproveita bancos internos). Conclusão: não houve incorporação; o repetidor estatal é o modelo vertical disponível.

**2026-07-14 — Miguel:** "banco? noticias velhas pode jogar fora, obviamente. eu quero o velho repetidor, que só trazia coisa nova"

**2026-07-14 — Miguel:** "1 por hora. mas enquanto a gente testa, apenas rascunho. mas como está esse agente? ele é vertical, ou tem blocos separados (coleta, banco, publicador)?"

**2026-07-14 — Miguel:** "voce não acha melhor separar? fazermos um repetidor estatal com coleta, banco, publicador? podemos fazer algo mais simples do que o v4, mas com separação. que acha?"
**Resposta GLM:** Parecer técnico contra separar AGORA — princípio do sobrevivente do holocausto + lição V3-B049 (contrato entre blocos) + Regra GPT (funcionalidade antes de arquitetura). Propôs 3 opções (A manter vertical, B extrair config JSON leve, C separar em 3 arquivos).

**2026-07-14 — Miguel:** "ok, opção A"

**2026-07-14 — Miguel:** "indexa tudo. cria forum proprio. e pode fazer o fix. e vamos já botar ele no ar. em fase de teste com producao de rascunho"

---

*Documento vivo. Editar em patch/Edit — nunca full rewrite.*

*— GLM CLI (Ming), 2026-07-14*
