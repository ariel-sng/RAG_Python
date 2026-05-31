from typing import cast
from uuid import uuid4

import chromadb
from chromadb.api.types import (
    Embeddings,
    Metadata,
    Metadatas,
)

from src.repositories.vector_store import VectorStore


class ChromaVectorStore(VectorStore):

    def __init__(
        self,
        persist_directory: str = "storage/chroma",
        collection_name: str = "documents",
    ):
        self.client = chromadb.PersistentClient(
            path=persist_directory
        )

        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )

    def save(
        self,
        embeddings: Embeddings,
        chunks: list[str],
        metadata: Metadata,
    ) -> None:

        ids = [
            str(uuid4())
            for _ in chunks
        ]

        metadatas: Metadatas = cast(
            Metadatas,
            [
                {
                    **metadata,
                    "chunk_index": i,
                    "total_chunks": len(chunks),
                }
                for i in range(len(chunks))
            ]
        )

        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=chunks,
            metadatas=metadatas,
        )

    def reset(self) -> None:
        self.client.delete_collection(
            self.collection.name
        )

        self.collection = self.client.get_or_create_collection(
            name=self.collection.name
        )