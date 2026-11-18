
# ==========================================
# GAMEDEV MENTOR AI 2.0
# Developer: Chandrakant Mahto
# Decode Labs Internship - Task 1
# ==========================================

import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types

# 1. Load API key
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("ERROR: Gemini API key not found!")
    print("Please check your .env file.")
    raise SystemExit(1)

# 2. Initialize Gemini
client = genai.Client(api_key=API_KEY)

# Model configuration
MODEL = "gemini-3.5-flash-lite"

# 3. AI personality
SYSTEM_INSTRUCTION = """
You are GameDev Mentor AI, created by Chandrakant Mahto.

Your mission is to help beginners learn game development.

You are an expert mentor in:

1. Unity Engine
2. Unreal Engine
3. Godot Engine
4. C# Programming
5. C++ Programming
6. Python Programming
7. Game Design
8. Game Development Careers
9. AI in Video Games
10. Beginner Game Projects

YOUR BEHAVIOUR:

- Explain concepts in simple English.
- Give practical examples.
- Break difficult concepts into small steps.
- Provide realistic learning roadmaps.
- Help users debug programming errors.
- Recommend suitable tools and technologies.
- Never invent facts or salary promises.
- Admit when you do not know an answer.
- Stay focused on game development.

You are friendly, knowledgeable and practical.
"""

# 4. Create conversation
try:
    chat = client.chats.create(
        model=MODEL,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            temperature=0.7
        )
    )

except Exception as error:
    print("Could not initialize Gemini:", error)
    raise SystemExit(1)


# 5. Welcome screen
print("\n" + "=" * 50)
print("             GAMEDEV MENTOR AI")
print("=" * 50)

print("\nWelcome to your AI-powered GameDev Mentor!")

name = input("\nEnter your name: ").strip()

if not name:
    name = "Developer"

print(f"\nHello {name}!")

print("""
I can help you with game development,
programming, game engines and career guidance.

COMMANDS:
- help : Show available commands
- bye  : Exit the chatbot
""")

print("=" * 50)


# 6. Main chatbot function
def get_ai_response(message):

    max_attempts = 3

    for attempt in range(max_attempts):

        try:
            response = chat.send_message(message)

            if response.text:
                return response.text

            return "I couldn't generate a response. Please try again."

        except Exception as error:

            error_message = str(error).upper()

            temporary_error = any(
                code in error_message
                for code in [
                    "503",
                    "UNAVAILABLE",
                    "429",
                    "RESOURCE_EXHAUSTED",
                    "500",
                    "INTERNAL"
                ]
            )

            if temporary_error:

                if attempt < max_attempts - 1:

                    wait_time = 2 ** (attempt + 1)

                    print(
                        f"\nServer temporarily busy. "
                        f"Retrying in {wait_time} seconds..."
                    )

                    time.sleep(wait_time)

                else:
                    return (
                        "Gemini is currently unavailable or "
                        "the API quota has been reached. "
                        "Please try again later."
                    )

            else:
                return f"API Error: {error}"


# 7. Main conversation loop
while True:

    try:

        user_message = input(f"\n{name}: ").strip()

        # Empty input
        if not user_message:
            continue

        # Exit command
        if user_message.lower() in ["bye", "exit", "quit"]:

            print("\nGameDev Mentor:")
            print(f"Goodbye {name}!")
            print("Keep learning and keep building games!")

            break

        # Help command
        elif user_message.lower() == "help":

            print("""
GAMEDEV MENTOR AI - HELP

You can ask questions like:

1. How do I start game development?
2. Unity vs Unreal Engine?
3. Explain C# for beginners.
4. How do I create my first 3D game?
5. Give me a 30-day learning roadmap.
6. What are game development career options?
7. How is AI used in video games?
8. Explain enemy AI in Unity.

You can also ask your own questions!
""")

            continue

        # AI response
        print("\nGameDev Mentor: Thinking...\n")

        answer = get_ai_response(user_message)

        print("GameDev Mentor:", answer)

    except KeyboardInterrupt:

        print("\n\nChatbot stopped. Goodbye!")
        break

    except Exception as error:

        print("\nUnexpected error:", error)


# 8. End program
print("\nThank you for using GameDev Mentor AI!")
