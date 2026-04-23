from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("API key missing ❌")
    exit(1)

client = genai.Client(api_key=api_key)

def analyze_logs(logs):
    try:
        logs = logs[-3000:]

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
            model="gemini-1.5-flash",   # change from 2.0 → 1.5
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error analyzing logs: {str(e)}"


with open("jenkins.log", "r") as f:
    logs = f.read()

print(analyze_logs(logs))