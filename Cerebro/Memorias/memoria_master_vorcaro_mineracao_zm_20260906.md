# Memória técnica — Master/Vorcaro/Mineração onda 2 (ZM, 06/09/2026)

Par do fórum: `Foruns/forum_master_vorcaro_mineracao_zm_20260906.md`

## Receitas que funcionaram

1. TCU atrás de WAF: o fetcher é bloqueado (página de firewall, código extB) — NÃO contornar. O caminho foi o REPÓRTER no navegador: Pesquisa Integrada (pesquisa.apps.tcu.gov.br) → busca "4592 2026" abre o acórdão com botão Download (PDF+RTF); busca do número do processo abre a página do processo; o link "CONECTA TCU: Vista eletrônica" abre o andamento COMPLETO (colar = evidência); as PEÇAS completas exigem cadastro/perfil ("você não tem perfil para acessar os autos") — só "Peças recentes — transparência ativa" são públicas.
2. Desbloqueio das peças TCU pela ORIGEM: peças que são documentos da ANM (Nota Técnica, Votos, Decisões, NTs CED/SOD) podem ser pedidas por LAI à ANM — mais rápido que LAI ao TCU. Textos prontos em `fontes-zm-master-onda-2-2026-09-06/lai-anm-textos-prontos.md`.
3. CVM postback ASP.NET: extrair __VIEWSTATE/GENERATOR/EVENTVALIDATION BRUTOS (sem encode duplo!) da página salva, POST com curl --data-urlencode NA MESMA SESSÃO de cookies; resposta 302 → /SWB/Arquivos/BuscaArquivo.aspx → seguir -L = PDF. Os 5 documentos da DF saem assim (HLDemFinanc, HLParAudInd, HLRelInstitCustod, HLEncargFdo, HLincVart14).
4. Colunas da CDA CVM: extrair células por <td> com índice — célula [9] = Posição Final mercado, [10] = % PL (vazio quando PL=zero). NÃO inferir vendas.
5. gov.br/Plone: PDF oficial de página "file" = URL + /@@download/file.
6. Registrar cada download com SHA-256 + timestamp BRT no MANIFEST (padrão da pasta).

## Pegas/armadilhas

- urllib travou sem erro na CVM (use curl com --max-time).
- RTF de acórdão pode ter 100MB+ — não commitar; só o PDF.
- O resumo "Visão geral do documento gerada com IA" do TCU NÃO é fonte — o documento começa depois dele.
- "274 áreas" (TCU 4592) vs "276 direitos" (alegação da 3D na peça 92) vs "116 áreas" (recorte imprensa de minerais críticos) — recortes diferentes, nunca misturar.
- Valor reduzido da 3D tem DUAS grafias oficiais: R$ 3.756.100,00 (ata 66ª ROP + voto do 870) e R$ 3.757.610,00 (manifestação da 3D, peça 92). Citar com fonte.
- Conecta lista ciências com NOME DO SERVIDOR da ANM e número do ofício — bom pra datar prazos (ciência 13/08/2026 → 90 dias → 11/11/2026).
- LAI: plataforma agora se chama Informa.BR (ex-Fala.BR); protocolo 48003.018654/2026-33 (ANM, prazo 28/09/2026).

## Commits principais (repo migueldorosario1/cafezinho)

Lote 1: 26a42f64…3394fb15 (21 arquivos + MANIFEST). Lote 2: b8a2d1f6 (continuidade) + 5b9e17f3 (receita 3D). Lote TCU: 21fedb65…9647acb4 (15 arquivos). 870: 1e1a9baf/5d08fabf/7bddbefe. LAI: 4d966ba9. Continuidade v2: 103fab74.
