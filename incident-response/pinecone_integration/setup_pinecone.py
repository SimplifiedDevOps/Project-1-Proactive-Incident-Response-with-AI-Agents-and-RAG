# pinecone_integration/setup_pinecone.py
import pinecone
from config.config import PINECONE_API_KEY, PINECONE_ENVIRONMENT

def initialize_pinecone():
    # Initialize Pinecone
    pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENVIRONMENT)
