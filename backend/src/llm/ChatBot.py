from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from src.config import Config

config = Config()
class ChatAssistant:
    """
    A class-based OpenAI chat assistant that uses context (content chunks) to answer questions.
    """
    def __init__(self):
        self.model = ChatOpenAI(
            model=config.get_openai_api_model(),
            temperature=0.5,
            api_key=config.get_openai_api_key()
        )
        self.chat_history = [
            SystemMessage(content='You are a helpful AI assistant. Your job is to understand the provided content and answer questions based on it.')
        ]

    def ask(self, user_input: str, similar_chunks: str) -> str:
        """
        Process a user question based on relevant content chunks.
        
        Args:
            user_input (str): The user's question.
            similar_chunks (str): Relevant text content to base the answer on.
        
        Returns:
            str: The AI's response.
        """
        message = f"""Here is some relevant content:\n{similar_chunks}\n\nNow answer the following question:\n{user_input}"""
        self.chat_history.append(HumanMessage(content=message))
        response = self.model.invoke(self.chat_history)
        self.chat_history.append(AIMessage(content=response.content))
        return response.content
