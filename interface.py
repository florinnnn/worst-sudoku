from tkinter import *

window = Tk()

window.title("Sudoku")
#window.geometry("500x500")
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

def fill(button):
    global notes
    number = nr.get()
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
                                    command = lambda i=i,j=j:fill(buttons[i][j]))
        elif i < 3 and j < 6:
            current_button = Button(middle_top_frame,
                                    text = "",
                                    font = ("Arial", 15),
                                    height = 2,
                                    width = 4,
                                    command = lambda i=i,j=j:fill(buttons[i][j]))
        elif i < 3 and j < 9:
            current_button = Button(right_top_frame,
                                    text = "",
                                    font = ("Arial", 15),
                                    height = 2,
                                    width = 4,
                                    command = lambda i=i,j=j:fill(buttons[i][j]))
        elif i < 6 and j < 3:
            current_button = Button(left_mid_frame,
                                    text = "",
                                    font = ("Arial", 15),
                                    height = 2,
                                    width = 4,
                                    command = lambda i=i,j=j:fill(buttons[i][j]))
        elif i < 6 and j < 6:
            current_button = Button(middle_mid_frame,
                                    text = "",
                                    font = ("Arial", 15),
                                    height = 2,
                                    width = 4,
                                    command = lambda i=i,j=j:fill(buttons[i][j]))
        elif i < 6 and j < 9:
            current_button = Button(right_mid_frame,
                                    text = "",
                                    font = ("Arial", 15),
                                    height = 2,
                                    width = 4,
                                    command = lambda i=i,j=j:fill(buttons[i][j]))
        elif i < 9 and j < 3:
            current_button = Button(left_bottom_frame,
                                    text = "",
                                    font = ("Arial", 15),
                                    height = 2,
                                    width = 4,
                                    command = lambda i=i,j=j:fill(buttons[i][j]))
        elif i < 9 and j < 6:
            current_button = Button(middle_bottom_frame,
                                    text = "",
                                    font = ("Arial", 15),
                                    height = 2,
                                    width = 4,
                                    command = lambda i=i,j=j:fill(buttons[i][j]))
        else:
            current_button = Button(right_bottom_frame,
                                    #anchor = NW,
                                    text = "",
                                    font = ("Arial", 15),
                                    height = 2,
                                    width = 4,
                                    command = lambda i=i, j=j:fill(buttons[i][j]))
        current_button.grid(row = i + 1, column = j + 1, sticky = NSEW)
        buttons[i][j] = current_button
notesButton = Button(text = "Notes - OFF",
                     font = ("Arial", 13),
                     height = 2,
                     width = 15,
                     command = lambda: switch())
notesButton.grid(row = 0, column = 3)
quit = Button(text = "close",
              font = (12),
              height = 1,
              width = 6,
              command=window.destroy)
quit.grid(row = 1, column = 3, pady = 10)
window.mainloop()