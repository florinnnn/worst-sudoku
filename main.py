from tkinter import *
from tkinter import messagebox

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
                    buttons[i][j]["fg"] = "gray"
    else:
        notes = False
        notesButton["text"] = "Notes - OFF"
        for i in range(9):
            for j in range(9):
                if buttons[i][j]["text"] == "":
                    buttons[i][j]["anchor"] = CENTER
                    buttons[i][j]["fg"] = "black"

nr = StringVar()

userInput = Frame(window)
userInput.grid(row = 3, column = 0, padx = 2, pady = 2)

inputLabel = Label(userInput,
                   font = ("Arial", 15),
                   height = 1,
                   width = 10,
                   text = "Number Input")
inputLabel.grid(row = 0, column = 0, padx = 2, pady = 2, sticky = NSEW)

intrare = Entry(userInput,
                #height = 2,
                width = 3,
                textvariable = nr)
intrare.grid(row = 0, column = 1, padx = 2, pady = 2, sticky = NSEW)

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
    if row == 9 - 1 and column == 9:
        return True

    if column == 9:
        row += 1
        column = 0

    if map[row][column] > 0:
        return solver(map, row, column + 1)

    for num in range(1, 9 + 1):
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
                    buttons[i][j]["anchor"] = CENTER
                    buttons[i][j]["fg"] = "black"
                    buttons[i][j]["text"] = str(startGrid[i][j])
            button["text"] = "SOLVED"
        else:
            return

start = False


def startGame(button):
    global start, startGrid
    if start == False:
        for i in range(9):
            for j in range(9):
                #print(type(i), type(j))
                if buttons[i][j]["text"] != "":
                    startGrid[i][j] = int(buttons[i][j]["text"])
        # check validity
        valid = True
        for i in range(9):
            for j in range(9):
                aux = startGrid[i][j]
                startGrid[i][j] = 0
                if aux == 0:
                    continue
                if not is_valid(startGrid, i, j, aux):
                    valid = False
                    buttons[i][j]["text"] = ""
                    aux = 0
                startGrid[i][j] = aux
        if not valid:
            messagebox.showerror("error", "same numbers in row/column/box")
            return
        mistakes.grid(row=3, column=1)
        notesButton.grid(row=0, column=3)
        solveButton["state"] = "normal"
        start = True
        button["text"] = "Stop"
        solver(startGrid, 0, 0)
        button.grid_forget()

def fill(button, i, j):
    global notes
    number = nr.get()
    if number.isdigit():
        if notes == False and int(number) != startGrid[i][j] and start == True:
            mistakesNumber = mistakes["text"].split(" ")
            mistakes["text"] = str(int(mistakesNumber[0]) + 1) + " mistakes"
            intrare.delete(0, END)
            return
    if "0" in number:
        intrare.delete(0, END)
        return
    if  button["anchor"] == NE and number.isdigit() and len(number) <= 3 and notes == True:
        button["text"] = number
    if button["text"] == "" and len(number) == 1 and number.isdigit():
        button["text"] = number
    if button["text"] != "" and number == "del" and (start == False or notes == True):
        button["text"] = ""
    if notes == False and button["anchor"] == NE and len(number) == 1 and number.isdigit():
        button["text"] = number
        button["anchor"] = CENTER
        button["fg"] = "black"
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