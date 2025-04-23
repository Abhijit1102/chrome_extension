# 🧠 AI-Powered URL QA Chatbot & Chrome Extension

This full-stack project allows you to ask intelligent questions about the content of any webpage. It features:

- ✅ A **FastAPI** backend that scrapes, embeds, stores, and retrieves contextual data from web URLs.
- 🧩 A **Chrome Extension** that connects to this backend and allows users to interact with it directly from their browser.

---

## 🌐 Backend – FastAPI Service

### Features

- 🔍 Scrape and extract text from any webpage
- 🧠 Use **HuggingFace** embeddings to vectorize text
- 🚀 Store and query vectors using **Qdrant**
- 🤖 AI chatbot generates context-aware answers
- 🗃️ Logs queries and responses to **MongoDB**

### Tech Stack

- FastAPI
- Qdrant
- HuggingFace Transformers
- MongoDB (via `motor`)
- BeautifulSoup for web scraping

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET`  | `/api/v1/health` | Check if the API is up |
| `POST` | `/api/v1/process_url` | Process a webpage and store embeddings |
| `POST` | `/api/v1/get_answer` | Ask a question and get an AI-generated answer |
| `POST` | `/api/v1/delete_collection` | Clear Qdrant vector collection |

### Run Backend

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

## 🧩 Chrome Extension – Frontend Interface
###  Features
- 📥 Loads content from the current tab URL

- 🧠 Asks questions and gets AI answers

- 💬 Display interface using a popup

- Uses Chrome APIs (tabs, cookies, storage, etc.)

## 💡 How It Works
- Open any webpage in your browser

- Click the Chrome extension and hit "Load URL"

- Ask any question about the webpage content

- Get a contextual answer from the backend AI

## 🛡️ Environment Variables (if applicable)

- Set up the following in your .env file or system environment:

- `MONGODB_URI`

- `QDRANT_URL` or local config

- `HuggingFace model`a details (in embeddings.py)

