import pandas as pd

games = pd.read_csv("games.csv")

print("AI Game Recommendation System\n")

genre = input("Genre : ")
difficulty = input("Difficulty (Easy/Medium/Hard) : ")
mode = input("Mode (Single/Multiplayer) : ")
spec = input("PC Type (Low/Mid/High) : ")

scores = []

for i in range(len(games)):

    score = 0

    if games.loc[i, "Genre"].lower() == genre.lower():
        score += 25

    if games.loc[i, "Difficulty"].lower() == difficulty.lower():
        score += 25

    if games.loc[i, "Mode"].lower() == mode.lower():
        score += 25

    if games.loc[i, "Spec"].lower() == spec.lower():
        score += 25

    scores.append(score)

games["Match"] = scores

games = games.sort_values(by="Match", ascending=False)

print("\nTop Recommendations\n")

count = 0

for i in range(len(games)):

    if games.iloc[i]["Match"] > 0:

        print("Game :", games.iloc[i]["Game"])
        print("Match :", games.iloc[i]["Match"], "%")
        print()

        count += 1

    if count == 3:
        break

if count == 0:
    print("No suitable game found.")