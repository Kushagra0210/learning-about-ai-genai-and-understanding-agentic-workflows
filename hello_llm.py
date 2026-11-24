import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("groq_api_key")
if not my_api_key:
    raise ValueError("Api key nhi hai ")

Client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"
role = "user"
prompt = "Do you know icecream amul"
message = {"role": role, "content": prompt}
messages = [message]
response = Client.chat.completions.create(model=model, messages=messages)
print(response.choices[0].message.content)
