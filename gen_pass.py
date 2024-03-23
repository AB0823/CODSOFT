import random
import string
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

win = Tk()
win.geometry('500x500')

user = Label(win, text="Enter User Name:", font=("Comic Sans MS", 12))
user.grid(row=1, column=1)

user_label = Label(win, text="")
user_label.grid(row=1, column=2)

user_entry = Entry(win)
user_entry.grid(row=1, column=2)

length = Label(win, text="Enter Password Length:", font=("Comic Sans MS", 12))
length.grid(row=3, column=1)

length_label = Label(win, text="")
length_label.grid(row=3, column=2)

length_entry = Entry(win)
length_entry.grid(row=3, column=2)

pawd = Label(win, text="Generated Password:", font=("Comic Sans MS", 12))
pawd.grid(row=5, column=1)

pawd_entry = Entry(win)
pawd_entry.grid(row=5, column=2)

pawd_label = Label(win, text="")
pawd_label.grid(row=5, column=2)

header_frame = Frame(win)
header_frame.grid(row=0, column=2, columnspan=4, sticky="ew")
header_label = Label(
    header_frame,
    text="Password Generator",
    font=("Comic Sans MS", 18, "underline"),
    )
header_label.pack(fill="x", padx=10, pady=10)  

def genpassword():
    password_length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    pawd_label.config(text=password)

def accept_message():
    messagebox.showinfo("Accepted", "Your input has been accepted.")

def reset_fields():
    user_entry.delete(0, END)
    length_entry.delete(0, END)
    pawd_label.config(text="")

win.title('Password Generator')

gb = Button(win, text="Generate Password", command=genpassword)
gb.grid(row=9, column=2)

acc = Button(win, text="Accept", command=accept_message)
acc.grid(row=11, column=2)

res = Button(win, text="Reset", command=reset_fields)
res.grid(row=13, column=2)

win.mainloop()
