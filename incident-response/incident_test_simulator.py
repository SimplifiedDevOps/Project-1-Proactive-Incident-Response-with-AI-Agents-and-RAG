# incident_test_simulator.py

import requests
import json
from datetime import datetime

# Simulated common incidents for testing
test_incidents = [
    {
        "description": "High memory usage on application servers.",
        "root_cause": "Memory leak in the application code.",
        "resolution_steps": "Restarted application service and patched memory leak."
    },
    {
        "description": "Database connection timeout.",
        "root_cause": "Network congestion in database cluster.",
        "resolution_steps": "Optimized network configuration and restarted database service."
    },
    {
        "description": "Slow response times in frontend services.",
        "root_cause": "High CPU usage due to increased traffic.",
        "resolution_steps": "Scaled up frontend instances and optimized code."
    }
]

# Define AI Agent endpoint URLs
AI_AGENT_URL = "http://localhost:5000/incident_alert"

def simulate_incident(incident):
    """
    Sends a simulated incident to the AI agent to test its response.
    """
    # Prepare payload with incident description
    payload = {
        "alerts": [
            {
                "annotations": {
                    "description": incident["description"]
                }
            }
        ]
    }
    
    # Send incident to AI agent and capture response
    response = requests.post(AI_AGENT_URL, json=payload)
    if response.status_code == 200:
        data = response.json()
        print(f"\nIncident: {incident['description']}")
        print("Agent Response:", json.dumps(data, indent=2))
    else:
        print(f"Failed to send incident. Status Code: {response.status_code}")

def test_incident_response_workflow():
    """
    Tests the incident response workflow by simulating incidents.
    """
    print("Starting Incident Response Workflow Tests...\n")
    
    for incident in test_incidents:
        simulate_incident(incident)
    
    print("\nIncident Response Workflow Testing Complete.")

# Run the test
if __name__ == "__main__":
    test_incident_response_workflow()
