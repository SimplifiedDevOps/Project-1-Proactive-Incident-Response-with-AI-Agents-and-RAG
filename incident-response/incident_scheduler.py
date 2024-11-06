# incident_scheduler.py

import schedule
import time
from datetime import datetime, timedelta
from incident_data_logger import log_incident_and_store

# Assuming you have a function that retrieves incidents from a database
def fetch_recent_incidents(since_time):
    """
    Fetch incidents that were logged after the specified time.
    Args:
        since_time (datetime): Fetch incidents logged after this time.
    Returns:
        List of incident dictionaries with keys: description, root_cause, resolution_steps.
    """
    # Replace with actual code to fetch from your database or log system.
    # Here is a mock example:
    return [
        {
            "incident_description": "Service outage due to memory overload.",
            "root_cause": "Memory leak in application code.",
            "resolution_steps": "Restarted service and applied patch."
        }
    ]

def update_pinecone_with_recent_incidents():
    # Calculate time 24 hours ago
    since_time = datetime.now() - timedelta(days=1)
    print(f"Checking for new incidents since {since_time}...")

    # Fetch recent incidents
    recent_incidents = fetch_recent_incidents(since_time)

    # Log each new incident and update Pinecone
    for incident in recent_incidents:
        log_incident_and_store(
            incident["incident_description"],
            incident["root_cause"],
            incident["resolution_steps"]
        )
    print("Pinecone updated with recent incidents.")

# Schedule the update task to run at regular intervals
schedule.every(24).hours.do(update_pinecone_with_recent_incidents)

print("Starting scheduled incident embedding updates...")
while True:
    schedule.run_pending()
    time.sleep(1)  # Sleep to avoid high CPU usage



# Setting Up a Cron Job for Regular Updates (Optional)
# -----------------------------------------------------
# Alternatively, you can set up a cron job to run `incident_scheduler.py` at regular intervals.
# This is ideal if you want to handle scheduling at the OS level rather than within Python.

# 1. Edit the Cron Table:
#    Run the following command to edit your crontab:
#    crontab -e

# 2. Add a Cron Job to run every day at midnight.
#    For example, add the following line in the crontab:

# 0 0 * * * /path/to/your/python /path/to/incident-response/incident_scheduler.py >> /path/to/logs/incident_update.log 2>&1

# Explanation:
# - This cron job runs `incident_scheduler.py` at midnight every day.
# - The output is appended to `incident_update.log`, and any errors are also logged.
# - Replace `/path/to/your/python` with the path to your Python executable.
# - Replace `/path/to/incident-response/incident_scheduler.py` with the path to your script.
# - Replace `/path/to/logs/incident_update.log` with your desired log file path.
