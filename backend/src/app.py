from fastapi import FastAPI, HTTPException, APIRouter
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from src.embeddings.Quadrant import QdrantVectorStore
from src.model.requestSchema import UrlRequest
from src.model.chatSchema import ChatRequest
from src.embeddings.huggingface_embeddings import get_embedding
from src.utils import DocumentProcessor
from src.llm.ChatBot import ChatAssistant
from src.database.mongodb_connection import MongoDBClient

import asyncio

qdrant_store = QdrantVectorStore()
chat = ChatAssistant()
client = MongoDBClient()

app = FastAPI(
    title="My API",
    openapi_url="/api/v1/openapi.json",
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_router = APIRouter(prefix="/api/v1")

@app.on_event("startup")
async def startup_event():
    await qdrant_store.create_collection()

@api_router.get("/heathcheck")
async def read_root():
    return {"message": "Api is running in port 8000!"}

@api_router.post("/process_url")
async def process_url(request: UrlRequest):
    try:
        processor = DocumentProcessor(request.url)
        processor.process_all()  
        chunks = processor.get_cleaned_chunks()

        for chunk in chunks:
            embedding = await get_embedding(chunk)
            metadata = {"source_url": request.url}
            await qdrant_store.upload_embedding(chunk, embedding, metadata)

        return {"message": "Text processed and uploaded to Qdrant."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@api_router.post("/get_answer")
async def chat_endpoint(request: ChatRequest):
    try:
        user_message = request.message
        embedding = await get_embedding(user_message)
        similar_chunks = await qdrant_store.search(embedding)

        content = "".join(chunk.payload["text"] for chunk in similar_chunks)
        response_message = chat.ask(user_message, content)
        client.insert_chat_log({"user_message": user_message, "response_message": response_message})
        return {"message": response_message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@api_router.get("/delete_collection")
async def delete_collection():
    try:
        await qdrant_store.delete_collection()
        return {"message": "Collection deleted."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
