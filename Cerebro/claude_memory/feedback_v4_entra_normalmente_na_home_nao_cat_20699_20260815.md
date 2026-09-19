---
name: feedback-v4-entra-normalmente-na-home-nao-cat-20699-20260815
description: "SUPERSEDE parte \"cat 20699\" da regra teto-fila-12h. Miguel/Codex 15/08 13:26 esclareceram que TODO V4 entra normalmente na home. Nunca aplicar cat 20699 em publish V4. Se fila estourou teto, manter pending (não publish NO-HOME)."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d556bf3a-514a-43d5-a6d6-417905366fd5
---

## Origem

Codex Miguel 15/08 13:26 escreveu carta [CODEX-MIGUEL→CLAUDE-MIGUEL-CORRIGIR-V6-NO-HOME-20699-20260815-1326] após varredura ZCode:
- Zero posts V4 atuais com cat 20699
- Worker V4 do NYC não usa 20699
- Único agente aplicando 20699 era EU (via "válvula NO-HOME" que registrei 14/08 16:38)

**Regra Miguel real:** todo V4 entra normalmente na home. Sem exceção via cat 20699.

## Regra que SUPERSEDA

`feedback_teto_fila_12h_cadencia_valvula_nohome_20260814.md` — a parte que dizia:
> "se `final_da_fila >= NOW + 12h` → aplicar VÁLVULA NO-HOME: publish agora + cat 20699"

**Parte revogada:** aplicar cat 20699.

## Regra vigente (15/08 13:35 em diante)

**Se fila estourou teto 12h:**
- **NÃO** aplicar `publish` + cat 20699
- **Manter** `pending` com log em `ciclos_vigilia_MD` explicando "fila cheia, aguarda próximo slot"
- Alternativa Codex: estacionar excesso em pending com aviso

**Se gancho HOJE ao vivo (votação em curso, morte, tragédia):**
- `publish` NORMAL sem cat 20699
- Preservar exceção da regra 12/08 23:15

**Nunca:**
- Aplicar cat 20699 em qualquer post V4 (author 5786)
- Aplicar cat 20699 em qualquer post do repetidor (5470)
- Confundir "estourou teto" com "gancho ao vivo"

## Implementação no meu pipeline

Meus patches PHP são temporários (`/tmp/patch_slot_X_HHMM.php` por ciclo). A lógica vive em template mental. Mudança efetiva:

**ANTES (patches até 15/08 13:35):**
```php
// Se fila estourou teto:
wp_update_post([..., "post_status" => "publish", "post_date" => NOW]);
wp_set_post_categories($id, array_merge($cats, [20699]));  // cat NO-HOME
```

**AGORA (15/08 13:35+):**
```php
// Se fila estourou teto:
// NÃO agendar, NÃO publish NO-HOME.
// Deixar pending com log no ciclos_vigilia_MD.
echo "SKIP $id: fila estourou teto — mantém pending pro próximo slot";
```

## Sobre o incidente 265928

Post 265928 (Procuradoria+Tarcísio+Haddad) foi publish + cat 20699 por mim ciclo 11:04. Cat 20699 removida pelo cleaner CafezinhoWP entre 12:33 (Grok Laura detectou) e 13:04 (verifiquei). Post está limpo agora.

Aprendizado paralelo: o cleaner CafezinhoWP RODA (contrário à minha suposição de que não estava rodando). Só que ele NÃO deveria precisar rodar porque eu nunca devia ter aplicado 20699.

## Auditoria

Ver `Cerebro/monitoramento_horario/bugs_encontrados/bugs_2026-08-15.jsonl` entry 11:07 (aplicação NO-HOME) — foi a única/última.

A partir de agora: qualquer log JSONL com `acao: valvula_no_home` significa erro (não devia ter feito).

## Relacionados

- [[feedback-teto-fila-12h-cadencia-valvula-nohome-20260814]] — SUPERSEDED em parte
- [[feedback-processo-autoaprendizado-ler-memoria-todo-ciclo-20260815]] — regra que garantiu que eu lesse e detectasse esse conflito
- [[feedback-migracao-canal-fechar-loop-no-antigo]] — como fui parar nessa regra incorreta (via inbox_trindade/claude.md relayed pelo ZCode)

## Regra âncora

**"Todo V4 entra normalmente na home. Nunca cat 20699. Fila cheia = pending, não publish NO-HOME."** — Miguel via Codex, 15/08 13:26 BRT
