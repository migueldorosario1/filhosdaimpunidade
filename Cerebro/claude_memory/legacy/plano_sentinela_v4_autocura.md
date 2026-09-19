---
name: Plano Sentinela V4 Autocura (A IMPLEMENTAR)
description: Autocura autônoma com consenso 3/3 LLMs, invariantes de segurança hard-coded, ramp-up de 4 semanas. Aprovado pelo Miguel em 2026-04-18 03h.
type: project
originSessionId: 45d53b87-5aea-4ee1-bde2-cc8f6a6aec6e
---
# CONTEXTO DA DECISÃO (essencial ler antes de codar)

Miguel opera O Cafezinho, que publica **200+ posts/dia** automatizados. A vigilância editorial manual é inviável no volume. Ele quer **autonomia total** do sistema de auditoria pra ter dias livres lendo livro, mas traumatizou 2x com automações paranoicas:

**Incidente 1 (2026-04-18 ~01h):** Sentinela V2 com `gpt-5-search-api` rebaixou 7 posts legítimos em 20s por falsos-positivos de fact-check ("não confirmei na web"). Foi desligado e posts restaurados.

**Incidente 2 (2026-04-17 ~20h):** Corretor Autônomo comentou 26 linhas do crontab (botão de pânico) após falhas de busca Wikimedia. Paralisou a operação inteira. Botão foi desativado.

Conclusão conjunta: automação com LLM é possível se o DESIGN for defensivo. O problema não foi IA, foi arquitetura sem salvaguardas.

Aprovação explícita: "sim, não é problema perder 1 post de vez em quando. ainda mais que o sistema que estamos montando é grande, publica mais de 200 posts por dia as vezes."

---

# ESTADO ATUAL (2026-04-18 03h, funcionando)

**Sentinela V3 (humano-em-loop)** está deployado e rodando. Cron `*/30 * * * *` no Cingapura. Detecta posts com problema via Claude Sonnet + fallback, grava em `/root/agent_data/suspeitos_caetano.json` (não mexe no post), manda alerta ao bot `@caetanoechicobot` no Telegram com 9 botões (Curar/Editar/Outra imagem/Gerar IA/WP/Rebaixar/Deletar/Manter/2ª Opinião). Modo DRIP: 1 alerta por vez, cada ação abre próximo da fila.

Arquivos chave (todos sincronizados Cingapura + local + NYC):
- `/root/agente_observador.py` — Sentinela V3
- `/root/agente_corretor_autonomo.py` — função `curar_post_unico(pid, modelos_excluir)` exposta
- `/root/agente_correcao.py` — Caetano bot V9 com CallbackQueryHandler
- `/root/agente_roteador_llm.py` — com filas novas `auditor_sentinela` (Claude→GPT→Grok→Gemini→Mistral) e `auditor_segunda_opiniao` (Perplexity→GPT-search→Grok→Gemini→Claude)

Bot Caetano processo: iniciar com `sudo bash -c "cd /root && nohup /root/venv/bin/python3 /root/agente_correcao.py > /root/agent_data/agente_correcao_bot.log 2>&1 &"`

Tutorial detalhado em `Outros/passagem/tutorial_sentinela_v3_para_antigravity.md`.

---

# V4 AUTOCURA — INVARIANTES DE SEGURANÇA (HARD-CODED, LLM NÃO PODE BURLAR)

Estas 6 regras devem ser verificações determinísticas no código do próprio V4, em função nomeada `verificar_invariantes()` que **todo ponto de ação** chama antes de agir. Se qualquer invariante falhar, ação é abortada.

1. **Blast radius = 1 post.** Nunca tocar em: crontab, config files, outros agentes, banco SQLite de sistema, .env, processos. Única mutation WP permitida: `POST /posts/{id}` com `{status: draft, featured_media: X, content: Y}`. JAMAIS `DELETE`, jamais `crontab -`, jamais `os.system`.

2. **Consenso 3/3 obrigatório pra AÇÃO.** 3 LLMs de famílias distintas (Anthropic + xAI + Google) devem retornar `status=ERRO` com mesma gravidade. 2/3 ou 1/3 → alerta humano via Sentinela V3 (tipo C).

