# Memória — EMU-8 título genérico: caso Janmashtami/Krishna (post 268998) — log técnico

**Data:** 04/09/2026 18:05→18:2x BRT · **Agente:** ZCode/GLM-5.3 (Dell) · **Sessão:** ordem do Miguel via chat com URL do post.

## Sequência executada

1. **Consulta prévia:** MONITORAMENTO_DE_TRABALHO lido (linha própria registrada; sem colisão — sessão YouTube paralela mexe em cats 28/20751, arquivos distintos). Post identificado via REST pública (UA navegador): id 268998, autor 5470, publish 14:48.
2. **Correção no canônico** (ssh alias `cafezinho-wp`):
   - `sudo -u www-data wp --path=/var/www/ocafezinho post update 268998 --post_title='Festa hindu celebra nascimento de divindade com lição sobre agir sob incerteza'` → Success.
   - `post get --field=post_name` → slug `janmashtami-celebra-krishna-com-licao-para-agir-sob-incerteza` PRESERVADO.
   - Purge: `wp eval 'rocket_clean_domain(); rocket_clean_minify();'` → "domain OK minify OK" (o purge_rocket.php standalone é morto — NODE_COFRE).
3. **Provas front** (curl UA navegador, `?v=2` para contornar cache de URL exata): `<title>`, `og:title` e `<h1 itemprop="headline">` com o título novo; home contém o título novo 1×; zero ocorrência do velho.
4. **EMU-8 nos manuais:**
   - `Cerebro/Estilo/MANUAL_DE_ESTILO_UNIFICADO.md`: checklist "as 8 regras" → "as **9** regras" + regra 9 (nome próprio desconhecido → genérico) + entrada EMU-8 datada no apêndice de emendas.
   - `Cerebro/Estilo/MANUAL_DE_ESCRITA_PORTAL.md`: novo bullet na seção 8 (estrutura) com o par ❌/✅ Janmashtami.
5. **Espelho NYC** (enforcement): `cp` backup `.bak_pre_emu8_20260904` → `scp` do portal atualizado → `grep -c 'EMU-8'` = 1 e md5 `aaae40683deb8ce9e52592fb73ce71e3` IGUAL nos dois lados.
6. **Catalogação:** NODE_ESTILO (linha EMU-8) + NODE_ATUALIZACOES (entrada) + este Tema Duplo. Memória ZM atualizada (`titulos-portal-uma-frase-sem-sigla-cargo.md`).

## Por que o espelho NYC resolve o enforcement

`v41_ciclo.py:587` monta o briefing do redator com `dados/MANUAL_DE_ESCRITA_PORTAL.md` (11.284c, provado em 02/09 na telemetria do briefing). A TESE dinâmica também lê linha+manual (V41_TESE_FRONTIER). Logo, EMU-8 entra no prompt do redator V4.1 na próxima corrida — sem tocar em código do ciclo.

## Caminhos e provas

| Item | Caminho / valor |
|---|---|
| Post | 268998 · autor 5470 · https://www.ocafezinho.com/2026/09/04/janmashtami-celebra-krishna-com-licao-para-agir-sob-incerteza/ |
| Título velho → novo | «Janmashtami celebra Krishna com lição para agir sob incerteza» → «Festa hindu celebra nascimento de divindade com lição sobre agir sob incerteza» |
| Backup do título | `Cerebro/Backups/posts_editados/268998_titulo_pre_emu8_20260904.md` |
| Manual NYC | `/root/v4_labs/dados/MANUAL_DE_ESCRITA_PORTAL.md` (backup `.bak_pre_emu8_20260904`) |
| md5 par | `aaae40683deb8ce9e52592fb73ce71e3` |
| Rollback título | wp post update com título antigo + purge rocket (comando no backup) |

## Pendências

- R1/R2 Tencent: EMU-8 entra no próximo bolo de diretrizes (atual = EMU-6 de 03/09).
- Gap estrutural conhecido (caso Kast): auditor advisor de títulos cobre só autor 5786; V4.1 publica pelo 5470.
- Não fiz varredura de outros títulos com nomes próprios desconhecidos (o Miguel apontou 1 post; oferta registrada no fórum).

## O que aconteceu / o que falta / o que preciso de você (Miguel)

Correção+regra+enforcement feitos e provados. Falta só a difusão para R1/R2 (próximo bolo). Do Miguel: nada obrigatório.
