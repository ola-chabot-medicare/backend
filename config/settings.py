import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env into the environment

class Settings:
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")        # Required for LLM & embeddings
    CHROMA_API_KEY: str = os.getenv("CHROMA_API_KEY", "")        # ChromaDB Cloud API key
    CHROMA_TENANT: str = os.getenv("CHROMA_TENANT", "")          # Chroma account/tenant name
    CHROMA_DATABASE: str = os.getenv("CHROMA_DATABASE", "")      # Chroma database name
    APP_ENV: str = os.getenv("APP_ENV", "development")
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"

settings = Settings()  # Single shared instance — import this everywhere