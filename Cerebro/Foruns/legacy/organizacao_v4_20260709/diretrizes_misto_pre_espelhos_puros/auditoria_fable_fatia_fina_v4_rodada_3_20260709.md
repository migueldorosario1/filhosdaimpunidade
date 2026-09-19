# Auditoria FABLE — fatia fina V4, terceira rodada (execução independente)

Data: 2026-07-09
Auditor: Fable (Claude Fable 5, Anthropic), parecerista externo
Objeto: pacote pós-ajustes do Codex (fatos_travados, anti-eco, escopo de bloqueios, encoding, arquivo cego, .py espelhados)

## Veredito

**APROVO COM 1 AJUSTE BLOQUEANTE NOVO.**

- Bloqueios das rodadas anteriores: **todos atendidos e verificados** (desta vez por execução, não por leitura).
- Pode preparar o redator LLM real/super_luxo? **Sim**, mantendo o julgamento cego como gate antes de institucionalizar.
- Pode habilitar publicação real? **Não** até corrigir a brecha da fonte manual (abaixo).

## Escopo

- Li: os 5 módulos .py espelhados (`curadoria_tese`, `ab_experiment`, `fluxo`, `wordpress_publicador`, `test_contracts`), os contratos atualizados, as duas variantes, a curadoria, o registro do experimento e o arquivo cego.
- Executei: subset da fatia fina de `test_contracts.py` em ambiente próprio + 5 sondagens adversariais fora da suíte.
- Não executei: a suíte completa de 45 testes de ponta a ponta — o espelho contém 5 dos ~21 módulos do pacote (`loader`, `camadas`, `telemetry`, `composer`, `memoria`, `imagem_destacada` etc. ausentes). Construí stubs mínimos e fiéis (loader de JSON, MediaCandidate com `as_dict`) apenas para satisfazer imports. O "OK 45" da suíte completa permanece autorrelato; o subset da fatia fina agora é verificação independente.

## Execução independente — resultado

Subset da fatia fina: **10/10 PASS**

```text
PASS test_curadoria_cria_tres_teses_e_frame_visual
PASS test_curadoria_sem_fonte_leitura_corrente_bloqueia
PASS test_producao_sem_curadoria_bloqueia
PASS test_modo_experimento_sem_curadoria_somente_dry_run
PASS test_ab_261439_grava_pacote_cego_sem_publicacao
PASS test_wordpress_publicador_dry_run_grava_tentativa
PASS test_wordpress_publicador_real_bloqueado_por_contrato
PASS test_wordpress_publicador_bloqueia_sem_featured_media
PASS test_wordpress_publicador_bloqueia_sem_curadoria_id
PASS test_wordpress_publicador_real_bloqueia_ascii_sem_acentos
```

## Sondagens adversariais (fora da suíte)

```text
A) payload com eco de template em fato_novo
   -> BLOQUEADO: anti_eco_template:fato_novo  [OK]

B) fatos_travados com apenas 1 item
   -> BLOQUEADO: fatos_travados_insuficientes  [OK]

C) modo_experimento + mode=real + real_wordpress_draft=True
   -> BLOQUEADO: curadoria_id_obrigatorio  [OK]

D) sem curadoria_id, sem experimento, mesmo em dry_run
   -> BLOQUEADO: curadoria_id_obrigatorio  [OK]

E) leitura_corrente com fonte=manual_editor + mode=real + real_wordpress_draft=True
   -> PASSOU (ok=True, issues=[])  [FALHA — brecha]
```

## AJUSTE BLOQUEANTE — cláusula decorativa: fonte manual em publicação real

O contrato `v4_curadoria_tese_v1.json` declara:

```text
fase_1.publicacao_real_exige_fonte_nao_manual: true
```

Mas `validate_gate` em `curadoria_tese.py` **não verifica essa cláusula**. Um payload com `leitura_corrente_timestamped.fonte = "manual_editor"` passa no gate em modo real com draft real. Verifiquei por execução direta (sondagem E acima).

Risco vivo hoje: zero — `real_publish.enabled: false` no publicador segura tudo. Mas é exatamente o padrão que este projeto combate: cláusula que existe no JSON e não existe no código vira bug silencioso no dia em que alguém habilitar publicação real.

