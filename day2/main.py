import os

# rock = a and x, worth 1 point
# paper = b and y, worth 2 points
# scissors = c and z, worth 3 points

f = open("input.txt", "r")
score = 0

for line in f:
    our_action = line[2]
    opponent_player = line[0]
    if our_action == "X":
        score += 1
        if opponent_player == "C":
            score += 6
        elif opponent_player == "A":
            score += 3
    if our_action == "Y":
        score += 2
        if opponent_player == "A":
            score += 6
        elif opponent_player == "B":
            score += 3
    if our_action == "Z":
        score += 3
        if opponent_player == "B":
            score += 6
        elif opponent_player == "C":
            score += 3

print(score)
