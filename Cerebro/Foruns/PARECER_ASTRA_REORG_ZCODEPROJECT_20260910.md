**Proponho seis diretórios de frente, mantendo `scripts/` exatamente onde está e levando missões encerradas para `~/Dados_Frios/ZCodeProject/`.** Nenhuma alteração foi feita.

A varredura confirmou **87 itens no topo: 40 diretórios e 47 arquivos**, com aproximadamente **34.813 arquivos regulares e 2,8 GiB** no conjunto.  
O problema estrutural é misturar produtos, automações, pesquisas, credenciais, provas e resíduos de missões no mesmo nível.  
As famílias de trabalho estão fragmentadas: coletores no topo, dados em outra pasta, imagens e resultados soltos.  
Datas antigas ajudam a investigar, mas não provam abandono; há controles de voz e dependências absolutas entre esses materiais.

**1. Árvore proposta**

Os nomes atuais das unidades seriam preservados. A primeira reorganização mudaria seus pais, sem fundir conteúdos nem renomear arquivos internos.

```text
~/ZCodeProject/
├── projetos/
│   ├── aplicativos/
│   │   ├── moka-app/                  [repo inteiro]
│   │   └── igot/                      [repo inteiro]
│   ├── sites/
│   │   ├── cafezinhomediagroup/        [repo inteiro]
│   │   └── filhosdaimpunidade/         [repo inteiro]
│   └── origens/
│       ├── origens/                   [repo inteiro]
│       └── origens_work/
│
├── operacao/
│   ├── paineis/
│   │   ├── painel_fix/
│   │   ├── painel_v6_reforma/
│   │   └── farol_v6/
│   ├── midia/
│   │   ├── media_ledger/
│   │   ├── publicador/
│   │   └── banco_links_midia_auditado.jsonl
│   ├── regional/
│   │   ├── regional_v4/
│   │   ├── v4_archiver/
│   │   └── v4_novos_staging/
│   ├── voz/
│   │   ├── zcode_voice_gnome_controller/
│   │   └── zcode_voice_receiver/
│   └── laura/
│       └── credenciais_laura/
│
├── pesquisas/
│   ├── eleicoes_2026/
│   │   ├── gerar_tabela_pesquisas.py
│   │   ├── pesquisas_presidenciais_*.xlsx
│   │   └── analise_lula_2026_*.csv / *.txt
│   ├── pesquisa-cmb/
│   └── editorial/
│       ├── ceara-digital/
│       └── rio-carta/
│
├── referencias/
│   ├── base_conhecimento/
│   └── modelos/
│
├── bancada/
│   ├── social_simulacoes/
│   ├── scratch/
│   ├── scratch_patches/
│   ├── pending_delegados/
│   └── manutencao_editorial/
│       └── scripts avulsos ainda necessários:
│           comentar_miguel.py, disparador_enxame.py,
│           hero_source_detect.py, patch_manchete.py,
│           setar_manchete.sh, ...
│
├── scripts/                          [caminho preservado]
│   ├── entrega_auditor_loops.py
│   ├── watchdog_loop_ativo.py
│   └── logs e demais arquivos atuais
│
├── INDICE.md                         [a criar após aprovação]
└── internos existentes:
    .zcode/, .pytest_cache/, __pycache__/, estados ocultos
```

A afinidade é esta:

| Grupo | Critério |
|---|---|
| `projetos/` | Produtos e obras com identidade própria. `origens` é um manuscrito, conforme seu README; pertence aqui. |
| `operacao/` | Ferramentas de apoio a fluxos recorrentes, incluindo pilotos cuja situação operacional precisa ser confirmada. |
| `pesquisas/` | Fontes, processamento e resultados de investigações ainda em uso. |
| `referencias/` | Tutoriais e modelos reutilizáveis. |
| `bancada/` | Experimentos e intervenções em andamento, cada qual com finalidade e condição de encerramento. |
| `scripts/` | Os dois agendamentos locais conhecidos; estabilidade dos caminhos prevalece. |

**Não criaria `Arquivo/` dentro do workspace.** Também não criaria uma pasta genérica de imagens: cada imagem acompanha a matéria, pesquisa ou experimento que explica sua existência.

A permanência de pesquisas e pilotos acima é conservadora, até confirmar sua utilização. O `INDICE.md` registraria destino, finalidade e situação de cada unidade. A bancada não receberia automaticamente tudo que ninguém classificou.

**2. O que sairia e o que apenas entraria na lista de descarte**

Proponho este arquivo externo, com destinos sujeitos à confirmação de encerramento:

