import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from backend.orchestrator import run_pipeline_stream
from utils.voice_input import get_voice_input
from utils.pdf_generator import create_pdf

st.set_page_config(page_title="AI Content Generator", layout="wide")

st.title("🚀 AI Content Generator")

# 🧠 Memory (chat history)
if "history" not in st.session_state:
    st.session_state.history = []

# 🧠 Store topic
if "topic" not in st.session_state:
    st.session_state.topic = ""

# 🔹 TEXT INPUT
topic_input = st.text_input("Enter Topic", value=st.session_state.topic)

# 🎤 VOICE INPUT
if st.button("🎤 Speak"):
    voice_text = get_voice_input()

    if voice_text:
        st.session_state.topic = voice_text
        st.success(f"You said: {voice_text}")
    else:
        st.error("Could not understand voice input")

# 🔽 CONTENT TYPE
content_type = st.selectbox(
    "Select Content Type",
    ["Blog", "LinkedIn", "Instagram", "YouTube"]
)

# 🔁 FINAL TOPIC
topic = st.session_state.topic or topic_input

# 🚀 GENERATE BUTTON
if st.button("Generate"):
    if topic.strip():
        st.session_state.history.append(("user", topic))

        output_placeholder = st.empty()
        full_output = ""

        # 🔥 LOADING SPINNER
        with st.spinner("Generating AI content..."):

            for chunk in run_pipeline_stream(topic, content_type):
                full_output += chunk
                output_placeholder.markdown(full_output)

        st.session_state.history.append(("assistant", full_output))

        # 📋 COPY VIEW
        st.markdown("## 📋 Copy Content")
        st.code(full_output, language="markdown")

        # 📄 TXT DOWNLOAD
        st.download_button(
            label="📄 Download as TXT",
            data=full_output,
            file_name="content.txt",
            mime="text/plain"
        )

        # 📥 PDF DOWNLOAD (FIXED)
        pdf_file = create_pdf(full_output)

        if pdf_file and os.path.exists(pdf_file):
            with open(pdf_file, "rb") as f:
                st.download_button(
                    label="📥 Download as PDF",
                    data=f,
                    file_name="ai_content.pdf",
                    mime="application/pdf"
                )
        else:
            st.error("❌ PDF not generated")

    else:
        st.warning("Please enter a topic or use voice input")

# 💬 CHAT HISTORY
st.markdown("## 💬 Chat History")

for role, msg in st.session_state.history:
    if role == "user":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🤖 AI:** {msg}")