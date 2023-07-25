import os
import re

f = open("input.txt", "r")


def range_overlap(range_1, range_2):
    start_range_1, end_range_1 = map(int, range_1.split("-"))
    start_range_2, end_range_2 = map(int, range_2.split("-"))

    return start_range_2 <= start_range_1 and end_range_1 <= end_range_2


def part_one_sol():
    score = 0
    for line in f:
        first_range, second_range = line.split(",")
        if range_overlap(first_range, second_range) or range_overlap(
            second_range, first_range
        ):
            score += 1
    print(score)
    f.close()


def part_two_sol():
    score = 0

    # x1 <= y2 && y1 <= x2

    for line in f:
        first_range, second_range = line.split(",")
        start_range_1, end_range_1 = map(int, first_range.split("-"))
        start_range_2, end_range_2 = map(int, second_range.split("-"))
        # 12, 80 - 12, 81
        #       12 <= 81 and 12 <= 80
        if start_range_1 <= end_range_2 and start_range_2 <= end_range_1:
            score += 1

    print(score)
    f.close()


# part_two_sol()
# part_one_sol()
