# pinecone_integration/store_and_query.py
from pinecone_integration.setup_pinecone import initialize_pinecone
from config.config import PINECONE_INDEX_NAME
import pinecone

# Initialize Pinecone and create the index if it doesn't exist
initialize_pinecone()
if PINECONE_INDEX_NAME not in pinecone.list_indexes():
    pinecone.create_index(PINECONE_INDEX_NAME, dimension=768)

index = pinecone.Index(PINECONE_INDEX_NAME)

def store_incident(incident_id, embedding_vector, metadata=None):
    # Store an embedding vector with metadata
    index.upsert([{
        "id": incident_id,
        "values": embedding_vector,
        "metadata": metadata or {}
    }])

def retrieve_similar_incidents(query_vector, top_k=5):
    # Query similar incidents based on the embedding vector
    results = index.query(vector=query_vector, top_k=top_k, include_metadata=True)
    return results["matches"]
