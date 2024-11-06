# main.py
from incidents.incident_processor import process_and_store_incident, handle_new_incident

# Example: Store a new incident
incident_id = "incident_001"
description = "Network latency issue detected in cluster."
metadata = {"type": "network_issue", "severity": "high"}
process_and_store_incident(incident_id, description, metadata)

# Example: Handle a new incident and retrieve similar incidents
new_incident_description = "Latency detected in network services."
similar_incidents = handle_new_incident(new_incident_description)

# Print similar incidents
for match in similar_incidents:
    print(f"Incident ID: {match['id']}, Metadata: {match['metadata']}")
