# GameDev Mentor Bot

## About

GameDev Mentor Bot is an AI-powered chatbot developed in Python as part of my Decode Labs AI Internship.

I created this project because I want to become a game developer. During my learning journey, I built simple 2D and 3D games and learned from many beginner mistakes. This chatbot is designed to help beginners learn game development by answering their questions, providing guidance, and explaining important concepts.

The project was initially developed as a rule-based chatbot and later upgraded into an AI-powered chatbot using the Google Gemini API.

## Features

- AI-powered responses using Google Gemini
- Career guidance for aspiring game developers
- Game development learning roadmaps
- Programming tools and technology suggestions
- AI in game development
- Beginner-friendly project ideas
- Guidance on common game development mistakes
- Interactive web-based chat interface
- Conversation history during the chat session
- Clear Chat functionality

## Technologies

- Python
- Google Gemini API
- Google GenAI SDK
- Streamlit
- Python-dotenv
- Environment variables for API key security

## Project Structure

```text
Task-1-Chandrakant/
│
├── app.py
├── chatbot.py
├── requirements.txt
├── README.md
├── .gitignore
└── image.png
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/cha574/decodelabs_tasks.git
```

2. Navigate to the project folder:

```bash
cd decodelabs_tasks/Task-1-Chandrakant
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project folder and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

## Run the Application

Run the Streamlit application using:

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to use the chatbot.

## Security

- The Gemini API key is stored in a `.env` file.
- The `.env` file is excluded from GitHub using `.gitignore`.
- Never share or upload your API key publicly.

## Developer

**Chandrakant Mahto**

Maharaja Surajmal Institute, Delhi

Decode Labs AI Internship
