# MEMÓRIA TÉCNICA — BRICS 1/6: rascunho 270342 (cúpula de Nova Déli × Trump "morto")

> Execução 1 da automação `automation-509b4252-b4f5-4ce3-be80-bdc3c76991db` (cron `0 */2 * * *`, maxRuns=6), disparada 12/09/2026 16:00 BRT, rodada em ZCode/Kimi K3 no Dell.

## Entrega

- **Post 270342** — «Sob ameaça de Trump, BRICS condena tarifas unilaterais» (54 chars) — status **draft**, autor **5486**, slug pendente (post_name vazio no draft), excerpt preenchido.
- **Taxonomia:** categorias **5003 Geopolítica + 5053 Brics**; 11 tags (brics 325, china 1236, geopolítica 564, Índia 1902, Irã 176, Nova Déli 6953, oriente médio 318, Rússia 1647, Sul Global 5111, tarifas 5383, Trump 1832).
- **Capa:** anexo **270343** (featured image) — "BRICS leaders arrive at the BRICS Business Forum 2026 on the sidelines of the 18th BRICS Summit at Bharat Mandapam.jpg", 2200x1508, Gabinete do PM da Índia/PIB, **GODL-India**, via Wikimedia Commons. Crédito SÓ no post_excerpt do anexo (legenda); alt preenchido. Mostra Pezeshkian+Modi+Putin+Ramaphosa caminhando juntos na cúpula de HOJE.
- **Métricas do texto:** 954 palavras, 5 intertítulos h3, 0 travessões, 0 dois-pontos no corpo, 0 "E,/Mas,/Porém," abrindo frase, 0 "exclusiv", 0 "Foto:", 0 Orwell/1984.
- **Aspas:** 19/19 validadas por grep nas fontes salvas (2 com normalização: case no 247 e word-joiner U+2060 em "Al Minhad" do InfoMoney).

## Pauta e fatos (todos com fonte)

- **18ª cúpula do BRICS**, Bharat Mandapam, Nova Déli, 12-13/09/2026; Xi (1ª visita à Índia desde 2019), Putin, Pezeshkian, Modi; Mauro Vieira pelo Brasil (Lula na campanha).
- **Declaração de Nova Déli (12/09):** "máxima prudência" no Oriente Médio; condena sanções sem aval do CS/ONU ("Apelamos para a eliminação de tais medidas ilegais..."); "ataques deliberados" a infra civil e usinas pacíficas sob salvaguardas AIEA; crítica a sanções a Cuba e ação militar dos EUA no Irã (Gazeta do Povo); "serious concerns" com tarifas contrárias à OMC (TASS); G20 "inaceitável" alterar composição + apoio pleno à África do Sul (247); Modi pede reforma do CSNU + mecanismo de continuidade (247).
- **Falas:** Xi — guerra "causou graves prejuízos... não serve aos interesses comuns"; BRICS "grupo de liderança"; "A China está disposta..." (Gazetaweb). Pezeshkian — "Não precisamos de um policial na região..." c/ Anwar Ibrahim (O Globo); Palestina "voz da justiça" (247). Putin — ampliação CSNU, multipolar "enfrenta resistência" (Interfax via O Globo).
- **Contraponto Trump (RETIFICADO ~17:1x):** ❌ VERSÃO ORIGINAL ERRADA dizia "8 de setembro de 2026, Trump declarou o BRICS 'morto'" — a frase é REAL mas de **14/02/2025** (Fortune, Times of India, ThePrint); a página de VÍDEO do agregador oneindia (09/09/2026) reciclou a aspa com data nova; nenhuma fonte primária/independente confirma fala fresca. ✅ VERSÃO NOVA no post: "morto" datado de fevereiro de 2025 + contraponto fresco = **projeto de sanções Graham**: Senado dos EUA aprovou em 07/08/2026 (86×11) tarifa de até 100% sobre Índia, China e mais 3 países compradores de petróleo russo; Câmara vota na semana de 14/09 (Reuters 11/09); empresários dos EUA pedem fim da tarifa de 100% (Hindustan Times 11/09); senador: "estamos acertando a Índia e a China, os principais culpados" (ToI/Firstpost 29/07); projeto batizado em homenagem a Lindsey Graham, morto em jul/2026 (CNN). Canadá tarifou US$ 20 bi (~R$ 102 bi, cotação 5,1262 de 11/09 19:30) em 08/09 (247); Índia cautelosa, rejeita moeda comum (Outlook/Srikumar Menon).
- **Guerra (contexto):** EUA+Israel atacaram o Irã no fim de fev/2026; Irã bloqueou Ormuz; 6 meses; base Al Minhad atingida fim de ago/2026; Saudita fechou oleoduto; houthis tomaram ilha em Bab el-Mandeb (O Globo+InfoMoney).

## Fontes salvas (html bruto, para re-verificação)

/tmp/brics_oglobo.html, brics_infomoney.html, brics_opovo.html, brics_gw_xi.html, brics_247.html, brics_247_pez.html, brics_tass.html, brics_outlook.html, brics_trump_dead.html (Dell, apagáveis após publish).

## Comandos-chave (provas)

- `wp post create /tmp/brics_materia1.html --post_status=draft --post_author=5486 --post_title='...' --post_category='5003,5053' --tags_input='...' --post_excerpt='...'` → **Success: Created post 270342**
- 🔴 **Aprendizado:** `--post_category` exige IDs por VÍRGULA; `'5003 5053'` com espaço → `Error: No such post category`. (Corrigir o prompt da automação na próxima revisão — o fórum §1 já cita a forma certa.)
- `wp media import ... --post_id=270342 --featured_image --caption='...' --alt='...'` → attachment **270343**
- Verificação: `wp post get 270342` (draft/5486) + `wp post term list` (5003+5053+11 tags) + `_thumbnail_id`=270343 + legenda ok + grep h3=5, travessão=0.
- Anti-duplicata: `wp post list --s='BRICS'` — mais próximos: draft 270268 (petróleo/Irã, ângulo diferente) e publish 269716 (degelo Xi-Índia, 11/09); sem sobreposição.

## wp-admin

https://www.ocafezinho.com/wp-admin/post.php?post=270342&action=edit

## Estado

- **O que aconteceu:** execução 1/6 completa, rascunho 270342 no ar c/ capa e taxonomia.
- **O que falta:** 5 execuções; Miguel revisar/publicar o 270342 (furo do dia).
- **Pendência registrada:** título "Sob ameaça de Trump, BRICS condena tarifas unilaterais" tem 54 chars (ok p/ push).
