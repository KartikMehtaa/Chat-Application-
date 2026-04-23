from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load .env file
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Model
model = genai.GenerativeModel("gemini-1.5-flash")


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

    response = model.generate_content(prompt)

    if response and hasattr(response, "text"):
        return response.text
    return "No response from Gemini"


# ✅ Correct path
log_path = "genai/jenkins.log"

print("Looking for:", log_path)

if not os.path.exists(log_path):
    print("Log file not found ❌")
    exit(1)

with open(log_path, "r") as f:
    logs = f.read()

print("Log file loaded ✅")

result = analyze_logs(logs)
print(result)