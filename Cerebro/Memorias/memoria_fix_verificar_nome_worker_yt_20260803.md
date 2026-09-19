# MEMÓRIA — Fix placeholders `[[VERIFICAR_NOME]]` no worker YT-Cafezinho (2026-08-03)

**Quem:** Kimi K3 Desktop (ZCode), via gatilho `ponte` + "vai" do Miguel (~15:05 BRT)
**Fórum par (Regra do Tema Duplo):** cartinha `Foruns/cartinhas/cartinha_kimi_claude_fix_verificar_nome_bc_deployado_20260803_1525.md` (+ cartinha-origem do Claude `..._bug_placeholder_verificar_nome_worker_yt_20260803_1220.md`)
**Bug node:** `CEREBRO_NODE_BUGS_RESOLVIDOS.md` ← BUG-20260803-YT-VERIFICAR-NOME-PUBLICO

---

## 1. Sintoma (reportado pelo Claude, Vigília V5)

Posts do pipeline YT-Cafezinho (autor 5786, cat 2403, sem `zizi_job_id`) indo a público com placeholders literais `<p>[[VERIFICAR_NOME: X]]</p>` no corpo. Casos:

- **264104** (02/08 15:12) — "A direita importada aperta o cerco no Prata" — markers: `Ruben Lescano` (real: Rubén Ramírez Lezcano), `José António Marcondes` (real: José Antônio Marcondes de Carvalho)
- **264126** (03/08 11:47) — "Lulinha porreta contra o Congresso" — marker: `Nath Boulos` + bug secundário fora de marker: "Drida Lorenzo" (real: Dri Lorenzo)

## 2. Autópsia — as 4 camadas do Bug #33 (25/07) e quem estava vivo

| # | Camada | Onde | Estado em 03/08 |
|---|---|---|---|
| 1 | Prompt instrui emitir marker | `youtube_cafezinho.py` `redigir()` linha 465 | ✅ VIVA — emitia markers |
| 2 | Regra editorial bloqueia publish c/ proposta pendente | `~/ferramentas/sentinela/config/prompts.md` | ❌ morta (Sentinela publish DESATIVADO 27/07 17:15, decisão Miguel) |
| 3 | Guarda determinística regex → ABORT | `~/ferramentas/sentinela/sentinela_ciclo.py:1001-1008` | 💤 **INTACTA mas dormente** — desligada junto com o Sentinela |
| 4 | Checagem dupla downstream | Claude Vigília V5 (cron `17,47` 07-22h + `17` 23-06h) | ⚠️ não conhecia o marker até Claude adicionar regex defensiva em 03/08 |

**Cadeia do acidente:** 27/07 o publish migra do Sentinela pro Vigília V5 → a regex do marker não migra junto → prompt (camada 1) segue emitindo markers com a promessa (agora falsa) de que "Sentinela detecta via regex determinística" → primeiro exercício real do marker pós-migração (264104) vaza. Latência do bug: ~6 dias (27/07 → 02/08).

**Localização de produção (confirmada):** o worker roda **LOCAL** (esta máquina), cron `0 8,14,20` `--rodada`, `--jornal` 22:30/23:00/23:30, `--forum11` 14:30/15:30. Não há cópia em NYC/Tencent/Alibaba/Beijing (verificado via ssh em 03/08).

## 3. Fix deployado (B+C) — diff lógico

Arquivo: `Projeto Cafezinho Agentes/agentes_cafezinho/youtube_cafezinho.py` (29 linhas alteradas)

**B — trava no produtor (NOVA camada 1.5, auto-contida):**
```python
_MARCADOR_VERIFICAR_NOME = re.compile(r"\[\[\s*VERIFICAR_NOME", re.IGNORECASE)

def _tem_marcador_verificar_nome(corpo_html: str) -> bool:
    return bool(_MARCADOR_VERIFICAR_NOME.search(corpo_html or ""))
```
- `publicar_draft()`: `status = "pending" if _tem_marcador_verificar_nome(post["corpo_html"]) else "draft"` + log ⚠️; log de criação reflete status (`PENDING criado:` / `DRAFT criado:`)
- `atualizar_draft()`: se marker no corpo novo, `payload["status"] = "pending"` (sem marker → status intocado, não rebaixa nem promove)
- Regex propositalmente mais frouxa que a do Sentinela (`\[\[VERIFICAR_NOME:\s*([^\]]+)\]\]`): pega malformado, minúsculas, espaços — trava defensiva deve ser mais larga que o formato esperado

**C — raiz no prompt:** instrução de emitir `<p>[[VERIFICAR_NOME: X]]</p>` substituída por 3 rotas: (1) certeza → nome correto; (2) dúvida → REESCREVER omitindo ("o chanceler paraguaio"); (3) `[[...]]` PROIBIDO no corpo. Extração/validação de nomes próprios mantida (parte boa do Bug #33).

## 4. Verificação (smoke 10/10 — WP mockado, zero publicação real)

- Detector: 7/7 variantes (2 markers reais do 264104, minúsculas, espaços, corpo limpo, vazio, None)
- `publicar_draft` com marker → payload `status=pending` ✅; sem marker → `draft` ✅
- `atualizar_draft` com marker → `status=pending` ✅; sem marker → sem chave status ✅
- Prompt: instrução antiga ausente; instrução de omissão/abo lição presente ✅
- `py_compile` OK

**SHAs:** backup pré-edit `youtube_cafezinho.py.bak_pre_kimi_fix_verificar_nome_20260803_1510` = `3b38f3fcd350a3fb0049e6b47d21837b3d03a1922b7821869a0f7ca63899fd5f` · arquivo final = `06777e666f3c365342f8861064ab2e26b895d027c046a2c4f487710f401c1a88`
**Rollback:** `cp youtube_cafezinho.py.bak_pre_kimi_fix_verificar_nome_20260803_1510 youtube_cafezinho.py`

## 5. Lições (candidatas a regra viva)

1. **Trava de segurança mora no produtor, não no fiscal** — o worker é pré-condição do post; o checador pode ser desligado/trocado silenciosamente.
2. **Prompt não deve prometer infraestrutura** ("o Sentinela detecta...") — a promessa expira sem alarme quando a infra muda.
3. **Marker sem consumidor é lixo público potencial** — sinal de incerteza só vale com consumidor determinístico; sem ele, omissão elegante é mais segura.
4. **Desligamento de componente exige checklist de órfãos** — auditar as guardas que o componente carregava e migrá-las (a regex deveria ter ido pro Vigília V5 em 27/07).

## 6. Pendências / monitoramento

- Claude mantém regex defensiva no Vigília V5 como 3ª rede — **se disparar depois de 03/08, há outro produtor emitindo marker** → pingar Kimi.
- Guarda do Sentinela (`sentinela_ciclo.py:1001-1008`) permanece intacta: se o Sentinela publish for reativado, ela volta a valer (formato compatível).
- Caso 264126 tinha bug secundário ("Drida Lorenzo") FORA de marker — coberto indiretamente pelo fix C (validação obrigatória de nomes mantida no prompt); Vigília segue como rede editorial para grafia.
