import argparse

from openai import OpenAI



from src.config.settings import Settings
from src.repositories.chroma_vector_store import ChromaVectorStore
from src.RAG.embedding_generator import OpenAIEmbeddingGenerator
from src.RAG.query_services import RagQueryService


def main() -> None:

    ### MANEJO DE ARGUMENTOS ###

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "question",
        type=str,
    )

    parser.add_argument(
        "--k",
        type=int,
        default=5,
    )

    args = parser.parse_args()

    ### CREACIÓN DE COMPONENTES  ###

    client = OpenAI(
        api_key=Settings.OPENAI_API_KEY,
    )

    openai_embedding_generator = OpenAIEmbeddingGenerator(
        client=client
    )

    vector = ChromaVectorStore(
            persist_directory="storage/chroma",
            collection_name="documents"
            )
    
    query_service = RagQueryService(
        embedding_generator=openai_embedding_generator,
        vector_store=vector
    )

    ### CONSULTA AL RAG  ###

    results = query_service.search(
        question=args.question,
        k=args.k,
    )

    for i, result in enumerate(results, start=1):
        print(f"[{i}]")
        print(f"Similarity: {result.similarity:.4f}")

        file_name = result.metadata.get("file_name")

        if file_name:
            print(f"File: {file_name}")

        print()
        print(result.document)
        print("\n" + "-" * 80 + "\n")


if __name__ == "__main__":
    main()