#!/usr/bin/env python3
"""
Consolida críticas ao worker V4 dos JSONL de bugs em arquivo MD legível.
Rodar: python3 consolidar_criticas.py
Saída: sugestoes_prompt_worker_v4.md
"""
import json, glob, os
from datetime import datetime
from collections import defaultdict

BUGS_GLOB = "/home/migueldorosario/Downloads/Antigravity Google/Cerebro/monitoramento_horario/bugs_encontrados/bugs_*.jsonl"
OUT = "/home/migueldorosario/Downloads/Antigravity Google/Cerebro/monitoramento_horario/criticas_worker_v4/sugestoes_prompt_worker_v4.md"

# Extrair TODAS as críticas dos JSONL
criticas = []
for path in sorted(glob.glob(BUGS_GLOB)):
    with open(path) as f:
        for linha in f:
            try:
                d = json.loads(linha)
                if isinstance(d.get("critica_worker_v4"), dict):
                    c = d["critica_worker_v4"]
                    c["_ts"] = d.get("ts", "")
                    c["_post_id"] = d.get("draft_id") or d.get("article_id") or "-"
                    c["_vertical"] = d.get("vertical", "-")
                    criticas.append(c)
            except Exception:
                continue

# Agrupar por categoria
por_categoria = defaultdict(list)
for c in criticas:
    por_categoria[c.get("categoria", "outros")].append(c)

# Contar recorrências
recorrencias = {cat: len(cs) for cat, cs in por_categoria.items()}
ordem = sorted(recorrencias.items(), key=lambda x: -x[1])

# Gerar MD
now = datetime.now().strftime("%Y-%m-%d %H:%M BRT")
lines = [
    "# Sugestões de prompt pro worker V4 — consolidado do Claude",
    "",
    f"**Última atualização:** {now}",
    f"**Total de críticas registradas:** {len(criticas)}",
    f"**Categorias distintas:** {len(por_categoria)}",
    "",
    "**Origem:** este arquivo é gerado automaticamente a partir do campo `critica_worker_v4` embedado nos JSONL de bugs do ciclo Vigília V5 do Claude Code (`Cerebro/monitoramento_horario/bugs_encontrados/bugs_*.jsonl`). Cada crítica vem de um bug editorial que o Claude corrigiu manualmente após WebSearch e que teria sido evitado se o worker tivesse aplicado a diretriz sugerida no momento da geração do draft.",
    "",
    "**Como o worker deve usar:** ler este arquivo INTEIRO no início de cada geração de draft. As sugestões abaixo são regras editoriais e factuais que o Cafezinho consolidou. Aplicá-las tende a reduzir taxa de reescrita pelo Claude na 4ª camada.",
    "",
    "---",
    "",
    "## Ranking de categorias por recorrência",
    "",
]
for cat, n in ordem:
    lines.append(f"- **{cat}** — {n} ocorrência(s)")

lines.extend(["", "---", "", "## Sugestões de prompt por categoria", ""])

for cat, n in ordem:
    cs = por_categoria[cat]
    lines.extend([f"### `{cat}` ({n} ocorrência{'s' if n>1 else ''})", ""])
    # Pegar a sugestão mais recente + gravidade
    ultima = cs[-1]
    lines.extend([
        f"**Gravidade:** {ultima.get('gravidade', '?')}",
        f"**Vertical(is) afetada(s):** {', '.join(set(c.get('_vertical','-') for c in cs))}",
        f"**Recorrência esperada:** {ultima.get('recorrencia_esperada', '?')}",
        "",
        f"**Descrição:** {ultima.get('descricao', '')}",
        "",
        f"**Sugestão de prompt:**",
        "",
        f"> {ultima.get('sugestao_prompt', '')}",
        "",
        f"**Casos registrados:**",
    ])
    for c in cs[-5:]:  # últimos 5
        lines.append(f"- {c.get('_ts', '?')[:16]} · post {c['_post_id']} · {c.get('descricao', '')[:150]}")
    lines.extend(["", "---", ""])

lines.extend([
    "",
    "## Nota final pro worker",
    "",
    "Se você (worker V4) processar uma pauta e reconhecer que ela cai em uma das categorias acima, APLIQUE a diretriz correspondente no draft. Isso reduz reescrita futura, custo de LLM, tempo de revisor e melhora a qualidade do que chega ao leitor do Cafezinho.",
    "",
    "Este arquivo é atualizado após cada ciclo de Vigília V5 do Claude quando novas críticas são registradas — atualize sua cópia local (se cacheada) periodicamente.",
])

with open(OUT, "w") as f:
    f.write("\n".join(lines))
print(f"Gerado: {OUT} ({len(criticas)} críticas, {len(por_categoria)} categorias)")
