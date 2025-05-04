import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class Config:
    def __init__(self):
        # HuggingFace
        self.HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
        self.HUGGINGFACE_API_URL = os.getenv("HUGGINGFACE_API_URL")

        # Qdrant
        self.QDRANT_URL = os.getenv("QDRANT_URL")
        self.QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
        self.QDRANT_COLLECTION_NAME = os.getenv("QDRANT_COLLECTION_NAME")

        # OpenAI
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        self.OPENAI_MODEL = os.getenv("OPENAI_MODEL")

        # MongoDB
        self.MONGODB_URL = os.getenv("MONGODB_URL")
        self.MONGODB_DB_NAME = os.getenv("MONGODB_DB_NAME")
        self.MONGODB_COLLECTION_NAME = os.getenv("MONGODB_COLLECTION_NAME")

    # HuggingFace getters
    def get_huggingface_api_key(self):
        return self.HUGGINGFACE_API_KEY

    def get_huggingface_api_url(self):
        return self.HUGGINGFACE_API_URL    

    # Qdrant getters
    def get_qdrant_url(self):
        return self.QDRANT_URL

    def get_qdrant_api_key(self):
        return self.QDRANT_API_KEY

    def get_qdrant_collection_name(self):
        return self.QDRANT_COLLECTION_NAME

    # OpenAI getters
    def get_openai_api_key(self):
        return self.OPENAI_API_KEY

    def get_openai_api_model(self):
        return self.OPENAI_MODEL  

    # MongoDB getters
    def get_mongodb_url(self):
        return self.MONGODB_URL 

    def get_mongodb_db_name(self):
        return self.MONGODB_DB_NAME   

    def get_mongodb_collection_name(self):    
        return self.MONGODB_COLLECTION_NAME


# Optional: test the configuration by printing all values
# if __name__ == "__main__":
#     config = Config()
#     print("HuggingFace API Key:", config.get_huggingface_api_key())
#     print("HuggingFace API URL:", config.get_huggingface_api_url())
#     print("Qdrant URL:", config.get_qdrant_url())
#     print("Qdrant API Key:", config.get_qdrant_api_key())
#     print("Qdrant Collection Name:", config.get_qdrant_collection_name())
#     print("OpenAI API Key:", config.get_openai_api_key())
#     print("OpenAI Model:", config.get_openai_api_model())
#     print("MongoDB URL:", config.get_mongodb_url())
#     print("MongoDB DB Name:", config.get_mongodb_db_name())
#     print("MongoDB Collection Name:", config.get_mongodb_collection_name())
