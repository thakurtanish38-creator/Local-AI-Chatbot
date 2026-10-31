
import requests

url = "http://localhost:11434/api/chat"

data = {
    "model": "qwen3:4b",
    "messages": [
        {
            "role": "user",
            "content": "Explain Python functions in simple words."
        }
    ],
    "stream": False
}

response = requests.post(url, json=data)

result = response.json()

print(result["message"]["content"])

