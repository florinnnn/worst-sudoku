from tkinter import *
from constants import *

startGrid = [[0 for i in range(9)] for j in range(9)]

window = Tk()

window.title("Sudoku")
window.configure(bg="white")
window.resizable(False, False)

left_top_frame = Frame(window)
left_top_frame.grid(row = 0, column = 0, padx = 2, pady = 2, sticky = NSEW)

middle_top_frame = Frame(window)
middle_top_frame.grid(row = 0, column = 1, padx = 2, pady = 2, sticky = NSEW)

right_top_frame = Frame(window)
right_top_frame.grid(row = 0, column = 2, padx = 2, pady = 2, sticky = NSEW)

left_mid_frame = Frame(window)
left_mid_frame.grid(row = 1, column = 0, padx = 2, pady = 2, sticky = NSEW)

middle_mid_frame = Frame(window)
middle_mid_frame.grid(row = 1, column = 1, padx = 2, pady = 2, sticky = NSEW)

right_mid_frame = Frame(window)
right_mid_frame.grid(row = 1, column = 2, padx = 2, pady = 2, sticky = NSEW)

left_bottom_frame = Frame(window)
left_bottom_frame.grid(row = 2, column = 0, padx = 2, pady = 2, sticky = NSEW)

middle_bottom_frame = Frame(window)
middle_bottom_frame.grid(row = 2, column = 1, padx = 2, pady = 2, sticky = NSEW)

right_bottom_frame = Frame(window)
right_bottom_frame.grid(row = 2, column = 2, padx = 2, pady = 2, sticky = NSEW)

buttons = [[None for i in range(9)] for j in range(9)]

notes = False

def switch():
    global notes
    if notes == False:
        notes = True
        notesButton["text"] = "Notes - ON"
        for i in range(9):
            for j in range(9):
                if buttons[i][j]["text"] == "":
                    buttons[i][j]["anchor"] = NE
    else:
        notes = False
        notesButton["text"] = "Notes - OFF"
        for i in range(9):
            for j in range(9):
                if buttons[i][j]["text"] == "":
                    buttons[i][j]["anchor"] = CENTER

nr = StringVar()

intrare = Entry(window, textvariable = nr, bg = "red")
intrare.grid(row = 3, column = 0, padx = 2, pady = 2, sticky = NSEW)

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

def solveSudoku(button):
    if start == True:
        if solver(startGrid, 0, 0):
            for i in range(9):
                for j in range(9):
                    buttons[i][j]["text"] = str(startGrid[i][j])
                #window.after(1000, None)
            button["text"] = "SOLVED"
        else:
            return

start = False

def startGame(button):
    global start, startGrid
    if start == False:
        start = True
        mistakes.grid(row=3, column=1)
        notesButton.grid(row=0, column=3)
        solveButton["state"] = "normal"
        button["text"] = "Stop"
        for i in range(9):
            for j in range(9):
                if buttons[i][j]["text"] != "":
                    startGrid[i][j] = int(buttons[i][j]["text"])
        solver(startGrid, 0, 0)

def fill(button, i, j):
    global notes
    number = nr.get()
    if number.isdigit():
        if notes == False and int(number) != startGrid[i][j] and start == True:
            mistakesNumber = mistakes["text"].split(" ")
            mistakes["text"] = str(int(mistakesNumber[0]) + 1) + " mistakes"
            return
    if "0" in number:
        intrare.delete(0, END)
        return
    if  button["anchor"] == NE and number.isdigit() and notes == True:
        button["text"] = number
    if button["text"] == "" and len(number) == 1 and number.isdigit():
        button["text"] = number
    if button["text"] != "" and number == "delete":
        button["text"] = ""
    if notes == False and button["anchor"] == NE and len(number) == 1 and number.isdigit():
        button["text"] = number
        button["anchor"] = CENTER
    intrare.delete(0, END)

for i in range(9):
    for j in range(9):
        if i < 3 and j < 3:
            current_button = Button(left_top_frame,
                                    text = "",
                                    font = ("Arial", 15),
                                    height = 2,
                                    width = 4,
                                    command = lambda i=i,j=j:fill(buttons[i][j], i, j))
        elif i < 3 and j < 6:
            current_button = Button(middle_top_frame,
                                    text = "",
                                    font = ("Arial", 15),
                                    height = 2,
                                    width = 4,
                                    command = lambda i=i,j=j:fill(buttons[i][j], i, j))
        elif i < 3 and j < 9:
            current_button = Button(right_top_frame,
                                    text = "",
                                    font = ("Arial", 15),
                                    height = 2,
                                    width = 4,
                                    command = lambda i=i,j=j:fill(buttons[i][j], i, j))
        elif i < 6 and j < 3:
            current_button = Button(left_mid_frame,
                                    text = "",
                                    font = ("Arial", 15),
                                    height = 2,
                                    width = 4,
                                    command = lambda i=i,j=j:fill(buttons[i][j], i, j))
        elif i < 6 and j < 6:
            current_button = Button(middle_mid_frame,
                                    text = "",
                                    font = ("Arial", 15),
                                    height = 2,
                                    width = 4,
                                    command = lambda i=i,j=j:fill(buttons[i][j], i, j))
        elif i < 6 and j < 9:
            current_button = Button(right_mid_frame,
                                    text = "",
                                    font = ("Arial", 15),
                                    height = 2,
                                    width = 4,
                                    command = lambda i=i,j=j:fill(buttons[i][j], i, j))
        elif i < 9 and j < 3:
            current_button = Button(left_bottom_frame,
                                    text = "",
                                    font = ("Arial", 15),
                                    height = 2,
                                    width = 4,
                                    command = lambda i=i,j=j:fill(buttons[i][j], i, j))
        elif i < 9 and j < 6:
            current_button = Button(middle_bottom_frame,
                                    text = "",
                                    font = ("Arial", 15),
                                    height = 2,
                                    width = 4,
                                    command = lambda i=i,j=j:fill(buttons[i][j], i, j))
        else:
            current_button = Button(right_bottom_frame,
                                    #anchor = NW,
                                    text = "",
                                    font = ("Arial", 15),
                                    height = 2,
                                    width = 4,
                                    command = lambda i=i, j=j:fill(buttons[i][j], i, j))
        current_button.grid(row = i + 1, column = j + 1, sticky = NSEW)
        buttons[i][j] = current_button

mistakes = Label(text = "0 mistakes",
                 font = ("Arial", 15),
                 height = 2,
                 width = 13)

notesButton = Button(text = "Notes - OFF",
                     font = ("Arial", 15),
                     height = 2,
                     width = 15,
                     command = lambda: switch())

solveButton = Button(text = "Solve using BT",
                     state = "disabled",
                     font = ("Arial", 15),
                     height = 2,
                     width = 13,
                     command = lambda: solveSudoku(solveButton))
solveButton.grid(row = 3, column = 2)

startButton = Button(text = "Start",
                     font = ("Arial", 15),
                     height = 2,
                     width = 5,
                     command = lambda:startGame(startButton))
startButton.grid(row = 1, column = 3, padx = 60, pady = 10)
quit = Button(text = "close",
              font = ("Arial", 15),
              height = 1,
              width = 6,
              command=window.destroy)
quit.grid(row = 2, column = 3, pady = 10)
window.mainloop()