Conserto (pequeno):

```text
1. validate_gate: quando mode == "real" ou real_wordpress_draft == True,
   exigir leitura_corrente_timestamped.fonte != "manual_editor"
   (issue sugerida: "fonte_manual_proibida_em_publicacao_real").
2. Novo teste: test_publicacao_real_bloqueia_fonte_manual.
   A suíte vira 46.
```

Este ajuste é bloqueante para **habilitar publicação real**, não para preparar o redator LLM real. As duas trilhas podem andar em paralelo.

## Ajustes anteriores — verificação item a item

```text
fatos_travados estruturado ......... OK (min_items: 2, fonte_ref,
                                     obrigatorio_no_texto, produtor_deve_cobrir;
                                     insuficiência bloqueia — verificado por execução)
anti-eco de template ............... OK (contrato + código; gerador mock corrigido:
                                     fato_novo agora extrai sentença real da fonte,
                                     não ecoa o título — verificado por execução)
escopo dos bloqueios de camada ..... OK (scope: fase_1_global declarado em
                                     v4_bancos_camadas; ambiguidade resolvida)
validação de encoding .............. OK (test_wordpress_publicador_real_bloqueia_
                                     ascii_sem_acentos passou na minha execução)
variante B com acentuação .......... OK (verificado no arquivo cego e no JSON)
.py espelhados ..................... PARCIAL (5 módulos; suíte completa não roda
                                     de forma independente — ver pendência abaixo)
arquivo cego separado .............. OK com 2 notas (abaixo)
```

## Notas sobre o julgamento cego

O arquivo `ab_261439_julgamento_cego_miguel.md` está bem construído: rótulos neutros (Laranja/Azul), instrução correta, sem vazamento de qual versão é qual, sem curadoria visível.

Duas notas honestas:

1. **Ordem fixa:** a versão curada aparece sempre primeiro (Laranja). Com n=1 e um leitor, irrelevante; nos próximos casos, randomizar a ordem por leitor para não acumular viés de posição.
2. **Limite inevitável deste caso:** o Miguel escreveu o feedback sobre o texto original — ele pode reconhecer o Texto Azul de memória. A cegueira dele é parcial por construção, não por falha do arquivo. Consequência prática: **o segundo leitor cego é o juiz verdadeiramente cego do 261439** e deixa de ser opcional. O julgamento do Miguel continua valendo como avaliação editorial; só não deve ser contado como cego puro.

## Pendências não-bloqueantes

```text
1. Espelhar o pacote v4_diretrizes/ completo (ou os módulos restantes)
   para que a suíte de 45/46 rode de ponta a ponta em auditoria externa.
2. Randomização de ordem no instrumento cego (próximos casos).
3. Registrar no experimento que o julgamento do Miguel neste caso é
   "cego parcial por memória do original".
```

## Caminho aprovado

```text
1. Corrigir brecha fonte manual + teste 46.        (antes de qualquer publish real)
2. Executar julgamento cego: Miguel + 2º leitor.   (gate de institucionalização)
3. Em paralelo: preparar redator LLM real/super_luxo
   respeitando routing_constraints (curador != redator,
   vetos default por família com override logado).
4. Após o cego: 3-5 casos adicionais em editorias
   diferentes antes de Fase 2 (fusões, embeddings, autocura).
```

## Cartinha ao Miguel

Miguel,

Desta vez não li o código — executei. Os dez testes da fatia fina passaram na minha máquina, e os gates aguentaram quatro das cinco tentativas que fiz de quebrá-los. A quinta encontrou a única fresta: a regra que proíbe fonte manual em publicação real existe no contrato mas não no código. Nada está em risco hoje, e o conserto é uma checagem e um teste. Mas repare no padrão — foi a cláusula que eu mais elogiei na rodada passada. Elogio de auditor também precisa de teste.

O sistema está pronto para a parte que importa: o julgamento cego. Uma advertência amiga sobre ele — você conhece o texto original de cor, foi você que o rejeitou. Julgue mesmo assim, seu olho é o que estamos calibrando; mas o veredito cego de verdade virá do segundo leitor. Escolha alguém que não leu nada disto.

Um abraço,
**Fable**
