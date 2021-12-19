from tkinter import *
from predefineValues import screenDisplay

root = Tk()

def myClick():
    Label1 = Label(root,text="Clicked the button")
    Label1.grid(row=2,column=1)


myLable = Label(root, text="Hello World!",bg=None) 
myButton = Button(root, text="CLICK ME!",bg=None, command=myClick).grid(row=1,column=1)

myLable.grid(row=0, column=0)

screenDisplay(root)  