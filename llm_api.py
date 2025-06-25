import os
import time
import requests
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Get API key from environment
api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    print("❌ API key not loaded. Make sure your .env file has the correct key.")
    exit()

def ask_llm(prompt, retries=3, delay=3):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    data = {
        "model": "deepseek/deepseek-r1:free",  # ✅ Changed to more stable free model
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    for attempt in range(retries):
        try:
            response = requests.post(url, headers=headers, json=data, timeout=20)
            print(f"Status code: {response.status_code}")
            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]
            elif response.status_code == 401:
                return "❌ 401 Unauthorized. Check your API key or rate limit."
            else:
                print(f"⚠️ Error {response.status_code}: {response.text[:300]}")
        except requests.exceptions.Timeout:
            print(f"⏱️ Timeout on attempt {attempt + 1}")
        except Exception as e:
            print(f"❌ Exception: {e}")
        time.sleep(delay * (2 ** attempt))  # Exponential backoff
    return "❌ All attempts failed. Try again later."

