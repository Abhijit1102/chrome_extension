# 🧠 AI-Powered Document Chat API

This is a FastAPI-based backend service that allows you to:

- Ingest and process documents from a URL
- Convert them into vector embeddings
- Store them in Qdrant (a vector database)
- Perform semantic search
- Generate responses using an LLM-based chatbot

## 🚀 Features

- ✅ Document ingestion and chunking from URLs
- ✅ Embedding generation using HuggingFace models
- ✅ Vector similarity search with Qdrant
- ✅ Intelligent question answering
- ✅ FastAPI with automatic Swagger/OpenAPI docs
- ✅ CORS-enabled for frontend integration

---

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- Qdrant running locally or via cloud

### Clone & Setup

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
pip install -r requirements.txt
```

🧪 Run the Server

```bash
uvicorn main:app --reload
```
Visit Swagger UI at: http://127.0.0.1:8000/api/v1/docs

📡 API Endpoints
GET /api/v1/healthcheck
Check API status.

POST /api/v1/process_url
Processes the content at a given URL, creates embeddings, and uploads to Qdrant.

```json 
{ "message": "Text processed and uploaded to Qdrant." }
```
POST /api/v1/get_answer
Queries your ingested documents with a natural language question.
Request:

```json
{
  "message": "What is the main topic of the article?"
}
```

Response:

```json
{ "message": "The article mainly discusses..." }
```

Response:

```json
{ "message": "Collection deleted." }
```
