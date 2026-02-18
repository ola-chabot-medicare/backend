import chromadb
from chromadb.utils import embedding_functions
from config.settings import settings


def get_chroma_client():
    return chromadb.PersistentClient(
        path=settings.CHROMA_PATH
    )


def get_collection():
    client = get_chroma_client()

    embedding_function = embedding_functions.OpenAIEmbeddingFunction(
        api_key=settings.OPENAI_API_KEY,
        model_name="text-embedding-3-small"
    )

    return client.get_or_create_collection(
        name="medical_collection",
        embedding_function=embedding_function
    )
