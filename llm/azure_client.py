from openai import AzureOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint=os.getenv("AZURE_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
)

DEPLOYMENT_NAME = "gpt-4o"


# ✅ NORMAL RESPONSE (used by agents)
def generate_response(messages):
    response = client.chat.completions.create(
        model=DEPLOYMENT_NAME,
        messages=messages,
        max_tokens=2000,
        temperature=0.7
    )

    if response and response.choices:
        return response.choices[0].message.content

    return "Error: No response from model"


# ✅ STREAMING RESPONSE (used for UI)
def stream_response(messages):
    response = client.chat.completions.create(
        model=DEPLOYMENT_NAME,
        messages=messages,
        stream=True,
        max_tokens=1000,
        temperature=0.7
    )

    for chunk in response:
        if chunk.choices:
            yield chunk.choices[0].delta.content or ""