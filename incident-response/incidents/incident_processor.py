# incidents/incident_processor.py
from embeddings.embedder import generate_embedding
from pinecone_integration.store_and_query import store_incident, retrieve_similar_incidents

def process_and_store_incident(incident_id, description, metadata=None):
    embedding_vector = generate_embedding(description)
    store_incident(incident_id, embedding_vector, metadata)

def handle_new_incident(description):
    query_vector = generate_embedding(description)
    return retrieve_similar_incidents(query_vector)
