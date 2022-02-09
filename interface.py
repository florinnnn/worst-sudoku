from tkinter import *

window = Tk()

window.title("Sudoku")
window.geometry("1280x920")
window.configure(bg="yellow")



left_top_frame = Frame(window)
left_top_frame.grid(row = 0, column = 0, padx = 5, pady = 5)

middle_top_frame = Frame(window)
middle_top_frame.grid(row = 0, column = 1, padx = 5, pady = 5)

right_top_frame = Frame(window)
right_top_frame.grid(row = 0, column = 2, padx = 5, pady = 5)

left_mid_frame = Frame(window)
left_mid_frame.grid(row = 1, column = 0, padx = 5, pady = 5)

middle_mid_frame = Frame(window)
middle_mid_frame.grid(row = 1, column = 1, padx = 5, pady = 5)

right_mid_frame = Frame(window)
right_mid_frame.grid(row = 1, column = 2, padx = 5, pady = 5)

left_bottom_frame = Frame(window)
left_bottom_frame.grid(row = 2, column = 0, padx = 5, pady = 5)

middle_bottom_frame = Frame(window)
middle_bottom_frame.grid(row = 2, column = 1, padx = 5, pady = 5)

right_bottom_frame = Frame(window)
right_bottom_frame.grid(row = 2, column = 2, padx = 5, pady = 5)

buttons = [[None for i in range(9)] for j in range(9)]

for i in range(9):
    for j in range(9):
        if i < 3 and j < 3:
            current_button = Button(left_top_frame,
                                    text = f"{i}{j}",
                                    font = (12),
                                    height = 1,
                                    width = 1)
        elif i < 3 and j < 6:
            current_button = Button(middle_top_frame,
                                    text = f"{i}{j}",
                                    font = (12),
                                    height = 1,
                                    width = 1)
        elif i < 3 and j < 9:
            current_button = Button(right_top_frame,
                                    text = f"{i}{j}",
                                    font = (12),
                                    height = 1,
                                    width = 1)
        elif i < 6 and j < 3:
            current_button = Button(left_mid_frame,
                                    text = f"{i}{j}",
                                    font = (12),
                                    height = 1,
                                    width = 1)
        elif i < 6 and j < 6:
            current_button = Button(middle_mid_frame,
                                    text = f"{i}{j}",
                                    font = (12),
                                    height = 1,
                                    width = 1)
        elif i < 6 and j < 9:
            current_button = Button(right_mid_frame,
                                    text = f"{i}{j}",
                                    font = (12),
                                    height = 1,
                                    width = 1)
        elif i < 9 and j < 3:
            current_button = Button(left_bottom_frame,
                                    text = f"{i}{j}",
                                    font = (12),
                                    height = 1,
                                    width = 1)
        elif i < 9 and j < 6:
            current_button = Button(middle_bottom_frame,
                                    text = f"{i}{j}",
                                    font = (12),
                                    height = 1,
                                    width = 1)
        else:
            current_button = Button(right_bottom_frame,
                                    text = f"{i}{j}",
                                    font = (12),
                                    height = 1,
                                    width = 1)
        current_button.grid(row = i + 1, column = j + 1, sticky = NSEW)
        buttons[i][j] = current_button

window.mainloop()