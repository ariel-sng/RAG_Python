from src.repositories.vector_store import VectorStore
from src.RAG.embedding_generator import EmbeddingGenerator
from src.models.search_result import SearchResult   

class RagQueryService:

    def __init__(
        self,
        embedding_generator: EmbeddingGenerator,
        vector_store: VectorStore,
    ):
        self.embedding_generator = embedding_generator
        self.vector_store = vector_store

    def search(
        self,
        question: str,
        k: int = 5,
    ) -> list[SearchResult]:
        embedding = self.embedding_generator.generate(
            [question]
        )[0]

        return self.vector_store.search(
            embedding=embedding,
            k=k,
        )