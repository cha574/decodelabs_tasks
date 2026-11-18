
import os
import time
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load API key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Page configuration
st.set_page_config(
    page_title="GameDev Mentor AI",
    page_icon="🎮",
    layout="centered"
)

# Custom styling
st.markdown("""
<style>
.main {
    background-color: #0e1117;
}
.title {
    text-align: center;
    font-size: 38px;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    color: #a0a0a0;
    margin-bottom: 25px;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown(
    '<div class="title">🎮 GameDev Mentor AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Your personal AI game development mentor</div>',
    unsafe_allow_html=True
)

st.divider()

# Sidebar
with st.sidebar:
    st.title("🎮 GameDev Mentor")
    st.write("AI-powered game development assistant.")

    st.subheader("What I can help with")
    st.write("""
    - Unity and Unreal Engine
    - C# and C++ programming
    - Game design
    - Beginner projects
    - Career guidance
    - AI in video games
    """)

    st.divider()

    st.caption("Developed by Chandrakant Mahto")

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.chat = None
        st.rerun()

# Check API key
if not API_KEY:
    st.error("Gemini API key not found. Check your .env file.")
    st.stop()

# Initialize Gemini client
@st.cache_resource
def get_client():
    return genai.Client(api_key=API_KEY)

client = get_client()

# AI instructions
SYSTEM_INSTRUCTION = """
You are GameDev Mentor AI, created by Chandrakant Mahto.

Your purpose is to help beginners learn game development.

You specialize in:
- Unity Engine
- Unreal Engine
- Godot Engine
- C# and C++
- Python
- Game design
- Game development careers
- AI in video games

Instructions:
1. Explain concepts in simple English.
2. Give practical examples.
3. Break complex topics into steps.
4. Provide realistic learning roadmaps.
5. Help users debug programming errors.
6. Never invent facts or salary promises.
7. Admit when you don't know something.
8. Stay focused on game development.
"""

MODEL = "gemini-3.5-flash-lite"

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat" not in st.session_state:
    st.session_state.chat = client.chats.create(
        model=MODEL,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            temperature=0.7
        )
    )

# Welcome message
if not st.session_state.messages:
    st.info(
        "👋 Welcome! Ask me anything about game development."
    )

# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input(
    "Ask your game development question..."
)

if user_input:

    # Display user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate AI response
    with st.chat_message("assistant"):

        response_placeholder = st.empty()

        with st.spinner("GameDev Mentor is thinking..."):

            answer = None

            for attempt in range(3):

                try:
                    response = st.session_state.chat.send_message(
                        user_input
                    )

                    answer = response.text or "No response generated."
                    break

                except Exception as error:

                    error_text = str(error).upper()

                    temporary_error = any(
                        code in error_text
                        for code in [
                            "503",
                            "UNAVAILABLE",
                            "429",
                            "RESOURCE_EXHAUSTED",
                            "500",
                            "INTERNAL"
                        ]
                    )

                    if temporary_error and attempt < 2:
                        time.sleep(2 ** (attempt + 1))
                    else:
                        answer = (
                            "Sorry, I couldn't get a response. "
                            "Please try again later.\n\n"
                            f"Error: {error}"
                        )
                        break

        response_placeholder.markdown(answer)

    # Save assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
