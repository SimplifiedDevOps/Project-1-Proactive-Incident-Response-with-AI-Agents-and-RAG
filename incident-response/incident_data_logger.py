# incident_data_logger.py

import pinecone
from embeddings.embedder import generate_embedding
from config.config import PINECONE_INDEX_NAME
from datetime import datetime
import uuid

# Initialize Pinecone
pinecone.init(api_key="YOUR_PINECONE_API_KEY", environment="YOUR_PINECONE_ENVIRONMENT")
index = pinecone.Index(PINECONE_INDEX_NAME)

def log_incident_and_store(incident_description, root_cause, resolution_steps):
    """
    Logs incident details, converts them to embeddings, and stores in Pinecone.

    Args:
        incident_description (str): Description of the incident.
        root_cause (str): Identified root cause of the incident.
        resolution_steps (str): Steps taken to resolve the incident.
    """

    # Prepare the incident data for embedding
    incident_data = f"Description: {incident_description}. Root Cause: {root_cause}. Resolution: {resolution_steps}."

    # Generate embedding for the incident
    embedding_vector = generate_embedding(incident_data)

    # Create a unique incident ID
    incident_id = str(uuid.uuid4())

    # Define metadata to store in Pinecone along with the embedding
    metadata = {
        "incident_id": incident_id,
        "description": incident_description,
        "root_cause": root_cause,
        "resolution_steps": resolution_steps,
        "timestamp": datetime.now().isoformat()
    }

    # Store the embedding and metadata in Pinecone
    index.upsert([{
        "id": incident_id,
        "values": embedding_vector,
        "metadata": metadata
    }])

    print(f"Incident {incident_id} logged and embedded in Pinecone.")

# Example usage
if __name__ == "__main__":
    # Sample incident data
    incident_description = "High latency in database response time."
    root_cause = "Database query optimization needed."
    resolution_steps = "Added indexing on frequently queried fields and optimized query structure."

    log_incident_and_store(incident_description, root_cause, resolution_steps)
