from constants import *

# functie printare sudoku rezolvat

def printSudoku(map):
    for i in range(N):
        for j in range(N):
            print(map[i][j], " ", end = "")
        print()

# functie verificare validitate so far

def is_valid(map, row, column, number):
    for i in range(9):
        if map[row][i] == number:
            return False

    for i in range(9):
        if map[i][column] == number:
            return False

    startRow = row - row % 3
    startColumn = column - column % 3
    for i in range(3):
        for j in range(3):
            if map[i + startRow][j + startColumn] == number:
                return False

    return True

# functie recursiva backtracking pt sudoku

def solver(map, row, column):
    if row == N - 1 and column == N:
        return True

    if column == N:
        row += 1
        column = 0

    if map[row][column] > 0:
        return solver(map, row, column + 1)

    for num in range(1, N + 1):
        if is_valid(map, row, column, num):
            map[row][column] = num
            if solver(map, row, column + 1):
                return True
        map[row][column] = 0
    return False