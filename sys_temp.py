import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()
# Get API key
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("Groq API key is missing!")
# Initialize Groq client
client = Groq(api_key=api_key)
model = "openai/gpt-oss-120b"
messages = [
    {
        "role": "system",
        "content": """
        You are an expert brand strategist.
        Suggest creative, memorable, one-word names
        for a food company.
        Names should be:
        - Unique and catchy
        - Easy to pronounce
        - Suitable for a food brand
        - Memorable
        """,
    },
    {"role": "user", "content": "Suggest 10 names for my food company."},
]
response = client.chat.completions.create(
    model=model, messages=messages, temperature=0.8
)
answer = response.choices[0].message.content
print(answer)
