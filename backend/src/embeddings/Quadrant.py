from qdrant_client.async_qdrant_client import AsyncQdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance
from src.config import Config

class QdrantVectorStore:
    def __init__(self):
        self.config = Config()
        self.client = AsyncQdrantClient(
            url=self.config.get_qdrant_url(),
            api_key=self.config.get_qdrant_api_key(),
            timeout=120
        )
        self.collection_name = self.config.get_qdrant_collection_name()
        self.vector_size = 384
        self.distance = Distance.COSINE

    async def create_collection(self):
        exists = await self.client.collection_exists(self.collection_name)
        if not exists:
            await self.client.recreate_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=self.vector_size,
                    distance=self.distance
                )
            )
            print(f"Collection '{self.collection_name}' created.")
        else:
            print(f"Collection '{self.collection_name}' already exists.")

    async def upload_embeddings(self, chunks, embeddings, metadata=None):
        # print("metadata : ",metadata)
        if metadata is None:
            metadata = {}

        
        points = [
            PointStruct(
                id=abs(hash(chunk)),  
                vector=embedding,
                payload={
                    "text": chunk,
                    **metadata
                }
            )
            for chunk, embedding in zip(chunks, embeddings)
        ]

        await self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )
        print(f"Uploaded {len(points)} embeddings to Qdrant.")

    async def delete_collection(self):
        exists = await self.client.collection_exists(self.collection_name)
        if exists:
            await self.client.delete_collection(collection_name=self.collection_name)
            print(f"Collection '{self.collection_name}' has been deleted.")
        else:
            print(f"Collection '{self.collection_name}' does not exist.")

    async def search(self, query_vector, top_k=3):
        results = await self.client.search(
            collection_name=self.collection_name,
            query_vector=query_vector,
            limit=top_k
        )
        return results
