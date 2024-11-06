# config/config.py
import os

# Pinecone API Configuration
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY", "your-pinecone-api-key")
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT", "us-west1-gcp")  # Example environment
PINECONE_INDEX_NAME = "incident-response-index"
EMBEDDING_DIMENSION = 768  # Match with your embedding model's output dimension
