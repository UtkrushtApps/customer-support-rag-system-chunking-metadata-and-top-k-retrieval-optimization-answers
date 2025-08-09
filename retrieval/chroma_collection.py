from chromadb.config import Settings
from chromadb import Client
from typing import List, Dict, Any
from chromadb.utils import embedding_functions

CHUNK_SIZE = 512
OVERLAP = 200

CHROMA_COLLECTION_NAME = "support_chunks"

CHROMA_SETTINGS = Settings(
    is_persistent=True,
    persist_directory="./chroma_db",
    anonymized_telemetry=False,
)
# Set optimal ANN search config for improved recall and low latency
ANN_COLLECTION_SETTINGS = {
    "distance_function": "cosine",
    "hnsw:space": "cosine",
    "hnsw:ef": 128,
    "hnsw:ef_construction": 200,
    "hnsw:M": 32  # Higher for better recall
}

def get_or_create_collection():
    client = Client(CHROMA_SETTINGS)
    ef = embedding_functions.DefaultEmbeddingFunction()
    try:
        collection = client.get_or_create_collection(
            name=CHROMA_COLLECTION_NAME,
            embedding_function=ef,
            metadata=ANN_COLLECTION_SETTINGS
        )
    except Exception:
        # fallback if already exists
        collection = client.get_collection(
            name=CHROMA_COLLECTION_NAME,
            embedding_function=ef
        )
    return collection
