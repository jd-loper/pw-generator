import random
from tkinter import *
import string
from tkinter.font import Font
import pyperclip  # Enables copy/paste functionality


def generate_password():  # Selects 4 random characters
    password = []
    for i in range(4):
        alpha = random.choice(string.ascii_letters)
        symbol = random.choice(string.punctuation)
        numbers = random.choice(string.digits)
        password.append(alpha)
        password.append(symbol)
        password.append(numbers)
    y = "".join(str(x)for x in password)
    lbl.config(text=y)
    pyperclip.copy(y)


def copy_password():
    password = lbl.cget("text")
    pyperclip.copy(password)


root = Tk()  # Creates GUI window
root.geometry("250x200")  # Window dimensions

btn = Button(root, text="Generate Password", command=generate_password)
btn.place(relx=0.5, rely=0.2, anchor=N)

btn_copy = Button(root, text="Copy Password", command=copy_password)
btn_copy.place(relx=0.5, rely=0.4, anchor=N)

myFont = Font(family="Courier New", size=14)
lbl = Label(root, font=myFont)
lbl.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()
