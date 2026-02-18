import uvicorn  

from fastapi import FastAPI

from api.routes import router as api_router


app = FastAPI(title="Medical Chatbot")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000,reload=True)