from abc import ABC, abstractmethod

from chromadb.api.types import (
    Embeddings,
    Metadata,
)


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