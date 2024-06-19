from tkinter import *
import tkinter as tk
import sys


windowMenu = Tk()
windowMenu.title("Mail Archiver")
windowMenu.geometry("600x400")
windowMenu["bg"]="mediumorchid2"

#############################################
#############################################
def read():
    windowRead = Tk()
    windowRead.title("Mail Archiver")
    windowRead.geometry("1600x900")
    windowRead["bg"]="navyblue"

    canvasLeft = tk.Canvas(windowRead, width=300, height=850, highlightthickness=0)
    canvasLeft.pack()
    canvasLeft.create_rectangle(0, 0, 300, 850, fill="honeydew4")
    canvasLeft.place(x=0,y=50)

    canvasTop = tk.Canvas(windowRead, width=1600, height=50, highlightthickness=0)
    canvasTop.pack()
    canvasTop.create_rectangle(0, 0, 1600, 50, fill="honeydew3")
    canvasTop.place(x=0,y=0)

    titleMain = Label(windowRead, text="***-- Read mode --***", font=20, background="royalblue1")
    titleMain.place(x=650, y=5, width=300, height=40)

    titleAuthor = Label(windowRead, text="*- Choose author from list -*", background="lavender", font=16)
    titleAuthor.place(x=25, y=85, width=250, height=30)



    listbox_frameLeft = tk.Frame(windowRead)
    listbox_frameLeft.place(x=25, y=150, width=250, height=300)

    listboxLeft = Listbox(listbox_frameLeft,)
    listboxLeft.pack(side="left", fill="both", expand=True)

    scrollbarLeft = Scrollbar(listbox_frameLeft, orient="vertical", command=listboxLeft.yview)
    scrollbarLeft.pack(side="right", fill="y")
    listboxLeft.config(yscrollcommand=scrollbarLeft.set)

    buttonLoadLeft = Button(windowRead, text="Load messages",background="mediumorchid2", activebackground="maroon1", font=18)
    buttonLoadLeft.place(x=50, y=600, width=200, height=40)



    listbox_frameMain = tk.Frame(windowRead)
    listbox_frameMain.place(x=400, y=150, width=1100, height=650)

    listboxMain = Listbox(listbox_frameMain,)
    listboxMain.pack(side="left", fill="both", expand=True)

    scrollbarMain = Scrollbar(listbox_frameMain, orient="vertical", command=listboxMain.yview)
    scrollbarMain.pack(side="right", fill="y")
    listboxMain.config(yscrollcommand=scrollbarMain.set)






##############################################
##############################################
def add():
    windowAdd = Tk()
    windowAdd.title("Mail Archiver")
    windowAdd.geometry("1600x900")
    windowAdd["bg"]="navyblue"

    canvasLeft = tk.Canvas(windowAdd, width=300, height=850, highlightthickness=0)
    canvasLeft.pack()
    canvasLeft.create_rectangle(0, 0, 300, 850, fill="honeydew4")
    canvasLeft.place(x=0,y=50)

    canvasTop = tk.Canvas(windowAdd, width=1600, height=50, highlightthickness=0)
    canvasTop.pack()
    canvasTop.create_rectangle(0, 0, 1600, 50, fill="honeydew3")
    canvasTop.place(x=0,y=0)

    titleMain = Label(windowAdd, text="***-- Add mode --***", font=18, background="salmon1")
    titleMain.place(x=650, y=10, width=300, height=30)

    textInputLeft = Text(windowAdd, background="floralwhite", wrap='word')   # ???
    textInputLeft.place(x=25, y=100, width=250, height=400)

    textInputMain = Text(windowAdd, background="mintcream", wrap='word')
    textInputMain.place(x=400, y=150, width=1100, height=650)




##############################################
def quit():
    sys.exit()

buttonRead = Button(text="Read archive", command=read, background="maroon1", activebackground="palegreen", foreground="white", highlightthickness=0, font=18)
buttonRead.place(x=200, y=80, width=200, height=40)

buttonAdd = Button(text="Add to archive", command=add, background="maroon1", activebackground="palegreen",foreground="white", highlightthickness=0, font=18)
buttonAdd.place(x=200, y=160, width=200, height=40)

buttonQuit = Button(text="Quit", command=quit, background="black", activebackground="plum1", foreground="white", highlightthickness=0)
buttonQuit.place(x=250, y=300, width=100, height=40)



windowMenu.mainloop()