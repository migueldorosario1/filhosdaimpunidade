# 🤝 ESCUTA CAFEZINHO — comunicação Telegram de todos os agentes com o Miguel

**Ordem do Miguel, 19/08/2026 ~16:30 (voz):** "trabalhar da rua pelo celular, com todos os agentes ligados a mim pelo celular — esse é o meu objetivo conceitual."

## Regras do canal

1. **Bots separados:** a **Baleia Azul** sai pelo bot **CEO Antigravidade** (@cafezinhoantigravitybot). A **ponte cafezinho** (@pontecafezinhobot) é o canal de COMUNICAÇÃO de todos os agentes (escuta + resposta). Nada da Baleia no bot da ponte.
2. **Escuta compartilhada:** o daemon `ponte_cafezinho.py` (no Dell) grava cada mensagem do Miguel em `cerebro-miguel/cerebro/Foruns/ponte_laura_completa/escuta/entrada_<id>.json` e faz push no GitHub — assim os agentes dos dois lados veem.
3. **Quem pega primeiro, responde** (anti-duplicação): ao ver uma entrada nova, o agente reivindica com `pegar(id, meu_agente)` (arquivo atômico `escuta/claims/entrada_<id>.<agente>.claim`). Quem perde a reivindicação **fica atento mas não responde** (evita respostas duplicadas ao Miguel).
4. **Janela de atenção:** depois de uma mensagem, todos ficam atentos **30 min**; se o assunto for importante, **2 horas**; se muito importante, **4 horas** (`escuta/atencao.json`, campo `janela_min`).
5. **Acesso:** todos os agentes têm (ou devem confirmar na ponte) acesso ao Cérebro, ao SSH do Cafezinho, ao GitHub (cerebro-miguel) e aos arquivos de trabalho. O token do bot vive nos cofres (`TELEGRAM_TOKEN_PONTE` nos .env.unificado espelhados) — nunca em chat.
6. **Prioridade:** o Miguel é o principal; quem ouve primeiro ganha a vantagem de responder; o ZCode é o mais importante nas respostas (mais demorado, mas o principal).
7. **Segurança:** operacionalidade primeiro (ordem do Miguel); a grande estratégia de segurança do Cafezinho fica para o final de 2026, com calma.

## Uso para agentes

```python
from ponte_cafezinho_client import tg_send, ler_escuta, pegar, atencao_janela
# arquivo: Downloads/Antigravity Google/ponte_cafezinho/ponte_cafezinho_client.py
for e in ler_escuta():
    if e["status"] == "nova" and pegar(e["id"], "meu-agente"):
        tg_send("🟢 recebi sua mensagem — trabalhando nisso.")
```

**Testificação de acesso (todos assinam na ponte de_laura/de_dell):** Cérebro ✓ · SSH cafezinho ✓ · GitHub ✓ · arquivos de trabalho ✓.
