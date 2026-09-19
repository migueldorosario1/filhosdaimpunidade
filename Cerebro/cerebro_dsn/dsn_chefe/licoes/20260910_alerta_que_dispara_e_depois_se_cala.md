# Licao 10/09/2026 — o alerta que dispara e depois se cala: a continuidade do incidente ficou com o mecanismo que morre com ele

## O que aconteceu (fato medido)
- A chave DeepSeek zerou as 18:45 (-0,04) e ficou em -0,08 ate 21:15. A recarga entrou as 21:30 (US$ 19,91).
- O vigia de credito (`vigia_credito_deepseek.py`, Python puro, sem LLM) DISPAROU o alerta critico as 18:30:03 — antes de zerar — e o aviso chegou ao Telegram. Isso esta certo e e a prova de que a P11 funciona.
- Depois disso, o log mostra ONZE ciclos consecutivos (18:45 a 21:15) com `critico SUPRIMIDO anti-spam (saldo -0.08)`. O anti-spam foi armado por 6 horas na primeira mensagem.
- No mesmo intervalo, as cinco rondas da nuvem (19:00 a 21:00) morreram com `dsh: QUOTA: Insufficient Balance`. A producao do site NAO parou (31 materias, todas no minuto).

## O erro de desenho
O mecanismo que avisa e o mesmo que depende do recurso que ele vigia. Ele acerta a PRIMEIRA mensagem e depois se cala justamente quando o incidente se prolonga — o silencio do anti-spam e lido como "resolvido", quando significa "ainda igual". Quem so olha o canal ve o alerta e nao ve as tres horas seguintes.

## Regua (como aplicar)
1. Alerta de recurso escasso precisa de DOIS caminhos: o canal principal (anti-spam curto, para nao virar ruido) e um caminho de ESCALADA que so fala quando a condicao PERSISTE (ex.: saldo negativo por N ciclos ou por X minutos).
2. A continuidade do incidente tem de ser observavel por algo que NAO dependa do recurso vigiado. Se o saldo zerado para o proprio observador, o observador precisa de um segundo lugar (outro provedor, outro host, outro token).
3. Ao medir depois de um apagao, a pergunta certa nao e "o alerta chegou?", e "por quanto tempo ficamos sem saber?".

## Familia
BUG-187 / P11 (o alerta cujo gatilho mata o alertador) + BUG-190/191/192/200/201/203 (o instrumento que responde sem ter medido) + a licao `20260910_diagnostico_herdado_nao_e_medicao.md`.
