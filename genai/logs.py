from dotenv import load_dotenv
import os
import time
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("API key missing ❌")
    exit(0)

client = genai.Client(api_key=api_key)

# 🔥 Two models (primary + fallback)
MODELS = [
    "gemini-2.5-flash",   # fast + primary
    "gemini-2.5-flash-lite"      # stable fallback
]


def analyze_logs(logs):
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

    for model in MODELS:
        for attempt in range(3):  # retry per model
            try:
                response = client.models.generate_content(
                    model=model,
                    contents=prompt
                )

                print(f"✅ Success with model: {model}")
                return response.text

            except Exception as e:
                print(f"❌ {model} attempt {attempt+1} failed: {e}")
                time.sleep(2 * (attempt + 1))  # backoff

    return "❌ All models failed due to API overload"


with open("jenkins.log", "r") as f:
    logs = f.read()

print(analyze_logs(logs))