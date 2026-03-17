from llm.azure_client import generate_response
from llm.azure_client import generate_response
def editor_agent(content):
    messages = [
        {
            "role": "system",
            "content": "You are a professional content editor."
        },
        {
            "role": "user",
            "content": f"""
Refine and improve the following content:

{content}

Make sure:
- It is COMPLETE (no missing parts)
- Properly formatted with headings
- Easy to read
- SEO optimized
- Professional quality

Return FINAL polished version only.
"""
        }
    ]

    return generate_response(messages)