import os
import json
import urllib.request

api_key = os.environ["GEMINI_API_KEY"]

prompt = """
Create a YouTube video script about an interesting fact from Japan.

Return ONLY valid JSON in this exact format:
{
  "title": "video title",
  "script": "full narration script"
}

The script should be around 500 words, engaging and suitable for a general audience.
"""

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

data = {
    "contents": [
        {
            "parts": [
                {
                    "text": prompt
                }
            ]
        }
    ]
}

request = urllib.request.Request(
    url,
    data=json.dumps(data).encode("utf-8"),
    headers={
        "x-goog-api-key": api_key,
        "Content-Type": "application/json"
    },
    method="POST"
)

with urllib.request.urlopen(request) as response:
    result = json.loads(response.read().decode("utf-8"))

text = result["candidates"][0]["content"]["parts"][0]["text"]

print(text)
