# 📜 CONTRATO DE TRABALHO — LIVRO "FILHOS DA IMPUNIDADE"

**Versão 1.0 · 25/07/2026 · Aprovado pelo Miguel.**
Toda sessão de trabalho no livro começa lendo este contrato. Depois dele, ler `Kimi K3/MANUAL_DE_ESTILO.md` e `Kimi K3/REFERENCIA_LITERARIA.md`.

## §1. O projeto
Livro de Miguel do Rosário em 2 volumes: Vol. 1 "O Foragido" (Eduardo Bolsonaro, 240 mil caracteres, prazo 05/08/2026) e Vol. 2 "O Malandro" (Flávio Bolsonaro). Arquitetura oficial: `Claude/ESQUEMA_V2_O_FORAGIDO_INVERTIDO.md`.

## §2. Os papéis
| Papel | Agente | Função |
|---|---|---|
| **Autor e palavra final** | **Miguel** | Voz, estilo, decisões, aprovação de cada capítulo. Sua palavra é final sobre TUDO |
| **Líder editorial (maestro)** | **ZCode/Kimi (computador)** | Integra arquivos, roda o auditor, faz git/backups/espelhos, mantém contrato e manifesto |
| **Arquiteto editorial** | **Claude** | Estrutura de capítulos, teses, depuração (autor do esquema V2 com o Miguel) |
| **Pesquisador-verificador** | **ChatGPT** | Varreduras web, documentos primários, fact-check com busca real. **Também escreve/revisa sob delegação do Miguel** (ex.: v4.5, regras #19–#21) |
| **Interface de bolso do autor** | **Kimi (celular)** | Revisões e aprovações rápidas do Miguel em qualquer lugar |
| **Agente local** | **Antigravity** | Trabalha no espelho local da máquina; sobe via ZCode/Kimi ou push próprio |

## §3. Fonte da verdade e espelhos
1. **Cânone:** `github.com/migueldorosario1/filhosdaimpunidade` (branch main) — a única fonte da verdade.
2. **Espelho local:** `~/Downloads/Antigravity Google/Outros/novo livro/` (onde o Antigravity trabalha).
3. **Espelho Drive:** `gdrive:novo livro` (onde o Claude trabalha).
4. **Fluxo de sincronia:** GitHub ←→ local (ZCode/Kimi, git pull/push) · GitHub → Drive (rclone diário 04:30) · Drive (Claude) → GitHub (ZCode/Kimi puxa e integra).
5. **Regra do multiagente:** SEMPRE `git pull` antes de escrever e antes de `git push`.

## §4. Cânone de estilo (leitura obrigatória antes de escrever)
`MANUAL_DE_ESTILO.md` (regras do Miguel #1–#21) + `REFERENCIA_LITERARIA.md` (voz: ~20 palavras/frase, cadência longa→mais longa→metade, adjetivo raro, ironia por justaposição e detalhe, nunca por epíteto). Protocolo de prova: fato oficial/reportagem/alegação/defesa separados pelo verbo; "foragido" é título editorial, não status processual.

## §5. Quem escreve primeiro
Rascunho com ZCode/Kimi, salvo capítulo delegado pelo Miguel a outro agente (registrar a delegação no MANIFESTO).

## §6. Conflitos
- **De fato:** decide a fonte primária. Em empate, decide o Miguel.
- **De estilo:** decide o MANUAL_DE_ESTILO. Em lacuna, decide o Miguel — e a decisão vira regra nova do manual, datada e numerada.

## §7. Versões (nada se perde)
Toda alteração relevante gera snapshot em `Kimi K3/versoes/` com nome `capNN_vX.Y_AAAAMMDD_HHMM.md`. Antes de publicar, rodar `verifica_estilo.py` e corrigir os alertas.

## §8. MANIFESTO (obrigatório)
**Toda mudança é anotada em `Kimi K3/MANIFESTO.md` ANTES do commit:** quem fez, o quê, onde, quando (entrada nova no topo). Commit sem manifesto não vale.

## §9. Proibições
1. Sobrescrever arquivo de outro agente sem aviso prévio (avisar no fórum do repo).
2. Publicar texto sem passar pelo auditor de estilo.
3. Colar chaves, tokens ou senhas em qualquer arquivo ou chat — o repo é público.
4. Escrever fora dos canais de sincronia (§3) — nada de cópias paralelas soltas.

## §10. Experimentos
Versões experimentais (teste de voz, alternativas de capítulo) vão para `Kimi K3/` com nome `capNN_experimental_<agente>.md` e entram no manifesto como "experimental". O Miguel decide se incorporam algo à versão oficial.

---
*Contrato vivo: mudanças só pelo Miguel, registradas aqui com data.*
