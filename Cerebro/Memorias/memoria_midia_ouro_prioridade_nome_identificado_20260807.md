# 🧠 Memória — Mídia Ouro: prioridade do nome identificado (07/08/2026)

> Log técnico completo do fórum `Foruns/forum_midia_ouro_prioridade_nome_identificado_20260807.md`.
> Sessão: ZCode (`k3-256k`), ~18:29→18:55 BRT. Servidor: Tencent (`ssh tencent` = **ubuntu@43.156.151.165**, sudo sem senha OK — atenção: o alias não é root; `/root` é 775 root:root, `/root/V3` é ubuntu, banco é root:root 644 → operações de escrita via `sudo`).

## 1. Mapa do sistema (descoberta)

- Serviço: `midia-ouro-panel.service` → `/root/painel_midia_ouro.py`, porta **8091** (nginx publica `/midia-ouro/` no :80).
- Banco: `/root/agent_data/banco_midia_ouro_v3/banco_midia_ouro_v3.db` (tabelas `midia_ouro` 739 regs, `fila_catalogacao_humana_ouro` 697; backups históricos `*_20260806` existentes).
- Classificador: `/root/V3/classificar_banco_ouro_midia.py` — cron `/etc/cron.d/midia-ouro-classificador` **`17,47 * * * *`** (root, venv). O `main()` **apaga a fila pendente e re-insere** a cada corrida → correções de dados/lógica devem ir no classificador, nunca direto na fila.
- Cânone de nomes: `/root/nomes_canonicos_ouro.py` (`canon`, `unificar_lista`, `unificar_json`) — criado 06/08 por ordem do Miguel ("usa só Lula"); mapeia "Luiz Inácio Lula da Silva"→"Lula", "Janja Lula da Silva"→"Janja" etc.
- Robô coletor: `/root/V3/robo_banco_ouro_midia_v3.py` (não toca a fila).

## 2. Reprodução do erro visto pelo Miguel

Card `8ec180fb…` ("Presidente Lula na cerimônia do Pacto Nacional Brasil Contra o Feminicídio"):
- `entidade`=**Hugo Motta** (fonte); `pessoas_visiveis_total`=7; `pessoas_identificadas_json`=`["Lula","Janja","Hugo Motta","Edson Fachin"]` (unificado).
- `metadados_json.gemini_vision_banco_ouro.personalidade_principal`=**"Luiz Inácio Lula da Silva"** (cru); `pessoas_identificadas` cruas com formas longas.
- O painel montava `nomes` = json unificado + principal cru inserido → exibia **"Luiz Inácio Lula da Silva" e "Lula" juntos** = queixa exata.

## 3. Edições (4 no classificador + 1 no painel)

Backups: `classificar_….py.bak_pre_prioridade_nome_20260807`, `painel_midia_ouro.py.bak_pre_prioridade_nome_20260807`, tabelas `midia_ouro_bak_priornome_20260807` (739) e `fila_ouro_bak_priornome_20260807` (697).

**`classificar_banco_ouro_midia.py`:**
1. Após unificar pessoas: `entidade_fonte = entidade`; se `len(pessoas_identificadas)==1` → `entidade = pessoas_identificadas[0]`; senão se `principal` → `entidade = principal` (nome identificado tem prioridade, ordem Miguel 07/08).
2. Aprova direta: `bloqueio_duro` = bloqueada | motivo começa `gemini_` | `licenca_a_verificar` | `multiplas_pessoas_identificacao_incompleta` | `personalidade_desfocada_ou_secundaria`. `regra_nome_unico` = não-bloqueio + 1 identificado + visíveis ≤1 (ou None) + score ≥ 450 + (sem gemini OU decisão APROVAR) → `uso_automatico`, `tipo_uso=uso_automatico_nome_identificado`, motivo `regra_nome_identificado_prioritario_miguel_20260807`, prioridade 0. (Motivos leves — título genérico, contextual, dimensão, ratio — não seguram mais.)
3. `main()`: UPDATE passou a gravar `entidade` (antes nunca atualizava); INSERT da fila usa `result["entidade"]` (fila mostra a entidade já corrigida).
4. Ramo `revisao_humana` (decisões humanas persistem) ganhou as chaves `entidade`/`entidade_fonte` para não quebrar o `main()`.

**`painel_midia_ouro.py`:**
5. `review_payload()`: após montar `nomes`, `nomes = unificar_lista(list(dict.fromkeys(nomes)))` — fim das 2 formas na exibição. (O `<pre>` "Parecer Gemini" segue mostrando o JSON cru do modelo — diagnóstico, proposital.)

## 4. Deploy e execução

```bash
scp /tmp/midiaouro/*.py tencent:/tmp/  # editados localmente com revisão
sudo cp painel… .bak_pre_prioridade_nome_20260807  # + backup tabelas via sqlite3
cp/sudo cp para /root/V3/ e /root/ ; chown root:root no painel
ast.parse OK ×2; py_compile OK (sudo, __pycache__ é root); md5 idênticos
sudo systemctl restart midia-ouro-panel → active; /midia-ouro/revisao 200
cd /root/V3 && sudo /root/venv/bin/python3 classificar_banco_ouro_midia.py
# → {"total": 739, "stats": {"bloqueada": 35, "uso_automatico": 241, "revisao_humana": 463}}
```

## 5. Provas (consultas contra backup `*_bak_priornome_20260807`)

- **11 entidades corrigidas** (`m.entidade != b.entidade`), incl. `8ec180fb…`: Hugo Motta → **Lula** (e irmã `014c2648…` da mesma cerimônia).
- **0 movimentos auto↔revisão indevidos** (auditoria `auto_para_revisao=0`, `revisao_para_auto=0` — os 4 `uso_automatico_nome_identificado` já eram auto; mudou tipo/motivo).
- **0** `pessoas_identificadas_json` com forma longa ("Luiz In%cio", "Janja Lula da Silva").
- Fila pendente 397→397: os 25 pendentes de 1 nome tinham bloqueio real (13 grupo incompleto, 5 desfocado, 6 score 353–417 < 450, 1 grupo 5 pessoas).
- API ao vivo (`/api/midia-ouro/review/next`): card do pacto exibe `['Lula','Janja','Hugo Motta','Edson Fachin']` — sem forma longa (antes traria o principal cru).
- ⚠️ Armadilha SQLite: aspas duplas em literais que coincidem com nome de coluna (`"uso_automatico"`) viram identificador → query errada silenciosamente. Usar aspas simples.

## 6. Efeito colateral conhecido

Card que mudou de entidade passa a competir na partição da nova entidade no filtro "máx 3 cards por personagem" (regra do próprio Miguel, 04/08) — pode sair da vitrine da fila (dados intactos). Instituições (Senado/Câmara/STF) já eram excluídas da fila desde 04/08.

## 7. Pendências para o Miguel

1. Grupo com `personalidade_principal` identificado também aprova direto? (hoje segue na fila para catalogação humana)
2. Ignorar `score ≥ 450` para as 6 fotos pequenas de 1 nome? (353–417)

— ZCode (`k3-256k`), 07/08/2026 ~18:55 BRT
