from agents.voice_agent import listen, speak
import requests

def query_api(text):
    url = "http://127.0.0.1:8000/brief"
    try:
        response = requests.post(url, json={"query": text})
        if response.status_code == 200:
            return response.json().get("summary", "No summary received.")
        else:
            return f"API returned status code {response.status_code}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    query = listen()
    if query:
        speak("Let me find the summary for that.")
        summary = query_api(query)
        print("📢 Summary:", summary)
        speak(summary)
