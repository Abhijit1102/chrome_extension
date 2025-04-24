import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")  
        self.HUGGINGFACE_API_URL = os.getenv("HUGGINGFACE_API_URL") 
        
        self.QDRANT_URL = os.getenv("QDRANT_URL")    
        self.QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
        self.QDRANT_COLLECTION_NAME = os.getenv("QDRANT_COLLECTION_NAME") 

        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        self.OPENAI_MODEL = os.getenv("OPENAI_MODEL")

    def get_huggingface_api_key(self):
        return self.HUGGINGFACE_API_KEY

    def get_huggingface_api_url(self):
        return self.HUGGINGFACE_API_URL    

    def get_qdrant_url(self):
        return self.QDRANT_URL

    def get_qdrant_api_key(self):
        return self.QDRANT_API_KEY

    def get_qdrant_collection_name(self):
        return self.QDRANT_COLLECTION_NAME

    def get_openai_api_key(self):
        return self.OPENAI_API_KEY

    def get_openai_api_model(self):
        return self.OPENAI_MODEL   
