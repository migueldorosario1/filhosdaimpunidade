---
name: Fix agente_performance servidor desatualizado — 2026-04-20
description: Cópia Cingapura ainda chamava load_dotenv() sem import; local já usava carregar_chaves. Deploy restaurou Maestro GA4. google-analytics-data já estava instalado.
type: project
originSessionId: ce520e95-41e3-4a15-9648-a544b965e78a
---
**Deployado 2026-04-20 ~16:10 BRT em Cingapura.**

## Sintoma
`performance.log` com tracebacks duplos: `ModuleNotFoundError: google.analytics` + `NameError: load_dotenv`. Idêntico ao bug histórico de `agente_observador` (memória `fix_observador_dotenv_20260417.md`).

## Causa raiz
Mesma pegadinha: versão local já tinha migrado pra `import carregar_chaves` (linha 12), mas cópia servidor ainda tinha `from dotenv import load_dotenv` antigo. Não sabíamos quando foi a divergência. `google-analytics-data` já estava instalado — o traceback `No module named google.analytics` era **histórico antigo** no log, não atual.

## Fix
- `rsync -rlptvz --no-o --no-g --checksum` da versão local pro `/tmp/` do servidor.
- `sudo cp /root/agente_performance.py /root/agente_performance.py.bak_pre_redeploy_20260420`.
- `sudo mv /tmp/agente_performance.py /root/ && sudo chown root:root`.
- md5 final: `73ae9fa98efb0663657dc390df94ce40`.

## Validação
Rodou manual no servidor e listou TOP POSTS do GA4 (18 títulos reais com views entre 4046 e 106120). Escreveu em `/root/agent_data/performance_weights.json` (6756 bytes, 16:13 BRT). Maestro lê desse path via `AGENT_DATA_DIR` em `maestro_editorial.py:23`.

## Arquivo órfão detectado (não impacta)
`/root/performance_weights.json` (path raiz, 8 dias atrás, 13/04) existe mas **não é lido pelo Maestro**. Legacy — pode apagar numa limpeza futura.

## Lição
Sempre que ver `ModuleNotFoundError: dotenv` em log, suspeitar de cópia desatualizada antes de qualquer coisa. Template de verificação: `grep -n 'from dotenv\|import carregar_chaves' /root/<arquivo>.py`.
