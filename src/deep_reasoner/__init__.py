"""
deep-reasoner
================

A powerful Python package extracted from OSA.
"""

__version__ = "0.1.0"
__author__ = "OSA Contributors"

from .core import DeepReasoner
from .exceptions import DeepReasonerError

__all__ = [
    "DeepReasoner",
    "DeepReasonerError",
]
