import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

st.set_page_config(
    page_title="Gemini ChatBot",
    page_icon="🤖",
    layout="centered",
)

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    st.error("❌ GOOGLE_API_KEY not found in .env")
    st.stop()

# Initialize Gemini client
client = genai.Client(api_key=API_KEY)

st.title("🤖 Gemini ChatBot")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
prompt = st.chat_input("Ask something...")
if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    try:
        # ✅ USE CORRECT MODEL FROM THE AVAILABLE LIST
        response = client.models.generate_content(
            model="gemini-2.5-flash",  # Changed to available model
            contents=prompt
        )

        reply = response.text

        st.chat_message("assistant").markdown(reply)
        st.session_state.messages.append(
            {"role": "assistant", "content": reply}
        )
    except Exception as e:
        st.error(f"Error: {str(e)}")