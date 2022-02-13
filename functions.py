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

grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

if solver(grid, 0, 0):
    printSudoku(grid)