3. **Circuit breaker.** Arquivo `/root/agent_data/autocura_acoes.json` guarda timestamp de cada ação. Se `len([a for a in acoes if a.timestamp > now-1h]) >= 3`, V4 pausa por 4h. Alerta `"🚨 3 ações em 1h — autocura pausada, revise"`. Reset automático em 4h ou via `/retomar_autocura` no Telegram.

4. **Quarentena de 2h.** Só opera em posts com `date` menor que `now - 2h`. Recém-publicados ficam para o Sentinela V3 humano-em-loop.

5. **Whitelist BR sensível.** Se título contém `Lula`, `STF`, `Congresso`, `Brasil`, `Planalto`, `Senado`, `Câmara`, `PT`, `PSOL`, `governo federal` — EXIGE gravidade `CRITICO` explícita + consenso 3/3. Evita que LLM gringo alucine "não confirmei esse acordo Lula-Espanha".

6. **Nenhum modelo com web search no auditor autônomo.** Proibidos: `gpt-5-search-api`, `perplexity sonar-*`. Permitidos: Claude Sonnet 4.6, Grok 4, Gemini 2.5 Flash. Web search só na `auditor_segunda_opiniao` que é chamada SOB DEMANDA pelo botão do Telegram, nunca autônomo.

---

# AÇÕES PERMITIDAS E REGRAS POR AÇÃO

Só 2 ações possíveis:

**A) Cura cirúrgica (chama `curar_post_unico(pid)` já existente).**
- Aplica-se quando gravidade = `CORRIGIVEL`
- Preserva 100% das palavras, só remove lixo determinístico (metalinguagem, HTML quebrado, citações `([domain](url))`)
- Após cura, **re-audita** com mesmo pipeline de consenso. Se ainda `ERRO` → degrada pra rebaixar.

**B) Rebaixar a draft.**
- Aplica-se quando gravidade = `CRITICO` E consenso 3/3
- Aplica-se após cura falhar 1x (não retenta)
- `POST /posts/{id} {status: draft}` — nada mais

**NÃO permitido sob nenhuma condição:**
- `DELETE /posts/{id}` (nunca lixeira, só humano)
- Editar título, categoria, tags (cirúrgica mexe só no content)
- Trocar featured_media (só Caetano bot via botão humano)
- Tocar em qualquer outro post além do alvo

---

# RAMP-UP DE 4 SEMANAS (OBRIGATÓRIO)

Miguel aprovou começar gradual. Cada semana adiciona 1 categoria ao escopo. Transição só com acurácia ≥ 95% na semana anterior (medido por % de ações NÃO revertidas por Miguel via Telegram).

**Semana 1 (começar primeiro):** apenas **regex puro, ZERO LLM**. Detecta e remove citações cruas `([en.wikipedia.org](https://...?utm_source=openai))`. Padrão: `r'\s*\(\[[^\]]+\]\([^)]+\)\)'`. Zero risco porque é determinístico.

**Semana 2:** adiciona metalinguagem literal via regex. Padrões: `As an AI`, `I cannot`, `I'm sorry`, `como um modelo de linguagem`, `não posso afirmar`, `Aqui está o artigo`, `Peço desculpas`. Remove o parágrafo inteiro que contém o match.

**Semana 3:** adiciona HTML quebrado via BeautifulSoup. Parágrafos vazios, tags abertas sem fechar, `<p></p>` redundantes.

**Semana 4:** adiciona **rebaixamento autônomo** pra títulos placeholder determinísticos: `Sabatina Exclusiva`, `Sabatina em Análise`, `ENTREVISTADO PRINCIPAL`, `Editorial`.

**Semana 5+:** **aí sim entra LLM**. Consenso 3/3 + cura cirúrgica via `curar_post_unico`. Plena operação.

---

# NOTIFICAÇÕES NO TELEGRAM (bot @caetanoechicobot)

**Tipo A — autocura silenciosa (som off):**
```
🔧 Autocurei | HH:MM
"Título do post..."
Removi: "trecho específico"
[🔍 ver diff] [↩️ reverter]
```

**Tipo B — rebaixamento automático (som curto):**
```
📥 Rebaixei a rascunho | HH:MM
"Título..."
motivo: gravidade CRITICO + consenso 3/3
[✅ confirmado] [↩️ republicar]
```

