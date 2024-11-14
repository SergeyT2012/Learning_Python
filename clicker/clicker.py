from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Clicker")
hamster_image = PhotoImage(file = "D:\\pythonpictures\\Image20241113151112.png")
window.config(bg = "black")
main_text_label = Label(window, text = "Tap the hamster to get tokens!", font = "{Comic Sans MS} 16", fg = "white", bg = "black")
main_text_label.pack()
click_counter = 0
current_click = 1
counter_label = Label(window,text = "You clicked "+str(click_counter)+" times", font = "{Comic Sans MS} 16", fg = "white", bg = "black")
counter_label.pack()
def on_click():
    global click_counter, current_click
    click_counter = click_counter + current_click
    if click_counter % 10 == 0 and click_counter % 3 == 0:
        current_click = current_click * 5
    counter_label.config(text="You clicked " + str(click_counter) + " times")


main_button = Button(window, image = hamster_image, bg = "black", command = on_click)
main_button.pack()
window.mainloop()