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


# Example
try:
    with open("jenkins.log", "r") as f:
        logs = f.read()
except FileNotFoundError:
    print("Log file not found")
    exit()

result = analyze_logs(logs)
print(result)