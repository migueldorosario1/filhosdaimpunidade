# -*- coding: utf-8 -*-
# Teste standalone do juiz de qualidade (sem tocar no WP, sem rodar ciclo)
import sys, json
sys.path.insert(0, "/root/v4_labs")
from codigo import v41_ciclo as m

env = m._env()

casos = [
    ("pauta", "economia",
     "Alcaraz supera pressão contra da torcida e Tommy Paul e está nas quartas do US Open",
     "O espanhol Carlos Alcaraz venceu o norte-americano Tommy Paul por 3 sets a 1, com parciais de 6/4, 3/6, 6/2 e 7/5, e avançou às quartas de final do Aberto dos Estados Unidos. A torcida local fez barulho contra o espanhol durante toda a partida. Alcaraz enfrenta agora o vencedor de Fritz e Tiafoe."),
    ("pauta", "ciencia",
     "Восемь аниме-плееров рунета изнутри: шифр Цезаря, пустой параметр и домен, который не существует",
     "Обзор восьми аниме-плееров, популярных в рунете. Автор разбирает технические особенности каждого: от шифрования субтитров до пустых параметров API."),
    ("pauta", "economia",
     "Senado aprova política de minerais críticos com R$ 7 bilhões e poder de barrar venda de mineradoras",
     "O Senado aprovou a criação da política nacional de minerais críticos, com fundo de R$ 7 bilhões e poder de veto do governo sobre a venda de mineradoras estratégicas a estrangeiros. O texto segue para sanção. A medida responde à disputa global por lítio, nióbio e terras raras entre EUA e China."),
    ("pauta", "nacional",
     "Os 11 produtos mais vendidos na Shopee: o que vender (ou comprar) em 2026",
     "Levantamento aponta os produtos mais vendidos na Shopee em 2026: capinha de celular, fone bluetooth, garrafa térmica, organizador de gaveta e outros itens baratos dominam o marketplace."),
    ("texto", "ciencia",
     "Artigo revisado e aprovado pelos critérios da casa",
     "PARECER DA REVISÃO: o texto atende aos critérios de clareza, tem três fontes primárias cruzadas e não apresenta vícios de IA. Recomenda-se a publicação. O artigo foi verificado pelo fact-check e não há pendências. Nada a corrigir."),
]

for modo, vert, tit, txt in casos:
    r = m._juiz_qualidade(env, vert, tit, txt, modo=modo)
    print(json.dumps({"modo": modo, "vertical": vert, "titulo": tit[:60],
                      "aprova": r.get("aprova"), "total": r.get("total"),
                      "notas": r.get("notas"), "motivo": r.get("motivo"),
                      "modelo": r.get("modelo")}, ensure_ascii=False))
