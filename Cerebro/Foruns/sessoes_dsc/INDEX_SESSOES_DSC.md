# INDEX_SESSOES_DSC — índice das conversas do DS Celular (DSC)

**Mantenedor:** sessão organizadora DSC (`session-d86e89a7`) · **Criado:** 01/09/2026 ~00:50 BRT
**Função:** 1 linha por conversa; caminho estável; robô lê o índice e mergulha só no registro que precisa.
**Fonte da verdade para atualização:** transcripts DSH em `/root/.dsh/sessions/--root-Cerebro--/session-<id>/session.jsonl.zstd` (o DSC organizador re-extrai quando o Miguel pedir "atualiza o registro").

## Regras vivas deste índice
1. **Nome completo, nunca genérico:** nenhum índice novo se chama só "INDEX". Exceção histórica: os `INDEX.md` do Loop Laura permanecem (robôs são instruídos a ler esse caminho).
2. **Tolerância (ordem do Miguel 01/09):** assunto de outro tema na sessão errada → DSC responde mesmo assim + aconselha voltar à sessão do tema + **grava tudo**.
3. **Foto do momento:** registros são snapshot; conversas vivas crescem — atualizar sob ordem.
4. **Destino:** alimentar o **DS Nuvem Memória** (vaga do tema 10) quando nascer.

## Conversas de tema (0–10)
| Tema | Sessão | Registro | Estado | Assunto em 1 linha |
|---|---|---|---|---|
| 0 LIVRE | 4c3a034b | `2026-08-31_tema0_livre_ideias_livros.md` | VIVA | DS-N Ideias a serviço das ideias; livro ORIGENS; editora própria pt/en/es/fr (IDEIA-004, commit f7f941ffe) |
| 1 PLANTÃO → ORGANIZADORA | d86e89a7 | `2026-09-01_tema1_sessao_organizadora_dsc.md` | VIVA | Esteira + ronda leve; promovida a sessão organizadora das conversas DSC |
| 2 REDES SOCIAIS | d127b92b | `2026-08-31_tema2_sprint_redes_sociais.md` | VIVA | Sprint liberada; X Premium confirmado; vaga DS-N Redes (DSC-20260901-001) |
| 3 ROBÔS DS NUVEM | 3d644132 | `2026-08-31_tema3_rh_coordenador_ds_nuvem.md` | VIVA | Vaga COORDENADOR (RH): boletim 1×/dia por robô p/ Miguel, Baleia Azul e DS-N Chefe |
| 4 MARKETING | 64edf6fb | `2026-08-31_tema4_marketing_ciclo_diario.md` | VIVA | Ciclo 17h: proposta → silêncio aprova → campanha multi-produto multi-canal |
| 5 MOKA | 5ab4b882 | `2026-08-31_tema5_moka_estante_writer.md` | VIVA | Estante (filtro/apagar), padronização de botões, chave vertical no celular, Writer minimalista + troca de modelo (DSC-016/017) |
| 6 SEGURANÇA E COFRE | 9ed4eef2 | `2026-08-31_tema6_robo_seguranca.md` | VIVA | Vaga ROBÔ SEGURANÇA: ronda 1h, antivírus, rotação de senhas, criptografia |
| 7 BALEIA AZUL | b770142c | `2026-08-31_tema7_nota_robô_editor_baleia_azul.md` | VIVA | Robô editor da Baleia Azul 2×/dia com métricas reais (nota já existente — não duplicada) |
| 8 YOUTUBE | cc9d94e3 | `2026-08-31_tema8_youtube_transcricoes.md` | VIVA | Agente antigo (bloco Vídeos) morto 28/08 (Transkriptor sem crédito); novo DS-N YouTube batizado; vídeos longos 1-2h+ |
| 8 YOUTUBE (2ª conversa) | e4203677 | `2026-09-01_tema8_roni_lessa_doc_investigacao.md` | VIVA | Ordem 01/09 04:0x: "Deni" (apelido do DS YouTube) pega Doc Investigação/Record (27/08) inteiro → transcrição → post Cafezinho; fila alimentada + gate CL + Telegram respondido (DSC-20260901-003) |
| 9 AUDIÊNCIA E DADOS | 383cc3ce | `2026-08-31_tema9_robo_metricas.md` | VIVA | Vaga ROBÔ MÉTRICAS 2h: consolida GA4+FAROL+LUMINA, orienta o site; custo terá robô próprio |
| 10 REGRAS E MEMÓRIA | 20e9290d | `2026-08-31_tema10_robo_memoria_indexacao.md` | VIVA | Vaga DS-N MEMÓRIA 8h; índice MAPA/JANELA/POÇO; 4 feridas da indexação |

## Sessões especiais
| Sessão | Registro | Assunto |
|---|---|---|
| 321015d0 (29/08, a origem) | `2026-08-31_sessao_grande_dsc.md` | A sessão grande que originou a divisão em temas (registro completo pré-existente) |
| 8d258a27 (31/08 11:19) | `2026-08-31_utilidade_ipad_credenciais_telegram.md` | DS iPad → Telegram assinado; confirmação das 4 vias da ponte (§82: sem valores) |
| — | `PROMPT_NOVA_CONVERSA_DSC.md` | Base colada em cada conversa nova do DSC |

## Pendências cross-tema (foto 01/09 ~00:50)
1. Prompts a colar no ZCode (nascer): **Marketing** (tema 4) · **DS-N Redes** após debate (tema 2) · vagas a escrever: Coordenador (3), Segurança (6), Métricas (9), Memória (10), Editor Baleia Azul (7).
2. Miguel: 4 decisões da arquitetura CL-041 §13 + `copy` do fix do lock da AGY.
3. Atualizar `PROMPT_NOVA_CONVERSA_DSC.md` com as regras novas (tolerância, sessão organizadora, índice) — **precisa de ✓ do Miguel**.

— DS Celular (DSC) · 01/09/2026 ~00:50 BRT
