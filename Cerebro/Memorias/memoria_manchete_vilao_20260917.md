# 🧠 MEMÓRIA — REGRA DO VILÃO-PESSOA NA MANCHETE — 17/09/2026

Irmã do fórum `Foruns/forum_manchete_vilao_20260917.md`. Registro técnico.

## Mecanismo da manchete (mapeado nesta sessão)

1. **Agente (NYC, `/root/agente_manchete.py`, cron `0 */2` UTC):** busca posts 24h → score (views GA4 hoje + 0,3×ontem + bônus recência + james 1M) → juiz LLM de alinhamento editorial (exige nota 5) → aplica via `POST /wp-json/cafezinho/v1/set-manchete` (plugin hello-highlight) + cats Redação/5087 + purge Rocket.
2. **Gate da renderização (WP `mu-plugins/cafezinho-real-image-gate.php`, função `cafezinho_get_real_highlight('Manchete')` no `front-page.php`):** manual válido (capa verificada + fora No Home + régua nacional 08-22h) prevalece; senão fallback = 60 recentes → filtro capa verificada → coroa o 1º.
3. **Causa da manchete chata (271567 "Fila de processos"):** fallback coroava "mais recente com capa" SEM critério de pessoa; post institucional de madrugada segurava a vaga porque os mais novos não tinham capa verificada/régua.

## Régua nova (ordem Miguel 17/09 ~09:5x: "vilão tem que ser PESSOA")

- **Detecção (`titulo_tem_vilao_pessoa` / `cafezinho_titulo_tem_vilao_pessoa`):** (a) lista viva de protagonistas no título (Lula, Bolsonaro, Flávio, Dino, Trump, Putin, Ciro, Elmano, Moraes, Gilmar, Fachin, Vorcaro, Tarcísio, Padilha, Zanin, Maduro, Netanyahu, Milei, Macron, Scholz, Biden, Boulos, Marçal, Datena, Temer, Alexandre, Michelle, Kim Jong, Xi Jinping, Haddad, Tebet, Alckmin, Gleisi, Randolfe, Deltan, Moro); (b) regex de par capitalizado (`[A-ZÀ-Ý][a-zà-ÿ]+(\s+(de|da|do|dos|das|e )?[A-ZÀ-Ý][a-zà-ÿ]+)+`) EXCETO denylist de instituições (supremo tribunal, banco central, congresso nacional, ministério..., polícia federal etc.) e EXCETO par no INÍCIO do título (nome de obra/empresa — caso "Feito Pipa", filme). Listas IDÊNTICAS em PHP e Python (mantê-las gêmeas ao editar).
- **Gate:** `cafezinho_ordenar_por_vilao_pessoa()` (usort estável, pessoa=1 primeiro, data preservada no grupo) aplicada no fallback com selo e no degrau sem-selo (top-12). Manual HUMANO intocável (só o agente e o fallback seguem a régua).
- **Agente:** score +500 com pessoa / −300 sem; campo `vilao_pessoa` no ranking; prompt do juiz ganhou REGRA DO VILÃO (institucional sem pessoa = máximo 4, nunca 5).

## Prova de produção (17/09 ~12:32 UTC)

Agente elegeu 271351 "Lula×Flávio Bolsonaro" (528,4 — bonus vilão visível) → manual não passou na validação do gate → **fallback com régua nova coroou 271566 "Decisão de Dino leva centrão a mirar fim do foro especial"** — curl da home confirma. A institucional 271567 saiu. Testes: Python 9/9 (filme e STF sem falso positivo); WP com IDs reais true/false/false/true.

## Rolagem/rollback

Backups: `cafezinho-real-image-gate.php.bak_pre_vilao_20260917` (WP) e `agente_manchete.py.bak_pre_vilao_20260917` (NYC). Restaurar = rollback; rocket_clean_home após restaurar o gate. Nota: aviso Telegram do agente morre no proxy IPRoyal 402 (pré-existente, não crítico).

— ZCode/GLM-5.3 (ZM, Dell) · 17/09/2026
