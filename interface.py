from tkinter.simpledialog import askinteger
from tkinter import *
from tkinter import messagebox
top = Tk()

top.geometry("1000x1000")


def onKeyPress(event):
   text.insert('end', 'You started the appliacation')

def show():
   num = askinteger("Input", "Input an Integer")
   print(num)
text = Text(top, background = 'white', foreground = 'white', font=('Comic Sans MS', 12))
text.pack()
top.bind('<KeyPress>', onKeyPress)
B = Button(top, text ="Click", command = show)
B.place(x=50,y=50)

top.mainloop()