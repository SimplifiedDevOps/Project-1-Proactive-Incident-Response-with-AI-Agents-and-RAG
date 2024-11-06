# ai_agent/incident_followup_chain.py

from langchain.chains import SequentialChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
import subprocess
import requests

# Define the templates for each task
query_logs_template = PromptTemplate(
    template="""
    You need to query logs for incident follow-up.
    Incident description: {incident_description}
    Fetch and analyze logs related to this incident.
    """
)

restart_service_template = PromptTemplate(
    template="""
    You have identified that a specific service needs to be restarted to resolve the incident.
    Incident description: {incident_description}
    Confirm if the service was restarted successfully.
    """
)

notify_team_template = PromptTemplate(
    template="""
    Notify the relevant teams about the current incident status.
    Incident description: {incident_description}
    Resolution status: {resolution_status}
    Additional notes: {additional_notes}
    """
)

# Define each step in the multi-step follow-up process

def query_logs(incident_description):
    # Example placeholder function that fetches logs from a server
    # Replace with actual log query logic if available
    print(f"Querying logs for incident: {incident_description}")
    return "Logs retrieved successfully."

def restart_service_in_k8s(incident_description):
    # Example Kubernetes restart command using kubectl
    print(f"Restarting service for incident: {incident_description}")
    try:
        subprocess.run(["kubectl", "rollout", "restart", "deployment/my-deployment"], check=True)
        return "Service restarted successfully."
    except subprocess.CalledProcessError as e:
        return f"Failed to restart service: {e}"

def notify_team(incident_description, resolution_status, additional_notes=""):
    # Example notification via Slack or email
    slack_webhook_url = "https://hooks.slack.com/services/T0000/B0000/XXXX"
    message = {
        "text": f"Incident: {incident_description}\nResolution Status: {resolution_status}\nNotes: {additional_notes}"
    }
    response = requests.post(slack_webhook_url, json=message)
    if response.status_code == 200:
        return "Team notified successfully."
    else:
        return "Failed to notify team."

# Define the SequentialChain

def create_followup_chain():
    return SequentialChain(
        chains=[
            query_logs_template.bind(function=query_logs),
            restart_service_template.bind(function=restart_service_in_k8s),
            notify_team_template.bind(function=notify_team)
        ],
        input_variables=["incident_description", "additional_notes"],
        output_variables=["logs_status", "service_status", "notification_status"]
    )

def handle_followup_with_chain(incident_description, additional_notes=""):
    # Execute the chain with given incident details
    chain = create_followup_chain()
    response = chain({
        "incident_description": incident_description,
        "additional_notes": additional_notes
    })
    return response
