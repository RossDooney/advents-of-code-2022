import os

#find overlappying char and use ord() to find its value. Then subtract ord('a') + 1 or ord('A') + 27

f = open("input.txt", "r")

first_part =""
second_part=""
common_char = ""
score = 0


for line in f:
    first_part = line[:len(line)//2]
    second_part = line[len(line)//2:]
    common_char = set(first_part).intersection(second_part).pop()
    if common_char.isupper() == True:
        score += int(ord(common_char) - ord('A')+27)
    else:
        score += int(ord(common_char) - ord('a')+1)

print(score)




