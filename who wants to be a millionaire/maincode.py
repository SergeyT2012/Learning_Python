from tkinter import *
window = Tk()
window.title("Who wants to be a millionaire!?")
maintext_1 = Label(window, text = "Become a millionaire!", font = "{Comic Sans MS} 16")
maintext_1.grid(columnspan = 4)
maintext_2 = Label(window, text = "You have 0 dollars", font = "{Comic Sans MS} 16")
maintext_2.grid(columnspan = 4)
question_label = Label(window, text = "What is the main city of Mexico?", font = "{Comic Sans MS} 16")
question_label.grid(columnspan = 4)
tries = 2
def wrong():
    global tries
    tries = tries - 1
    if tries == 0:
        exit()
    window.config(bg = "red")
def win():
    window.config(bg = "yellow")
def win2():
    window.config(bg = "pink")
def win3():
    window.config(bg = "green")
def win4():
    window.config(bg = "red")
def right3():
    window.config(bg = "green")
    maintext_2.config(text = "You have a million dollars")
    question_label.config(text = "You won!")
    first_question_button_A.config(text ="Co", command = win)
    first_question_button_B.config(text="ng", command = win2)
    first_question_button_C.config(text="ra", command = win3)
    first_question_button_D.config(text="ts!", command = win4)
def right2():
    window.config(bg = "green")
    maintext_2.config(text = "You have 100000 dollars")
    question_label.config(text = "What is a banana?")
    first_question_button_A.config(text ="A) Fruit", command = wrong)
    first_question_button_B.config(text="B) Berry", command = right3)
    first_question_button_C.config(text="C) Vegetable", command = wrong)
    first_question_button_D.config(text="D) Soup", command = wrong)
def right():
    window.config(bg = "green")
    maintext_2.config(text = "You have 1000 dollars")
    question_label.config(text = "What is 2+2*2?")
    first_question_button_A.config(text ="A) 4", command = wrong)
    first_question_button_B.config(text="B) 6", command = right2)
    first_question_button_C.config(text="C) 22", command = wrong)
    first_question_button_D.config(text="D) 8", command = wrong)

first_question_button_A = Button(window, text = "A) Kyiv", font = "{Comic Sans MS} 16", width = 10, command = wrong)
first_question_button_A.grid(row = 3, column = 0)
first_question_button_B = Button(window, text = "B) Berlin", font = "{Comic Sans MS} 16", width = 10, command = wrong)
first_question_button_B.grid(row = 3, column = 1)
first_question_button_C = Button(window, text = "C)New Mexico", font = "{Comic Sans MS} 16", width = 10, command = right)
first_question_button_C.grid(row = 3, column = 2)
first_question_button_D = Button(window, text = "D) London", font = "{Comic Sans MS} 16", width = 10, command = wrong)
first_question_button_D.grid(row = 3, column = 3)
window.mainloop()