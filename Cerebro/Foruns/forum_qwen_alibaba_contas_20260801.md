# FÓRUM — Qwen/Alibaba: contas, assinatura, Vision API e Prometheus (01/08/2026)

**Data:** 2026-08-01 ~14:00 BRT · Kimi K3 (ZCode), perguntas do Miguel
**Memória irmã (logs de smoke):** `Memorias/memoria_qwen_alibaba_contas_20260801.md`
**Relacionado:** `forum_unificacao_cofre_chaves_20260801.md` (tabela de vencedores)

## Perguntas do Miguel → Respostas provadas ao vivo

### 1. "A conta migueldorosario2@gmail.com funciona?" → ✅ SIM

- `QWEN_API_KEY_2` (`sha8=bcd8a903`, id `migueldorosario2`, endpoint dedicado `ws-aduzgn18hhh3ckpj.ap-southeast-1.maas…`): **qwen-plus HTTP 200 (3,0s)** e **qwen-vl-plus HTTP 200 (1,6s)** — texto E visão vivos hoje.
- Obs.: a chave é **órfã** (só existe no espelho `root/.env.unificado`) → entra no cofre v2 da unificação como fallback oficial do Qwen (já é `role=fallback` no `chaves_api_map.json`).

### 2. "Vale a pena fazer assinatura Qwen?" → **Não, não agora**

- O uso do ecossistema é **API DashScope/Model Studio = pay-as-you-go**, e barato: qwen-plus **$0,26/$0,78** por 1M tok (in/out); qwen-vl-plus ~$0,26/1M — é o **vision mais barato do catálogo** (P5, primário do tribunal visual desde 25/05).
- **Não existe assinatura estilo "ChatGPT Plus" que cubra API** na Alibaba. A assinatura do app Qwen Chat (consumidor) **não** dá direito a API.
- O que existe na nuvem: pacotes pré-pagos de tokens (resource plans, desconto por volume) — só compensa com volume alto e previsível; nosso volume atual não justifica.
- **Prova de hoje: Vision API já funciona sem assinatura nenhuma, nas duas contas (paygo).**
- Ressalva: documentação oficial de billing 404 nesta sessão (4 URLs); se aparecer oferta de pacote no console Billing do Model Studio, reavaliar — critério: desconto > 20% sobre nosso gasto mensal Qwen observado.

### 3. "Assinatura vale para Vision API?" → Pergunta muda de forma: **Vision API já está coberta pelo paygo**

- qwen-vl-plus respondeu "Red." corretamente hoje nas duas contas (smoke PNG 64×64). Vision não exige plano especial — é cobrança por token como texto.

### 4. Drift Qwen RESOLVIDO (unificação)

| Chave | sha8 | Teste 01/08 | Destino |
|---|---|---|---|
| `QWEN_API_KEY` produção (root) | `3af892f5` | ✅ 200 (8,7s) | **VENCEDORA → cofre v2** |
| `QWEN_API_KEY` cofre canônico | `850f5099` | ❌ **HTTP 401 (chave inválida)** | quarentena — provável chave morta/rotacionada (candidata a pertencer à conta legacy) |

### 5. Conta legacy `migueldorosario@gmail.com` (não usa mais) → ações de segurança

- Candidatos a pertencer a ela: a chave morta `850f5099`, a `0a93e3ae` de 17/05 (sumiu dos cofres) e o **`AccessKey.csv` (AK `LTAI…`) guardado em `Cerebro/alibaba/`**.
- ⚠️ **Incidente leve de governança:** AccessKey real salva no Cérebro viola a regra "sem segredos no Cérebro". 
- **Checklist para Miguel no console Alibaba da conta legacy (3 min):** (a) desativar a AccessKey `LTAI…`; (b) revogar API keys de Model Studio da conta; (c) confirmar cobrança zerada; (d) só então eu destruo o `AccessKey.csv` (movendo para quarentena criptografada antes, se preferir lastro).

### 6. "Prometheus na conta aiatolahnews@gmail.com está funcionando?" → **Não consigo provar daqui; evidência local diz que o pipeline está PARADO**

- O exportador local de métricas de chaves (`agent_data/prometheus/chaves_api.prom`) está **congelado desde 22/06 10:47** (40 dias) — último check: qwen 1/1 OK, kimi já falhava na época.
- Se for o **Alibaba Cloud Managed Prometheus (ARMS)** da conta aiatolahnews: não há credencial dessa conta no cofre → verificação real é sua no console (checklist de 2 min: workspace ARMS ativo? remote write com dados recentes? targets up?).
- Ação nossa: Fase 0 da OPERAÇÃO COFRE ÚNICO inclui checar nos servidores o cron do exportador e qualquer `remote_write` para ARMS. Na Fase 4, o cron de auditoria semanal pode **reviver** esse pipeline — se quiser métricas na ARMS da aiatolahnews, preciso da URL de remote write + credencial dessa conta (no cofre v2).

## Decisões pendentes de Miguel

1. Executar checklist da conta legacy (desativar AK) → me autorizar a destruir/quarentenar `AccessKey.csv`.
2. Prometheus/ARMS: quer que o exportador revivido (Fase 4) publique na conta aiatolahnews? Se sim, fornecer remote-write URL + credencial.
3. Resource plan Qwen: só reavaliar se console mostrar desconto > 20% (sem ação agora).
