# -*- coding: utf-8 -*-
# PATCH R2 (dsn_revisor2.py) — Missão Qualidade 07/09/2026 (ordem Miguel:
# "O R1 e o R2 tem que melhorar muito... tem que ter curadoria... padrão Metrópoles/Fórum")
# 1) novo item 4) QUALIDADE DA PAUTA (gate editorial no revisor final)
# 2) bolo do título += EMU-9 (80c + gancho tech) e EMU-10 (torneio traduzido/esporte BR)
import shutil, py_compile

P = "/home/ubuntu/dsn_revisor2/dsn_revisor2.py"
shutil.copy2(P, P + ".bak_pre_juiz_qualidade_20260907")
src = open(P, encoding="utf-8").read()

A1 = '''Caso-escola: ❌ EUA barram robôs e drones, mas China mantém escala → ✅ Governo Trump barra importação de drones e robôs da China.\\\\n'
'''
assert src.count(A1) == 1, "A1: " + str(src.count(A1))
R1 = '''Caso-escola: ❌ EUA barram robôs e drones, mas China mantém escala → ✅ Governo Trump barra importação de drones e robôs da China. (7) CONTAGEM EMU-9 (06/09): máximo 80 caracteres com espaços — acima disso, corte; tecnologia precisa de gancho humano ou geopolítico (nunca nicho seco de biblioteca/app); torneio estrangeiro TRADUZIDO (Aberto dos EUA, não US Open) e esporte estrangeiro só com brasileiro em campo ou futebol (EMU-10).\\\\n'
'''
src = src.replace(A1, R1)

A2 = '''            "3) OLHO/excerto: coerente com o título e o texto?\\n"
            "Responda EXATAMENTE no formato:\\n"'''
assert src.count(A2) == 1, "A2: " + str(src.count(A2))
R2 = '''            "3) OLHO/excerto: coerente com o título e o texto?\\n"
            "4) QUALIDADE DA PAUTA — padrão da casa 07/09/2026 (ordem Miguel: a referência de "
            "interesse é a home da Metrópolis e da revista Fórum): a matéria interessa ao leitor "
            "brasileiro? Responda VEREDITO: CORRECOES com pendência «FORA DO PADRÃO DE QUALIDADE: "
            "...» se for: matéria de serviço/listicle de vendas, loteria, guia de trânsito, dica de "
            "compra; esporte estrangeiro sem brasileiro e sem futebol; tecnologia estrangeira de "
            "nicho sem impacto global ou brasileiro (app/biblioteca de outro país, review de "
            "software, resumo de produtos); metalinguagem (parecer ou relatório sobre a própria "
            "matéria — nota zero, nunca aprovar).\\n"
            "Responda EXATAMENTE no formato:\\n"'''
src = src.replace(A2, R2)

open(P, "w", encoding="utf-8").write(src)
py_compile.compile(P, doraise=True)
print("R2 PATCH + PY_COMPILE OK")
