# Project 1: Rule-Based Chatbot
# Name: Chandrakant Mahto
# College: Maharaja Surajmal Institute, delhi
# Internship: Decode Labs AI Internship
# This chatbot answers basic questions about game development.

print("=" * 40)
print("        GameDev Mentor Bot")
print("=" * 40)

name = input("Before we start, what is your name ? ")

print("\nHello", name)
print("Myself the creator,I want to become the best game developer, and I have already created some")
print("simple 2D and 3D games. During my learning journey I made many mistakes,")
print("so I created this chatbot to help beginners avoid those mistakes.")
print("Welcome to GameDev Mentor Bot.b")
print("I can answer beginner questions about game development.")
print("\nType 'help' to see all commands.")
print("Type 'bye' to exit.\n")

responses = {

    "hello":
    "Hello! Nice to meet you.",

    "hi":
    "Hi! How can I help you?",

    "who are you":
    "I am GameDev Mentor Bot. I answer some beginner questions about game development.",

    "career":
    """
Game Development Career

Yes, you can become a game developer without a CS degree.
From what I have learned, companies usually care more about your skills and projects.

Some popular roles are:
- Gameplay Programmer
- Game Designer
- Level Designer
- QA Tester

Developers earn money in different ways like studio jobs, freelancing, selling games or ads.
""",

    "learning":
    """
If you are new, don't try to learn everything together.

I would do it like this:

Python or C#
        
Choose one game engine
        
Build 2 or 3 small games
        
Learn Git
        
Create a portfolio

Everyone learns at a different speed, so don't compare yourself with others.
""",

    "tools":
    """
For beginners I would suggest Unity.

Why?

- Easy to learn
- Lots of tutorials
- Huge community

Useful software:
VS Code
Unity Hub
Blender
Git

Python is good for learning programming, but C# is more useful if you want to make games in Unity.
""",

    "games":
    """
I think starting with 2D games is a better choice.

My first projects would be:

• Snake
• Flappy Bird
• Character Controller (3D)

Many beginners try to make games like GTA or PUBG.
I think that's too difficult for a first project.
Finish one small game first.
""",

    "ai":
    """
I use AI mainly when I get stuck.

For example:
- understanding code
- fixing errors
- getting ideas

But I never copy everything directly.
I always try to understand what the code is doing.

That helps me learn faster.
""",

    "mistakes":
    """
Big mistakes beginners make:

Watching tutorials every day but never making a project.

Trying to build a huge game.

Giving up after the first bug.

Not finishing projects.

My advice?
Complete one small project before starting the next one.
""",
    "my first game":
"""
The first game I completed was a cube runner.
It wasn't perfect, but finishing it taught me much more than
watching tutorials for weeks.

My advice:
Don't worry about making a perfect game.
Focus on completing one.
""",

    "help":
    """
Available commands

hello
career
learning
tools
games
ai
mistakes
who are you
my first game
bye
"""
}

while True:

    user = input("\nYou : ").lower().strip()

    if user == "bye":
        print("\nGameDev_Bot : Thanks for chatting with me.")
        print("Good luck with your game development journey!")
        break

    elif user in responses:
        print("\nGameDev_Bot :")
        print(responses[user])

    else:
        print("\nGameDev_Bot : Sorry, I don't know the answer.")
        print("Type 'help' to see the available commands.")
