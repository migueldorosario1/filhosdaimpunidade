---
name: feedback-corrigir-erro-qualidade-corpo-automatico
description: No monitoramento posso corrigir AUTOMATICAMENTE erro objetivo de qualidade no CORPO do post (não só título) + acumular tudo num registro pra correção estrutural futura + relatório de saúde pro Miguel
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d7137897-dcad-4847-af64-a409ee24938c
---

No loop de monitoramento §53, ao encontrar **erro objetivo de qualidade** no CORPO do post (não só título), **corrijo na hora** via WP API mantendo `status=publish` + slug intacto, **anoto** em `Foruns/registro_erros_qualidade_redacao.md` com de/para + hipótese de causa estrutural.

**Erro objetivo = corrigir:** ortografia, capitalização de nome próprio, pontuação quebrada/órfã (`, .`), truncamento, tradução ruim, frase sem sentido, bloco vazado.

**NÃO mexer (domínio do Miguel):** ângulo, tom, linha editorial, SEO. Nunca o slug. Nunca prender post.

Além de corrigir, devo: (1) **acumular** todo erro no registro pra depois fazer correções ESTRUTURAIS (não remendo post a post); (2) sugerir correção estrutural **mesmo sem erro encontrado**; (3) produzir **relatório de saúde** pro Miguel — tá com erro demais? tá se deteriorando? o sistema está firme/resistindo depois de tanta mudança? Mantém um **placar por tick** (posts/erros/taxa) pra ver tendência.

**Why:** Miguel 02/06 ~14:48 BRT expandiu a autonomia (antes era só título — [[feedback_corrigir_titulo_fraco_automatico]]). Motivo: fizemos muita mudança no sprint (diretrizes/mídia/interlink/mailchimp) e ele quer saber se o sistema resiste. "Corrija na hora... anota... faz o relatório pra mim... pra ver se o sistema vai resistir."

**How to apply:** em cada tick, ler post na íntegra, corrigir erro objetivo de corpo na hora, logar no registro, atualizar placar de saúde. Distinguir erro cosmético (pontuação/grafia = geração de texto do redator) de deterioração de linha editorial/vazamento (alarme grave). Alinha com [[feedback_llm_sempre_para_editorial_nunca_lista_fixa]] (correção via LLM/reescrita, detecção pode ser determinística) e [[feedback_soltar_posts_nao_prender]].
