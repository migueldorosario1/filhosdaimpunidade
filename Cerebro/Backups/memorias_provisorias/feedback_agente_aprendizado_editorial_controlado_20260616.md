# Feedback — Agente de Aprendizado Editorial Controlado

Data: 2026-06-16  
Origem: Miguel + Codex  
Forum: `Projeto Cafezinho Agentes/Foruns/forum_agente_aprendizado_editorial_controlado_20260616.md`

Miguel pediu estudar um agente capaz de usar os relatorios de qualidade, diretrizes, monitoramento humano, auditor de titulos e ticks do Claude Daemon para melhorar diretrizes editoriais, prompts e demais pontos que afetam a qualidade dos posts.

Diretriz central: o agente deve aprender com os sinais, mas nao pode transformar diagnostico em regra dura nem aplicar mudancas sozinho na fase inicial. Miguel esclareceu que o objetivo de longo prazo e automatizar tambem o processo de melhoria editorial, desde que isso amadureca por fases e com gates fortes. A arquitetura recomendada e um agente de aprendizado editorial controlado:

- primeira fase read-only;
- propostas com evidencia;
- diffs candidatos separados;
- simulacao antes/depois;
- autorizacao humana/Daemon antes de qualquer deploy;
- rollback e medicao pos-mudanca;
- websearch obrigatorio quando envolver fato, fonte, cargo, data, imagem ou identidade.

Meta evolutiva: read-only -> propostas -> diffs candidatos -> simulacao -> deploy supervisionado -> automacao restrita de baixo risco -> automacao assistida de patches seguros.

O Legado passa a ser tratado como sistema canonico de producao. A Reforma pode servir como laboratorio, mas o agente de aprendizado deve proteger o Legado contra alteracoes automaticas mal calibradas.
