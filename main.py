import uvicorn  
import settings
import chroma

from fastapi import FastAPI, Depends
from chromadb.client import Client
from api.routes import router as api_router


app = FastAPI(title="Medical Chatbot")

_client = get_chroma_client()
_collection = get_collection()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000,reload=True)