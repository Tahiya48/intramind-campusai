from dataclasses import dataclass
from typing import Optional


@dataclass
class Document:
    """
    Standard representation of content entering the RAG pipeline.
    """

    text: str
    source: str
    document_type: str
    title: Optional[str] = None
    page: Optional[int] = None
    domain: Optional[str] = None
    chunk_index: Optional[int] = None