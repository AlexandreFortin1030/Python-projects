from tkinter import *
import tkinter as tk
import sys


windowMenu = Tk()
windowMenu.title("Mail Archiver")
windowMenu.geometry("600x400")
windowMenu["bg"]="dodgerblue"

#############################################
#############################################
def read():
    windowRead = Tk()
    windowRead.title("Mail Archiver")
    windowRead.geometry("1600x900")
    windowRead["bg"]="navyblue"

    canvas = tk.Canvas(windowRead, width=300, height=900, highlightthickness=0)
    canvas.pack()
    canvas.create_rectangle(0, 0, 300, 900, fill="black")
    canvas.place(x=0,y=0)





##############################################
##############################################
def add():
    windowAdd = Tk()
    windowAdd.title("Mail Archiver")
    windowAdd.geometry("1600x900")
    windowAdd["bg"]="navyblue"

    canvas = tk.Canvas(windowAdd, width=300, height=900, highlightthickness=0)
    canvas.pack()
    canvas.create_rectangle(0, 0, 300, 900, fill="black")
    canvas.place(x=0,y=0)





##############################################
def quit():
    sys.exit()

buttonRead = Button(text="Read messages", command=read, background="royalblue", highlightthickness=0)
buttonRead.place(x=200, y=80, width=200, height=40)

buttonAdd = Button(text="Add messages", command=add, background="royalblue", highlightthickness=0)
buttonAdd.place(x=200, y=160, width=200, height=40)

buttonQuit = Button(text="Quit", command=quit, background="navyblue", foreground="white", highlightthickness=0)
buttonQuit.place(x=250, y=300, width=100, height=40)



windowMenu.mainloop()