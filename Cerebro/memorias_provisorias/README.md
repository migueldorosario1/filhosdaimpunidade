# Memórias Provisórias — Regra §90 Cérebro

> **Cérebro canônico:** `/home/migueldorosario/Downloads/Antigravity Google/Cerebro/` — ver [00_CEREBRO_CANONICO.md](../00_CEREBRO_CANONICO.md)
> **Despertar leve (ler primeiro):** [INDICE_DESPERTAR_LEVE.md](./INDICE_DESPERTAR_LEVE.md) → `despertar_leve_<agente>.md`

> **Cada agente da Trindade mantém aqui sua memória provisória de 3 horas.**
> Entradas com mais de 3h são movidas pelo próprio agente para `Backups/memorias_provisorias/`.

## Regras

1. **Janela:** 3 horas. Tudo mais antigo → backup automático
2. **Um arquivo por agente:** `memoria_{agente}_viva.md`
3. **Formato:** timestamp + ação + resultado + ponteiro pro fórum/canal
4. **Quem escreve:** cada agente escreve SOMENTE no seu arquivo
5. **Backup:** `Backups/memorias_provisorias/memoria_{agente}_YYYYMMDD_HHMM.md`
6. **Maestro:** memória fica na raiz do projeto (`memoria_maestro_viva.md`) por ser o índice central

## Agentes obrigatórios

| Agente | Despertar leve | Memória viva |
|--------|----------------|--------------|
| Claude Maestro | `despertar_leve_claude.md` | `memoria_maestro_viva.md` |
| Codex | `despertar_leve_codex.md` | `memoria_codex_viva.md` |
| DeepSeek | `despertar_leve_deepseek.md` | `memoria_deepseek_viva.md` |
| Kimi | `despertar_leve_kimi.md` | `memoria_kimi_viva.md` |
| GLM | `despertar_leve_glm.md` | `memoria_glm_viva.md` |
| Qwen | `despertar_leve_qwen.md` | `memoria_qwen_viva.md` |
| Grok | `despertar_leve_grok.md` | `memoria_grok_viva.md` |
| Antigravity | `despertar_leve_antigravity.md` | `memoria_antigravity_viva.md` |
| AGY | `despertar_leve_agy.md` | `memoria_agy_viva.md` |
| Kilo | `despertar_leve_kilo.md` | `memoria_kilo_viva.md` |

## Rotina de backup

Ao iniciar sessão, cada agente:
1. Lê seu `memoria_*_viva.md`
2. Move entradas com >3h para `Backups/memorias_provisorias/memoria_{agente}_YYYYMMDD_HHMM.md`
3. Mantém no arquivo vivo só o que é recente

O Maestro pode ler TODAS as memórias provisórias para coordenar.
