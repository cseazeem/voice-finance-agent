from agents.voice_agent import listen, speak

if __name__ == "__main__":
    query = listen()
    if query:
        speak(f"You said: {query}")
