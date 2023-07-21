import os


f = open("calories.txt", "r")
count = 0
biggest_elf = 0
current_elf = 0
for line in f:
    count += 1
    if line != "\n":
        current_elf += int(line)
    else:
        if biggest_elf < current_elf:
            biggest_elf = current_elf
        current_elf = 0

print(biggest_elf)
