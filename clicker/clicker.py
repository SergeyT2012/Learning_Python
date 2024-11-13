from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Clicker")
hamster_image = PhotoImage(file = "D:\\pythonpictures\\Image20241113151112.png")
window.config(bg = "black")
main_text_label = Label(window, text = "Tap the hamster to get tokens!", font = "{Comic Sans MS} 16", fg = "white", bg = "black")
main_text_label.pack()
click_counter_variable = 0
counter_label = Label(window,text = "You clicked "+str(click_counter_variable)+" times", font = "{Comic Sans MS} 16", fg = "white", bg = "black")
counter_label.pack()
def click_counter():
    global click_counter_variable
    if click_counter_variable < 10:
        click_counter_variable = click_counter_variable + 1
        counter_label.config(text = "You clicked "+str(click_counter_variable)+" times")
        if click_counter_variable == 10:
            messagebox.showinfo("Yay! ","You get 100 tokens.")
    elif click_counter_variable >= 10 and click_counter_variable < 50:
        click_counter_variable = click_counter_variable + 2
        counter_label.config(text = "You clicked "+str(click_counter_variable)+" times")
        if click_counter_variable == 50:
            messagebox.showinfo("Yay!","You get 800 tokens!")
    elif click_counter_variable >= 50 and click_counter_variable < 100:
        click_counter_variable = click_counter_variable + 5
        counter_label.config(text = "You clicked "+str(click_counter_variable)+" times")
        if click_counter_variable == 100:
            messagebox.showinfo("Yay!","You get 1000 tokens!")
    elif click_counter_variable >= 100 and click_counter_variable < 200:
        click_counter_variable = click_counter_variable + 10
        counter_label.config(text = "You clicked "+str(click_counter_variable)+" times")
        if click_counter_variable == 200:
            messagebox.showinfo("Yay!","You get 1750 tokens!")
    elif click_counter_variable >= 200 and click_counter_variable < 400:
        click_counter_variable = click_counter_variable + 20
        counter_label.config(text = "You clicked "+str(click_counter_variable)+" times")
        if click_counter_variable == 400:
            messagebox.showinfo("Yay!","You get 2500 tokens!")
    elif click_counter_variable >= 400 and click_counter_variable < 600:
        click_counter_variable = click_counter_variable + 50
        counter_label.config(text = "You clicked "+str(click_counter_variable)+" times")
        if click_counter_variable == 600:
            messagebox.showinfo("Yay!","You get 3000 tokens!")
    elif click_counter_variable >= 600 and click_counter_variable < 1000:
        click_counter_variable = click_counter_variable + 100
        counter_label.config(text = "You clicked "+str(click_counter_variable)+" times")
        if click_counter_variable == 1000:
            messagebox.showinfo("Yay!","You get 5000 tokens!")
    elif click_counter_variable >= 1000 and click_counter_variable < 5000:
        click_counter_variable = click_counter_variable + 500
        counter_label.config(text = "You clicked "+str(click_counter_variable)+" times")
        if click_counter_variable == 5000:
            messagebox.showinfo("Yay!","You get 6000 tokens!")
    elif click_counter_variable >= 5000 and click_counter_variable < 10000:
        click_counter_variable = click_counter_variable + 1000
        counter_label.config(text = "You clicked "+str(click_counter_variable)+" times")
        if click_counter_variable == 10000:
            messagebox.showinfo("Yay!","You get 10000 tokens!")
    elif click_counter_variable >= 10000 and click_counter_variable < 50000:
        click_counter_variable = click_counter_variable + 1000
        counter_label.config(text = "You clicked "+str(click_counter_variable)+" times")
        if click_counter_variable == 50000:
            messagebox.showinfo("Yay!","You get 15000 tokens!")

main_button = Button(window, image = hamster_image, bg = "black", command = click_counter)
main_button.pack()
window.mainloop()