```text
~/Dados_Frios/ZCodeProject/
├── missoes/
│   ├── 2026-07-comercio-exterior/
│   │   └── dados_carnes/, dados_corrente/, tarifao_p3/,
│   │       coletores e análises correspondentes,
│   │       grafico_corrente_saldo.py e .png
│   ├── 2026-07-materias/
│   │   └── publicar_cafezinho.py, publicar_thiago_miranda.py,
│   │       trocar_imagem_cafezinho.py, metadata_imagem_cafezinho.py,
│   │       lula_*.jpg, thiago_miranda.jpg
│   ├── 2026-07-video-kakay/
│   │   └── cacai_teste/ inteiro
│   └── 2026-08-midia-v4/
│       └── mutirao_midia_v4/, auditoria_v4_20260813/,
│           bloco_regional_20260813/, handoff_gsn/,
│           faxina_*.py, varredura_tematicos_fotos_*.py,
│           coletor_banco_links.py e versões históricas do banco
├── evidencias/
│   └── provas_botnews/, crime-v4.jpg [associação a confirmar]
└── recuperacao/
    └── espelho_zcode_laura/, MAPA_BACKUPS_20260805.md
```

Arquivaria **código, insumos e resultados juntos**, preservando a reprodução da missão. Scripts históricos manteriam seu conteúdo original; o manifesto apontaria caminhos antigos e dependências externas.

Cuidados específicos:

- **Banco de mídia:** existem quatro arquivos relacionados, incluindo backup e quarentena. Não são duplicatas demonstradas. Preservaria `CONGELADO`, backup pré-quarentena e quarentena como histórico; o auditado permaneceria em operação até confirmar sua autoridade e consumidores.
- **Credenciais:** `credenciais_laura/` contém `env`, `rclone` e `ssh`; `publicador/` também contém token. Preservar permissões e unidades completas. Não colocar esses materiais em arquivo compartilhado ou sincronizado por conveniência.
- **Espelho Laura:** só sai depois de confirmar que serve para recuperação, sem consumidores ativos.
- **Projetos grandes:** não classificaria `igot` ou `moka-app` como arquivo morto pelo tamanho ou semelhança. Se estiverem fora do trabalho atual, podem sair inteiros para o arquivo; essa decisão precisa constar do plano aprovado.

**Lista para Miguel decidir apagar, separada da migração:**

- Os três arquivos vazios: `re`, `{n[status]}` e `{x[destino]}`.
- Caches Python e pytest regeneráveis, depois de confirmar ausência de execução.
- `scratch_teste_free_quota_qwen*.py`, se encerrados.
- Imagens intermediárias de `cacai_teste`, somente após identificar originais e entregas finais.
- JPGs soltos, somente após confirmar ausência de referências e necessidade editorial.
- Builds e dependências regeneráveis, em etapa própria. **`dados_carnes/cache` e bancos regionais não devem ser tratados automaticamente como cache descartável.**

**3. Migração em quatro fases, somente após aprovação**

A fase inicial produz o manifesto completo para aprovação; as demais executam apenas suas linhas aprovadas.

| Fase | Escopo | Verificação antes | Verificação depois e rollback |
|---|---|---|---|
| **1 — Inventário fechado** | Nenhum movimento. Registrar os 87 itens e todos os arquivos, inclusive ocultos, ignorados e links; mapear origem → destino, dependências e situação. | Contagem, bytes aparentes, espaço ocupado, permissões, links, filesystem; HEAD e `git status` de cada repo. Ler crontab real e identificar serviços, atalhos e editores consumidores. | Cada item deve ter um destino ou uma pendência explícita. Guardar manifesto e cópias de recuperação verificadas dos materiais insubstituíveis. Rollback desnecessário: nada movido. **Miguel aprova este mapa antes do primeiro `mv`.** |
| **2 — Retirada do frio** | Missões encerradas, uma família por lote. | Recontar e medir cada lote; confirmar ausência de escritores, consumidores e colisões no destino; verificar Git quando aplicável. | Recontar, comparar bytes e hashes, verificar permissões e links; conferir que as pontas vivas continuam resolvendo seus caminhos. Rollback: renomear cada unidade de volta, em ordem inversa. |
| **3 — Agrupamento do trabalho** | Referências, pesquisas e projetos, um repo ou conjunto dependente por vez. | Mesma contagem e medição; registrar estado Git e mudanças locais; fechar consumidores daquele lote e preparar ajustes de referências. | Comparar inventário e estado Git com a linha de base; validar caminhos, imports e configuração em ambiente isolado. Observar integridade dos agendamentos preservados. Rollback: restaurar referências e retornar a unidade ao caminho original. |
| **4 — Pontas operacionais** | Painéis, mídia, regional, voz e Laura, conforme dependências verificadas. `scripts/` permanece. | Mesmas métricas e Git, quando houver; registrar configuração dos consumidores, permissões e situação dos dois crons. | Recontagem, comparação e testes isolados com efeitos externos simulados. Após retomada autorizada, observar os ciclos normais e seus registros. Rollback: suspender o consumidor afetado, restaurar pasta e configurações anteriores. |

