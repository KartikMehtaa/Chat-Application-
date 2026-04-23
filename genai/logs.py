from dotenv import load_dotenv
import os
from google import genai

# Load env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Create client
client = genai.Client(api_key=api_key)

def analyze_logs(logs):
    prompt = f"""
    You are a DevOps expert.

    Analyze these Jenkins pipeline logs:
    - Find errors
    - Explain root cause
    - Suggest fix

    Logs:
    {logs}
    """

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    return response.text


# Read log
log_path = "jenkins.log"

if not os.path.exists(log_path):
    print("Log file not found ❌")
    exit(1)

with open(log_path, "r") as f:
    logs = f.read()

result = analyze_logs(logs)
print(result)