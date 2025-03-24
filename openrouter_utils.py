import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

def call_openrouter_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or try gpt-4 or other free models listed
        messages=[
            {"role": "system", "content": "You are a certified dietitian."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content
