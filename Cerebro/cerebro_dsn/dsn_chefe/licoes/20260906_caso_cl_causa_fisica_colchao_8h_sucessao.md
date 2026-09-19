# Lição 06/09/2026 — CASO CL encerrado com causa FÍSICA + REGRA DO COLCHÃO DE 8H + ordem definitiva de sucessão

Data: 2026-09-06 · Autor: DS Nuvem Chefe (DS-N Chefe) · Ronda 229ª (slot 07:30)

## O quê

1. O CASO CL (06/09, ausência de publicação 00:14→07:15, ~8h30 sem posts) foi ENCERRADO com causa raiz FÍSICA: queda de energia na máquina da Laura por MAU CONTATO NA TOMADA (dito pelo Miguel ~07:2x; confirmado pela própria CL no CL-20260906-001: fora de 00:14 a 07:15). NÃO houve falha de software — a esteira, os vigias e os demais publicadores rodaram a noite toda. Publicação restaurada: 269178 no ar 07:18; mutirão ordenado pelo Miguel (CL publica o acumulado, um por vez, intervalo 15 min).

2. REGRA NOVA DO DONO — REGRA DO COLCHÃO DE 8H: o publicador ativo mantém SEMPRE programação future ≥ 8 horas à frente (mín. 2-3 posts agendados cobrindo a madrugada/próximas 8h); o WordPress publica agendado SOZINHO (wp-cron da hospedagem, independe do computador do publicador). Ronda de fechamento do publicador: repor o colchão antes de encerrar (ritual fixo). Vigia (eu): conferir na ronda se existe future ≥ 8h; abaixo disso = ALERTA.

3. ORDEM DEFINITIVA DE SUCESSÃO (IDEIA-019, adendo do dono): 0º Miguel (se on-line) · 1º substituto = CLOUD MIGUEL · 2º substituto = ZM (AGY-LAURA SAIU do 1º lugar). Gatilho automático: 1ª janela de 3h sem post = alerta; 2ª consecutiva = sucessão ativa sozinha. Retorno do titular: reassume, substituto vira sombra 1 ronda. Ativação de HOJE foi CANCELADA (causa era física; CL voltou). Desenho final: DS-N Ideias (bloco 019).

4. AGY-LAURA: pausa de ~33h (AL-628 04/09 → AL-629 06/09 07:22) teve a MESMA causa física (máquina/energia); processo reiniciado ~07:16. Pergunta do Miguel "AGY operacional?" → SIM, com AL-629 como prova.

## Por quê

- A queda mais longa de publicação da série (~8h30) veio de infraestrutura FÍSICA (uma tomada), não de lógica de esteira nem de LLM. Vigia que presume "agente sumiu = bug" erra o diagnóstico (aqui: 9 janelas de 3h vazias contadas como um único evento de publicador ausente — correto — mas a CURA não estava no software).
- O WordPress publica agendados sozinho: se houvesse colchão, a madrugada teria saído posts MESMO com a Laura fora. Colchão = 1ª linha de defesa (automática); sucessão = 2ª (assume em 2 janelas de 3h). Somadas: queda de publicador nunca mais zera o site.
- O failover da Baleia (ed. 36 manhã enviada 07:07 com a CL fora, formato audiência) funcionou de ponta a ponta — a editoria titular (eu) não depende do gate noturno da CL.

## Como aplicar

1. **Vigia (ronda):** conferir o COLCHÃO — future ≥ 8h no espelho; abaixo = ALERTA na ronda (item 5b do bloco). Método atual: future conferido pelos blocos dos publicadores (CL lista os futures; AL traz esteira_future) porque meu sandbox NÃO tem credencial REST de escrita/leitura de future — MELHORIA proposta: ZM/DSH-us65 instalar sonda REST autenticada (status=future) para o vigia consultar sozinho.
2. **Fechamento da CL (ritual novo):** repor colchão ≥ 8h (2-3 posts) antes de encerrar sessão; vigia noturno confere.
3. **Gatilho de sucessão (quando o plano 019 do Ideias fechar):** 1ª janela 3h = alerta meu; 2ª = ativar 1º substituto (Cloud Miguel), senão ZM; posts assinados "sucessão ativa"; CL volta → sombra 1 ronda → reassume.
4. **Sugestão técnica ao Miguel (próxima conversa):** nobreak/tomada fixa para o computador da Laura (a queda de 8h30 veio de um mau contato).
5. Não arquivar o CASO CL como "bug de esteira": registrar como INCIDENTE-1154 mantido (série zero recuo intacta — o hiato foi infra física, não recuo da série).

Referências: relays DSH-us65 06/09 (IDEIA-019 · cancelamento · colchão) · CL-20260906-001 (de_laura.md) · ZM 50ª · AL-629 · bloco DS-N-20260906-229.
