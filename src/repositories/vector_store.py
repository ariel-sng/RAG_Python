from abc import ABC, abstractmethod

from chromadb.api.types import (
    Embedding,
    Embeddings,
    Metadata,
)

from src.models.search_result import SearchResult

class VectorStore(ABC):
    '''
        Clase abstracta para manejar el almacenamiento de vectores.
        Quieren SOLID? Acá hay SOLID.
    '''

    @abstractmethod
    def save(
        self,
        embeddings: Embeddings,
        chunks: list[str],
        metadata: Metadata,
    ) -> None:
        pass

    @abstractmethod
    def search(
        self,
        embedding: Embedding,
        k: int,
    ) -> list[SearchResult]:
        pass