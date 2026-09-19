# Lição: GATE-TEXTO (scan_ponte_consenso) (2026-09-01)

**O quê:** Minha regex casava ID + 'consenso|resgate|elegível' e a CL-024 CONDICIONADA virou sinal verde → texto sujo ao ar. Fix: MARCADORES_DECISAO (CL-\d{4,}) obrigatório + MARCADORES_PEDIDO (condicionado/só após/aguardando/...) bloqueia.

**Por quê:** caso real da operação da casa.

**Como aplicar:** ver MEMORIA_VIVA (regras).
