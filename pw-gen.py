import random  # Enables random selection of characters
from tkinter import *  # Enables GUI
import string
from tkinter.font import Font  # Enables font selection
import pyperclip  # Enables copy/paste functionality


def generate_password():  # Selects 4 random characters
    password = []  # Creates empty list
    for i in range(4):
        alpha = random.choice(string.ascii_letters)  # Selects random letter
        symbol = random.choice(string.punctuation)  # Selects random symbol
        numbers = random.choice(string.digits)  # Selects random number
        password.append(alpha)  # Adds random character to list
        password.append(symbol)  # Adds random character to list
        password.append(numbers)  # Adds random character to list
    y = "".join(str(x) for x in password)  # Converts list to string
    lbl.config(text=y)  # Displays password
    pyperclip.copy(y)  # Copies password to clipboard


def copy_password():
    password = lbl.cget("text")  # Gets password from label
    pyperclip.copy(password)  # Copies password to clipboard


root = Tk()  # Creates GUI window
root.title("Password Generator")  # Window title
root.geometry("250x200")  # Window dimensions

btn = Button(root, text="Generate Password", command=generate_password)
btn.place(relx=0.5, rely=0.2, anchor=N)  # Places button

btn_copy = Button(root, text="Copy Password", command=copy_password)
btn_copy.place(relx=0.5, rely=0.4, anchor=N)

myFont = Font(family="Courier New", size=14)  # Creates font
lbl = Label(root, font=myFont)  # Creates label
lbl.place(relx=0.5, rely=0.6, anchor=CENTER)  # Places label

root.mainloop()  # Runs GUI
