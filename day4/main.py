import os
import re

f = open("input.txt", "r")
score = 0
def range_overlap(range_1, range_2):
    start_range_1, end_range_1 = map(int, range_1.split('-'))
    start_range_2, end_range_2 = map(int, range_2.split('-'))

    return start_range_2 <= start_range_1 and end_range_1 <= end_range_2
for line in f:
    first_range, second_range = line.split(',')
    if range_overlap(first_range, second_range) or range_overlap(second_range, first_range):
        score+=1


    

print(score)
        

