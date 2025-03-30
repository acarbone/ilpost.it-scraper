from dataclasses import dataclass
from typing import Optional

@dataclass
class Article:
    """Data class representing an article"""
    title: str
    link: str
    date: Optional[str] = None
