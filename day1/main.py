import os
import numpy as np


f = open("calories.txt", "r")
count = 0
biggest_elf = np.array([0, 0, 0])
current_elf = 0
total_calories = 0
for line in f:
    count += 1
    if line != "\n":
        current_elf += int(line)
    else:
        if biggest_elf[0] < current_elf:
            biggest_elf[0] = current_elf
            biggest_elf = np.sort(biggest_elf)[::1]
        current_elf = 0

for i in range(0, len(biggest_elf)):
    total_calories = total_calories + biggest_elf[i]


print(total_calories)
