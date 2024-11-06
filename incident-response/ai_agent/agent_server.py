# agent_server.py

from flask import Flask, request, jsonify
from ai_agent.agent import handle_incident_with_agent
from ai_agent.incident_followup_chain import handle_followup_with_chain

app = Flask(__name__)

@app.route('/incident_alert', methods=['POST'])
def incident_alert():
    alert_data = request.json  # Extract alert data
    incident_description = alert_data["alerts"][0]["annotations"]["description"]
    
    # Initial incident processing and suggestion
    initial_response = handle_incident_with_agent(incident_description)
    
    return jsonify({"status": "received", "response": initial_response})

@app.route('/incident_followup_chain', methods=['POST'])
def incident_followup_chain():
    # Handle multi-step follow-up with LangChain chain
    data = request.json
    incident_description = data.get("incident_description")
    additional_notes = data.get("additional_notes", "")
    
    # Execute the multi-step follow-up chain
    followup_response = handle_followup_with_chain(incident_description, additional_notes)
    
    return jsonify({"status": "followup_chain_executed", "response": followup_response})

if __name__ == "__main__":
    app.run(port=5000)
