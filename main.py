import random
from tkinter import *

canvas = Tk()
canvas.title("THROW THE DICE!")
canvas.geometry("300x500")

def roll():
    value = int(entry1.get())
    rand = random.randint(1, value)
    string = str(rand)
    entry.delete(0, END)
    entry.insert(0, string)
    throw = "You threw: " + str(string) + ' with ' + str(value) + ' side cube'
    throw = Label(canvas, text=throw)
    throw.pack()

lab_var1 = Label(canvas, text="Dice").pack()
entry1 = Entry(canvas, width=3)
entry1.pack()

button = Button(canvas, text="ROLL!", command=roll)
button.pack()

label = Label(canvas, text="")
entry = Entry(canvas, width=3)
entry.pack()

canvas.mainloop()
