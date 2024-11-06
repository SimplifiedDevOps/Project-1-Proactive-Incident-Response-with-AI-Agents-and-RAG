# agent_server.py

from flask import Flask, request, jsonify
from ai_agent.agent import handle_incident_with_agent
from ai_agent.incident_followup_chain import handle_followup_with_chain
from incident_data_logger import log_incident_and_store
import json
import os

app = Flask(__name__)

# File to store feedback
FEEDBACK_FILE = "feedback_log.json"

def store_feedback(incident_id, feedback_text, rating):
    """
    Stores feedback in a JSON file for later analysis.
    """
    feedback_data = {
        "incident_id": incident_id,
        "feedback_text": feedback_text,
        "rating": rating,
        "timestamp": datetime.now().isoformat()
    }
    
    # Check if feedback file exists and load existing data
    if os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, 'r') as f:
            feedback_list = json.load(f)
    else:
        feedback_list = []

    # Append new feedback to list
    feedback_list.append(feedback_data)

    # Save feedback back to file
    with open(FEEDBACK_FILE, 'w') as f:
        json.dump(feedback_list, f, indent=2)

    print("Feedback stored successfully.")

@app.route('/feedback', methods=['POST'])
def feedback():
    """
    API endpoint to receive feedback from operators.
    """
    data = request.json
    incident_id = data.get("incident_id")
    feedback_text = data.get("feedback_text")
    rating = data.get("rating")  # Rating between 1 and 5 for example
    
    # Store feedback for continuous improvement
    store_feedback(incident_id, feedback_text, rating)

    return jsonify({"status": "feedback received"}), 200
