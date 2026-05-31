from pathlib import Path
import sys
from openai import OpenAI

from src.config.settings import Settings
from src.repositories.chroma_vector_store import ChromaVectorStore
from src.services.document_ingestion_service import DocumentIngestionService
from src.services.document_loader import DocumentLoader
from src.services.embedding_generator import OpenAIEmbeddingGenerator
from src.services.text_chunker import TextChunker


def main() -> None:
    args = sys.argv[1:]

    reload = False

    if "--reload" in args:
        reload = True
        args.remove("--reload")

    if len(args) != 1:
        print(
            "Uso: uv run python -m src.scripts.run_ingestion [--reload] <archivo>"
        )
        sys.exit(1)

    file_path = args[0]

    if not Path(file_path).exists():
        print(f"Archivo no encontrado: {file_path}")
        sys.exit(1)

    client = OpenAI(
        api_key=Settings.OPENAI_API_KEY,
    )

    vector_store = ChromaVectorStore(
        persist_directory="storage/chroma",
        collection_name="documents",
    )

    if reload:
        print("Limpiando colección...")
        vector_store.reset()

    ingestion_service = DocumentIngestionService(
        loader=DocumentLoader(),
        chunker=TextChunker(
            chunk_size=500,
            chunk_overlap=100,
        ),
        embedding_generator=OpenAIEmbeddingGenerator(
            client=client,
        ),
        vector_store=vector_store,
    )

    ingestion_service.ingest(
        file_path=file_path,
        metadata={
            "file_name": Path(file_path).name,
        },
    )

    print(
        f"Ingestión completada correctamente: {file_path}"
    )


if __name__ == "__main__":
    main()