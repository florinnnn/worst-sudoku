from constants import *

# functie printare sudoku rezolvat

def printSudoku(map):
    for i in range(N):
        for j in range(N - 1):
            print(map[i][j], " ", end = "")
        print(map[i][j])