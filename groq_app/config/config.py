from dotenv import load_dotenv 
import os

load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

from langchain_groq import ChatGroq
from nemoguardrails.llm.providers import register_chat_provider

def groq_factory(model, **kwargs):
    return ChatGroq(
        api_key=GROQ_API_KEY,
        model=model
    )

register_chat_provider("groq", groq_factory)

