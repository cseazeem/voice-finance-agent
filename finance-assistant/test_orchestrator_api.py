import requests

url = "http://127.0.0.1:8000/brief"
payload = {
    "query": "Asia tech stock performance"
}

response = requests.post(url, json=payload)
print("✅ Status:", response.status_code)
print("🧠 Summary:", response.json())
