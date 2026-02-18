"""
Connect to ChromaDB using persistent local client
1. get_collection() for storing/querying vectors
2. test_chroma_connection() for health checks.
"""

import chromadb
from chromadb.utils import embedding_functions
from config.settings import settings
import os
from utils.logger import logger


def get_chroma_client() -> chromadb.CloudClient:
    """Connect to ChromaDB Cloud using CloudClient (official method)."""
    client = chromadb.CloudClient(
        api_key = settings.CHROMA_API_KEY,
        tenant = settings.CHROMA_TENANT,
        database = settings.CHROMA_DATABASE,
    )
    logger.info(f"ChromaDB Cloud connected | db={settings.CHROMA_DATABASE}")
    return client

def get_collection(collection_name: str = "medical_collection") -> chromadb.Collection:
    client = get_chroma_client()
    
    # Use OpenAI embedding model to convert text -> vectors
    embedding_function = embedding_functions.OpenAIEmbeddingFunction(
        api_key = settings.OPENAI_API_KEY,
        model_name = "text-embedding-3-small"
    )

    # Safe to call everytime - won't duplicate if collection already exists
    collection = client.get_or_create_collection(
        name = collection_name,
        embedding_function = embedding_function,
        metadata = {"description": "FDA medical data for RAG-based chatbot"},
        hnsw = {"m": 16, "ef_construction": 64}  # Optimized for speed
    )

    logger.info(f"Collection '{collection_name}' ready with {collection.count()} items")
    return collection

def test_chroma_connection() -> bool:
    """Ping ChromaDB to verify it's avlive (used in health check)"""
    try:
        client = get_chroma_client()
        client.heartbeat()    # Lightweight ping - raises exception if down
        logger.info("ChromaDB connection: OK")
        return True
    
    except Exception as e:
        logger.error(f"ChromaDB connection failed: {e}")
        return False



     
