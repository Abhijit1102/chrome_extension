import httpx
from src.config import Config

config = Config()

hf_headers = {
    "Authorization": f"Bearer {config.HUGGINGFACE_API_KEY}"
}

async def get_embedding(text: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            config.get_huggingface_api_url(),
            headers=hf_headers,
            json={"inputs": text},
            timeout=30.0 
        )
        response.raise_for_status()
        return response.json()
