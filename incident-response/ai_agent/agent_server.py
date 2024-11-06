# agent_server.py

from flask import Flask, request, jsonify
from incidents.incident_processor import handle_new_incident

app = Flask(__name__)

@app.route('/incident_alert', methods=['POST'])
def incident_alert():
    # Receive the alert data sent by Alertmanager
    alert_data = request.json  # Extract alert data

    # Access the description from the alert annotations
    incident_description = alert_data["alerts"][0]["annotations"]["description"]
    
    # Process the incident with the AI agent to find similar incidents
    similar_incidents = handle_new_incident(incident_description)
    
    # Respond back with the status and any similar incidents found
    return jsonify({"status": "received", "similar_incidents": similar_incidents})

if __name__ == "__main__":
    app.run(port=5000)
