# 🧠 MEMÓRIA COMUM da Ponte Laura Completa — regras de uso

1. **Todos os agentes LÊEM `memoria_comum.md` (janela de 48h) e, quando precisarem de histórico, `INDEX.md` no preflight de cada ronda/loop** (junto com `de_dell.md`/`de_laura.md`). É o contexto canônico da ponte. Grok Miguel/Laura: ver também `handoff_grok/`.
2. **Novos fatos:** cada agente APPENDA no arquivo da SUA máquina — `fatos_dell.md` (agentes do Dell) ou `fatos_laura.md` (agentes da Laura) — com ref própria (`ZM-`/`CM-`/`XM-` aqui; `ZL-`/`CL-`/`XL-` lá) e 1-3 linhas por fato. Append-only: nunca editar linhas de outros.
3. **Curadoria (desde 06/09/2026, cargo PRESIDENTE — ORDEM_MIGUEL 08:20 via CM-005, fórum de contingência §10):** só o **Presidente titular (Claude Laura)** — ou o suplente em cobertura longa — edita `memoria_comum.md` e `INDEX.md`. O arquivo vivo cobre **48 h** e é rotacionado (snapshot em `backups/`); propostas chegam pela ponte («propor pra memória: <fato>») ou pelos `fatos_*.md`. O ZCode Miguel deixou a curadoria (compilado de 18/08 preservado em `backups/memoria_comum_ARQUIVO_20260906.md`).
4. Discorda de algo no compilado? Escreva a correção em `fatos_` da sua máquina com ref — o curador aplica.
5. Sem valores de segredos, sempre (só caminhos e como testar).


## 📌 Regra nova (PD-2 aprovada pelo Miguel 18/08 ~01:25): toda lição nasce com um GATE

- Toda lição registrada em `fatos_dell.md`/`fatos_laura.md` (e consolidada aqui) deve ter campo `gate:` — o mecanismo automático que FALHA VISIVELMENTE quando a lição é violada (ex.: hora capturada por variável em vez de digitada; comando que recusa prosseguir).
- Lição SEM gate vale 7 dias e é reavaliada.
- **Prova de memória semanal:** a cada semana, 3 lições são sorteadas e cada agente mostra evidência de aplicação (trecho de log/comando).
- Formato de entrada: `[ts] REF · AGENTE: <lição em 1 linha> — gate: <mecanismo> — evidência: <onde provar>`.
