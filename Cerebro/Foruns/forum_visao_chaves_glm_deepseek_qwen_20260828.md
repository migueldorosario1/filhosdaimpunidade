# 🎯 FÓRUM — Visão por chave: GLM (assinatura) NÃO serve · DeepSeek SERVE e é o mais barato (28/08/2026)

**Criado:** 2026-08-28 ~10:00 BRT · ZCode/DeepSeek · Ordem do Miguel: "vê se a chave do GLM serve pra gente usar como visão no cafezinho... vê se o Jip-Sic [DeepSeek] também serve... vê se são baratos"
**Memória-irmã:** `Memorias/memoria_visao_chaves_glm_deepseek_qwen_20260828.md`

## O que foi pedido

Testar AGORA, com as chaves que o Miguel já tem, se os modelos de **visão** do GLM (assinatura Z.ai) e do DeepSeek servem para o uso do Cafezinho (enxergar personagem, enxergar notícia/capa) e se são baratos. Referência do Miguel: "a chave do Qwen serve" — ou seja, Qwen-VL é o padrão atual.

## Resultado dos testes (tudo ao vivo, 28/08 ~09:50)

| Provedor | Chave | Modelos de visão | Teste real (foto do Lula, capa do post 267802) | Preço |
|---|---|---|---|---|
| **GLM (Z.ai)** | assinatura Coding Plan (sha8 `084efcbd`) + contas `bf908cec` e `151cc374` | `glm-4.5v`/`glm-4.6v` EXISTEM na plataforma | ❌ **429 "Insufficient balance or no resource package"** em TODAS as chaves | GLM-4.6V: US$0,30/0,90 por 1M (in/out) · GLM-4.5V: US$0,60/1,80 |
| **DeepSeek** | saldo pay-as-you-go (sha8 `f0aaa272`, US$ 64,62) | `deepseek-v4-flash-vision-exp` ✅ listado na chave | ✅ **ACERTOU 2/2**: "Luiz Inácio Lula da Silva, Presidente do Brasil" + descrição de cena + aval de capa | US$0,22/0,66 por 1M off-peak (0,44/1,32 peak) · **imagem = máx 384 tokens ≈ US$0,00008 por imagem** |
| **Qwen-VL** (referência atual) | Token Plan | `qwen-vl-plus` ✅ | ⚠️ **errou 1× com prompt longo** (chamou Lula de **Bolsonaro**) · acertou 2/2 com pergunta curta | plano por janela (75M tokens/5h) |

## Decisões / conclusões

1. **Chave do GLM NÃO serve para visão hoje.** As chaves funcionam em texto/coding (10 modelos glm-4.5→glm-5.3-flash, HTTP 200), mas o pacote da assinatura NÃO cobre os modelos de visão (429 de saldo/pacote em todas as 3 contas). Para usar GLM Vision seria preciso **recarregar/contratar pacote** na conta Z.ai.
2. **Chave do DeepSeek SERVE e é a mais barata das opções de visão.** Mesmo saldo já usado no resto do ecossistema. Custo de uma análise completa de capa ≈ US$0,0003 (895 tokens) → ~10 mil análises por US$3. Não tem janela de 5h, só saldo.
3. **Peculiaridade do DeepSeek Vision:** é modelo de raciocínio — gasta ~100–250 `reasoning_tokens` ANTES da resposta. Chamadas precisam de `max_tokens ≥ 300`, senão devolve vazio (aconteceu no teste com teto 60).
4. **Alerta Qwen-VL:** o erro Lula→Bolsonaro aconteceu 1× com prompt longo ("curador visual... 4 perguntas") e não se repetiu com pergunta curta (2/2). Contexto do prompt importa. Recomendação: prompts de identificação diretos e, se possível, dupla-checagem (DeepSeek Vision × Qwen-VL).

## O que está pronto / o que falta / o que preciso de você (Miguel)

- **Pronto:** teste completo ao vivo das 3 opções + preços + registro no Cérebro.
- **Falta:** decisão do Miguel — plugar `deepseek-v4-flash-vision-exp` no pipeline de visão do Cafezinho (auditor visual de capas V4/V4.1, Tribunal Visual) usando a chave DeepSeek já existente.
- **Preciso de você:** (1) "vai" para eu trocar o auditor visual do pipeline para DeepSeek Vision (ou DeepSeek 1º + Qwen como dupla-checagem); (2) se quiser GLM Vision também, recarregar um pacote na conta Z.ai (o plano de assinatura atual não inclui visão).

## ✅ DEPLOY EXECUTADO — 28/08 ~13:40 (Miguel deu "vai")

**O que mudou no NYC** (`/root/v4_labs/codigo/`):

1. **`media_vision_providers.py`** — novo `DeepSeekVisionProvider` (API OpenAI-compatible, `deepseek-v4-flash-vision-exp`, `max_tokens` default 4000 com piso de 300 porque o modelo gasta ~1200 tokens só de raciocínio antes de responder) + `DoubleCheckMediaVisionProvider` (primário DeepSeek; Qwen/Gemini de secundário; divergência em campos críticos ou gap de confiança >0,30 marca `ambiguous_identity=true` e usa a menor confiança — fail-closed).
2. **Factory:** com `DEEPSEEK_API_KEY` no ambiente → **DeepSeek 1º + dupla-checagem Qwen**. Sem a chave → comportamento antigo intacto (Qwen→Gemini). Retrocompatível.
3. **`vision_healthcheck_cli.py`** — cenários cientes de `DEEPSEEK_API_KEY` + imagem PNG real via PIL (a imagem sintética antiga era rejeitada pelo validador do DeepSeek com 400).
4. **Testes:** `test_media_vision_providers.py` estendido — **38/38 OK** (DeepSeek, dupla-checagem, factory).
5. **Healthcheck ao vivo (cofre real):** 7/8 cenários ok — `current_env` = `deepseek_qwen_doublecheck` ✅ (DeepSeek e Qwen concordaram na foto do Lula, confiança 0.95); o único "não ok" é o cenário negativo `no_media_keys` (esperado). Casos `with_invalid_qwen`/`without_qwen` = DeepSeek responde sozinho ✅.
6. **Prova E2E com capa real** (foto Lula do post 267802, via pipeline completo): `entity_present=true`, `identity_confidence=0.95`, bboxes OK, `provider_id=deepseek_qwen_doublecheck`.
7. **Backups de rollback:** `*.bak_pre_deepseek_vision_20260828` no NYC.

**O que falta / o que preciso de você:** nada bloqueante — o pipeline já usa DeepSeek Vision + dupla-checagem a partir do próximo ciclo. Se quiser GLM Vision também, recarregue pacote na conta Z.ai. Custo novo por análise de capa: ~US$0,001–0,002 no DeepSeek (a dupla-checagem Qwen sai do Token Plan).
