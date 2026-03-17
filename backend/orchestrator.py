from agents.planner import planner_agent
from agents.writer import writer_agent
from agents.editor import editor_agent
from memory.chat_memory import ChatMemory

# ✅ Initialize memory
memory = ChatMemory()

def run_pipeline_stream(user_input, content_type):

    memory.add_user(user_input)

    history = memory.get_history()

    # Build context
    context = ""
    for msg in history:
        context += f"{msg['role']}: {msg['content']}\n"

    # Planner
    plan = planner_agent(context)
    yield "### 📌 Content Plan\n\n" + plan + "\n\n"

    # Writer
    draft = writer_agent(plan, content_type)
    yield "### ✍️ Generated Content\n\n" + draft + "\n\n"

    # Editor
    final = editor_agent(draft)

    memory.add_assistant(final)

    yield "### ✅ Final Output\n\n"

    for char in final:
        yield char