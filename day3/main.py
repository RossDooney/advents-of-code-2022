import os

# find overlappying char and use ord() to find its value. Then subtract ord('a') + 1 or ord('A') + 27

# f = open("input.txt", "r")

# first_part = ""
# second_part = ""
# score is 2639,the while loop does one to many iterations causing an error, could resolve by just using first solution with a 3rd var, but this feels closer to a good solution. Will rewrite later
common_char = ""
score = 0
count = 0

def solution1():
    with open("input.txt", "r") as f:
        line = True
        while line:
            line = (f.readline().rstrip(), f.readline().rstrip(), f.readline().strip())
            common_char = set.intersection(*map(set, line)).pop()
            if common_char.isupper() == True:
                score += int(ord(common_char) - ord("A") + 27)
            else:
                score += int(ord(common_char) - ord("a") + 1)
            print(score)




# for line in f:
#     # common_char = set(first_part).intersection(second_part).pop()
#     if common_char.isupper() == True:
#         score += int(ord(common_char) - ord("A") + 27)
#     else:
#         score += int(ord(common_char) - ord("a") + 1)

print(score)
