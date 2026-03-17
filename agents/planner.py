from llm.azure_client import generate_response

def planner_agent(context):
    messages = [
        {
            "role": "system",
            "content": "You are a senior content strategist."
        },
        {
            "role": "user",
            "content": """
Create a COMPLETE content strategy based on the conversation provided.

Include:
1. Target Audience
2. Content Goals
3. Content Pillars
4. 10 Video Ideas
5. Blog Structure

Make it structured and clear.
"""
        },
        {
            "role": "user",
            "content": context   # ✅ pass context separately (NO f-string issue)
        }
    ]

    return generate_response(messages)