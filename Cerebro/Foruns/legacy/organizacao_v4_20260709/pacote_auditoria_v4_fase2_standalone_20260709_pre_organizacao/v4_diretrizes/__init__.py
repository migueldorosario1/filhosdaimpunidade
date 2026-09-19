"""Camada de diretrizes externas do V4.

Este pacote nao chama LLM e nao publica nada. Ele apenas carrega arquivos
externos e monta um contrato editorial em modo local/dry-run.
"""

from .composer import ContractComposer
from .content_ingestion import V4ContentIngestion
from .curadoria_tese import V4CuradoriaTese
from .ab_experiment import V4CuradoriaABExperiment
from .agentes import TechnicalAgentFactory
from .camadas import LayerAccessController
from .loader import DirectiveLoader
from .fluxo import V4DryRunFlow
from .feedback import V4EditorFeedbackStore
from .imagem_destacada import V4FeaturedImageEvaluator
from .llm_adapter import V4LLMAdapter
from .llm_dashboard import V4LLMDashboard
from .llm_decisions import V4LLMDecisionStore
from .llm_healthcheck import V4LLMHealthcheck
from .llm_orchestrator import V4LLMOrchestrator
from .media_audit import V4AuditedMediaStore
from .media_sources import V4MediaSourceCollector
from .memoria import V4MemoryStore
from .model_router import V4ModelRouter
from .operacao import V4OperationRunner
from .operational_dashboard import V4OperationalDashboard
from .recompute_costs import V4CostRecomputer
from .redator_shadow import V4ShadowRedator
from .telemetry import V4Telemetry
from .wordpress_publicador import V4WordPressPublisher
from .wordpress_media import V4WordPressMediaMapper
from .schema import EditorialContract

__all__ = [
    "ContractComposer",
    "V4ContentIngestion",
    "V4CuradoriaABExperiment",
    "V4CuradoriaTese",
    "DirectiveLoader",
    "EditorialContract",
    "LayerAccessController",
    "TechnicalAgentFactory",
    "V4FeaturedImageEvaluator",
    "V4DryRunFlow",
    "V4EditorFeedbackStore",
    "V4LLMAdapter",
    "V4LLMDashboard",
    "V4LLMDecisionStore",
    "V4LLMHealthcheck",
    "V4LLMOrchestrator",
    "V4AuditedMediaStore",
    "V4MediaSourceCollector",
    "V4MemoryStore",
    "V4ModelRouter",
    "V4OperationRunner",
    "V4OperationalDashboard",
    "V4CostRecomputer",
    "V4ShadowRedator",
    "V4Telemetry",
    "V4WordPressPublisher",
    "V4WordPressMediaMapper",
]
