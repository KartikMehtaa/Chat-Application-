from dotenv import load_dotenv
import os
from google import genai

# Load env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("API key missing ❌")
    exit(1)

client = genai.Client(api_key=api_key)

def analyze_logs(logs):
    try:
        logs = logs[-3000:]  # limit logs

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
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error analyzing logs: {str(e)}"


log_path = "jenkins.log"

if not os.path.exists(log_path):
    print("Log file not found ❌")
    exit(1)

with open(log_path, "r") as f:
    logs = f.read()

result = analyze_logs(logs)
print(result)