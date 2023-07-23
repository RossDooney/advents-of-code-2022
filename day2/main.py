import os

# x=lose,y=draw,z=win

f = open("input.txt", "r")
score = 0

for line in f:
    results = line[2]
    opponent_player = line[0]

    if results == "Z":
        score += 6
        if opponent_player == "A":
            score += 2
        elif opponent_player == "B":
            score += 3
        else:
            score += 1
    elif results == "Y":
        score += 3
        if opponent_player == "A":
            score += 1
        elif opponent_player == "B":
            score += 2
        else:
            score += 3
    else:
        if opponent_player == "A":
            score += 3
        elif opponent_player == "B":
            score += 1
        else:
            score += 2


print(score)
