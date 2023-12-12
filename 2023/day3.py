import numpy as np
from helpers.matrix_operations import pad_array

file = open("input.txt", "r")
lines = file.read().splitlines()

matrix = pad_array(lines, ".")

nonSymbols = "0123456789."
firstOccurance = True


def get_number(matrix, row, col):
    number = matrix[row][col]
    index, revindex = 1, -1
    while matrix[row][col + index].isdigit():
        number += matrix[row][col + index]
        index += 1

    number = number[::-1]
    while matrix[row][col + revindex].isdigit():
        number += matrix[row][col + revindex]
        revindex -= 1

    return int(number[::-1])


def main(matrix):
    score = 0
    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            if char == "*":
                print("hi")
                numbers_adj_to_gears = []
                for subrow in range(i - 1, i + 2):
                    firstOccurance = True
                    for subcol in range(j - 1, j + 2):
                        if matrix[subrow][subcol].isdigit() and firstOccurance:
                            numbers_adj_to_gears.append(
                                get_number(matrix, subrow, subcol)
                            )
                            firstOccurance = False
                        elif not matrix[subrow][subcol].isdigit():
                            firstOccurance = True

                if len(numbers_adj_to_gears) == 2:
                    score += np.prod(numbers_adj_to_gears)

    print(score)


main(matrix)

# too low: 69932862
