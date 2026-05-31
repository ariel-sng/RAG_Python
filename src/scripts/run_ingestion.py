from pathlib import Path
import sys
from openai import OpenAI

from src.config.settings import Settings
from src.repositories.chroma_vector_store import ChromaVectorStore
from src.RAG.ingestion_service import RagIngestionService
from src.RAG.document_loader import DocumentLoader
from src.RAG.embedding_generator import OpenAIEmbeddingGenerator
from src.RAG.text_chunker import TextChunker


def main() -> None:
    
    ### MANEJO DE ARGUMENTOS ###
    
    args = sys.argv[1:]
    reload = "--reload" in args

    if reload:
        args.remove("--reload")

    # si no queda solamente un argumento, es un error ya que debería ser máximo 2
    if len(args) != 1:
        print("Uso incorrecto: uv run python -m src.scripts.run_ingestion [--reload] <archivo>")
        sys.exit(1)

    file_path = args[0]

    ### CREACIÓN DE COMPONENTES  ###

    vector_store = ChromaVectorStore(
        persist_directory="storage/chroma",
        collection_name="documents",
        reload=reload,
    )


    client = OpenAI(
        api_key=Settings.OPENAI_API_KEY,
    )

    ingestion_service = RagIngestionService(
        loader=DocumentLoader(),
        chunker=TextChunker(
            chunk_size=10, # Por ahora, pongo un chunk size muy pequeño para probar, sé perfectamente que es ridículo
            chunk_overlap=2,
        ),
        embedding_generator=OpenAIEmbeddingGenerator(
            client=client,
        ),
        vector_store=vector_store,
    )

    ### LA INGESTA  ###

    print(f"Iniciando ingestión del archivo: {file_path}")
    try:
        ingestion_service.ingest(
            file_path=file_path,
            metadata={
                "file_name": Path(file_path).name, 
                # Por ahora, solo agrego como metada el nombre del archivo, pero se pueden agregar más metadatos a futuro
            },
        )
    except Exception as ex:
        print(f"ERROR inesperado: {ex}")
        sys.exit(1)


    print(f"Ingestión completada correctamente: {file_path}")


if __name__ == "__main__":
    main()