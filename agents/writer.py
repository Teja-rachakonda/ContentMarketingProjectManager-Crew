from llm.azure_client import generate_response

def writer_agent(plan, content_type):

    if content_type == "Blog":
        instruction = """
Write a FULL blog post with:
- Title
- Introduction
- Sections
- Conclusion
- Call-to-action
"""
    
    elif content_type == "LinkedIn":
        instruction = """
Convert this into a professional LinkedIn post:
- Short and engaging
- Use simple language
- Add spacing for readability
"""
    
    elif content_type == "Instagram":
        instruction = """
Create 5 Instagram captions:
- Short and catchy
- Use emojis
- Add hashtags
"""
    
    elif content_type == "YouTube":
        instruction = """
Create a YouTube video script:
- Hook (first 10 seconds)
- Main content
- Ending + CTA
"""
    
    else:
        instruction = "Generate content"

    messages = [
        {"role": "system", "content": "You are an expert content creator."},
        {"role": "user", "content": f"""
Using this plan:

{plan}

{instruction}
"""}
    ]

    return generate_response(messages)