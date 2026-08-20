# 🧠 Memória — Algoritmo de Velocidade / Gravidade Temporal no Top 10 (Espelho `cafezinho.news`)

> **Data:** 20/08/2026 17:20 BRT · **Autor:** ZCode (Gemini 3.6 Flash / High)
> **Tema Relacionado:** `Foruns/forum_algoritmo_velocidade_top10_espelho_20260820.md`

---

## 📌 Resumo Executivo
Implementação e validação em produção (servidor NYC) do **Algoritmo de Velocidade e Gravidade Temporal ($V_2$)** para o ranking do Top 10 Tendências do portal Espelho (`cafezinho.news`). A mudança atende à ordem direta do Miguel para evitar que matérias antigas "bloqueiem" matérias novas em aceleração.

---

## 🛠️ Detalhes da Alteração Técnica

### File Editado:
- `/root/top_tendencias_push.py` no servidor NYC (`146.190.134.195`).

### Backup Preservado:
- `/root/top_tendencias_push.py.bak_pre_velocidade_20260820`

### Cálculo Matemático Aplicado ($V_2$):
```python
# Janela de cálculo: Postagens publicadas nas últimas 48h
# date_gmt capturada via REST API do WordPress para precisão de segundos

horas_desde_pub = max(0.1, (now - post_date).total_seconds() / 3600.0)
score_velocidade = round(total_views / ((horas_desde_pub + 1.5) ** 1.2), 2)
```

### Arquitetura de Push Duplo:
1. **Payload 1 (`www.ocafezinho.com`):** Mantém ordenação legada por `views_brutas` acumuladas (preserva canônico).
2. **Payload 2 (`cafezinho.news`):** Ordenado por `score_velocidade` decrescente, incluindo campos explicativos no JSON enviado via REST API (`views_per_hour`, `horas_publicado`, `gravity_score`).

---

## 📊 Indicadores de Sucesso no Teste
- **Matérias de 19h–22h de idade** com ~50-100 acessos subiram diretamente para o ranking do Top 10 devido à alta taxa de crescimento proporcional à idade.
- **Matérias de 48h de idade** perderam posições de destaque se não mantiveram tração recente.
- O endpoint REST do Espelho processou a resposta HTTP 200 OK sem erros de validação.

---

## 🔄 Procedimento de Reversão (Rollback)
Caso necessário retornar ao modelo 100% acumulado bruto:
```bash
ssh root@146.190.134.195 "cp /root/top_tendencias_push.py.bak_pre_velocidade_20260820 /root/top_tendencias_push.py && /root/venv/bin/python /root/top_tendencias_push.py"
```
