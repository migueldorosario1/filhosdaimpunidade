# 🚚 Transporte do `de_dell.md` → repo canônico da ponte (BUG-20260829-DS-023)

**Preparado por:** DS (DeepSeek/DSH, Dell) — ronda 15/15, 29/08/2026 ~11:45 BRT
**Executor necessário:** ZCode/CM (acesso ao repo `~/cerebro-miguel`) **ou** Miguel (aprovação de escalação de sandbox do DS).
**Objetivo:** restaurar a ponte GitHub do lado Dell — `de_dell.md` invisível à Laura desde 28/08 20:17 (~14h).

## Prova de que o transporte é seguro (append-only)

- Cópia de trabalho: `/home/migueldorosario/Downloads/Antigravity Google/Cerebro/Foruns/ponte_laura_completa/de_dell.md` (841 linhas, viva com DS-008..022, INSUMO, enigmas, ZM-001, nomeação da Baleia).
- Canônico da ponte: `/home/migueldorosario/cerebro-miguel/cerebro/Foruns/ponte_laura_completa/de_dell.md` (301 linhas, último commit `82c7bda2` 28/08 20:17).
- `diff` (trabalho × canônico): **540 linhas só na cópia de trabalho, 0 só no canônico** → superconjunto puro; nada se perde.
- Scan de segredos no delta: só MENÇÕES a caminhos (`Outros/chaves/...`, `%USERPROFILE%\.dsh\deepseek_env`), nenhum valor de chave/token.

## ⚠️ Salvaguarda obrigatória (DS-015)

O working tree do `~/cerebro-miguel` tem **itens não rastreados sensíveis** (`Cerebro/Cofres/`, `CEREBRO_NODE_COFRE_CHAVES.md`, `CEREBRO_NODE_CHAVES_E_LLMS.md`, `Outros/chaves/`). **NUNCA `git add -A` / `git add .`.** Usar `git add` por caminho único.

## Comando pronto (rodar de `~/cerebro-miguel`, fora do sandbox do DS)

```bash
cd ~/cerebro-miguel
# 1. backup
cp cerebro/Foruns/ponte_laura_completa/de_dell.md cerebro/Foruns/ponte_laura_completa/de_dell.md.bak_pre_transporte_DS_20260829
# 2. transporte (cópia de trabalho -> canônico)
cp "/home/migueldorosario/Downloads/Antigravity Google/Cerebro/Foruns/ponte_laura_completa/de_dell.md" cerebro/Foruns/ponte_laura_completa/de_dell.md
# 3. add SELETIVO (só o de_dell.md)
git add cerebro/Foruns/ponte_laura_completa/de_dell.md
# 4. revisar o staged antes de commitar (deve ser só o de_dell.md)
git diff --cached --stat
# 5. commit + push
git commit -m "ds: DS-20260829-023 transporte de_dell.md (copia de trabalho -> canonico da ponte) — ponte Dell volta ao GitHub apos ~14h; INSUMO CL-006, enigmas 268209/268201, ZM-001 e nomeacao da Baleia agora visiveis a Laura (ronda 15/15 CEO em treinamento)"
git push origin main
# 6. verificar
git status -sb && git log --oneline -2
```

## Após o transporte (próximas rondas do DS)

1. Confirmar no GitHub que o `de_dell.md` do `cerebro-miguel` contém a DS-023 (prova externa).
2. Reavaliar a solução "b" da DS-021/022: apontar o cron/rotina do DS para escrever direto no repo canônico (evita nova divergência).
3. A memória pessoal (`memorias_provisorias/memoria_ds_ceo_viva.md`, atualizada na ronda 15/15) também precisa de espelho no GitHub — entra no mesmo transporte ou no sync de rotina.
