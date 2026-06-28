# 🎮 AI Game Recommendation System

This project was developed as part of my AI Internship at DecodeLabs.

The purpose of this project is to recommend games based on the user's preferences. The user selects a game genre, difficulty level, game mode, and PC type. Based on these choices, the program calculates a match score and recommends the most suitable games.

## Features

- Recommend games based on user preferences
- Match score for every recommended game
- Displays the top matching games
- Uses a simple CSV dataset
- Easy to understand and beginner-friendly

## Technologies Used

- Python
- Pandas

## Project Workflow

1. Load the game dataset
2. Take user input
3. Compare user preferences with every game
4. Calculate a match score
5. Sort games based on the score
6. Display the best recommendations

## Dataset

The project uses a custom **games.csv** file.

Each game contains:

- Game Name
- Genre
- Difficulty
- Mode
- Platform
- PC Requirement

## Example

**User Input**

```
Genre : Action
Difficulty : Medium
Mode : Multiplayer
PC Type : Low
```

**Output**

```
Top Recommendations

Game : Valorant
Match : 100%

Game : CS2
Match : 75%

Game : Apex Legends
Match : 75%
```

## Learning Outcomes

Through this project, I learned:

- Basic recommendation systems
- Working with CSV files using Pandas
- Data filtering and comparison
- Match score calculation
- Sorting data based on user preferences

## Future Improvements

- Add more games to the dataset
- Create a Streamlit web application
- Improve recommendations using Machine Learning
- Add game images and descriptions

## Author

**Chandrakant Mahto**

AI Internship – DecodeLabs