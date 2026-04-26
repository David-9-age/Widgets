from tkinter import *
from datetime import date

root = Tk()
root.title("Getting Started with Widgets")
root.geometry('400x300')

lbl = Label (text = 'Welcome to my App', fg = 'yellow', bg= 'blue', width=30)

lbl.pack(pady=5)

name_lbl = Label(text= 'Full Name', bg='#3895D3')
name_lbl.pack(pady=5)

name_entry = Entry()
name_entry.pack(pady=5)

def display():
    name = name_entry.get()
    greet = "Hello" + name + "\n"
    message = "Welcome to the application!\nToday's date is: " + str(date.today())

    text_box.delete("1.0", END)

    text_box.insert(END, greet)
    text_box.insert(END, message)

btn = Button(text="Begin", command=display, bg = "#1261A0", fg='white')
btn.pack(pady=10)

text_box = Text(height=5, width=40)
text_box.pack(pady=5)
root.mainloop()