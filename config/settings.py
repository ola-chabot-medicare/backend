import os 

from dotenv import load_dotenv 

load_dotenv()
class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    CHROMA_API_KEY = os.getenv("CHROMA_API_KEY")
    CHROMA_TENANT = os.getenv("CHROMA_TENANT")
    CHROMA_DATABASE = os.getenv("CHROMA_DATABASE")
    CHROMA_COLLECTION = os.getenv("CHROMA_COLLECTION", "medicare-chatbot")

settings = Settings()