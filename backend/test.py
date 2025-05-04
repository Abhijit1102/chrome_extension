import sys
import asyncio
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from src.embeddings.huggingface_embeddings import get_embedding
from src.embeddings.Quadrant import QdrantVectorStore

from src.utils import DocumentProcessor
if __name__ == "__main__":
    # Example usage
    url = "https://en.wikipedia.org/wiki/Quantum_computing"
    processor = DocumentProcessor(url)
    processor.process_all()
    print("length of chunks : ",len(processor.get_cleaned_chunks()))
    chunks = processor.get_cleaned_chunks()
    async def main():
        embeddings = await get_embedding(chunks)
        qdrant_store = QdrantVectorStore()
        await qdrant_store.create_collection()
        await qdrant_store.upload_embeddings(chunks, embeddings, metadata={"source_url": url})

    asyncio.run(main())