"""
The Price is Right - Deal Hunting Agentic AI System

An autonomous multi-agent system that finds online deals by collaborating with
a fine-tuned LLM, RAG pipeline, and traditional ML models.
"""

__version__ = '1.0.0'
__author__ = 'Your Name'
__email__ = 'your.email@example.com'

from .deal_agent_framework import DealAgentFramework
from .items import Item
from .testing import Tester

__all__ = [
    'DealAgentFramework',
    'Item',
    'Tester',
]
