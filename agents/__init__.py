"""
Agents package for The Price is Right deal hunting system.

This package contains various AI agents that work together to find and evaluate deals.
"""

from .agent import Agent
from .deals import Deal, DealSelection, Opportunity, ScrapedDeal
from .planning_agent import PlanningAgent
from .scanner_agent import ScannerAgent
from .ensemble_agent import EnsembleAgent
from .specialist_agent import SpecialistAgent
from .frontier_agent import FrontierAgent
from .random_forest_agent import RandomForestAgent
from .messaging_agent import MessagingAgent

__all__ = [
    'Agent',
    'Deal',
    'DealSelection',
    'Opportunity',
    'ScrapedDeal',
    'PlanningAgent',
    'ScannerAgent',
    'EnsembleAgent',
    'SpecialistAgent',
    'FrontierAgent',
    'RandomForestAgent',
    'MessagingAgent',
]

__version__ = '1.0.0'
