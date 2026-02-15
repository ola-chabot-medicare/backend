# Medical Chatbot Backend

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6F61?style=for-the-badge&logo=databricks&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

A FastAPI-based backend service for a medical chatbot application, leveraging ChromaDB for vector storage and LangChain for conversational AI capabilities.

---

## 🛠️ Tech Stack

| Technology | Description |
|------------|-------------|
| ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) | Core programming language |
| ![FastAPI](https://img.shields.io/badge/-FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) | Modern, high-performance web framework for building APIs |
| ![ChromaDB](https://img.shields.io/badge/-ChromaDB-FF6F61?style=flat-square&logo=databricks&logoColor=white) | Vector database for efficient similarity search and retrieval |
| ![LangChain](https://img.shields.io/badge/-LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white) | Framework for developing LLM-powered applications |
| ![Uvicorn](https://img.shields.io/badge/-Uvicorn-499848?style=flat-square&logo=gunicorn&logoColor=white) | ASGI server for running the FastAPI application |

---

## 📁 Project Structure

```
backend/
│
├── 📂 api/                      # API layer
│   └── routes.py                # API route definitions and endpoint handlers
│
├── 📂 config/                   # Configuration
│   └── settings.py              # Application settings and environment variables
│
├── 📂 models/                   # Data models
│   └── schemas.py               # Pydantic request/response schemas
│
├── 📂 services/                 # External service integrations
│   └── llm.py                   # LangChain LLM integration
│
├── 📂 utils/                    # Utility functions
│   └── logger.py                # Logging configuration and utilities
│
├── 📄 .env                      # Environment variables (not in git)
├── 📄 .gitignore                # Git ignore rules
├── 📄 Dockerfile                # Docker container configuration
├── 📄 example.env               # Environment variables template
├── 📄 main.py                   # FastAPI application entry point
├── 📄 README.md                 # Project documentation
└── 📄 requirements.txt          # Python dependencies
```

### 📂 Folder Descriptions

| Folder | Purpose |
|--------|---------|
| `api/` | API layer with route handlers and endpoint definitions |
| `config/` | Application configuration and environment settings |
| `models/` | Pydantic schemas for request/response data validation |
| `services/` | External service integrations (LLM, ChromaDB, embeddings) |
| `utils/` | Shared utility functions like logging |

---

## ⚙️ Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Docker (optional, for containerized deployment)

---

## 🚀 Installation

### 💻 Local Development

1. **Clone the repository** (if not already done):
   ```bash
   git clone <repository-url>
   cd backend
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**:
   Create a `.env` file in the root directory:
   ```env
   # Add your environment variables here
   # Example:
   # OPENAI_API_KEY=your_api_key_here
   ```

6. **Run the application**:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

### 🐳 Docker Deployment

1. **Build the Docker image**:
   ```bash
   docker build -t medical-chatbot-backend .
   ```

2. **Run the container**:
   ```bash
   docker run -p 8000:8000 medical-chatbot-backend
   ```

---

## 📖 API Documentation

Once the server is running, you can access:

| Documentation | URL |
|---------------|-----|
| 📗 Swagger UI | [http://localhost:8000/docs](http://localhost:8000/docs) |
| 📘 ReDoc | [http://localhost:8000/redoc](http://localhost:8000/redoc) |

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🤖 **AI-Powered Chat** | Conversational AI powered by LangChain and LLMs |
| 🔍 **Semantic Search** | Vector-based document retrieval using ChromaDB |
| ⚡ **High Performance** | Fast and async request handling with FastAPI |
| 📚 **RAG Pipeline** | Retrieval-Augmented Generation for accurate medical responses |
| 🔒 **Secure** | Environment-based configuration for sensitive data |

---

## 🔐 Environment Variables

Create a `.env` as same as `example.env` file in the root directory:

```env
# LLM Configuration
OPENAI_API_KEY=your_openai_api_key_here

# ChromaDB Configuration
CHROMA_PERSIST_DIR=./data/chroma_db

# Application Settings
APP_ENV=development
DEBUG=true
```

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `OPENAI_API_KEY` | OpenAI API key for LLM access | ✅ Yes | - |
| `CHROMA_PERSIST_DIR` | ChromaDB persistence directory | ❌ No | `./data/chroma_db` |
| `APP_ENV` | Application environment | ❌ No | `development` |
| `DEBUG` | Enable debug mode | ❌ No | `false` |

---

## 🧪 Development

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app tests/

# Run specific test file
pytest tests/test_api/test_chat.py
```

### Code Formatting

```bash
# Install dev dependencies
pip install black isort flake8

# Format code
black .
isort .

# Lint code
flake8 app/
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/health` | Health check endpoint |
| `POST` | `/api/chat` | Send message to chatbot |
| `GET` | `/api/chat/history` | Get conversation history |
| `DELETE` | `/api/chat/history` | Clear conversation history |

---

## 🔗 Related

| Resource | Description |
|----------|-------------|
| 🎨 [Frontend](../frontend) | The frontend application for this chatbot |

---

## 📄 License

This project is part of the MedicalChatbot application.

---

<p align="center">
  Made with ❤️ using FastAPI, LangChain & ChromaDB
</p>