**Tipo C — humano decide (som normal, atual V3):**
```
⚠️ Consenso dividido | HH:MM
Claude/GPT: suspeito, Grok: legítimo
[📝 curar] [📥 rebaixar] [✅ manter]
```

**Resumo diário 08h:** "24h: curei 37, rebaixei 8, humano decidiu 5x. Reversões suas: 1 (97% acurácia)."

**Relatório semanal sexta 14h:** cálculo de acurácia cumulativa pra semana + decisão de ramp-up.

---

# KILL SWITCHES

Comandos no Caetano bot:
- `/pausa_autocura` → flag em `/root/agent_data/autocura_pausada.flag`. V4 verifica arquivo antes de agir. Sentinela V3 continua operando.
- `/silencio_2h` → Tipos A e B vão pra fila, só Tipo C toca. Reset automático em 2h.
- `/retomar_autocura` → remove flag.

Hard switch no código:
```python
SAFE_MODE_DISABLE = False  # Se algum dia quiser matar autocura completa, editar .py manualmente.
```
Nenhum LLM, nenhuma config externa, nenhum comando remoto pode mudar isso. Só `vim agente_autocura.py`.

---

# ARQUIVOS NOVOS A CRIAR

1. `/root/agente_autocura_v4.py` — agente principal, roda via cron (sugestão: a cada 1h pra ter tempo de consenso). Importa `curar_post_unico` e reaproveita filas do roteador.

2. `/root/agent_data/autocura_acoes.json` — log de ações com timestamp + post_id + tipo (cura|rebaixa) + diff + modelos usados.

3. `/root/agent_data/autocura_pausada.flag` — arquivo de flag pra kill switch.

4. Regex patterns centralizados em `/root/autocura_patterns.py` — lista de padrões determinísticos por categoria (openai_citations, metalinguagem, html_quebrado, titulos_placeholder).

---

# INTEGRAÇÃO COM SENTINELA V3 EXISTENTE

V3 NÃO é substituído. Vira o **backstop humano do V4**:
- V4 tenta primeiro. Se consenso 3/3 → age sozinho (Tipo A ou B).
- Se divergência (2/3 ou 1/3) → registra no `suspeitos_caetano.json` como `status=pendente` → Sentinela V3 existente pega no próximo ciclo e alerta humano (Tipo C).
- Mesmo bot Caetano, mesmo menu. Unificação limpa.

No código: V4 roda ANTES do Sentinela V3 na mesma hora. Se V4 já agiu em um post, V3 pula (lê autocura_acoes.json e ignora post_ids recém-processados).

---

# COMPROMISSO DE ENGENHARIA DEFENSIVA

**Ao codar V4 na próxima sessão, estas práticas são obrigatórias:**

1. Função `paralisar_crontab()` do `agente_corretor_autonomo.py` deve ser **deletada** (não só `if False`). Código morto perigoso não pode existir.

2. Todo commit de código V4 deve ter comentário `# INVARIANTE X: razão` em cima de cada check de segurança.

3. Teste seco antes de deploy: rodar V4 com `DRY_RUN=True` (só loga ações, não executa) por 3 rodadas. Miguel confere log. Só depois remove DRY_RUN.

4. Nunca fazer `rsync -a` pra /root de servidor (memória `regra_critica_rsync_nao_usar_a.md`). Sempre `--no-o --no-g --checksum`.

5. Sincronizar NYC só DEPOIS de V4 validado em Cingapura por 48h.

---

# COMO COMEÇAR NA PRÓXIMA SESSÃO

Após Miguel pedir "lê a memória e continua":

1. Ler esta memória + `plano_sentinela_v3_caetano.md` + `regra_critica_rsync_nao_usar_a.md`
2. Verificar estado do V3 + Caetano bot (deveriam estar rodando)
3. Confirmar com Miguel: "tudo como deixamos? posso começar Semana 1 (regex-cura determinístico)?"
4. Se sim: criar `agente_autocura_v4.py` com SÓ a Semana 1 (regex citações OpenAI), `DRY_RUN=True` por default
5. Testar com 10 posts históricos (235984, 236073, etc. que tiveram citações OpenAI). Conferir que detecta e geraria cura correta.
6. Se Miguel aprovar dry-run → remover flag, agendar cron a cada 1h, monitorar 24h.

**Ordem de implementação futura (semanas 2-5): só após Miguel aprovar explicitamente cada upgrade.**
