from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .curadoria_tese import V4CuradoriaTese
from .loader import DirectiveLoader


class V4CuradoriaABExperiment:
    """Experimento A/B local para comparar texto sem curadoria contra texto curado."""

    def __init__(self, root: str | Path = ".") -> None:
        self.loader = DirectiveLoader(root)
        self.root = self.loader.root
        self.curadoria = V4CuradoriaTese(self.root)

    def run_261439(self, execute: bool = False) -> dict[str, Any]:
        auditado_path = self.root / "v4_data/auditado/v4_real_001.json"
        original_path = self.root / "v4_data/producao/v4_real_001.producao.json"
        auditado = self._read_json(auditado_path)
        original = self._read_json(original_path)
        leitura = {
            "fonte": "manual_editor",
            "timestamp_brt": "2026-07-09T00:00:00-03:00",
            "resumo_consenso": (
                "A leitura corrente trata a pauta como disputa Lula x Flavio Bolsonaro sobre tarifa, "
                "soberania e guerra de narrativas antes da eleicao."
            ),
            "fontes_consultadas": [
                "forum_v4_curadoria_tese_editorial_20260708",
                "feedback_editorial_miguel",
            ],
        }
        curadoria = self.curadoria.create(auditado, leitura, curador_modelo="mock-curador-v4-ab")
        variant_b = self._variant_b(auditado, original, curadoria)
        package = {
            "schema_version": "v1",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "experiment_id": "ab_261439_curadoria_v4_fase_1",
            "mode": "dry_run_ab_261439",
            "blind_review_required": True,
            "external_publish": False,
            "real_wordpress_draft": False,
            "item_id": auditado["item_id"],
            "post_id": 261439,
            "curadoria_id": curadoria["curadoria_id"],
            "variants": [
                {
                    "label": "A",
                    "source": "v4_data/producao/v4_real_001.producao.json",
                    "curadoria_id": None,
                    "titulo": original.get("titulo"),
                    "texto": original.get("texto_dry_run") or original.get("conteudo"),
                },
                {
                    "label": "B",
                    "source": "v4_data/producao/v4_real_001.variant_b.producao.json",
                    "curadoria_id": curadoria["curadoria_id"],
                    "titulo": variant_b["titulo"],
                    "texto": variant_b["texto_dry_run"],
                },
            ],
            "interpretacao": {
                "n_equals_1": True,
                "uso": "smoke test editorial; nao institucionaliza a etapa sozinho",
                "criterio": "a versao vencedora deve entregar promessa ao leitor, nao apenas polimento",
            },
        }
        paths = {
            "curadoria": "v4_data/curadoria/v4_real_001.curadoria.json",
            "variant_b": "v4_data/producao/v4_real_001.variant_b.producao.json",
            "package": "agent_data/v4/ab_experiments/ab_261439_curadoria_v4_fase_1.json",
        }
        if execute:
            self._write_json(self.root / paths["curadoria"], curadoria)
            self._write_json(self.root / paths["variant_b"], variant_b)
            self._write_json(self.root / paths["package"], package)
        return {"ok": True, "mode": "written" if execute else "dry_run", "paths": paths, "package": package}

    def _variant_b(
        self,
        auditado: dict[str, Any],
        original: dict[str, Any],
        curadoria: dict[str, Any],
    ) -> dict[str, Any]:
        title = "Tarifa dos EUA transforma Trump em problema eleitoral para Flávio Bolsonaro"
        sources = auditado.get("fontes") or []
        source_links = " e ".join(f'<a href="{url}">{label}</a>' for label, url in zip(["Associated Press", "El País"], sources))
        text = (
            "<p>Flávio Bolsonaro foi a Washington tentar conter uma tarifa associada ao campo político "
            "que a direita brasileira costuma tratar como aliado. Esse é o ponto que muda a matéria: "
            "a pressão de Trump contra produtos brasileiros pode virar custo econômico, reacender a pauta "
            "da soberania e entregar a Lula uma bandeira eleitoral que ele sabe usar.</p>\n\n"
            "<p>Segundo a Associated Press, a administração Trump voltou a discutir uma tarifa de 25% "
            "sobre produtos brasileiros, apesar de os Estados Unidos manterem superávit comercial com o Brasil. "
            "Flávio argumentou ao USTR que a pressão tarifária poderia fortalecer Lula. A pergunta editorial, "
            "portanto, não é apenas quem venceu a troca de acusações; é por que o próprio bolsonarismo precisou "
            "pedir a Washington que não criasse um problema para sua campanha.</p>\n\n"
            "<p>A contradição fica mais concreta quando o Pix entra na mesa. O El País registrou que o sistema "
            "brasileiro de pagamentos se tornou ponto sensível porque autoridades americanas o veem como concorrente "
            "dos meios privados de pagamento. Flávio tenta defender o Pix sem romper com a lógica de acomodação aos EUA, "
            "e Lula explora esse flanco como disputa de soberania financeira.</p>\n\n"
            "<p>A consequência política é direta: a direita brasileira descobre que alinhamento externo tem custo "
            "quando a potência aliada transforma disputa política em tarifa contra o país. Lula tenta ocupar o lugar "
            "de defensor do interesse nacional; Flávio tenta impedir que a própria referência internacional da direita "
            "entregue esse terreno ao adversário.</p>\n\n"
            f"<p><strong>Fontes:</strong> {source_links or original.get('fonte', 'AP + El País')}.</p>"
        )
        return {
            "item_id": auditado["item_id"],
            "curadoria_id": curadoria["curadoria_id"],
            "editoria": auditado["editoria"],
            "titulo": title,
            "primary_entity": auditado.get("primary_entity"),
            "status": "producao_ab_dry_run",
            "texto_dry_run": text,
            "fatos_travados": curadoria.get("fatos_travados", []),
            "promessa_ao_leitor": curadoria["promessa_ao_leitor"],
            "frame_visual": curadoria["frame_visual"],
            "manifesto": {
                "step": "ab_261439_variant_b",
                "external_publish": False,
                "real_wordpress_draft": False,
                "curadoria_id": curadoria["curadoria_id"],
                "modo_experimento": "dry_run_ab_261439",
            },
        }

    @staticmethod
    def _read_json(path: Path) -> dict[str, Any]:
        return json.loads(path.read_text(encoding="utf-8"))

    @staticmethod
    def _write_json(path: Path, payload: dict[str, Any]) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