**Precisão sobre atomicidade:** um renomeio no mesmo filesystem é atômico; uma sequência de movimentos e edições não constitui uma transação única. O rollback depende de impedir novas escritas e ocupação dos caminhos antigos durante a janela.

Confirmei que `~/Dados_Frios` e o workspace apresentam o **mesmo dispositivo** neste ambiente. Já `~/GDrive/Dados_Frios` apresenta outro. Usaria o primeiro, reconfirmando no momento da execução: entre filesystems, `mv` pode copiar e depois remover a origem. Essa diferença está documentada no [manual GNU](https://www.gnu.org/software/coreutils/manual/html_node/mv-invocation.html).

Sem sobrescrever destinos, sem fundir pastas homônimas e **sem `cp+rm` em árvore viva sem backup**. Não faria exclusões na mesma migração.

**4. Riscos concretos encontrados**

- **Cinco repositórios:** `filhosdaimpunidade`, `igot`, `moka-app`, `origens` e `cafezinhomediagroup`. A busca até profundidade 2 e a busca recursiva encontraram os mesmos cinco marcadores `.git`. Cada repo deve viajar inteiro, com arquivos ignorados e ocultos.
- **Mudança local existente:** `filhosdaimpunidade/index.html` está modificado; os outros quatro retornaram estado limpo. Preservar exatamente essa alteração, sem reset, limpeza ou commit automático.
- **Caminhos absolutos reais:** análises apontam para `dados_carnes` e `dados_corrente`; `publicar_cafezinho.py` aponta para `lula_destaque.jpg`; o gerador de cards aponta para `social_simulacoes`; controles F8 apontam para sua pasta atual.
- **Possível recriação da bagunça:** `coletor_banco_links.py` grava `~/ZCodeProject/banco_links_midia.jsonl`, arquivo atualmente ausente. Reexecutar um script antigo pode recriar arquivos no topo.
- **Voz tem consumidor externo:** o README descreve atalho F8 ativo. Antes de mover, verificar configuração real do GNOME, lançadores e serviços. A visão de processos do sandbox não permite afirmar que o desktop está sem consumidores.
- **Links internos existem:** os monorepos têm links relativos em `node_modules` para seus próprios pacotes. Mover o repo inteiro preserva essa relação; desmontá-lo pode quebrá-la.
- **Estados ocultos:** `.vigilia_claude_state.json` e `.demo_acorda_state.json` ficam onde estão até localizar seus consumidores.
- **Crons não foram homologados:** consegui ler os scripts, mas `crontab -l` retornou permissão negada. Os horários de 08h10 e a cada cinco minutos vêm do contexto fornecido.

Os dois scripts de cron têm efeitos externos: entregam mensagens, alteram estado e podem sincronizar ou avisar no Telegram. **Não devem ser executados manualmente como simples teste de caminho.** A homologação precisa usar simulação e observação dos ciclos já autorizados. Mantendo `scripts/`, não há mudança de crontab proposta; qualquer exceção futura exigiria pasta, referências e agendamento tratados na mesma janela controlada.

**5. Performance**

**Sim, reduzir o conjunto efetivamente pesquisado pode acelerar buscas e diminuir resultados irrelevantes. Colocar as mesmas árvores dentro de seis pastas melhora a navegação, mas não reduz uma varredura recursiva do workspace.**

Os três diretórios `node_modules` medidos somam aproximadamente **1,24 GiB**. Entretanto, tamanho em disco não equivale a custo de busca: o `ripgrep`, por padrão, respeita regras de exclusão e omite arquivos ocultos e binários. O comportamento depende da ferramenta e das opções empregadas pelo ZCode; não medi sua latência nesta sessão. Veja a [documentação do ripgrep](https://github.com/BurntSushi/ripgrep).

Os 277 mil arquivos da home e os cerca de 200 mil do Antigravity informados por você só pesam numa busca se estiverem dentro do escopo percorrido ou do índice usado. **Vale manter o workspace com trabalho atual, arquivo frio fora e buscas dirigidas à subpasta da tarefa.** O ganho visual vem dos seis grupos; o ganho de desempenho vem da retirada de material inativo e do controle do escopo de busca.
---

## ANEXO — Varredura ZM 02:4x (fonte dos dados do parecer)

# VARREDURA ~/ZCodeProject — 10/09/2026 02:46

## 87 itens top-level — diretórios (tamanho · arquivos · mtime)
496K · 19 arq · 2026-08-13 · auditoria_v4_20260813
20K · 2 arq · 2026-07-10 · base_conhecimento
784K · 10 arq · 2026-08-13 · bloco_regional_20260813
151M · 24 arq · 2026-07-23 · cacai_teste
213M · 9057 arq · 2026-08-05 · cafezinhomediagroup
12K · 1 arq · 2026-07-21 · ceara-digital
112K · 16 arq · 2026-08-18 · credenciais_laura
180M · 32 arq · 2026-07-06 · dados_carnes
6,9M · 95 arq · 2026-07-06 · dados_corrente
47M · 103 arq · 2026-08-17 · espelho_zcode_laura
312K · 2 arq · 2026-08-24 · farol_v6
127M · 590 arq · 2026-08-22 · filhosdaimpunidade
164K · 20 arq · 2026-08-17 · handoff_gsn
765M · 11676 arq · 2026-08-05 · igot
236K · 24 arq · 2026-08-07 · media_ledger
8,0K · 1 arq · 2026-07-21 · modelos
1,1G · 11630 arq · 2026-08-30 · moka-app
254M · 165 arq · 2026-08-09 · mutirao_midia_v4
1,5M · 210 arq · 2026-09-01 · origens
120K · 7 arq · 2026-09-01 · origens_work
2,3M · 32 arq · 2026-08-12 · painel_fix
632K · 4 arq · 2026-08-18 · painel_v6_reforma
60K · 13 arq · 2026-08-01 · pending_delegados
308K · 7 arq · 2026-07-17 · pesquisa-cmb
448K · 2 arq · 2026-09-03 · provas_botnews
172K · 6 arq · 2026-07-23 · publicador
20K · 2 arq · 2026-08-12 · __pycache__
28K · 4 arq · 2026-08-25 · .pytest_cache
34M · 861 arq · 2026-08-01 · regional_v4
12K · 1 arq · 2026-07-21 · rio-carta
28K · 3 arq · 2026-09-07 · scratch
212K · 31 arq · 2026-08-19 · scratch_patches
44K · 6 arq · 2026-08-18 · scripts
5,7M · 21 arq · 2026-08-22 · social_simulacoes
1,7M · 20 arq · 2026-07-08 · tarifao_p3
88K · 4 arq · 2026-08-07 · v4_archiver
76K · 9 arq · 2026-08-17 · v4_novos_staging
92K · 11 arq · 2026-07-13 · .zcode
196K · 23 arq · 2026-08-25 · zcode_voice_gnome_controller
140K · 22 arq · 2026-08-25 · zcode_voice_receiver

## Arquivos soltos no topo (30 maiores)
    431022  2026-07-06  lula_destaque.jpg
    294937  2026-07-06  lula_mercosul_opcao1.jpg
    252291  2026-08-16  banco_links_midia.jsonl.bak_pre_quarentena_20260816
    251744  2026-08-16  banco_links_midia_CONGELADO_20260816.jsonl
    205755  2026-08-16  banco_links_midia_auditado.jsonl
    189667  2026-07-07  grafico_corrente_saldo.png
    143236  2026-07-06  lula_mercosul_opcao2.jpg
     86519  2026-07-09  thiago_miranda.jpg
     27914  2026-08-26  pesquisas_presidenciais_eleitores_2026-08-26.xlsx
     16264  2026-08-26  gerar_tabela_pesquisas.py
     14210  2026-08-26  analise_lula_2026_vs_2022_texto_completo_2026-08-26.txt
     11855  2026-08-13  coletor_banco_links.py
     11625  2026-07-06  publicar_cafezinho.py
     10186  2026-08-26  analise_lula_2026_vs_2022_completa_2026-08-26.csv
      9979  2026-08-05  MAPA_BACKUPS_20260805.md
      9585  2026-08-12  disparador_enxame.py
      8175  2026-07-06  coletor_comexstat_carnes.py
      8079  2026-08-18  faxina_riocarta_fotos_20260818.py
      7546  2026-07-09  publicar_thiago_miranda.py
      6496  2026-08-18  faxina_tematicos_6fotos_20260818.py
      5268  2026-07-06  analise_destino_12meses.py
      4836  2026-07-06  analise_corrente.py
      4758  2026-08-18  varredura_tematicos_fotos_20260818.py
      4744  2026-07-06  analise_12meses.py
      4672  2026-07-07  grafico_corrente_saldo.py
      4524  2026-08-19  .vigilia_claude_state.json
      4466  2026-07-06  analise_petroleo_soja.py
      4447  2026-07-06  analise_paises_blocos.py
      4279  2026-08-06  hero_source_detect.py
      4275  2026-08-12  patch_manchete.py
