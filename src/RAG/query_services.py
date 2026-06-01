import json

from src.models.search_result import SearchResult
from src.models.rag_search_result import RAGSearchResult
from src.repositories.vector_store import VectorStore
from src.RAG.embedding_generator import EmbeddingGenerator
from src.RAG.prompt_builder import PromptBuilder
from src.RAG.llm_generator import LLMGenerator 

class RagQueryService:

    def __init__(
        self,
        embedding_generator: EmbeddingGenerator,
        vector_store: VectorStore,
        prompt_builder: PromptBuilder,
        llm_generator: LLMGenerator,
    ):
        self.embedding_generator = embedding_generator
        self.vector_store = vector_store
        self.prompt_builder = prompt_builder
        self.llm_generator = llm_generator

    def search(
        self,
        question: str,
        k: int = 5,
    ) -> list[RAGSearchResult]:
       
        embedding = self.embedding_generator.generate(  [question] )[0]

        return self.vector_store.search(
            embedding=embedding,
            k=k,
        )
    
    def answer(
        self,
        question: str,
        k: int = 5,
    ) -> SearchResult:

        results = self.search(
            question=question,
            k=k,
        )

        prompt = self.prompt_builder.build(
            question=question,
            context_chunks=results,
        )
        
        system_answer = self.llm_generator.generate(
            prompt
        )

        return SearchResult(
            question=question,
            answer=system_answer,
            chunks=results,
        )
    

    
    def save_rag_result(
        self,
        result: SearchResult,
        output_file: str = "rag_result.json",
    ):
        print("Guardando resultado del RAG en formato JSON...")
        data = {
            "question": result.question,
            "system_answer": result.answer,
            "chunks": [
                {
                    "document": chunk.document,
                    "distance": chunk.distance,
                    "metadata": chunk.metadata,
                }
                for chunk in result.chunks
            ],
        }

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        print("Archivo guardado con éxito.")