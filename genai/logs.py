import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

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
    return response.text


# Example
with open("jenkins.log", "r") as f:
    logs = f.read()

result = analyze_logs(logs)
print(result)